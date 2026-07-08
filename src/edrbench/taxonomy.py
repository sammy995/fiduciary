"""Load and index the Enterprise AI Trust Taxonomy (Banking v1)."""
from __future__ import annotations

from pathlib import Path

import yaml

from edrbench.schemas import Control, Taxonomy


def load_taxonomy(path: str | Path = "data/taxonomy.yaml") -> Taxonomy:
    raw = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    return Taxonomy.model_validate(raw)


def control_index(tax: Taxonomy) -> dict[str, Control]:
    idx: dict[str, Control] = {}
    for dim in tax.dimensions:
        for control in dim.controls:
            if control.id in idx:
                raise ValueError(f"duplicate control id: {control.id}")
            idx[control.id] = control
    return idx
