# Decision Context and Management Records

Optional record support for [Decision Scopes](../docs/DECISION-SCOPES.md). Use existing records
where they already carry this information. Start with the context block; create portfolio,
initiative, or gate records only when the decision needs them. Empty example fields are not
approvals. Populated records belong in the adopting project's declared workspace/system.
The [standing reference method](../docs/MANAGEMENT-REFERENCE.md) defines the baseline coverage
and how records can be combined. Artifact coverage does not require a separate file or Desk
for every level.

## Project decision context

- Purpose / accepted outcome: `<charter or concise statement; owner>`
- Strategy source: `<record and revision; or stated purpose with its limits>`
- Portfolio / selection authority: `<upstream record and owner, or combined project owner>`
- Initiative / plan: `<record and owner; or bounded project goal serves this scope>`
- Current authority / capacity: `<delegation or decision, allowed scope/resources/time, assumptions>`
- Escalate when / to: `<boundary and decision owner; route through Desk if adopted>`
- Next review / gate: `<event/date and owner, or no formal gate with a change trigger>`
- Record locations / audience: `<artifact index; private/public boundary>`
- Decision surface: `<one shared Desk within declared ownership/access, or existing request/decision record>`
- Review arrangement: `<reviewer, cadence/event, evidence needed, decision rights and escalation>`
- Human/agent role map: `<accountable human owner; executing agents and their delegated scope>`
- Unresolved context: `<unknowns, affected decisions, owner/next disposition>`

## Portfolio mandate and review

- Scope / strategic direction / accountable portfolio owner:
- Selection principles and decision rights: `<how alternatives are judged; no invented scoring>`
- Resource boundary: `<approved capacity/envelopes, assumptions and source records>`
- Component inventory: `<candidate and selected effort IDs; posture, owners, parent links>`
- Allocation/outlook: `<commitments versus capacity; actual/forecast source, unknowns>`
- Value/risk review: `<outcome evidence, cross-component dependencies and tradeoffs>`
- Review trigger / next decision / authoritative ruling location:

This block can be the introduction to `PORTFOLIO.md` or inherited from an existing charter.
Portfolio components use the opportunity/investment shape below; do not duplicate their
initiative plans or execution queues here.

## Portfolio opportunity or investment

- Stable ID / title:
- Accountable owner:
- Outcome / strategic relationship: `<why consider this; distinguish proposed from accepted goals>`
- Posture: `<candidate / invest / sustain / hold / wind down, or mapped local meaning>`
- Decision status and authority: `<proposed / accepted / superseded / declined; actual ruling link>`
- Stage / evidence so far: `<unknown is allowed>`
- Authorized scope / capacity: `<none for an unselected candidate; actual envelope for active work>`
- Options / tradeoffs: `<including defer or stop when relevant; estimates labeled with confidence>`
- Next decision / owner / trigger: `<what must be decided before further investment>`
- Linked initiatives / work / proof: `<do not invent delivery tasks for a future candidate>`
- History: `<dated changes and source; preserve superseded decisions>`

## Initiative or program

- Stable ID / title / owner:
- Mandate / accountable sponsor / executing lead:
- Outcome, intended beneficiary, and evidence of success:
- Parent goals / portfolio decisions and revisions:
- Scope / exclusions / dependencies:
- Stage and next milestone or gate:
- Current authorized envelope / capacity assumptions:
- Material risks / uncertainties and owners:
- Current assessment: `<as-of/source revision, progress, forecast, confidence and next decision>`
- Benefit review: `<measure/baseline/target/evidence and owner; unknown or not yet observed>`
- Work source / operating handoff:
- Review trigger / change authority / decision history:

One initiative record may cover a project. Several initiatives may belong to one program.
Use relationships that reflect actual responsibility; record structures need not mirror an
organization chart. Multiple contributors do not remove the need for an accountable owner.
Keep delivery evidence distinct from outcome/benefit evidence. A brief rationale and capacity
assumption can suffice for a small initiative; use a fuller business case where warranted.

## Stage or investment decision

- Stable decision ID / affected scope:
- Decision level: `<work / initiative / portfolio; classify the ruling requested, not its origin>`
- Status: `<proposed / accepted / superseded / declined>`
- Owner / authority basis:
- Current stage / requested next stage or action:
- Evidence / uncertainty: `<outcome, feasibility, alternatives, resources, risk as relevant>`
- Options and recommendation: `<go / hold / redirect / stop or local equivalents>`
- Requested scope / capacity / resource commitment and limits:
- Actual ruling / rationale / conditions: `<only after authorized decision; canonical ledger link>`
- Effective revision / date / review or expiry trigger:
- Affected work / dependencies / revalidation disposition:

If the Desk owns the ruling, link its ledger here. If another governance system owns it, link
that record from the Desk's closure. Proposals, recommendations, accepted rulings, and proof
of execution remain distinct. Routine work already covered by an envelope needs no new gate.
Keep the decision level with the ruling. Independent scope and investment authorizations use
linked requests on the shared board; one decision must not stand in for both authorities.
