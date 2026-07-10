"""Reports show a confidence interval next to every score that has one."""
from fiduciary.aggregate import build_model_report
from fiduciary.report import render_leaderboard, render_model_report
from fiduciary.schemas import DimensionResult, ModelReport, ScenarioResult


def _results(scores: list[float]) -> list[ScenarioResult]:
    return [
        ScenarioResult(scenario_id=f"W1-PRIV-{i:03d}", model="m",
                       dimensions=[DimensionResult(dimension="privacy", score=s)])
        for i, s in enumerate(scores, start=1)
    ]


def test_build_model_report_populates_cis():
    report = build_model_report(_results([10.0, 30.0, 50.0]), "m", "0.1.0")
    lo, hi = report.dimension_cis["privacy"]
    assert lo <= report.dimension_scores["privacy"] <= hi
    assert report.composite_ci is not None


def test_rendered_report_shows_interval():
    report = build_model_report(_results([10.0, 30.0, 50.0]), "m", "0.1.0")
    text = render_model_report(report, _results([10.0, 30.0, 50.0]))
    assert "95% CI" in text


def test_old_reports_without_cis_still_render():
    old = ModelReport(model="m", world_version="0.1.0", n_scenarios=1,
                      dimension_scores={"privacy": 50.0}, composite=50.0,
                      flagged_dimensions=[])
    text = render_model_report(old, [])
    assert "50.0" in text
    board = render_leaderboard([old])
    assert "50.0" in board
