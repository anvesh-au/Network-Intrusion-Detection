"""H3: can a bounded index cover benign traffic it has never seen?

Corrected CIC-IDS2017, benign flows only.
  pool  = Mon+Tue benign (chronological). First 80% = candidates for the index, last 20% = calibration.
  test  = Wed, Thu, Fri benign, each day separately (capped).
Selection of `size` index entries from the candidates: random vs greedy k-center (farthest-first).
Score = mean distance to 10 nearest index entries; tau = 99th pct of calibration scores (target FPR 1%).
Also: tpr_* = share of attack flows (all families, Tue-Fri, no hold-out) scored above tau, using the benign-only index.
Metric = fraction of each test day's benign flows with score > tau.
"""
from __future__ import annotations
import argparse, json, sys, time
from pathlib import Path
import numpy as np, pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
from data_improved import load_improved  # noqa: E402
from h1_unknown_separability import Prep, knn  # noqa: E402


def kcenter(X, m, seed):
    """greedy farthest-first traversal; returns indices of m centers."""
    rng = np.random.default_rng(seed)
    first = int(rng.integers(len(X)))
    idx = [first]
    sq = (X * X).sum(1)
    d = np.maximum(sq + sq[first] - 2 * X @ X[first], 0)
    for _ in range(m - 1):
        j = int(d.argmax()); idx.append(j)
        d = np.minimum(d, np.maximum(sq + sq[j] - 2 * X @ X[j], 0))
    return np.array(idx)


def score(index, Q, k):
    d, _ = knn(index, Q, k)
    return d.mean(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv_dir", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--k", type=int, default=10)
    ap.add_argument("--cand", type=int, default=200_000, help="candidate pool cap for k-center")
    ap.add_argument("--sizes", default="500,1000,2000,5000,10000,20000")
    ap.add_argument("--test_cap", type=int, default=50_000)
    a = ap.parse_args(); a.out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(a.seed)

    df, feats = load_improved(a.csv_dir)
    ben = df[df.family == "benign"]
    pool = ben[ben.file_idx <= 1].sort_values(["file_idx", "pos"])
    n = len(pool); cut = int(0.8 * n)
    cand_df, cal_df = pool.iloc[:cut], pool.iloc[cut:]
    prep = Prep().fit(pool[feats].to_numpy(np.float64))
    P = lambda d: prep(d[feats].to_numpy(np.float64))  # noqa: E731
    cand_full = P(cand_df)
    cal = P(cal_df.sample(n=min(30_000, len(cal_df)), random_state=a.seed))
    days = {}
    for fi, name in ((2, "wed"), (3, "thu"), (4, "fri")):
        d = ben[ben.file_idx == fi]
        days[name] = P(d.sample(n=min(a.test_cap, len(d)), random_state=a.seed))
    att = df[(df.family != "benign") & (df.file_idx >= 1)]
    att = pd.concat([g.sample(n=min(3000, len(g)), random_state=a.seed) for _, g in att.groupby("family")])
    att_fam = att.family.to_numpy(); Xatt = P(att)
    print(f"candidates={len(cand_full):,} calibration={len(cal):,} tests={ {k: len(v) for k, v in days.items()} }")
    sub = rng.choice(len(cand_full), size=min(a.cand, len(cand_full)), replace=False)
    cand = cand_full[sub]

    rows = []
    def run(method, size, index):
        tau = np.quantile(score(index, cal, a.k), 0.99)
        r = dict(seed=a.seed, method=method, size=size, tau=float(tau))
        for name, Xd in days.items():
            r[f"fpr_{name}"] = float((score(index, Xd, a.k) > tau).mean())
        sa = score(index, Xatt, a.k) > tau
        for fam in sorted(set(att_fam)):
            r[f"tpr_{fam}"] = float(sa[att_fam == fam].mean())
        r["tpr_mean"] = float(np.mean([r[k] for k in r if k.startswith("tpr_")]))
        rows.append(r)
        print(f"  {method:8s} size={size:7,d} tau={tau:.3f} " + " ".join(f"{k}={r[k]:.3f}" for k in r if k.startswith("fpr_")) + f" tpr_mean={r['tpr_mean']:.3f}", flush=True)

    t0 = time.time()
    for size in [int(s) for s in a.sizes.split(",")]:
        run("random", size, cand[rng.choice(len(cand), size, replace=False)])
        run("kcenter", size, cand[kcenter(cand, size, a.seed)])
        print(f"  ({time.time() - t0:.0f}s)")
    run("full", len(cand_full), cand_full)
    pd.DataFrame(rows).to_csv(a.out / "h3_results.csv", index=False)
    json.dump(vars(a) | {"csv_dir": str(a.csv_dir), "out": str(a.out)}, open(a.out / "args.json", "w"), indent=1)


if __name__ == "__main__":
    main()
