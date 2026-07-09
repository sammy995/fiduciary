# Reproducing a TrustBench run

Every published number is reproducible from a pinned world version and this
procedure. If any step's output differs, the run is not comparable — say so.

## Setup
    python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
    pip install -e ".[dev]"
    python -m pytest                                    # must be green, fully offline

## Verify the pinned world
    trustbench validate
Prints `OK`. This checks scenario cross-references AND that every world file
matches the sha256 manifest (`data/world/manifest.yaml`). A benchmark result
is only meaningful with the world version it ran against (docs/04).

## Run (requires provider API keys in env)
    trustbench run    --model <candidate> --out results/<run-id>
    trustbench judge  --run results/<run-id> --model <candidate> --judges <j1>,<j2>[,<j3>]
    trustbench score  --run results/<run-id> --model <candidate>
    trustbench report --run results/<run-id>

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
