# 06 — Scope and Roadmap

## The scope decision (and the honest tension in it)

Two decisions frame this project:

- **Primary goal:** ship a *credible public artifact fast.*
- **V1 breadth:** *one domain (banking), full 13-dimension taxonomy.*

These pull against each other. "Full 13 dimensions × real judge validation" is a large body of work for a small team, and it fights "ship fast." The reconciliation, baked into the roadmap below:

> **Design all 13 dimensions now** (the taxonomy is cheap and is the intellectual contribution). **Ship the runnable benchmark in waves**, so a credible, defensible artifact exists after Wave 1 and every wave after that just deepens it. Never hold the first public artifact hostage to the full 13.

The number-one way benchmarks die is trying to do everything at once. This sequencing is the guardrail.

## Phases

### Phase 0 — Frame (no code)
Write the one-page vision: mission, the decision it enables, users, non-users, success metric, research questions. Most of this already exists across these docs; consolidate it. **Do not write code yet.**

### Phase 1 — Landscape review
The ~40–60 row benchmark spreadsheet and the written review (see [`02-landscape-and-gap.md`](02-landscape-and-gap.md)). Output: the contribution is *proven* distinct, not asserted.

### Phase 2 — Taxonomy (publishable on its own)
Finalize the dimension/control/test tree for banking with every control mapped to a real framework ([`03-taxonomy.md`](03-taxonomy.md)). This is candidate Paper 1.

### Phase 3 — TrustBank v0
Build the minimum coherent world to support Wave-1 dimensions: Retail + Mortgage, synthetic customers, the policy/document set, and the regulation subset the scenarios cite. Version it.

### Phase 4 — Scenario + rubric set (Wave 1)
Author ~50–150 scenarios across **Privacy, Escalation, Policy & Compliance, Fairness (lending)**, each with a human-authored rubric and the full evidence-chain mapping. Quality over count.

### Phase 5 — Evaluation harness
Implement Layer 1 (deterministic), Layer 2 (rubric application), Layer 3 (multi-judge). Produce per-dimension scores + evidence trails + the composite.

### Phase 6 — Reliability study (the credibility keystone)
Human-validate a representative sample; report κ / α / agreement %. Tune judges until agreement is defensible. This is candidate Paper 2 and the project's headline result.

### Phase 7 — First public artifact
Run several frontier models through Wave 1. Publish: the taxonomy, the methodology, the reliability numbers, a small leaderboard, and everything needed to reproduce it (world version, scenarios, rubrics, harness).

### Phase 8+ — Deepen
Add Waves 2 and 3 dimensions; add the longitudinal scenario track; invite external contributors and reviewers. Only here does "suite" or "product" or "standard" become a live question.

## What ships when (milestone view)

| Milestone | Contains | Doubles as |
|-----------|----------|------------|
| **M1** | Landscape review + Banking trust taxonomy | Paper 1; proof of domain command |
| **M2** | TrustBank v0 + Wave-1 scenarios & rubrics | The dataset artifact |
| **M3** | Evaluation harness + reliability study | Paper 2; the trust keystone |
| **M4** | Public Wave-1 benchmark + leaderboard | The flagship public proof artifact |

M1 alone is a real, citable output. That's the point of the sequencing: value at every step, nothing all-or-nothing.

## Explicit cuts for v1 (YAGNI)

- ❌ Multi-industry suite (healthcare, insurance). Later, only if banking lands.
- ❌ Longitudinal scenarios in Wave 1 (v2 stretch).
- ❌ A hosted API / dashboard product. Later branch.
- ❌ 5,000 scenarios. A curated few-hundred with strong rubrics beats a shallow thousand.
- ❌ Any "industry standard" positioning. Earned, not declared.
