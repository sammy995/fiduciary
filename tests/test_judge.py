from trustbench.judge import build_judge_prompt, extract_json, judge_transcript
from trustbench.runner import parse_action
from trustbench.scenarios import load_scenarios
from trustbench.schemas import Transcript

DIM_NAMES = {"privacy": "Privacy", "escalation": "Human Oversight / Escalation",
             "policy_compliance": "Policy & Compliance", "fairness": "Fairness (lending)"}


def get(scenario_id: str):
    return next(s for s in load_scenarios("data/scenarios/wave1") if s.id == scenario_id)


def make_transcript(s, response: str) -> Transcript:
    return Transcript(scenario_id=s.id, model="mock:test", world_version="0.1.0",
                      system_prompt="sys", user_prompt=s.task, response=response,
                      declared_action=parse_action(response))


def test_judge_prompt_format():
    s = get("W1-PRIV-001")
    t = make_transcript(s, "I refuse.\nACTION: refuse")
    prompt = build_judge_prompt(s, t, "privacy", "Privacy")
    assert "- [W1-PRIV-001-r1] (weight 3.0)" in prompt
    assert "I refuse." in prompt
    assert "JSON" in prompt
    # criteria from other dimensions must not appear
    assert "W1-PRIV-001-r4" not in prompt


def test_extract_json_tolerates_fences():
    assert extract_json('Here you go:\n```json\n{"scores": []}\n```\nDone.') == {"scores": []}
    assert extract_json('{"a": {"b": 1}} trailing') == {"a": {"b": 1}}


def test_judge_transcript_with_mock_judge():
    s = get("W1-PRIV-001")
    t = make_transcript(s, "I refuse. POL-001.\nACTION: refuse")
    scores = judge_transcript(s, t, ["mock:judge"], DIM_NAMES)
    total_criteria = sum(len(v) for v in s.rubric.values())
    assert len(scores) == total_criteria
    assert all(sc.score == 8 and sc.judge_model == "mock:judge" for sc in scores)
    dims = {sc.dimension for sc in scores}
    assert dims == set(s.scored_dimensions)
