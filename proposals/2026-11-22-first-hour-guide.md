# Process Change Proposal — A First-Hour Start Page

- Proposal: add one page that takes a newcomer through a single real change at Delivery scope in
  about an hour, and link it from the README, the docs index, and the adoption guide.
- Status: Proposed; awaiting maintainer review.
- Date: 2026-11-22
- Mode: Process evolution
- Proposed version: 1.12.0 (minor: new guidance)
- Source: the maintainer reported new users interested in Velocity and chose, on 2026-11-22, a
  one-page first-hour guide for people who build software with AI agents, delivered as a pull
  request before the link is shared.
- Triggering evidence: the adoption guide's Delivery scope points a newcomer to five documents and
  three templates before the first change. A 2026-10-04 field scan compared this with a roughly
  40-line orchestration guide that is usable on the first day.
- Affected control plane: Delivery (documentation only).
- Affected protected artifacts: new `docs/FIRST-HOUR.md`; one sentence each in `docs/INDEX.md` and
  `docs/PROJECT-ADOPTION-GUIDE.md`; `README.md`; `CHANGELOG.md`.
- Proposed disposition: Velocity repo proposal; one pull request.
- Authority owner: Mike, Velocity Maintainer.
- Project-specific or reusable: reusable. Names no project, tool, or vendor. The worked example is
  invented.
- Compatibility risk: none. The page restates existing Delivery-scope rules (pin a release, agent
  fragment, a thin overlay, tranche with acceptance criteria and proof mapping, Fixer may propose
  but not apply changes to them, scenario versus mechanism proof, separate acceptance, closeout).
  It adds no rule and changes no template.
- Rollout plan: release with the next minor version; then add the page to the website's
  navigation.

## Checks Against The Canon

Every instruction on the page maps to an existing rule: pinning to
[Pin a Release](../docs/PROJECT-ADOPTION-GUIDE.md#pin-a-release); the overlay lines to
[Overlay Requirements](../docs/PROJECT-ADOPTION-GUIDE.md#overlay-requirements) and the production
approval sentence to [Role Authority](../docs/ROLE-AUTHORITY.md#criticality-does-not-grant-mutation-authority);
the tranche fields, lane, and mode to the [tranche template](../templates/tranche-template.md) and
[Lifecycle Model](../docs/LIFECYCLE-MODEL.md); "propose, never apply" to
[Artifact Authority Boundaries](../docs/ARTIFACT-AUTHORITY-BOUNDARIES.md#rules); proof classes and
the closeout to the [Proof Model](../docs/PROOF-MODEL.md#proof-classes) and the boundaries'
closeout requirement; separate acceptance to
[Scaling The Role Split](../docs/PROJECT-ADOPTION-GUIDE.md#scaling-the-role-split).

## Decision

- Accepted:
- Rejected:
- Deferred:
- Owner: Mike, Velocity Maintainer
- Date:
