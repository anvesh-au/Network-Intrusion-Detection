"""H5b: benign gate when known AND unseen attacks are present together.

Same data/split as H5 (corrected CIC-IDS2017; Mon/Tue benign train, calibration slice, Wed-Fri benign test).
Each fold holds out 2 attack families as UNSEEN; the other 6 are KNOWN.
  known attacks : XGBoost trains on their first 60% (in time, within the label); test uses the remaining 40%
  unseen attacks: never trained on; test uses all their rows
All gates get ONE threshold (99th pct of calibration benign) and score the benign + known + unseen test flows together.
Gates: knn20k, knnfull (benign-only index), ae, vae (benign-only), xgb (benign-vs-rest on known attacks).
Metrics per fold: benign FPR, TPR on known families (macro), TPR on unseen families (macro), TPR on all (macro).
"""
from __future__ import annotations
import argparse, json, sys, time
from pathlib import Path
import numpy as np, pandas as pd, torch
import xgboost as xgb

sys.path.insert(0, str(Path(__file__).parent))
from data_improved import load_improved  # noqa: E402
from h1_unknown_separability import Prep  # noqa: E402
from h5_benign_gate import knn_score, recon_err, train_ae  # noqa: E402

FOLDS = [("bot", "web"), ("dos", "portscan"), ("ddos", "bruteforce"), ("heartbleed", "infiltration")]


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
    torch.set_num_threads(8); rng = np.random.default_rng(a.seed)

    df, feats = load_improved(a.csv_dir)
    df = df.sort_values(["file_idx", "pos"]).reset_index(drop=True)
    ben = df[df.family == "benign"]
    att = df[df.family != "benign"].copy()
    att["cpos"] = att.groupby("Label").cumcount() / att.groupby("Label")["Label"].transform("size")
    pool = ben[ben.file_idx <= 1]
    cut = int(0.8 * len(pool)); tr_df, cal_df = pool.iloc[:cut], pool.iloc[cut:]
    prep = Prep().fit(pool[feats].to_numpy(np.float64))
    P = lambda d: prep(d[feats].to_numpy(np.float64))  # noqa: E731
    Xtr = P(tr_df); cal = P(cal_df.sample(n=min(30_000, len(cal_df)), random_state=a.seed))
    days = {n: P(ben[ben.file_idx == fi].sample(n=min(a.test_cap, (ben.file_idx == fi).sum()), random_state=a.seed))
            for fi, n in ((2, "wed"), (3, "thu"), (4, "fri"))}
    Xday = np.concatenate(list(days.values()))
    fams = sorted(att.family.unique())
    t0 = time.time()
    sub = Xtr[rng.choice(len(Xtr), min(a.cand, len(Xtr)), replace=False)]
    idx20 = sub[rng.choice(len(sub), 20_000, replace=False)]
    gates = {"knn20k": lambda X: knn_score(idx20, X), "knnfull": lambda X: knn_score(Xtr, X)}
    for name, vae in (("ae", False), ("vae", True)):
        m = train_ae(Xtr, vae, a.epochs, a.seed); gates[name] = lambda X, m=m: recon_err(m, X)
    unsup = {n: (f(cal), f(Xday)) for n, f in gates.items()}
    print(f"unsupervised gates ready {time.time() - t0:.0f}s", flush=True)
    Xb = Xtr[rng.choice(len(Xtr), min(a.xgb_benign, len(Xtr)), replace=False)]

    rows = []
    for fold, unseen in enumerate(FOLDS):
        known = [f for f in fams if f not in unseen]
        # test attack rows: unseen -> all rows; known -> later 40% in time
        parts = []
        for f in fams:
            g = att[att.family == f]
            g = g if f in unseen else g[g.cpos >= 0.6]
            parts.append(g.sample(n=min(3000, len(g)), random_state=a.seed))
        te = pd.concat(parts); Xte = P(te); fam_te = te.family.to_numpy()
        # xgb
        ktr = att[att.family.isin(known) & (att.cpos < 0.6)]
        ktr = pd.concat([g.sample(n=min(a.attack_cap, len(g)), random_state=a.seed) for _, g in ktr.groupby("Label")])
        Xk = P(ktr); X = np.concatenate([Xb, Xk]); y = np.r_[np.zeros(len(Xb)), np.ones(len(Xk))]
        clf = xgb.XGBClassifier(n_estimators=150, max_depth=8, learning_rate=0.1, tree_method="hist", n_jobs=8, random_state=a.seed)
        clf.fit(X, y, sample_weight=np.where(y == 1, len(Xb) / len(Xk), 1.0) ** 0.5)
        s = lambda Z: clf.predict_proba(Z)[:, 1]  # noqa: E731
        res = {n: (c, d, g(Xte)) for n, ((c, d), g) in zip(unsup, [(unsup[n], gates[n]) for n in unsup])}
        res["xgb"] = (s(cal), s(Xday), s(Xte))
        for n, (c, d, at) in res.items():
            tau = np.quantile(c, 0.99)
            r = dict(seed=a.seed, fold="+".join(unseen), gate=n, fpr=float((d > tau).mean()))
            tpr = {f: float((at[fam_te == f] > tau).mean()) for f in fams}
            for f in fams: r[f"tpr_{f}"] = tpr[f]
            r["tpr_known"] = float(np.mean([tpr[f] for f in known])); r["tpr_unseen"] = float(np.mean([tpr[f] for f in unseen]))
            r["tpr_all"] = float(np.mean(list(tpr.values())))
            rows.append(r)
            print(f"  unseen={r['fold']:22s} {n:8s} fpr={r['fpr']:.3f} known={r['tpr_known']:.2f} unseen={r['tpr_unseen']:.2f} all={r['tpr_all']:.2f}", flush=True)
    pd.DataFrame(rows).to_csv(a.out / "h5b_results.csv", index=False)
    json.dump(vars(a) | {"csv_dir": str(a.csv_dir), "out": str(a.out)}, open(a.out / "args.json", "w"), indent=1)


if __name__ == "__main__":
    main()
