# Source Dependence and Cross-Publication Transportability in Extrusion Bioprinting

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21517730.svg)](https://doi.org/10.5281/zenodo.21517730)

## Associated article

**Source Dependence and Cross-Publication Transportability of Machine-Learning Models in Extrusion Bioprinting: A Hierarchical Reanalysis of Cell Viability and Filament Geometry**

## Repository purpose

This is the journal-facing reproducibility repository for the associated article. Tagged GitHub releases are permanently archived in Zenodo. The repository contains the data, locked analysis definitions, executable workflow, consolidated verification artifacts, tables, figure source data, and final figures needed to inspect and reproduce the reported analyses without exposing readers to caches, obsolete files, duplicate outputs, or thousands of internal task fragments.

## Permanent links

- **GitHub repository:**  
  https://github.com/mahdi-arabinour/source-dependence-extrusion-bioprinting-reproducibility

- **Current archived Zenodo release:**  
  https://doi.org/10.5281/zenodo.21519626

- **Concept DOI for all versions:**  
  https://doi.org/10.5281/zenodo.21517730

- **Current archived version:**  
  `v1.0.4`

## Start here

1. Read [`REPRODUCE.md`](REPRODUCE.md).
2. Install the environment from `requirements.txt` or `environment.yml`.
3. Review the immutable source datasets in `data/raw/` and the canonical modeling datasets in `data/processed/`.
4. Review the locked features, preprocessing rules, model specifications, hyperparameters, and validation splits in `config/`.
5. Run the notebook in `notebooks/` from the repository root or from the `notebooks/` directory.
6. Compare regenerated outputs with the curated artifacts in `results/`, `tables/`, `figure_source_data/`, and `figures/`.
7. Run the following command to check the public package structure and manifest:

```bash
python scripts/validate_package.py
```

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

The package supports inspection and rerunning of the locked workflow from source data through publication-aware validation, hierarchical analyses, model interpretation, sensitivity analyses, and manuscript reporting.

Random row-wise validation and publication-grouped validation answer different questions and should not be treated as interchangeable. SHAP values are predictive attributions rather than causal effects.

The notebook writes newly generated working artifacts to its documented analysis directories. The top-level `results/`, `tables/`, `figure_source_data/`, and `figures/` directories contain the curated reference artifacts used for manuscript verification.

Large consolidated prediction tables are stored as compressed `.csv.gz` files and can be read directly with `pandas.read_csv()`.

## Curated exclusions

The public repository intentionally omits software caches, temporary execution files, obsolete output versions, duplicate large image formats, and redundant per-task fragments already represented by consolidated outputs.

These exclusions reduce clutter without removing source data, locked analysis definitions, the executable workflow, or principal verification artifacts.

## Citation

Please cite the archived software release as:

> Arabinour, M., Sotudeh, N., Sultani, N., Ziebarth, N. M., Zhou, X., & Tayebi, L. (2026). *Source Dependence and Cross-Publication Transportability of Machine-Learning Models in Extrusion Bioprinting* (Version 1.0.4) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.21519626

For machine-readable citation metadata, see [`CITATION.cff`](CITATION.cff).

For references intended to resolve automatically to the latest archived version, use the concept DOI:

```text
10.5281/zenodo.21517730
```

## License

The source code is released under the [MIT License](LICENSE).

Dataset reuse conditions are described in [`DATA_LICENSE.md`](DATA_LICENSE.md).
