"""Load and validate scenario files against the world and taxonomy."""
from __future__ import annotations

from pathlib import Path

import yaml

from trustbench.schemas import Customer, Scenario, Taxonomy, World
from trustbench.taxonomy import control_index

CUSTOMER_FIELDS = set(Customer.model_fields)


def load_scenarios(dir_path: str | Path = "data/scenarios/wave1") -> list[Scenario]:
    scenarios: list[Scenario] = []
    for path in sorted(Path(dir_path).glob("*.yaml")):
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
        scenario = Scenario.model_validate(raw)
        if path.stem != scenario.id:
            raise ValueError(f"filename {path.name} does not match scenario id {scenario.id}")
        scenarios.append(scenario)
    return sorted(scenarios, key=lambda s: s.id)


def _check_disclosure_pattern(pattern: str, world: World) -> str | None:
    if "." not in pattern:
        return f"malformed forbidden_disclosures pattern: {pattern}"
    prefix, field = pattern.split(".", 1)
    if field not in CUSTOMER_FIELDS:
        return f"unknown customer field in pattern {pattern!r}: {field}"
    if prefix != "*" and prefix not in world.customers:
        return f"unknown customer id in pattern {pattern!r}: {prefix}"
    return None


def validate_scenarios(scenarios: list[Scenario], world: World, taxonomy: Taxonomy) -> list[str]:
    problems: list[str] = []
    controls = control_index(taxonomy)
    for s in scenarios:
        loc = s.id
        if s.role not in world.roles:
            problems.append(f"{loc}: unknown role {s.role}")
        if s.customer_id is not None and s.customer_id not in world.customers:
            problems.append(f"{loc}: unknown customer {s.customer_id}")
        for pid in s.policy_ids:
            if pid not in world.policies:
                problems.append(f"{loc}: unknown policy {pid}")
        if s.dimension not in s.scored_dimensions:
            problems.append(f"{loc}: primary dimension not in scored_dimensions")
        if set(s.rubric) != set(s.scored_dimensions):
            problems.append(f"{loc}: rubric keys {sorted(s.rubric)} != scored_dimensions {sorted(s.scored_dimensions)}")
        for criteria in s.rubric.values():
            for c in criteria:
                if not c.id.startswith(f"{s.id}-r"):
                    problems.append(f"{loc}: criterion id {c.id} must start with {s.id}-r")
        for ev in s.evidence:
            if ev.control_id not in controls:
                problems.append(f"{loc}: unknown control {ev.control_id}")
        for pid in s.checks.must_cite_policies:
            if pid not in s.policy_ids:
                problems.append(f"{loc}: must_cite policy {pid} not in policy_ids")
        for pattern in s.checks.forbidden_disclosures:
            problem = _check_disclosure_pattern(pattern, world)
            if problem:
                problems.append(f"{loc}: {problem}")
    return problems
