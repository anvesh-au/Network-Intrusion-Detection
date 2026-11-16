"""H5: which layer-1 benign gate separates attacks best at ~1% benign false alarms?

Same split as H3 (corrected CIC-IDS2017): pool = Mon+Tue benign, first 80% = training, last 20% = calibration;
test = Wed/Thu/Fri benign (per day) + attack flows of every family (Tue-Fri, <=3000 per family).
Gates (score high = abnormal; tau = 99th pct of calibration benign scores):
  knn20k / knnfull : mean distance to 10 nearest benign index entries (H3 baseline)
  ae / vae         : reconstruction error of an MLP (benign only)
  xgb              : 1 - P(benign), benign-vs-rest; leave-one-family-out (trained on the OTHER families' attacks)
Metrics: benign FPR per day, attack TPR per family, mean TPR, mean AUROC (family vs Wed-Fri benign).
"""
from __future__ import annotations
import argparse, json, sys, time
from pathlib import Path
import numpy as np, pandas as pd, torch, torch.nn as nn
import xgboost as xgb
from sklearn.metrics import roc_auc_score

sys.path.insert(0, str(Path(__file__).parent))
from data_improved import load_improved  # noqa: E402
from h1_unknown_separability import Prep, knn  # noqa: E402


class AE(nn.Module):
    def __init__(self, d, z=16, vae=False):
        super().__init__()
        self.vae = vae
        self.enc = nn.Sequential(nn.Linear(d, 128), nn.ReLU(), nn.Linear(128, 64), nn.ReLU())
        self.mu = nn.Linear(64, z); self.lv = nn.Linear(64, z) if vae else None
        self.dec = nn.Sequential(nn.Linear(z, 64), nn.ReLU(), nn.Linear(64, 128), nn.ReLU(), nn.Linear(128, d))

    def forward(self, x):
        h = self.enc(x); mu = self.mu(h)
        if not self.vae:
            return self.dec(mu), mu, None
        lv = self.lv(h).clamp(-8, 4)
        return self.dec(mu + torch.randn_like(mu) * (0.5 * lv).exp()), mu, lv


def train_ae(X, vae, epochs, seed, bs=1024, beta=0.1):
    torch.manual_seed(seed)
    m = AE(X.shape[1], vae=vae); opt = torch.optim.Adam(m.parameters(), 1e-3)
    Xt = torch.from_numpy(X); n = len(Xt)
    for ep in range(epochs):
        perm = torch.randperm(n); tot = 0
        for i in range(0, n, bs):
            x = Xt[perm[i:i + bs]]
            rec, mu, lv = m(x)
            loss = ((rec - x) ** 2).mean()
            if vae:
                loss = loss + beta * (-0.5 * (1 + lv - mu ** 2 - lv.exp()).sum(1).mean()) / x.shape[1]
            opt.zero_grad(); loss.backward(); opt.step(); tot += loss.item() * len(x)
        if ep % 5 == 0 or ep == epochs - 1:
            print(f"    {'vae' if vae else 'ae'} epoch {ep}: loss {tot / n:.4f}", flush=True)
    return m.eval()


@torch.no_grad()
def recon_err(m, X):
    out = []
    for i in range(0, len(X), 8192):
        x = torch.from_numpy(X[i:i + 8192]); rec, _, _ = m(x)
        out.append(((rec - x) ** 2).mean(1).numpy())
    return np.concatenate(out)


def knn_score(index, Q, k=10):
    return knn(index, Q, k)[0].mean(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv_dir", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--epochs", type=int, default=20)
    ap.add_argument("--cand", type=int, default=200_000)
    ap.add_argument("--xgb_benign", type=int, default=150_000)
    ap.add_argument("--attack_cap", type=int, default=10_000)
    ap.add_argument("--test_cap", type=int, default=50_000)
    a = ap.parse_args(); a.out.mkdir(parents=True, exist_ok=True)
    torch.set_num_threads(8)
    rng = np.random.default_rng(a.seed)

    df, feats = load_improved(a.csv_dir)
    ben = df[df.family == "benign"]
    pool = ben[ben.file_idx <= 1].sort_values(["file_idx", "pos"])
    cut = int(0.8 * len(pool)); tr_df, cal_df = pool.iloc[:cut], pool.iloc[cut:]
    prep = Prep().fit(pool[feats].to_numpy(np.float64))
    P = lambda d: prep(d[feats].to_numpy(np.float64))  # noqa: E731
    Xtr = P(tr_df); cal = P(cal_df.sample(n=min(30_000, len(cal_df)), random_state=a.seed))
    days = {n: P(ben[ben.file_idx == fi].sample(n=min(a.test_cap, (ben.file_idx == fi).sum()), random_state=a.seed))
            for fi, n in ((2, "wed"), (3, "thu"), (4, "fri"))}
    att = df[(df.family != "benign") & (df.file_idx >= 1)]
    att = pd.concat([g.sample(n=min(3000, len(g)), random_state=a.seed) for _, g in att.groupby("family")])
    fams = sorted(att.family.unique()); att_fam = att.family.to_numpy(); Xatt = P(att)
    print(f"train={len(Xtr):,} cal={len(cal):,} attacks={dict(zip(*np.unique(att_fam, return_counts=True)))}", flush=True)

    # per-gate scores: dict name -> (cal, {day: scores}, attack scores)  [xgb handled per family]
    scores = {}
    def add(name, f):
        scores[name] = (f(cal), {d: f(X) for d, X in days.items()}, f(Xatt))
    t0 = time.time()
    sub = Xtr[rng.choice(len(Xtr), min(a.cand, len(Xtr)), replace=False)]
    idx20 = sub[rng.choice(len(sub), 20_000, replace=False)]
    add("knn20k", lambda X: knn_score(idx20, X)); print(f"knn20k {time.time() - t0:.0f}s", flush=True)
    add("knnfull", lambda X: knn_score(Xtr, X)); print(f"knnfull {time.time() - t0:.0f}s", flush=True)
    for name, vae in (("ae", False), ("vae", True)):
        m = train_ae(Xtr, vae, a.epochs, a.seed); add(name, lambda X, m=m: recon_err(m, X))
        print(f"{name} {time.time() - t0:.0f}s", flush=True)

    rows = []
    def record(name, cal_s, day_s, att_s_by_fam):
        tau = np.quantile(cal_s, 0.99)
        r = dict(seed=a.seed, gate=name, tau=float(tau))
        for d, s in day_s.items():
            r[f"fpr_{d}"] = float((s > tau).mean())
        benign_all = np.concatenate(list(day_s.values()))
        for f in fams:
            s = att_s_by_fam[f]
            r[f"tpr_{f}"] = float((s > tau).mean())
            r[f"auc_{f}"] = float(roc_auc_score(np.r_[np.zeros(len(benign_all)), np.ones(len(s))], np.r_[benign_all, s]))
        r["tpr_mean"] = float(np.mean([r[f"tpr_{f}"] for f in fams])); r["auc_mean"] = float(np.mean([r[f"auc_{f}"] for f in fams]))
        rows.append(r)
        print(f"  {name:8s} tau={tau:.3f} fpr={np.mean([r[f'fpr_{d}'] for d in days]):.3f} tpr_mean={r['tpr_mean']:.3f} auc_mean={r['auc_mean']:.3f}", flush=True)

    for name, (c, ds, at) in scores.items():
        record(name, c, ds, {f: at[att_fam == f] for f in fams})

    # XGBoost benign-vs-rest, leave-one-family-out
    known = df[(df.family != "benign")]
    known["cpos"] = known.groupby("Label").cumcount() / known.groupby("Label")["Label"].transform("size")
    Xb = Xtr[rng.choice(len(Xtr), min(a.xgb_benign, len(Xtr)), replace=False)]
    cal_s, day_s, att_s = [], None, {}
    for f in fams:
        ktr = known[(known.family != f) & (known.cpos < 0.6)]
        ktr = pd.concat([g.sample(n=min(a.attack_cap, len(g)), random_state=a.seed) for _, g in ktr.groupby("Label")])
        Xk = P(ktr); X = np.concatenate([Xb, Xk]); y = np.r_[np.zeros(len(Xb)), np.ones(len(Xk))]
        w = np.where(y == 1, len(Xb) / len(Xk), 1.0) ** 0.5
        clf = xgb.XGBClassifier(n_estimators=150, max_depth=8, learning_rate=0.1, tree_method="hist", n_jobs=8, random_state=a.seed)
        clf.fit(X, y, sample_weight=w)
        s = lambda Z: clf.predict_proba(Z)[:, 1]  # noqa: E731
        att_s[f] = s(Xatt[att_fam == f]); cal_s.append(s(cal))
        if day_s is None:
            day_s = {d: [] for d in days}
        for d in days: day_s[d].append(s(days[d]))
        print(f"  xgb fold {f} {time.time() - t0:.0f}s", flush=True)
    # per-family thresholds (each fold has its own model); average FPR/TPR is reported across folds
    r = dict(seed=a.seed, gate="xgb", tau=float("nan"))
    fprs = {d: [] for d in days}; tprs = {}; aucs = {}
    for i, f in enumerate(fams):
        tau = np.quantile(cal_s[i], 0.99)
        for d in days: fprs[d].append(float((day_s[d][i] > tau).mean()))
        tprs[f] = float((att_s[f] > tau).mean())
        ben = np.concatenate([day_s[d][i] for d in days])
        aucs[f] = float(roc_auc_score(np.r_[np.zeros(len(ben)), np.ones(len(att_s[f]))], np.r_[ben, att_s[f]]))
    for d in days: r[f"fpr_{d}"] = float(np.mean(fprs[d]))
    for f in fams: r[f"tpr_{f}"] = tprs[f]; r[f"auc_{f}"] = aucs[f]
    r["tpr_mean"] = float(np.mean(list(tprs.values()))); r["auc_mean"] = float(np.mean(list(aucs.values())))
    rows.append(r)
    print(f"  xgb      fpr={np.mean([r[f'fpr_{d}'] for d in days]):.3f} tpr_mean={r['tpr_mean']:.3f} auc_mean={r['auc_mean']:.3f}", flush=True)
    pd.DataFrame(rows).to_csv(a.out / "h5_results.csv", index=False)
    json.dump(vars(a) | {"csv_dir": str(a.csv_dir), "out": str(a.out)}, open(a.out / "args.json", "w"), indent=1)


if __name__ == "__main__":
    main()
