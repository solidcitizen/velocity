# Project Adoption Guide

Velocity is adopted through a thin project overlay.

## What Stays In Velocity

- reusable role definitions
- lifecycle state model
- proof taxonomy
- artifact authority boundaries
- branch hygiene requirements
- process evolution governance
- templates for packets, tranches, closeout, review packs, role briefs, and the executive
  check-in desk
- optional evaluation, automated-transition, and measured-pilot templates
- optional development contracts for decision context, work semantics, and portable records

## Choose Your Scope

Velocity is adopted in scopes. Each scope is a bundle of rules and templates that already exist
here; a scope holds no rule of its own, and a rule that lives only in a scope's description has
become a second core. Each scope contains the one before it, so a project moves outward without
re-learning what it already runs, and "conformant at Delivery scope" is a claim a team can make
honestly.

**Delivery.** One project, one delivery lead, one operator. The [Lifecycle Model](LIFECYCLE-MODEL.md),
[Role Authority](ROLE-AUTHORITY.md), [Artifact Authority Boundaries](ARTIFACT-AUTHORITY-BOUNDARIES.md),
[Proof Model](PROOF-MODEL.md) and [Branch Hygiene](BRANCH-HYGIENE.md), with the
[tranche](../templates/tranche-template.md), [issue record](../templates/issue-record-template.md)
and [agent guide fragment](../templates/AGENTS.fragment.md) templates. Start here. Most projects
need nothing else.

**Automation.** Adds the artifacts that let work cross a boundary without a person carrying it:
[role briefs](../templates/role-brief.md), [handoff packets](../templates/handoff-packet.md),
[review packs](../templates/review-pack-template.md), the
[agent evaluation pack](../templates/agent-evaluation-pack.md),
[automation transition contract](../templates/automation-transition-contract.md) and
[measured automation pilot](../templates/automation-pilot.md), the
[system invariant register](../templates/system-invariant-register.md) with its
[enforcement field](../templates/adr-enforcement-field.md),
[architecture decision records](../templates/architecture-decision-record.md), and
[Control Planes](CONTROL-PLANES.md). Adopt it when an agent's output reaches a lane a person
would otherwise have gated. Experimental, opt-in: the
[portable project records profile](PORTABLE-PROJECT-RECORDS.md) with its
[artifact index](../templates/artifact-index.md), for continuing a project across agents and tools.

**Entity.** Adds the operator's standing surfaces for a function or a company rather than a
single project, beginning with the [Executive Check-in Desk](../templates/executive-checkin-desk.md).
Adopt it where an operator sits outside day-to-day delivery and decisions would otherwise live in
chat history. Experimental, opt-in: the [Work Board](../templates/work-board.md) or a
[Markdown work tracker](../templates/work-tracker.md) under the [work contract](WORK-MANAGEMENT.md),
and the [file helper](../templates/project-records.md) that keeps desk and board data safe.

**Portfolio** is emerging and is not yet a scope. One operator across several entities is a real
position, and the only rule Velocity has for it today is the desk's cross-desk pointer. It is
named in the [manifesto](../MANIFESTO.md#one-core-two-lifecycles) as direction so the gap is
visible. The experimental [decision levels](DECISION-LEVELS.md),
[management reference](MANAGEMENT-REFERENCE.md), [decision records](../templates/decision-records.md)
and [tracker binding](../templates/tracker-binding-and-handoff.md) are its first explorations; none
of them is a scope or a requirement.

## What Stays In The Project Repo

- project architecture
- product issue logs
- project-specific lane map
- environment names and commands
- deployment and promotion runbooks
- project-specific risks and invariants
- current mission, packet, and review-pack artifacts
- product-specific acceptance scenarios

## Recommended Project Files

In the consuming project:

- `AGENTS.md` - short pointer to Velocity plus local commands and constraints.
- `docs/LIFECYCLE-OVERLAY.md` - project-specific overlay.
- `docs/SYSTEM-ISSUE-LOG.md` - project issue index.
- `docs/SYSTEM-ISSUE-DETAILS.md` - detailed issue records.
- `docs/agent-packets/` - project handoff packets.
- `docs/agent-missions/` - project mission ledger if used.
- `docs/review-packs/` - operator-facing project review artifacts.
- a project ADR index and decision records, using the project's established location.

## Overlay Requirements

A project overlay must define:

- lane names and authority boundaries
- supported dev/test/deploy commands
- production mutation approval path, including the exact approval phrase(s) that authorize production mutation and whether `ship it` qualifies
- project-specific proof harnesses
- issue numbering and issue-doc format
- branch naming conventions
- role map (which roles are distinct owners vs. hats on one person)
- planning or cadence integration (Scrum, Kanban, Shape Up, or a local method)
- issue-record profile default and escalation triggers
- incident escalation path
- local exceptions to Velocity, if any

Project overlays may specialize Velocity. They may not silently override core lifecycle governance.

If a project needs to change a core Velocity rule, open a Velocity process-change proposal.

## Scaling The Role Split

Velocity scales down as well as up; the authority boundaries matter more than the number of people involved. The original use case is a team of one doing high-volume AI-assisted development, where the roles are a self-binding device — deliberate mode switches for one human working with agents, not bureaucracy. For solo or very small teams, roles may be hats rather than people; the session should still name the current hat and never self-approve a protected change in the same breath that produced it. At minimum, separate the moment of implementation from the moment of acceptance.

The practical minimum for solo AI-assisted work:

- frame the work as Coordinator before asking for implementation
- switch to Fixer only after scope, lane, and proof are clear
- switch to Tester or validation mode before accepting operator-facing behavior
- switch to Architect before changing invariants, ownership, or proof contracts
- switch to Velocity Maintainer only when reusable lifecycle policy is explicitly being changed

In a pair or small team, the most valuable real separations are Operator/Coordinator from Fixer (scope and acceptance), Fixer from Tester (operator-visible workflow claims), and project-overlay owner from Velocity Maintainer (reusable policy). In high-risk, regulated, production-critical, or incident-prone contexts, use stronger separation across Coordinator, Fixer, Tester, Architect, and promotion authority.

Velocity governs authority, proof, lifecycle state, role handoff, and process evolution. It does not define sprint length, estimation units, roadmap cadence, team topology, backlog prioritization, or the release calendar — use Scrum, Kanban, Shape Up, incident command, or a local method for those, and let the overlay say how they map in.

## ADR Discipline

Architect review already applies to changes to architecture contracts, authority boundaries,
replay/retry semantics, durable status truth, operator-facing state contracts, and lifecycle
proof rules; see [Role Authority](ROLE-AUTHORITY.md#architect). Use an ADR to preserve the
context, options, rationale, accepted decision, and consequences of significant architecture
work. The optional [Architecture Decision Record](../templates/architecture-decision-record.md)
provides a complete format; an existing project format can serve the same purpose.

Keep a proposed decision distinct from an accepted one, link the authorized review and
acceptance, and preserve a replaced decision through a superseding record. Link the decision
to its implementation tranches and proof. For each load-bearing invariant, use the existing
[Enforcement field](../templates/adr-enforcement-field.md) and keep it aligned with the
[System Invariant Register](../templates/system-invariant-register.md). Acceptance of a design
does not prove its implementation or authorize live promotion.

This is recommended recordkeeping support for existing authority and proof rules, not a new
requirement to create an ADR for every change or to migrate all historical decisions. ADRs are
established practice; the template credits their lineage. Populated product decisions stay in
the consuming project. Decisions about Velocity itself belong in this repository's `adrs/`.

## Executive Check-in Discipline

The [Handoff Packet](../templates/handoff-packet.md) and [Review Pack Template](../templates/review-pack-template.md)
carry one piece of work to its next owner or readout. Neither one answers a different, recurring
need: a standing, cross-cutting page of everything the project's [Operator](ROLE-AUTHORITY.md#operator)
must decide or do right now, so an ask never survives only as "the earlier message" in chat. The
optional [Executive Check-in Desk](../templates/executive-checkin-desk.md) is that companion
artifact — every ask gets a stable ID that is never renumbered, closed asks move to a dated
ledger instead of disappearing, and the page is republished the same turn an ask is added,
answered, or closed. Silence is never consent: an ask stays open until the operator answers it,
and a decision within the team's own authority is made, owned, and recorded on the page rather
than parked for a veto window. The desk is built from a data file by the template's renderer,
which validates the file against the contract; only the project name, operator, maintainer,
time-zone label, and color tokens vary per project. An operator who runs several projects meets
several desks, so the desk is a shared surface: a project that needs something the data file
cannot express raises a Velocity proposal rather than building a local variant. Adopt it only where an operator genuinely sits outside day-to-day delivery
and would otherwise have no single place to find what is still open.

## Adopting Portable Project Records

These profiles are experimental and opt-in, on the 2.0 channel. Start with
[experimental adoption](EXPERIMENTAL-ADOPTION.md) for the fixed pin, record choices, and
qualification limits. A project that adopts none of them stays exactly where it is.

For the optional [Portable Project Records profile](PORTABLE-PROJECT-RECORDS.md), name a
project-owned operational workspace and link one [artifact index](../templates/artifact-index.md)
from the overlay and all agent entry files. Record responsible roles, audience, source/view
locations, tool pin, update commands, writer coordination, and recovery. Public code and private
operational records can have separate homes. Git/GitHub are optional storage/collaboration choices.

A project can retain an authoritative [Markdown TODO](../templates/work-tracker.md), choose
the structured [Work Board](../templates/work-board.md), or bind an existing tracker through the
[Tracker Binding and Handoff](../templates/tracker-binding-and-handoff.md) record. Keep one
authoritative backlog per declared scope. The [work contract](WORK-MANAGEMENT.md) supplies
state and completion meanings; import/retirement is necessary only for a chosen migration.
The Desk remains the operator decision/action surface and can stay in
place when work migrates. The [file helper](../templates/project-records.md) supplies a shared
procedure for authorized AI sessions using JSON; it does not parse Markdown. Native panels
remain optional views. Check the profile's
qualification record before claiming cross-vendor or tracker-migration support.

Declare the [decision context](DECISION-LEVELS.md) in the existing overlay or index: purpose,
selection/initiative owners, current authority and capacity assumptions, escalation, and review.
The profile asks an adopting effort to acknowledge these scopes; separate portfolio,
business-case, resource, and gate records are conditional on the decisions involved. Use the
[management record templates](../templates/decision-records.md) only where useful. Small projects
can combine ownership and inherit a short context block; larger efforts link upstream systems.
Existing work within its authority can proceed while unrelated upstream unknowns are resolved.
This development profile is optional and does not change earlier conformance.

Use the [standing management reference](MANAGEMENT-REFERENCE.md) to map baseline work,
initiative, and portfolio artifacts, their review triggers, and their decision route. Coverage
can be combined in existing records. Default to a shared Check-in Desk within aligned
ownership/access; split it for distinct authorities, accountable leads, or access/review needs.
Status belongs in the management views. No new Desk filters or synchronization are implied.

## Overlay Experiments

A project may test a local rule in its overlay before proposing a Velocity core change. An overlay experiment should state its name, owner, start date, intended duration or review trigger, the local rule being tested, the Velocity core rule it touches, a compatibility check against shared-context / separated-write-authority, the evidence to collect, and the promotion path if it works. Overlay experiments must not silently contradict core governance: they may specialize commands, issue formats, lane names, proof harnesses, and routing, but they may not remove acceptance-proof-first, erase lane proof boundaries, or let the role being evaluated rewrite its own evaluation criteria.

## Adopting Measured Automation

The v1.4 templates are opt-in support for the existing authority and proof model. They do not
retroactively change prior conformance, introduce automatic acceptance, or adopt the manifesto's
delegation grades. Start with one workflow and prove its behavior before widening its scope.

1. **Use Capture, Decision, and Tranche.** Record the observation and evidence in the
   project's existing issue record. Have the appropriate owner decide the direction, then
   define bounded scope, acceptance criteria, and proof in a tranche. Keep requirements
   and architecture in their existing authoritative homes. Link the accepted revision from
   handoffs or other working copies rather than creating a second independently editable record.
2. **Make context usable.** Keep the agent entry file short, link authoritative guidance,
   and package repeated procedures as versioned skills or equivalent adapters. Preserve policy
   ownership and record which versions ran. Test both whether the adapter loads and whether
   the behavior it requests occurs; instructions alone do not enforce an invariant.
3. **Qualify the development agent.** Instantiate the
   [Agent Evaluation Pack](../templates/agent-evaluation-pack.md). Include successful work,
   authority denials, scenario-proof failures, and incident regressions. Protect the checks
   from the candidate, compare against the baseline, and retain all attempted-run outcomes.
4. **Qualify one handoff.** Fill the
   [Transition Contract](../templates/automation-transition-contract.md). Bind the accepted
   artifact revision to the next action, verify authorization at execution, and test stale,
   duplicate, interrupted, and denied paths. Put mandatory enforcement outside the agent's
   write authority and exercise every relevant mutation route. Isolate concurrent work and
   serialize shared writes; add parallel sessions only while review capacity keeps up.
5. **Measure before expanding.** Use the [Measured Pilot](../templates/automation-pilot.md)
   for baseline, shadow, bounded execution, and a recorded disposition. Monitor a signal with
   a deterministic rule and route findings into normal issue capture and triage. Pre-approved
   recovery still needs a scoped authority record and rehearsal evidence.

The [worked example](../examples/measured-automation/README.md) supplies synthetic cases and
a tabletop trace. It is not a running integration or proof of improved delivery. A project
chooses its runtime, commands, budgets, fixtures, and rollout independently. A request to update
Velocity does not itself migrate or enable automation in a consuming project.
