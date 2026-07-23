# Processed Analysis Data

These files were generated deterministically from the unchanged
supplementary data files stored in `data/raw/`.

## Primary files

- `cell_viability_all_rows.csv`
  - Canonicalized version of all 617 cell-viability observations.

- `cell_viability_primary.csv`
  - Primary deduplicated cell-viability dataset with 608 observations.

- `filament_diameter_all_rows.csv`
  - Canonicalized version of all 339 filament-diameter observations.

- `filament_diameter_primary.csv`
  - Primary deduplicated filament-diameter dataset with 286 observations.

## Important rules

1. No missing values were imputed during dataset construction.
2. Exact duplicate identification was based on the registered original
   data values, before model fitting.
3. Publication identifiers, outcomes, and legacy threshold labels are
   retained for traceability but excluded from locked predictor sets.
4. The filament-to-nozzle ratio is defined as filament diameter divided
   by outer-nozzle inner diameter.
5. The ratio denominator is excluded from all ratio-target predictor sets.
6. Original raw files remain unchanged.
