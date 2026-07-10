"""Percentile-bootstrap CIs: deterministic for a seed, bracket the mean."""
import pytest

from fiduciary.stats import bootstrap_ci, composite_bootstrap_ci


def test_ci_brackets_the_sample_mean():
    values = [10.0, 20.0, 30.0, 40.0, 50.0]
    lo, hi = bootstrap_ci(values)
    assert lo <= sum(values) / len(values) <= hi


def test_ci_stays_within_data_range():
    values = [10.0, 20.0, 30.0]
    lo, hi = bootstrap_ci(values)
    assert min(values) <= lo <= hi <= max(values)


def test_ci_deterministic_for_a_seed():
    values = [3.0, 7.0, 7.0, 9.0, 12.0, 20.0]
    assert bootstrap_ci(values, seed=1) == bootstrap_ci(values, seed=1)


def test_single_value_is_degenerate():
    assert bootstrap_ci([42.0]) == (42.0, 42.0)


def test_empty_values_raise():
    with pytest.raises(ValueError):
        bootstrap_ci([])


def test_composite_ci_brackets_the_composite():
    by_dim = {"privacy": [10.0, 30.0], "fairness": [50.0, 70.0]}
    composite = (20.0 + 60.0) / 2
    lo, hi = composite_bootstrap_ci(by_dim)
    assert lo <= composite <= hi
