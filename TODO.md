# Velocity Work — Development Scope

Authoritative Markdown queue for the bounded effort in [ARTIFACTS.md](ARTIFACTS.md), on this
proposal branch. It does not import every other Velocity queue or operational Desk item.
Project identity: `velocity`. Priority owner: Velocity Maintainer; coordinating editor: Codex
in the Coordinator responsibility. Accountable human owner: Mike as Velocity Maintainer.
All items inherit `VEL-PF-1` and its declared authority; their outcome plan is
[VEL-INI-1](INITIATIVES.md#vel-ini-1--decision-aware-work-and-portable-continuity).
Queue order within a state gives the next-work preference, without granting new authority.

States and update discipline: [work contract](docs/WORK-MANAGEMENT.md) and
[binding/history/recovery](ARTIFACTS.md#update-history-and-recovery). No checkbox or board
snapshot overrides an explicit state. Dates below are records of events, not deadlines.

## Current tranche

### VEL-WI-8 — Publish the experimental 2.0 release

- State: `done`
- Owner: Coordinator; Mike as Maintainer accepted experimental publication.
- Scope / done when: publish a fixed `v2.0.0-experimental.1` tag and GitHub prerelease on
  `codex/2.0-experimental`, provide project adoption instructions, and verify remote source,
  tag/branch identity, prerelease status, and stable-release disposition.
- Source: Maintainer's 2026-09-21 instruction to release this for consuming projects and
  permission to use an experimental 2.0 release branch; recorded in the proposal.
- Context: `VEL-PF-1`, `VEL-INI-1`; current session capacity. No project migration or stable
  main merge is required by this work item.
- Completion: 2026-09-21; [GitHub prerelease](https://github.com/solidcitizen/velocity/releases/tag/v2.0.0-experimental.1)
  is published, with tag resolving to `aa9462b784416f1db1e743e0f0a8f5041d95d0d4` and the
  experimental branch published. Public HTTPS clone, six release-file byte comparisons,
  remote tag/branch identity, and stable v1.7.2 read-back passed. See the
  [publication receipt](examples/portable-records/RELEASE-RECEIPT.md).
- History: 2026-09-21, Coordinator prepared and published the release under the explicit
  ruling, verified it remotely, then recorded this closeout without moving the fixed tag.

### VEL-WI-7 — Qualify decisions on the shared Check-in Desk

- State: `done`
- Owner: Coordinator, with named Architect and Tester review passes.
- Scope / done when: one Desk retains its five sections; Work, Initiative, or Portfolio
  identifies the ruling requested and survives closure without creating another queue.
- Source: Maintainer's 2026-09-21 agreement to one board with qualified decision requests.
- Context: `VEL-PF-1`, `VEL-INI-1`; implementation and local proof within existing capacity.
- Completion: 2026-09-21; shared contract/schema/renderer, strict open-decision profile check,
  helper retention guard, and [three-level example](examples/decision-scopes/desk.json).
  25 local tests passed, including classification, pointers, closure/history/export, and
  prior file-workflow scenarios. This does not qualify a live project migration or AI vendor.
- History: 2026-09-21, Coordinator implemented the agreed semantics; Architect review kept
  authority and management level separate; Tester checked the shared board and retained rulings.

### VEL-WI-6 — Define the standing reference method and decision surfaces

- State: `done`
- Owner: Coordinator; Architect review of artifact/authority boundaries.
- Scope / done when: a PMI-informed reference method names the baseline artifacts, review
  loop, and decision routing at work, initiative, and portfolio levels; examples show when
  one Desk suffices and when separate authorities need their own surfaces. Velocity's scoped
  records demonstrate the method without starting the future goal-setting candidate.
- Source: Maintainer's 2026-09-21 request to define the standing method and assess boards per level.
- Research scope: includes the follow-up question about PMI's adaptation for AI entities;
  distinguish verified public guidance from unreviewed full-standard coverage.
- Context: `VEL-PF-1`; current documentation/review scope and capacity from the artifact index.
- Completion: 2026-09-21; [reference method](docs/MANAGEMENT-REFERENCE.md), expanded templates,
  [initiative record](INITIATIVES.md), and
  [eight-case review](examples/decision-scopes/README.md#reference-method-review). Local links,
  whitespace and public-source checks passed. This closes definition/review preparation;
  it does not accept policy, qualify a new UI, or claim full PMI-standard coverage.
- History: 2026-09-21, Coordinator researched primary sources, defined the method, then
  completed named Architect/Tester documentary review and recorded its limits.

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

- State: `done`
- Owner: Coordinator with named Architect and Tester review passes.
- Scope / done when: documentation/links and local file-support checks pass, decision scenarios
  are reviewed, qualification limits are recorded, and the draft PR describes the final scope.
  Maintainer acceptance, merge, release, and live pilots are separate outcomes.
- Source: framework proof and closeout obligations for the authorized change.
- Context: [VEL-PF-1](PORTFOLIO.md#vel-pf-1--decision-aware-work-and-portable-records).
- Completion: 2026-09-21; [review and proof](examples/decision-scopes/README.md), 17 passing
  file-support tests, local link/anchor and whitespace checks, and
  [draft PR #14](https://github.com/solidcitizen/velocity/pull/14) updated and read back with
  foundation commit `edbeb54`. No policy acceptance or release is claimed.
- History: 2026-09-21, Coordinator started validation, recorded the Architect/Tester review
  results, pushed the foundation, verified the draft PR, and closed review preparation.

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
