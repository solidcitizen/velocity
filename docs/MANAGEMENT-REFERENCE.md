# Work, Initiative, and Portfolio Reference Method

The standing reference method for the proposed [Portable Project Records](PORTABLE-PROJECT-RECORDS.md)
profile. Status: development, pending Maintainer acceptance and release. This defines the
baseline for that profile's adopters, not a new requirement for prior conformant projects.

Work, initiative, and portfolio are **management levels** under [Decision Scopes](DECISION-SCOPES.md).
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

Use the [work template](../templates/work-tracker.md) and
[decision/management record templates](../templates/decision-records.md). Typical file homes
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
umbrella here, not a claim that every initiative is a PMI program or that a work item is a project.

## A management view and a Check-in Desk have different jobs

Each level needs a readable management view of its baseline records. Markdown can supply it;
three additional dashboards are not required. A Work Board shows execution, an initiative
view shows outcome progress, and a portfolio view shows choices and resource/value tradeoffs.

The [Check-in Desk](../templates/executive-checkin-desk.md) is the action/decision surface for
its declared operator and responsible lead. It presents what needs an answer or an operator
action, plus the decision history. Keep ordinary status narrative in the management views,
as the existing Desk contract requires.

**Default for a compact adoption: one shared Desk across the three levels when the decision
owner, accountable lead, and access boundary are the same.** Identify the management level
and affected record in the ask. Provide level-specific views if useful; a filter does not
create a new authoritative ledger. Without a Desk adoption, use a durable pending-decision
section and ruling history in the existing records. Chat alone is never the standing record.

Create separate decision surfaces when there are distinct decision authorities, separate
accountable leads, confidentiality boundaries, or enough volume/different review cycles to
justify them. Portfolio committees and program sponsors may warrant distinct forums even if
their UI is shared. One person with several hats can use one surface while naming the hat
under which each decision is made.

A governance board is a person/group with decision rights; a visual board is a presentation.
A dashboard cannot establish quorum, delegated authority, or a decision. If a committee owns
the ruling, keep its actual approval evidence in the declared governance record and link it.

For human–agent work, distinguish the executor from the accountable owner. Map an agent's
role to a named human owner and escalation route in the context or
[role brief](../templates/role-brief.md); retain the agent's own identity in execution history.
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

The current JSON Desk has no scope-filtering UI, portfolio roll-up, committee workflow, or
automatic cross-desk synchronization. Use existing prose/reference fields for context and
the documented pointer convention; do not add undeclared schema fields or claim those future
integrations exist. This method does not modify the shared renderer or accept the separately
owned Entity Development Lifecycle board proposal.

## Review and escalation contract

Each adopting effort declares the responsible reviewer, cadence or event trigger, information
needed, decisions available within authority, escalation destination, and where the ruling
and resulting actions are recorded. A lightweight starting cadence is:

| Level | Reference review trigger | Result of the review |
| --- | --- | --- |
| Work | At working-session resumption and any state/blocker change; periodically triage the queue while work is active. | Next authorized action, accurate wait/owner, or closure proof. |
| Initiative | At milestones/gates or material changes; a weekly review is a starting option for active efforts. | Updated outcome forecast, risk response, change/gate decision, or a specific upstream ask. |
| Portfolio | At selection/resource decisions or material changes; a monthly review is a starting option for an active portfolio. | Revalidated selection, priority, allocation, continuation posture, and benefit/risk outlook. |

Cadences are tailoring defaults, not PMI-prescribed intervals or scheduled automations.
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

## What PMI informs, and what Velocity defines

Primary sources reviewed 2026-09-21:

| PMI source | Supported point | Use here |
| --- | --- | --- |
| [PMBOK Guide, Eighth Edition (2025)](https://www.pmi.org/standards/pmbok) | PMI's public overview emphasizes organizational value, accountability, and adapting practices/tools to context. | Keep the baseline useful at small scale; tailor the machinery. |
| [Governance of Portfolios, Programs, and Projects: A Practice Guide (2016)](https://www.pmi.org/standards/governance) | Its stated purpose distinguishes governance levels while identifying common elements. | Shared decision discipline with level-specific responsibilities. |
| [The Standard for Program Management, Fifth Edition (2024)](https://www.pmi.org/standards/program-management-fifth-edition) | Related projects are coordinated toward benefits beyond their individual contributions. | Initiative/program reviews assess outcomes and dependencies, not just task counts. |
| [The Standard for Portfolio Management, Fourth Edition (2017)](https://www.pmi.org/standards/for-portfolio-management) | Portfolios group projects, programs, and other activities around strategic objectives; the standard is principle-based. | Portfolio decisions concern the mix of efforts and strategic contribution. |
| [The Standard for Artificial Intelligence in Portfolio, Program and Project Management (2026)](https://www.pmi.org/standards/artificial-intelligence) | Its overview covers applying AI and managing AI initiatives, with technology-independent guidance and human oversight. | AI governance is established adjacent work that this method must acknowledge. |
| [PMI's human–agent RACI guidance (2026)](https://www.pmi.org/blog/stakeholder-management-raci) | Agents may perform bounded work; humans retain accountability, approval and escalation ownership. | Separate executor identity from accountable ownership and document decision rights. |

The standards references above are public publication overviews, supplemented by PMI's
practitioner guidance, not a clause-by-clause review of the full standards. They support
differentiated governance and tailoring; they do not establish a
requirement for three software boards. The artifact baseline, review loop, filenames, cadence
options, and shared-Desk default above are **Velocity's reference design**, informed by those
sources. No PMI compliance or certification claim is made.

PMI is already adapting practice for teams containing AI agents. A complete comparison with
its AI standard is needed before claiming that Velocity fills an uncovered gap in autonomous
entity governance or strategic goal-setting. The public sources reviewed here do not establish
that PMI supplies, or lacks, a complete lifecycle for entities forming and pursuing their own
goals. Keep that question open in the future discovery scope.

See the [scenario review](../examples/decision-scopes/README.md#reference-method-review) and
Velocity's [own artifact mapping](../ARTIFACTS.md) for the worked application and proof limits.
