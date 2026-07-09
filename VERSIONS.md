# Component versions

Fiduciary versions its components independently (see
[ADR 0009](docs/design-decisions/0009-independent-versioning.md)). A result is
only comparable to another when this whole tuple matches. Every published run
records it.

| Component | Version | Source of truth |
|---|---|---|
| Engine (`fiduciary` package) | 0.1.0 | `pyproject.toml` |
| Taxonomy | 1.0.0 | `data/taxonomy.yaml` (`version:`) |
| World (TrustBank) | 0.1.0 | `data/world/org.yaml` + `data/world/manifest.yaml` (sha256) |
| Scenario set (Wave 1) | 1.0.0 | `data/scenarios/wave1/` (56 scenarios) |
| Judge | 0.1.0 | judge prompt + scoring rules in `src/fiduciary/{judge,aggregate}.py` |

## Rules

- Change any world file → bump the World version in `org.yaml` and regenerate
  the manifest.
- Change judge prompts or scoring math → bump the Judge version here and note it
  in `CHANGELOG.md`.
- Add/edit scenarios → bump the Scenario-set version.
- Leaderboards and published scores must display this tuple, not just the engine
  version.
