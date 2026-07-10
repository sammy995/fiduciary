"""Evidence lines cite framework mappings only when the crosswalk is reviewed."""
from fiduciary.report import crosswalk_refs, render_model_report
from fiduciary.schemas import (
    DimensionResult, EvidenceChain, ModelReport, ScenarioResult,
)

CROSSWALK = {
    "review_status": "reviewed",
    "mappings": {
        "PRIV-C1": {
            "nist_ai_rmf": ["MEASURE 2.10"],
            "iso_42001": ["A.7.2 (data management) [verify]"],
            "eu_ai_act": [],
            "sector": ["GDPR Art. 5(1)(b),(c)"],
            "other": [],
        }
    },
}


def _result_with_evidence() -> tuple[ModelReport, list[ScenarioResult]]:
    evidence = EvidenceChain(
        control_id="PRIV-C1", regulation="GDPR Art. 5(1)(b),(c)",
        risk_level="critical", expected_evidence="refusal", mitigation="DLP")
    dim = DimensionResult(dimension="privacy", score=10.0, evidence=[evidence])
    result = ScenarioResult(scenario_id="W1-PRIV-001", model="m", dimensions=[dim])
    report = ModelReport(model="m", world_version="0.1.0", n_scenarios=1,
                         dimension_scores={"privacy": 10.0}, composite=10.0,
                         flagged_dimensions=[])
    return report, [result]


def test_refs_formatted_from_mapping():
    refs = crosswalk_refs(CROSSWALK, "PRIV-C1")
    assert "NIST AI RMF MEASURE 2.10" in refs
    assert "ISO/IEC 42001 A.7.2" in refs


def test_refs_empty_for_unmapped_control_or_no_crosswalk():
    assert crosswalk_refs(CROSSWALK, "NOPE-C1") == ""
    assert crosswalk_refs(None, "PRIV-C1") == ""


def test_report_includes_refs_when_crosswalk_passed():
    report, results = _result_with_evidence()
    text = render_model_report(report, results, crosswalk=CROSSWALK)
    assert "maps to: NIST AI RMF MEASURE 2.10" in text


def test_report_unchanged_without_crosswalk():
    report, results = _result_with_evidence()
    text = render_model_report(report, results)
    assert "maps to:" not in text
