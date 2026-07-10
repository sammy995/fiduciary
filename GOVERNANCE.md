# Governance

Honest starting point: this is a single-maintainer research project. This
document exists so that the rules are fixed before they are needed, and so
that growth into shared governance has a written path.

## Roles

- Maintainer: merge rights, release rights, final call on method changes.
  Listed in MAINTAINERS.md.
- Scenario reviewers: people with banking, compliance, risk, or audit
  experience who review scenario PRs. Listed in MAINTAINERS.md when
  recruited.
- External advisors: planned; reviewers of the taxonomy and the
  reliability methodology who are not contributors.

## Decision rules

- Changes to scoring math, judge prompts, or the taxonomy require an ADR
  in docs/design-decisions/ and the version bumps defined in VERSIONS.md.
- Scenario additions or edits require the review checklist in
  CONTRIBUTING.md and bump the scenario-set version.
- The reliability decision gate (reliability/PREREGISTRATION.md) cannot be
  weakened after data collection has started. Deviations are documented,
  not silently applied.
- No public leaderboard before the reliability gate clears. This rule is
  not waivable by any single person.

## Conflicts of interest

- Contributors disclose their employer and any model-vendor affiliation in
  the PR that adds them to MAINTAINERS.md.
- Results submitted by a model's own vendor are labeled as such wherever
  they appear.
- Judges never score a sibling model alone (REPRODUCING.md rule).

## Changing this document

By PR, merged by the maintainer, after sitting open for at least seven
days so watchers can object.
