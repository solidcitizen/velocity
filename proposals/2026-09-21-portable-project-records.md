# Decision-Aware Work and Portable Project Records

- Status: Accepted for experimental publication; stable integration pending
- Date: 2026-09-21
- Authority owner: Mike, Velocity Maintainer
- Mode: Process evolution
- Affected control planes: Shared authority/proof rules and reusable automation support;
  project decision ownership remains with the declared project/upstream authorities.
- Accepted version: v2.0.0-experimental.1 (opt-in prerelease); stable canon remains v1.7.2
- Branch: `codex/portable-project-records`, [draft PR #14](https://github.com/solidcitizen/velocity/pull/14)
- Release channel: `codex/2.0-experimental`; fixed tag `v2.0.0-experimental.1`
- Disposition: experimental publication authorized; publication receipt tracked as VEL-WI-8.

## Problem and resulting behavior

A project can already use `TODO.md` for work management. Requiring conversion to a structured
board confuses the contract with a storage format. Conversely, a sophisticated task board
does not establish why an initiative is selected, what resources it may consume, or who
decides whether it advances to its next stage.

The proposed profile connects strategy, portfolio investment, initiative development, and
work execution. Every adopter declares its decision context; work inherits it. Small efforts
can use one owner, an assumed capacity, and a Markdown queue. Larger efforts link their
existing management records and stage gates. Work state, development stage, investment
posture, and decision status remain separate.

The same work semantics can be carried by Markdown, the structured Work Board pilot, or an
external tracker. Project-owned sources continue across AI sessions; vendor panels are
replaceable views. The Check-in Desk routes decisions at any scope without creating a
competing backlog or approval ledger.

## Source, authority, and evidence

The Maintainer requested vendor-independent artifacts, a lightweight tracker, and a path to
the project's chosen system, then authorized implementation with “I like it proceed.”
Subsequent review clarified that TODO can itself carry work management and that portfolio,
investment, and stage decisions must be acknowledged without putting all their machinery in
every small project's queue.

The Maintainer then explicitly requested: “see how we best formalize what we are discussing
within velocity” and “use our own framework's structure to put goal-setting as a
portfolio-level future thing to tackle.” This authorizes reusable process changes and the
scoped Velocity trial records together. It does not authorize executing strategic goal-setting,
migrating other projects, accepting policy, merging, or releasing.

The follow-up request defines the standing reference method and baseline artifacts at work,
initiative and portfolio levels, asks whether each needs a decision board, and asks about PMI's
adaptation for AI entities. It authorizes the reference definition and scoped example update;
new governance services, rendered dashboards, or strategic-goal execution are not implied.

The Maintainer then agreed: “one check-in board, each decision request is qualified by the
lane that it is handling.” This selects the single-Desk default and explicit Work, Initiative,
or Portfolio decision-level metadata, distinct from execution lanes.

The subsequent instruction was to have this “actually released to the repo” for consuming
projects, with permission to “put it on github as an experimental release branch of 2.0 or
something.” This accepts the profile for experimental adoption and delegates branch/tag/release
publication to this Codex session. The chosen pin is `v2.0.0-experimental.1` on
`codex/2.0-experimental`. This supersedes the earlier release exclusion for this bounded
prerelease; it does not accept the separate Entity Development Lifecycle proposal or authorize
a stable-main merge, project migration, new spend, or execution of strategic goal-setting.

Read-only inspection of private consuming projects informed the separation of work, operating
controls, initiative planning, and investment authority. That is maintainer-context evidence,
not a public reference implementation or independent validation. The public scenarios are
synthetic and self-contained.

The earlier local artifact inspection found a continuity gap: sources and discovery lived
under one AI application's project/memory locations and views in scratch storage. Another
tool's ability to read the files did not establish discovery from the project entry point.
The existing Desk contract already separates source, rendering, stable IDs, and authority.
The Work Board pilot inspected at `e97f0188bf571e5c4000ffabee454c7471e9702f` supplies JSON states,
dependencies, and completion references. Its history is integrated into this branch; it
remains development support, not released canon.

## Proposed contracts

1. **Decision awareness.** [Decision Scopes](../docs/DECISION-SCOPES.md) names the four
   connected scopes, inherited purpose/authority/capacity, conditional management records,
   escalation, parent-change review, and AI participation boundaries. These are separate
   from L0–L5, lanes, modes, and control planes. Recurring operations are an additional pattern.
2. **Common work meaning.** [Lightweight Work Management](../docs/WORK-MANAGEMENT.md)
   defines stable identity, ownership, priority, the seven state meanings, bounded scope,
   dependencies, appropriate completion evidence, reopening, history, and uncertainty.
   A future portfolio opportunity is not a delivery commitment.
3. **Alternative bindings.** Markdown TODO can remain authoritative indefinitely. The JSON
   pilot and an external tracker are alternatives. One authoritative source owns work in a
   declared scope; derived views do not create another queue. Import is optional and retires
   a source only after a chosen, reconciled cutover.
4. **Portable records.** [Portable Project Records](../docs/PORTABLE-PROJECT-RECORDS.md)
   defines discovery, audience, source ownership, updates, writer coordination, recovery,
   view freshness, qualification, and handoff. Git/GitHub are useful choices, not requirements.
   Public code may coexist with private operational records.
5. **One ruling.** A Desk decision stays in its ledger. Where an upstream system owns the
   ruling, the Desk closes with a pointer to it. Releasing a dependent action checks the exact
   authority, remaining dependencies, current parent decision, and scope. Existing envelopes
   permit routine bounded work without a new approval for every task.

[ADR-0002](../adrs/0002-decision-context-and-work-bindings.md) records alternatives, invariants,
enforcement limits, and consequences. The core authority/proof model is retained. Record
access, actor metadata, a task state, or a model change cannot grant approval authority.

The [standing reference method](../docs/MANAGEMENT-REFERENCE.md) makes those contracts
operational: baseline artifacts, a frame/select/execute/assess/adjust loop, tailored review
triggers, and decision coverage at each level. A shared Desk is the compact default within
aligned authority, lead ownership, and access; separate decision rights can require separate
surfaces. Management status remains outside the Desk. Baseline artifact coverage does not
require a fixed file count or three dashboards. Agent execution and human accountability are
explicitly distinct.

PMI's 2026 AI standard and human–agent guidance are relevant adjacent work. The comparison
uses public sources and does not establish that PMI lacks an AI-entity lifecycle. Full-standard
comparison is a future research need before claiming a distinctive coverage gap.

## Templates and implementation boundary

- [Decision records](../templates/decision-records.md): small inherited context; optional
  portfolio opportunity, initiative, and stage/investment decision records.
- [Markdown tracker](../templates/work-tracker.md): a complete manual versioned binding.
  There is no supplied TODO parser, automatic state validator, lock, or TODO-to-HTML adapter.
- [Artifact index](../templates/artifact-index.md), agent fragment, adoption and tranche
  guidance: discover the selected binding and context without copying records into AI memory.
- Existing JSON [file support](../templates/project-records.md): empty Desk/Board startup,
  guarded local cooperating-writer updates, revision checks, idempotent retries, durable
  interrupted-operation recovery, source/view receipts, and exact snapshot handoff comparison.
  It supplies neither an authorization service nor a distributed/Markdown writer.
- [Tracker binding and handoff](../templates/tracker-binding-and-handoff.md): preserve record
  identity, meaning, context, history, evidence access, and recovery before retiring a source.
  A JSON export or matching fixture is not a live destination qualification.

The structured templates retain their shared renderer/content rules. The Desk now declares
`decision_level` in its schema and displays Work, Initiative, or Portfolio. The profile check
requires it on every open Decide, including pointers; the helper guards retention through
closure. Legacy standalone desks may omit it, and unclassified historical rulings are not
guessed. Authority, semantic classification, and agreement with an upstream owning ask remain
review duties. No filter or new board section is added.

## Velocity's own trial

[ARTIFACTS.md](../ARTIFACTS.md) declares this branch's scope, authority, audience, Markdown
binding, revision handling, and recovery. [TODO.md](../TODO.md) carries bounded execution and
uncommitted qualification work. [PORTFOLIO.md](../PORTFOLIO.md) separates:

- `VEL-PF-1`: the currently authorized foundation, with local proof and a Maintainer review gate;
- `VEL-PF-2`: strategic goal-setting, captured as a future portfolio candidate with no execution
  envelope, deadline, automatic start, or corresponding committed task.

[INITIATIVES.md](../INITIATIVES.md) carries the current effort's outcome plan and assessment as
`VEL-INI-1`. Its authority comes from `VEL-PF-1`; work stays in TODO. The existing proposal/PR
records remain this scoped trial's review and ruling route, without creating another Desk.

The future candidate's next decision is whether to charter bounded discovery, including
authority, constraints, capacity, evidence, and a review gate. This proposal defines the
interface to accepted goals; it does not deliver a goal-setting method or an autonomous
strategist. The manifesto records the broader direction without making it current canon.

These records cover this effort, not every Velocity proposal or live operational ask. The
earlier local HTML work preview remains a snapshot, not the authority for this Markdown queue.
There is no consuming-project data migration or replacement of an existing live Desk.

## Related proposals and sequencing

| Related work | Relationship and disposition |
| --- | --- |
| Work Board pilot | Integrated inspected history into this branch. Shared JSON support remains a pilot; its owner branch is unchanged. |
| [Entity Development Lifecycle, PR #11](https://github.com/solidcitizen/velocity/pull/11) | Shared broader direction. Its initiative/executive views and peer exchange remain separately owned proposals. Reconcile vocabulary, authority, and source bindings before accepting overlapping contracts; this work does not accept or rewrite that branch. |
| Cross-vendor continuation | Backlog qualification: select two actual integrations and a bounded project. Fresh CLI processes are supporting proof only. |
| External tracker | Backlog qualification: owner chooses destination, access, scope, and migration owner; prove real read/write, cutover, and recovery. |
| Strategic goal-setting | Future portfolio candidate `VEL-PF-2`; selection and charter precede any execution tranche. |
| Release/adoption | Maintainer authorized experimental publication as v2.0.0-experimental.1. Stable integration and live project migrations remain separate. |

## Proof and review

The [decision walkthrough](../examples/decision-scopes/README.md) reviews a retained TODO,
unknown history, capacity escalation, a capital gate, delegated work, changed parent authority,
recurring obligations, upstream rulings, concurrent writers, migration, a future candidate,
and an agent-proposed goal. It includes the actual Velocity trial records and states the
limits of documentary review.

The [JSON qualification record](../examples/portable-records/QUALIFICATION.md) records the
existing 17 local contract tests, synthetic process-continuation/mapping workflow, and local
HTML inspection. All 17 tests were rerun and passed for this tranche; 239 local links/anchors
in its 28 changed/new Markdown files and `git diff --check` passed before the foundation commit.
The helper's behavior and renderer layouts are not changed by the decision-contract additions.

The standing-method follow-up adds eight documentary review cases and scoped initiative
records, with local link/anchor, whitespace and public-source checks. It changes no runtime
or schema; the prior runtime tests were not rerun and do not qualify new management behavior.
Its source review includes PMI's 2026 AI standard overview and agent-team guidance, with
full-standard comparison explicitly outstanding.

The single-Desk follow-up adds runtime decision-level qualification, history retention,
legacy handling, and a three-level example. The 25-test suite passes, including the existing
file workflow and eight additional scenario checks. Updated proof and release checks are
recorded in the [qualification record](../examples/portable-records/QUALIFICATION.md).

Architect and Tester are named review responsibilities within this implementation session,
as allowed by Role Authority; this is not independent Maintainer acceptance. Required live
proof remains outstanding for actual model/provider continuation, protected role denial,
external reads/writes, cutover/recovery, and measured decision acceleration. No amount of
documentation or local test success closes those claims.

## Compatibility, affected artifacts, and disposition

- Classification: reusable proposed policy and template support, synthetic examples, and
  Velocity's scoped trial records. No private project material is published.
- Protected artifacts: `docs/MANAGEMENT-REFERENCE.md`, `docs/DECISION-SCOPES.md`, `docs/WORK-MANAGEMENT.md`,
  `docs/PORTABLE-PROJECT-RECORDS.md`, `docs/LIFECYCLE-MODEL.md`,
  `docs/CONTROL-PLANES.md`, `docs/ARTIFACT-AUTHORITY-BOUNDARIES.md`,
  `docs/PROJECT-ADOPTION-GUIDE.md`, `docs/INDEX.md`, the linked record/adoption/tranche and
  Desk/Work templates and JSON support under `templates/`, `adrs/0002-decision-context-and-work-bindings.md`,
  and `AGENTS.md`. Root direction, proposal, changelog, trial records, examples, and tests
  provide context and proof.
- Authority basis: the Maintainer's explicit process-evolution and self-adoption requests
  above. Separate private project migrations are excluded.
- Compatibility: optional development profile, mandatory semantics only for its adopters.
  Earlier conformance is unchanged. Making new context/records mandatory for all prior
  adopters requires a separate compatibility and version decision. The experimental 2.0 label
  identifies the channel, not a finalized breaking-change contract.
- Decision: accepted for opt-in experimental publication by the Maintainer's explicit request
  above. Stable acceptance/merge and live adoption remain separate.
- Branch disposition: retain `codex/portable-project-records` and draft PR #14 for stable
  integration review; publish its prepared snapshot to `codex/2.0-experimental` and the fixed
  `v2.0.0-experimental.1` tag/GitHub prerelease. Shared main and other owners' worktrees retain
  their ownership. Publication read-back is the completion condition for `VEL-WI-8` in TODO.
- Prior operations: `VEL-PF-1-20260921-foundation`, `-closeout`, and `-method` record the
  preparation history. This follow-up uses `VEL-PF-1-20260921-decision-levels` and
  `VEL-PF-1-20260921-experimental-release`.
