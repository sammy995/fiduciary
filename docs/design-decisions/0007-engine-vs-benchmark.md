# ADR 0007 — Fiduciary is an evaluation engine; banking is instance #1

## Context
The reusable innovation is not the banking scenarios — it is the **method and
machinery** for evaluating an AI acting inside a simulated regulated
organization: a synthetic-world format, a layered judge, evidence-chain
scoring, and a reliability protocol. Banking is one application running on top.

Think of it as an **Enterprise Digital Twin for AI Evaluation**. Only the
synthetic world changes across domains; the engine, methodology, judge, and
scoring are shared.

## Decision
Keep a clean seam between the **engine** (`src/fiduciary/`: runner, layer-1,
judge, aggregate, report, reliability — all domain-agnostic) and the **content**
(`data/`: taxonomy, TrustBank world, scenarios — banking-specific). Nothing in
`src/fiduciary/` hard-codes banking; domain specifics live only in data.

## Rejected alternatives
- **Bake banking into the harness.** Faster now, but forecloses reuse and turns
  a platform into a one-off dataset.
- **Build the multi-domain platform before proving one domain.** Premature
  generality; prove banking end-to-end first (see the milestone below).

## Consequences
- Future domains (healthcare, insurance, government, manufacturing) reuse the
  engine and only add a `data/<domain>/` world + taxonomy + scenarios.
- The engine and the banking benchmark are versioned independently
  (see [ADR 0009](0009-independent-versioning.md)).
- Near-term milestone stays narrow: *one realistic scenario → one model → a
  reproducible score → an inspectable "why".* Everything else is scaling.
