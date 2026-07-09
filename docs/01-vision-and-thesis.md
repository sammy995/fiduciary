# 01 — Vision and Thesis

## The single sentence

Fiduciary measures whether an AI system can be responsibly deployed inside a regulated enterprise, by observing how it behaves when it acts as an employee inside a realistic simulated organization.

## The decision it helps make

The test of a good benchmark is not "what can I measure?" It is: **"What important deployment decision cannot currently be made with confidence, because there is no accepted way to measure it?"**

The decision here:

> A bank (or insurer, or hospital) wants to deploy an AI assistant or agent into a regulated workflow. Legal, compliance, risk, and security all have to sign off. Today they have no shared, credible measurement to sign off *against*. They rely on vendor claims, ad-hoc red-teaming, and gut feel.

Fiduciary aims to become the measurement they point at. "The model scores X on deployment readiness for regulated banking, and here is the evidence trail for every failure."

## Why "governance" is the right frame — and why it's misunderstood

Governance is **not a capability.** You don't ask "can the model do governance?" the way you ask "can it solve calculus?" Governance is a **property of behavior in context**: does the system stay inside policy, escalate when it should, leave an audit trail, treat people fairly, and recognize the limits of its own authority?

Existing "governance evaluation" is shallow — usually a binary: *did it leak PII? yes/no. did it refuse? yes/no.* Real governance is layered and situational. That shallowness is the opening.

## Thesis (the claim we're staking)

1. The valuable, unclaimed question is **organizational deployment readiness**, not model intelligence or abstract safety.
2. That question can only be answered in **context** — which requires simulating an organization, not listing prompts.
3. The bottleneck to adoption is not the dataset; it is **trust in the evaluation**. Whoever demonstrates a reliable, reproducible, human-validated evaluation methodology owns the space.
4. Domain depth in regulated finance is the moat. The scarce skill is knowing what a bank's compliance, risk, and audit functions actually require — not prompt engineering.

## Who it's for

- **Primary users:** risk, compliance, and AI-governance functions inside regulated organizations who must approve or reject a deployment.
- **Secondary users:** researchers studying enterprise-AI evaluation; vendors who want a credible external readiness score; auditors and regulators looking for a reference method.

## Who it's NOT for

- People choosing a model for general chat, coding, or reasoning quality — that's already well served.
- Teams wanting a pure safety red-team — overlaps but is not the goal.
- Anyone wanting a single global "is this model good" number. The output is deployment-context-specific and evidence-backed, on purpose.

## What success looks like for v1

A credible, public, reproducible artifact that:

- scores several frontier models on banking deployment readiness across a defined set of trust dimensions,
- attaches an auditable evidence trail to every failure (control → risk → regulation → mitigation),
- and reports a measured agreement rate between its automated judges and expert human reviewers.

That artifact simultaneously functions as research (publishable methodology), as a portfolio proof of expertise, and as the seed of a possible product or standard later — without needing to be any of those things to be worth building.
