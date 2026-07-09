# Paper 1 — A deployment-readiness benchmark and trust taxonomy for AI in regulated banking

**Status:** outline. Publishable independently of any code.

## Abstract (to write)
One paragraph: the unclaimed question (organizational deployment readiness), the
taxonomy as the contribution, and why context-dependent evaluation requires a
simulated organization.

## 1. Introduction
- The decision no one can currently make with confidence (docs/01).
- Governance as a property of behavior in context, not a capability.

## 2. Landscape and gap
- The benchmark landscape by family; the exact gap
  (docs/02, `research/landscape.csv`, `research/landscape-review.md`).

## 3. The enterprise trust taxonomy (banking)
- 13 dimensions → controls → tests; every control mapped to a named framework
  (`data/taxonomy.yaml`, docs/03).
- Why banking fairness is not the usual bias test.

## 4. The evidence-chain mapping
- `failure → control → risk → regulation → expected evidence → mitigation`.

## 5. Threats to validity
- Pull from `docs/threats-to-validity.md` (construct validity of the taxonomy).

## 6. Related work / 7. Conclusion
- Position against TrustLLM-style model-centric trustworthiness benchmarks:
  organization-relative, context-dependent, evidence-backed.

_References: `references/references.bib`._
