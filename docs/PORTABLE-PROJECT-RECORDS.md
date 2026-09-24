# Portable Project Records

An opt-in profile for decision context, lightweight work management, the Check-in Desk, and
bindings to a project's chosen tracker. This profile and its file support are development
additions accepted for `v2.0.0-experimental.1`; the Work Board remains a pilot. See
[experimental adoption](EXPERIMENTAL-ADOPTION.md). Qualification is specific to the
tested tools and scope.

## Purpose and authority

Every durable artifact adopted under this profile has a project-owned, discoverable source
of truth, a responsible role, an explicit audience, and a documented update and recovery path.
An authorized successor can continue without the originating AI session. Vendor displays are
replaceable views. A tracker handoff preserves identity, meaning, decisions, and evidence.

The existing [Artifact Authority Boundaries](ARTIFACT-AUTHORITY-BOUNDARIES.md),
[Role Authority](ROLE-AUTHORITY.md), and [Proof Model](PROOF-MODEL.md) apply. Reading a file,
using another model, or possessing a connector grants no new authority. An update command's
actor field is attribution, not authentication or proof of approval. Mandatory controls belong
outside the evaluated agent's write authority where the project requires enforcement.

## Record ownership and discovery

The project overlay links one artifact index, using the [Artifact Index](../templates/artifact-index.md)
template or an equivalent existing index. Every supported agent entry file points there. The
index identifies stable project/artifact identity, canonical location, responsible role,
audience/access, format and tool pin, read/update/validate/display procedures, history, and recovery.

File sources live in a retained project workspace, independent of agent caches and session
scratch directories. A public code repository can use a separate private operational workspace.
Public discovery information must not expose private contents or sensitive metadata. Git is
a useful default for versioned text; neither Git nor GitHub is required. Lifecycle state and
audience are separate: a draft can be public and an accepted decision can remain private.

Use appropriate documented formats: a Markdown TODO can be the authoritative work tracker;
structured Desk and Work records use their shared schemas when selected. A record's identity
includes its project scope. Renames and moves preserve that identity or a durable cross-reference.

## Decision context and work meaning

[Decision Levels](DECISION-LEVELS.md) connects strategy, portfolio investment, initiative
development, and execution. An adopter declares its governing purpose, owners, capacity
assumptions/envelope, and escalation path once. Work inherits that context. Separate business
cases, portfolio tools, and stage gates are used only where the decisions require them.
Completion, development stage, and investment authority remain distinct.

[Lightweight Work Management](WORK-MANAGEMENT.md) defines common work semantics independently
of file format. The queue tracks actions; upstream records own direction and investment.
Recurring obligations retain occurrence history and do not close when one run completes.

## Two tracking modes

- **File mode:** a Markdown queue such as `TODO.md`, or the structured JSON Work Board, is the
  authoritative lightweight tracker. The common minimum is ID, title, owner, and state, with
  context inherited and additional fields required by the claim. The
  [Markdown template](../templates/work-tracker.md) supplies a versioned manual workflow;
  the JSON pilot supplies guarded commands and HTML. Choose the binding explicitly.
- **External-tracker mode:** the project maps its existing/chosen tracker through the
  [Tracker Binding and Handoff](../templates/tracker-binding-and-handoff.md) record. Native
  fields, linked records, or an adapter preserve the same meanings. No second writable backlog
  is created to satisfy Velocity. A continuing Work Board is a derived view of that authority.

A project may start in either mode or stay in file mode indefinitely. Distinguish wanted work
from committed work, held/blocked work from active work, and dropped work from completed work.
The [common work contract](WORK-MANAGEMENT.md) and [Work Board](../templates/work-board.md) share
the seven state meanings. An external tracker may use different labels if its mapping
preserves these distinctions and the proof.

The Work Board describes work; the [Check-in Desk](../templates/executive-checkin-desk.md)
records operator asks and decisions under its existing contract, at any decision level. Work
links to the relevant Desk ask. A ruling remains in its authoritative ledger; when an upstream
system owns it, the Desk closes with a pointer, rather than becoming a second editable approval.
Answering one ask releases only its covered dependency and scope. Migrating work does not
require migrating the Desk. Recurring-control records and the software that runs them are
distinct; transferring one does not transfer the other.

## Shared update and presentation contract

1. Discover and read the authoritative record, current revision, and acting role's authority.
2. Resolve the request to stable IDs and prepare a candidate. Preserve unchanged history,
   evidence, and uncertainty. Obtain missing meaning/authority; do not add routine approvals
   where the role already has authority.
3. Validate through the declared binding: semantic review for manual Markdown, the pinned
   validator for structured files, or the qualified tracker adapter. Serialize cooperating
   writers or use conditional writes. A stale writer rereads and reconciles.
4. Save with recorded actor, request/operation identity, starting/resulting revisions, reason,
   and any required approval evidence. Retries cannot duplicate consequential updates.
5. Read back the source and regenerate/refresh each declared derived view in the same turn. Identify
   which source revision was displayed and verify that display through the selected integration.

Coupled Desk/Work changes use a transaction or durable pending operation. Record the decision
before releasing dependent work. A partial update or failed view refresh remains visible and
recoverable; source-save success is not display success. Do not discard the last usable page,
report stale information as current, or reinterpret silence as approval.

Markdown itself is a usable view for its binding. The structured Desk/Work baseline display
is standalone HTML in an ordinary browser. AI side panels and hosted pages are optional views.
Where adopted, shared renderers own validation, content, totals, and layout;
project wrappers locate storage, coordinate writes, perform project evidence preflights, and
publish/open views. They do not fork the content rules. The
[file helper](../templates/project-records.md) supplies local cooperating-writer mechanics;
its documented limitations remain part of the qualification claim. It supports JSON sources,
not Markdown parsing/editing. This profile supplies no TODO-to-HTML adapter.

## Adoption and tracker migration

An existing TODO can adopt the work contract in place and remain authoritative. Add explicit
semantics while preserving wording/history and marking unknown ownership, dates, and status.
If the owner chooses a different binding, retain a dated source copy, reconcile the import,
and only then retire the old writable queue. Historical reported completion remains distinct
from evidenced completion. Do not invent tasks merely to initialize an empty board.

A tracker handoff names its scope, audience, owner, mappings, and cutover authority. Snapshot
the records and history, map every identity to a destination or immutable archive reference,
and rehearse the import. Preserve Desk links, dependencies, states, ownership, dates,
uncertainty, proof, control history, and evidence access. An unmapped field is a visible gap.
The owner may accept an explicitly stated loss only if it does not waive authority/proof rules.

Before cutover, freeze writes or reconcile a final delta. Verify every record and a real
authorized destination update, not only totals. Record cutover time/revision and the owner's
decision; update the index and every supported agent integration. Archive the old queue and
stop its writes. Rehearse recovery that retains changes made after cutover. Back up tracker
data separately from source-code Git history. Export alone is not a qualified migration.

## Instructions for agents in an adopting project

Add this to the project's agent guide when the profile is adopted; it was moved here from the
shared agent fragment so that a project at the Delivery scope never meets it:

> If the project adopts Portable Project Records, read the artifact index linked from its
> overlay before locating or updating work and Desk records. Use its authoritative locations,
> role boundaries, pinned shared commands, current revisions, and recovery procedure. Agent
> memory is not the authority. Do not create a second backlog, bypass a pending operation, or
> report a view current without checking the selected display. External-tracker mode routes work
> to its declared binding; the retained local board is an archive. Changing models/tools does
> not change role authority.

## Qualification and compatibility

Use the [Agent Evaluation Pack](../templates/agent-evaluation-pack.md) for model, prompt, tool,
or integration changes. Name the tested configurations. Qualify each claimed capability with
the applicable scenarios; a file-only adopter need not qualify an unused external tracker:

- an empty start, TODO retained as the tracker, and provenance-preserving conversion when chosen;
- inherited decision context, changed parent authority, and future opportunities kept uncommitted;
- Tool A creates, fresh Tool B continues from the project entry point, and A resumes correctly;
- an operator decision and the exact dependent work change across the visible surfaces;
- stale/concurrent writes, retries, interrupted updates, and failed display refresh;
- role denial through the project's actual enforcement boundary;
- a selected destination's mapping, real read/write behavior, cutover, and recovery.

Local contract checks and synthetic examples support these claims but do not substitute for
cross-vendor or destination workflow proof. See the
[qualification record](../examples/portable-records/QUALIFICATION.md) for this implementation's
actual coverage and remaining work. Adoption is optional; earlier conformance is not re-judged.
Live project migrations and publication remain separately scoped project work.
