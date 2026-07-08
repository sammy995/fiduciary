# EDR-Bench — Enterprise Deployment Readiness Benchmark

> **The one question this project answers:**
> *"Can this AI system be trusted to operate inside a regulated enterprise?"*

Not "which model is smartest." Not "which model is safest in the abstract." Frontier labs and academic groups already own those questions (MMLU, HELM, SWE-bench, safety evals). This project owns a different, largely unclaimed question: **deployment readiness inside a regulated organization.**

---

## Why this is different

Almost every benchmark follows: `question → model → answer → correct?`

That works for knowledge. It fails for governance, because governance is **contextual and organizational**. "Can I approve this loan?" has no correct answer in a vacuum. It only has a correct answer given a customer, a policy, a regulation, a history, and an escalation path.

So EDR-Bench does not test a model against trivia. It drops the model into a **simulated regulated enterprise** and makes it act as an employee. Then it judges the behavior against what that enterprise's policies and regulators would actually require.

```text
Synthetic bank  →  policies + customers + data + regulations  →
model acts as employee  →  layered judge scores the behavior  →
Trust Score + evidence trail + deployment verdict
```

## The core bet

Three things, combined, make this novel and defensible:

1. **A synthetic regulated enterprise ("TrustBank")** — a coherent, realistic bank with customers, staff, policies, documents, and regulatory obligations. Not a prompt list; a world.
2. **Agent-as-employee evaluation** — the model is given a role and a task inside that world, so context-dependent judgment can actually be measured.
3. **A layered, validated judge** — deterministic checks + human-authored rubrics + multi-model consensus, with a measured agreement rate against expert humans. The reliability of the *evaluation itself* is treated as a first-class research result, not an afterthought.

The moat is domain depth. Anyone can generate 1,000 prompts. Very few people can encode what a bank's compliance officer, risk manager, and auditor actually require — and that domain knowledge is the differentiator here.

## What version 1 is (decided scope)

- **One domain:** retail + basic commercial banking. One synthetic bank, not a multi-industry suite.
- **Full trust taxonomy designed** for that domain (all 13 dimensions — see [`docs/03-taxonomy.md`](docs/03-taxonomy.md)), but the **runnable benchmark ships in waves** so a credible artifact exists early and deepens over time.
- **Wave 1 runnable dimensions:** Privacy, Human Oversight / Escalation, Policy & Compliance, and Fairness (lending). These are the highest-signal, most measurable, most bank-specific.
- **Output:** a public, reproducible benchmark that scores frontier models, plus a methodology write-up demonstrating judge reliability. This doubles as a credible research + portfolio artifact.

## What this is NOT (v1)

- Not a multi-industry "TrustBench" suite yet.
- Not a model-intelligence leaderboard.
- Not a commercial product yet (that's a later branch, only if the artifact lands).
- Not a claim to be an "industry standard." Standards are earned over years through adoption; see [`docs/07-trust-and-standardization.md`](docs/07-trust-and-standardization.md).

## Repository map

| File | What's in it |
|------|--------------|
| [`docs/01-vision-and-thesis.md`](docs/01-vision-and-thesis.md) | The decision this helps make; the thesis; who it's for and not for |
| [`docs/02-landscape-and-gap.md`](docs/02-landscape-and-gap.md) | The benchmark landscape and the exact gap being claimed |
| [`docs/03-taxonomy.md`](docs/03-taxonomy.md) | The 13-dimension enterprise trust taxonomy for banking |
| [`docs/04-synthetic-enterprise-and-scenarios.md`](docs/04-synthetic-enterprise-and-scenarios.md) | TrustBank (the digital twin) and the scenario engine |
| [`docs/05-evaluation-framework.md`](docs/05-evaluation-framework.md) | The layered judge and how the evaluation earns trust |
| [`docs/06-scope-and-roadmap.md`](docs/06-scope-and-roadmap.md) | Honest phasing; what ships when; what gets cut |
| [`docs/07-trust-and-standardization.md`](docs/07-trust-and-standardization.md) | How a benchmark becomes trusted (and why marketing isn't in that equation) |
| [`docs/08-risks-and-kill-criteria.md`](docs/08-risks-and-kill-criteria.md) | The hard parts, failure modes, and explicit kill/pivot triggers |
| [`docs/09-next-actions.md`](docs/09-next-actions.md) | Concrete next steps, in order |
| [`10-public-presence/`](10-public-presence/README.md) | Parallel workstream: the five flywheels and the research→peer-review→content engine — **staged and gated on the artifact, not before it** |
| [`11-institution/`](11-institution/README.md) | The long-arc institution layer (advisory board, governance, standardization, commercial) — **a deliberately empty gated stub until a proven, adopted artifact exists** |

## Status

**Design phase. No code yet — deliberately.** The intellectual contribution (taxonomy + evaluation methodology) is written down before any implementation, because that is what earns citation and trust. Building starts only after the design is reviewed.

**Working name:** EDR-Bench / TrustBank. Both are provisional — rename freely.
