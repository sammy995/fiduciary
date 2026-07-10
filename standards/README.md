# Standards mappings

This directory maps Fiduciary taxonomy controls to external frameworks. The
mappings are informative. They say which framework clause a control relates
to. They are not a claim that passing the control demonstrates compliance
with that clause, and Fiduciary results are not a certification of anything.

Why the mapping exists: organizations that adopt ISO/IEC 42001, follow the
NIST AI RMF, or fall under the EU AI Act need behavioral evidence about the
AI systems they deploy. The crosswalk lets a Fiduciary evidence trail point
at the framework clause the evidence is relevant to, so a compliance or
audit reader can file it in their own control structure.

Rules:

- `review_status` in `crosswalk.yaml` starts as `pending-human-review`.
  Reports only render crosswalk references once a human with compliance
  knowledge has reviewed every row and set it to `reviewed`.
- Entries marked `verify` cite a standard the maintainers could not check
  against the authoritative text (usually because it is paywalled). They
  must be confirmed before any public publication.
- The crosswalk has its own version, tracked in `VERSIONS.md`. Changing any
  mapping bumps it.
- Empty lists are deliberate. A control with no defensible mapping to a
  framework maps to nothing rather than to a stretched reference.
