# Public Standard And ADR Recordkeeping Support

- Status: Prepared for maintainer review
- Date: 2026-09-09
- Authority owner: Mike, Velocity Maintainer
- Mode: Process evolution
- Source: Mike's requests to publish Velocity as an AI-agnostic standard, clean up the repo
  for public visibility, credit Anthropic's ideas, and embed ADR discipline.
- Disposition: Velocity repo proposal; branch/commit/push requested through launch preparation.
- Proposed version: v1.5.0

## Change

Add an optional complete ADR template and connect it to existing architecture review,
authority, invariant enforcement, implementation, and supersession records. Existing ADR
formats remain usable. The change adds recommended recordkeeping support rather than a
new universal requirement or historical migration.

Remove Anthropic's artifact-filename convention from Velocity's adoption guidance and credit
it in the comparison. Keep Velocity's established Capture, Decision, and Tranche vocabulary.
Credit the September automation ideas and the older ADR tradition. Link the public site and
qualify adoption claims as maintainer-reported experience rather than independent validation.

Resolve three existing editorial inconsistencies found during publication review: a proof
mapping comment disagreed with the named-deferral rule, and the role brief overstated both
the index's authority and the scope of production approval phrases.

## Protected Artifacts And Compatibility

- `docs/PROJECT-ADOPTION-GUIDE.md`: recommended ADR support and attribution cleanup.
- `docs/INDEX.md`: discoverability of the new template.
- `templates/architecture-decision-record.md`: optional record format.
- `docs/PROOF-MODEL.md`: remove a contradictory inline comment; preserve the existing rule.
- `templates/role-brief.md`: clarify references to existing project and authority rules.

Classification: reusable template support and explanatory corrections. No project overlay
is migrated. No new role, changed approval boundary, weaker invariant requirement, automatic
acceptance, or live authorization is introduced. Website implementation is a separate
publication project; this repository continues to own the reusable method.

## Publication Review

The repository history scan covered 15 commits and 70 unique historical blobs. Pattern checks
found no private keys, common provider-token formats, credentials in URLs, private network
addresses, or personal filesystem paths. Release notes, issue/PR bodies, and discussion/review
comments were also inspected or pattern-checked. This is a bounded review, not a guarantee
that every possible secret format can be detected. Historical project examples and ordinary
author metadata remain in the public history; no Git history rewrite is proposed.

## Acceptance And Proof

Maintainer acceptance is pending. The operator has authorized public launch and repository
visibility change; this proposal records the separate reusable-artifact review required by
Velocity governance. Verification and the final branch disposition will be recorded with
the maintainer's decision.
