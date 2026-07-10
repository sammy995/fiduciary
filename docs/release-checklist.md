# Release checklist

Order matters: Zenodo archiving hooks the release event, so the webhook
must be on before the tag exists.

Human steps, in order:

1. Confirm `CHANGELOG.md` has a dated section for the release and
   `VERSIONS.md` reflects the component tuple being released.
2. Confirm CI is green on main, including the offline test suite and
   `fiduciary validate`.
3. Log in to zenodo.org with the GitHub account, enable the
   sammy995/fiduciary repository under GitHub integration.
4. Create the git tag (for example `v0.1.0`) and a GitHub release whose
   notes copy the changelog section.
5. Zenodo mints a DOI for the release. Copy the concept DOI (the one that
   always resolves to the latest version).
6. Add the DOI badge to README.md and the `doi` field to CITATION.cff,
   then commit.
7. Register the project at bestpractices.dev (OpenSSF Best Practices
   Badge) and work through its checklist; most items (tests, CI, license,
   contribution policy, versioned releases) already hold.
8. Optional, recommended: add an ORCID iD to CITATION.cff and .zenodo.json.

Standing rules:

- No release while `fiduciary validate` fails or any test is red.
- No leaderboard numbers in release notes until the reliability gate in
  reliability/PREREGISTRATION.md has been cleared and the reliability
  report is linked next to every number.
