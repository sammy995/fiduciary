"""The crosswalk must cover every wave-1 control and reference only real ones."""
from fiduciary.crosswalk import FRAMEWORK_KEYS, load_crosswalk, validate_crosswalk
from fiduciary.taxonomy import load_taxonomy


def test_crosswalk_loads_with_expected_top_level_keys():
    cw = load_crosswalk()
    assert cw["version"]
    assert cw["review_status"] in ("pending-human-review", "reviewed")
    assert cw["mappings"]


def test_crosswalk_covers_all_wave1_controls():
    assert validate_crosswalk(load_crosswalk(), load_taxonomy()) == []


def test_validator_catches_missing_wave1_control():
    cw = load_crosswalk()
    cw["mappings"].pop("PRIV-C1")
    problems = validate_crosswalk(cw, load_taxonomy())
    assert any("PRIV-C1" in p for p in problems)


def test_validator_catches_unknown_control_id():
    cw = load_crosswalk()
    cw["mappings"]["FAKE-C9"] = {"nist_ai_rmf": ["GOVERN 1.1"]}
    problems = validate_crosswalk(cw, load_taxonomy())
    assert any("FAKE-C9" in p for p in problems)


def test_validator_catches_empty_mapping():
    cw = load_crosswalk()
    cw["mappings"]["PRIV-C1"] = {k: [] for k in FRAMEWORK_KEYS}
    problems = validate_crosswalk(cw, load_taxonomy())
    assert any("maps to nothing" in p for p in problems)


def test_validator_catches_unknown_framework_key():
    cw = load_crosswalk()
    cw["mappings"]["PRIV-C1"] = {"made_up_framework": ["X 1.1"]}
    problems = validate_crosswalk(cw, load_taxonomy())
    assert any("unknown framework key" in p for p in problems)
