# Decision Scopes

Development contract for the opt-in [Portable Project Records](PORTABLE-PROJECT-RECORDS.md)
profile. Acceptance and release are pending. Earlier adopters are not re-judged.

Velocity's direction is to accelerate evidence-backed decision-making throughout an entity's
work: establishing direction, choosing investments, developing outcomes, and executing work.
An entity can be a product, organization, household, or other governed effort. Its authority
and obligations come from its charter and accountable owners, not from this vocabulary.

## Four connected scopes

| Decision scope | Question it owns | Typical authoritative record | Lightweight participation |
| --- | --- | --- | --- |
| Strategy | What outcomes should we pursue, for whom, and within which values and constraints? | Charter, mission, accepted goals | Link the existing purpose and goal owner. Goal-setting methods are future work. |
| Portfolio / investment | Which efforts merit starting, continuing, changing, or stopping, and what capacity may they consume? | Portfolio decisions, investment envelopes, business cases where needed | Name the selection authority and existing capacity assumption; a separate portfolio system is optional. |
| Initiative / program / project | How will this effort achieve its outcome, across stages, dependencies, and risks? | Initiative plan, roadmap, program plan, gate decisions | A bounded project goal and next review can be sufficient. |
| Work execution | What action is ready, who owns it, what blocks it, and what proves completion? | `TODO.md`, structured Work Board, or a chosen tracker | Use the [work-management contract](WORK-MANAGEMENT.md) in one authoritative queue. |

These are decision scopes, not mandatory organizational tiers. A small project may combine
their ownership and records. A large program may have several nested initiatives and an
upstream portfolio outside its own workspace. Cross-cutting work may link several outcomes;
it still names one accountable owner and its applicable constraints. Do not invent a parent
initiative merely to fill a hierarchy.

Scopes do not replace the [L0–L5 abstraction layers, lanes, or modes](LIFECYCLE-MODEL.md).
For example, architecture work is still L1 whether its consequences concern one project or
an entire portfolio. No new Velocity role or control plane is introduced. A CFO, PMO, sponsor,
or committee can be a project's named decision authority without becoming a universal role.

Recurring operations are an additional work pattern across these scopes, not another rung
in this hierarchy. A continuing service or function may have a mandate, an operating envelope,
improvement initiatives, and recurring obligations alongside discrete projects.

The [standing reference method](MANAGEMENT-REFERENCE.md) defines baseline artifacts and the
review loop for work, initiatives, and portfolios. It requires decision coverage at each
level while allowing one shared Desk where owners, responsibility, and access align.

## Awareness is universal within the adopted profile; machinery is conditional

Every adopting effort declares its decision context once in its overlay, charter, or artifact
index. Work inherits that context and links a more specific record only when needed. Use the
[decision-record templates](../templates/decision-records.md), or equivalent existing records,
to identify:

- purpose or accepted outcome and its accountable owner;
- the nearest governing initiative and portfolio/selection authority, combined locally or
  linked upstream as appropriate;
- the authority and resource/capacity envelope for the current work, including assumptions;
- what requires escalation, who can decide it, and the next relevant review or gate;
- the authoritative records and their revisions, with unresolved context marked unknown.

A valid small-project declaration might be: “The project owner sets direction and priorities;
this work uses existing maintainer capacity; new spend or external commitments need an owner
decision.” It does not need invented cost estimates, a CFO, a business case, or a gate calendar.
An assumed capacity is recorded as an assumption, not fabricated as an approved budget.
Missing upstream information does not create unlimited authority. Existing independently
authorized work can continue; the affected out-of-envelope commitment waits for its owner.

Scale the records with the decision's exposure, uncertainty, dependencies, and reversibility,
not just team size. A small construction effort may need stronger investment gates than a
large queue of routine maintenance. Formal resource allocation, financial modeling, and
portfolio optimization remain with the chosen management process and its authoritative system.

## Keep execution, maturity, and investment separate

| Fact | Examples | What it does not establish |
| --- | --- | --- |
| Work state | backlog, doing, blocked, done | Whether the parent effort is funded or should continue |
| Development stage | discovery, design, implementation, operation | Permission to enter or fund the next stage |
| Investment posture | candidate, invest, sustain, hold, wind down | A spend authorization or task completion |
| Decision status | proposed, accepted, superseded, declined | Whether its implementation or outcome has been verified |

Labels can differ by project. Preserve the meanings and link to the current decision.
In particular, a future portfolio opportunity is not an executable commitment, a high-ranked
backlog item is not funded, and completing all tasks does not prove the intended benefit.

Where a stage gate applies, identify the decision owner, the evidence needed, available
options, and the proposed next scope and resource envelope before the gate. Record the actual
decision, rationale, conditions, authority, and review trigger afterward. Go, hold, redirect,
and stop are meaningful outcomes; passing a technical test does not make the decision.
Templates support these records without prescribing one stage model or approval cadence.

Existing delegation and an accepted envelope permit routine work within their bounds.
Do not send every task back for investment approval. Escalate changes to outcome, scope,
resource commitments, material risk, or authority when the declared boundary is crossed.
An approved investment envelope does not waive separate deployment, privacy, or live-action
authority required by the project.

When a parent decision changes, its owner identifies affected initiatives, work, and recurring
obligations. Revalidate their next actions against the new revision and retain history.
Hold or block the affected work explicitly; do not silently delete tasks or stop unrelated
authorized obligations. A goal change cannot retroactively rewrite completion evidence.

## Decisions and the Check-in Desk

The [Check-in Desk](../templates/executive-checkin-desk.md) is an attention and decision surface
at any scope. An ask links the affected goal, investment, initiative, gate, or work record and
states the exact decision/action, owner, consequence, and next disposition. The Desk does not
select strategy, compute business cases, or grant additional authority.

For a decision made through the Desk, its ledger is authoritative; other records link to it.
If an established upstream system owns the decision, the Desk carries an ask and closes with
a pointer to that authoritative ruling. There is one decision authority and one authoritative
ruling, not two independently editable approvals. Respect audience/access boundaries when
surfacing decisions across projects. Closing an ask releases only the dependency it covers.

## AI participation and future goal-setting

AI can gather evidence, suggest goals and alternatives, prepare cases, plan bounded work, and
execute within a declared mandate. It cannot infer authority to adopt a new goal, expand an
investment envelope, change its acceptance criteria, or approve its own protected work.
An expressly delegated decision still has a scope, evidence requirement, and accountable owner.

“Self-actualization” here describes a desired organizational capability to establish goals and
find ways to achieve them. It is not a claim about model consciousness or a delegation rule.
Strategic goal formation, competing values, outcome evaluation, and goal revision require
their own future design and qualification. Velocity records that opportunity at portfolio
scope in [VEL-PF-2](../PORTFOLIO.md#vel-pf-2--strategic-goal-setting), with no execution commitment.

Evaluate acceleration through a bounded [measured pilot](../templates/automation-pilot.md):
time to a usable decision, active human effort, waiting, rework, decision quality, and resource
use, as relevant to the selected scope. More completed tasks or more autonomous actions alone
do not establish better decisions. This profile makes no measured acceleration claim.

## Lineage and compatibility

Project/portfolio separation and staged investment decisions are established management
practice. Jean Miller's [2002 PMI conference paper on portfolio management](https://www.pmi.org/learning/library/proven-project-portfolio-management-process-8503)
discusses selection, strategic alignment, and capacity. Stage-Gate's
[Discovery-to-Launch description](https://www.stage-gate.com/about/stage-gate-innovation-performance-framework/discovery-to-launch-process/)
separates evidence-producing stages from resource and continuation decisions. These sources
inform this design; this is not a claim of PMI certification, compliance, or a complete
Stage-Gate implementation. Source review: 2026-09-21.

Velocity contributes the explicit connection to role authority, proof, portable records, and
AI continuation. The [architecture proposal](../adrs/0002-decision-context-and-work-bindings.md)
records that boundary. The separate Entity Development Lifecycle proposal remains under
review; shared direction does not accept its templates or migrate its pilots. This profile's
requirements apply on adoption. Making them mandatory for all prior adopters would require a
separate compatibility decision and version assessment.
