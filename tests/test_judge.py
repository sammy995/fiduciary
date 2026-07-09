from fiduciary.judge import build_judge_prompt, extract_json, judge_transcript
from fiduciary.runner import parse_action
from fiduciary.scenarios import load_scenarios
from fiduciary.schemas import Transcript

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


def test_extract_json_repairs_trailing_commas():
    # weaker judge models routinely emit a trailing comma before the closing bracket
    assert extract_json('{"scores": [{"criterion_id": "x", "score": 6},]}') == {
        "scores": [{"criterion_id": "x", "score": 6}]}


def test_repairable_judge_reply_is_scored():
    s = get("W1-PRIV-001")
    t = make_transcript(s, "I refuse. POL-001.\nACTION: refuse")
    scores = judge_transcript(s, t, ["mock:commajudge"], DIM_NAMES)
    assert len(scores) == sum(len(v) for v in s.rubric.values())
    assert all(sc.score == 6 for sc in scores)


def test_broken_judge_reply_is_skipped_not_fatal():
    s = get("W1-PRIV-001")
    t = make_transcript(s, "I refuse. POL-001.\nACTION: refuse")
    # one judge returns garbage, the other is fine — the run must survive and
    # still return the good judge's scores (no exception, no missing crash)
    scores = judge_transcript(s, t, ["mock:brokenjudge", "mock:judge"], DIM_NAMES)
    models = {sc.judge_model for sc in scores}
    assert models == {"mock:judge"}
    assert len(scores) == sum(len(v) for v in s.rubric.values())


def test_judge_transcript_with_mock_judge():
    s = get("W1-PRIV-001")
    t = make_transcript(s, "I refuse. POL-001.\nACTION: refuse")
    scores = judge_transcript(s, t, ["mock:judge"], DIM_NAMES)
    total_criteria = sum(len(v) for v in s.rubric.values())
    assert len(scores) == total_criteria
    assert all(sc.score == 8 and sc.judge_model == "mock:judge" for sc in scores)
    dims = {sc.dimension for sc in scores}
    assert dims == set(s.scored_dimensions)
