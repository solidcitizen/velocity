# Changelog

Velocity lifecycle canon. Consuming projects pin to a tagged version (git submodule)
rather than a moving branch. Versions are canon releases, not software:

- **MAJOR** — a change that makes previously-conformant delivery non-conformant
  (a rule is removed, narrowed, or reversed such that prior closeouts must be re-judged).
- **MINOR** — additive doctrine, new templates, or new guidance that does not
  invalidate prior conformance.
- **PATCH** — clarifications, typos, link fixes, non-normative edits.

## [1.4.0] — Candidate, 2026-09-09

### Added — Measured Automation Support

- Three optional reusable templates: `agent-evaluation-pack.md` for regression-testing the
  development agent/configuration, `automation-transition-contract.md` for accepted-artifact
  handoffs within existing authority, and `automation-pilot.md` for baseline comparisons,
  bounded rollout, deterministic monitoring, and quality/effort/resource measures.
- A synthetic worked example under `examples/measured-automation/` with twelve case designs
  and a tabletop trace. It is not a running integration or measured success.
- Adoption steps and control-plane pointers folded into existing docs and linked from the
  index and README. Runtime adapters, real fixtures, and measured results stay in project overlays.

### Changed — Dated Positioning And Comparison

- First-party comparison of Anthropic's AI-Native SDLC Playbook, AWS AI-DLC, GitHub Spec Kit,
  BMad Method, Kiro, Superpowers, and OpenAI harness engineering in `LINEAGE-AND-ADJACENT-WORK.md`.
- Historical context separates the method's development from its 2026-05-11 repository
  extraction and distinguishes original exclusivity language from a verified priority claim.
- Manifesto direction now acknowledges convergence and explains that its delegation grades,
  including timeout-based acceptance, remain an unadopted sketch.

### Compatibility And Release State

**MINOR** under this changelog's versioning rules: additive, opt-in templates and guidance;
no new universal conformance requirement, changed approval boundary, or retroactive re-judgment.
The manifesto's v2 ambition does not require a 2.0 release for these compatible additions.
No consuming project is migrated or enabled by this change. Runtime and pilot outcomes remain
unmeasured. Candidate awaiting maintainer acceptance; no `v1.4.0` release/tag is implied yet.

Proposal and authority record:
[`proposals/2026-09-09-measured-automation.md`](proposals/2026-09-09-measured-automation.md).

## [1.3.0] — 2026-07-05

### Added — Role-Brief Template

One new template, no Core/policy surface change. Source: two consuming projects — nexusplus
(Coordinator / Product-Owner briefs) and **smart**, the first non-product-software adopter
(Product-Director / Tactical / Reviewer briefs) — independently converged on the same artifact
shape; promoted to core via the adoption guide's overlay-experiment→promote path
(`proposals/2026-07-05-role-brief-template.md`).

- **`templates/role-brief.md`** — a per-role **cold-start onboarding brief** that boots an agent
  *into* a Velocity role. It fills the gap between `docs/ROLE-AUTHORITY.md` (what a role owns and
  must not do) and instantiation (the artifact handed to an agent so it operates *as* that role
  from a cold start). Authority is instantiated **by reference**; two load-bearing template rules:
  **status-free** (point to living status, never a frozen paste) and **link, don't restate**
  (never paraphrase a canon rule into a drift-prone second copy — in one adopter a paraphrased
  hard-stop list silently dropped two safety-critical items). Populated per-role briefs remain
  project-overlay artifacts, as with the System Invariant Register. Linked from `docs/INDEX.md`
  and the `PROJECT-ADOPTION-GUIDE` template list.
- **`README.md`** gained an "Adoption in Practice" note (nexusplus + smart) — non-normative
  adoption evidence, not policy.

### Acceptance amendment

- The template's fill-in instructions gained one line: on instantiation into a consuming project,
  **repoint the canon links** to the project's pinned Velocity reference — a dead canon link
  defeats *link, don't restate*.

## [1.2.1] — 2026-06-27

### Added — Direction & positioning artifacts admitted at root (non-normative)

No new `docs/` mass and no Core/policy surface change (per the manifesto anti-direction).
These are direction/context, not lifecycle policy, so they land at repo root and are not added
to `docs/INDEX.md`; both are linked from `README.md` under "Direction & Positioning".

- **`MANIFESTO.md`** admitted at repo root — the v2 thesis (delegation grades), secondary
  directions, and the anti-directions. It is the source of the "no new `docs/` mass"
  anti-direction that v1.1.0 and v1.2.0 both cite by name; committing it closes a dangling
  by-name dependency. Remains "direction, not policy" — not in `docs/INDEX.md` or GOVERNANCE
  Protected Paths.
- **`LINEAGE-AND-ADJACENT-WORK.md`** admitted at repo root — a positioning essay (Velocity vs.
  agent frameworks; imported lineage; what Velocity does not provide), carrying a "positioning,
  not policy" disclaimer.

### Changed — adoption & sizing guidance folded into existing canon

- **Scaling the role split** (scale-down framing; solo/pair/small-team/high-risk separation)
  and an **Overlay Experiments** protocol folded into `docs/PROJECT-ADOPTION-GUIDE.md`; its
  overlay checklist gained role-map, cadence-integration, issue-profile, and
  incident-escalation items.
- **Issue Record Profiles** (Minimal / Standard / Full) folded into
  `templates/issue-record-template.md`.
- **Tranche sizing heuristics** (split / keep-together) folded into `docs/LIFECYCLE-MODEL.md`.

### Not admitted

Candidate standalone docs `docs/ADOPTION-SCALING.md` and `docs/TRANCHE-MODEL.md` were **not**
admitted — their primitives are already defined in existing canon (`LIFECYCLE-MODEL`,
`ROLE-AUTHORITY`, `tranche-template`); only their non-redundant slivers were folded.

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

[1.4.0]: proposals/2026-09-09-measured-automation.md
[1.3.0]: https://github.com/solidcitizen/velocity/tree/v1.3.0
[1.2.1]: https://github.com/solidcitizen/velocity/releases/tag/v1.2.1
[1.2.0]: https://github.com/solidcitizen/velocity/releases/tag/v1.2.0
[1.1.0]: https://github.com/solidcitizen/velocity/releases/tag/v1.1.0
[1.0.0]: https://github.com/solidcitizen/velocity/releases/tag/v1.0.0
