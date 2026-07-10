# Reproducing a Fiduciary run

Every published number is reproducible from a pinned world version and this
procedure. If any step's output differs, the run is not comparable — say so.

## Setup
    python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
    pip install -e ".[dev]" -c constraints.txt
    python -m pytest                                    # must be green, fully offline

`constraints.txt` pins the exact dependency versions a published run used;
a constraints file only pins versions, it does not force extra packages
onto other platforms.

## Verify the pinned world
    fiduciary validate
Prints `OK`. This checks scenario cross-references AND that every world file
matches the sha256 manifest (`data/world/manifest.yaml`). A benchmark result
is only meaningful with the world version it ran against (docs/04).

## Run (requires provider API keys in env)
    fiduciary run    --model <candidate> --out results/<run-id>
    fiduciary judge  --run results/<run-id> --model <candidate> --judges <j1>,<j2>[,<j3>]
    fiduciary score  --run results/<run-id> --model <candidate>
    fiduciary report --run results/<run-id>

Rules for comparable runs:
- temperature 0 (hard-coded), judges from >=2 different vendors,
  never judge a model only with itself.
- Record in the run directory: `run_config.json` is written automatically;
  keep it.

## Outputs
- `results/<run-id>/report/<model>.md` — per-dimension scores, flags, and the
  evidence trail for every failure (control -> risk -> regulation -> mitigation).
- `results/<run-id>/report/leaderboard.md` — cross-model table.
- Composite is never published without its components (docs/05).

## Reliability study
Human-agreement procedure and decision gate: `reliability/PILOT-RUNBOOK.md`.
Published scores must link the reliability report of the same judge
configuration.

## Artifact evaluation levels

Mapping to ACM Artifact Review and Badging v1.1 terms, so external
reviewers know what to expect:

- Available: the repository is public under Apache-2.0; releases are
  tagged and archived with a DOI (docs/release-checklist.md).
- Functional: `python -m pytest` runs the full suite offline;
  `fiduciary validate` checks world, taxonomy, scenarios, crosswalk, and
  the sha256 manifest. Both must be green on a fresh clone with
  `pip install -e ".[dev]" -c constraints.txt`.
- Reproduced: rerunning a published configuration (same version tuple,
  same judge models) should reproduce Layer-1 results byte-for-byte;
  judge-level scores can vary with provider-side model updates, which is
  why published numbers carry the judge identity and date, plus bootstrap
  confidence intervals.

Environment capture for a published run:

    python -m pip freeze > results/<run-id>/environment.txt
