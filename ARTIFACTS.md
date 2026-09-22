# Velocity Development Artifact Index

This is Velocity's own trial adoption of the proposed decision/work contract. It covers the
decision-aware work and portable-records effort on `codex/portable-project-records`, for
[draft PR #14](https://github.com/solidcitizen/velocity/pull/14). It is not a complete inventory
of Velocity's work, an adoption by all consuming projects, or a migration of an existing live
Desk. These branch records become shared defaults only through review and integration.

## Decision context

- Project identity: `velocity`; these public records use the `VEL-` ID namespace.
- Purpose: accelerate evidence-backed decisions across strategy, portfolio investment,
  initiative development, and execution while preserving accountable authority.
- Strategy source: the Maintainer's 2026-09-21 direction, recorded in the
  [proposal](proposals/2026-09-21-portable-project-records.md) and
  [manifesto](MANIFESTO.md#decision-making-throughout-an-entity). A strategic goal-setting
  method is future work, not an accepted capability.
- Portfolio/selection authority: Velocity Maintainer. [PORTFOLIO.md](PORTFOLIO.md) distinguishes
  the currently authorized effort from an unselected future opportunity.
- Initiative/plan: [VEL-INI-1](INITIATIVES.md#vel-ini-1--decision-aware-work-and-portable-continuity)
  carries the outcome plan under `VEL-PF-1`; no additional program layer is needed. Mike as
  Maintainer is the accountable human owner; Codex executes the Coordinator responsibility.
  Architect and Tester responsibilities are explicit review passes, not independent acceptance.
- Current authority/capacity: the Maintainer authorized formalization and these trial records
  on 2026-09-21. Use the existing session and repository capacity for docs, local proof, and
  review preparation. No monetary/resource budget is estimated or approved by this record.
- Escalate to the Maintainer for a scope/resource expansion, goal adoption, acceptance of
  reusable policy, merge/release/public-site change, or live project migration. Routine edits
  and validation within this requested scope need no repeated approval.
- Next gate: Maintainer review of the proposed contracts and evidence; no promised date.
  Record the ruling in the existing review/decision record and link it here when it exists.
- Audience: public repository content. Private operational data and agent-session locations
  are excluded. All public examples are self-contained or explicitly synthetic.
- Unknowns: release/version, live pilot owners/configurations, external tracker destination,
  and the scope/evidence contract for strategic goal-setting. None is assumed approved.

## Sources and views

| Record | Authority in this branch scope | Responsible owner | View / update |
| --- | --- | --- | --- |
| Portfolio opportunities and investment context | [PORTFOLIO.md](PORTFOLIO.md) | Maintainer decides; Coordinator records | Markdown; retain decision source and history |
| Execution queue | [TODO.md](TODO.md) | Coordinator within declared authority | Markdown; serialized editor and Git review/read-back |
| Initiative mandate, plan, and assessment | [INITIATIVES.md](INITIATIVES.md) | Maintainer accountable; Coordinator maintains | Markdown; link work proof and portfolio rulings |
| Reusable design proposal | [Process proposal](proposals/2026-09-21-portable-project-records.md), [ADR-0002](adrs/0002-decision-context-and-work-bindings.md) | Maintainer acceptance; Architect review | Proposed text and draft PR; acceptance recorded separately |
| Proof and limitations | [Decision walkthrough](examples/decision-scopes/README.md), [JSON qualification](examples/portable-records/QUALIFICATION.md) | Tester responsibility | Review/test results; no unsupported live claims |
| Other proposals | Their existing proposal files and owner branches | Existing owners | References only; no ownership transfer |

No new Check-in Desk is adopted by this index. Existing operational asks remain with their
current authority; this branch does not copy them into a competing ledger. A future portfolio
candidate creates no immediate operator ask. The earlier local HTML work preview was a
proposal/ask snapshot, not this queue's source; its temporary `WI-` labels are not these `VEL-`
identities. It must be labeled stale or refreshed through a qualified binding before being
presented as a view of this queue.

## Reference-method mapping

The [reference method](docs/MANAGEMENT-REFERENCE.md) is applied to this scoped trial through
the three source files above. Shared purpose/mandate and the role map live in this index;
portfolio selection principles and resource outlook live in the portfolio introduction;
the initiative record owns milestones, assessment, risks, and outcome evidence. Work history
and closure receipts remain in TODO and its linked proof records.

The Maintainer reviews this proposed method through the existing proposal and draft PR #14.
Those records carry the current review request and any eventual scope/acceptance ruling.
They are a declared decision route for this tranche, not a claim that a full operational Desk
or governance system has been deployed. Existing live Desk ownership is unchanged. There is
no reason to create three duplicate pending-approval asks for one Maintainer decision.

Review triggers: working-session resumption and work changes; initiative checkpoint/scope
changes; portfolio selection or resource decisions and explicit Maintainer review. This trial
uses events rather than adopting the reference's optional weekly/monthly cadences. Each
decision names its actual scope; no meeting or scheduled automation is created.

## Update, history, and recovery

The binding is Markdown under [Lightweight Work Management](docs/WORK-MANAGEMENT.md). The
working revision is the Git base commit plus the reviewed working diff; committed revisions
are identified by SHA. Read the current branch, worktree, and source before editing. One
coordinating editor owns this worktree at a time; Git does not lock concurrent live editors.
Another agent must take a handoff or reconcile changed versions before writing.

Record state/scope changes with their actor and reason, check dependencies/authority/proof,
save, and read back the source. Commits record the request/change identity; their hashes and
parents identify resulting/starting saved revisions. On retry, reconcile that identity and
the saved source before writing again. This foundation's request is
`VEL-PF-1-20260921-foundation`; its closeout is a separate recorded change.
The standing-method follow-up uses `VEL-PF-1-20260921-method`.
Retain prior closures in Git and the item history. These
Markdown files are the current view; no TODO HTML generation is declared. The JSON helper is
not this queue's writer. For coupled decisions, preserve the authoritative ruling before
updating dependent work and record a pending update if interrupted.

Git commits and the remote feature branch retain this tranche's reviewed history. Before
recovery, preserve any newer working or remote changes and reconcile through a corrective
commit; do not reset over another editor's work. This is ordinary versioned recovery, not a
qualified operational backup or distributed-lock service. Resolve the final pin from the
accepted commit/tag if the project adopts these development contracts beyond this branch.
