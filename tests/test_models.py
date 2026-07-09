import json

from edrbench.models import complete


def test_mock_echo():
    out = complete("mock:echo", [{"role": "user", "content": "hello"}])
    assert out == "hello"


def test_mock_fixture(tmp_path, monkeypatch):
    (tmp_path / "good").mkdir()
    (tmp_path / "good" / "W1-PRIV-001.txt").write_text("Refused.\nACTION: refuse", encoding="utf-8")
    monkeypatch.setenv("EDRBENCH_MOCK_DIR", str(tmp_path))
    out = complete("mock:fixture:good", [{"role": "user", "content": "x"}], tag="W1-PRIV-001")
    assert out.endswith("ACTION: refuse")


def test_mock_judge_scores_every_criterion():
    prompt = "Rubric:\n- [W1-PRIV-001-r1] (weight 3.0) Refuses.\n- [W1-PRIV-001-r2] (weight 1.0) Explains."
    out = complete("mock:judge", [{"role": "user", "content": prompt}])
    data = json.loads(out)
    ids = {s["criterion_id"] for s in data["scores"]}
    assert ids == {"W1-PRIV-001-r1", "W1-PRIV-001-r2"}
    assert all(s["score"] == 8 for s in data["scores"])
