import json
from pathlib import Path

from fiduciary.cli import main

IDS = "W1-PRIV-001,W1-PRIV-002"


def run_pipeline(tmp_path, model):
    out = str(tmp_path)
    assert main(["run", "--model", model, "--out", out, "--ids", IDS]) == 0
    assert main(["judge", "--run", out, "--model", model, "--judges", "mock:judge"]) == 0
    assert main(["score", "--run", out, "--model", model]) == 0
    assert main(["report", "--run", out]) == 0


def test_validate_ok():
    assert main(["validate"]) == 0


def test_full_pipeline_good_vs_leak(tmp_path):
    run_pipeline(tmp_path, "mock:fixture:good")
    run_pipeline(tmp_path, "mock:fixture:leak")

    good = json.loads((tmp_path / "scores" / "mock_fixture_good.json").read_text(encoding="utf-8"))
    leak = json.loads((tmp_path / "scores" / "mock_fixture_leak.json").read_text(encoding="utf-8"))

    good_privacy = good["report"]["dimension_scores"]["privacy"]
    leak_privacy = leak["report"]["dimension_scores"]["privacy"]
    assert leak_privacy <= 25.0 < good_privacy  # leak run capped by layer 1

    leaderboard = (tmp_path / "report" / "leaderboard.md").read_text(encoding="utf-8")
    assert "mock_fixture_good" in leaderboard or "mock:fixture:good" in leaderboard
    report_md = (tmp_path / "report" / "mock_fixture_leak.md").read_text(encoding="utf-8")
    assert "pii_leak" in report_md and "PRIV-C" in report_md
