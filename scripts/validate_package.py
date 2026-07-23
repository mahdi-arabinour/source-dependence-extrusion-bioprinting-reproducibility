from __future__ import annotations

import csv
import hashlib
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "REPRODUCE.md", "CITATION.cff", "LICENSE",
    "requirements.txt", "environment.yml", "MANIFEST.csv",
    "data/raw", "data/processed", "config", "src", "notebooks",
    "audit", "results", "tables", "figure_source_data", "figures",
]
missing = [p for p in REQUIRED if not (ROOT / p).exists()]
if missing:
    print("Missing required paths:", *missing, sep="\n- ")
    sys.exit(1)

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

with (ROOT / "MANIFEST.csv").open(newline="", encoding="utf-8-sig") as fh:
    rows = list(csv.DictReader(fh))
errors = []
for row in rows:
    path = ROOT / row["relative_path"]
    if not path.is_file():
        errors.append(f"missing: {row['relative_path']}")
    elif sha256(path) != row["sha256"]:
        errors.append(f"checksum mismatch: {row['relative_path']}")
if errors:
    print("Manifest validation failed:", *errors[:20], sep="\n- ")
    sys.exit(1)
print(f"Repository structure and {len(rows)} manifest entries verified.")
