# ADR 0009 — Version each component independently

## Context
A single `v1 / v2` on the whole repository hides what actually changed. A result
is only comparable to another if the *world*, *scenario set*, *judge*, and
*taxonomy* it ran against are each identified. These evolve at different rates.

## Decision
Version the components independently and record them in
[`VERSIONS.md`](../../VERSIONS.md):

| Component | Meaning |
|---|---|
| Engine (`fiduciary`) | The harness/CLI package version (`pyproject.toml`). |
| Taxonomy | The dimension/control tree (`data/taxonomy.yaml` `version`). |
| World (TrustBank) | Policies, customers, regulations (`data/world/org.yaml` + sha256 manifest). |
| Scenario set | The Wave-1 scenario collection. |
| Judge | Judge prompts + scoring rules. |

Every published run records the tuple of versions it used; `run_config.json`
plus the pinned manifest make a run reproducible.

## Rejected alternatives
- **One repository version.** Cannot tell whether two scores differ because the
  model changed or because the world/judge did.
- **No versioning until v1.0.** Reproducibility must exist from the first
  public number, not be retrofitted.

## Consequences
- Changing the world bumps the world version and the manifest; changing judge
  prompts bumps the judge version — even if the engine package version is
  unchanged.
- Leaderboards must display the version tuple, not just the engine version.
