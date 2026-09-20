# Governance

Velocity lifecycle policy is governed separately from product delivery.

## Maintainer Authority

Only the Velocity Maintainer role may approve changes to reusable lifecycle policy.

Project roles may propose changes, including Coordinator, Fixer, Tester, Architect, and Process Reviewer. Proposal authority is not merge authority.

## Delegated Mechanics

The maintainer may delegate two mechanics, in writing, to a named session or role: merging a proposal the maintainer has explicitly approved, and release stamping (the acceptance record, the annotated tag, and the release notes). Delegation transfers no approval authority. A delegate never merges without the maintainer's explicit approval of that proposal, and every acceptance record names the approval it acted on. A delegate is not an eighth lifecycle role; the seven roles in [Role Authority](../docs/ROLE-AUTHORITY.md) are unchanged.

## Protected Paths

Core lifecycle paths are protected artifacts, stated as directories so that new files inherit the protection:

- `docs/` (every file, including `docs/INDEX.md`)
- `governance/`
- `templates/`
- `adrs/`
- `AGENTS.md`

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
6. Merge only after explicit maintainer approval, by the maintainer or a delegate acting on that approval.
7. At acceptance, update the proposal's header (Status, Accepted version, Disposition) and record the approval in the changelog and the proposal's Proof and Disposition; stamp the release. A merged proposal never reads "not merged".

## Project-Specific Leakage Check

Before merging a lifecycle change, ask:

- Does this name a specific product, host, database, command, or environment?
- Is the rule generally reusable, or should it be an overlay example?
- Does it change delivery authority or automation authority?
- Does it let the role being evaluated rewrite its own evaluation criteria?
- Does it preserve shared context with separated write authority?

