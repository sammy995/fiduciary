# ADR 0004 — Plain versioned files, no database

## Context
Reproducibility and transparency are the product. Reviewers and adopters must
be able to read, diff, cite, and pin every artifact.

## Decision
Store everything as plain UTF-8 files: taxonomy and scenarios in **YAML**,
customers in **JSON**, policies/regulations in **Markdown** (with YAML
front-matter). The world is pinned by a **sha256 manifest** with line endings
normalized so it verifies identically on every OS. No database, no web
framework — files in, files out.

## Rejected alternatives
- **A database.** Opaque to reviewers, not diff-able in a PR, adds
  operational burden, and undermines "read the whole world in a text editor."
- **One giant JSON blob.** Hard to review and merge; scenario-per-file keeps
  diffs and authorship clean.
- **Raw-byte manifest (no newline normalization).** Rejected after it made a
  CRLF working tree disagree with an LF CI checkout — see the fix in
  `src/fiduciary/world.py`.

## Consequences
- Anyone can audit the entire world and every scenario without running code.
- `fiduciary validate` cross-checks every reference and the manifest in CI.
- Large-scale generation (see [ADR 0008](0008-anti-reward-hacking.md)) must emit
  the same file formats.
