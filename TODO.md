# Velocity Work — Development Scope

Authoritative Markdown queue for the bounded effort in [ARTIFACTS.md](ARTIFACTS.md), on this
proposal branch. It does not import every other Velocity queue or operational Desk item.
Project identity: `velocity`. Priority owner: Velocity Maintainer; coordinating editor: Codex
in the Coordinator responsibility. All items inherit `VEL-PF-1` and its declared authority.
Queue order within a state gives the next-work preference, without granting new authority.

States and update discipline: [work contract](docs/WORK-MANAGEMENT.md) and
[binding/history/recovery](ARTIFACTS.md#update-history-and-recovery). No checkbox or board
snapshot overrides an explicit state. Dates below are records of events, not deadlines.

## Current tranche

### VEL-WI-1 — Formalize decision context across scopes

- State: `done`
- Owner: Coordinator; Architect review of semantics; Maintainer retains acceptance.
- Scope / done when: proposed strategy/portfolio/initiative/execution contract, authority
  integration, compatibility, and lineage are reviewable, with synthetic decision scenarios.
- Source: Maintainer's 2026-09-21 instruction to formalize the broader vision.
- Context: [VEL-PF-1](PORTFOLIO.md#vel-pf-1--decision-aware-work-and-portable-records).
- Completion: 2026-09-21; [proposed contract](docs/DECISION-SCOPES.md),
  [ADR](adrs/0002-decision-context-and-work-bindings.md), and
  [review walkthrough](examples/decision-scopes/README.md). This closes preparation of the
  proposal, not Maintainer acceptance of policy.
- History: 2026-09-21, Coordinator started the authorized tranche, then closed its drafting
  scope after the named Architect/Tester review passes.

### VEL-WI-2 — Make TODO a first-class tracker and record the future portfolio opportunity

- State: `done`
- Owner: Coordinator.
- Scope / done when: common state semantics and Markdown binding are explicit, these scoped
  project records use them, and `VEL-PF-2` is captured as an uncommitted portfolio candidate.
- Source: Maintainer clarification that TODO carries work management, followed by the request
  to use Velocity's own framework for future strategic goal-setting.
- Context: [VEL-PF-1](PORTFOLIO.md#vel-pf-1--decision-aware-work-and-portable-records).
- Completion: 2026-09-21; [work semantics](docs/WORK-MANAGEMENT.md),
  [Markdown binding](templates/work-tracker.md), this queue, [artifact index](ARTIFACTS.md),
  and [VEL-PF-2](PORTFOLIO.md#vel-pf-2--strategic-goal-setting), checked in the review walkthrough.
- History: 2026-09-21, Coordinator implemented and reviewed the requested records;
  goal-setting execution remains excluded.

### VEL-WI-3 — Verify the foundation and prepare its review

- State: `doing`
- Owner: Coordinator with named Architect and Tester review passes.
- Scope / done when: documentation/links and local file-support checks pass, decision scenarios
  are reviewed, qualification limits are recorded, and the draft PR describes the final scope.
  Maintainer acceptance, merge, release, and live pilots are separate outcomes.
- Source: framework proof and closeout obligations for the authorized change.
- Context: [VEL-PF-1](PORTFOLIO.md#vel-pf-1--decision-aware-work-and-portable-records).
- History: 2026-09-21, Coordinator began local validation and review preparation.

## Backlog — not committed

### VEL-WI-4 — Qualify actual cross-vendor continuation

- State: `backlog`
- Owner: Coordinator; Maintainer selects pilot scope and responsible operator.
- Scope / done when: two named AI integrations continue from a shared project entry point and
  demonstrate authorized changes, interruption/recovery, conflicts, and current views.
- Source / uncertainty: [existing qualification gap](examples/portable-records/QUALIFICATION.md);
  pilot project/configurations, access boundary, capacity, and dates are not selected.
- Context: `VEL-PF-1`; outside the present implementation tranche's execution authorization.

### VEL-WI-5 — Qualify a chosen tracker handoff

- State: `backlog`
- Owner: Coordinator; Maintainer selects destination and migration owner.
- Scope / done when: real destination reads/authorized writes, mapping, cutover, evidence
  access, and recovery after a destination update are proven within a selected pilot.
- Source / uncertainty: [tracker handoff contract](templates/tracker-binding-and-handoff.md);
  destination, credentials/access, project, capacity, and dates are not selected.
- Context: `VEL-PF-1`; no live migration is authorized by this backlog entry.

Strategic goal-setting is [VEL-PF-2](PORTFOLIO.md#vel-pf-2--strategic-goal-setting), not a task
commitment here. Selecting it later requires a portfolio decision and bounded discovery scope.
