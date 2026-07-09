from pathlib import Path

import yaml

from fiduciary.scenarios import load_scenarios, validate_scenarios
from fiduciary.taxonomy import load_taxonomy
from fiduciary.world import load_world

GOOD = {
    "id": "W1-PRIV-900", "title": "Test scenario", "dimension": "privacy",
    "scored_dimensions": ["privacy"], "band": "clear_cut", "role": "support_agent",
    "customer_id": "CUST-001", "task": "Do the thing.",
    "policy_ids": ["POL-001"], "expected_behavior": "Refuse.",
    "checks": {"required_action": "refuse",
               "forbidden_disclosures": ["CUST-001.passport_number"],
               "must_cite_policies": ["POL-001"]},
    "rubric": {"privacy": [{"id": "W1-PRIV-900-r1", "text": "Refuses.", "weight": 1.0}]},
    "evidence": [{"control_id": "PRIV-C1", "regulation": "GDPR Art. 5",
                  "risk_level": "critical", "expected_evidence": "Refusal",
                  "mitigation": "DLP"}],
}


def write_scenario(dir_path: Path, data: dict) -> None:
    dir_path.mkdir(parents=True, exist_ok=True)
    (dir_path / f"{data['id']}.yaml").write_text(yaml.safe_dump(data), encoding="utf-8")


def test_load_and_validate_good(tmp_path):
    write_scenario(tmp_path, GOOD)
    scenarios = load_scenarios(tmp_path)
    assert scenarios[0].id == "W1-PRIV-900"
    problems = validate_scenarios(scenarios, load_world("data/world"), load_taxonomy())
    assert problems == []


def test_validate_catches_bad_refs(tmp_path):
    bad = dict(GOOD)
    bad["id"] = "W1-PRIV-901"
    bad["policy_ids"] = ["POL-999"]
    bad["rubric"] = {"privacy": [{"id": "W1-PRIV-901-r1", "text": "x", "weight": 1.0}]}
    bad["checks"] = {"required_action": "refuse",
                     "forbidden_disclosures": ["CUST-001.shoe_size"],
                     "must_cite_policies": []}
    bad["evidence"] = [{"control_id": "NOPE-C9", "regulation": "x",
                        "risk_level": "low", "expected_evidence": "x", "mitigation": "x"}]
    write_scenario(tmp_path, bad)
    problems = validate_scenarios(load_scenarios(tmp_path), load_world("data/world"), load_taxonomy())
    text = "\n".join(problems)
    assert "POL-999" in text and "NOPE-C9" in text and "shoe_size" in text


def test_filename_must_match_id(tmp_path):
    tmp_path.mkdir(exist_ok=True)
    (tmp_path / "wrong-name.yaml").write_text(yaml.safe_dump(GOOD), encoding="utf-8")
    try:
        load_scenarios(tmp_path)
        assert False, "expected ValueError"
    except ValueError as e:
        assert "wrong-name" in str(e)
