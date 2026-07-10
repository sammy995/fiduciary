"""Load and validate the standards crosswalk (standards/crosswalk.yaml)."""
from __future__ import annotations

from pathlib import Path

import yaml

CROSSWALK_PATH = "standards/crosswalk.yaml"
FRAMEWORK_KEYS = ("nist_ai_rmf", "iso_42001", "eu_ai_act", "sector", "other")


def load_crosswalk(path: str = CROSSWALK_PATH) -> dict:
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


def validate_crosswalk(crosswalk: dict, taxonomy) -> list[str]:
    problems: list[str] = []
    mappings = crosswalk.get("mappings") or {}
    wave1_ids = {c.id for d in taxonomy.dimensions if d.wave == 1 for c in d.controls}
    all_ids = {c.id for d in taxonomy.dimensions for c in d.controls}

    for cid in sorted(wave1_ids - set(mappings)):
        problems.append(f"crosswalk: wave-1 control {cid} has no mapping")
    for cid in sorted(set(mappings) - all_ids):
        problems.append(f"crosswalk: mapping references unknown control {cid}")

    for cid, entry in sorted(mappings.items()):
        if not isinstance(entry, dict):
            problems.append(f"crosswalk: {cid} entry is not a mapping")
            continue
        for key in entry:
            if key not in FRAMEWORK_KEYS:
                problems.append(f"crosswalk: {cid} has unknown framework key {key}")
        if not any(entry.get(k) for k in FRAMEWORK_KEYS):
            problems.append(f"crosswalk: {cid} maps to nothing")
    return problems
