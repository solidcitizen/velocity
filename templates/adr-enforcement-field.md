# ADR `Enforcement:` Field Convention

An ADR states invariants. Under the invariant-binding doctrine ([Proof Model → Invariant Binding](../docs/PROOF-MODEL.md#invariant-binding)), an invariant is real only if a mechanism enforces it. This convention makes each ADR invariant carry its enforcement rung and binding location inline, so a reader can tell a *bound* invariant from a *hoped-for* one without leaving the ADR.

This template lives in Velocity (reusable convention). The applied annotations are project-overlay artifacts in the consuming project's ADRs.

## The Field

Annotate each load-bearing invariant in an ADR's invariants list with an inline `Enforcement:` field:

```
Enforcement: PREVENT|DETECT|RUNTIME_GUARD + <file:line>
```

- The rung is one of `PREVENT`, `DETECT`, `RUNTIME_GUARD` (or `HOPE` for an invariant deliberately left unenforced — which flags it as an open obligation, not a closed decision).
- `<file:line>` points to the actual enforcing mechanism: a DB constraint/trigger/index, an RLS `WITH CHECK`, a runtime guard, or the test that fails on violation. Multiple bindings may be listed (`PREVENT capture + DETECT guard`).
- An invariant with no enforceable binding yet must say so explicitly: `Enforcement: HOPE — deferred to <owner> by <gate>`. Never leave a load-bearing invariant un-annotated.

## Example

```md
## Invariants

- Source/evidence events are immutable; `raw_payload` is never rewritten after capture.
  Enforcement: PREVENT + server/migrations/sync-events-immutable-evidence.sql:105 (BEFORE UPDATE trigger) + DETECT server/tests/integration/migration-constraints.test.ts

- An authored scalar edit survives any from-sources reprojection.
  Enforcement: PREVENT (sparse capture) server/storage.ts:12504 + DETECT server/tests/integration/reprojection-authored-truth-prevent.test.ts
```

## Adopting

- Add the field when an ADR is written or when an invariant is later bound; do not change the ADR's status or decision to add an `Enforcement:` line — it is an annotation of how the existing decision is enforced.
- Keep the inline annotation consistent with the project's standing [System Invariant Register](./system-invariant-register.md): the register is the cross-ADR roll-up; the inline field is the in-context binding.
- An ADR that already has a prose `## Enforcement` section should keep it; the inline field is a per-invariant summary pointer, not a replacement for that section.
