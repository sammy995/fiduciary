# Research workstream (Phase 1 — landscape review)

Canonical artifact: [`landscape.csv`](landscape.csv) (~44 benchmark rows) and
[`landscape-review.md`](landscape-review.md). These get committed and cited.
Zotero + Obsidian are the working layer beneath them.

## Per-paper workflow

1. **Zotero** — collection `TrustBench` with sub-collections mirroring the
   `Research/` folders: Evaluation, Benchmarks, Judge Reliability, Governance,
   Safety, Security, Bias, Statistics, Synthetic Data, Enterprise Architecture,
   Agent Evaluation, Regulation. Save each paper via the browser connector or
   DOI; the Zotero citation key is the paper's stable handle.

2. **Obsidian** — one note per paper, named after the Zotero key. This IS the
   one-page structured review the reading-list plan prescribes:

   ```markdown
   # <Paper title>
   **Zotero key:** <key> · **Year:** · **Family:** (fills a landscape.csv row)
   ## Strengths
   ## Weaknesses
   ## Ideas TrustBench should adopt
   ## Ideas TrustBench should reject
   ## New research questions
   ## Content-idea notes (for the fan-out later)
   ```

3. **Transfer** — after each note, fill that paper's row in `landscape.csv`.
   The CSV is the source of truth; Zotero/Obsidian feed it.

Priority order for filling rows: safety, agent-governance, and
LLM-as-judge-reliability entries first — those are the nearest competitors and
the credibility backbone (docs/02, docs/05).
