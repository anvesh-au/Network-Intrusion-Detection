"""Loader for the corrected CIC-IDS2017 (Engelen et al., CNS 2022: CICIDS2017_improved.zip).

- Rows are sorted by the real Timestamp within each day; `pos` = rank within the day in [0, 1).
- "... - Attempted" rows (attacks that failed / carry no attack payload) are dropped.
- "Infiltration - Portscan" (the infiltrated host scanning the LAN) is put in the portscan family.
- Identifier columns (id, Flow ID, IPs, ports, Timestamp, Attempted Category) are dropped from features.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday"]
ID_COLS = {"id", "Flow ID", "Src IP", "Src Port", "Dst IP", "Dst Port", "Timestamp", "Attempted Category",
           "Label"}
FAMILY = {
    "BENIGN": "benign",
    "FTP-Patator": "bruteforce", "SSH-Patator": "bruteforce",
    "DoS Hulk": "dos", "DoS GoldenEye": "dos", "DoS Slowloris": "dos", "DoS Slowhttptest": "dos",
    "Heartbleed": "heartbleed",
    "Web Attack - Brute Force": "web", "Web Attack - XSS": "web", "Web Attack - SQL Injection": "web",
    "Infiltration": "infiltration",
    "Infiltration - Portscan": "portscan", "Portscan": "portscan",
    "DDoS": "ddos", "Botnet": "bot",
}


def load_improved(csv_dir: Path):
    parts = []
    for i, d in enumerate(DAYS):
        df = pd.read_csv(csv_dir / f"{d}.csv", low_memory=False)
        df["Label"] = df["Label"].astype(str).str.strip()
        df = df[~df["Label"].str.endswith("Attempted")]
        df["ts"] = pd.to_datetime(df["Timestamp"])
        df = df.sort_values("ts", kind="stable").reset_index(drop=True)
        df["file_idx"] = i
        df["pos"] = np.arange(len(df)) / len(df)
        parts.append(df)
    df = pd.concat(parts, ignore_index=True)
    unknown = set(df["Label"].unique()) - set(FAMILY)
    if unknown:
        raise ValueError(f"unmapped labels: {unknown}")
    df["family"] = df["Label"].map(FAMILY)
    feats = [c for c in df.columns if c not in ID_COLS | {"family", "file_idx", "pos", "ts"}]
    df[feats] = df[feats].apply(pd.to_numeric, errors="coerce").replace([np.inf, -np.inf], np.nan)
    n0 = len(df)
    df = df.dropna(subset=feats)
    n1 = len(df)
    df = df.drop_duplicates(subset=feats, keep="first")
    print(f"rows: {n0:,} -> {n1:,} (nan/inf) -> {len(df):,} (dedup); {len(feats)} features")
    return df.reset_index(drop=True), feats
