# Reproducing the analysis

## 1. Environment

Recommended setup:

- Python 3.12
- Linux or macOS; Windows should also work in a standard Python environment
- Master random seed: 42

Using `venv`:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Alternatively:

```bash
conda env create -f environment.yml
conda activate source-dependence-bioprinting
```

## 2. Inputs

The immutable source files are in `data/raw/`. Do not overwrite them. Canonical analysis-ready datasets are in `data/processed/`; selected row-lineage and quality-control evidence is retained in `audit/`.

## 3. Locked definitions

Review `config/` before execution. It contains the locked feature sets, variable registry, preprocessing rules, model and hyperparameter specifications, publication mapping, and inner/outer split assignments.

## 4. Execute

Start Jupyter from the repository root:

```bash
python -m notebook
```

Open the notebook in `notebooks/` and run it from top to bottom. The notebook uses repository-relative paths and does not require Google Drive or interactive file upload. Reusable functions are under `src/`.

The workflow covers source registration, dataset construction, row lineage, plausibility checks, publication-aware split locking, leakage-safe preprocessing, baselines, nested cross-validation, paired comparisons, publication-level heterogeneity, hierarchical analyses, grouped out-of-fold SHAP, sensitivity analyses, classification analyses, and reporting.

## 5. Verification

Compare regenerated outputs with the curated reference artifacts under `results/`, `tables/`, `figure_source_data/`, and `figures/`. Large `.csv.gz` files are ordinary gzip-compressed CSV files and can be read directly with pandas.

Run:

```bash
python scripts/validate_package.py
```

to verify required paths and SHA-256 values recorded in `MANIFEST.csv`.

## 6. Expected safeguards

The locked workflow is designed so that publication groups do not overlap across grouped train/test partitions; outer test rows are excluded from inner tuning; preprocessing is fitted only on training data; split definitions and model candidates remain fixed; model interpretation uses grouped out-of-fold predictions; and sensitivity and classification analyses follow prespecified definitions.

## 7. Reporting

Use the locked tables and figure-source files rather than manually transcribing values from plots. Internal caches, obsolete files, and redundant per-task fragments are intentionally excluded from this journal-facing package.
