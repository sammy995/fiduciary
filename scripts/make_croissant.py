"""Generate data/croissant.json: Croissant-style metadata for the scenario set.

Structural approximation of the MLCommons Croissant 1.0 format. Before
claiming Croissant conformance anywhere public, a human runs the official
mlcroissant validator against this file (optional dependency, not part of
the test suite).
"""
from __future__ import annotations

import glob
import json

OUT = "data/croissant.json"


def build() -> dict:
    files = sorted(glob.glob("data/scenarios/wave1/*.yaml"))
    return {
        "@context": {
            "@vocab": "https://schema.org/",
            "sc": "https://schema.org/",
            "cr": "http://mlcommons.org/croissant/",
            "fiduciary": "https://github.com/sammy995/fiduciary#",
        },
        "@type": "sc:Dataset",
        "dct:conformsTo": "http://mlcommons.org/croissant/1.0",
        "name": "fiduciary-wave1-scenarios",
        "description": (
            "56 governance scenarios for evaluating AI behavior inside a "
            "synthetic regulated bank: privacy, escalation, policy "
            "compliance, and fairness in lending. Each scenario carries a "
            "rubric and an evidence chain. Synthetic data only."
        ),
        "license": "https://www.apache.org/licenses/LICENSE-2.0",
        "url": "https://github.com/sammy995/fiduciary",
        "version": "1.1.0",
        "citeAs": "See CITATION.cff",
        "fiduciary:scenarioCount": len(files),
        "distribution": [
            {
                "@type": "cr:FileSet",
                "@id": "wave1-scenarios",
                "name": "wave1-scenarios",
                "encodingFormat": "application/x-yaml",
                "includes": "data/scenarios/wave1/*.yaml",
            }
        ],
        "recordSet": [
            {
                "@type": "cr:RecordSet",
                "@id": "scenarios",
                "name": "scenarios",
                "field": [
                    {"@type": "cr:Field", "name": "id", "dataType": "sc:Text"},
                    {"@type": "cr:Field", "name": "dimension", "dataType": "sc:Text"},
                    {"@type": "cr:Field", "name": "band", "dataType": "sc:Text"},
                    {"@type": "cr:Field", "name": "role", "dataType": "sc:Text"},
                    {"@type": "cr:Field", "name": "task", "dataType": "sc:Text"},
                    {"@type": "cr:Field", "name": "expected_behavior", "dataType": "sc:Text"},
                ],
            }
        ],
    }


def main() -> None:
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(build(), fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
