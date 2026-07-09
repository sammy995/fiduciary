import csv
import json
from pathlib import Path

from trustbench.cli import main
from trustbench.reliability import agreement_metrics, automated_criterion_means, bin_score


def test_bin_score():
    assert bin_score(2.0) == 0
    assert bin_score(5.0) == 1
    assert bin_score(9.0) == 2


def test_agreement_metrics_perfect():
    human = {"a|r1": [8.0, 8.0], "a|r2": [3.0, 3.0], "b|r1": [10.0, 10.0]}
    auto = {"a|r1": 8.0, "a|r2": 3.0, "b|r1": 10.0}
    m = agreement_metrics(human, auto)
    assert m["n"] == 3
    assert m["raw_within_1"] == 1.0
    assert m["cohen_kappa"] == 1.0
    assert m["krippendorff_alpha"] > 0.9


def test_agreement_metrics_disagreement():
    human = {"a|r1": [1.0, 2.0], "a|r2": [2.0, 1.0], "b|r1": [9.0, 10.0], "b|r2": [1.0, 1.0]}
    auto = {"a|r1": 9.0, "a|r2": 9.0, "b|r1": 2.0, "b|r2": 9.0}
    m = agreement_metrics(human, auto)
    assert m["raw_within_1"] == 0.0
    assert m["cohen_kappa"] <= 0.0


def test_export_and_compute_roundtrip(tmp_path):
    run = tmp_path / "run"
    model = "mock:fixture:good"
    main(["run", "--model", model, "--out", str(run), "--ids", "W1-PRIV-001,W1-PRIV-002"])
    main(["judge", "--run", str(run), "--model", model, "--judges", "mock:judge"])

    sheets = tmp_path / "sheets"
    assert main(["reliability-export", "--run", str(run), "--model", model,
                 "--out", str(sheets), "--n", "3"]) == 0
    sheet = sheets / "rating_sheet.csv"
    rows = list(csv.DictReader(sheet.open(encoding="utf-8")))
    assert rows and all(r["human_score"] == "" for r in rows)
    assert (sheets / "responses" / "W1-PRIV-001.txt").exists()

    # simulate a human rater who mostly agrees with the mock judge (8s) but
    # scores one criterion lower, so the value domain has >1 distinct value
    # (required by krippendorff.alpha).
    ratings = tmp_path / "ratings"
    ratings.mkdir()
    with (ratings / "rater1.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        for i, r in enumerate(rows):
            r["human_score"] = "3" if i == 0 else "8"
            w.writerow(r)

    assert main(["reliability-compute", "--run", str(run), "--model", model,
                 "--ratings", str(ratings)]) == 0
    report = (run / "reliability_report.md").read_text(encoding="utf-8")
    assert "raw_within_1" in report and "cohen_kappa" in report


def test_automated_means_shape(tmp_path):
    run = tmp_path / "run"
    model = "mock:fixture:good"
    main(["run", "--model", model, "--out", str(run), "--ids", "W1-PRIV-001"])
    main(["judge", "--run", str(run), "--model", model, "--judges", "mock:judge"])
    means = automated_criterion_means(run, model)
    assert means["W1-PRIV-001|W1-PRIV-001-r1"] == 8.0
