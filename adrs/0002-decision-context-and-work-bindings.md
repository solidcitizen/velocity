# ADR-0002: Decision Context and Work Bindings

- Status: Proposed; implementation authorized, policy acceptance pending
- Date: 2026-09-21
- Authority owner: Velocity Maintainer
- Proposal: [Decision-aware work and portable records](../proposals/2026-09-21-portable-project-records.md)

## Context

An artifact format cannot define the whole work-management contract. `TODO.md` can already
be a project's tracker, while a sophisticated board can still lack a clear investment mandate.
All efforts participate in wider decisions even when one owner combines the responsibilities.
Velocity needs this context without turning a lightweight queue into a portfolio product.

## Options

1. Require the JSON Work Board as the starter system. This unnecessarily migrates existing
   Markdown queues and confuses the meaning of work with its storage and presentation.
2. Expand every work item into a complete portfolio/business-case record. This duplicates
   authority, adds upkeep, and burdens small efforts with irrelevant detail.
3. Define decision context and common work semantics, with conditional management records and
   Markdown, structured-file, or external bindings. This is the proposed approach.

## Proposed decision

Adopt [Decision Scopes](../docs/DECISION-SCOPES.md) and
[Lightweight Work Management](../docs/WORK-MANAGEMENT.md) within the opt-in portability profile.
Keep strategy, portfolio investment, initiative development, and work execution connected but
distinct. Let work inherit an explicit context. Keep operations recurrence orthogonal.

Make Markdown a first-class authoritative binding. Keep the JSON pilot's renderer and guarded
writer as one implementation, not a required migration path. A future rendered TODO adapter
is a separately qualified capability. Preserve one authority for work and for each ruling.

Record strategic goal-setting as a future portfolio opportunity. Define the interface to
accepted goals now; defer methods for creating, selecting, and revising goals. This does not
delegate goal adoption or expand agent authority.

## Invariants and enforcement

| Invariant | Enforcement and limitation |
| --- | --- |
| Reading context or proposing a goal cannot grant decision authority | DETECT: explicit context/authority review at commitment and protected actions. Host/service enforcement remains the adopting project's responsibility. |
| A view or AI switch cannot create a second writable queue | DETECT: artifact-index binding and handoff review. RUNTIME_GUARD: the existing JSON helper refuses work writes after external cutover; direct editors are outside that guard. |
| Work completion, stage advancement, and investment approval stay distinct | DETECT: state/decision review and the published counterexample walkthrough. No runtime semantic enforcement is claimed for Markdown. |
| Parent changes retain history and revalidate affected work | DETECT: named decision owner and revision-linked impact review; no automatic propagation engine is supplied. |
| New requirements do not silently invalidate older adopters | DETECT: development/adoption labels and release compatibility review by the Maintainer. |

## Consequences and reconsideration

Small projects can keep one TODO and a short context block. Larger efforts can connect existing
portfolio and program systems without copying their contents. Lightweight file editing remains
dependent on cooperating writers and review. Universal mandatory adoption, automated strategy,
distributed concurrency, and a live external connector need further design and proof.

Revisit after actual cross-tool continuation, a representative management decision pilot, or
evidence that inherited context cannot express a real authority boundary. The related Entity
Development Lifecycle proposal remains separately owned and unaccepted; reconcile its initiative
and executive views before accepting overlapping contracts.

## Review and proof

Architect review is a named responsibility in this implementation session, separate from the
drafting pass; it is not independent acceptance. The final review and scenario evidence are in
the [decision-scope walkthrough](../examples/decision-scopes/README.md). Maintainer acceptance,
version assignment, merge, and release are not recorded by this ADR.
