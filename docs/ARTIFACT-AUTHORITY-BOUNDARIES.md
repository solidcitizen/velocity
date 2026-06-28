# Artifact Authority Boundaries

Velocity separates shared SDLC context from write authority over SDLC artifacts.

## Core Rule

Shared context, separated write authority.

Agents may read broadly. Agents may not freely rewrite requirements, acceptance criteria, proof mappings, branch disposition, or lifecycle policy because an implementation or validation pass exposed friction.

## Why This Exists

A recurring AI delivery failure is implementation-shaped validation: the agent tests what it built rather than what was specified.

This is usually an authority problem, not a test-count problem:

- the implementation role controls the proof wording
- acceptance criteria drift toward the implementation
- mechanism proof replaces scenario proof
- closeout claims success against a narrowed target that was never explicitly accepted
- lifecycle rules are edited by the same role whose work they evaluate

Protected artifacts make this drift visible.

## Protected Artifacts

| Artifact | Primary authority | Allowed contributor behavior | Protected from |
| --- | --- | --- | --- |
| Issue invariant and operator sentence | Coordinator, with operator evidence | Fixer/Tester may propose clarifications with evidence | silent rewrite to match implementation |
| Acceptance criteria | Coordinator; Architect when semantic | Fixer may propose implementation-informed changes; Tester may challenge adequacy | unilateral weakening by implementation role |
| Proof mapping | Coordinator owns; Tester validates | Fixer supplies internal proof candidates | mechanism proof replacing scenario proof |
| Implementation code/tests | Fixer | Tester/Coordinator may identify gaps | unrelated policy edits hidden in code tranche |
| Independent acceptance evidence | Tester | Fixer may provide reproduction notes | retesting only the implementation mechanism |
| Architecture invariants and authority boundaries | Architect | Coordinator routes decisions; Fixer proposes constraints | routine implementation changing contracts |
| Branch disposition | Coordinator | Fixer reports branch state and PR/parked status | stale branches or unmerged work left implicit |
| Lifecycle process recommendations | Process Reviewer | Coordinator may propose adoption | memory-only recommendations treated as policy |
| Velocity lifecycle policy | Velocity Maintainer, with Architect review when design-significant | Project roles may propose changes | delivery roles self-modifying governance |
| Project overlay policy | Project Coordinator, with Velocity Maintainer for lifecycle-impacting changes | Delivery roles may propose changes | project-specific drift masquerading as core lifecycle policy |
| Production / live-lane mutation | Operator, unless explicitly delegated | Delivery roles may prepare and request a promotion candidate; see [Criticality Does Not Grant Mutation Authority](ROLE-AUTHORITY.md#criticality-does-not-grant-mutation-authority) | implicit authorization from urgency or prior-tranche approval |

## Rules

Acceptance criteria and proof mappings are protected artifacts.

Fixer may propose changes to them, but should not unilaterally apply those changes when the change affects:

- the operator sentence
- a violated invariant
- scenario-vs-mechanism proof
- closeout state
- promotion readiness
- architecture or authority boundaries
- lifecycle process contracts

Tester may challenge proof adequacy, but should not silently rewrite the requirement to fit observed behavior.

Coordinator should explicitly record when acceptance criteria or proof mapping changes, including who accepted the change and why.

Architect should approve changes that alter invariants, ownership, authority boundaries, proof contracts, or SDLC process contracts.

Velocity Maintainer should approve changes to reusable lifecycle policy.

## Closeout Requirement

For workflow or operator-trust defects, closeout must state:

- the original operator sentence or invariant
- the scenario proof that directly maps to it
- any mechanism proof that only supports the design
- whether acceptance criteria or proof mapping changed
- who had authority for the change

If the direct scenario proof is missing, the work is not behavior-proven.

