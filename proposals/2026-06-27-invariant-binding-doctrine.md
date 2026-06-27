# Process Change Proposal — Invariant-Binding Doctrine

> PROPOSAL — pending owner approval. This proposes amendments to the Velocity proof model and two new reusable templates. It does not assert acceptance; the Velocity Maintainer approves.

- Proposal: Fold the invariant-binding doctrine into the proof model — the enforcement ladder (PREVENT > DETECT > RUNTIME_GUARD > HOPE), blast×silence×reversibility triage with a lethal quadrant that must reach PREVENT, the seam-review gate, bind-to-touched (not bind-to-declared), no-residual-for-load-bearing, loudness-as-binding, and a standing System Invariant Register — and add two templates (the register format and the inline ADR `Enforcement:` field convention).
- Source: Nexusplus integrity pilot, 2026-06-26/27. An invariant-proof-binding audit found 11 load-bearing invariants stated but unbound; they were bound through this discipline across PRs #168–#182.
- Triggering evidence: The audit traced the unbound invariants to a *methodology* gap, not a missing rule. Velocity's proof model bound proof to the tranche's *declared* invariant and offered a `residual / blocked` disposition, so load-bearing invariants a change *touched* fell through unbound. There was no enforcement ladder to climb, no triage to decide where to spend prevention, no explicit seam-review gate for cross-subsystem invariants, and no standing register to make enforcement decay visible.
- Affected control plane: Shared Control Plane (proof rules, artifact authority); Delivery Control Plane (proof mapping, closeout); Automation Control Plane (templates).
- Affected protected artifacts: `docs/PROOF-MODEL.md`; `templates/` (two new templates).
- Proposed disposition: Velocity repo proposal for reusable lifecycle policy, with consuming-project overlay artifacts (the populated register and per-ADR annotations) kept in the project repo.
- Authority owner: Velocity Maintainer, with Architect review for proof-contract and authority-boundary wording.
- Project-specific or reusable: Reusable core policy. Nexusplus is the triggering and validating example; nothing in the doctrine names a Nexusplus host, command, table, or environment.
- Compatibility risk: The proof model previously permitted a bare `residual / blocked` proof-mapping disposition. This proposal intentionally invalidates that disposition *for load-bearing invariants* — they must be bound or explicitly deferred to a named owner. Existing closeouts that leaned on `residual` for a load-bearing invariant are retroactively non-conformant and should be re-triaged. Non-load-bearing invariants are unaffected.
- Rollout plan: Amend `docs/PROOF-MODEL.md` (Core Rule note, Proof Mapping fix, new Invariant Binding section). Add `templates/system-invariant-register.md` and `templates/adr-enforcement-field.md`. Link both from the docs index when the maintainer accepts. Consuming projects seed their own populated register and annotate their ADRs as overlay work.

## Evidence

The discipline was validated end to end on Nexusplus before being proposed as canon (eat-our-own-dogfood: pilot first, then canonize the proven scaffolding).

- An invariant-proof-binding audit found **11 load-bearing invariants stated but UNBOUND** (10 of 11 were *seam* invariants — spanning two subsystems, owned by neither side's tests). Several were already silently corrupting production: authored edits were being reverted on reprojection, and ADR-0031's headline "father/son false-merge is closed" promise was not actually enforced in the matcher.
- The invariants were bound by climbing the enforcement ladder, triaging the lethal quadrant to `PREVENT`:
  - **U1/U2** (authored scalar + attribute-retirement edits survive reprojection) — `RUNTIME_GUARD` loud guard first (#168), then `PREVENT` via sparse-delta capture + re-based `DETECT` guard (#170; ADR-0034). Employment-field survival explicitly **deferred to a named owner**, not silently dropped.
  - **U6/U7** (kin-edge and distinct-birthday false-merge hard-blocks) — `DETECT` + fail-closed block in the matcher (#169), plus an inbound auto-merge kin-ambiguity gate (#171).
  - **U3** (source/evidence immutable) — `PREVENT` via a `BEFORE UPDATE` trigger (#178).
  - **U8** (RLS fail-closed `WITH CHECK` on fact tables) + a `PREVENT` drift guard (#172–#175).
  - **U4** (company-merge context convergence) (#176/#177); **U10** (single active edge) `PREVENT` partial-unique index (#179); **U5** (outbound never force-collapses two masters) `DETECT` (#180).
- **Adversarial verification caught a real ship-blocking defect on most PRs**, including two silent-data-loss bugs *inside the very fix meant to stop silent data loss* (a whole-state authored snapshot reverted unedited fields; a delta keyer mis-saw a provider re-normalization as a deletion and wrongly retired a legitimate attribute — both in #170), and a guard that revealed contact split had been silently corrupting authored contacts. This is the evidence that *loudness is a binding* and that bind-to-touched is load-bearing: the catches were on invariants the change *touched* but had not *declared*.

## Proposed Text

The full proposed text is the diff to `docs/PROOF-MODEL.md` (Core Rule note + Proof Mapping rewrite + new `## Invariant Binding` section) and the two new templates `templates/system-invariant-register.md` and `templates/adr-enforcement-field.md` carried in this branch. Summary of the load-bearing additions:

```md
- Core Rule: "An invariant is real only if a mechanism enforces it ... Proof must map
  to every invariant a change touches, not only the invariant the tranche declared."
- Proof Mapping: load-bearing invariants may not close as `residual` / `out of scope`;
  the mapping line carries an `Enforcement:` rung + file:line.
- Invariant Binding section:
  - Enforcement ladder PREVENT > DETECT > RUNTIME_GUARD > HOPE.
  - Loudness is a binding; Detect decays, Prevent is permanent.
  - Triage = blast radius × silence × reversibility; lethal quadrant MUST reach PREVENT.
  - Seam invariants are the highest-risk class → explicit seam-review gate at design time.
  - Bind-to-touched, not bind-to-declared.
  - No residual disposition for a load-bearing invariant (bind or explicitly defer to a named owner).
  - Standing System Invariant Register (persistent enforcement-status tracking; decay-visible).
  - Guarded-but-untested is not fully bound.
```

## Compatibility / Reconciliation Notes For The Maintainer

- This **amends** the existing proof model rather than adding a parallel doc, consistent with the manifesto anti-direction against growing `docs/` mass. The doctrine lives inside the proof model (its natural home) plus two templates.
- The existing `## Proof Mapping` section already had the `residual / blocked` disposition. That line is the precise failure mechanism the pilot found; the amendment narrows it (load-bearing invariants may not use it) rather than removing the disposition wholesale (non-load-bearing invariants may still defer).
- The existing `Closeout Requirement` in `ARTIFACT-AUTHORITY-BOUNDARIES.md` and the closeout fields in `TRANCHE-MODEL` / `tranche-template` already require mapping proof back to the original invariant; this doctrine extends that from *the declared invariant* to *all touched load-bearing invariants*, and adds the enforcement rung. No contradiction; a strict extension.

## Decision

- Accepted:
- Rejected:
- Deferred:
- Owner: Velocity Maintainer
- Date:
