# Paper 3 — First results and the judge-reliability study

**Status:** outline. Gated on the reliability pilot clearing its decision gate.

## Abstract (to write)
Wave-1 deployment-readiness results for several frontier models, and the
measured agreement between the automated judge stack and expert humans.

## 1. Setup
- Models evaluated; judge configuration (≥2 vendors); pinned version tuple
  (`VERSIONS.md`); reproduction (`REPRODUCING.md`).

## 2. Reliability results (the headline)
- Automated-vs-human agreement per dimension (κ, α, raw); where the judge is and
  is not a substitute for humans. Report negative results too.

## 3. Deployment-readiness results
- Per-dimension scores + composite per model; the leaderboard; representative
  evidence trails.

## 4. Findings
- What separates "looks fine" from "deployable" (e.g. protocol adherence and
  auditability failures a leaderboard-accuracy number hides).

## 5. Public-vs-private gap (when available)
- Overfitting signal from held-out/generated scenarios (ADR 0008).

## 6. Threats to validity & limitations
- External validity; one-world caveat; small human sample
  (`docs/threats-to-validity.md`).

_References: `references/references.bib`._
