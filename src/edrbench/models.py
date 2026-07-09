"""Single entry point for all model calls. mock:* models never touch the network."""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

DEFAULT_MOCK_DIR = "tests/fixtures/mock_responses"
CRITERION_RE = re.compile(r"\[([A-Z0-9]+-[A-Z]+-\d+-r\d+)\]")


def _mock(model: str, messages: list[dict], tag: str | None) -> str:
    last = messages[-1]["content"]
    if model == "mock:echo":
        return last
    if model == "mock:judge":
        ids = CRITERION_RE.findall(last)
        scores = [{"criterion_id": i, "score": 8, "rationale": "mock"} for i in ids]
        return json.dumps({"scores": scores})
    if model.startswith("mock:fixture:"):
        variant = model.split(":", 2)[2]
        if tag is None:
            raise ValueError("mock:fixture requires tag=scenario_id")
        root = Path(os.environ.get("EDRBENCH_MOCK_DIR", DEFAULT_MOCK_DIR))
        return (root / variant / f"{tag}.txt").read_text(encoding="utf-8")
    raise ValueError(f"unknown mock model: {model}")


def complete(model: str, messages: list[dict], temperature: float = 0.0,
             tag: str | None = None) -> str:
    if model.startswith("mock:"):
        return _mock(model, messages, tag)
    from litellm import completion  # imported lazily so tests never need it

    resp = completion(model=model, messages=messages,
                      temperature=temperature, num_retries=3)
    return resp.choices[0].message.content
