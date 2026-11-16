"""H6: daily/hourly index-update harness (test-then-train replay).

Corrected CIC-IDS2017. Training block = Mon-Wed (24 capture hours); replay = Thu+Fri in 1-hour blocks.
Classes: 0 benign, 1..8 attack families (merged), prediction column 9 = "unknown" (flagged, no known class).
Index = benign sample (<=100k) + attack exemplars (<=2000 per class, k-center). kNN-raw, k=10, one fixed tau
(99th pct of held-out benign scores at the start, no audits).
Per block:  score -> flagged flows -> k-means (B clusters) -> oracle labels the B representatives -> update.
Approaches: A0 frozen | A1 append-only with caps | A2 = A1 + retire exemplars with no hit for 3 blocks (20 anchors/class kept)
Benign rule: B1 random sample of the confirmed/assumed-benign pool | B2 recency-weighted (half-life 6 blocks)
Outputs per config: confusion_total.csv (true x predicted), conf_by_block.npy, blocks.csv.
"""
from __future__ import annotations
import argparse, json, sys, time
from pathlib import Path
import numpy as np, pandas as pd
import copy
import torch
from sklearn.cluster import MiniBatchKMeans

sys.path.insert(0, str(Path(__file__).parent))
from data_improved import load_improved  # noqa: E402
from h1_unknown_separability import Prep, knn  # noqa: E402
from h3_benign_coverage import kcenter  # noqa: E402
from h5_benign_gate import train_ae  # noqa: E402

FAMS = ["bruteforce", "dos", "heartbleed", "web", "infiltration", "portscan", "bot", "ddos"]
CID = {"benign": 0, **{f: i + 1 for i, f in enumerate(FAMS)}}
NAMES = ["benign"] + FAMS
UNK = 9
COLS = NAMES + ["unknown"]


@torch.no_grad()
def recon_det(m, X):
    """deterministic reconstruction error (decode the latent mean) of an AE/VAE."""
    out = []
    for i in range(0, len(X), 16384):
        x = torch.from_numpy(np.ascontiguousarray(X[i:i + 16384], dtype=np.float32))
        out.append(((m.dec(m.mu(m.enc(x))) - x) ** 2).mean(1).numpy())
    return np.concatenate(out)


def finetune_ae(m, X, epochs, seed, lr=5e-4, bs=1024):
    torch.manual_seed(seed); m.train(); opt = torch.optim.Adam(m.parameters(), lr)
    Xt = torch.from_numpy(np.ascontiguousarray(X, dtype=np.float32))
    for _ in range(epochs):
        perm = torch.randperm(len(Xt))
        for i in range(0, len(Xt), bs):
            x = Xt[perm[i:i + bs]]; rec, mu, lv = m(x); loss = ((rec - x) ** 2).mean()
            if m.vae:
                loss = loss + 0.1 * (-0.5 * (1 + lv - mu ** 2 - lv.exp()).sum(1).mean()) / x.shape[1]
            opt.zero_grad(); loss.backward(); opt.step()
    m.eval()


def make_protos(X, c, pmax, rmin, seed):
    """sub-prototypes of one class: k-means centroids with a radius (95th pct member distance, floor rmin) and a count."""
    n = len(X)
    K = n if n <= 10 else min(pmax, max(1, n // 10))
    if K == n:
        return X.astype(np.float32), np.full(K, c), np.ones(K), np.full(K, rmin)
    km = MiniBatchKMeans(n_clusters=K, n_init=1, random_state=seed, batch_size=4096).fit(X)
    cent, lab = km.cluster_centers_.astype(np.float32), km.labels_
    dist = np.linalg.norm(X - cent[lab], axis=1)
    cnt = np.bincount(lab, minlength=K); ok = cnt > 0
    rad = np.array([max(rmin, float(np.quantile(dist[lab == k], 0.95))) if cnt[k] else rmin for k in range(K)])
    return cent[ok], np.full(int(ok.sum()), c), cnt[ok].astype(float), rad[ok]


def score(Xi, yi, Q, k=10, with_d=False):
    d, i = knn(Xi, Q, k)
    w = 1.0 / (d + 1e-3)
    votes = np.zeros((len(Q), 9))
    np.add.at(votes, (np.repeat(np.arange(len(Q)), k), yi[i].ravel()), w.ravel())
    return (votes.argmax(1), d.mean(1), i, d) if with_d else (votes.argmax(1), d.mean(1), i)


def run_config(cfg, init, blocks, tau, a, rng_seed, dbg=None):
    """cfg = (approach, benign_rule, B). Returns confusion by block and block table."""
    approach, brule, B = cfg
    is3 = approach in ("A3", "A3b")   # A3 = kNN vote + radius check; A3b = nearest-prototype-in-radius rule
    rng = np.random.default_rng(rng_seed)
    Xp, added = init["Xpool"].copy(), np.full(len(init["Xpool"]), -1.0)
    Xa, ya = init["Xa"].copy(), init["ya"].copy()
    last_hit = np.full(len(Xa), -1.0); anchor = np.zeros(len(Xa), bool)
    if is3:   # attack side = sub-prototypes (centroid, class, count, radius)
        Pp = init["P"]; Xa, ya, Pn, Prad = Pp["Xc"].copy(), Pp["yc"].copy(), Pp["n"].copy(), Pp["rad"].copy()
        last_hit = np.full(len(Xa), -1.0)

    pcl = init["pool_cl"].copy() if brule == "B3" else None
    vae = copy.deepcopy(init["vae"]) if brule == "B4" else None

    def add_pool(X, t):
        nonlocal Xp, added, pcl
        if len(X) == 0:
            return
        Xp = np.concatenate([Xp, X]); added = np.concatenate([added, np.full(len(X), float(t))])
        if brule == "B3":   # assign new flows to the nearest of the pool's k-means clusters
            pcl = np.concatenate([pcl, knn(init["centers"], np.ascontiguousarray(X, dtype=np.float32), 1)[1][:, 0]])

    def sample_benign(t):
        n = min(a.benign_index, len(Xp))
        if brule in ("B1", "B4") or t < 0:
            return Xp[rng.choice(len(Xp), n, replace=False)]
        if brule == "B3":   # density-aware: flatten density, cluster weight ~ size^0.5, so each flow weighs size^-0.5
            w = np.bincount(pcl, minlength=len(init["centers"]))[pcl].astype(float) ** -0.5
            keys = np.log(w) + rng.gumbel(size=len(w))
            return Xp[np.argpartition(-keys, n - 1)[:n]]
        w = 0.5 ** ((t - added) / a.half_life)
        keys = np.log(w) + rng.gumbel(size=len(w))
        return Xp[np.argpartition(-keys, n - 1)[:n]]

    Xb = init["Xb"].copy()
    confs, pconfs, rows = [], [], []
    for t, (name, Xq, yq) in enumerate(blocks):
        Xi = np.concatenate([Xb, Xa]); yi = np.concatenate([np.zeros(len(Xb), int), ya]); nb = len(Xb)
        def label_b4(Q_):   # layer 1: AE/VAE gate; layer 2: attack index names what the gate flags
            lab = np.zeros(len(Q_), int); ia = np.where(recon_det(vae, Q_) > tau_g)[0]
            if len(ia):
                if approach == "A3b":
                    dp, ip = knn(np.ascontiguousarray(Xa, dtype=np.float32), np.ascontiguousarray(Q_[ia], dtype=np.float32), 1)
                    lab[ia] = np.where(dp[:, 0] <= Prad[ip[:, 0]], ya[ip[:, 0]], UNK)
                else:   # A1: vote among attack exemplars; name only if the nearest same-class exemplar is within tau_name
                    pr_, _, nb_, dd_ = score(Xa, ya, Q_[ia], with_d=True)
                    j = (ya[nb_] == pr_[:, None]).argmax(1)
                    lab[ia] = np.where(dd_[np.arange(len(ia)), j] <= init["tau_name"], pr_, UNK)
            return lab

        def label_of(pred, nov, nbr, d, Q_):
            lab = np.where(pred != 0, pred, np.where(nov > tau, UNK, 0))
            if approach == "A3b":   # a prototype claims a flow if it is within its radius and nearer than the nearest benign entry
                dp, ip = knn(np.ascontiguousarray(Xa, dtype=np.float32), np.ascontiguousarray(Q_, dtype=np.float32), 1)
                dp, ip = dp[:, 0], ip[:, 0]
                isb = nbr < nb
                db = np.where(isb.any(1), d[np.arange(len(d)), isb.argmax(1)], d[:, -1])
                claim = (dp <= Prad[ip]) & (dp < db)
                return np.where(claim, ya[ip], np.where(nov > tau, UNK, 0))
            if approach == "A3":   # name a class only if the nearest same-class prototype is within its radius
                c = np.where(pred != 0)[0]
                if len(c):
                    nn_ = nbr[c]; isc = (nn_ >= nb) & (yi[nn_] == pred[c][:, None])
                    j = isc.argmax(1); pid = nn_[np.arange(len(c)), j] - nb
                    ok = isc.any(1) & (d[c, j] <= Prad[np.clip(pid, 0, len(Prad) - 1)])
                    lab[c[~ok]] = UNK
            return lab
        if brule == "B4":
            tau_g = float(np.quantile(recon_det(vae, init["Xcal"]), 0.99))   # re-calibrated on the fixed held-out benign slice
            lab = label_b4(Xq); plab = label_b4(init["Xpr"]); nbr = None
        else:
            pred, nov, nbr, dq = score(Xi, yi, Xq, with_d=True)
            lab = label_of(pred, nov, nbr, dq, Xq)
            pp, pn, pnbr, pd_ = score(Xi, yi, init["Xpr"], with_d=True)   # probe: known attacks held out in time, same index
            plab = label_of(pp, pn, pnbr, pd_, init["Xpr"])
        alarm = lab != 0
        conf = np.zeros((9, 10), int); np.add.at(conf, (yq, lab), 1); confs.append(conf)
        pc = np.zeros((9, 10), int); np.add.at(pc, (init["ypr"], plab), 1); pconfs.append(pc)
        ben = yq == 0
        row = dict(t=t, block=name, n=len(yq), n_benign=int(ben.sum()), fpr=float(alarm[ben].mean()) if ben.any() else np.nan,
                   n_alarm=int(alarm.sum()), tau=float(tau_g if brule == "B4" else tau), labels_used=0, contam=0,
                   benign_repr=int(sum(p_.numel() for p_ in vae.parameters())) if brule == "B4" else int(Xb.size))
        # hits (for A2)
        m = lab > 0
        if approach == "A2" and m.any():
            nn_ = nbr[m]; sel = (nn_ >= nb) & (yi[nn_] == lab[m][:, None])
            last_hit[np.unique(nn_[sel]) - nb] = t
        if approach != "A0":
            fl = np.where(alarm)[0]
            if len(fl):
                sub = fl if len(fl) <= 50_000 else rng.choice(fl, 50_000, replace=False)
                nc = min(B, len(sub))
                km = MiniBatchKMeans(n_clusters=nc, n_init=1, random_state=rng_seed, batch_size=4096).fit(Xq[sub])
                dist = np.linalg.norm(Xq[sub] - km.cluster_centers_[km.labels_], axis=1)
                order = np.lexsort((dist, km.labels_)); first = np.r_[True, km.labels_[order][1:] != km.labels_[order][:-1]]
                reps = sub[order[first]]
                row["labels_used"] = len(reps)
                ry = yq[reps]
                if dbg is not None:   # diagnostics only; does not change results
                    cl = np.full(len(Xq), -1); cl[sub] = km.labels_
                    inf = np.where((yq == 5) & (cl >= 0))[0]
                    cinf = sorted(set(cl[inf]))
                    dbg.append(dict(block=name, n_flagged=len(fl), clustered=len(sub), n_clusters=nc,
                                    rep_labels=np.bincount(ry, minlength=9).tolist(), n_infil=int((yq == 5).sum()), infil_flagged=len(inf),
                                    infil_clusters=len(cinf),
                                    cluster_size=[int((cl == c).sum()) for c in cinf],
                                    cluster_infil_share=[round(float((yq[cl == c] == 5).mean()), 4) for c in cinf],
                                    rep_label_of_cluster=[int(yq[dict(zip(np.unique(km.labels_), reps))[c]]) for c in cinf]))
                add_pool(Xq[reps[ry == 0]], t)
                if is3:
                    for x, c in zip(Xq[reps[ry > 0]], ry[ry > 0]):
                        ids = np.where(ya == c)[0]
                        if len(ids):
                            dd = np.linalg.norm(Xa[ids] - x, axis=1); j = int(dd.argmin())
                            if dd[j] <= Prad[ids[j]]:   # merge into the nearest sub-prototype of this class
                                i = ids[j]; Pn[i] += 1; Xa[i] += (x - Xa[i]) / Pn[i]; last_hit[i] = t; continue
                        Xa = np.vstack([Xa, x[None]]); ya = np.append(ya, c); Pn = np.append(Pn, 1.0)
                        Prad = np.append(Prad, a.rmin); last_hit = np.append(last_hit, float(t))
                elif (ry > 0).any():
                    Xa = np.concatenate([Xa, Xq[reps[ry > 0]]]); ya = np.concatenate([ya, ry[ry > 0]])
                    last_hit = np.concatenate([last_hit, np.full((ry > 0).sum(), t)]); anchor = np.concatenate([anchor, np.zeros((ry > 0).sum(), bool)])
            un = np.where(lab == 0)[0]
            if len(un):
                s = rng.choice(un, min(a.assumed_benign, len(un)), replace=False)
                row["contam"] = int((yq[s] > 0).sum())
                add_pool(Xq[s], t)
            if is3:   # cap: merge the two closest sub-prototypes of a class until it fits (never delete a variant)
                for c in range(1, 9):
                    while (ya == c).sum() > a.pmax:
                        ids = np.where(ya == c)[0]; Dm = np.linalg.norm(Xa[ids][:, None] - Xa[ids][None], axis=2)
                        np.fill_diagonal(Dm, np.inf); u, v = np.unravel_index(Dm.argmin(), Dm.shape); i, j = ids[u], ids[v]
                        tot = Pn[i] + Pn[j]; Xa[i] = (Pn[i] * Xa[i] + Pn[j] * Xa[j]) / tot
                        Prad[i] = max(Prad[i], Prad[j]) + Dm[u, v] / 2; Pn[i] = tot; last_hit[i] = max(last_hit[i], last_hit[j])
                        k_ = np.ones(len(Xa), bool); k_[j] = False; Xa, ya, Pn, Prad, last_hit = Xa[k_], ya[k_], Pn[k_], Prad[k_], last_hit[k_]
                Xb = sample_benign(t)
                if brule == "B4":
                    finetune_ae(vae, Xb, 1, rng_seed)
                for c in range(1, 9):
                    row[f"idx_{NAMES[c]}"] = int((ya == c).sum())
                row["pool"] = len(Xp); rows.append(row); continue
            # per-class housekeeping
            keep = np.ones(len(Xa), bool)
            for c in range(1, 9):
                ids = np.where(ya == c)[0]
                if len(ids) == 0:
                    continue
                if approach == "A2":
                    anchor[ids] = False
                    anchor[ids[kcenter(Xa[ids], min(a.anchors, len(ids)), rng_seed)]] = True
                    old = (t - last_hit[ids] > a.max_age) & ~anchor[ids]
                    keep[ids[old]] = False
                    ids = ids[~old]
                if len(ids) > a.cap:
                    chosen = ids[kcenter(Xa[ids], a.cap, rng_seed)]
                    drop = np.setdiff1d(ids, chosen); keep[drop] = False
            Xa, ya, last_hit, anchor = Xa[keep], ya[keep], last_hit[keep], anchor[keep]
            Xb = sample_benign(t)
            if brule == "B4":
                finetune_ae(vae, Xb, 1, rng_seed)
        for c in range(1, 9):
            row[f"idx_{NAMES[c]}"] = int((ya == c).sum())
        row["pool"] = len(Xp)
        rows.append(row)
    return np.stack(confs), np.stack(pconfs), pd.DataFrame(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv_dir", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--budgets", default="100,500")
    ap.add_argument("--approaches", default="A0,A1,A2")
    ap.add_argument("--brules", default="B1,B2")
    ap.add_argument("--cap", type=int, default=2000)
    ap.add_argument("--benign_index", type=int, default=100_000)
    ap.add_argument("--assumed_benign", type=int, default=3000)
    ap.add_argument("--half_life", type=float, default=6.0)
    ap.add_argument("--max_age", type=int, default=3)
    ap.add_argument("--anchors", type=int, default=20)
    ap.add_argument("--pool_clusters", type=int, default=2000, help="B3: k-means clusters over the benign pool")
    ap.add_argument("--suffix", default="", help="appended to the config tag of non-A0 runs")
    ap.add_argument("--pmax", type=int, default=100, help="A3: max sub-prototypes per class")
    ap.add_argument("--rmin_frac", type=float, default=0.5, help="A3: minimum prototype radius = rmin_frac * tau")
    ap.add_argument("--max_blocks", type=int, default=0)
    a = ap.parse_args(); a.out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(a.seed)

    df, feats = load_improved(a.csv_dir)
    df["cid"] = df.family.map(CID)
    tr = df[df.file_idx <= 2]; rp = df[df.file_idx >= 3]
    ben = tr[tr.cid == 0].sort_values("ts")
    cut = int(0.85 * len(ben)); cand, calset = ben.iloc[:cut], ben.iloc[cut:]
    prep = Prep().fit(cand[feats].to_numpy(np.float64))
    P = lambda d: prep(d[feats].to_numpy(np.float64))  # noqa: E731
    Xpool = P(cand); Xcal = P(calset.sample(n=min(30_000, len(calset)), random_state=a.seed))
    # known attacks (Mon-Wed): first 60% in time -> training exemplars, last 40% -> probe set scored every block
    ka = tr[tr.cid > 0].sort_values("ts").copy()
    ka["cpos"] = ka.groupby("cid").cumcount() / ka.groupby("cid")["cid"].transform("size")
    probe = pd.concat([g.sample(n=min(3000, len(g)), random_state=a.seed) for _, g in ka[ka.cpos >= 0.6].groupby("cid")])
    Xpr, ypr = P(probe), probe.cid.to_numpy()
    Xa, ya, train_att = [], [], {}
    for c in sorted(set(ka.cid)):
        X = P(ka[(ka.cid == c) & (ka.cpos < 0.6)]); train_att[c] = X
        if len(X) > a.cap:
            X = X[kcenter(X, a.cap, a.seed)]
        Xa.append(X); ya.append(np.full(len(X), c))
    Xa, ya = np.concatenate(Xa), np.concatenate(ya)
    Xb = Xpool[rng.choice(len(Xpool), min(a.benign_index, len(Xpool)), replace=False)]
    init = dict(Xpool=Xpool, Xa=Xa, ya=ya, Xb=Xb, Xpr=Xpr, ypr=ypr)
    if "B3" in a.brules.split(","):
        sub_ = Xpool[rng.choice(len(Xpool), 150_000, replace=False)]
        kmp = MiniBatchKMeans(n_clusters=a.pool_clusters, n_init=1, random_state=a.seed, batch_size=8192).fit(sub_)
        init["centers"] = kmp.cluster_centers_.astype(np.float32)
        init["pool_cl"] = np.concatenate([knn(init["centers"], np.ascontiguousarray(Xpool[i:i + 100_000]), 1)[1][:, 0] for i in range(0, len(Xpool), 100_000)])
    if "B4" in a.brules.split(","):
        init["vae"] = train_ae(Xpool[rng.choice(len(Xpool), 200_000, replace=False)], True, 20, a.seed); init["Xcal"] = Xcal
        print("B4: initial VAE trained", flush=True)
    p0, n0, _ = score(np.concatenate([Xb, Xa]), np.r_[np.zeros(len(Xb), int), ya], Xcal)
    tau = float(np.quantile(n0, 0.99)); a.rmin = a.rmin_frac * tau
    pr = [make_protos(train_att[c], c, a.pmax, a.rmin, a.seed) for c in sorted(train_att)]
    init["P"] = dict(Xc=np.concatenate([p[0] for p in pr]), yc=np.concatenate([p[1] for p in pr]),
                     n=np.concatenate([p[2] for p in pr]), rad=np.concatenate([p[3] for p in pr]))
    dsame = [np.linalg.norm(Xpr[ypr == c][:, None] - train_att[c][rng.choice(len(train_att[c]), min(2000, len(train_att[c])), replace=False)][None], axis=2).min(1) for c in sorted(train_att) if (ypr == c).any()]
    init["tau_name"] = float(np.quantile(np.concatenate(dsame), 0.95))
    print(f"tau_name (A1+B4 naming bound) = {init['tau_name']:.2f}", flush=True)
    print(f"A3 start: {len(init['P']['yc'])} sub-prototypes, radius median {np.median(init['P']['rad']):.2f} (rmin {a.rmin:.2f})", flush=True)
    print(f"known at start: { {NAMES[c]: int((ya == c).sum()) for c in sorted(set(ya))} }  tau={tau:.3f}  "
          f"cal alarm rate (vote or novelty) = {((p0 != 0) | (n0 > tau)).mean():.3f}", flush=True)

    rp = rp.assign(blk=rp.file_idx.astype(str) + "-" + rp.ts.dt.hour.astype(str).str.zfill(2)).sort_values("ts")
    blocks = []
    for name, g in rp.groupby("blk", sort=True):
        blocks.append((name, P(g), g.cid.to_numpy()))
    if a.max_blocks:
        blocks = blocks[:a.max_blocks]
    print(f"{len(blocks)} replay blocks: " + ", ".join(f"{n}({len(y):,})" for n, _, y in blocks), flush=True)

    cfgs = [("A0", "B1", 0)]
    cfgs += [(ap_, br, B) for ap_ in a.approaches.split(",") if ap_ != "A0" for br in a.brules.split(",") for B in map(int, a.budgets.split(","))]
    for cfg in cfgs:
        t0 = time.time(); tag = f"{cfg[0]}_{cfg[1]}_B{cfg[2]}{a.suffix}" if cfg[0] != "A0" else "A0"
        conf, pconf, tab = run_config(cfg, init, blocks, tau, a, a.seed)
        d = a.out / tag; d.mkdir(exist_ok=True); json.dump({"seconds": time.time() - t0}, open(d / "runtime.json", "w"))
        np.save(d / "conf_by_block.npy", conf); np.save(d / "probe_conf_by_block.npy", pconf); tab.to_csv(d / "blocks.csv", index=False)
        pd.DataFrame(conf.sum(0), index=NAMES, columns=COLS).to_csv(d / "confusion_total.csv")
        pd.DataFrame(pconf[0], index=NAMES, columns=COLS).to_csv(d / "probe_confusion_first.csv")
        pd.DataFrame(pconf[-1], index=NAMES, columns=COLS).to_csv(d / "probe_confusion_last.csv")
        tot = conf.sum(0); b = tot[0]
        f = lambda m, c: "  -  " if m[c].sum() == 0 else f"{1 - m[c, 0] / m[c].sum():.2f}/{m[c, c] / m[c].sum():.2f}"  # noqa: E731
        print(f"{tag:14s} FPR={1 - b[0] / b.sum():.4f} replay detect/named: " + " ".join(f"{NAMES[c]}:{f(tot, c)}" for c in range(4, 9)) +
              " | probe first->last: " + " ".join(f"{NAMES[c]}:{f(pconf[0], c)}->{f(pconf[-1], c)}" for c in (1, 2, 3)) + f"  ({time.time() - t0:.0f}s)", flush=True)
    json.dump(vars(a) | {"csv_dir": str(a.csv_dir), "out": str(a.out), "tau": tau}, open(a.out / "args.json", "w"), indent=1)


if __name__ == "__main__":
    main()
