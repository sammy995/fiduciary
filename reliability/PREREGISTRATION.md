# Preregistration: judge-reliability pilot study

This document freezes the hypotheses, design, and decision rules of the
reliability pilot before any data is collected. It follows the intent of
the OSF preregistration practice: committing to the analysis before seeing
the results, so the decision gate cannot drift after the fact. The git tag
`prereg-reliability-v1` marks the frozen version.

## Research question

Does the automated judge stack (Layer 1 deterministic checks plus
multi-model rubric-anchored LLM judges) agree with expert human raters
closely enough to substitute for them when scoring Wave-1 scenarios?

## Hypotheses

- H1: Overall Krippendorff's alpha (interval metric, criterion-level 0 to
  10 scores, human raters vs the automated criterion mean) is at least
  0.667.
- H2: Alpha for the privacy dimension is at least 0.80 (its rubric criteria
  are the most concrete; the July 2026 inter-judge precursor measured 0.72
  between two local judges on privacy).
- H3 (exploratory, no gate): dimensions with more concrete rubric wording
  show higher agreement.

## Design

- Sample: 5 scenarios covering at least 3 dimensions and at least 2
  difficulty bands, chosen before recruitment, for example W1-PRIV-001,
  W1-PRIV-002, W1-ESC-001, W1-POL-001, W1-FAIR-002.
- Candidate transcripts: one real model run per scenario at temperature 0.
- Judges: at least two frontier models from different vendors, temperature
  0. The July 2026 precursor showed local 7B to 9B judges are too noisy
  (overall alpha 0.41); they are excluded.
- Raters: 2 or 3 people; at least one is not a project author and has
  banking, compliance, risk, or audit familiarity. Raters score each
  rubric criterion 0 to 10 using the policy documents as ground truth,
  independently, without conferring.
- Procedure and export format: reliability/PILOT-RUNBOOK.md.

## Metrics

Primary: Krippendorff's alpha (interval) between the human ratings and the
automated criterion means, computed by `fiduciary reliability-compute`.
Secondary: Cohen's kappa on scores binned to fail (0 to 3), partial (4 to
7), pass (8 to 10); raw within-one-point agreement; per-dimension alpha.

## Decision gate (frozen)

- Alpha at or above 0.80 overall: proceed to full Wave-1 runs and the full
  study.
- Alpha 0.667 to 0.80: tighten the weakest-dimension rubrics, move more
  checks into Layer 1, re-run once. Proceed only if the re-run clears.
- Alpha below 0.667 after one improvement iteration: pivot the evaluation
  method. Do not scale scenario authoring. Do not publish scores.

## Reporting commitment

The agreement numbers are published regardless of outcome, including a
negative result, with the same prominence either way. Any deviation from
this preregistration is listed in the eventual write-up under a
"deviations" heading with a reason.

## Ethics note

Raters are adult professionals scoring synthetic transcripts; no personal
data is collected beyond rater initials on rating sheets. If this study is
later submitted to a venue that requires human-subjects review, the
recruitment and consent procedure will be documented before submission.
