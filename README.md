# Velocity

**Build anything with agents, and keep authority over what you build.**

Velocity is a standard for work done with AI agents: who may change the goal, what bounds a piece
of work, what counts as proof that it is done, and how automation is allowed to expand. None of
those rules name a kind of system. They were written for software delivery, which is still the
way most projects meet them, and they are written so that nothing stops at the edge of a
codebase.

**Start with one project.** Adopt the [Delivery scope](docs/PROJECT-ADOPTION-GUIDE.md#choose-your-scope),
which is a handful of rules and three short templates, on one bounded change. Nothing here limits you to
one project, or to software: the scopes above it carry the same core outward to an automated
handoff, to a function, and to a company. Take the scope you need and leave the rest.

Velocity is intentionally project-independent. Repositories consume it through a project overlay;
they do not own the general rules.

## Purpose

Velocity exists to make agent-assisted work repeatable while preserving human authority over
goals, risk, and process evolution. Where it is applied is the adopter's choice; the
[manifesto](MANIFESTO.md#one-core-two-lifecycles) records how far that is meant to reach and what
has to be true before a rule follows it there.

Read the [Velocity field guide](https://velocitystandard.org) for a practical,
AI-agnostic introduction, then use this repository for the authoritative rules and templates.
The guide explains the method; it does not create a second source of lifecycle policy.

Current canon: **v1.9.1 — the reconciled trunk: experimental templates by scope, starting with the
Work Board**.
See the [Changelog](CHANGELOG.md) for compatibility and release status. The additive templates help
projects evaluate development agents, qualify automated handoffs, and measure delivery results;
they do not activate automation or change existing approval boundaries.

Core goals:

- manage delivery best practice independent of any one repository, product, or function
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

Pick a scope, then start small. [Choose Your Scope](docs/PROJECT-ADOPTION-GUIDE.md#choose-your-scope)
sets out three: **Delivery** for one project with one lead and one operator, **Automation** when an
agent's output reaches a lane a person would otherwise have gated, and **Entity** when an operator
sits outside day-to-day delivery. Each contains the one before it, so moving outward adds
artifacts and never re-teaches what you already run.

Whichever you pick: read the [Project Adoption Guide](docs/PROJECT-ADOPTION-GUIDE.md), define a
thin local overlay, and use the [Tranche Template](templates/tranche-template.md) on one bounded
change. Velocity works with your chosen AI tools and delivery cadence.

## Beyond the Delivery Scope: Experimental Templates

Opt-in templates for projects that outgrow one project and one operator, placed by
[scope](docs/PROJECT-ADOPTION-GUIDE.md#choose-your-scope). None is required at any scope.

- **Automation:** [portable project records](templates/portable-project-records.md) and an
  [artifact index](templates/artifact-index.md), for continuing a project across agents and tools.
- **Entity:** the [Work Board](templates/work-board.md), piloted on real work; the
  [work-management contract](templates/work-management.md) that gives every way of keeping work
  the same state meanings; a [Markdown work tracker](templates/work-tracker.md); and the
  [file helper](templates/project-records.md) that keeps desk and board data safe.
- **Portfolio, emerging:** [decision levels](templates/decision-levels.md),
  [decision records](templates/decision-records.md), and
  [tracker binding and handoff](templates/tracker-binding-and-handoff.md).

What has and has not been proven is stated in the
[decision-level walkthrough](examples/decision-levels/README.md) and the
[portable-records worked example](examples/portable-records/README.md). The
[management reference](examples/management-reference/README.md) is one worked design, and a dated
[snapshot of Velocity's own trial](examples/velocity-self-adoption/README.md) shows the records in
use.

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
