"""Inter-judge agreement for a run directory.

An honest *precursor* to the Layer-0 human study: it measures whether the
multiple judge models agree with EACH OTHER (Cohen's κ, Krippendorff's α),
pooled and per dimension. High inter-judge agreement is necessary but not
sufficient for trust; the human-agreement study (reliability/PILOT-RUNBOOK.md)
remains the keystone. Low inter-judge agreement is already a red flag that the
judges (or rubrics) are too noisy to publish a leaderboard from.

Usage:
    python scripts/inter_judge_agreement.py --run results/<run-id> \
        --judge-a ollama_chat/qwen2.5:7b --judge-b ollama_chat/gemma2:9b
"""
from __future__ import annotations

import argparse
import collections
import glob
import json
from pathlib import Path

from fiduciary.reliability import agreement_metrics

DIMENSIONS = ["privacy", "escalation", "policy_compliance", "fairness"]


def load(run: str, judge_a: str, judge_b: str):
    bykey: dict[str, dict[str, int]] = collections.defaultdict(dict)
    dim_of: dict[str, str] = {}
    for f in glob.glob(f"{run}/judgements/*.json"):
        name = Path(f).name
        cand = name.rsplit("__", 1)[1].removesuffix(".json")
        scen = name.split("__", 1)[0]
        for e in json.loads(Path(f).read_text(encoding="utf-8")):
            k = f"{cand}|{scen}|{e['criterion_id']}"
            bykey[k][e["judge_model"]] = e["score"]
            dim_of[k] = e["dimension"]
    return bykey, dim_of


def metrics_for(keys, bykey, ja, jb):
    both = [k for k in keys if ja in bykey[k] and jb in bykey[k]]
    if not both:
        return None
    human = {k: [bykey[k][ja]] for k in both}
    auto = {k: bykey[k][jb] for k in both}
    return agreement_metrics(human, auto)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--run", required=True)
    p.add_argument("--judge-a", required=True)
    p.add_argument("--judge-b", required=True)
    args = p.parse_args()

    bykey, dim_of = load(args.run, args.judge_a, args.judge_b)
    keys = list(bykey)
    overall = metrics_for(keys, bykey, args.judge_a, args.judge_b)
    print(f"Inter-judge agreement — {args.judge_a} vs {args.judge_b}")
    print(f"overall: n={overall['n']} raw_within_1={overall['raw_within_1']} "
          f"cohen_kappa={overall['cohen_kappa']} krippendorff_alpha={overall['krippendorff_alpha']}")
    for dim in DIMENSIONS:
        m = metrics_for([k for k in keys if dim_of.get(k) == dim], bykey, args.judge_a, args.judge_b)
        if m:
            print(f"  {dim:<20} n={m['n']:<4} raw={m['raw_within_1']:<6} "
                  f"kappa={m['cohen_kappa']:<7} alpha={m['krippendorff_alpha']}")
    print("\nNorms: alpha>=0.80 reliable; 0.667-0.80 tentative; <0.667 not a substitute.")


if __name__ == "__main__":
    main()
