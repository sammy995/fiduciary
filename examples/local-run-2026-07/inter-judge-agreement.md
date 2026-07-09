# Inter-judge agreement (precursor to the human study)

Do the two judges agree with **each other**? This is a necessary-but-not-
sufficient precursor to the Layer-0 human-agreement keystone
([`../../reliability/PILOT-RUNBOOK.md`](../../reliability/PILOT-RUNBOOK.md)).
Reproduce with:

```bash
python scripts/inter_judge_agreement.py --run results/leaderboard-001 \
  --judge-a ollama_chat/qwen2.5:7b --judge-b ollama_chat/gemma2:9b
```

## Result (qwen2.5:7b vs gemma2:9b, pooled over all 6 candidates)

| Slice | n | raw within ±1 | Cohen κ | Krippendorff α |
|---|---|---|---|---|
| **Overall** | 237 | 0.50 | 0.34 | **0.41** |
| Privacy | 42 | 0.71 | 0.60 | 0.72 |
| Escalation | 69 | 0.39 | 0.28 | 0.40 |
| Policy & Compliance | 92 | 0.44 | 0.26 | 0.23 |
| Fairness | 34 | 0.62 | 0.33 | 0.40 |

Norms (Krippendorff): α ≥ 0.80 reliable · 0.667–0.80 tentative · **< 0.667 not a
substitute**. Cohen's κ ≥ 0.6 substantial (Landis & Koch).

## Reading

- **These two local judges do not agree enough to trust the leaderboard**
  (overall α = 0.41). This is exactly why the example run is labeled a
  demonstration, not a validated ranking.
- **Privacy is the closest to usable** (α = 0.72, κ = 0.60) — its rubric
  criteria are the most concrete/observable ("discloses no account data").
- **Policy, Escalation, and Fairness are unreliable** with these judges — their
  rubrics leave more room for judge interpretation.

## What this points to (before any public leaderboard)

1. **Stronger judges** — re-run with frontier models; local 7–9B judges are too
   noisy for the softer dimensions.
2. **Tighter rubrics** — make Policy / Escalation / Fairness criteria as
   concrete and checkable as the Privacy ones.
3. **More Layer 1** — move what can be deterministic out of LLM judgment.
4. **Then the human study** — inter-judge agreement is not human agreement; the
   κ/α against expert raters remains the keystone.

Full method and decision gate: [`../../reliability/PILOT-RUNBOOK.md`](../../reliability/PILOT-RUNBOOK.md).
