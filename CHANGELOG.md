# Changelog

Velocity lifecycle canon. Consuming projects pin to a tagged version (git submodule)
rather than a moving branch. Versions are canon releases, not software:

- **MAJOR** — a change that makes previously-conformant delivery non-conformant
  (a rule is removed, narrowed, or reversed such that prior closeouts must be re-judged).
- **MINOR** — additive doctrine, new templates, or new guidance that does not
  invalidate prior conformance.
- **PATCH** — clarifications, typos, link fixes, non-normative edits.

## Unreleased — Decision-Aware Work and Portable Records (development)

- Add decision scopes connecting strategy, portfolio investment, initiative development, and
  execution. Adopters inherit a small authority/capacity context; business cases and stage gates
  are conditional. Distinguish work state, development stage, investment posture, and rulings.
- Define common work semantics with Markdown TODO as a first-class authoritative tracker,
  alongside structured JSON and external bindings. No automatic Markdown parser/renderer is supplied.
- Add management-record templates, a proposed ADR, synthetic decision walkthroughs, and
  Velocity's scoped artifact index, TODO, and portfolio. Strategic goal-setting is future
  portfolio candidate VEL-PF-2, with no execution commitment.
- Add an opt-in profile and shared artifact index for project-owned records, independent of
  an AI vendor's memory or artifact panel. Public code and private operational records may
  have separate homes; Git and GitHub remain optional.
- Integrate the existing Work Board pilot with the Check-in Desk. Add empty startup and local
  guarded updates with revision checks, retry identities, recoverable coupled writes, view
  receipts, and complete record/history exports, using the existing shared renderers.
- Add tracker-binding and handoff guidance, exact normalized-snapshot comparison, and archive
  labeling/write retirement after an authorized cutover. No live tracker connector is included.
- Add a runnable synthetic TODO/Desk/Work example and qualification record. Local checks do
  not establish cross-vendor operation, external-tracker integration, or live migration.

Implementation authorized by Mike as Velocity Maintainer on 2026-09-21: "I like it proceed",
then the explicit request to formalize decision levels and record future strategic goal-setting
using Velocity's own framework. Requirements apply only on adoption of this development profile;
prior conformance is unchanged. Related Entity Development Lifecycle work remains separately owned.
Prepared for review; no acceptance, merge, version assignment, or release is recorded here.
See the [proposal and implementation record](proposals/2026-09-21-portable-project-records.md).

## [1.7.2] — 2026-09-20

### Clarified — Documentation currency and delegated release mechanics

- Governance now states the two mechanics the maintainer may delegate in writing: merging a
  proposal the maintainer has explicitly approved, and release stamping. Delegation transfers no
  approval authority and creates no eighth role; every acceptance record names the approval it
  acted on. Practice since v1.5.1 is now written down.
- Protected paths are stated once, as directories, matching `AGENTS.md` and recorded practice:
  `docs/`, `governance/`, `templates/`, `adrs/`, and `AGENTS.md`.
- A proposal's header lines (Status, version, Disposition) are updated at acceptance, so no
  merged proposal reads "not merged". Three accepted proposals corrected.
- The README states the core invariant once and links to its canonical statement instead of
  paraphrasing it, and points to the adoption guide for what stays in a project repository.
- Release link definitions in this changelog now cover every release; the issue form's version
  placeholder no longer names a specific release.

**PATCH**: clarifications and corrections of existing rules and records. No lifecycle rule,
role, approval boundary, proof obligation, or prior conformance changes.

Prompted by the maintainer's observation of stale references on 2026-09-20 and two independent
read-only audits the same day. Accepted by Mike as Velocity Maintainer on 2026-09-20 for merge and
release as `v1.7.2`. See the [proposal and acceptance record](proposals/2026-09-20-documentation-currency.md).

## [1.7.1] — 2026-09-19

### Clarified — Check-in Desk pointers close with their owner

- A pointer entry (an ask owned by another desk) now closes when the owning ask closes: state
  `answered` or `withdrawn`, the same date, a ruling naming the owner's decision, and `owned_by`
  kept; the renderer lists it under Already answered with "owned by <project> CK-n". The 1.7.0
  schema described pointers as open-only, which left a decided question showing as open.
- The renderer tolerates a withdrawn ruling that already begins with the word "withdrawn".

**PATCH**: clarification of an existing rule plus a renderer and schema fix. No new field is
required; desks built on 1.7.0 render unchanged.

Reported from a consuming project's migration on 2026-09-19 as a template gap rather than a
local variant, which is the intended path. Accepted by Mike as Velocity Maintainer on 2026-09-19 for
merge and release as `v1.7.1`. See the [proposal and acceptance record](proposals/2026-09-19-desk-pointer-closure.md).

## [1.7.0] — 2026-09-19

### Changed — Executive Check-in Desk, repeatable by construction

- The desk is now built from a data file (`templates/executive-checkin-desk.example.json`,
  defined by `templates/executive-checkin-desk.schema.json`) with a dependency-free renderer
  (`templates/render-checkin-desk.py`) that validates the file against the contract and computes
  the header totals, ordering, and reply examples. The HTML starter is now the renderer's output.
- The contract states what was previously implied: exact headings and field labels, the `CK`
  prefix everywhere, the time of day in the header stamp, a maintainer slot, and an ID on every
  team decision. Only the project name, operator, maintainer, time-zone label, and color tokens
  vary per project.
- Three gaps closed: withdrawn asks keep their ID and close with a reason; one ask open on two
  desks has one owner and a pointer on the other; team-decision status opens with one of four
  fixed words.
- Adoption guidance: the desk is a shared surface across an operator's projects; a need the
  data file cannot express is raised as a Velocity proposal, never met with a local variant.

**MINOR**: additive files and a tightened optional template. No lifecycle rule, role authority,
proof obligation, or delivery closeout is re-judged. Desks instantiated before this release
should be migrated per the template's migration steps; the migration keeps every existing ID.

Proposed under Mike's request, as Velocity Maintainer, after a maintainer-reported audit of five
private consuming desks. Accepted by Mike as Velocity Maintainer on 2026-09-19 for merge and release
as `v1.7.0`. See the [proposal and acceptance record](proposals/2026-09-19-checkin-desk-repeatability.md).

## [1.6.0] — 2026-09-19

### Added — Executive Check-in Desk Template

- Optional reusable template: a standing, ID-tracked page of everything the project's Operator
  must decide or do, with a Markdown skeleton (`templates/executive-checkin-desk.md`) and a
  generic, dependency-free HTML starter (`templates/executive-checkin-desk.html`) with light/dark
  theming and placeholder content only.
- Silence is never consent: an ask stays open until the Operator answers it, and decisions within
  the team's own authority are made, owned, and recorded in a "Decided by the team" ledger rather
  than parked for a veto window. (Revised 2026-09-18 on maintainer review, which rejected the
  first draft's "if silent, it stands" default.)
- Companion to the existing Handoff Packet and Review Pack Template: those carry one piece of
  work to its next owner; this is the cross-cutting surface of every open ask to the Operator.
- New "Executive Check-in Discipline" guidance in the Project Adoption Guide; linked from the
  docs index.

**MINOR**: additive template and adoption guidance only. No changed authority boundary, proof
obligation, role definition, or prior conformance. The template documents an existing practice
from a private consuming project (in use there since 2026-09-14 under a project-specific name)
generalized to remove any project-specific naming, data, or secrets. Affected protected
artifacts: `templates/` (one new Markdown file, one new HTML file) and `docs/INDEX.md`;
`docs/PROJECT-ADOPTION-GUIDE.md` gains one adoption-guidance section.

Proposed under Mike's request, as Velocity Maintainer, to generalize the pattern into reusable
canon. Accepted by Mike as Velocity Maintainer on 2026-09-19 for merge and release as `v1.6.0`.
See the [proposal and acceptance record](proposals/2026-09-18-executive-checkin-desk-template.md).

## [1.5.1] — 2026-09-19

### Clarified — Public References and Examples

- Replace private-project references in the README and docs index with a self-contained,
  illustrative project overlay and a policy/project mapping.
- Generalize private project names and inaccessible implementation identifiers in historical
  proposals and changelog entries. Label those accounts as maintainer-reported private work;
  retain original acceptance dates, policy text, and the rationale for adopted rules.
- Update the field-guide address to the approved `velocitystandard.org` domain.

**PATCH**: publication and example cleanup only. No lifecycle rule, role authority, proof
obligation, template, or prior conformance changes. The only affected protected artifact is
`docs/INDEX.md`, whose example links change. Historical tags and Git history remain intact.

Proposed under Mike's request to remove reliance on private projects from the public repo.
Accepted by Mike as Velocity Maintainer on 2026-09-19 (merge of PR #7) for release as `v1.5.1`.
See the [proposal and acceptance record](proposals/2026-09-09-public-reference-cleanup.md).

## [1.5.0] — 2026-09-09

### Added — ADR Recordkeeping Support

- Optional complete Architecture Decision Record template: context, alternatives, rationale,
  review/acceptance, enforcement links, consequences, delivery, and supersession.
- Adoption guidance connects ADRs to the existing Architect review, invariant-binding,
  project ownership, and promotion rules. Existing project ADR formats remain usable.
- Credit the established ADR tradition, including Michael Nygard's 2011 account.

### Clarified — Public Presentation And Attribution

- Replace the imported artifact-filename convention in the adoption guide with Velocity's
  existing Capture, Decision, Tranche, and issue-record vocabulary.
- Credit Anthropic's influence on the September automation additions beside the comparison.
- Link the public field guide and qualify project adoption accounts and historical examples.
- Align a proof-mapping comment with the existing named-deferral rule; clarify that a role
  brief follows the project's declared index policy and distinguishes artifact ownership from
  live-promotion approval wording.

**MINOR**: additive template and recommended guidance, plus editorial corrections. No changed
authority boundary, proof obligation, or prior conformance. No universal per-change ADR
requirement or historical migration is introduced. Authority: Mike's request to publish and
clean up Velocity, credit external concepts, keep the standard primary, and embed ADR discipline
on 2026-09-09. Affected protected artifacts: `docs/PROJECT-ADOPTION-GUIDE.md`, `docs/INDEX.md`,
and `templates/architecture-decision-record.md`.
Other protected editorial corrections: `docs/PROOF-MODEL.md` and `templates/role-brief.md`.

Accepted by Mike as Velocity Maintainer on 2026-09-09 for merge and release as `v1.5.0`.
See the [proposal and acceptance record](proposals/2026-09-09-public-standard-and-adrs.md).

## [1.4.0] — 2026-09-09

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

### Compatibility And Acceptance

**MINOR** under this changelog's versioning rules: additive, opt-in templates and guidance;
no new universal conformance requirement, changed approval boundary, or retroactive re-judgment.
The manifesto's v2 ambition does not require a 2.0 release for these compatible additions.
No consuming project is migrated or enabled by this change. Runtime and pilot outcomes remain
unmeasured. Accepted by Mike as Velocity Maintainer on 2026-09-09 for merge and release as
`v1.4.0`; the acceptance amendment records that decision and finalizes release labels.

Proposal and authority record:
[`proposals/2026-09-09-measured-automation.md`](proposals/2026-09-09-measured-automation.md).

## [1.3.0] — 2026-07-05

### Added — Role-Brief Template

One new template, no Core/policy surface change. Source: maintainer-reported experience in
two private projects — a software application (Coordinator / Product-Owner briefs) and an
operations framework (Product-Director / Tactical / Reviewer briefs). Both reportedly
converged on the same artifact shape; promoted to core via the adoption guide's overlay-experiment→promote path
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
- **`README.md`** gained an "Adoption in Practice" note about two private projects —
  maintainer-reported background, not policy or independently reproducible evidence.

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
anti-direction) plus minimal pointer and template edits. Source: a maintainer-reported
incident in a private application (2026-05-14), where an agent read urgency language (`critical`) as
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
maintainer-reported integrity pilot in a private application (2026-06-26/27), where an audit
identified 11 load-bearing invariants without enforcement. The pilot informed this doctrine;
its implementation and review artifacts are not publicly reproducible evidence.

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
  binding-quality lessons reported while implementing reversible operations:
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

[1.7.2]: https://github.com/solidcitizen/velocity/releases/tag/v1.7.2
[1.7.1]: https://github.com/solidcitizen/velocity/releases/tag/v1.7.1
[1.7.0]: https://github.com/solidcitizen/velocity/releases/tag/v1.7.0
[1.6.0]: https://github.com/solidcitizen/velocity/releases/tag/v1.6.0
[1.5.1]: https://github.com/solidcitizen/velocity/releases/tag/v1.5.1
[1.5.0]: https://github.com/solidcitizen/velocity/releases/tag/v1.5.0
[1.4.0]: https://github.com/solidcitizen/velocity/releases/tag/v1.4.0
[1.3.0]: https://github.com/solidcitizen/velocity/releases/tag/v1.3.0
[1.2.1]: https://github.com/solidcitizen/velocity/releases/tag/v1.2.1
[1.2.0]: https://github.com/solidcitizen/velocity/releases/tag/v1.2.0
[1.1.0]: https://github.com/solidcitizen/velocity/releases/tag/v1.1.0
[1.0.0]: https://github.com/solidcitizen/velocity/releases/tag/v1.0.0
