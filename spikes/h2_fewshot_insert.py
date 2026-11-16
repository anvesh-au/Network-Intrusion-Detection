"""H2: can a few labelled examples teach a new attack class without retraining?

Corrected CIC-IDS2017, leave-one-family-out, same chronological splits as H1
(train < 60% of each day by timestamp, val benign 60-70%, test benign >= 70%).
For held-out family X (sorted by time):
  shots = the first k rows of X (what an analyst would label first), k in {0,1,5,10,50}
  test  = X rows after the first k_max shots (fixed across k), capped
kNN methods: insert the k shots into the index as class "NEW" (encoder NOT retrained).
XGBoost: retrained from scratch with the k shots added as class "NEW".
Isolation Forest: k-independent reference (cannot learn a class).

Per k: recall_new  = X test rows predicted as NEW
       detect      = X test rows that raise an alarm (NEW, any attack, or novel)
       benign_fpr  = test benign rows that raise an alarm
       known_to_new= known-attack test rows predicted as NEW (damage to known classes)
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.ensemble import IsolationForest

sys.path.insert(0, str(Path(__file__).parent))
from data_improved import load_improved  # noqa: E402
from h1_unknown_separability import Prep, embed, knn, train_encoder  # noqa: E402

KS = [0, 1, 5, 10, 50]


def knn_predict(Xidx, yidx, Q, k, eps=1e-3):
    """distance-weighted vote over k neighbours; score = mean distance (novelty)."""
    d, i = knn(Xidx, Q, k)
    w = 1.0 / (d + eps)
    n_cls = int(yidx.max()) + 1
    votes = np.zeros((len(Q), n_cls))
    np.add.at(votes, (np.repeat(np.arange(len(Q)), k), yidx[i].ravel()), w.ravel())
    return votes.argmax(1), d.mean(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv_dir", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--k", type=int, default=10)
    ap.add_argument("--benign_train", type=int, default=150_000)
    ap.add_argument("--attack_cap", type=int, default=10_000)
    ap.add_argument("--benign_test", type=int, default=50_000)
    ap.add_argument("--known_test", type=int, default=2_000)
    ap.add_argument("--steps", type=int, default=2000)
    ap.add_argument("--families", default="")
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(a.seed)

    df, feats = load_improved(a.csv_dir)
    # benign: position within the day; attacks: position within their own class (each attack is a
    # single time window, so a day-position split would put whole classes in train-only or test-only)
    df = df.sort_values(["file_idx", "pos"]).reset_index(drop=True)
    cpos = df.groupby("Label").cumcount() / df.groupby("Label")["Label"].transform("size")
    p = np.where(df["family"] == "benign", df["pos"], cpos)
    df["split"] = np.where(p < 0.6, "train", np.where(p < 0.7, "val", "test"))
    print(df.groupby(["family", "split"]).size().unstack(fill_value=0))

    def cap(d, n):
        return d.sample(n=min(n, len(d)), random_state=int(rng.integers(1 << 31)))

    ben = df[df.family == "benign"]
    ben_tr, ben_val, ben_te = (cap(ben[ben.split == s], n) for s, n in
                               (("train", a.benign_train), ("val", 20_000), ("test", a.benign_test)))
    families = [f for f in a.families.split(",") if f] or sorted(set(df.family) - {"benign"})
    rows = []
    for fam in families:
        t0 = time.time()
        X_all = df[df.family == fam].sort_values(["file_idx", "pos"])
        k_max = min(max(KS), len(X_all) // 2)
        ks = [k for k in KS if k <= k_max]
        print(f"\n=== held-out family: {fam} (n={len(X_all)}, k up to {k_max}) ===")
        shots_all = X_all.iloc[:k_max]
        x_te = cap(X_all.iloc[k_max:], a.attack_cap)

        known = df[(df.family != "benign") & (df.family != fam)]
        att_tr = pd.concat([cap(g, a.attack_cap) for _, g in known[known.split == "train"].groupby("Label")])
        known_te = cap(known[known.split == "test"], a.known_test)
        tr = pd.concat([ben_tr, att_tr])
        labels = sorted(tr.Label.unique()) + ["NEW"]; lid = {l: i for i, l in enumerate(labels)}
        ytr = tr.Label.map(lid).to_numpy(); B, NEW = lid["BENIGN"], lid["NEW"]

        prep = Prep().fit(tr[feats].to_numpy(np.float64))
        P = lambda d: prep(d[feats].to_numpy(np.float64))  # noqa: E731
        Xtr, Xval, Xshot = P(tr), P(ben_val), P(shots_all)
        te = pd.concat([ben_te.assign(g="benign"), x_te.assign(g="new"), known_te.assign(g="known")])
        Xte, g = P(te), te.g.to_numpy()

        enc = train_encoder(Xtr, ytr, a.steps, a.seed)
        spaces = {"knn_raw": (Xtr, Xval, Xshot, Xte),
                  "knn_enc": tuple(embed(enc, M) for M in (Xtr, Xval, Xshot, Xte))}

        iso = IsolationForest(n_estimators=300, random_state=a.seed, n_jobs=8).fit(Xtr[ytr == B])
        tau_iso = np.quantile(-iso.score_samples(Xval), 0.99)
        alarm_iso = -iso.score_samples(Xte) > tau_iso

        for k in ks:
            yidx = np.concatenate([ytr, np.full(k, NEW)])
            for name, (Etr, Eval, Eshot, Ete) in spaces.items():
                Eidx = np.concatenate([Etr, Eshot[:k]])
                _, sval = knn_predict(Eidx, yidx, Eval, a.k)
                tau = np.quantile(sval, 0.99)
                pred, ste = knn_predict(Eidx, yidx, Ete, a.k)
                alarm = (pred != B) | (ste > tau)
                rows.append(dict(family=fam, k=k, method=name, pred=pred, alarm=alarm))
            # XGBoost retrained with the shots
            Xx = np.concatenate([Xtr, Xshot[:k]])
            present = np.unique(yidx); remap = {c: i for i, c in enumerate(present)}
            yy = np.vectorize(remap.get)(yidx)
            _, inv, cnt = np.unique(yy, return_inverse=True, return_counts=True)
            clf = xgb.XGBClassifier(n_estimators=200, max_depth=8, learning_rate=0.1, tree_method="hist",
                                    n_jobs=8, random_state=a.seed)
            clf.fit(Xx, yy, sample_weight=1 / np.sqrt(cnt[inv]))
            bi = remap[B]
            tau = np.quantile(1 - clf.predict_proba(Xval)[:, bi], 0.99)
            pt = clf.predict_proba(Xte)
            pred = present[pt.argmax(1)]
            rows.append(dict(family=fam, k=k, method="xgb", pred=pred, alarm=(1 - pt[:, bi]) > tau))
            rows.append(dict(family=fam, k=k, method="iforest", pred=np.where(alarm_iso, -1, B), alarm=alarm_iso))
            for r in rows[-4:]:
                p, al = r.pop("pred"), r.pop("alarm")
                r.update(n_x=int((g == "new").sum()),
                         recall_new=float((p[g == "new"] == NEW).mean()),
                         detect=float(al[g == "new"].mean()),
                         benign_fpr=float(al[g == "benign"].mean()),
                         known_to_new=float((p[g == "known"] == NEW).mean()))
                print(f"  k={k:2d} {r['method']:8s} recall_new={r['recall_new']:.3f} detect={r['detect']:.3f} "
                      f"benign_fpr={r['benign_fpr']:.3f} known_to_new={r['known_to_new']:.3f}")
        print(f"  ({time.time() - t0:.0f}s)")
        pd.DataFrame(rows).to_csv(a.out / "h2_results.csv", index=False)

    json.dump(vars(a) | {"csv_dir": str(a.csv_dir), "out": str(a.out)}, open(a.out / "args.json", "w"), indent=1)


if __name__ == "__main__":
    main()
