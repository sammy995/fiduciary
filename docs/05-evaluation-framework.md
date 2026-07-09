# 05 — The Evaluation Framework (the part that earns trust)

This is the hardest and most important part of the project. The dataset is not the bottleneck to adoption — **trust in the evaluation is.** If reviewers, vendors, and regulators don't believe the scoring is fair and reproducible, nothing else matters. So the evaluation methodology is treated as a first-class research result, not plumbing.

**A single LLM judge is never trusted, and shouldn't be.** The design is layered.

## The three (plus one) layers

### Layer 1 — Deterministic checks
Objective, code-verifiable failures. No model judgment involved.
- Did it leak PII / a secret?
- Did it cite a policy that exists, or fabricate one?
- Did it perform an action outside its granted authority?
- Did it escalate when the scenario required a hard escalation?

These are fast, cheap, reproducible, and non-negotiable. Many failures should be caught here.

### Layer 2 — Human-authored rubric
Each scenario ships with an expert-written rubric defining good behavior for **that** scenario, scored per dimension (not one global score). A single response might score:

```
Privacy        9/10
Escalation    10/10
Policy         6/10
Fairness       8/10
Explainability 5/10
```

Per-dimension scoring is richer and more actionable than pass/fail, and it maps straight back to the taxonomy.

### Layer 3 — LLM-as-judge, but plural and specialized
For the qualitative dimensions (explanation quality, reasoning, escalation appropriateness), use models as judges — with three safeguards:
- **Dimension-specific judges**, not one mega-judge. A "Privacy judge," a "Fairness judge," etc., each with a focused rubric.
- **Multiple judge models from different vendors.** Agreement → high confidence. Disagreement → the item is **flagged**, not silently averaged.
- **Judge against the rubric**, never against the judge's free-floating opinion. The rubric anchors the score to the world's ground truth.

### Layer 0 — Human validation (the credibility keystone)
On a representative sample of scenarios, expert humans score independently. Then measure how well the automated stack agrees with them using standard inter-rater metrics:
- **Cohen's κ** (two raters), **Krippendorff's α** (multiple raters), plus raw agreement %.

**Demonstrating high automated-vs-human agreement is the single most important result the project can produce.** In modern evaluation papers, the novelty is often not the dataset but the proof that the evaluation method is reliable. This is the moat and the headline.

## Scoring model

- Every dimension gets a 0–100 score with a visible confidence band.
- A composite **Trust Score** rolls them up, but the composite is always shown **with** its components — never as a bare number, because the components are what a risk officer acts on.
- Every failed test emits the evidence chain from [`03-taxonomy.md`](03-taxonomy.md): `failure → control → risk → regulation → expected evidence → mitigation`.

Example output shape:

```
Deployment Readiness (Banking) — Model X
  Privacy        95  ██████████
  Escalation     88  █████████░
  Policy         76  ████████░░
  Fairness       73  ███████░░░
  Security       84  ████████░░
  ────────────────────────────
  Composite      83   (confidence: high; 2 dimensions flagged for human review)
```

## Reliability research questions (a whole paper lives here)

- Do judges from different vendors agree with expert humans? By how much, per dimension?
- Does multi-judge majority or weighted voting beat any single judge?
- How stable are scores across runs (temperature, ordering, paraphrase)?
- How reproducible is a full evaluation given a pinned world version?

Answering these credibly is what separates this from the large pile of benchmarks that stop at "we used one frontier model as a judge."
