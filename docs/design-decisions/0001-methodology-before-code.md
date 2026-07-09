# ADR 0001 — Methodology and taxonomy before code

## Context
Benchmarks are social systems disguised as technical systems. What earns
citation and trust is the *method*, not the implementation. Writing code first
tends to lock in accidental design choices that the methodology never
justified.

## Decision
Write the vision, the trust taxonomy, the synthetic-world design, and the
evaluation methodology **first** (`docs/01`–`docs/09`), then implement. The
repository layout mirrors the methodology, not a web-app skeleton.

## Rejected alternatives
- **Code first, document later.** Fast to start, but the contribution becomes
  "another benchmark repo" with no defensible, citable method.
- **Skip the taxonomy, ship scenarios.** Datasets get stale; a taxonomy becomes
  shared vocabulary others adopt. The taxonomy is the cheaper, more durable
  asset.

## Consequences
- The intellectual contribution exists independently of the code and can be
  published as a paper on its own.
- The code is an *implementation* of the method — see [ADR 0007](0007-engine-vs-benchmark.md).
- Directory names correspond to paper sections (taxonomy, world, scenarios,
  evaluation, reliability, threats-to-validity).
