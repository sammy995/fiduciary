# Contributing to TrustBench

Thanks for helping build a benchmark serious institutions can trust. TrustBench
is a **social system disguised as a technical system** — its value comes from
transparency, reproducibility, and domain rigor. Contributions are judged
against that bar.

## The most valuable contribution: scenarios

If you have **banking, compliance, risk, audit, or financial-regulation**
experience, authoring scenarios is where you add the most. A scenario drops a
model into a role inside TrustBank and defines what good behavior looks like.

### Anatomy of a scenario

Every scenario lives in [`data/scenarios/wave1/<id>.yaml`](data/scenarios/wave1/)
and must satisfy `trustbench validate`. Use an existing exemplar
(`W1-PRIV-001`, `W1-ESC-002`, `W1-FAIR-002`) as your template. Hard rules:

1. **Filename equals `id`** (`W1-<DIM>-NNN.yaml`), `DIM ∈ PRIV, ESC, POL, FAIR`.
2. **The primary `dimension` is first** in `scored_dimensions`.
3. `rubric` keys **exactly** equal `scored_dimensions`; every criterion id
   starts with `<scenario-id>-r`.
4. Every `evidence[].control_id` exists in [`data/taxonomy.yaml`](data/taxonomy.yaml).
5. `checks.must_cite_policies` ⊆ `policy_ids`; `forbidden_disclosures` patterns
   reference real `Customer` fields (`*.field` or `CUST-ID.field`).
6. **World-consistency rule:** every fact a scenario relies on must exist in a
   policy section, a regulation file, a customer record, or the task text. The
   "correct" behavior must be *derivable from the world*, never from opinion.
7. Set `required_action` (`answer` / `escalate` / `refuse`) so Layer 1 can score
   it deterministically.

Run `trustbench validate` — a green "OK" is required before you open a PR.

## Development setup

```bash
python -m venv .venv && source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
python -m pytest        # must be green (offline, no API keys)
trustbench validate     # world + taxonomy + scenarios + manifest
```

If you change anything under `data/world/`, regenerate the manifest and commit
it (a pinned world is what makes results reproducible):

```bash
python -c "from trustbench.world import write_manifest; write_manifest('data/world')"
```

## Code contributions

- **Test-first.** Every behavior change ships with a test; CI runs the full
  suite offline.
- Keep new files focused and match the surrounding style. No new heavy runtime
  dependencies without discussion.
- Model calls go through `trustbench.models.complete`; keep all tests runnable
  with the `mock:` protocol (no network in CI).

## Judge & methodology changes

The evaluation is the product. Changes to Layer-1 checks, judge prompts, or the
scoring math must explain their effect on reproducibility and, where relevant,
on human-agreement (see [`reliability/PILOT-RUNBOOK.md`](reliability/PILOT-RUNBOOK.md)).
Prefer moving checks *into* Layer 1 (deterministic) over widening LLM judgment.

## Pull requests

1. Branch from `main`.
2. `python -m pytest` and `trustbench validate` both green.
3. Describe *what deployment concern* your change measures or improves.
4. One logical change per PR.

By contributing you agree your work is licensed under [Apache 2.0](LICENSE).
