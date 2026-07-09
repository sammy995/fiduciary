from trustbench.scenarios import load_scenarios, validate_scenarios
from trustbench.taxonomy import load_taxonomy
from trustbench.world import load_world


def test_wave1_set_complete_and_valid():
    scenarios = load_scenarios("data/scenarios/wave1")
    assert len(scenarios) == 56
    for dim, prefix in [("privacy", "W1-PRIV"), ("escalation", "W1-ESC"),
                        ("policy_compliance", "W1-POL"), ("fairness", "W1-FAIR")]:
        count = sum(1 for s in scenarios if s.id.startswith(prefix))
        assert count == 14, f"{prefix}: {count}"
    problems = validate_scenarios(scenarios, load_world("data/world"), load_taxonomy())
    assert problems == [], "\n".join(problems)


def test_band_mix():
    scenarios = load_scenarios("data/scenarios/wave1")
    for prefix in ["W1-PRIV", "W1-ESC", "W1-POL", "W1-FAIR"]:
        subset = [s for s in scenarios if s.id.startswith(prefix)]
        bands = [s.band for s in subset]
        assert bands.count("clear_cut") >= 3, prefix
        assert bands.count("governance_loaded") >= 6, prefix
        assert bands.count("conflict") >= 3, prefix


def test_every_exemplar_has_checks_and_evidence():
    for s in load_scenarios("data/scenarios/wave1"):
        assert s.checks.required_action is not None, s.id
        assert s.evidence, s.id
        assert s.expected_behavior.strip(), s.id
