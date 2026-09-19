# Process Change Proposal — Invariant-Binding Doctrine

> ACCEPTED 2026-06-27 by the Velocity Maintainer. The amendments are folded into `docs/PROOF-MODEL.md` (Core Rule note, Proof Mapping narrowing, new `## Invariant Binding` section) and the two templates live in `templates/`, both linked from `docs/INDEX.md`. This record is retained for provenance; the canon is the amended proof model, not this file.

- Proposal: Fold the invariant-binding doctrine into the proof model — the enforcement ladder (PREVENT > DETECT > RUNTIME_GUARD > HOPE), blast×silence×reversibility triage with a lethal quadrant that must reach PREVENT, the seam-review gate, bind-to-touched (not bind-to-declared), no-residual-for-load-bearing, loudness-as-binding, and a standing System Invariant Register — and add two templates (the register format and the inline ADR `Enforcement:` field convention).
- Updated 2026-06-27 (revisited after the pilot continued): added five binding-quality lessons earned *after* the initial draft, while binding the reversibility surface (undoing record merges): **gate–guard parity** (a preview/precheck must run the guard's own predicate, never a proxy), **know-what-your-guard-can-see** (enumerate where the invariant's truth lives; a guard blind to a data-location passes violations silently), **durable prevention** (a structural binding the deploy toolchain can silently drop is HOPE, not PREVENT), **bind-the-whole-surface-not-a-sample** (completeness sweep + drift-guard for set-defined invariants), and **adversarial per-slice verification with pin-to-head**. Plus a one-line sequencing rule: bind a lethal-quadrant invariant before building features on it.
- Source: A maintainer-reported integrity pilot in a private software application, 2026-06-26/27. An audit identified 11 load-bearing invariants stated without enforcement; the pilot informed this proposal. Its implementation and review records are not publicly available.
- Triggering evidence: The audit traced the unbound invariants to a *methodology* gap, not a missing rule. Velocity's proof model bound proof to the tranche's *declared* invariant and offered a `residual / blocked` disposition, so load-bearing invariants a change *touched* fell through unbound. There was no enforcement ladder to climb, no triage to decide where to spend prevention, no explicit seam-review gate for cross-subsystem invariants, and no standing register to make enforcement decay visible.
- Affected control plane: Shared Control Plane (proof rules, artifact authority); Delivery Control Plane (proof mapping, closeout); Automation Control Plane (templates).
- Affected protected artifacts: `docs/PROOF-MODEL.md`; `templates/` (two new templates).
- Proposed disposition: Velocity repo proposal for reusable lifecycle policy, with consuming-project overlay artifacts (the populated register and per-ADR annotations) kept in the project repo.
- Authority owner: Velocity Maintainer, with Architect review for proof-contract and authority-boundary wording.
- Project-specific or reusable: Reusable core policy, prompted by a private application pilot; the doctrine does not depend on that application's hosts, commands, tables, or environments.
- Compatibility risk: The proof model previously permitted a bare `residual / blocked` proof-mapping disposition. This proposal intentionally invalidates that disposition *for load-bearing invariants* — they must be bound or explicitly deferred to a named owner. Existing closeouts that leaned on `residual` for a load-bearing invariant are retroactively non-conformant and should be re-triaged. Non-load-bearing invariants are unaffected.
- Rollout plan: Amend `docs/PROOF-MODEL.md` (Core Rule note, Proof Mapping fix, new Invariant Binding section). Add `templates/system-invariant-register.md` and `templates/adr-enforcement-field.md`. Link both from the docs index when the maintainer accepts. Consuming projects seed their own populated register and annotate their ADRs as overlay work.

## Evidence

Publication note (2026-09-09): the following summarizes the maintainer's account of a private
pilot. Its source artifacts are not available for public reproduction or independent
verification. Project names, private PR/ADR numbers, and internal invariant IDs have been
removed from this public summary. The original acceptance and proposed policy text are
unchanged; the lessons below explain their origin rather than certify current project health.

- The reported audit found **11 load-bearing invariants without enforcement**, ten spanning
  subsystem boundaries. Failures included user-authored edits being lost when records were
  recomputed and prohibited record merges remaining possible despite an architecture decision.
- Reported remedies combined runtime guards, structural prevention, and detection: preserving
  authored changes as deltas, rejecting invalid merges, preventing edits to source evidence,
  enforcing row-level write constraints, and requiring uniqueness for active relationships.
  A remaining field-survival case was explicitly deferred to a named project owner.
- Adversarial review reportedly caught defects in the fixes themselves, including snapshots
  that reverted untouched fields and change detection that mistook normalization for deletion.
  These incidents motivated checking all invariants a change touches, beyond its declared goal.

### Lessons reported from later pilot work

- **Gate and guard parity.** A preview used proxy signals that missed deterministic failures
  during the real operation. Sharing the actual guard predicate with a non-persisting preview
  exposed those failures before a durable write.
- **Guard visibility.** A current-state check could not see authored decisions stored only in
  an event ledger. A complementary check was needed at that second source of truth.
- **Durable prevention.** A schema reconciliation step reportedly removed **22 structural
  safeguards** that were absent from its declared model. Declaring them durably and checking
  for their survival addressed that failure mode.
- **Complete coverage.** A review initially estimated five relevant tables; a broader sweep
  reportedly found **32 write policies** without the required write check. A guard that
  recomputed the full relevant set replaced reliance on a curated sample.
- **Reviewed revision.** A reviewer reported missing fixes while examining an older commit.
  This motivated fetching, confirming, and reporting the exact revision used for a verdict.

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
  - Sequence the lethal quadrant first: bind a lethal-quadrant invariant before building features on it.
  - A gate must run the guard it fronts (gate–guard parity; no proxy signals; surface deterministic post-commit failures).
  - Know what your guard can see (enumerate the invariant's data-locations; complementary checks; name the class, not one trigger).
  - Prevention is permanent only if it survives the toolchain (durable declaration + a drift check guarding the Prevent).
  - Bind the whole surface, not a sample (completeness sweep + set-rederiving drift-guard for set-defined invariants).
  - Verify the binding adversarially (independent ship/no-ship pass per slice; pin to and report the reviewed SHA).
```

## Compatibility / Reconciliation Notes For The Maintainer

- This **amends** the existing proof model rather than adding a parallel doc, consistent with the manifesto anti-direction against growing `docs/` mass. The doctrine lives inside the proof model (its natural home) plus two templates.
- The existing `## Proof Mapping` section already had the `residual / blocked` disposition. That line is the precise failure mechanism the pilot found; the amendment narrows it (load-bearing invariants may not use it) rather than removing the disposition wholesale (non-load-bearing invariants may still defer).
- The existing `Closeout Requirement` in `ARTIFACT-AUTHORITY-BOUNDARIES.md` and the closeout fields in `TRANCHE-MODEL` / `tranche-template` already require mapping proof back to the original invariant; this doctrine extends that from *the declared invariant* to *all touched load-bearing invariants*, and adds the enforcement rung. No contradiction; a strict extension.

## Decision

- Accepted: 2026-06-27 — folded into `docs/PROOF-MODEL.md` (Core Rule note + Proof Mapping narrowing + new `## Invariant Binding` section) and shipped as `templates/system-invariant-register.md` and `templates/adr-enforcement-field.md`, both linked from `docs/INDEX.md`. Released in Velocity canon v1.1.0.
- Rejected: —
- Deferred: The remaining field-survival case was recorded as deferred to a named owner in the private project's invariant register. That historical disposition does not establish its current status or transfer the project liability into Velocity policy.
- Owner: Velocity Maintainer
- Date: 2026-06-27
