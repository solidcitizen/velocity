# Process Change Proposal — Protect The Checks From The Change They Judge

- Proposal: make Velocity's rule against rewriting requirements and tests bindable. State that
  weakening a check that carries acceptance or proof-mapping evidence is a change to that protected
  artifact. Add proof-model doctrine for protecting checks and for turning operator corrections
  into bindings, and add an opt-in reference template a project can bind with its own platform.
- Status: Proposed; awaiting maintainer review.
- Date: 2026-11-16
- Mode: Process evolution
- Proposed version: 1.12.0 (minor)
- Source: the maintainer asked how Velocity "bans" rewriting requirements or tests. The answer, from
  the canon at v1.11.0, was that it bans them by authority, declaration, and independent proof, but
  ships no mechanism, so by its own enforcement ladder the protection of the checks is `HOPE`. The
  maintainer then shared a public 2026 conference talk on agent environments
  (youtube.com/watch?v=O_zcc6Xl12g). Its team reports thousands of agent pull requests a month with a
  low revert rate, on the principle that every correction becomes a deterministic check rather than
  another instruction line. The talk does not say who may change those checks. The maintainer
  approved drafting this proposal on 2026-11-16.
- Triggering evidence:
  1. [Artifact Authority Boundaries](../docs/ARTIFACT-AUTHORITY-BOUNDARIES.md) protects acceptance
     criteria and proof mappings, and gives the Fixer ownership of "code and test changes", but
     never says whether deleting or loosening a test that carries acceptance evidence is a change to
     the protected artifact. A reader can take it either way.
  2. The [Proof Model](../docs/PROOF-MODEL.md) says "A `DETECT` test can be deleted, skipped, or
     quietly made to pass" and asks for tests that guard the removal of structural bindings, but
     applies neither point to the checks themselves.
  3. The [Project Adoption Guide](../docs/PROJECT-ADOPTION-GUIDE.md) says "Protect the checks from
     the candidate" and "Put mandatory enforcement outside the agent's write authority" for agent
     qualification and handoffs, without a pattern a project can bind.
  4. The maintainer's own agent sessions keep a growing list of dated prose corrections. Several of
     them could be checks: a scripted session-start sweep, a pull request body check, and a pre-release
     tag check. Two field scans (2026-10-04, from shared posts; 2026-11-16, the talk above) found the
     same advice independently: turn routine checks and corrections into code, and keep agents unable
     to edit the controls that judge them.
- Affected control plane: Delivery (proof and acceptance) and Shared (authority boundaries).
- Affected protected artifacts: `docs/PROOF-MODEL.md`, `docs/ARTIFACT-AUTHORITY-BOUNDARIES.md`,
  `docs/ROLE-AUTHORITY.md`, `templates/AGENTS.fragment.md`; new `templates/protected-checks.md`,
  linked from `docs/INDEX.md` and `docs/PROJECT-ADOPTION-GUIDE.md`; `CHANGELOG.md`.
- Proposed disposition: Velocity repo proposal; one pull request.
- Authority owner: Mike, Velocity Maintainer. Merge and release follow his approval.
- Project-specific or reusable: reusable. Names no project, tool, platform, or account.
- Compatibility risk: low, and argued below.
- Rollout plan: release as 1.12.0; consuming projects adopt the template when they choose. Nothing
  migrates automatically.

## Change

1. **Proof Model, two sections** after *Guarded-But-Untested Is Not Fully Bound*:
   - *Protect The Checks From The Change They Judge.* Adding a check is ordinary work; weakening one
     is a protected change. Weakening is defined (delete, skip, disable, loosen, suppress, exempt,
     narrow the gate). A written justification is not an exemption. The protection belongs outside
     the builder's write authority, and the detector guards itself. Where one session holds write
     access to code, tests, and gate together, the protection is recorded as `HOPE`.
   - *Turn Corrections Into Bindings.* An operator correction is an invariant, bound at the highest
     rung it can reach: design it out, then check it automatically, and write it down only when
     neither is possible yet, with the reason. Retire the prose when a check replaces it.
2. **Artifact Authority Boundaries.** A table row for checks that carry acceptance or proof-mapping
   evidence. One rule paragraph: such a check is part of the protected artifact, so the Fixer may
   propose weakening it but should not apply that change alone. The closeout line on changed criteria
   or proof mapping now names a weakened, skipped, or removed check as such a change.
3. **Role Authority.** A Fixer *must not* line for the same case, and a Process Reviewer duty to ask
   of each repeated correction whether it can be designed out or checked first.
4. **Agent entry fragment.** A short *Checks And Corrections* section, so agents read the rule where
   they start.
5. **New template, Protected Checks.** List the protected checks with owners; require the owner's
   review on the hosting platform; fail weakening automatically in the gate; guard the detector;
   record the enforcement level in the register; keep a correction record whose prose column should
   shrink over time. Includes the solo-operator case.

## Compatibility

MINOR by the changelog's rule: additive doctrine, a new template, and clarifications that do not make
previously conformant delivery non-conformant.

- The boundaries paragraph and the Fixer line name a case the existing rules already cover. The
  Fixer should not unilaterally apply changes to acceptance criteria or proof mappings that affect
  scenario-versus-mechanism proof, and the closeout must already declare changes to either. Removing
  or loosening the check that carries that proof is such a change. A project in which the Fixer
  silently deleted acceptance tests was not conformant before this proposal.
- The closeout requirement gains no new field. The existing line is clarified.
- The proof-model sections use *should*, and the template is opt-in. No project must bind its checks
  mechanically to stay conformant; it must record honestly what level its protection is at.

If the maintainer reads the boundaries paragraph as a new obligation rather than a clarification,
the alternative is to keep it out of this release and ship the doctrine and template alone.

## Not In Scope

- No tool, platform, or vendor is named or required. The template describes path ownership,
  required review, and a weakening detector in neutral terms.
- No change to who owns implementation tests. The Fixer still writes and changes mechanism tests
  freely; the rule covers only weakening a check that carries acceptance or proof-mapping evidence,
  plus whatever the project lists.
- No change to delegation grades or automatic acceptance.

## Proof and Disposition

Prepared on branch `proposal/protect-the-checks` from `main` at v1.11.0. `git diff --check` clean;
internal links and anchors checked; renderer tests pass unchanged (no code change).

## Decision

- Accepted:
- Rejected:
- Deferred:
- Owner: Mike, Velocity Maintainer
- Date:
