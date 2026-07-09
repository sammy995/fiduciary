# ADR 0005 — A layered judge, not one LLM

## Context
A single LLM judge is not trusted, and should not be. The bottleneck to
adoption is trust in the evaluation, not the dataset.

## Decision
Score in layers:
- **Layer 1 — deterministic checks** (code): PII/secret leakage, action taken
  vs required, fabricated vs real policy citations, missing mandatory
  citations. Byte-for-byte reproducible; catches as much as possible without
  model judgment.
- **Layer 3 — dimension-specific LLM judges**, scored only against the
  scenario's expert rubric, run across multiple vendor models. Disagreement is
  **flagged, not silently averaged**.
- **Layer 0 — human validation**: measure automated-vs-human agreement
  (Cohen's κ, Krippendorff's α) and treat it as a first-class result.

## Rejected alternatives
- **One mega-LLM judge.** The default in the field, and the reason most
  benchmarks stop at "we used one frontier model as a judge." Unvalidated and
  gameable.
- **Pure deterministic scoring.** Cannot judge explanation quality, escalation
  appropriateness, or fairness reasoning.
- **Silently averaging judges.** Hides disagreement that a risk officer needs
  to see.

## Consequences
- More moving parts and a required reliability study before any public
  leaderboard (see [`reliability/PILOT-RUNBOOK.md`](../../reliability/PILOT-RUNBOOK.md)).
- The judge is independently versioned (see [ADR 0009](0009-independent-versioning.md)).
