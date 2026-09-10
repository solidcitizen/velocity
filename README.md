# Velocity

Velocity is a reusable software delivery lifecycle for AI-assisted engineering.

It is intentionally project-independent. Product repositories consume Velocity through a project overlay; they do not own the general lifecycle rules.

## Purpose

Velocity exists to make agent-assisted delivery repeatable across projects while preserving human authority over goals, risk, and process evolution.

Read the [Velocity field guide](https://velocitystandard.org) for a practical,
AI-agnostic introduction, then use this repository for the authoritative rules and templates.
The guide explains the method; it does not create a second source of lifecycle policy.

Current canon: **v1.5.0 — ADR recordkeeping support and public standard**.
See the [Changelog](CHANGELOG.md) for compatibility and release status. The additive templates help
projects evaluate development agents, qualify automated handoffs, and measure delivery results;
they do not activate automation or change existing approval boundaries.

Core goals:

- manage SDLC best practices independent of any one product repo
- separate delivery authority from lifecycle-rule authority
- let specialist roles share context without allowing them to rewrite the criteria that judge their work
- make proof expectations explicit and portable across local, staging, host-qualified, and production lanes
- provide templates that projects can adopt with project-specific overlays

## Authority

The core invariant is:

> Shared context, separated write authority.

Delivery roles may read Velocity rules and propose changes. They may not directly modify Velocity governance during ordinary product delivery.

Lifecycle-rule changes are owned by the Velocity maintainer role and require explicit process-change disposition.

## Documents

- [Lifecycle Model](docs/LIFECYCLE-MODEL.md)
- [Role Authority](docs/ROLE-AUTHORITY.md)
- [Artifact Authority Boundaries](docs/ARTIFACT-AUTHORITY-BOUNDARIES.md)
- [Control Planes](docs/CONTROL-PLANES.md)
- [Proof Model](docs/PROOF-MODEL.md)
- [Branch Hygiene](docs/BRANCH-HYGIENE.md)
- [Project Adoption Guide](docs/PROJECT-ADOPTION-GUIDE.md)
- [Governance](governance/GOVERNANCE.md)

## Direction & Positioning

Not lifecycle policy, and not part of the governed `docs/` set:

- [Manifesto](MANIFESTO.md) — direction, not policy: where Velocity should evolve next.
- [Lineage and Adjacent Work](LINEAGE-AND-ADJACENT-WORK.md) — positioning, not policy: where Velocity sits relative to agent frameworks and prior art.
- [2026 playbook comparison](LINEAGE-AND-ADJACENT-WORK.md#comparison-reviewed-2026-09-09) — dated primary-source comparison, historical context, and adoption decisions.

## Put It Into Practice

Start with the [Project Adoption Guide](docs/PROJECT-ADOPTION-GUIDE.md), define a thin local
overlay, and use the [Tranche Template](templates/tranche-template.md) on one bounded change.
Velocity works with your chosen AI tools and delivery cadence.

For significant architecture work, use the [ADR discipline guidance](docs/PROJECT-ADOPTION-GUIDE.md#adr-discipline)
and [Architecture Decision Record](templates/architecture-decision-record.md) to connect the
decision, its authority, and the mechanisms that enforce its invariants.

For the optional v1.4 automation additions, read the
[source attribution](LINEAGE-AND-ADJACENT-WORK.md#attribution-for-the-september-additions),
[adoption steps](docs/PROJECT-ADOPTION-GUIDE.md#adopting-measured-automation), and
[synthetic worked example](examples/measured-automation/README.md). Use the three templates together:

- [Agent Evaluation Pack](templates/agent-evaluation-pack.md) — qualify changes to the development agent.
- [Automation Transition Contract](templates/automation-transition-contract.md) — connect accepted artifacts to authorized actions.
- [Measured Automation Pilot](templates/automation-pilot.md) — compare delivery time, human effort, quality, and cost.

## Adoption Pattern

Each product repo should keep only:

- a short local `AGENTS.md` reference to Velocity
- project-specific lane, command, environment, and risk details
- project-specific issue logs, packets, missions, and review packs

Reusable lifecycle policy belongs here.

## Public Examples

These self-contained examples require no access to another repository:

- [Project overlay](examples/project-overlay/README.md) — an illustrative application showing
  how to name local artifacts, lanes, commands, and approval boundaries.
- [Policy and project mapping](examples/project-overlay/policy-mapping.md) — what belongs in
  Velocity and what stays with a consuming project.
- [Measured automation](examples/measured-automation/README.md) — a synthetic worked example
  of evaluation, accepted-artifact handoffs, and a bounded pilot.

Example paths and commands are illustrative; they are not a supplied application or current
operating instructions. Adapt them to your own project and its pinned Velocity version.

## Development History

Velocity grew out of the maintainer's work in private software and operations projects.
Those projects are not public reference implementations. Historical proposals describe
maintainer-reported experience, not independently reproducible evidence, customer
endorsements, or measured gains. Public examples illustrate the method without claiming to
reproduce those projects or their results.

Public availability does not turn a proposal or the manifesto into adopted policy; consult
the changelog for release status.
