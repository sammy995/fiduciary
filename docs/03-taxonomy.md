# 03 — The Enterprise Trust Taxonomy (Banking)

The taxonomy is the primary intellectual contribution — more than any dataset. Datasets get stale; a good taxonomy becomes the shared vocabulary others adopt. It is also cheap to produce and publishable on its own.

Three levels: **Dimension → Control → Test.**

- **Dimension** — a top-level property of a trustworthy deployed system (the 13 below).
- **Control** — a specific requirement inside a dimension, mapped to a real regulation or framework.
- **Test** — a scenario in TrustBank that exercises that control and produces scorable evidence.

## The 13 dimensions (designed in full for banking)

Wave tags indicate build order (see [`06-scope-and-roadmap.md`](06-scope-and-roadmap.md)); the taxonomy is complete regardless of when each becomes runnable.

| # | Dimension | Core question | Example controls (mapped to real frameworks) | Wave |
|---|-----------|---------------|-----------------------------------------------|------|
| 1 | **Privacy** | Does it protect personal data? | PII recognition, data minimization, redaction, retention, purpose limitation (GDPR Art. 5) | **1** |
| 2 | **Human Oversight / Escalation** | Does it hand off when it should? | Recognize regulated advice, high-risk actions, out-of-authority decisions; escalate instead of answer | **1** |
| 3 | **Policy & Compliance** | Does it stay inside policy and law? | EU AI Act, GDPR, SR 11-7, PCI-DSS, AML/KYC; detect violations and offer compliant alternatives | **1** |
| 4 | **Fairness (lending)** | Does it treat comparable people comparably? | Disparate treatment in credit/mortgage decisions; counterfactual consistency; protected-attribute handling | **1** |
| 5 | **Security** | Can it be turned against the org? | Prompt injection, indirect injection, tool/function abuse, data exfiltration, secret leakage (OWASP LLM Top 10) | 2 |
| 6 | **Safety** | Does it avoid harmful output with calibrated refusal? | Harmful advice, over- vs under-refusal calibration, hallucinated confidence | 2 |
| 7 | **Explainability** | Can it justify a decision? | State reasoning, confidence, limitations, assumptions, evidence, and unknowns | 2 |
| 8 | **Auditability** | Can an auditor reconstruct the decision? | Traceability, citations, version, policy referenced, decision path, prompt history | 2 |
| 9 | **Governance** | Can the system itself be governed? | Intended-use enforcement, out-of-scope detection, documentation/model-card generation, change control | 3 |
| 10 | **Agent Governance** | Are its actions bounded? | Least privilege, tool selection, approval gates, financial limits, identity propagation, recursion limits | 3 |
| 11 | **Robustness** | Does it hold up under messy input? | Typos, noise, code-switching, long context, contradictions, truncation | 3 |
| 12 | **Operational Risk** | Does it fail safely? | Fail-closed behavior, retry/rollback reasoning, drift and abuse detection | 3 |
| 13 | **Deployment Readiness (composite)** | Would legal/risk/security sign off? | Roll-up view that aggregates the above into a go / no-go with evidence | 3 |

## Why fairness here is not the usual bias test

Generic bias tests are US-centric and single-attribute (male/female, black/white, decontextualized). Banking fairness is richer and more useful: **loan, mortgage, credit-limit, fraud-flagging, and account-closure decisions**, across attributes that actually drive regulatory scrutiny — age, nationality, language, disability, socioeconomic status, financial vulnerability. And it is contextual: the "correct" answer depends on the applicant's actual financials, not just their demographic. That contextual, decision-embedded framing is what makes it novel.

## The mapping every test must carry

Each test is only useful if a failure is legible to an enterprise. So every test records:

```
Failure  →  Control violated  →  Risk level  →  Relevant regulation  →  Expected evidence  →  Recommended mitigation
```

Example: a prompt-injection success maps to `OWASP LLM01 → high risk → NIST AI RMF Govern/Map → expected control: input isolation → mitigation: untrusted-content sandboxing`. That chain is what makes the output "gold for enterprises" rather than an academic score.

## Deliverable

A published **Enterprise AI Trust Taxonomy (Banking v1)** — the dimension/control/test tree with every control mapped to a named regulation or framework. This is a standalone artifact and a candidate first paper, independent of any code.
