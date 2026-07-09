from fiduciary.report import render_bar, render_leaderboard, render_model_report
from fiduciary.schemas import (DimensionResult, EvidenceChain, Layer1Failure,
                              ModelReport, ScenarioResult)


def make_report(model="m1", composite=83.0):
    return ModelReport(model=model, world_version="0.1.0", n_scenarios=2,
                       dimension_scores={"privacy": 95.0, "escalation": 88.0,
                                         "policy_compliance": 76.0, "fairness": 73.0},
                       composite=composite, flagged_dimensions=["fairness"])


def make_results():
    ev = EvidenceChain(control_id="PRIV-C1", regulation="GDPR Art. 5",
                       risk_level="critical", expected_evidence="Refusal",
                       mitigation="DLP filter")
    fail = Layer1Failure(check="pii_leak", severity="critical", detail="leaked CUST-003.iban")
    return [ScenarioResult(scenario_id="W1-PRIV-002", model="m1", dimensions=[
        DimensionResult(dimension="privacy", score=10.0, flagged=True,
                        layer1_failures=[fail], evidence=[ev])])]


def test_render_bar():
    assert render_bar(95.0) == "██████████"
    assert render_bar(73.0) == "███████░░░"
    assert render_bar(0.0) == "░░░░░░░░░░"


def test_model_report_contains_scores_and_evidence():
    text = render_model_report(make_report(), make_results())
    assert "95.0" in text and "privacy" in text
    assert "PRIV-C1" in text and "GDPR Art. 5" in text and "DLP filter" in text
    assert "pii_leak" in text and "W1-PRIV-002" in text


def test_leaderboard_sorted():
    text = render_leaderboard([make_report("weak", 50.0), make_report("strong", 90.0)])
    assert text.index("strong") < text.index("weak")
    assert "Composite" in text
