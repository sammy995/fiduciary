# 08 — Risks, Hard Parts, and Kill Criteria

An honest feasibility read. The idea is strong and well-aligned with the creator's regulated-finance and AI-governance background — that background is the moat. But the failure modes are specific and worth naming up front, with explicit triggers to pivot or stop.

## The five hard parts (in order of danger)

### 1. Scope collapse (highest risk)
13 dimensions × many regulations × the temptation of multiple industries = a project that never ships. This is the most common way benchmarks die.
- **Mitigation:** the wave discipline in [`06-scope-and-roadmap.md`](06-scope-and-roadmap.md). Wave 1 is four dimensions, one domain, one world. Everything else is explicitly deferred.
- **Watch for:** "let's just add healthcare / one more dimension before we publish." That sentence is the danger.

### 2. Judge reliability doesn't hold
If automated judges don't agree with expert humans, the whole trust story falls apart — and this is genuinely uncertain until measured.
- **Mitigation:** lean hard on Layer 1 (deterministic) for as much as possible; keep LLM judgment scoped to narrow, well-defined dimensions; flag disagreement instead of averaging it.
- **This is the make-or-break experiment.** Run a small reliability pilot early (a handful of scenarios, a few human raters) *before* scaling scenario authoring.

### 3. Expert-human validation is expensive and slow
The credibility keystone needs real domain experts (compliance, risk, legal, security) to rate scenarios. Access, time, and cost are real constraints for a small team.
- **Mitigation:** keep the validation sample small but representative; recruit a few reviewers rather than a panel; the creator's own domain expertise covers part of the banking rubric authoring.
- **Watch for:** substituting "the model agrees with itself" for real human validation. That's not validation.

### 4. The synthetic world is a content mountain
A coherent bank with consistent customers, policies, documents, and regulation mappings is a lot of careful authoring — and inconsistencies quietly break "ground truth."
- **Mitigation:** smallest coherent world for Wave 1; scripts for data, hand-curation for policies/rubrics; version and consistency-check the world.

### 5. "Standard" is a multi-year social outcome, not a build
Treating standardization as something you ship leads to premature, credibility-damaging claims.
- **Mitigation:** it's the last phase, gated on a proven artifact and adoption. Never positioned as a standard before it is depended upon.

## Kill / pivot criteria (decide these now, honor them later)

- **Pivot the evaluation** if, after a serious reliability pilot, automated-vs-human agreement stays low (e.g., κ well below acceptable norms) across dimensions and can't be lifted by better rubrics or more deterministic checks. The scoring approach — not the whole idea — is what changes.
- **Narrow further** if Wave 1 (four dimensions) can't reach a shippable, reproducible state in the planned window. Cut to two dimensions and still ship.
- **Reconsider the domain** only if the landscape review reveals a credible public benchmark already occupying exactly this niche (context-aware, simulated-enterprise, validated) — unlikely, but that's what Phase 1 checks for.
- **Stop** only if both the taxonomy and the reliability method fail to produce anything citable or reproducible — i.e., neither the intellectual contribution nor the method holds. Given the taxonomy is publishable on its own, this is a low-probability total-loss case.

## The reassuring part

Because value is staged (taxonomy → dataset → method → leaderboard), most failure modes cost a milestone, not the project. Milestone 1 — the landscape review plus the banking trust taxonomy — is a real, citable output even if everything downstream stalls. That staging is the main defense against the risks above.
