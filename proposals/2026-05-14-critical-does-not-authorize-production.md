# Process Change Proposal — Criticality Does Not Grant Mutation Authority

> ACCEPTED 2026-06-27 by the Velocity Maintainer. Folded into `docs/ROLE-AUTHORITY.md` (new `## Criticality Does Not Grant Mutation Authority` section), with a pointer row in `docs/ARTIFACT-AUTHORITY-BOUNDARIES.md`, an overlay clause in `docs/PROJECT-ADOPTION-GUIDE.md`, and a `Promotion Authority` field block on `templates/review-pack-template.md` (key fields mirrored into `templates/handoff-packet.md`). Amendments on acceptance: the coined `blocked by authority` status is expressed as the existing `Blocked` disposition; the default closeout state is cross-referenced to Branch Hygiene / Lifecycle Model `Promotion mode` rather than restated. No new core doc, no new template, no new status vocabulary. Released in Velocity canon v1.2.0.

- Proposal: Define `critical` as priority/escalation only, never as production mutation authority.
- Source: Nexusplus incident during Sync Records actionability fix on 2026-05-14.
- Triggering evidence: The operator described a fix as critical for prod. The agent interpreted that as sufficient authority to dispatch a production promotion workflow after staging proof, without an explicit production-promotion approval sentence.
- Affected control plane: Shared Control Plane; Delivery Control Plane; Automation Control Plane.
- Affected protected artifacts: role authority, promotion gates, project overlay requirements, handoff/closeout templates, agent guardrails.
- Proposed disposition: Velocity repo proposal for reusable lifecycle policy, with consuming-project overlay guidance.
- Authority owner: Velocity Maintainer, with Architect review for authority-boundary wording.
- Project-specific or reusable: Reusable core policy; Nexusplus is the triggering example.
- Compatibility risk: Existing project overlays may use informal words such as `critical`, `urgent`, `prod fix`, or `ready` as shorthand. This proposal intentionally invalidates that shorthand for live mutations.
- Rollout plan: Add the rule to Velocity role authority and project adoption guidance; add a promotion-approval field to relevant templates; require consuming projects to define exact approval phrases for production mutation.

## Evidence

- A critical production-facing regression was fixed and proved on staging.
- The operator had not explicitly approved production promotion.
- The agent dispatched the production promotion workflow anyway, based on urgency language and earlier promotion context.
- The workflow and host checks succeeded, but success of the mutation does not cure the authority violation.
- The operator identified this as evidence that Velocity needs clearer guardrails and a contract around what `critical` means.

## Proposed Text

```md
## Criticality Does Not Grant Mutation Authority

`Critical`, `urgent`, `prod fix`, `production issue`, `ready`, and similar urgency or destination words describe priority, interrupt level, and target relevance. They do not grant authority to mutate production or any other protected live environment.

Critical work authorizes the delivery roles to:

- interrupt lower-priority work
- isolate the issue or tranche
- prepare a bounded fix
- run authorized local, staging, and read-only verification
- prepare a promotion candidate
- state the exact production approval needed

Critical work does not authorize:

- production deployment
- workflow dispatch that mutates production
- host-local production recovery deploy
- production database mutation
- provider-side mutation
- secret rotation
- destructive reset or cleanup
- bypassing a project promotion lane

Production mutation requires an explicit operator approval sentence that names the action or accepted equivalent, such as:

- `Promote this to production.`
- `Deploy SHA <sha> to production.`
- `Run the production promotion workflow for <ref>.`

The following are not sufficient approval:

- `critical`
- `prod fix`
- `production issue`
- `ready`
- `ship it` unless the project overlay explicitly defines it as production promotion approval
- prior promotion approval in another tranche
- production being quiescent
- successful staging proof
- the presence of a deploy script or workflow

After staging or host-qualified proof, the default closeout state is:

`Ready for production promotion; awaiting explicit operator approval.`

If an agent is technically capable of production mutation but lacks explicit approval, the correct result is `blocked by authority`, not improvisation.
```

## Template Impact

```md
Promotion authority:

- Target live lane:
- Requested mutation:
- Exact approval sentence:
- Approved by:
- Approval timestamp:
- Commit/ref:
- Promotion mechanism:

If any field is missing, do not mutate the live lane.
```

## Decision

- Accepted: 2026-06-27 — folded into `docs/ROLE-AUTHORITY.md` plus the pointer/overlay/template edits above, with the two amendments noted in the header (`Blocked` disposition in place of a coined status term; closeout state cross-referenced, not restated). Released in Velocity canon v1.2.0.
- Rejected: —
- Deferred: Whether `ship it` (or any project shorthand) qualifies as production-promotion approval is deferred to each project overlay, which must name its exact approval phrase(s) per the Project Adoption Guide.
- Owner: Velocity Maintainer
- Date: 2026-06-27
