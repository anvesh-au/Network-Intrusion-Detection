"""Plot replay confusion matrices (mean of seeds) for one attack/benign configuration.  usage: h6_plot_confusion.py A3b B3 [r1.0]"""
import sys
from pathlib import Path
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

ap, br = sys.argv[1], sys.argv[2]; suf = f"_{sys.argv[3]}" if len(sys.argv) > 3 else ""
root = Path(__file__).parent / "results" / "h6"
N = ["benign", "bruteforce", "dos", "heartbleed", "web", "infiltration", "portscan", "bot", "ddos"]; C = N + ["unknown"]
fig, axes = plt.subplots(1, 2, figsize=(17, 6.6))
for ax, B in zip(axes, (100, 500)):
    tag = f"{ap}_{br}_B{B}{suf}"
    m = np.mean([np.load(root / f"seed{s}/{tag}/conf_by_block.npy").sum(0) for s in (0, 1)], 0)
    keep = [i for i in range(9) if m[i].sum() > 0]          # classes present in the replay
    m = m[keep]; rn = m / m.sum(1, keepdims=True)
    ax.imshow(rn, cmap="Blues", vmin=0, vmax=1)
    for i in range(len(keep)):
        for j in range(10):
            if m[i, j] >= 0.5:
                ax.text(j, i, f"{rn[i, j] * 100:.0f}%\n{int(round(m[i, j])):,}", ha="center", va="center", fontsize=7.5,
                        color="white" if rn[i, j] > 0.55 else "black")
    ax.set_xticks(range(10)); ax.set_xticklabels(C, rotation=40, ha="right")
    ax.set_yticks(range(len(keep))); ax.set_yticklabels([f"{N[i]} (n={int(round(m[k].sum())):,})" for k, i in enumerate(keep)])
    ax.set_xlabel("predicted"); ax.set_ylabel("true class"); ax.set_title(f"{ap} + {br}{suf.replace('_', ', ')}, {B} labels/block")
    for k in range(len(keep) + 1): ax.axhline(k - .5, color="white", lw=.6)
fig.suptitle("Replay (Thu+Fri, 1-hour blocks): rows = true class, cell = % of that class (and flows); mean of 2 seeds", fontsize=11)
fig.tight_layout(); out = root / f"confusion_{ap}_{br}{suf}.png"; fig.savefig(out, dpi=130); print(out)
