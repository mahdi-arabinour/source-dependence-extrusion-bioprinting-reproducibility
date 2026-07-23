# Source Dependence and Cross-Publication Transportability in Extrusion Bioprinting

## Associated article

**Source Dependence and Cross-Publication Transportability of Machine-Learning Models in Extrusion Bioprinting: A Hierarchical Reanalysis of Cell Viability and Filament Geometry**

## Repository purpose

This is the journal-facing reproducibility repository for the associated article. The same tagged release is intended for GitHub and permanent archiving in Zenodo. It contains the data, locked analysis definitions, executable workflow, consolidated verification artifacts, tables, figure source data, and final figures needed to inspect and reproduce the reported analyses without exposing readers to caches, obsolete files, duplicate outputs, or thousands of internal task fragments.

## Start here

1. Read [`REPRODUCE.md`](REPRODUCE.md).
2. Install the environment from `requirements.txt` or `environment.yml`.
3. Review the immutable source datasets in `data/raw/` and canonical modeling datasets in `data/processed/`.
4. Review locked features, preprocessing rules, model specifications, hyperparameters, and validation splits in `config/`.
5. Run the notebook in `notebooks/` from the repository root or from the `notebooks/` directory.
6. Compare regenerated outputs with the curated artifacts in `results/`, `tables/`, `figure_source_data/`, and `figures/`.
7. Run `python scripts/validate_package.py` to check the public package structure and manifest.

## Repository structure

- `data/raw/` — immutable literature-derived source datasets
- `data/interim/` — registered intermediate datasets retained for lineage
- `data/processed/` — canonical analysis-ready datasets
- `config/` — locked variables, features, models, preprocessing, hyperparameters, and split assignments
- `src/` — reusable Python modules
- `notebooks/` — sanitized executable end-to-end analysis notebook using repository-relative paths
- `audit/` — selected quality-control, leakage-control, lineage, and checkpoint evidence
- `results/` — consolidated predictions, metrics, statistical comparisons, sensitivity analyses, and locked outputs
- `tables/` — manuscript and supplementary tables
- `figure_source_data/` — numeric data underlying reported figures
- `figures/` — final PDF and PNG figures
- `scripts/` — package validation utility

## Reproducibility scope

The package supports inspection and rerunning of the locked workflow from source data through publication-aware validation, hierarchical analyses, model interpretation, sensitivity analyses, and manuscript reporting. Random row-wise validation and publication-grouped validation answer different questions and should not be treated as interchangeable. SHAP values are predictive attributions rather than causal effects.

The notebook writes newly generated working artifacts to its documented analysis directories. The top-level `results/`, `tables/`, `figure_source_data/`, and `figures/` directories contain the curated reference artifacts used for manuscript verification. Large consolidated prediction tables are stored as `.csv.gz` and can be read directly with `pandas.read_csv()`.

## Curated exclusions

The public repository intentionally omits software caches, temporary execution files, obsolete output versions, duplicate large image formats, and redundant per-task fragments already represented by consolidated outputs. These exclusions reduce clutter without removing source data, locked analysis definitions, the executable workflow, or principal verification artifacts.

## Citation

Use the metadata in [`CITATION.cff`](CITATION.cff). A Zenodo DOI badge and DOI citation will be added after the first clean GitHub release is archived.

## License

Code is released under the MIT License. Dataset reuse conditions are described in [`DATA_LICENSE.md`](DATA_LICENSE.md).
