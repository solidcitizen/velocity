# Velocity

Velocity is a reusable software delivery lifecycle for AI-assisted engineering.

It is intentionally project-independent. Product repositories consume Velocity through a project overlay; they do not own the general lifecycle rules.

## Purpose

Velocity exists to make agent-assisted delivery repeatable across projects while preserving human authority over goals, risk, and process evolution.

Its broader direction is to accelerate decisions from strategy and portfolio investment
through initiative development, execution, and ongoing operations. The
[manifesto](MANIFESTO.md#decision-making-throughout-an-entity) describes that ambition;
the development profile below lays the groundwork without claiming those capabilities are released.

Read the [Velocity field guide](https://velocitystandard.org) for a practical,
AI-agnostic introduction, then use this repository for the authoritative rules and templates.
The guide explains the method; it does not create a second source of lifecycle policy.

Current canon: **v1.7.2 — documentation currency and delegated release mechanics**.
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

The rule is stated once, in [Artifact Authority Boundaries](docs/ARTIFACT-AUTHORITY-BOUNDARIES.md) and [Role Authority](docs/ROLE-AUTHORITY.md). In short: delivery roles read the rules and propose changes; only the Velocity Maintainer, or a delegate acting on the maintainer's explicit approval, changes lifecycle policy, through the [process-change flow](governance/GOVERNANCE.md#process-change-flow).

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

## Decision-Aware Work and Portable Records (development)

An optional [Portable Project Records profile](docs/PORTABLE-PROJECT-RECORDS.md) is under
development alongside the lightweight Work Board pilot. [Decision scopes](docs/DECISION-SCOPES.md)
connect each effort to its purpose, selection authority, capacity, and escalation path.
[Lightweight work management](docs/WORK-MANAGEMENT.md) defines the common semantics:
`TODO.md` can remain the tracker, with structured JSON and external systems as alternative bindings.
The Check-in Desk routes decisions at any scope. See the
[decision walkthrough](examples/decision-scopes/README.md) and
[file-support qualification limits](examples/portable-records/README.md).
This development support does not change the current canon release or qualify an AI provider
or external tracker without its scenario evidence.

Velocity is trying this structure in its own scoped [artifact index](ARTIFACTS.md),
[work queue](TODO.md), and [portfolio](PORTFOLIO.md). Strategic goal-setting is recorded there
as a future portfolio opportunity, not committed delivery work.

## Feedback

Questions, mistakes, and proposed changes all go through
[GitHub issues](https://github.com/solidcitizen/velocity/issues/new/choose). Pick the form that
fits: a change to the standard, feedback on the field guide, or a mistake or broken link.
There is no other channel, so the conversation and the change it produces stay together here.
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

A product repository keeps a short `AGENTS.md` pointer to Velocity and its own project-specific material; reusable lifecycle policy belongs here. The boundary is defined once, in the adoption guide's [What Stays In The Project Repo](docs/PROJECT-ADOPTION-GUIDE.md#what-stays-in-the-project-repo).

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
