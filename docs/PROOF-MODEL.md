# Proof Model

Velocity requires proof to be explicit, comparable, and mapped to the claim being made.

## Core Rule

No change may be marked complete or green without explicitly stating its proof class coverage.

Lower-order proof may not silently substitute for higher-order proof.

For operator-reported workflow defects, implementation-mechanism proof may not substitute for acceptance proof. The first regression proof should replay the operator's reported workflow sentence from observable start state to expected observable outcome.

An invariant is real only if a mechanism enforces it. A prose statement of an invariant is not a force; writing a rule down does not make the system obey it. Proof must therefore map to every invariant a change *touches*, not only the invariant the tranche declared. See [Invariant Binding](#invariant-binding).

## Proof Classes

### Class A - Scenario / Browser / End-User Proof

Proves:

- UI behavior and rendering
- user interaction flows
- enabled and disabled states
- end-to-end wiring across visible surfaces
- operator usability and affordances

For workflow claims, Class A must be scenario-shaped.

### Class B - HTTP / API / Runtime Contract Proof

Proves:

- server behavior and sequencing
- status transitions and API contracts
- data mutations observable via API
- coordination behavior visible at runtime

### Class C - Logs / Database / Trace Proof

Proves:

- internal state transitions
- execution traces
- data-level correctness
- migration or repair effects

### Class D - Code Reasoning / Static Proof

Proves intended logic only.

Class D is not sufficient on its own.

## Minimum Proof by Claim

| Claim type | Minimum proof |
| --- | --- |
| UI, product, or operator behavior | Class A |
| Workflow requirement | Scenario-shaped Class A |
| Server/control-plane/sequencing behavior | Class B |
| Data repair or migration result | Class C plus lane-appropriate runtime proof |
| End-to-end system behavior | Class A plus Class B |
| Architecture intent only | Class D may support design, but not behavioral completion |

## V-Model Mapping

Use the V-model to map requirement level to proof level:

| Requirement level | Proof level |
| --- | --- |
| Operator sentence / user workflow | scenario acceptance proof |
| Cross-component system contract | system/API/runtime proof |
| Component behavior | integration proof |
| Mechanism or helper behavior | unit/static/design proof |

Mechanism proof cannot close a workflow requirement.

Example:

- Requirement: `switch to main -> logout -> login -> main is selected`
- Scenario proof: browser switches list through the UI, logs out, logs in, and asserts `main` is selected.
- Mechanism proof only: preseed recent-list storage and assert boot selection.

## Proof Mapping

Proof maps to invariants *touched*, not only the invariant *declared*. Before closeout, enumerate every load-bearing invariant the change touches — including invariants owned by an adjacent subsystem (see [Seam Invariants](#seam-invariants)) — and map each one.

Every closeout should include:

```md
Proof mapping:
- <invariant or operator sentence> -> <direct test/check/evidence> -> <Enforcement: PREVENT|DETECT|RUNTIME_GUARD + file:line>
- <touched invariant not yet bound> -> deferred to <owner> by <date or gate>
```

A load-bearing invariant may not be closed as `residual` or `out of scope`. It must be bound (mapped to an enforcing mechanism) or **explicitly and visibly deferred to a named owner**, never silently dropped. The original Velocity proof mapping allowed a bare `residual / blocked` disposition; that disposition is the failure path that lets a load-bearing invariant fall through unbound, and it is no longer permitted for load-bearing invariants. See [No Residual Disposition For A Load-Bearing Invariant](#no-residual-disposition-for-a-load-bearing-invariant).

Do not describe SHA, health, or DB identity proof as behavior validation. Those are deployment or environment proof, not operator-behavior proof.

## Invariant Binding

This section governs how invariants are enforced and proven. It exists because a recurring AI-delivery failure is the *malformed-imperative fallacy*: stating an invariant in prose and treating the statement itself as enforcement. A specification is a claim about intended behavior. It becomes a real constraint only when a mechanism makes a violation either impossible, caught, or loud.

### The Enforcement Ladder

Every load-bearing invariant should be bound as high on this ladder as cost allows. Higher rungs are strictly stronger.

| Rung | Name | Meaning | Examples |
| --- | --- | --- | --- |
| 1 (highest) | `PREVENT` | A violation is unrepresentable by construction. The illegal state cannot be expressed. | type that excludes the bad case, DB `NOT NULL` / `CHECK` / `UNIQUE` / partial-unique constraint, RLS `WITH CHECK`, `BEFORE UPDATE` trigger that rejects the change, total function with no error branch |
| 2 | `DETECT` | A violation is representable but a test fails when it occurs. | unit/integration/scenario test asserting the invariant, regression test replaying the failure |
| 3 | `RUNTIME_GUARD` | A violation is representable and may reach production, but the code fails closed and loud at runtime instead of proceeding silently. | fail-closed assertion that throws/aborts on the illegal transition, guard that refuses to write rather than write wrong |
| 4 (lowest) | `HOPE` | Only prose states the invariant. Nothing enforces it. | a sentence in an ADR with no test, constraint, or guard |

Two rules govern movement on the ladder:

- **Loudness is itself a binding.** A `RUNTIME_GUARD` that fails closed and loud is a real enforcement, strictly better than silence. Converting a silent corruption into a loud abort is a legitimate, shippable first binding even before `PREVENT` is reached.
- **Detect decays; Prevent is permanent.** A `DETECT` test can be deleted, skipped, or quietly made to pass; a structural `PREVENT` constraint holds until someone deliberately removes it (and removing it can itself be tested — see the guarded-but-untested note below). For enduring invariants, prefer structural prevention. *Permanence is conditional:* a structural binding is only permanent if it survives the project's build and deploy toolchain — see [Prevention Is Permanent Only If It Survives The Toolchain](#prevention-is-permanent-only-if-it-survives-the-toolchain).

`HOPE` is acceptable only for an invariant that is *both cheap to lose and loud when lost by other means* — i.e. an invariant whose violation announces itself anyway. Any load-bearing invariant on `HOPE` is an unbound invariant and a defect.

### Triage: Which Invariants Must Earn PREVENT

Climbing to `PREVENT` has a cost. Triage decides where to spend it, scoring each invariant on three axes:

- **Blast radius** — how much is corrupted when it breaks (one field vs. an aggregate vs. cross-tenant).
- **Silence** — does a violation announce itself, or corrupt quietly? Silent failures are far more dangerous than loud ones.
- **Reversibility** — can the damage be undone after the fact, or is it irreversible (e.g. already written to a user's device, already overwrote the only copy)?

The **lethal quadrant** is *high-blast × silent × irreversible*. Invariants in the lethal quadrant **MUST** be bound at `PREVENT`. Silent-but-reversible or loud-but-irreversible invariants should be made `RUNTIME_GUARD`-loud at minimum and climb to `PREVENT` as cost allows. An invariant that is *cheap-and-loud* (low blast, self-announcing, reversible) may rest on `HOPE`.

Record the triage class alongside each invariant so the spend is visible and reviewable.

**Sequence the lethal quadrant first.** When a lethal-quadrant invariant is unbound — or, worse, already being violated silently in production — binding it takes priority over new feature work that rests on it. Building features on top of an unbound load-bearing invariant compounds the blast radius and entangles the eventual fix. Stop the silent corruption (a loud `RUNTIME_GUARD` is a cheap, shippable first step) before extending the surface that depends on the invariant holding.

### Seam Invariants

A **seam invariant** spans two subsystems and is owned by neither side's test suite. It is the highest-risk class of invariant: each side assumes the other enforces it, so it falls into the gap between them and ends up on `HOPE` while everyone believes it is bound.

- Any change that touches a seam must enumerate the seam invariants explicitly and bind them on one declared side.
- A change at a seam requires an explicit **seam-review gate** at design time (Architect posture), before implementation, to assign ownership and the binding side. This is a tranche-shaping obligation, not a closeout afterthought.
- Seam invariants are exactly the invariants most likely to be missed by *bind-to-declared* proof, which is why proof binds to *touched*, not *declared*.

### Bind-To-Touched, Not Bind-To-Declared

Proof must map to every invariant a change **touches**, not only the invariant the tranche **declared**. The failure this prevents: a tranche declares one invariant, proves it, and closes green while silently weakening or relying on a second, load-bearing invariant it also touched but never named. The classic enabler was a proof model that bound proof to the declared invariant and offered a `residual / out-of-scope` escape hatch for the rest — so load-bearing invariants fell through that hatch unbound and uncounted.

At tranche shaping, list the invariants the change *touches*. At closeout, every touched load-bearing invariant must appear in the proof mapping with its Enforcement rung and binding mechanism.

### No Residual Disposition For A Load-Bearing Invariant

A load-bearing invariant — one whose violation corrupts truth, crosses a trust boundary, or breaks an operator-facing contract — may not be closed as `residual`, `out of scope`, or `blocked` without a successor.

It must be one of:

- **Bound** — mapped to an enforcing mechanism at a stated rung, with `file:line`.
- **Explicitly deferred** — recorded as an open obligation with a **named owner** and a gate or date, visible in the standing register (below). A deferral is a tracked liability, not a closed item.

Silent omission of a load-bearing invariant is a proof-model violation, not a scoping choice.

### Standing System Invariant Register

Per-tranche proof mapping is necessary but not sufficient: it proves the invariants *one change* touched, and says nothing about the invariants no current change happens to touch. Enforcement also **decays** — a `DETECT` test gets skipped, a guard gets refactored away — and per-tranche proof cannot see that decay.

A project should therefore keep a **standing System Invariant Register**: a persistent, project-owned list of every load-bearing invariant and its *current* Enforcement status over time. It is the durable counterpart to the per-tranche proof mapping. Each integrity-touching tranche reads the register, and at closeout *flips the entry* for any invariant it bound or moved on the ladder. The register makes decay and regression visible because the status is tracked continuously, not reconstructed per change.

The register format and the inline ADR `Enforcement:` field are reusable templates ([System Invariant Register](../templates/system-invariant-register.md), [process change proposal note on the `Enforcement:` field convention](../templates/adr-enforcement-field.md)). The *populated* register and the per-ADR annotations are project-overlay artifacts, not Velocity core.

### Guarded-But-Untested Is Not Fully Bound

A `PREVENT` mechanism that exists but has no test guarding its *removal* is one careless migration away from silent un-binding. A `DROP TRIGGER`, a dropped constraint, or a deleted RLS policy can quietly demote an invariant from `PREVENT` to `HOPE`. Where the cost is reasonable, add a `DETECT` test that asserts the structural mechanism is present, so removing the prevention fails a test. Track such mechanisms in the register as `PREVENT` with a noted test gap until that test exists.

### A Gate Must Run The Guard It Fronts

A *gate* is any pre-flight check that decides whether an operation may proceed: a preview, a "can I do this?" validation, a precondition checked before a commit. A *guard* is the enforcement the operation will actually hit at runtime. When a gate fronts a guard, the gate must answer the **same** question the guard will — ideally by **running the guard's own predicate** (one shared check both call) or by **dry-running the real operation without persisting**. It must never approximate the guard with a *proxy signal*.

Every proxy has a gap, and the gap is a **false pass**: the gate says "go", the operation commits, and the guard then rejects it — after a durable state change, which is the worst place to discover the violation. A gate keyed on a stand-in ("a decision record exists", "this event is newer than the merge") misses every case the stand-in does not cover, silently, until one of those cases reaches the guard post-commit.

- Build the gate from the **same predicate** the guard enforces, or dry-run the actual operation against every aggregate it will touch. One check, not two kept in sync — two will drift.
- Treat "the precheck and the enforcement are derived separately" as a defect waiting to happen. Factor the decision into one function both import.
- **Defense in depth.** If a *deterministic* failure can still occur after a durable commit — e.g. a resume loop re-running a step that will always reject — it must become **visible**: fail or flag after repeated identical failure. A deterministic post-commit error that retries forever, while the gate keeps passing, is an invisible outage.

### Know What Your Guard Can See

Running the real check is necessary but not sufficient: the guard itself may have a structural **blind spot**. A guard that inspects only one representation of the truth is blind to truth stored in another representation — and a guard blind to a violation does not throw, it **passes**, so the violation is applied *silently*, which is worse than a loud rejection.

Before trusting a guard, **enumerate where the invariant's truth actually lives**. If authored truth exists in two places — say, a projected current-state and a separate event ledger — a guard that reads only the projection cannot see a violation expressed only in the ledger. Such an invariant needs **complementary checks, one per data-location**, not a single check assumed to be total. When you adopt "run the real check," do not delete a complementary check that covered a location the real check cannot see; map the locations first.

Name a binding for the *class* it enforces, not the one trigger you first noticed — a blocker named after a single cause hides the cases it does not catch.

### Prevention Is Permanent Only If It Survives The Toolchain

"Detect decays; Prevent is permanent" holds only if the structural binding actually survives the project's build and deploy machinery. A schema-reconciliation or migration tool that rewrites storage to match a declared model will **silently drop** any constraint, index, trigger, or policy it does not see in that model. A `PREVENT` mechanism the toolchain can erase on the next deploy is not permanent — it is `HOPE` wearing a `PREVENT` badge, and its removal is *silent*, exactly the failure `PREVENT` was meant to exclude.

- Declare structural bindings **where the reconciler preserves them**, so a deploy cannot quietly remove them.
- Add a build-time **drift check** that fails if a binding the project depends on is missing from the durable declaration. This is the `DETECT` that guards the `PREVENT` against the toolchain itself.
- In the register, a structural binding the toolchain can silently drop is recorded as not-yet-durable (effectively `HOPE`) until its durability is itself guarded.

### Bind The Whole Surface, Not A Sample

When an invariant is defined over a **set of sites** — every write policy on a class of tables, every structural guard, every entry point that can reach a state transition — bind it by **enumerating the full surface**, not by fixing the sites you happened to notice. An estimate by sampling undercounts: a surface believed to be five may turn out to be thirty. For this class of invariant the right closer is a **completeness sweep** plus a **drift-guard that re-derives the full set** from its definition and fails when a qualifying site is unbound. A sampled binding leaves silent gaps that read, from the closeout, as full coverage.

### Verify The Binding Adversarially

A binding is a claim, and the author of a fix is the worst judge of whether it holds. The strongest signal that a binding is real is an **independent, adversarial pass** that tries to *defeat* it — across several lenses (does it reproduce the original failure? does it admit a neighboring bad state? does it over-block a legitimate one?) — producing a ship / no-ship verdict before the change merges. In the pilot this caught a real, ship-blocking defect on most integrity changes, including silent-data-loss bugs *inside the fix meant to stop silent data loss*.

Two disciplines make adversarial verification trustworthy:

- **Pin to the verified artifact.** The verifier must fetch, confirm, and report the exact commit it reviewed. A verdict rendered against a stale revision is worse than none — it can produce a confident false rejection of code that is actually correct.
- **Verify per slice, not per batch.** Verify each binding as it lands, so a defect is caught against the change that introduced it rather than diffused across a pile of merged work.
