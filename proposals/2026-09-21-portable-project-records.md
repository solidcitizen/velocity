# Portable Project Records and Tracker Handoff

- Status: Proposed; not adopted or implemented
- Date: 2026-09-21
- Authority owner: Mike, Velocity Maintainer
- Mode: Process evolution
- Source: The maintainer's request to incorporate AI-vendor-independent artifacts, the
  lightweight work tracker, and a path to the project's chosen tracking system.
- Disposition: Integration proposal for the existing Work Board pilot and Check-in Desk.
  No release, live-record migration, or external integration is enabled by this document.
- Accepted version: None

## Outcome and evidence

A project can begin with a TODO file, adopt Velocity's lightweight tracker, change its AI
tool, and later move to another tracker without losing work, decisions, evidence, or authority.
Remaining on the lightweight tracker indefinitely is a valid choice. Projects with an existing
tracker can map it directly; they do not need to adopt the file implementation first.

The maintainer's review found a populated desk whose JSON source lived in an AI application's
project directory, whose rendered HTML lived in session scratch storage, and whose discovery
instructions lived in that application's memory. The source was readable by another agent,
but the project entry point did not identify it. This is observed local evidence of a
discovery and continuity gap, not a cross-vendor acceptance test. No private records are needed
to understand or reproduce the proposed qualification scenarios below.

The current [Desk contract](../templates/executive-checkin-desk.md) already separates data from
rendering, preserves IDs, and names the writing role. The Work Board pilot on
`proposal/work-board`, inspected at `e97f0188bf571e5c4000ffabee454c7471e9702f`, already supplies
a file, schema, validator, renderer, work states, dependencies, and completion references.
That revision is a development snapshot, not released canon. This proposal supplies a common
operating contract around those artifacts; it does not create another board implementation.

## Proposed policy

> Every durable artifact adopted under this profile has a project-owned, discoverable source
> of truth, a responsible role, an explicit audience, and a documented update and recovery path.
> An authorized successor can continue the work without the originating AI session. Vendor
> displays are replaceable views. A tracker handoff preserves identities, meaning, decisions,
> and evidence, and ends with one declared authority for each record.

This is an opt-in portability profile until accepted. Existing role and proof rules continue
to apply. Reading a record, possessing a connector, or changing AI models grants no new write
or approval authority. Qualified operation is claimed only for the tested integrations and
versions, never for every model or vendor by inference.

## 1. Shared discovery and storage

The project overlay links one artifact index. Every supported agent entry file points to that
same index. A human-readable table is sufficient; an additional registry service is unnecessary.
Each entry identifies:

- stable project/artifact identity, purpose, responsible role, and authoritative location;
- audience and access requirements, including the boundary between private and public records;
- file format/schema and pinned validator/renderer, or external system and field/state mapping;
- supported read, update, validate, render/open, export, and recovery procedures;
- revision identification, writer coordination, and locations of history and derived views.

Canonical file sources live in a project-owned workspace with documented retention and backup.
Agent memory directories and temporary output directories are not canonical homes under this
profile. A public code repository may point authorized operators to a separate private
operational workspace without publishing its contents or sensitive metadata. Git is a useful
default for text history, but neither Git nor GitHub is required.

Illustrative layout, resolved relative to the declared operational workspace:

```text
ARTIFACTS.md             # ownership, locations, procedures, audience
checkin/desk.json        # authoritative operator decision/action ledger
work/board.json          # authoritative work records in file mode
history/                 # audit records or a documented version-history mechanism
views/desk.html          # generated portable view
views/board.html         # generated portable view
```

These paths illustrate a layout, not new required filenames. An external-tracker project
replaces the work-file entry with its tracker binding. An export or cache is labeled as such,
with its source revision and collection time, and cannot become a second independent backlog.

## 2. Lightweight work tracking and the Desk

The lightweight tracker remains optional template support. Ordinary work starts with the
pilot's small required record: identity, title, owner, and state. Required information grows
with the claim: an active item names its bounded scope, a blocked item names its blocker, a
completed item cites appropriate evidence, and a dropped item records its reason. Size,
benefit, initiatives, dates, and recurring controls are used when applicable. Completion
evidence does not require a new document for every small task; an existing appropriate
record or verification result can serve. A citation alone does not judge proof adequacy.

Retain the pilot's distinctions among backlog, committed, doing, blocked, held, done, and
dropped. External systems can use different labels if the documented mapping preserves those
meanings, including the difference between wanted work and a delivery commitment.

The Work Board answers what is being done, waiting, or planned. The Check-in Desk records
operator decisions/actions and decisions owned by the team under its existing contract.
Work references Desk asks; an approval is not duplicated into a second editable decision
ledger. Answering an ask releases only the dependency covered by that answer, not every
blocker or authority boundary attached to an item. Moving work to another tracker does not
require moving the Desk.

Qualify a truly empty starting desk/board. The currently inspected schemas require at least
one entry; adoption must not require inventing an ask or task to make a new project validate.
Any change to that behavior belongs in the shared schema and renderer, not a project wrapper.

## 3. One update procedure across AI tools

All supported AI integrations follow the same procedure:

1. Read the index, current source revision, relevant evidence, and acting role's authority.
2. Resolve the requested change to stable IDs. Ask only when meaning or authority is missing;
   ordinary updates within granted authority do not acquire a new confirmation requirement.
3. Prepare and validate the candidate with the shared, pinned implementation. Identify the
   actor, request, starting revision, and any decision/approval evidence governing the change.
4. Commit through serialized ownership or a conditional write against the starting revision.
   A stale writer rereads and reconciles; it must not silently overwrite a newer change.
5. Read back the saved source, render its revision, and refresh the configured operator view.
6. Report the result with source and view revisions. If rendering or publication fails,
   record that the source was saved but the view is stale; do not report a complete update.

Retries reuse the recorded operation identity or reconcile the actual result before writing
again, so they cannot assign a second ID to the same request. Coupled Desk/Board updates need
either a transaction or a durable pending operation and recovery procedure. Record the
decision before releasing the work it authorizes; an interrupted update must remain visible
and repairable. A conflicting operator answer is resolved through the existing authority
model rather than whichever agent writes last.

Keep the existing requirement to refresh the operator view in the same turn. A failure receipt
explains an unmet requirement; it does not turn a stale display into conformant success.
Record view identity and source revision in a generated footer or publication receipt. A
timestamp alone does not prove that a view contains the current source.

## 4. Portable presentation and thin integrations

The baseline view is standalone HTML readable in an ordinary browser. Source records remain
readable independently. A vendor's side panel is an optional presentation integration; no
particular panel API, hosting account, or AI session is necessary to recover the source and
produce the baseline view. Preserve the shared renderer's content and layout contract.

AI integrations locate the project, invoke the documented update procedure, and open or
refresh the appropriate view. They do not independently redefine states, permissions,
validation, ordering, or totals. Credentials remain in the environment's credential mechanism.
Missing access is reported explicitly and does not result in a new privately maintained copy.

Shared validation and rendering stay in Velocity's template support. Shared file-update
mechanics needed for qualification should also be reusable support. Project wrappers may
resolve storage, coordinate writes, perform documented evidence preflights, and publish/open
the output; they must not reimplement the artifact's content rules. Integration instructions
identify the exact commands that exist rather than assuming every agent discovers them.

## 5. Tracker adoption and handoff

Two supported modes are sufficient: **file mode**, using the lightweight tracker, and
**external-tracker mode**, binding to the project's chosen tracker. The shared work-record
meaning applies in both. A tracker binding names the destination, record and field mappings,
write authority, query/export mechanism, recovery procedure, and qualified scope.

Adopting from a TODO file preserves the original as a dated source. Retain wording and origin,
record uncertain fields, and distinguish historical reported completion from verified proof.
Reconcile the import before retiring the TODO file as an active queue.

Moving to an external tracker is a bounded project migration:

1. Select the destination and record scope, audience, responsible owner, and cutover authority.
   Scale, collaboration, reporting, or integrations may motivate a move; no automatic threshold
   forces it. Source selection is separate from approval to expose data or purchase services.
2. Snapshot the source and inventory open work, closed/dropped history, dependencies, Desk
   references, owners, dates, uncertainty, completion evidence, and recurring controls.
3. Define the mapping and rehearse import in an appropriate test scope. Every old identity
   receives a destination identity or an explicit immutable archive location. For example,
   project `example-app` item `WI-7` may map to destination issue `482`; old references still
   resolve through that crosswalk. Display names may change without changing project identity.
4. Preserve distinctions the destination lacks in documented fields or linked durable records.
   For example, a tracker with only Open/Closed must still distinguish held from doing and
   dropped from completed. A control's history, next due date, and execution mechanism need an
   explicit disposition; moving a work item does not migrate its scheduler. Missing mappings
   block cutover or require the owner to accept a specifically documented loss of semantics.
   Such acceptance cannot waive Velocity's authority or proof requirements.
5. Coordinate a brief write freeze or a verified final-delta transfer. Reconcile each record,
   not just totals: text, state meaning, ownership, references, evidence access, and history.
   Verify real reads and an authorized update in the destination, including a Desk dependency.
6. Record the cutover revision/time and owner decision. Switch the artifact index and all
   supported agents to the destination. Retain the source as a dated, read-only archive with
   the crosswalk. Any remaining Velocity board reads from the destination as a derived view.
7. Exercise recovery. Before cutover, the source remains authoritative; afterward, reconcile
   new destination changes before any rollback. Never resume an old snapshot as a writable
   queue while losing updates made after cutover.

A generic JSON/CSV export is transfer support, not proof of destination compatibility. The
first supported destination is selected by the pilot project's owner and qualified end to end.
Unimplemented connectors are recorded as unsupported. An external tracker needs a documented
export and restoration path; a Git clone of code does not establish recovery of tracker data.

## Delivery sequence and ownership

| Tranche | Deliverable and completion condition |
| --- | --- |
| 1. Common contract | Accept the profile, artifact-index template, tracker-binding/handoff template, and adoption guidance. Keep storage ownership, lifecycle state, audience, and authority explicit. |
| 2. Shared file support | Integrate into the existing Desk and Work Board work: empty start, revision/history support, guarded update mechanics, portable views, and failure reporting. Reuse their schemas and renderers. |
| 3. Cross-vendor pilot | In a project-owned private operational workspace, qualify two independent AI-tool integrations against the same source and browser baseline, including interrupted and conflicting updates. |
| 4. Tracker handoff pilot | Rehearse and verify one owner-selected tracker destination, its identity mapping, Desk links, final-delta cutover, export, and recovery. |
| 5. Release and adoption | Publish only the support actually qualified. State remaining limitations. Migrate existing live projects in separately owned, bounded tranches. |

Implementation changes to `proposal/work-board` and the Entity Development Lifecycle proposal
are coordinated with their existing owner. This proposal records dependencies without taking
over those branches. Entity/portfolio views can consume these records, but are not needed to
adopt lightweight tracking. Integrate the portable-storage and tracker-binding rules into that
work so it does not establish competing authoritative records.

## Required acceptance evidence

Use the existing [Proof Model](../docs/PROOF-MODEL.md) and
[Agent Evaluation Pack](../templates/agent-evaluation-pack.md). Models, prompts, tools, and
entry instructions are identified in qualification evidence; a new model or integration gets
the relevant evaluations rather than inheriting an unsupported claim of equivalent behavior.

| Scenario | Expected observable result | Proof |
| --- | --- | --- |
| Empty project / TODO adoption | Empty views work; imported items retain source, uncertainty, and historical-completion labels. | Runtime contract and operator view |
| Tool A creates; fresh Tool B continues; A resumes | Using only the project entry point and authorized access, each finds the same IDs, history, and current source; an authorized update survives the handoffs. No original chat/memory is supplied. | End-to-end scenario, source revisions, view read-back |
| Operator answers a Desk ask | Exact authorized decision is retained; the correct work dependency changes; unrelated blockers and approvals remain. | Operator scenario and state evidence |
| Two agents edit the same revision | One serialized update succeeds; the stale write is refused or explicitly reconciled without lost data. | Runtime contract |
| Retry / interrupted coupled update | No duplicate work or approval; pending work resumes or is reconciled from recorded state. | Runtime contract and trace |
| Render/publish failure | Saved source and last displayed revision are distinguished; the operator is told the view is stale. Retry restores the current view. | End-to-end scenario and trace |
| Unauthorized update | Access does not substitute for role authority; protected decisions remain unchanged. | Runtime denial and state evidence |
| Tracker cutover | Every record has a disposition; IDs, state meanings, evidence, controls, and Desk references survive; the selected destination becomes the sole writable work authority. | Destination runtime and operator scenario |
| Recovery after a new destination update | New changes survive restoration or reconciled rollback; the archived queue does not silently become writable. | Recovery rehearsal |

An agent's successful read, a valid JSON file, or a rendered screenshot alone does not close
the cross-vendor or tracker-handoff claim. Preserve the tested revisions and limitations.

## Scope, authority, and compatibility

- Authority basis: the maintainer's request to work out incorporation authorizes this proposed
  process design. Adoption, merge, and release follow [Governance](../governance/GOVERNANCE.md).
- Classification: reusable policy and template-support proposal. Populated operational
  records, vendor credentials, publication targets, and live migrations remain project work.
- Protected artifacts changed by this proposal: none. It changes only this proposal file.
- Proposed implementation touches: a new common contract in `docs/`, `docs/INDEX.md`,
  `docs/PROJECT-ADOPTION-GUIDE.md`, `templates/AGENTS.fragment.md`, artifact-index and tracker
  handoff templates, and the Desk/Work Board schemas, renderers, and shared update support.
  A synthetic example belongs in `examples/`; no private project record is copied into canon.
- Compatibility: an additive, opt-in profile can be a MINOR release. Prior conformance is not
  re-judged. Existing adopters migrate explicitly. A decision to impose new mandatory rules on
  all prior adopters requires a separate compatibility assessment under the
  [versioning policy](../CHANGELOG.md), not an automatic minor-version claim.
- Version and timing: unassigned. Coordinate with the existing Work Board pilot's disposition;
  do not relabel that pilot accepted or promise a release date through this proposal.

## Proof and disposition

Proposal-only evidence: inspected current canon and the named Work Board development snapshot;
checked local Markdown links and `git diff --check`. No cross-vendor workflow, external-tracker
integration, migration, or recovery scenario has been run for this proposal. Those outcomes
remain unproven until the acceptance scenarios above are executed.

Decision: pending Velocity Maintainer review. Branch disposition: ready for PR on
`codex/portable-project-records`; local proposal commit only, not pushed, merged, or released.
