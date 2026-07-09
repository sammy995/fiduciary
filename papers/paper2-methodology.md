# Paper 2 — Synthetic-enterprise design and a layered, human-validated evaluation method

**Status:** outline.

## Abstract (to write)
The synthetic organization (TrustBank) as a digital twin; the layered judge;
and the claim that the *reliability of the evaluation itself* is a first-class
result.

## 1. Synthetic enterprise design
- TrustBank: policies, customers, regulations, roles (docs/04, `data/world/`).
- The world-consistency rule; pinning and versioning (ADR 0002, ADR 0009).

## 2. Scenario engine
- `role + customer + task + policy + expected behavior + evidence`; difficulty
  bands; the reward-hacking-resistant roadmap (ADR 0008).

## 3. Layered evaluation
- Layer 1 deterministic; Layer 3 dimension-specific multi-model judges; Layer 0
  human validation (docs/05, ADR 0005).

## 4. Scoring
- Weighted rubric scoring, Layer-1 caps, disagreement flags, composite with
  components (ADR 0006).

## 5. Reliability protocol
- Cohen's κ / Krippendorff's α; the pilot and decision gate
  (`reliability/PILOT-RUNBOOK.md`).

## 6. Threats to validity
- Internal validity: judge bias, prompt sensitivity, reproducibility
  (`docs/threats-to-validity.md`).

_References: `references/references.bib`._
