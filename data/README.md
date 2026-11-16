# Data

## `cicids2017_improved/`: corrected CIC-IDS2017 (used by every spike except H1)

- **Files:** `monday.csv` … `friday.csv` (1.1 GB total), 2,087,997 rows.
- **Source:** Engelen et al., *Troubleshooting an Intrusion Detection Dataset: the CICIDS2017 Case Study* (CNS 2022). Downloaded from `https://intrusion-detection.distrinet-research.be/CNS2022/Datasets/CICIDS2017_improved.zip`.
- **Differences from the original MachineLearningCVE CSVs:** real timestamps (rows are not sorted in time), "Attempted" attack labels, fixed flow artefacts, 91 columns.
- **Loader:** `spikes/data_improved.py` (`load_improved`): sorts by timestamp, drops "Attempted" rows and identifier columns, merges sub-attacks into 8 families, drops NaN/inf and duplicates → 1,706,121 flows, 82 features.
- **Usage:** `--csv_dir data/cicids2017_improved` for `spikes/h2_*`, `h3_*`, `h5*`, `h6_*`.

The original MachineLearningCVE CSVs (used only by H1, `spikes/h1_unknown_separability.py`) are not copied here; the earlier download is gone. Re-download them to rerun H1.
