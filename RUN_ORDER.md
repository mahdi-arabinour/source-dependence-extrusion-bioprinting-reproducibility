# Recommended run order

1. Create the Python environment described in `REPRODUCE.md`.
2. Confirm the immutable inputs under `data/raw/`.
3. Review the locked analysis definitions under `config/`.
4. Start Jupyter from the repository root and run the notebook in `notebooks/` from top to bottom.
5. Use modules under `src/` where the notebook imports reusable functions.
6. Compare regenerated results with `results/`, `tables/`, `figure_source_data/`, and `figures/`.
7. Run `python scripts/validate_package.py`.
