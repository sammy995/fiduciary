# Changelog

All notable changes to TrustBench are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] — 2026-07-09

First public research preview.

### Added
- **Trust taxonomy (banking v1):** 13 dimensions, controls mapped to real
  frameworks (GDPR, EU AI Act, SR 11-7, PCI-DSS, AML directives, EBA, NIST AI
  RMF, OWASP LLM Top 10).
- **TrustBank synthetic world:** 5 policies, 6 regulation excerpts, org chart,
  40 synthetic customers (incl. fairness matched-pairs and vulnerability
  markers), pinned by a sha256 manifest.
- **Wave-1 scenario set:** 56 scenarios (14 each across Privacy, Escalation,
  Policy & Compliance, Fairness), each with an expert rubric and evidence chain.
- **Layered evaluation harness:** Layer-1 deterministic checks, Layer-3
  dimension-specific multi-model judges anchored to rubrics, aggregation with
  disagreement flags and per-failure evidence trails.
- **Reliability toolkit:** human rating-sheet export and Cohen's κ /
  Krippendorff's α agreement metrics, with a pilot runbook and decision gate.
- **CLI:** `validate`, `run`, `judge`, `score`, `report`, `reliability-export`,
  `reliability-compute` — fully testable offline via a `mock:` model protocol.
- Phase-1 benchmark landscape (44 rows) and review scaffold.

[0.1.0]: https://github.com/sammy995/trustbench/releases/tag/v0.1.0
