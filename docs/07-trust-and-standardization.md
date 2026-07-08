# 07 — How a Benchmark Becomes Trusted

The most important reframe in this whole project:

> **Benchmarks are social systems disguised as technical systems.** The code is the easy part. The hard part is persuading researchers, vendors, regulators, and enterprises that the benchmark measures something important, scores it fairly, and is governed trustworthily. To do this well, think of yourself as **founding a small institution**, not shipping software. That single reframe changes most design decisions.

## Nobody declares themselves a standard

OWASP, MITRE, NIST, MLCommons — none became standards by announcing it. They became standards because others repeatedly depended on them, over years, because they were transparent, reproducible, and independently governed. Standardization is an **outcome**, not a launch. It is deliberately the *last* item on the roadmap, not the first.

## The trust equation

```
Trust  =  Transparency
        + Reproducibility
        + Independent validation
        + Open governance
        + Adoption over time
```

Note what is **not** in that equation: marketing. Persuasion here comes from method, not messaging.

## Design consequences (bake these in from line one)

- **Open everything** — taxonomy, scenarios, rubrics, harness, judge prompts, results. Versioned and citable.
- **Deterministic where possible** — every objective check reproducible byte-for-byte; every world state pinned to a version.
- **Independent validation** — the human-agreement study ([`05-evaluation-framework.md`](05-evaluation-framework.md)) is the credibility keystone. Without it, trust never forms.
- **Publish before (or alongside) code** — writing the taxonomy and methodology as papers first establishes intellectual ownership and forces rigor. Candidate sequence:
  1. Why enterprise AI needs a deployment-readiness benchmark
  2. The enterprise AI trust taxonomy (banking)
  3. Synthetic-enterprise benchmark design
  4. Judge / evaluation reliability
  5. First results
- **An advisory board, eventually** — not famous names; *competent reviewers*: an AI-safety researcher, a governance expert, a banker, a security person, a lawyer, a statistician, a benchmark methodologist. Their independent scrutiny is what makes external parties trust the scoring.
- **Community mechanics, when there's something to govern** — public repo, issue templates, an RFC process, versioned releases, a contribution path. Premature community is noise; community around a working, validated artifact is how standards begin.

## Where to submit later (only once the artifact is proven)

NIST AI RMF working groups, OWASP, ISO/IEC (42001 ecosystem), MLCommons, Cloud Security Alliance, IAPP, and financial-sector supervisory bodies. These are Phase-8+ moves. Listed here so the long arc is visible — not so it's attempted early.

## The one-line filter for every decision

Before adding a feature, dimension, or claim, ask: **does this increase transparency, reproducibility, independent validation, open governance, or genuine adoption?** If not, it doesn't serve trust, and trust is the actual product.
