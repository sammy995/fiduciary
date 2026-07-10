# NeurIPS-style paper checklist, pre-filled from the repository

Fill the remaining items at submission time. "Pointer" names the repo
evidence that answers the question.

| # | Question | Answer | Pointer |
|---|---|---|---|
| 1 | Do the main claims match the paper's scope? | at submission | papers/ outlines fix the claims per paper |
| 2 | Are limitations discussed? | yes | docs/threats-to-validity.md |
| 3 | Theory assumptions and proofs | n/a | no theoretical results |
| 4 | Full disclosure for reproducibility | yes | REPRODUCING.md, VERSIONS.md, run_config.json per run |
| 5 | Open access to data and code | yes | Apache-2.0 repo; DOI per docs/release-checklist.md |
| 6 | Experimental settings specified | yes | temperature 0, judge configuration rules in REPRODUCING.md |
| 7 | Error bars / statistical significance | yes | seeded bootstrap CIs on all scores (src/fiduciary/stats.py) |
| 8 | Compute resources | at submission | record model, provider, token counts per run |
| 9 | Code of ethics conformity | at submission | |
| 10 | Broader impacts | partially | docs/01-vision-and-thesis.md and docs/08-risks-and-kill-criteria.md |
| 11 | Safeguards for misuse | yes | canary GUID; no real personal data (data/DATASHEET.md) |
| 12 | Licenses of used assets | yes | NOTICE, LICENSE |
| 13 | New assets documented | yes | data/DATASHEET.md, data/croissant.json |
| 14 | Crowdsourcing / human subjects | attention | the reliability study uses expert raters; reliability/PREREGISTRATION.md carries the ethics note; check the venue's human-subjects policy before submission |
| 15 | IRB approvals | attention | same as 14; document consent procedure if the venue requires it |
