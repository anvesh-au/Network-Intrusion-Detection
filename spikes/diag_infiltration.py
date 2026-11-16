"""Why is infiltration never named? Re-run A1/B1 (seed 0) up to the infiltration blocks and log cluster stats."""
import sys, json
from pathlib import Path
import numpy as np, pandas as pd
sys.path.insert(0, str(Path(__file__).parent))
import h6_daily_harness as H
from argparse import Namespace

a = Namespace(cap=2000, benign_index=100_000, assumed_benign=3000, half_life=6.0, max_age=3, anchors=20, seed=0)
csv = Path(sys.argv[1]); B = int(sys.argv[2])
df, feats = H.load_improved(csv); df["cid"] = df.family.map(H.CID)
tr = df[df.file_idx <= 2]; rp = df[df.file_idx >= 3]
rng = np.random.default_rng(0)
ben = tr[tr.cid == 0].sort_values("ts"); cut = int(.85 * len(ben)); cand, cal = ben.iloc[:cut], ben.iloc[cut:]
prep = H.Prep().fit(cand[feats].to_numpy(np.float64)); P = lambda d: prep(d[feats].to_numpy(np.float64))
Xpool = P(cand); Xcal = P(cal.sample(n=30000, random_state=0))
ka = tr[tr.cid > 0].sort_values("ts").copy(); ka["cpos"] = ka.groupby("cid").cumcount() / ka.groupby("cid")["cid"].transform("size")
probe = pd.concat([g.sample(n=min(3000, len(g)), random_state=0) for _, g in ka[ka.cpos >= .6].groupby("cid")])
Xa, ya = [], []
for c in sorted(set(ka.cid)):
    X = P(ka[(ka.cid == c) & (ka.cpos < .6)])
    if len(X) > a.cap: X = X[H.kcenter(X, a.cap, 0)]
    Xa.append(X); ya.append(np.full(len(X), c))
Xa, ya = np.concatenate(Xa), np.concatenate(ya); Xb = Xpool[rng.choice(len(Xpool), 100000, replace=False)]
init = dict(Xpool=Xpool, Xa=Xa, ya=ya, Xb=Xb, Xpr=P(probe), ypr=probe.cid.to_numpy())
p0, n0, _ = H.score(np.concatenate([Xb, Xa]), np.r_[np.zeros(len(Xb), int), ya], Xcal); tau = float(np.quantile(n0, .99))
rp = rp.assign(blk=rp.file_idx.astype(str) + "-" + rp.ts.dt.hour.astype(str).str.zfill(2)).sort_values("ts")
blocks = [(n, P(g), g.cid.to_numpy()) for n, g in rp.groupby("blk", sort=True)]
blocks = blocks[:8]   # through 3-18
dbg = []
H.run_config(("A1", "B1", B), init, blocks, tau, a, 0, dbg=dbg)
NM = H.NAMES
for d in dbg:
    if d["n_infil"]:
        print(f"B={B} block {d['block']}: flagged={d['n_flagged']} clusters={d['n_clusters']} infil={d['n_infil']} (flagged&clustered {d['infil_flagged']}) "
              f"in {d['infil_clusters']} clusters; sizes={d['cluster_size']} infil share={d['cluster_infil_share']} "
              f"rep labels of those clusters={[NM[c] for c in d['rep_label_of_cluster']]}; reps chosen by class={dict(zip(NM, d['rep_labels']))}")

# geometry: are the later infiltration flows closer to earlier infiltration flows, or to DoS / portscan exemplars?
inf = rp[rp.cid == 5].sort_values("ts"); hour = inf.ts.dt.hour.to_numpy(); Xi_ = P(inf)
a17, b18 = Xi_[hour == 17], Xi_[hour == 18]
ps = rp[(rp.cid == 6) & (rp.blk == "3-17")]; Xps = P(ps.sample(n=min(3000, len(ps)), random_state=0))
def mind(Q, R):
    d, _ = H.knn(np.ascontiguousarray(R, dtype=np.float32), np.ascontiguousarray(Q, dtype=np.float32), 1); return d[:, 0]
d_inf, d_dos = mind(b18, a17), mind(b18, Xa[ya == 2])
d_ps, d_ben = mind(b18, Xps), mind(b18, Xb)
print(f"\n17 infiltration flows of 3-18: median distance to nearest ... all 19 earlier infiltration flows {np.median(d_inf):.2f}; "
      f"DoS exemplars {np.median(d_dos):.2f}; Thu 3-17 portscan flows {np.median(d_ps):.2f}; benign index {np.median(d_ben):.2f}; tau={tau:.2f}")
print(f"nearer to an earlier infiltration flow than to any DoS exemplar: {(d_inf < d_dos).sum()}/17; than to portscan: {(d_inf < d_ps).sum()}/17")
