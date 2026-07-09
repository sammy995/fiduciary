# ADR 0002 — Evaluate inside a simulated organization

## Context
Governance is contextual. "Can I approve this loan?" or "Export every
customer's passport" has no correct answer in a vacuum — only given a customer,
a policy, a regulation, a history, and an escalation path.

## Decision
The unit of evaluation is a **role + task inside a coherent synthetic
organization** (TrustBank), not a standalone prompt. "Correct behavior" must be
*derivable from the world* — a fact a scenario relies on must exist in a policy
section, regulation file, customer record, or the task text.

## Rejected alternatives
- **A prompt list.** Cheap and scalable, but decontextualized: it cannot
  measure escalation, authority limits, prior history, or auditability.
- **Real bank data.** Impossible for legal/privacy reasons and not
  reproducible or shareable.

## Consequences
- Requires building and maintaining a consistent world (a content cost — see
  [ADR 0004](0004-yaml-and-files.md) and the threats-to-validity notes).
- Enables scoring context-dependent, organization-relative behavior no
  prompt-based benchmark can reach.
- The world must be *pinned and versioned* for results to be reproducible.
