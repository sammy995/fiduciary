# Landscape Review (Phase 1)

Status: IN PROGRESS — complete `landscape.csv` first (one row per benchmark,
all nine columns), prioritizing safety, agent-governance, and
LLM-as-judge-reliability entries, then finish this document.

## Method
One row per serious benchmark (~44 in `landscape.csv`). Columns follow
docs/02-landscape-and-gap.md. Sources: original papers/repos only; no
secondary summaries for the "judge_method" and "context_aware" columns.

## Findings by family
(For each family — knowledge/reasoning, software/agents, general evaluation,
safety/red-team, bias/fairness, compliance/policy, domain-specific
finance/legal/medical, judge-reliability — 2–4 sentences: what the family
measures, its strongest entries, and why it does not answer the
deployment-readiness question.)

## Nearest neighbors
(The 3–5 closest benchmarks to TrustBench and, for each, the exact reason it
does not occupy the niche: not context-aware, not organization-relative, no
validated judge, no evidence trail. If one DOES occupy the niche, invoke the
"reconsider the domain" criterion in docs/08 — better to learn now.)

## The gap (one paragraph, defensible)
Draft, to be confirmed by the rows above: every surveyed benchmark evaluates
a model in isolation — question in, answer out, judged against a static key.
None simulates a regulated organization and scores context-dependent,
organization-relative behavior (policy, role, authority, escalation,
auditability) with an evaluation methodology whose human-agreement is itself
measured and reported. TrustBench claims exactly that combination: a
synthetic regulated enterprise, agent-as-employee scenarios, and a layered,
human-validated judge with per-failure evidence chains.

## What we borrow
(Named techniques lifted from surveyed work, with attribution: e.g.
agreement metrics from the judge-reliability literature (Cohen's κ,
Krippendorff's α), rubric-anchored judging from MT-Bench, dataset
documentation norms from Datasheets for Datasets.)
