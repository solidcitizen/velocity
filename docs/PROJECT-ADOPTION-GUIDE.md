# Project Adoption Guide

Velocity is adopted through a thin project overlay.

## What Stays In Velocity

- reusable role definitions
- lifecycle state model
- proof taxonomy
- artifact authority boundaries
- branch hygiene requirements
- process evolution governance
- templates for packets, tranches, closeout, review packs, and role briefs
- optional evaluation, automated-transition, and measured-pilot templates

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
