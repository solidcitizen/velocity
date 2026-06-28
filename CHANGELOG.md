# Changelog

Velocity lifecycle canon. Consuming projects pin to a tagged version (git submodule)
rather than a moving branch. Versions are canon releases, not software:

- **MAJOR** — a change that makes previously-conformant delivery non-conformant
  (a rule is removed, narrowed, or reversed such that prior closeouts must be re-judged).
- **MINOR** — additive doctrine, new templates, or new guidance that does not
  invalidate prior conformance.
- **PATCH** — clarifications, typos, link fixes, non-normative edits.

## [1.2.0] — 2026-06-27

### Added — Criticality Does Not Grant Mutation Authority

Folded into `docs/ROLE-AUTHORITY.md` (its natural home; no new core doc, per the manifesto
anti-direction) plus minimal pointer and template edits. Source: the Nexusplus Sync Records
actionability incident (2026-05-14), where an agent read urgency language (`critical`) as
sufficient authority to dispatch a production promotion workflow after staging proof, without
an explicit production-promotion approval sentence.

- **Core Rule** — `critical`, `urgent`, `prod fix`, `production issue`, `ready`, `ship it`,
  and similar urgency/destination words describe priority and target relevance; they do **not**
  grant authority to mutate production or any protected live environment. The new
  `## Criticality Does Not Grant Mutation Authority` section in `docs/ROLE-AUTHORITY.md`
  enumerates what critical authorizes, what it does not, the explicit operator approval
  sentences that *do* authorize production mutation, and the signals that are **not** sufficient
  (including successful staging proof and prior-tranche approval).
- **Default closeout** — after staging/host-qualified proof, the default state is the
  promotion-readiness disposition (cross-referenced to Branch Hygiene and Lifecycle Model
  `Promotion mode`, not restated): *Ready for production promotion; awaiting explicit operator
  approval.* When capable-but-unapproved, the correct result is the existing `Blocked`
  disposition (reason: missing production-mutation authority), not improvisation.
- **Pointer + obligations** — one new row in the `docs/ARTIFACT-AUTHORITY-BOUNDARIES.md`
  Protected Artifacts table (Production / live-lane mutation → Operator unless delegated);
  `docs/PROJECT-ADOPTION-GUIDE.md` Overlay Requirements now requires the overlay to define the
  exact production-mutation approval phrase(s), including whether `ship it` qualifies.
- **Template block** — a `Promotion Authority` field block (Target live lane / Requested
  mutation / Exact approval sentence / Approved by / Approval timestamp / Commit-ref / Promotion
  mechanism; *"if any field is missing, do not mutate the live lane"*) added to the existing
  `templates/review-pack-template.md`, with the two decisive fields mirrored into
  `templates/handoff-packet.md`. No new template.

### Compatibility

**Additive doctrine (MINOR)**, not a breaking change. Existing canon already required explicit
approval/delegation for production mutation (`ROLE-AUTHORITY` Operator: "production mutation
approval unless explicitly delegated"; `LIFECYCLE-MODEL` `Promotion mode`: "live or higher-lane
mutation has been explicitly approved"; "do not cross from one mode to another implicitly"). Any
closeout that promoted on bare urgency language was already non-conformant under v1.1.0; this
makes that constraint enforceable and adds the explicit-approval-sentence requirement plus the
template block. It invalidates an **informal overlay shorthand** (`critical` / `prod fix` /
`ready` as live-mutation authority), not a Velocity-conformant practice, so it does not trip the
MAJOR re-judge test.

Proposal of record: [`proposals/2026-05-14-critical-does-not-authorize-production.md`](proposals/2026-05-14-critical-does-not-authorize-production.md).

## [1.1.0] — 2026-06-27

### Added — Invariant-Binding Doctrine

Folded into `docs/PROOF-MODEL.md` (its natural home; no new core doc, per the manifesto
anti-direction against growing `docs/` mass) plus two reusable templates. Source: the
Nexusplus integrity pilot (2026-06-26/27), where an audit found 11 load-bearing invariants
stated but unbound and bound them through this discipline.

- **Core Rule** — an invariant is real only if a mechanism enforces it; proof must map to
  every invariant a change *touches*, not only the one the tranche *declared*.
- **Proof Mapping** — narrowed: a load-bearing invariant may no longer close as
  `residual` / `out of scope`; it is bound (with an `Enforcement:` rung + `file:line`) or
  explicitly deferred to a named owner.
- **New `## Invariant Binding` section** — the enforcement ladder
  (`PREVENT > DETECT > RUNTIME_GUARD > HOPE`); loudness-as-binding; Detect-decays /
  Prevent-is-permanent; blast × silence × reversibility triage with a lethal quadrant that
  MUST reach `PREVENT`; sequence-the-lethal-quadrant-first; seam invariants + a design-time
  seam-review gate; bind-to-touched (not bind-to-declared); no-residual-for-load-bearing;
  the standing System Invariant Register; guarded-but-untested-is-not-fully-bound; and five
  binding-quality lessons earned binding the reversibility surface (PRs #186, #193–#197):
  gate–guard parity, know-what-your-guard-can-see, durable-prevention-survives-the-toolchain,
  bind-the-whole-surface-not-a-sample, and adversarial-per-slice-verification-with-pin-to-head.
- **New templates** — `templates/system-invariant-register.md` (standing register format) and
  `templates/adr-enforcement-field.md` (inline ADR `Enforcement:` field convention), both
  linked from `docs/INDEX.md`.

### Compatibility

The pre-existing bare `residual / blocked` proof-mapping disposition is intentionally
invalidated **for load-bearing invariants** — they must be bound or explicitly deferred to a
named owner. Existing closeouts that leaned on `residual` for a load-bearing invariant are
retroactively non-conformant and should be re-triaged. Non-load-bearing invariants are
unaffected. (Treated as MINOR rather than MAJOR: the canon line is new — v1.0.0 was the
establishing commit with no downstream conformance history to break beyond the triggering
pilot, which drove the change.)

Proposal of record: [`proposals/2026-06-27-invariant-binding-doctrine.md`](proposals/2026-06-27-invariant-binding-doctrine.md).

## [1.0.0] — Velocity lifecycle canon established

Initial canon: lifecycle model, role authority, artifact-authority boundaries, control planes,
proof model, branch hygiene, project-adoption guide, governance, and the core template set.

[1.2.0]: https://github.com/solidcitizen/velocity/releases/tag/v1.2.0
[1.1.0]: https://github.com/solidcitizen/velocity/releases/tag/v1.1.0
[1.0.0]: https://github.com/solidcitizen/velocity/releases/tag/v1.0.0
