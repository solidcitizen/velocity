# System Invariant Register

A standing, project-owned register of every load-bearing invariant and its current enforcement status over time. It is the durable counterpart to the per-tranche proof mapping in [Proof Model → Invariant Binding](../docs/PROOF-MODEL.md#invariant-binding).

This template lives in Velocity (reusable format). The *populated* register is a project-overlay artifact, kept in the consuming project's repo.

## How To Use

- Add a row when an invariant is identified as load-bearing (its violation corrupts truth, crosses a trust boundary, or breaks an operator-facing contract).
- Each integrity-touching tranche reads the register before work, and at closeout **flips the status** of any invariant it bound or moved on the enforcement ladder.
- Never delete a row to "resolve" it. A retired invariant is marked retired, with the reason; a deferred one keeps a named owner and a gate.
- `Enforcement` uses the ladder: `PREVENT` > `DETECT` > `RUNTIME_GUARD` > `HOPE` (see Proof Model). Climb as high as cost allows; the lethal quadrant must reach `PREVENT`.
- `Triage class` records `blast radius × silence × reversibility`. Call out the **lethal quadrant** (high-blast × silent × irreversible) explicitly.
- `Binding mechanism (file:line)` is the actual enforcing code/constraint/test location. `HOPE` rows have no binding and are a defect to be scheduled, not a resting state.
- `Seam?` marks invariants that span two subsystems owned by neither side's test suite (highest-risk class; require a seam-review gate).

## Register

| ID | Invariant statement | Enforcement | Binding mechanism (file:line) | Triage class | Seam? | Status | Owner / notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| U-NN | <one-sentence statement of the load-bearing invariant> | PREVENT \| DETECT \| RUNTIME_GUARD \| HOPE | `path/to/file.ext:NN` (constraint / trigger / test / guard) | high\|med\|low blast × silent\|loud × reversible\|irreversible (mark LETHAL if high×silent×irreversible) | yes / no | BOUND \| LOUD-GUARDED \| DETECT-ONLY \| DEFERRED \| UNBOUND \| RETIRED | <named owner for any deferral; PR refs; test-gap notes> |

## Status Vocabulary

- `BOUND` — enforced at the stated rung; for `PREVENT`, ideally with a removal-detecting test (else note the test gap).
- `LOUD-GUARDED` — `RUNTIME_GUARD` in place (fails closed and loud); climbing to `PREVENT` is the next step where warranted.
- `DETECT-ONLY` — a test catches violations but nothing prevents or runtime-guards them; decay risk.
- `DEFERRED` — explicitly deferred to a named owner with a gate/date; a tracked liability, not closed.
- `UNBOUND` — load-bearing and on `HOPE`; a defect.
- `RETIRED` — no longer load-bearing; keep the row with the reason and date.
