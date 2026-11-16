"""H1: do unseen attack families land far from everything known?

Leave-one-family-out on CIC-IDS2017 (MachineLearningCVE CSVs), chronological splits.
For each held-out family X:
  train  = rows in the first 60% of each day-file, all classes except X
  val    = benign rows at 60-70% of each file (threshold calibration only)
  test   = benign rows in the last 30% of each file  +  ALL rows of X (never seen)
Methods (all trained without X):
  knn_raw : kNN over standardised (signed-log) raw features
  knn_enc : kNN over a supervised SupCon MLP encoder (64-d, L2-normalised)
  xgb     : XGBoost multi-class; score = 1 - P(benign)
  iforest : Isolation Forest on train benign
Metrics per method: AUROC(X vs test benign) of the score, and the operating point
calibrated on val benign at 1% FPR: TPR on X and FPR on test benign.
For kNN methods the alarm is "novel (dist > tau) OR kNN vote says attack".
"""
from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path

import faiss
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import xgboost as xgb
from sklearn.ensemble import IsolationForest
from sklearn.metrics import roc_auc_score

FILES = [  # chronological order of the capture week
    "Monday-WorkingHours.pcap_ISCX.csv",
    "Tuesday-WorkingHours.pcap_ISCX.csv",
    "Wednesday-workingHours.pcap_ISCX.csv",
    "Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv",
    "Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv",
    "Friday-WorkingHours-Morning.pcap_ISCX.csv",
    "Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv",
    "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
]
DROP = {"Destination Port", "Fwd Header Length.1"}  # port = dataset shortcut; .1 = duplicate column
FAMILY = {
    "BENIGN": "benign",
    "DoS Hulk": "dos", "DoS GoldenEye": "dos", "DoS slowloris": "dos", "DoS Slowhttptest": "dos",
    "DDoS": "ddos", "PortScan": "portscan", "Bot": "bot",
    "FTP-Patator": "bruteforce", "SSH-Patator": "bruteforce",
    "Web Attack - Brute Force": "web", "Web Attack - XSS": "web", "Web Attack - Sql Injection": "web",
    "Infiltration": "infiltration", "Heartbleed": "heartbleed",
}


def load(csv_dir: Path) -> pd.DataFrame:
    parts = []
    for i, f in enumerate(FILES):
        df = pd.read_csv(csv_dir / f, encoding="latin-1", low_memory=False)
        df.columns = [c.strip() for c in df.columns]
        df["file_idx"] = i
        df["pos"] = np.arange(len(df)) / len(df)  # relative position within the day-file (row order = time order)
        parts.append(df)
    df = pd.concat(parts, ignore_index=True)
    # "Web Attack \x96 Brute Force" -> "Web Attack - Brute Force"
    df["Label"] = df["Label"].astype(str).map(lambda s: " ".join(re.sub(r"[^\x20-\x7e]+", "-", s).split()))
    unknown = set(df["Label"].unique()) - set(FAMILY)
    if unknown:
        raise ValueError(f"unmapped labels: {unknown}")
    df["family"] = df["Label"].map(FAMILY)
    feats = [c for c in df.columns if c not in DROP | {"Label", "family", "file_idx", "pos"}]
    df[feats] = df[feats].apply(pd.to_numeric, errors="coerce").replace([np.inf, -np.inf], np.nan)
    n0 = len(df)
    df = df.dropna(subset=feats)
    n1 = len(df)
    df = df.drop_duplicates(subset=feats, keep="first")  # keep earliest occurrence; no train/test twins
    print(f"rows: {n0:,} -> {n1:,} (nan/inf) -> {len(df):,} (dedup)")
    return df.reset_index(drop=True), feats


class Prep:
    """signed log1p + standardise + clip; fitted on train only."""

    def fit(self, X):
        Z = np.sign(X) * np.log1p(np.abs(X))
        self.mu, self.sd = Z.mean(0), Z.std(0) + 1e-6
        return self

    def __call__(self, X):
        Z = (np.sign(X) * np.log1p(np.abs(X)) - self.mu) / self.sd
        return np.clip(Z, -10, 10).astype(np.float32)


class Encoder(nn.Module):
    def __init__(self, d_in, d_out=64):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(d_in, 256), nn.BatchNorm1d(256), nn.GELU(),
                                 nn.Linear(256, 256), nn.BatchNorm1d(256), nn.GELU(),
                                 nn.Linear(256, d_out))

    def forward(self, x):
        return F.normalize(self.net(x), dim=1)


def supcon(z, y, t=0.1):
    sim = z @ z.T / t
    eye = torch.eye(len(z), dtype=torch.bool)
    sim = sim.masked_fill(eye, -1e9)
    pos = (y[:, None] == y[None, :]) & ~eye
    logp = sim - torch.logsumexp(sim, dim=1, keepdim=True)
    has = pos.any(1)
    return -((logp * pos).sum(1)[has] / pos.sum(1)[has]).mean()


def train_encoder(X, y, steps, seed, bs=1024):
    torch.manual_seed(seed)
    rng = np.random.default_rng(seed)
    _, inv, cnt = np.unique(y, return_inverse=True, return_counts=True)
    w = 1.0 / np.sqrt(cnt[inv]); w /= w.sum()  # softened class balance
    enc = Encoder(X.shape[1]); opt = torch.optim.AdamW(enc.parameters(), 1e-3, weight_decay=1e-4)
    Xt, yt = torch.from_numpy(X), torch.from_numpy(y)
    enc.train()
    for s in range(steps):
        idx = torch.from_numpy(rng.choice(len(X), bs, p=w))
        loss = supcon(enc(Xt[idx]), yt[idx])
        opt.zero_grad(); loss.backward(); opt.step()
        if s % 500 == 0 or s == steps - 1:
            print(f"    supcon step {s:5d} loss {loss.item():.3f}")
    enc.eval()
    return enc


@torch.no_grad()
def embed(enc, X):
    return torch.cat([enc(torch.from_numpy(X[i:i + 8192])) for i in range(0, len(X), 8192)]).numpy()


def knn(index_X, query_X, k):
    idx = faiss.IndexFlatL2(index_X.shape[1]); idx.add(index_X)
    d, i = idx.search(query_X, k)
    return np.sqrt(np.maximum(d, 0)), i


def knn_method(Xtr, ytr, benign_id, Xval, Xte, k):
    """score = mean dist to k nearest known exemplars; vote = majority label among them."""
    out = {}
    for name, Q in (("val", Xval), ("test", Xte)):
        d, i = knn(Xtr, Q, k)
        out[name] = (d.mean(1), (ytr[i] != benign_id).mean(1) > 0.5)
    btr = Xtr[ytr == benign_id]
    out["test_bdist"] = knn(btr, Xte, k)[0].mean(1)  # distance to benign only
    return out


def evaluate(score_val, score_te, is_x, vote_val=None, vote_te=None, fpr=0.01):
    tau = np.quantile(score_val, 1 - fpr)
    alarm_te = score_te > tau
    if vote_te is not None:
        alarm_te = alarm_te | vote_te
    ben = ~is_x
    return {"auroc": roc_auc_score(is_x, score_te),
            "tpr@1%": alarm_te[is_x].mean(),
            "test_fpr": alarm_te[ben].mean()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv_dir", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--k", type=int, default=10)
    ap.add_argument("--benign_train", type=int, default=150_000)
    ap.add_argument("--attack_cap", type=int, default=10_000)
    ap.add_argument("--benign_test", type=int, default=50_000)
    ap.add_argument("--steps", type=int, default=2000)
    ap.add_argument("--families", default="")
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(a.seed)
    faiss.omp_set_num_threads(8); torch.set_num_threads(8)

    df, feats = load(a.csv_dir)
    split = np.where(df["pos"] < 0.6, "train", np.where(df["pos"] < 0.7, "val", "test"))
    df["split"] = split
    print(df.groupby(["family", "split"]).size().unstack(fill_value=0))

    def cap(d, n):
        return d.sample(n=min(n, len(d)), random_state=int(rng.integers(1 << 31)))

    families = [f for f in a.families.split(",") if f] or sorted(set(FAMILY.values()) - {"benign"})
    ben = df[df.family == "benign"]
    ben_tr, ben_val, ben_te = (cap(ben[ben.split == s], n) for s, n in
                               (("train", a.benign_train), ("val", 20_000), ("test", a.benign_test)))
    rows = []
    for fam in families:
        t0 = time.time()
        print(f"\n=== held-out family: {fam} ===")
        known_att = df[(df.family != "benign") & (df.family != fam) & (df.split == "train")]
        att_tr = pd.concat([cap(g, a.attack_cap) for _, g in known_att.groupby("Label")])
        tr = pd.concat([ben_tr, att_tr])
        x_rows = cap(df[df.family == fam], a.attack_cap)  # all rows of X are unseen
        te = pd.concat([ben_te, x_rows])
        is_x = (te.family == fam).to_numpy()

        labels = sorted(tr.Label.unique()); lid = {l: i for i, l in enumerate(labels)}
        ytr = tr.Label.map(lid).to_numpy(); b = lid["BENIGN"]
        prep = Prep().fit(tr[feats].to_numpy(np.float64))
        Xtr, Xval, Xte = (prep(d[feats].to_numpy(np.float64)) for d in (tr, ben_val, te))

        res = {}
        # 1. kNN on raw features
        o = knn_method(Xtr, ytr, b, Xval, Xte, a.k)
        res["knn_raw"] = evaluate(o["val"][0], o["test"][0], is_x, o["val"][1], o["test"][1])
        res["knn_raw"]["auroc_bdist"] = roc_auc_score(is_x, o["test_bdist"])
        # 2. kNN on supervised encoder
        enc = train_encoder(Xtr, ytr, a.steps, a.seed)
        Etr, Eval, Ete = embed(enc, Xtr), embed(enc, Xval), embed(enc, Xte)
        o = knn_method(Etr, ytr, b, Eval, Ete, a.k)
        res["knn_enc"] = evaluate(o["val"][0], o["test"][0], is_x, o["val"][1], o["test"][1])
        res["knn_enc"]["auroc_bdist"] = roc_auc_score(is_x, o["test_bdist"])
        # 3. XGBoost
        clf = xgb.XGBClassifier(n_estimators=300, max_depth=8, learning_rate=0.1, tree_method="hist",
                                n_jobs=8, random_state=a.seed)
        _, inv, cnt = np.unique(ytr, return_inverse=True, return_counts=True)
        clf.fit(Xtr, ytr, sample_weight=(1 / np.sqrt(cnt[inv])))
        pv, pt = clf.predict_proba(Xval), clf.predict_proba(Xte)
        res["xgb"] = evaluate(1 - pv[:, b], 1 - pt[:, b], is_x)
        res["xgb"]["auroc_1-maxp"] = roc_auc_score(is_x, 1 - pt.max(1))
        # 4. Isolation Forest (benign only)
        iso = IsolationForest(n_estimators=300, random_state=a.seed, n_jobs=8).fit(Xtr[ytr == b])
        res["iforest"] = evaluate(-iso.score_samples(Xval), -iso.score_samples(Xte), is_x)

        for m, r in res.items():
            rows.append({"family": fam, "n_x": int(is_x.sum()), "method": m, **r})
            print(f"  {m:8s} " + "  ".join(f"{k}={v:.3f}" for k, v in r.items()))
        print(f"  ({time.time() - t0:.0f}s)")
        pd.DataFrame(rows).to_csv(a.out / "h1_results.csv", index=False)

    R = pd.DataFrame(rows)
    piv = R.pivot(index="family", columns="method", values=["auroc", "tpr@1%", "test_fpr"]).round(3)
    piv.to_csv(a.out / "h1_pivot.csv")
    print("\n", piv.to_string())
    print("\nmedian AUROC:", R.groupby("method").auroc.median().round(3).to_dict())
    json.dump(vars(a) | {"csv_dir": str(a.csv_dir), "out": str(a.out)}, open(a.out / "args.json", "w"), indent=1)


if __name__ == "__main__":
    main()
