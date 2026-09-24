# Velocity Docs Index

## Core

- [Lifecycle Model](LIFECYCLE-MODEL.md)
- [Role Authority](ROLE-AUTHORITY.md)
- [Artifact Authority Boundaries](ARTIFACT-AUTHORITY-BOUNDARIES.md)
- [Control Planes](CONTROL-PLANES.md)
- [Proof Model](PROOF-MODEL.md)
- [Branch Hygiene](BRANCH-HYGIENE.md)
- [Project Adoption Guide](PROJECT-ADOPTION-GUIDE.md) — including [Choose Your Scope](PROJECT-ADOPTION-GUIDE.md#choose-your-scope) and [Pin a Release](PROJECT-ADOPTION-GUIDE.md#pin-a-release)

## Governance

- [Governance](../governance/GOVERNANCE.md)
- [Process Change Proposal](../templates/process-change-proposal.md)
- [ADR-0001: Independent Lifecycle Repository](../adrs/0001-independent-lifecycle-repo.md)
- [ADR-0002: Decision Context and Work Bindings](../adrs/0002-decision-context-and-work-bindings.md) — accepted for experimental adoption only

## Templates, by adoption scope

Each scope contains the one before it. Entries marked *experimental* are opt-in and are not part
of any scope's requirements.

**Delivery**

- [AGENTS Fragment](../templates/AGENTS.fragment.md)
- [Tranche Template](../templates/tranche-template.md)
- [Issue Record Template](../templates/issue-record-template.md)

**Automation**

- [Role Brief](../templates/role-brief.md)
- [Handoff Packet](../templates/handoff-packet.md)
- [Review Pack Template](../templates/review-pack-template.md)
- [Agent Evaluation Pack](../templates/agent-evaluation-pack.md)
- [Automation Transition Contract](../templates/automation-transition-contract.md)
- [Measured Automation Pilot](../templates/automation-pilot.md)
- [System Invariant Register](../templates/system-invariant-register.md)
- [Architecture Decision Record](../templates/architecture-decision-record.md)
- [ADR `Enforcement:` Field Convention](../templates/adr-enforcement-field.md)
- [Portable Project Records](../templates/portable-project-records.md) — *experimental*; continuing a project across agents and tools
- [Artifact Index](../templates/artifact-index.md) — *experimental*; shared discovery and ownership

**Entity**

- [Executive Check-in Desk](../templates/executive-checkin-desk.md) — with its data-file schema, example, and renderer
- [Work Board](../templates/work-board.md) — *experimental*; piloted on real work, with data schema and renderer
- [Work Management](../templates/work-management.md) — *experimental*; the shared meaning of work states across bindings
- [Markdown Work Tracker](../templates/work-tracker.md) — *experimental*; a TODO file as the authoritative queue
- [Project Records File Support](../templates/project-records.md) — *experimental*; guarded updates, recovery, views, and export

**Portfolio** (emerging; not a scope)

- [Decision Levels](../templates/decision-levels.md) — *experimental*; work, initiative, and portfolio decision context
- [Decision and Management Records](../templates/decision-records.md) — *experimental*; inherited context, opportunities, initiatives, and gates
- [Tracker Binding and Handoff](../templates/tracker-binding-and-handoff.md) — *experimental*; preserving meaning and authority when moving trackers

## Examples

- [Illustrative Project Overlay](../examples/project-overlay/README.md)
- [Policy and Project Mapping](../examples/project-overlay/policy-mapping.md)
- [Measured Automation Worked Example](../examples/measured-automation/README.md)
- [Portable Records Worked Example](../examples/portable-records/README.md) — synthetic command-line continuation and mapping, with explicit proof limits
- [Decision-Level Walkthrough](../examples/decision-levels/README.md) — synthetic cases and explicit review limits
- [Management Reference](../examples/management-reference/README.md) — a worked reference design for work, initiative, and portfolio records and reviews
- [Velocity Self-Adoption Snapshot](../examples/velocity-self-adoption/README.md) — Velocity's own trial records as of 2026-09-21; a dated example, not a work queue
