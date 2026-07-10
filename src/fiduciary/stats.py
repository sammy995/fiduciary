"""Percentile-bootstrap confidence intervals for scores.

Uncertainty is reported alongside every published score (GUM-style
reporting: a result without its uncertainty is incomplete). Plain
random.Random keeps this dependency-free and deterministic per seed.
"""
from __future__ import annotations

import random


def _percentile_interval(sorted_means: list[float], level: float) -> tuple[float, float]:
    n = len(sorted_means)
    lo_idx = int((1 - level) / 2 * n)
    hi_idx = min(n - 1, int((1 + level) / 2 * n) - 1)
    return (round(sorted_means[lo_idx], 1), round(sorted_means[hi_idx], 1))


def bootstrap_ci(values: list[float], n_boot: int = 2000, level: float = 0.95,
                 seed: int = 0) -> tuple[float, float]:
    if not values:
        raise ValueError("bootstrap_ci needs at least one value")
    if len(values) == 1:
        return (round(values[0], 1), round(values[0], 1))
    rng = random.Random(seed)
    n = len(values)
    means = sorted(sum(rng.choices(values, k=n)) / n for _ in range(n_boot))
    return _percentile_interval(means, level)


def composite_bootstrap_ci(scores_by_dim: dict[str, list[float]],
                           n_boot: int = 2000, level: float = 0.95,
                           seed: int = 0) -> tuple[float, float]:
    if not scores_by_dim or not all(scores_by_dim.values()):
        raise ValueError("composite_bootstrap_ci needs non-empty score lists")
    rng = random.Random(seed)
    dims = sorted(scores_by_dim)
    samples = []
    for _ in range(n_boot):
        dim_means = [
            sum(rng.choices(scores_by_dim[d], k=len(scores_by_dim[d]))) / len(scores_by_dim[d])
            for d in dims
        ]
        samples.append(sum(dim_means) / len(dim_means))
    return _percentile_interval(sorted(samples), level)
