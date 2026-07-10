"""The report command must not emit crosswalk mappings while review is pending,
and must not crash when the crosswalk file is absent. The gate tests stub
load_crosswalk so they hold regardless of the shipped file's review_status."""
import json
from argparse import Namespace

from fiduciary.cli import cmd_report
from fiduciary.schemas import (
    DimensionResult, EvidenceChain, ModelReport, ScenarioResult,
)

STUB_MAPPINGS = {
    "PRIV-C1": {
        "nist_ai_rmf": ["MEASURE 2.10"],
        "iso_42001": [],
        "eu_ai_act": [],
        "sector": ["GDPR Art. 5(1)(b),(c)"],
        "other": [],
    }
}


def _write_scores(run_dir):
    evidence = EvidenceChain(
        control_id="PRIV-C1", regulation="GDPR Art. 5(1)(b),(c)",
        risk_level="critical", expected_evidence="refusal", mitigation="DLP")
    dim = DimensionResult(dimension="privacy", score=10.0, evidence=[evidence])
    result = ScenarioResult(scenario_id="W1-PRIV-001", model="m", dimensions=[dim])
    report = ModelReport(model="m", world_version="0.1.0", n_scenarios=1,
                         dimension_scores={"privacy": 10.0}, composite=10.0,
                         flagged_dimensions=[])
    scores = run_dir / "scores"
    scores.mkdir(parents=True)
    (scores / "m.json").write_text(json.dumps({
        "report": json.loads(report.model_dump_json()),
        "results": [json.loads(result.model_dump_json())],
    }), encoding="utf-8")


def test_pending_crosswalk_never_reaches_reports(tmp_path, monkeypatch):
    _write_scores(tmp_path)
    monkeypatch.setattr("fiduciary.cli.load_crosswalk", lambda: {
        "review_status": "pending-human-review", "mappings": STUB_MAPPINGS})
    assert cmd_report(Namespace(run=str(tmp_path))) == 0
    text = (tmp_path / "report" / "m.md").read_text(encoding="utf-8")
    assert "maps to:" not in text


def test_reviewed_crosswalk_reaches_reports(tmp_path, monkeypatch):
    _write_scores(tmp_path)
    monkeypatch.setattr("fiduciary.cli.load_crosswalk", lambda: {
        "review_status": "reviewed", "mappings": STUB_MAPPINGS})
    assert cmd_report(Namespace(run=str(tmp_path))) == 0
    text = (tmp_path / "report" / "m.md").read_text(encoding="utf-8")
    assert "maps to: NIST AI RMF MEASURE 2.10" in text


def test_missing_crosswalk_file_does_not_crash(tmp_path, monkeypatch):
    _write_scores(tmp_path)
    monkeypatch.chdir(tmp_path)  # no standards/crosswalk.yaml here
    assert cmd_report(Namespace(run=str(tmp_path))) == 0
    text = (tmp_path / "report" / "m.md").read_text(encoding="utf-8")
    assert "maps to:" not in text
