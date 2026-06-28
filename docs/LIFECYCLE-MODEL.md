# Lifecycle Model

Velocity organizes AI-assisted software delivery by lifecycle stage, abstraction layer, lane, and mode.

## Product Lifecycle

Use this axis to describe the maturity problem in focus:

- `Requirement capture` - record the operator need, defect, ambiguity, or goal.
- `Translation` - convert the need into explicit product and system responsibilities.
- `Functional design` - define user-facing behavior, states, and edge cases.
- `Architecture` - define invariants, ownership, authority boundaries, and durable system shape.
- `System hardening` - improve resilience, observability, security, performance, and operability.
- `Stabilization` - close correctness, truthfulness, recovery, and trust gaps.
- `Operations` - observe and manage deployed runtime behavior.

## Feature Delivery Lifecycle

Use this axis to describe the stage of the work item:

- `Capture` - formalize observation and evidence.
- `Decision` - choose product, architecture, lane, or priority direction.
- `Tranche` - define bounded scope, acceptance criteria, and proof gate.
- `Implementation` - make code, test, and documentation changes.
- `Verification` - collect evidence against the intended contract.
- `Promotion` - deploy or mutate a higher lane with explicit authority.
- `Monitoring` - observe behavior after promotion or during runtime watch.
- `Incident` - respond to active breakage, degradation, or rollback risk.

## Abstraction Layers

- `L0 Mission` - business goal, human owned.
- `L1 Architecture` - invariants, boundaries, and tradeoffs, human-led/shared.
- `L2 Tranche` - bounded scope and proof gate, shared/AI-heavy.
- `L3 Implementation` - code, tests, docs, and local proof, AI-owned within scope.
- `L4 Host Verify` - host-qualified or production proof, shared/human-approved.
- `L5 Incident` - fact gathering and bounded response, human-led/AI-assisted.

## Lanes

Every claim should identify its lane when authority matters:

- `repo` - code and docs only.
- `local implementation` - local runtime and local test proof.
- `staging` - non-production, production-like verification.
- `host-qualified verification` - readonly checks on the real host or equivalent runtime.
- `promotion` - deploys, migrations, restarts, rollback, or other live mutations.
- `architecture decision` - invariants, contracts, and proof rules.

Projects may rename lanes, but they must preserve the distinction between local proof, staging proof, host-qualified truth, and promotion authority.

## Modes

Modes define allowed behavior:

- `Issue capture mode` - write or update formal issue records, classify lightly, then stop.
- `Validation mode` - observe behavior and collect proof; default output is evidence and classification.
- `Patching mode` - bounded implementation has been authorized.
- `Promotion mode` - live or higher-lane mutation has been explicitly approved.
- `Process evolution mode` - lifecycle rules or agent governance are being changed.

Do not cross from one mode to another implicitly.

## Standard Task Frame

Use this frame for substantive work:

```md
- Goal:
- Product lifecycle:
- Feature delivery lifecycle:
- Layer:
- Lane:
- Mode:
- Attention focus:
- Constraints:
- Done:
- Proof class:
- Change state:
- Next action:
- Branch hygiene:
```

## Tranche Sizing

Velocity does not prescribe sprint length or estimation units; project overlays own cadence and sizing. Velocity requires only that a tranche stay small enough to keep authority and proof clear.

Split a tranche when:

- it changes both architecture and implementation
- it needs more than one proof lane to make its core claim
- acceptance criteria are still being negotiated
- it mixes unrelated issue records
- it requires both local patching and live promotion
- it would leave branch disposition ambiguous

Keep a tranche together when:

- the proof mapping is coherent
- the same authority owner can accept the scope
- the same branch can carry the work cleanly
- the implementation and verification support one claim

