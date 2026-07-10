# 10 — Measurement standards

A benchmark is a test instrument. This document states which measurement
standards Fiduciary borrows, what each one demands, and where in the repo
the demand is met. Nothing here claims certification against any of these
standards; they are the discipline, not a badge.

## Validity, structured per the testing Standards

The Standards for Educational and Psychological Testing (AERA, APA, NCME,
2014) treat validity as an argument built from sources of evidence. Mapping
their five sources onto Fiduciary:

| Source of validity evidence | Where Fiduciary addresses it |
|---|---|
| Test content | Every expected behavior must be derivable from a policy, regulation, customer record, or task in the pinned world (docs/04). The taxonomy maps each control to a named framework clause (standards/crosswalk.yaml). |
| Response processes | The ACTION protocol makes the model's chosen action explicit and auditable; transcripts store the full prompt and response. |
| Internal structure | Per-dimension scoring with disagreement flags instead of silent averaging; the planned wrong-action ablation checks whether Layer-1 failures measure governance behavior or protocol formatting. |
| Relations to other variables | Open question. Correlating Fiduciary scores with general-capability benchmarks is future work; divergence is the interesting result. |
| Consequences of testing | Deployment-readiness claims are gated: no public leaderboard until the judge-reliability study clears its threshold (reliability/PILOT-RUNBOOK.md). |

## Reliability

Automated judges are only a substitute for expert humans to the degree that
agreement is measured and reported. Thresholds follow the norms already
used in the code: Krippendorff's alpha at or above 0.80 is reliable,
0.667 to 0.80 is tentative, below 0.667 is not a substitute; Cohen's kappa
read per Landis and Koch. The reliability study is preregistered
(reliability/PREREGISTRATION.md) and its result is a headline output of the
project whether it is positive or negative.

## Uncertainty

Following the spirit of the GUM (JCGM 100:2008): a reported value without
its uncertainty is incomplete. Every dimension score and composite carries
a seeded percentile-bootstrap 95% confidence interval over scenarios
(src/fiduciary/stats.py). Leaderboard differences whose intervals overlap
are not treated as rankings.

## Laboratory discipline, borrowed from ISO/IEC 17025

Three principles are adopted (not certified): documented procedures for
every run (REPRODUCING.md, run_config.json), impartiality rules (judges
from at least two vendors, never judging a sibling model alone,
disagreement flagged), and traceability (the sha256 world manifest pins the
reference material a score was measured against; the VERSIONS.md tuple
makes any two results comparable or explicitly incomparable).

## What is deliberately not claimed

No conformance with any standard named here. No equivalence between
passing scenarios and legal compliance. No generalization beyond the pinned
world and version tuple a result was produced on.
