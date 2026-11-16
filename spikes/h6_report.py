"""Aggregate H6 results over seeds -> results/h6/REPORT.md (summary + every confusion matrix)."""
import sys
from pathlib import Path
import numpy as np, pandas as pd
sys.path.insert(0, str(Path(__file__).parent))
from h6_daily_harness import COLS, NAMES  # noqa: E402

root = Path(__file__).parent / "results" / "h6"
seeds = sorted(p for p in root.glob("seed*") if p.is_dir())
cfgs = [d.name for d in sorted(seeds[0].iterdir()) if d.is_dir()]
order = ["A0"] + [c for c in cfgs if c != "A0"]

def to_md(df, index=True):
    d = df.reset_index() if index else df
    cols = [str(c) for c in d.columns]
    rows = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    rows += ["| " + " | ".join(str(v) for v in r) + " |" for r in d.itertuples(index=False)]
    return "\n".join(rows)

def mean_conf(cfg, fname, first=None):
    arrs = []
    for s in seeds:
        a = np.load(s / cfg / fname)
        arrs.append(a.sum(0) if first is None else a[first])
    return np.mean(arrs, 0)

def md(m):
    df = pd.DataFrame(np.rint(m).astype(int), index=NAMES, columns=COLS)
    df.insert(0, "n", df.sum(1))
    df.index.name = "true \\ pred"
    return to_md(df)

summ = []
for c in order:
    m = mean_conf(c, "conf_by_block.npy"); p0 = mean_conf(c, "probe_conf_by_block.npy", 0); p1 = mean_conf(c, "probe_conf_by_block.npy", -1)
    r = dict(config=c, benign_fpr=1 - m[0, 0] / m[0].sum())
    for f in range(4, 9):
        r[f"{NAMES[f]} detect/named"] = f"{1 - m[f, 0] / m[f].sum():.2f}/{m[f, f] / m[f].sum():.2f}"
    for f in (1, 2, 3):
        r[f"probe {NAMES[f]} named first->last"] = f"{p0[f, f] / p0[f].sum():.2f}->{p1[f, f] / p1[f].sum():.2f}"
    bl = pd.concat([pd.read_csv(s / c / "blocks.csv") for s in seeds])
    r["labels/block"] = bl.labels_used.mean(); r["contam (attacks in benign adds, total/seed)"] = bl.contam.sum() / len(seeds)
    summ.append(r)
S = pd.DataFrame(summ)
out = ["# H6 report (mean of %d seeds)\n" % len(seeds), "## Summary\n", to_md(S.round(3), index=False), ""]
for c in order:
    out += [f"## {c}\n", "**Replay (Thu+Fri), true class x predicted, flows:**\n", md(mean_conf(c, "conf_by_block.npy")), "",
            "**Known-attack probe (held-out last 40% of Mon-Wed attacks), first block:**\n", md(mean_conf(c, "probe_conf_by_block.npy", 0)), "",
            "**Known-attack probe, last block:**\n", md(mean_conf(c, "probe_conf_by_block.npy", -1)), ""]
(root / "REPORT.md").write_text("\n".join(out)); print(S.round(2).to_string())
