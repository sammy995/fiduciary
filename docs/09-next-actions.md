# 09 — Next Actions

Concrete, ordered. The discipline: **no code until the taxonomy and methodology are written down.** The thinking is the asset; the code is the easy part.

## Immediate (this week)

1. **Read these docs end to end** and mark disagreements. This is a design to pressure-test, not a plan to obey.
2. **Lock the two framing decisions** already made: (a) credible public artifact first; (b) banking only, full taxonomy designed, runnable in waves. Confirm they still feel right after reading.
3. **Name it.** EDR-Bench / TrustBank are placeholders. A name that says "deployment readiness for regulated AI" is worth ten minutes.

## Ongoing weekly habit (starts now, never stops)

- **Research networking — 2 hours, every week, no exceptions.** One real conversation with one researcher or practitioner (AI-safety researcher, governance lead, ML-evaluation researcher, responsible-AI PM, bank model-risk leader, open-source maintainer). This is the relationships flywheel ([`../10-public-presence/README.md`](../10-public-presence/README.md)). Over three years it compounds into 150–200 conversations — co-authors, reviewers, advisors, invitations — a network that cannot be replicated later. It costs two hours and starts before any artifact exists.

## Phase 1 — Landscape (the next real work)

4. **Build the landscape spreadsheet** (~40–60 rows) using the columns in [`02-landscape-and-gap.md`](02-landscape-and-gap.md). Prioritize safety, agent-governance, and LLM-as-judge-reliability entries.
5. **Write the 2–3 page landscape review** ending in one paragraph: the exact, defensible gap. If the gap doesn't survive the review, better to learn it now.

## Phase 2 — Taxonomy (first publishable artifact)

6. **Finalize the banking trust taxonomy** from [`03-taxonomy.md`](03-taxonomy.md): for each of the four Wave-1 dimensions, write 3–5 concrete controls, each mapped to a named regulation, each with an example scenario sketch.
7. **Draft Paper 1** ("why enterprise AI needs a deployment-readiness benchmark" + the taxonomy). This can exist before any code.

## De-risking spike (do early, out of order, on purpose)

8. **Run a tiny reliability pilot before scaling anything.** Author ~5 scenarios with rubrics, have 2–3 people (including at least one non-you domain reviewer) score them, run 2 LLM judges, and eyeball agreement. This tests the single make-or-break assumption ([`08-risks-and-kill-criteria.md`](08-risks-and-kill-criteria.md), risk #2) cheaply, before committing to the full build.

## When ready to build (Phase 3+)

9. Stand up **TrustBank v0** — smallest coherent world for Wave-1 dimensions; version it from day one.
10. Author the **Wave-1 scenario + rubric set** (~50–150, quality over count).
11. Build the **layered evaluation harness** and run the **reliability study**.
12. **Publish the first artifact:** taxonomy + methodology + reliability numbers + small leaderboard + full reproduction materials.

## A note on sequencing

Items 4–7 (landscape + taxonomy + Paper 1) and item 8 (the reliability spike) are the highest-leverage next moves. They produce citable output, test the riskiest assumption, and require almost no engineering. Do them before building the world. Everything expensive comes after the cheap things have de-risked it.
