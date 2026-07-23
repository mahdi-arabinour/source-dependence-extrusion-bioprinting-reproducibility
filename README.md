# Source Dependence and Cross-Publication Transportability in Extrusion Bioprinting

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21519626.svg)](https://doi.org/10.5281/zenodo.21519626)

## Associated article

**Source Dependence and Cross-Publication Transportability of Machine-Learning Models in Extrusion Bioprinting: A Hierarchical Reanalysis of Cell Viability and Filament Geometry**

## Repository purpose

This repository provides the data, locked analysis definitions, executable workflow, validation outputs, tables, figure source data, and final figures required to reproduce the analyses reported in the associated article.

The current archived release is **v1.0.4**:

https://doi.org/10.5281/zenodo.21519626

## Original data source

This study is a secondary reanalysis of previously published extrusion-bioprinting data.

The original data were published by:

> Tian, S., Stevens, R., McInnes, B. T., & Lewinski, N. A. (2021). Machine Assisted Experimentation of Extrusion-Based Bioprinting Systems. *Micromachines, 12*(7), 780. https://doi.org/10.3390/mi12070780

Original dataset repository:

https://osf.io/97dkx/

Users relying on the original experimental data should cite the Tian et al. publication.

## Permanent links

- **GitHub repository:**  
  https://github.com/mahdi-arabinour/source-dependence-extrusion-bioprinting-reproducibility

- **Archived release, v1.0.4:**  
  https://doi.org/10.5281/zenodo.21519626

- **Concept DOI for all versions:**  
  https://doi.org/10.5281/zenodo.21517730

## Start here

1. Read [`REPRODUCE.md`](REPRODUCE.md).
2. Install the environment from `requirements.txt` or `environment.yml`.
3. Review the source and processed datasets in `data/`.
4. Review the locked analysis settings in `config/`.
5. Run the notebook in `notebooks/`.
6. Compare regenerated outputs with `results/`, `tables/`, `figure_source_data/`, and `figures/`.
7. Validate the package structure:

```bash
python scripts/validate_package.py
