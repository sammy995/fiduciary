# Security & Data Policy

## Synthetic data only

Fiduciary contains **no real personal or financial data**. Every bank,
customer, account number, passport number, policy, and document is synthetic
and fictional. IBANs use the fictional country code `TB`; emails end in
`@example.com` / `@trustbank.example`. If you believe any data resembles a real
individual or institution, open an issue and it will be changed.

## Reporting a vulnerability

If you find a security issue in the harness (e.g. a path-handling or
deserialization flaw), please **do not open a public issue**. Instead, use
GitHub's private vulnerability reporting ("Report a vulnerability" under the
Security tab) or contact the maintainer directly. You will get an
acknowledgement within a few days.

## Scope

Fiduciary evaluates model *behavior*; it is not a production system and stores
no user data. Real model runs require your own provider API keys or a local
model server — keep those keys in your environment (`.env` is gitignored), never
in the repository.
