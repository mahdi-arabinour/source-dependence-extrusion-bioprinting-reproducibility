# Source Dependence and Cross-Publication Transportability in Extrusion Bioprinting

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21517730.svg)](https://doi.org/10.5281/zenodo.21517730)

## Associated article

**Source Dependence and Cross-Publication Transportability of Machine-Learning Models in Extrusion Bioprinting: A Hierarchical Reanalysis of Cell Viability and Filament Geometry**

---

## Repository purpose

This repository accompanies the associated journal article and provides the complete reproducibility package used in the study.

Tagged GitHub releases are automatically archived in Zenodo, ensuring long-term preservation, persistent DOIs, and versioned reproducibility. The repository contains the curated datasets, locked analysis definitions, executable workflow, statistical analyses, model outputs, tables, figure source data, and publication figures required to reproduce the reported results.

---

## Permanent links

**GitHub repository**

https://github.com/mahdi-arabinour/source-dependence-extrusion-bioprinting-reproducibility

**Latest archived Zenodo release (Version 1.0.4)**

https://doi.org/10.5281/zenodo.21519626

**Concept DOI (always resolves to the newest version)**

https://doi.org/10.5281/zenodo.21517730

**Current archived GitHub release**

`v1.0.4`

---

## Start here

1. Read **REPRODUCE.md**.
2. Install the environment using **requirements.txt** or **environment.yml**.
3. Review the immutable literature-derived datasets in `data/raw/`.
4. Review the canonical processed datasets in `data/processed/`.
5. Review the locked configuration files in `config/`.
6. Execute the notebook in `notebooks/`.
7. Compare regenerated outputs with the curated reference outputs in:
   - `results/`
   - `tables/`
   - `figure_source_data/`
   - `figures/`
8. Run

```bash
python scripts/validate_package.py
```

to verify the integrity of the public package.

---

## Repository structure

```
data/
├── raw/                  Immutable source datasets
├── interim/              Registered intermediate datasets
└── processed/            Analysis-ready datasets

config/                   Locked preprocessing and model definitions
src/                      Reusable Python modules
notebooks/                End-to-end analysis notebook
audit/                    Quality-control and validation evidence
results/                  Model outputs and statistical analyses
tables/                   Manuscript and supplementary tables
figure_source_data/       Numerical data underlying figures
figures/                  Final manuscript figures
scripts/                  Validation utilities
```

---

## Reproducibility scope

This repository supports complete reproduction of the published analyses, including

- publication-aware validation,
- grouped cross-validation,
- hierarchical analyses,
- SHAP interpretation,
- sensitivity analyses,
- statistical comparisons,
- manuscript tables,
- publication figures.

Random row-wise validation and publication-grouped validation evaluate different generalization scenarios and should not be interpreted interchangeably.

SHAP values represent predictive feature attributions rather than causal effects.

The notebook generates fresh working outputs while the top-level directories

- `results/`
- `tables/`
- `figure_source_data/`
- `figures/`

contain the curated reference artifacts corresponding to the published manuscript.

Large prediction files are distributed as compressed `.csv.gz` files and can be read directly using `pandas.read_csv()`.

---

## Curated exclusions

To keep the archive concise while preserving reproducibility, the public repository intentionally excludes

- Python cache files,
- temporary execution files,
- obsolete intermediate outputs,
- duplicated image formats,
- redundant task-specific artifacts,
- unnecessary development files.

No source datasets, executable analyses, locked configurations, or published results have been removed.

---

## Citation

If you use this repository, please cite the archived Zenodo software release:

> Arabinour, M., Sotudeh, N., Sultani, N., Ziebarth, N. M., Zhou, X., & Tayebi, L. (2026). *Source Dependence and Cross-Publication Transportability of Machine-Learning Models in Extrusion Bioprinting* (Version 1.0.4) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.21519626

Citation metadata are also provided in **CITATION.cff**.

For citations that should always resolve to the newest archived release, use the **Concept DOI**:

```
10.5281/zenodo.21517730
```

---

## License

The source code is released under the **MIT License**.

Dataset reuse conditions are described in **DATA_LICENSE.md**.
