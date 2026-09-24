# Management Reference (worked example)

A worked reference design, kept as an example rather than as policy: one way to lay out work,
initiative, and portfolio records, their reviews, and where their decisions go. Nothing here is
required at any adoption scope.

The standing reference method for the experimental [Portable Project Records](../../templates/portable-project-records.md)
profile, released in v1.9.0. See [experimental adoption](../../templates/portable-project-records.md#adopting-the-profile-in-a-project). This defines the
baseline for that profile's adopters, not a new requirement for prior conformant projects.

Work, initiative, and portfolio are **management levels** under [Decision Levels](../../templates/decision-levels.md).
They do not rename Velocity's execution lanes or L0–L5 layers. Strategy supplies accepted
direction to these levels; strategic goal-setting remains a separate future design effort.

## The standing method

At each level, maintain a purpose and mandate, an ordered inventory or plan, a current
evidence-backed assessment, and a route for decisions with retained rulings. Repeat this loop:

1. **Frame.** Read the accepted purpose, current parent decisions, owners, capacity assumptions,
   and authority boundaries. Identify the authoritative records and their revisions.
2. **Select and authorize.** Classify an input at the level where its decision belongs. A
   potential investment enters the portfolio as a candidate; an action within existing scope
   can enter the work queue. The appropriate owner selects scope and resources. Capture is
   not a commitment, and a task's priority is not an investment authorization.
3. **Plan and execute.** Translate authorized outcomes into initiative milestones and bounded
   work. Carry the governing decision references downward. Act within the envelope and route
   exceptions to the nearest owner with the needed authority.
4. **Verify and assess.** Record completion proof at work level, progress toward outcomes at
   initiative level, and value/capacity/risk implications at portfolio level. A completed task
   or delivered output alone does not establish realized benefit.
5. **Decide and adjust.** Review on the declared cadence or material change, record the ruling,
   revalidate affected work, and refresh its views. Continue, change, hold, or stop within the
   applicable authority. Retain history and unresolved obligations through closure/handoff.

Feedback travels upward as evidence, forecasts, risks, and decision requests. Decisions travel
downward as scoped authority, priorities, conditions, and limits. Upward reporting should not
copy every task; downward direction should not erase the responsibility of the delivery owner.

## Baseline artifacts by level

These are **logical artifacts**, not a minimum file count. A short section or linked existing
system can satisfy a row. Name its owner and canonical location in the shared artifact index.

| Level and question | Baseline records | Standing management view | Decision coverage |
| --- | --- | --- | --- |
| **Work:** What action is next, what blocks it, and what proves it done? | Authoritative queue (`TODO.md` or mapped tracker); bounded scope/acceptance inline or in a linked issue/tranche; completion evidence and history; dependency/decision references. | Ready/active/waiting/closed work, owner, next action, blockers, and proof. | Local choices within delegation are made and recorded where consequential. Exceptions route to the responsible owner. |
| **Initiative:** Are we achieving the intended outcome within our mandate? | Initiative brief/charter; plan or roadmap with milestones, dependencies and material risks/issues; current status and outcome/benefit evidence; stage/change decisions and operating handoff. | Outcome, owner, stage, next milestone, capacity/forecast, material risk, evidence/confidence, and next decision. | Sponsor/initiative owner handles scope and stage choices within its mandate; investment or cross-initiative exceptions go upstream. |
| **Portfolio:** Is this the right mix of efforts for our goals and available capacity? | Mandate and selection principles; inventory of candidates and authorized initiatives/other components; capacity/allocation outlook; value/risk review and selection/continuation decisions. | Strategic contribution, relative priority/posture, resource commitments versus capacity, material dependencies, outcome evidence, and pending investment choices. | Declared portfolio authority selects, prioritizes, allocates, continues, redirects, holds, or stops components. Goal changes route to the goal owner. |

All levels inherit the project/organizational charter where sufficient. Each has access to a
decision/request ledger, but the same ledger may serve all three. A consequential ruling
records its owner, authority, affected scope, rationale/evidence, conditions, date/revision,
and affected next actions. Routine actions already governed by that ruling do not need new
decision records for every execution step.

Use the [work template](../../templates/work-tracker.md) and
[decision/management record templates](../../templates/decision-records.md). Typical file homes
are `TODO.md`, `INITIATIVES.md` (or one file per initiative), and `PORTFOLIO.md`. Context may live
in a charter or artifact index. Rulings may live in the existing Desk ledger, an external
governance system, or a declared Decisions section. These names are defaults, not a prescribed
folder structure. Do not create a second decision log when one already owns the rulings.

An initiative brief always states why the effort matters and how its outcome will be judged.
Expand it into a business case, benefits plan, integrated schedule, resource plan, or formal
risk register when the decision exposure warrants it. A small effort can state assumed
maintainer capacity; it need not invent money estimates. A recurring function can maintain an
operating mandate and obligation register alongside its improvement initiatives.

For programs, coordinate related projects and their combined benefits. For a single project,
one initiative brief can carry its mandate and plan. “Initiative” is Velocity's convenient
umbrella here, not a claim that every initiative is a program or that a work item is a project in
any external standard's sense.

## A management view and a Check-in Desk have different jobs

Each level needs a readable management view of its baseline records. Markdown can supply it;
three additional dashboards are not required. A Work Board shows execution, an initiative
view shows outcome progress, and a portfolio view shows choices and resource/value tradeoffs.

The [Check-in Desk](../../templates/executive-checkin-desk.md) is the action/decision surface for
its declared operator and responsible lead. It presents what needs an answer or an operator
action, plus the decision history. Keep ordinary status narrative in the management views,
as the existing Desk contract requires.

**The reference default is one Check-in Desk within its declared ownership and access scope,
with every decision request qualified as Work, Initiative, or Portfolio.** These are decision
levels, separate from Velocity's execution lanes. The same board retains its existing Decide,
Do, Decided by the team, Already answered, and How to reply sections and one CK ID sequence.
Management levels do not create three boards or three approval queues.

| Decision level | Question being decided | Example |
| --- | --- | --- |
| Work | What happens to bounded work within the current mandate? | Resolve a reserved priority choice or accept a work result. |
| Initiative | What outcome, scope, plan, or development stage should this effort pursue within its investment envelope? | Change the pilot outcome or pass a delegated milestone gate. |
| Portfolio | Which efforts merit selection, resources, continuation, or a changed investment envelope? | Fund discovery, reallocate capacity, hold, or stop an investment. |

Classify the **ruling requested**, not the task that discovered the need. A work item needing
additional investment raises a Portfolio request. A gate between stages may be Initiative or Portfolio
depending on the authority exercised. Each ask names one primary level, its affected record,
the decision owner/hat and authority basis, options/recommendation, and what waits. Link other
affected levels; the label neither grants authority nor creates a new gate for delegated work.

In JSON, use `decision_level: work | initiative | portfolio`; the shared renderer displays
**Decision level**. The profile requires it on all open Decide entries, including pointers,
and preserves it with the ruling. Do and team entries may also carry it. In a Markdown or
external decision record, carry the same explicit field and values. Without a Desk adoption,
use a durable pending-decision section and ruling history in the existing records. Chat alone
is never the standing record. See the [synthetic unified Desk](../decision-levels/desk.json).

Different hats, review cadences, or record levels alone do not call for additional boards.
Separate desks are appropriate only where authority ownership or access boundaries prevent
one shared source under one responsible lead. Distinct decision forums can use the same
surface where its ownership/access contract permits. One person with several hats names the
hat under which each ruling is made. Existing separately owned desks are not merged implicitly.

A governance board is a person/group with decision rights; a visual board is a presentation.
A dashboard cannot establish quorum, delegated authority, or a decision. If a committee owns
the ruling, keep its actual approval evidence in the declared governance record and link it.

For human–agent work, distinguish the executor from the accountable owner. Map an agent's
role to a named human owner and escalation route in the context or
[role brief](../../templates/role-brief.md); retain the agent's own identity in execution history.
State what it may recommend, execute within delegation, or route for approval, and how to
pause or recover its work. This does not require a fresh approval for each authorized action.

Separate desks preserve the current ownership rule: only each desk's lead writes its source.
An escalated question has one owning ask; another desk can hold an `owned_by` pointer. The
pointer closes with the owner under the existing contract. Do not duplicate the same question
at three levels, count the pointers as three pending decisions, or authorize one agent to
write every desk just because it can read them. Existing desks are not merged automatically.

One action may still need several independent authorizations, such as an outcome/scope ruling
and a funding decision. Keep these as linked, distinct decisions with their own owners and
conditions. One ask per question prevents duplicates; it does not collapse genuinely separate
decision rights or release work while another required authorization is missing.

The JSON support validates and displays decision levels; the optional strict check requires
qualification of open decisions. Legacy standalone desks remain valid without the field,
and unlabeled historical rulings are not retrospectively guessed. The file helper applies
the strict profile check and guards retention on closure. Meaning, authority, and agreement
with an owning desk's classification still require review.

No level filter, portfolio roll-up, committee workflow, or automatic cross-desk synchronization
is supplied. Level labels do not accept the separately owned Entity Development Lifecycle
board proposal.

## Review and escalation contract

Each adopting effort declares the responsible reviewer, cadence or event trigger, information
needed, decisions available within authority, escalation destination, and where the ruling
and resulting actions are recorded. A lightweight starting cadence is:

| Level | Reference review trigger | Result of the review |
| --- | --- | --- |
| Work | At working-session resumption and any state/blocker change; periodically triage the queue while work is active. | Next authorized action, accurate wait/owner, or closure proof. |
| Initiative | At milestones/gates or material changes; a weekly review is a starting option for active efforts. | Updated outcome forecast, risk response, change/gate decision, or a specific upstream ask. |
| Portfolio | At selection/resource decisions or material changes; a monthly review is a starting option for an active portfolio. | Revalidated selection, priority, allocation, continuation posture, and benefit/risk outlook. |

Cadences are tailoring defaults, not intervals prescribed by any external standard, and not scheduled automations.
Do not wait for the next meeting when an authority boundary, material risk, or imminent
commitment needs action. A small owner-led project may combine all reviews in one check-in.
No-change reviews can record the reviewed revision and unchanged disposition succinctly.

Escalate to the nearest authority that can decide the issue. State the precise question,
options/recommendation, supporting evidence and uncertainty, consequence/deadline, and exact
work that waits. If the same individual owns both levels, retain the distinction between
the two decision rights without creating an artificial approval chain. Silence grants nothing.

Every management view names its as-of date/source revision and separates verified results,
estimates, and unknowns. Portfolio summaries retain the boundary between approved resources,
commitments, actual use, and forecasts; they can link the financial/resource system. Do not sum
ordinal task sizes into a budget or infer benefits from the percentage of tasks closed.
Refresh affected views after decisions; preserve unrelated authorized work and obligations.

## Sources

The established management practice that informed this reference design is credited in the
[lineage document](../../LINEAGE-AND-ADJACENT-WORK.md#management-and-ai-practice-reviewed-2026-09-21).
The artifact baseline, review loop, filenames, cadence options, and shared-desk default are
Velocity's own design; no certification or compliance with any external standard is claimed.

See the [scenario review](../decision-levels/README.md#reference-method-review) and
Velocity's [own artifact mapping](../velocity-self-adoption/ARTIFACTS.md) for the worked application and proof limits.
