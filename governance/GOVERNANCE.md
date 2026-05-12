# Governance

Velocity lifecycle policy is governed separately from product delivery.

## Maintainer Authority

Only the Velocity Maintainer role may approve changes to reusable lifecycle policy.

Project roles may propose changes, including Coordinator, Fixer, Tester, Architect, and Process Reviewer. Proposal authority is not merge authority.

## Protected Paths

Core lifecycle paths are protected artifacts:

- `docs/LIFECYCLE-MODEL.md`
- `docs/ROLE-AUTHORITY.md`
- `docs/ARTIFACT-AUTHORITY-BOUNDARIES.md`
- `docs/CONTROL-PLANES.md`
- `docs/PROOF-MODEL.md`
- `docs/BRANCH-HYGIENE.md`
- `docs/PROJECT-ADOPTION-GUIDE.md`
- `governance/GOVERNANCE.md`
- `templates/`

Ordinary delivery work in a consuming project must not directly edit these paths.

## Process Change Flow

1. Capture the proposed change with evidence.
2. Classify disposition:
   - automation memory only
   - Velocity repo proposal
   - project overlay proposal
   - coordinator-owned project change
   - branch/commit/push requested
3. If it affects reusable lifecycle policy, create a Velocity branch.
4. State the authority owner and affected protected artifacts.
5. Review for project-specific leakage.
6. Merge only after explicit maintainer approval.

## Project-Specific Leakage Check

Before merging a lifecycle change, ask:

- Does this name a specific product, host, database, command, or environment?
- Is the rule generally reusable, or should it be an overlay example?
- Does it change delivery authority or automation authority?
- Does it let the role being evaluated rewrite its own evaluation criteria?
- Does it preserve shared context with separated write authority?

