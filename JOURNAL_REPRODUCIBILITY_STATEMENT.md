# Journal Reproducibility Statement

This study is a secondary reanalysis of a literature-derived,
multi-publication extrusion-bioprinting dataset. The complete computational
archive contains the original data files, processed datasets, row-lineage
records, feature registries, locked validation splits, preprocessing code,
model specifications, nested cross-validation outputs, publication-level
statistical analyses, hierarchical-model outputs, grouped out-of-fold SHAP
results, sensitivity analyses, classification analyses, figures, tables,
source data, checkpoints, execution logs, and cryptographic manifests.

All validation procedures were designed to separate conventional row-wise
prediction from transportability to publications absent from training.
Preprocessing operations were fitted within training partitions only.
Publication-grouped and leave-one-publication-out designs prevented source
overlap between training and test partitions. Uncertainty was evaluated at
the publication level.

The archive is deterministic and SHA-256 indexed. Packaging did not retrain
models or recompute SHAP values. Every included file was verified directly
from the completed ZIP archive.
