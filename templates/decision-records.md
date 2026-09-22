# Decision Context and Management Records

Optional record support for [Decision Scopes](../docs/DECISION-SCOPES.md). Use existing records
where they already carry this information. Start with the context block; create portfolio,
initiative, or gate records only when the decision needs them. Empty example fields are not
approvals. Populated records belong in the adopting project's declared workspace/system.

## Project decision context

- Purpose / accepted outcome: `<charter or concise statement; owner>`
- Strategy source: `<record and revision; or stated purpose with its limits>`
- Portfolio / selection authority: `<upstream record and owner, or combined project owner>`
- Initiative / plan: `<record and owner; or bounded project goal serves this scope>`
- Current authority / capacity: `<delegation or decision, allowed scope/resources/time, assumptions>`
- Escalate when / to: `<boundary and decision owner; route through Desk if adopted>`
- Next review / gate: `<event/date and owner, or no formal gate with a change trigger>`
- Record locations / audience: `<artifact index; private/public boundary>`
- Unresolved context: `<unknowns, affected decisions, owner/next disposition>`

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
- Outcome and evidence of success:
- Parent goals / portfolio decisions and revisions:
- Scope / exclusions / dependencies:
- Stage and next milestone or gate:
- Current authorized envelope / capacity assumptions:
- Material risks / uncertainties and owners:
- Work source / operating handoff:
- Review trigger / change authority / decision history:

One initiative record may cover a project. Several initiatives may belong to one program.
Use relationships that reflect actual responsibility; record structures need not mirror an
organization chart. Multiple contributors do not remove the need for an accountable owner.

## Stage or investment decision

- Stable decision ID / affected scope:
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
