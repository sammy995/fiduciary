"""Render human-readable markdown reports and the leaderboard."""
from __future__ import annotations

from fiduciary.schemas import ModelReport, ScenarioResult

DIM_LABEL = {"privacy": "Privacy", "escalation": "Escalation",
             "policy_compliance": "Policy", "fairness": "Fairness"}


def render_bar(score: float) -> str:
    filled = round(score / 10)
    return "█" * filled + "░" * (10 - filled)


def render_model_report(report: ModelReport, results: list[ScenarioResult]) -> str:
    lines = [
        f"# Deployment Readiness (Banking) — {report.model}",
        "",
        f"World version: `{report.world_version}` · Scenarios: {report.n_scenarios}",
        "",
        "| Dimension | Score | |",
        "|---|---|---|",
    ]
    for dim, score in sorted(report.dimension_scores.items()):
        flag = " ⚑" if dim in report.flagged_dimensions else ""
        lines.append(f"| {DIM_LABEL.get(dim, dim)}{flag} | {score} | `{render_bar(score)}` |")
    lines += ["", f"**Composite: {report.composite}**"
              + (f" — {len(report.flagged_dimensions)} dimension(s) flagged for human review"
                 if report.flagged_dimensions else ""), "", "## Evidence trail", ""]

    any_evidence = False
    for result in results:
        for d in result.dimensions:
            if not d.evidence and not d.layer1_failures:
                continue
            any_evidence = True
            lines.append(f"### {result.scenario_id} — {d.dimension} (score {d.score})")
            for f in d.layer1_failures:
                lines.append(f"- Layer-1 `{f.check}` ({f.severity}): {f.detail}")
            for ev in d.evidence:
                lines.append(
                    f"- Control **{ev.control_id}** → risk **{ev.risk_level}** → "
                    f"{ev.regulation} → expected: {ev.expected_evidence} → "
                    f"mitigation: {ev.mitigation}")
            lines.append("")
    if not any_evidence:
        lines.append("No layer-1 failures — all evidence at judge level.")
    return "\n".join(lines) + "\n"


def render_leaderboard(reports: list[ModelReport]) -> str:
    lines = [
        "# Fiduciary Wave-1 Leaderboard (Banking)",
        "",
        "| Model | Privacy | Escalation | Policy | Fairness | Composite | Flags |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in sorted(reports, key=lambda r: r.composite, reverse=True):
        d = r.dimension_scores
        lines.append(
            f"| {r.model} | {d.get('privacy', '—')} | {d.get('escalation', '—')} | "
            f"{d.get('policy_compliance', '—')} | {d.get('fairness', '—')} | "
            f"**{r.composite}** | {', '.join(r.flagged_dimensions) or '—'} |")
    return "\n".join(lines) + "\n"
