"""Layer 0: human-validation tooling — rating sheets and agreement metrics."""
from __future__ import annotations

import csv
import json
import random
import statistics
from collections import defaultdict
from pathlib import Path

import krippendorff
from sklearn.metrics import cohen_kappa_score

from fiduciary.runner import _safe_model_name, transcript_path
from fiduciary.scenarios import load_scenarios
from fiduciary.schemas import Transcript

SCENARIO_DIR = "data/scenarios/wave1"


def _judged_scenarios(run_dir: Path, model: str):
    out = []
    for scenario in load_scenarios(SCENARIO_DIR):
        j = run_dir / "judgements" / f"{scenario.id}__{_safe_model_name(model)}.json"
        if j.exists():
            out.append(scenario)
    return out


def export_rating_sheets(run_dir: Path, model: str, out_dir: Path,
                         n_per_dimension: int = 3, seed: int = 42) -> Path:
    rng = random.Random(seed)
    scenarios = _judged_scenarios(run_dir, model)
    by_prefix: dict[str, list] = defaultdict(list)
    for s in scenarios:
        by_prefix[s.id.rsplit("-", 1)[0]].append(s)
    sample = []
    for prefix in sorted(by_prefix):
        pool = by_prefix[prefix]
        rng.shuffle(pool)
        sample.extend(pool[:n_per_dimension])

    responses_dir = out_dir / "responses"
    responses_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for s in sample:
        t = Transcript.model_validate_json(
            transcript_path(run_dir, s.id, model).read_text(encoding="utf-8"))
        (responses_dir / f"{s.id}.txt").write_text(
            f"TASK:\n{t.user_prompt}\n\nEXPECTED (expert rubric context):\n"
            f"{s.expected_behavior}\n\nMODEL RESPONSE:\n{t.response}\n", encoding="utf-8")
        for dim in s.scored_dimensions:
            for c in s.rubric[dim]:
                rows.append({"scenario_id": s.id, "dimension": dim,
                             "criterion_id": c.id, "criterion_text": c.text,
                             "human_score": "", "notes": ""})
    sheet = out_dir / "rating_sheet.csv"
    with sheet.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return sheet


def automated_criterion_means(run_dir: Path, model: str) -> dict[str, float]:
    means: dict[str, float] = {}
    grouped: dict[str, list[int]] = defaultdict(list)
    for path in sorted((run_dir / "judgements").glob(f"*__{_safe_model_name(model)}.json")):
        for entry in json.loads(path.read_text(encoding="utf-8")):
            scenario_id = path.name.split("__")[0]
            grouped[f"{scenario_id}|{entry['criterion_id']}"].append(entry["score"])
    for key, values in grouped.items():
        means[key] = sum(values) / len(values)
    return means


def bin_score(x: float) -> int:
    if x <= 3.5:
        return 0
    if x <= 6.5:
        return 1
    return 2


def agreement_metrics(human: dict[str, list[float]], auto: dict[str, float]) -> dict:
    keys = sorted(set(human) & set(auto))
    human_median = [statistics.median(human[k]) for k in keys]
    auto_vals = [auto[k] for k in keys]

    raw = sum(1 for h, a in zip(human_median, auto_vals) if abs(h - a) <= 1) / len(keys)
    kappa = cohen_kappa_score([bin_score(h) for h in human_median],
                              [bin_score(a) for a in auto_vals])
    if kappa != kappa:  # NaN when both raters constant and equal -> perfect agreement
        kappa = 1.0

    n_raters = max(len(v) for v in human.values())
    matrix = []
    for i in range(n_raters):
        matrix.append([human[k][i] if i < len(human[k]) else float("nan") for k in keys])
    matrix.append(auto_vals)
    alpha = krippendorff.alpha(reliability_data=matrix, level_of_measurement="interval")

    return {"n": len(keys), "raw_within_1": round(raw, 3),
            "cohen_kappa": round(float(kappa), 3),
            "krippendorff_alpha": round(float(alpha), 3)}


def read_rating_csvs(ratings_dir: Path) -> dict[str, list[float]]:
    human: dict[str, list[float]] = defaultdict(list)
    for path in sorted(Path(ratings_dir).glob("*.csv")):
        with path.open(encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row["human_score"].strip():
                    key = f"{row['scenario_id']}|{row['criterion_id']}"
                    human[key].append(float(row["human_score"]))
    return human


def render_reliability_report(metrics: dict, per_dimension: dict[str, dict]) -> str:
    lines = ["# Judge-reliability report", "",
             "| Slice | n | raw_within_1 | cohen_kappa | krippendorff_alpha |",
             "|---|---|---|---|---|",
             f"| overall | {metrics['n']} | {metrics['raw_within_1']} | "
             f"{metrics['cohen_kappa']} | {metrics['krippendorff_alpha']} |"]
    for dim, m in sorted(per_dimension.items()):
        lines.append(f"| {dim} | {m['n']} | {m['raw_within_1']} | "
                     f"{m['cohen_kappa']} | {m['krippendorff_alpha']} |")
    lines += ["", "Interpretation norms: α ≥ 0.80 reliable; 0.667–0.80 tentative; "
              "below 0.667 the automated judge is NOT a substitute for humans "
              "(Krippendorff). κ ≥ 0.6 substantial (Landis & Koch)."]
    return "\n".join(lines) + "\n"
