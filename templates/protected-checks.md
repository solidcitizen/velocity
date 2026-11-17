# Protected Checks

> Opt-in template support for [Protect The Checks From The Change They Judge](../docs/PROOF-MODEL.md#protect-the-checks-from-the-change-they-judge)
> and [Turn Corrections Into Bindings](../docs/PROOF-MODEL.md#turn-corrections-into-bindings). It changes no role, no
> approval boundary, and no closeout field. A project fills it in its overlay and binds it with its
> own hosting platform and gate. Velocity names no tool.

Checks are what let a project trust agent work without reading every line of it. The role whose work a
check judges should not be able to weaken that check alone. This template turns that rule into a
mechanism in four steps, and adds a short record for corrections.

## 1. List The Protected Checks

| Check | Where it lives (path or setting) | What it proves (invariant or acceptance criterion) | Owner (not the builder) | Detected by |
| --- | --- | --- | --- | --- |
| `<acceptance or scenario tests>` | `<path>` | `<criterion or operator sentence>` | `<role or person>` | step 3 |
| `<lint and type rules>` | `<config path>` | `<invariants they bind>` | `<role or person>` | step 3 |
| `<gate definition: the workflow that runs the checks>` | `<path or setting>` | the checks run on every change | `<role or person>` | step 3 |
| `<verifier scope and thresholds>` | `<path or setting>` | `<what surface is covered>` | `<role or person>` | step 3 |
| the weakening detector (step 3) | `<path>` | weakening is caught | `<role or person>` | itself, step 4 |
| this list | `<path>` | the protected set is complete | `<role or person>` | step 4 |

Start with the checks that carry acceptance or proof-mapping evidence. Those are already protected
artifacts under [Artifact Authority Boundaries](../docs/ARTIFACT-AUTHORITY-BOUNDARIES.md); the rest are the project's
choice.

## 2. Require The Owner's Review

Configure the hosting platform so a change that touches a protected location cannot merge without
approval from that location's owner, and so the author of a change cannot approve it. Most platforms
provide this through path ownership rules and required reviews on the protected branch.

- The owner is a person or a role other than the builder. An agent session does not approve its own
  change, and a second session acting on the first session's instructions is not an independent owner.
- **Solo operator.** The owner is the operator acting in a separate, recorded moment (a review action
  or a decision record), not the same working session that made the change. See
  [Project Adoption Guide](../docs/PROJECT-ADOPTION-GUIDE.md): never self-approve a protected change in
  the same breath that produced it.
- Path ownership cannot tell adding a check from weakening one, so the owner also sees additions.
  Keep that review light; the detector in step 3 is what tells the two apart.

## 3. Fail Weakening Automatically

Add a step to the gate that compares the change with its target branch and fails, unless the change
carries an approval only the owner can give, when it finds any of these in a protected location:

- a protected test deleted or renamed, or fewer protected tests collected than on the target branch
- a new skip, focus, expected-failure, or disabled marker in a protected test
- a new suppression for a protected rule: an inline disable comment, an ignore-file entry, or an
  exemption list entry
- a protected threshold lowered, or a protected scope narrowed
- a change to a protected configuration file or to the gate definition that the step cannot
  classify as strengthening

A change that only adds checks, raises a threshold, or widens a scope passes. Where the step cannot
tell which way a change goes, it fails closed. The failure message names what was weakened and who
can approve it. The approval record names the approver and the reason.

## 4. Guard The Guard

The weakening detector and this list are protected checks themselves. A change that removes, narrows,
or bypasses either one fails like any other weakening. Add a test that fails if the detector is not
run by the gate, as in [Guarded-But-Untested Is Not Fully Bound](../docs/PROOF-MODEL.md#guarded-but-untested-is-not-fully-bound).

## 5. Record The Enforcement Level

In the [System Invariant Register](system-invariant-register.md), record the protection of the checks
as an invariant of its own:

- before steps 2 and 3 exist: `HOPE` (the role rules and the closeout declaration only)
- with step 2 only: a required review stands between the change and the merge, but no check finds
  the weakening; record `HOPE` and note the review
- with steps 2 to 4: `DETECT`, with the detector's location

At closeout, a weakened, skipped, or removed check that carries acceptance or proof-mapping evidence
is declared as a change to the proof mapping, with who approved it.

## Correction Record

Each correction the operator gives an agent gets one line. The goal is to move lines out of the
prose column over time.

| Date | Correction (operator's words) | Rung reached | Where it lives | If prose: why not yet designed out or checked | Prose retired |
| --- | --- | --- | --- | --- | --- |
| `<YYYY-MM-DD>` | `<sentence>` | design / check / prose | `<path, rule, or instruction file>` | `<reason>` | yes / no / n/a |

A correction that reaches design or check has its prose version removed from instruction files, so
two statements of one rule cannot drift apart. Review the prose rows at each process review; a long
prose column is a finding.
