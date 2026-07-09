from edrbench.scenarios import load_scenarios, validate_scenarios
from edrbench.taxonomy import load_taxonomy
from edrbench.world import load_world

EXPECTED_IDS = [
    "W1-ESC-001", "W1-ESC-002", "W1-FAIR-001", "W1-FAIR-002",
    "W1-POL-001", "W1-POL-002", "W1-PRIV-001", "W1-PRIV-002",
]


def test_exemplars_load_and_validate():
    scenarios = load_scenarios("data/scenarios/wave1")
    assert [s.id for s in scenarios] == EXPECTED_IDS
    problems = validate_scenarios(scenarios, load_world("data/world"), load_taxonomy())
    assert problems == [], "\n".join(problems)


def test_every_exemplar_has_checks_and_evidence():
    for s in load_scenarios("data/scenarios/wave1"):
        assert s.checks.required_action is not None, s.id
        assert s.evidence, s.id
        assert s.expected_behavior.strip(), s.id
