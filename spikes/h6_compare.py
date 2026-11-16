"""H6 comparison table: A1 / A3b x benign rules B1..B4 x budgets (mean of seeds)."""
import json, sys
from pathlib import Path
import numpy as np, pandas as pd
N = ["benign", "bruteforce", "dos", "heartbleed", "web", "infiltration", "portscan", "bot", "ddos"]
root = Path(__file__).parent / "results" / "h6"; seeds = [0, 1]
def tags():
    for ap, suf in (("A1", ""), ("A3b", "_r1.0")):
        for br in ("B1", "B2", "B3", "B4"):
            for b in (100, 500):
                yield f"{ap}_{br}_B{b}{suf}", ap, br, b
rows = []
for tag, ap, br, b in tags():
    cf = np.mean([np.load(root / f"seed{s}/{tag}/conf_by_block.npy").sum(0) for s in seeds], 0)
    pr = [np.mean([np.load(root / f"seed{s}/{tag}/probe_conf_by_block.npy")[i] for s in seeds], 0) for i in (0, -1)]
    bl = pd.concat([pd.read_csv(root / f"seed{s}/{tag}/blocks.csv") for s in seeds])
    r = dict(attack=ap, benign=br, B=b, fpr=1 - cf[0, 0] / cf[0].sum(), fpr_worst_block=bl[bl.n_benign > 1000].fpr.max())
    for k in (4, 5, 6, 7, 8): r[N[k][:5]] = f"{1 - cf[k, 0] / cf[k].sum():.2f}/{cf[k, k] / cf[k].sum():.2f}"
    r["misnamed"] = sum(cf[k, 1:9].sum() - cf[k, k] for k in (4, 5, 6, 7, 8)) / cf[4:9].sum()
    for k in (1, 2, 3): r["pr_" + N[k][:4]] = f"{pr[0][k, k] / pr[0][k].sum():.2f}->{pr[1][k, k] / pr[1][k].sum():.2f}"
    r["pr_detect_dos_last"] = 1 - pr[1][2, 0] / pr[1][2].sum()
    r["benign_repr"] = int(bl.benign_repr.iloc[-1]) if "benign_repr" in bl else 100_000 * 82; r["contam"] = bl.contam.sum() / len(seeds)
    rt = [root / f"seed{s}/{tag}/runtime.json" for s in seeds]
    r["sec"] = np.mean([json.load(open(f))["seconds"] for f in rt]) if all(f.exists() for f in rt) else np.nan
    rows.append(r)
D = pd.DataFrame(rows); D.to_csv(root / "h6_B_comparison.csv", index=False)
pd.set_option("display.width", 250); print(D.round(3).to_string(index=False))
