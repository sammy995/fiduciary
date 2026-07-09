# Threats to validity

Reviewers will ask these questions. We answer them before they do, and update
this document as the method changes. Structured as construct / internal /
external validity, plus limitations.

## Construct validity — are we measuring "deployment readiness"?

- **The taxonomy is a claim, not ground truth.** The 13 dimensions and their
  controls are an expert model of what regulated deployment requires. They are
  mapped to real frameworks (GDPR, EU AI Act, SR 11-7, PCI-DSS, AML, EBA, NIST
  AI RMF, OWASP), but the mapping and the choice of dimensions are themselves
  contestable. *Mitigation:* every control cites a named framework; the taxonomy
  is published for critique independently of the code.
- **Rubric weights encode value judgments.** Criterion weights decide what
  "good" emphasizes. *Mitigation:* weights are visible in each scenario file and
  reviewable; Layer-1 caps keep objective failures dominant regardless of
  weights.
- **"Correct behavior" is author-defined.** *Mitigation:* the world-consistency
  rule forces every expected behavior to be derivable from a policy, regulation,
  customer record, or the task — not from the author's opinion.

## Internal validity — is the score caused by model behavior, not artifacts?

- **Judge bias and self-preference.** An LLM judge may favor a sibling model or
  a verbose style. *Mitigation:* multiple vendors, rubric-anchored scoring,
  disagreement flagged not averaged, and Layer-1 checks that need no judgment.
- **Prompt/format sensitivity.** The required `ACTION:` line and system-prompt
  wording affect outcomes. *Mitigation:* fixed template, temperature 0, and a
  planned robustness/mutation study (see [ADR 0008](design-decisions/0008-anti-reward-hacking.md)).
- **Reproducibility drift.** *Mitigation:* pinned world via sha256 manifest,
  `run_config.json` per run, deterministic Layer 1.

## External validity — do results generalize?

- **One synthetic bank is not every bank.** TrustBank is deliberately small.
  Scores are relative to *this* world and taxonomy version, not a universal
  claim. *Mitigation:* independent versioning (see [ADR 0009](design-decisions/0009-independent-versioning.md));
  results are always reported with the world/scenario/judge versions.
- **Synthetic ≠ real.** A synthetic world may miss the messiness of production.
  *Mitigation:* deepen the world (emails, audit findings, incident reports, risk
  register) so it reads like an actual bank; treat realism as an ongoing goal.
- **Banking-only today.** Generalization to healthcare/insurance/government is a
  hypothesis the engine is built to test, not a proven result.

## Reward-hacking / gaming

- A public set can be trained on. *Mitigation (roadmap):* held-out private
  scenarios, generated scenarios, and a mutation engine; report public-vs-private
  gaps as a finding (see [ADR 0008](design-decisions/0008-anti-reward-hacking.md)).

## Limitations (stated plainly)

- Judge-reliability is **not yet measured** on this world; no public leaderboard
  should be published until the pilot clears its decision gate
  ([`reliability/PILOT-RUNBOOK.md`](../reliability/PILOT-RUNBOOK.md)).
- Wave-1 covers 4 of 13 dimensions; longitudinal (stateful, multi-day) scenarios
  are not yet implemented.
- Human validation depends on scarce domain experts; the sample will be small
  and must be reported honestly, including negative results.
