# ADR 0008 — Design against benchmark reward-hacking from day one

## Context
Every adopted benchmark is eventually optimized *for*, not *by*. Models (and
vendors) tune to the public set; scores inflate while real deployment readiness
does not. A governance benchmark that can be gamed is worse than none, because
it launders false assurance.

## Decision
Treat the scenario set like a software test suite that must resist overfitting.
The intended structure:

- **Public scenarios** — open, citable, reproducible (what ships today).
- **Held-out private scenarios** — never published; used to detect a model
  that aces the public set but not the private one (the overfitting signal).
- **Generated scenarios** — templated from the world (`role + customer + task +
  policy + expected behavior`) so the space is larger than any memorizable list.
- **A mutation engine** — paraphrase, swap customers, perturb amounts and
  policies, reorder — to test robustness and break memorization.

Report public-vs-private gaps as a first-class result. A large gap is itself a
finding about the model.

## Status
**Roadmap, not yet built.** Today's 56 scenarios are the public set. The
private/generated/mutation tiers are the next methodological investment, ranked
above adding more hand-written public scenarios.

## Rejected alternatives
- **One growing public set.** Simple, but its ceiling is the day a lab decides
  to train on it.
- **Fully generated only.** Loses the hand-curated domain rigor that is the
  moat; generation augments curation, it does not replace it.

## Consequences
- The file formats (see [ADR 0004](0004-yaml-and-files.md)) must support
  programmatic generation and mutation, not just hand-authoring.
- Reliability (see [ADR 0005](0005-layered-judge.md)) must hold on generated
  and mutated items, not only curated ones.
