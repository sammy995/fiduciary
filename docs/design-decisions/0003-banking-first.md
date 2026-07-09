# ADR 0003 — Banking as the first domain

## Context
Fiduciary is domain-general in principle (see [ADR 0007](0007-engine-vs-benchmark.md)),
but a first instance must be chosen. The scarce, defensible skill is knowing
what a regulated organization's compliance, risk, and audit functions actually
require.

## Decision
Ship **retail + basic commercial banking** first: one synthetic bank
(TrustBank), the four highest-signal dimensions (Privacy, Escalation, Policy &
Compliance, Fairness), and a rich map to real regulation (GDPR, EU AI Act,
SR 11-7, PCI-DSS, AML directives, EBA).

## Rejected alternatives
- **Multi-industry suite from day one** (healthcare + insurance + banking).
  The number-one way benchmarks die is trying to do everything at once.
- **Healthcare first.** Equally regulated, but the author's domain depth is in
  regulated finance — depth is the moat.

## Consequences
- Deferred domains (healthcare, insurance, government) reuse the engine, method,
  judge, and scoring; only the synthetic world changes.
- The banking taxonomy is complete (13 dimensions designed); the *runnable*
  benchmark ships in waves so a credible artifact exists early.
