"""EDR-Bench command-line interface: validate -> run -> judge -> score -> report."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from edrbench.aggregate import build_model_report, score_scenario
from edrbench.judge import judge_transcript
from edrbench.layer1 import run_layer1
from edrbench.report import render_leaderboard, render_model_report
from edrbench.runner import _safe_model_name, run_scenario, save_transcript, transcript_path
from edrbench.scenarios import load_scenarios, validate_scenarios
from edrbench.schemas import JudgeScore, ModelReport, ScenarioResult, Transcript
from edrbench.taxonomy import load_taxonomy
from edrbench.world import load_world, verify_manifest, write_manifest

WORLD_ROOT = "data/world"
SCENARIO_DIR = "data/scenarios/wave1"


def _select(scenario_dir: str, ids: str | None):
    scenarios = load_scenarios(scenario_dir)
    if ids:
        wanted = set(ids.split(","))
        scenarios = [s for s in scenarios if s.id in wanted]
        missing = wanted - {s.id for s in scenarios}
        if missing:
            raise SystemExit(f"unknown scenario ids: {sorted(missing)}")
    return scenarios


def cmd_validate(_args) -> int:
    world = load_world(WORLD_ROOT)
    problems = validate_scenarios(load_scenarios(SCENARIO_DIR), world, load_taxonomy())
    problems += verify_manifest(WORLD_ROOT)
    for p in problems:
        print(f"PROBLEM: {p}")
    print("OK" if not problems else f"{len(problems)} problem(s)")
    return 1 if problems else 0


def cmd_manifest(_args) -> int:
    print(f"wrote {write_manifest(WORLD_ROOT)}")
    return 0


def cmd_run(args) -> int:
    problems = verify_manifest(WORLD_ROOT)
    if problems:
        for p in problems:
            print(f"MANIFEST: {p}")
        return 1
    world = load_world(WORLD_ROOT)
    run_dir = Path(args.out)
    for scenario in _select(args.scenarios, args.ids):
        transcript = run_scenario(world, scenario, args.model)
        print(f"ran {scenario.id} -> {save_transcript(transcript, run_dir)}")
    (run_dir / "run_config.json").write_text(json.dumps(
        {"model": args.model, "world_version": world.version,
         "scenario_dir": args.scenarios, "ids": args.ids}, indent=2), encoding="utf-8")
    return 0


def cmd_judge(args) -> int:
    run_dir = Path(args.run)
    judges = args.judges.split(",")
    dimension_names = {d.key: d.name for d in load_taxonomy().dimensions}
    out_dir = run_dir / "judgements"
    out_dir.mkdir(parents=True, exist_ok=True)
    for scenario in _select(SCENARIO_DIR, None):
        t_path = transcript_path(run_dir, scenario.id, args.model)
        if not t_path.exists():
            continue
        transcript = Transcript.model_validate_json(t_path.read_text(encoding="utf-8"))
        scores = judge_transcript(scenario, transcript, judges, dimension_names)
        out = out_dir / f"{scenario.id}__{_safe_model_name(args.model)}.json"
        out.write_text(json.dumps([s.model_dump() for s in scores], indent=2), encoding="utf-8")
        print(f"judged {scenario.id} ({len(scores)} criterion scores)")
    return 0


def cmd_score(args) -> int:
    run_dir = Path(args.run)
    world = load_world(WORLD_ROOT)
    results: list[ScenarioResult] = []
    for scenario in _select(SCENARIO_DIR, None):
        t_path = transcript_path(run_dir, scenario.id, args.model)
        j_path = run_dir / "judgements" / f"{scenario.id}__{_safe_model_name(args.model)}.json"
        if not (t_path.exists() and j_path.exists()):
            continue
        transcript = Transcript.model_validate_json(t_path.read_text(encoding="utf-8"))
        judge_scores = [JudgeScore.model_validate(x)
                        for x in json.loads(j_path.read_text(encoding="utf-8"))]
        failures = run_layer1(world, scenario, transcript)
        results.append(score_scenario(scenario, failures, judge_scores, args.model))
    if not results:
        print("nothing to score")
        return 1
    report = build_model_report(results, args.model, world.version)
    scores_dir = run_dir / "scores"
    scores_dir.mkdir(parents=True, exist_ok=True)
    out = scores_dir / f"{_safe_model_name(args.model)}.json"
    out.write_text(json.dumps(
        {"results": [r.model_dump() for r in results],
         "report": report.model_dump()}, indent=2), encoding="utf-8")
    print(f"scored {len(results)} scenarios -> {out}")
    return 0


def cmd_report(args) -> int:
    run_dir = Path(args.run)
    report_dir = run_dir / "report"
    report_dir.mkdir(parents=True, exist_ok=True)
    reports: list[ModelReport] = []
    for path in sorted((run_dir / "scores").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        report = ModelReport.model_validate(data["report"])
        results = [ScenarioResult.model_validate(r) for r in data["results"]]
        (report_dir / f"{path.stem}.md").write_text(
            render_model_report(report, results), encoding="utf-8")
        reports.append(report)
    (report_dir / "leaderboard.md").write_text(render_leaderboard(reports), encoding="utf-8")
    print(f"wrote {len(reports)} report(s) + leaderboard -> {report_dir}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="edrbench")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("validate").set_defaults(fn=cmd_validate)
    sub.add_parser("manifest").set_defaults(fn=cmd_manifest)

    p = sub.add_parser("run")
    p.add_argument("--model", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--scenarios", default=SCENARIO_DIR)
    p.add_argument("--ids", default=None)
    p.set_defaults(fn=cmd_run)

    p = sub.add_parser("judge")
    p.add_argument("--run", required=True)
    p.add_argument("--model", required=True)
    p.add_argument("--judges", required=True)
    p.set_defaults(fn=cmd_judge)

    p = sub.add_parser("score")
    p.add_argument("--run", required=True)
    p.add_argument("--model", required=True)
    p.set_defaults(fn=cmd_score)

    p = sub.add_parser("report")
    p.add_argument("--run", required=True)
    p.set_defaults(fn=cmd_report)

    args = parser.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
