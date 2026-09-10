# ADR-<number>: <one architectural decision>

> Optional record format for the existing [Architect review responsibilities](../docs/ROLE-AUTHORITY.md#architect)
> and [artifact authority boundaries](../docs/ARTIFACT-AUTHORITY-BOUNDARIES.md).
> Use one record per significant decision, or map these fields to the project's existing ADR format.
> This template introduces no new approval role or universal ADR requirement for every change.
> Delete this guidance block when instantiating the record.

- Status: Proposed | Accepted | Rejected | Deprecated | Superseded
- Date:
- Decision owner:
- Architect review: <reviewer, evidence, date, or pending>
- Acceptance: <authorized owner, decision record, reviewed revision, date, or pending>
- Related issue / tranche:
- Supersedes / superseded by:

## Context

What problem requires a durable decision? Record relevant evidence, constraints, unknowns,
and the current system behavior. Keep facts separate from assumptions.

## Options And Tradeoffs

Describe the viable alternatives, including retaining the current design where relevant.
Explain their consequences for trust boundaries, ownership, operability, and reversibility.

## Decision And Rationale

State the proposed or accepted decision and why it fits the context. Make its scope and
non-goals clear. A proposed decision is not permission to change a protected contract.

## Invariants And Enforcement

- <load-bearing invariant>
  Enforcement: <PREVENT|DETECT|RUNTIME_GUARD + binding location and evidence>
- <unbound invariant>
  Enforcement: HOPE — deferred to <named owner> by <date or gate>; open obligation.

Use the [ADR enforcement convention](adr-enforcement-field.md) and link the corresponding
[System Invariant Register](system-invariant-register.md) entries. Identify cross-subsystem
invariants and the side responsible for binding each one. Apply the existing proof model's
triage and deferral rules; an accepted ADR does not close an unbound invariant.

## Consequences And Delivery

Record benefits, costs, risks, and follow-up obligations. Link the implementation tranches,
claim-appropriate proof, and any migration or recovery plan. Architecture acceptance does
not authorize a separate live mutation; use the project's promotion authority path.

## Reconsideration And Supersession

State the evidence or changed conditions that would justify revisiting this decision.
Preserve the context and rationale of an accepted decision when replacing it. Record the
replacement decision and link both records rather than silently overwriting the old rationale.
Updating an enforcement pointer does not itself change the decision or its acceptance status.

## Lineage

This format follows the established ADR tradition, including Michael Nygard's
[Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
(2011). Velocity adds links to its existing authority, proof, enforcement, and delivery records;
it does not claim to have originated ADRs.
