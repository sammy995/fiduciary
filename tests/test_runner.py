from pathlib import Path

from fiduciary.runner import build_system_prompt, parse_action, run_scenario, save_transcript, transcript_path
from fiduciary.scenarios import load_scenarios
from fiduciary.world import load_world


def get(scenario_id: str):
    return next(s for s in load_scenarios("data/scenarios/wave1") if s.id == scenario_id)


def test_system_prompt_contains_role_policies_and_action_protocol():
    world = load_world("data/world")
    s = get("W1-PRIV-002")
    prompt = build_system_prompt(world, s)
    assert "Customer Support Agent" in prompt
    assert "POL-001" in prompt and "Purpose limitation" in prompt
    assert "CUST-003" in prompt and "Carmen Ilves" in prompt
    assert "ACTION: answer" in prompt and "ACTION: refuse" in prompt


def test_no_customer_block_when_customer_is_none():
    world = load_world("data/world")
    s = get("W1-PRIV-001")
    assert "Customer record" not in build_system_prompt(world, s)


def test_parse_action():
    assert parse_action("blah\nACTION: refuse") == "refuse"
    assert parse_action("ACTION: escalate\nmore text\naction: ANSWER") == "answer"
    assert parse_action("no action line") is None


def test_run_and_save(tmp_path):
    world = load_world("data/world")
    s = get("W1-PRIV-001")
    t = run_scenario(world, s, "mock:echo")
    assert t.scenario_id == "W1-PRIV-001"
    assert t.world_version == world.version
    assert t.response == s.task  # mock:echo returns the user prompt
    path = save_transcript(t, tmp_path)
    assert path == transcript_path(tmp_path, "W1-PRIV-001", "mock:echo")
    assert path.exists()
