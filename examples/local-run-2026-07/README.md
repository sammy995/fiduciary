# Example run — local open models (July 2026)

An **illustrative** end-to-end run of Fiduciary Wave-1, to show what the harness
produces. It is **not a validated ranking** — see the caveat below.

## Setup

| | |
|---|---|
| Candidates | `qwen2.5:0.5b`, `gemma3:1b`, `qwen2.5:7b`, `llama3.1:8b`, `gemma2:9b`, `qwen3:14b` (all local via Ollama) |
| Judges | `qwen2.5:7b` + `gemma2:9b` (two families, temperature 0) |
| Scenarios | 12 of 56 — 3 per dimension, mixed difficulty bands |
| Version tuple | engine 0.1.0 · taxonomy 1.0.0 · world 0.1.0 · scenario-set 1.0.0 (subset) · judge 0.1.0 |

## Leaderboard

See [`leaderboard.md`](leaderboard.md). Summary (composite, 0–100):

| Rank | Model | Privacy | Escalation | Policy | Fairness | Composite |
|---|---|---|---|---|---|---|
| 1 | gemma2:9b | 69.0 | 61.1 | 55.4 | 42.7 | **57.0** |
| 2 | qwen3:14b | 50.0 | 70.5 | 59.6 | 25.0 | **51.3** |
| 3 | qwen2.5:7b | 44.3 | 51.9 | 42.2 | 25.0 | **40.8** |
| 4 | llama3.1:8b | 21.7 | 52.4 | 36.2 | 45.7 | **39.0** |
| 5 | gemma3:1b | 10.0 | 48.2 | 15.6 | 46.7 | **30.1** |
| 6 | qwen2.5:0.5b | 8.3 | 33.4 | 31.2 | 25.0 | **24.5** |

## Failure fingerprint (Layer-1, out of 12 scenarios)

| Model | wrong action | PII leak | fabricated policy | missing citation |
|---|---|---|---|---|
| gemma2:9b | 7 | 0 | 0 | 1 |
| qwen3:14b | 8 | 0 | 0 | 0 |
| qwen2.5:7b | 9 | 0 | 0 | 4 |
| llama3.1:8b | 9 | 0 | 0 | 8 |
| gemma3:1b | 10 | 0 | 0 | 10 |
| qwen2.5:0.5b | 8 | 0 | 0 | 10 |

## What it illustrates

- **Taking the wrong governance action (escalate / refuse / answer) is the
  universal weak point — 7–10 of 12 for every model**, including the leader.
  Model size barely moves it.
- **Bigger is not uniformly safer.** `qwen3:14b` cites policy best (0 missing)
  but its **Fairness is capped at 25** — it took a wrong action on a
  fairness-critical scenario. A weaker model beats it on that dimension.
- **No PII leaks and no fabricated policies** were caught at Layer 1 for any
  model on this subset.
- A model can *look* fine (polite refusals) yet fail deployment readiness on
  protocol adherence and auditability — the gap a leaderboard-accuracy number
  hides. See a full evidence trail in [`report-gemma2-9b.md`](report-gemma2-9b.md)
  and [`report-qwen3-14b.md`](report-qwen3-14b.md).

## ⚠️ Why this is not a validated ranking

The judges here are **local open models**, and **no human-agreement study has
been run** for this configuration. Per the project's own gate
([`../../reliability/PILOT-RUNBOOK.md`](../../reliability/PILOT-RUNBOOK.md)), a
leaderboard is only authoritative once the automated judge stack is shown to
agree with expert humans (Cohen's κ, Krippendorff's α) above the decision
threshold. Treat these numbers as a **methodology demonstration**, not a verdict
on any model.

## Reproduce

```bash
IDS=W1-PRIV-001,W1-PRIV-002,W1-PRIV-008,W1-ESC-001,W1-ESC-006,W1-ESC-008,\
W1-POL-001,W1-POL-006,W1-POL-009,W1-FAIR-001,W1-FAIR-002,W1-FAIR-012
for M in ollama_chat/qwen2.5:0.5b ollama_chat/gemma3:1b ollama_chat/qwen2.5:7b \
         ollama_chat/llama3.1:8b ollama_chat/gemma2:9b ollama_chat/qwen3:14b; do
  fiduciary run   --model "$M" --out results/demo --ids "$IDS"
  fiduciary judge --run results/demo --model "$M" --judges ollama_chat/qwen2.5:7b,ollama_chat/gemma2:9b
  fiduciary score --run results/demo --model "$M"
done
fiduciary report --run results/demo
```
