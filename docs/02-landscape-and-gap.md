# 02 — Landscape and the Gap

Before building anything, be able to say precisely where this sits and why it isn't a duplicate. "Benchmark" is one of the most crowded words in AI. There are hundreds. The contribution has to be stated as an exact gap.

## The landscape, grouped by what it measures

| Family | Examples | Measures | Relevant weakness for us |
|--------|----------|----------|--------------------------|
| Knowledge / reasoning | MMLU, BIG-bench, GPQA | What the model knows / can reason | No notion of policy, context, or consequence |
| Software / agents | SWE-bench, agent benchmarks | Task completion capability | Capability, not governability |
| General evaluation | HELM | Broad multi-metric model evaluation | Model-centric, not deployment-context-centric |
| Safety / red-team | harm refusal sets, jailbreak suites | Harmful output rates, robustness | Abstract safety, not organizational fitness |
| Bias / fairness | demographic parity sets | Group-level disparities | Usually US-centric, decontextualized, single-attribute |
| Compliance / policy | scattered PII and refusal checks | Binary "did it leak / did it refuse" | Shallow; no evidence trail; no org context |

## The gap being claimed

Everything above evaluates a **model in isolation**. Almost nobody evaluates whether **an AI system is deployable inside a regulated organization** — where the answer depends on policy, role, prior history, jurisdiction, escalation, and auditability.

Stated as a single sentence:

> **TrustBench measures context-dependent, organization-relative deployment readiness, using a simulated regulated enterprise and a validated evaluation methodology — a combination no existing public benchmark provides.**

## The Phase-1 research task (do this before coding)

Build a landscape spreadsheet. One row per serious benchmark (~40–60 rows). Columns:

`Benchmark | Year | What it measures | Judge method | Dataset style (static/dynamic) | Context-aware? | Enterprise-deployment framing? | Its weakness | What we borrow`

Cover: capability, safety, bias, security/red-team, agents, and any finance/healthcare/legal-specific evals. Read closely: the newer safety and agent-governance work, and any "LLM-as-a-judge reliability" papers — the last group matters most, because our credibility rests on judge reliability.

Deliverable: a **Landscape Review** document. When it's done, the exact contribution is provable, not asserted — which is the difference between "another benchmark" and a citable one.

## Two adjacent bodies of work to mine (not compete with)

- **Governance / risk frameworks** — EU AI Act, NIST AI RMF, ISO/IEC 42001, SR 11-7, GDPR, DORA, OWASP LLM Top 10. These are not benchmarks; they are the **source of ground truth** for what "correct behavior" means. Every scenario should map to a control in one of these.
- **LLM-as-judge reliability literature** — the methodological backbone for [`05-evaluation-framework.md`](05-evaluation-framework.md). Borrow their agreement metrics (Cohen's κ, Krippendorff's α) rather than inventing new ones.
