# Executive Check-in Desk Template

- Status: Proposed; awaiting maintainer review and merge approval
- Date: 2026-09-18
- Authority owner: Mike, Velocity Maintainer
- Mode: Process evolution
- Source: Mike's request to generalize a pattern practiced on a private consuming project
  since 2026-09-14 (there, "CEO Check-in Desk") into a reusable Velocity template.
- Disposition: Velocity repo proposal; branch, commit, and pull request prepared for
  maintainer review; not merged.
- Proposed version: v1.6.0 (minor)

## Change

Add `templates/executive-checkin-desk.md`: a contract plus Markdown skeleton for a living,
ID-tracked page listing everything a project's Operator must decide or do. The contract
requires stable never-renumbered `CK-<n>` IDs, self-contained asks (what it is, options, the
delivery lead's lean, a deadline in the Operator's time zone, and an explicit "if silent"),
four fixed sections (Decide, Do, Already answered, How to reply), header totals, same-turn
republication on any add/answer/close, and delegated rulings recorded as decisions with a
stated default.

Add `templates/executive-checkin-desk.html`: a generic, dependency-free HTML starter with the
same sections, light/dark theming via `prefers-color-scheme`, and placeholder content only —
no project name, no real dates or names, no secrets.

Add a short "Executive Check-in Discipline" section to `docs/PROJECT-ADOPTION-GUIDE.md`
positioning the new template as a companion to the existing Handoff Packet and Review Pack
Template: those carry one piece of work to its next owner or readout; this is the standing,
cross-cutting surface of every open ask to the Operator specifically. Link the template from
`docs/INDEX.md`, next to Handoff Packet and Review Pack Template, and fold it into the
"What Stays In Velocity" template list.

## Why

The failure this template closes: an ask made once, mid-session, and later referred to only
as "the earlier message" — the Operator then has no durable way to find what they ruled, what
is still open, or what happens if they never answer, without searching chat scrollback. This
is the same failure mode `docs/ROLE-AUTHORITY.md` already names for the Coordinator ("must
not bury operator decisions inside long narrative updates"); the difference is that Velocity
had no artifact whose job was specifically to prevent it at the Operator layer. The template
also operationalizes the existing [Criticality Does Not Grant Mutation
Authority](../docs/ROLE-AUTHORITY.md#criticality-does-not-grant-mutation-authority) rule for
delegated calls: a lean is not approval, so every delegated ruling states an explicit
if-silent default rather than treating silence as consent.

## Scope and Authority

- New protected artifacts: `templates/executive-checkin-desk.md`,
  `templates/executive-checkin-desk.html`.
- Other protected-path edits: `docs/INDEX.md` (one new link), `docs/PROJECT-ADOPTION-GUIDE.md`
  (one new section, one bullet-list addition).
- Classification: reusable template support and adoption guidance. No project overlay is
  migrated, no role, approval boundary, or proof obligation changes, and no automation is
  authorized or enabled by this change.
- Authority basis: Mike's direct request, as Velocity Maintainer, to add this artifact to
  Velocity canon. This authorizes preparing the branch and pull request; merge and release
  remain subject to the existing explicit-maintainer-approval rule (see
  `governance/GOVERNANCE.md` Process Change Flow).
- Project-specific or reusable: reusable core template. The template and HTML starter name no
  project, host, command, or environment; the originating consuming project and its
  project-specific name are described only in this proposal's provenance, not in the shipped
  artifacts.
- Compatibility risk: low — purely additive. `templates/` and `docs/` gain new content; no
  existing template, rule, or link is altered in a way that changes its meaning.

## Proof and Disposition

Checked by hand: both new template files use only relative links that resolve within this
repository (`../docs/ROLE-AUTHORITY.md#operator`,
`../docs/ROLE-AUTHORITY.md#coordinator`, `../docs/ROLE-AUTHORITY.md#criticality-does-not-grant-mutation-authority`,
`handoff-packet.md`, `review-pack-template.md`); the HTML starter was read back in full for
placeholder-only content, valid nesting, and light/dark CSS variables with no external
dependency. `docs/INDEX.md` and `docs/PROJECT-ADOPTION-GUIDE.md` were read back to confirm the
new lines match existing list and heading conventions. No secrets, credentials, or
project-identifying data appear in either new template file.

Branch: `docs/executive-checkin-desk`, prepared in an isolated worktree so the maintainer's
main checkout is untouched. Opened as a pull request for review; not merged.
