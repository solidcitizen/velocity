# Illustrative Project Overlay

This self-contained example shows how an application could consume Velocity. It is not
an extract from a private repository, a runnable application, or evidence of a completed
adoption. Paths, commands, and lane choices below are illustrative.

The application owns its architecture, issue records, commands, environments, and promotion
paths. Velocity owns reusable lifecycle policy. Start with the
[Project Adoption Guide](../../docs/PROJECT-ADOPTION-GUIDE.md) and pin a released Velocity
version before adapting this overlay.

## Local Sources of Truth

An example project keeps:

- `AGENTS.md`: the local agent guide and reference to the pinned Velocity version.
- `docs/issues/`: issue records and triage.
- `docs/agent-packets/`: handoff packets.
- `docs/review-packs/`: review artifacts and proof.
- `docs/ARCHITECTURE.md` and `adrs/`: project architecture and accepted decisions.
- Its own environment definitions, service controls, and promotion procedures.

Velocity supplies the [lifecycle model](../../docs/LIFECYCLE-MODEL.md),
[role authority](../../docs/ROLE-AUTHORITY.md),
[proof model](../../docs/PROOF-MODEL.md),
[branch hygiene](../../docs/BRANCH-HYGIENE.md), and
[reusable templates](../../docs/INDEX.md#templates). Link to those rules; do not maintain
competing copies in the project overlay.

## Example Lane Map

| Lane | Project-specific scope |
| --- | --- |
| Repository | Read and edit code/docs, run local checks, and shape a tranche. |
| Local implementation | Run the local app and its integration or browser tests. |
| Staging | Verify against a named non-production environment and data set. |
| Host-qualified verification | Read-only checks against an explicitly identified host. |
| Promotion | Approved deployment, migration, restart, or recovery actions. |
| Architecture decision | Project invariants, ADRs, authority boundaries, and proof contracts. |

Name the actual target and access needed for each lane in your overlay. A passing check in
one lane does not establish behavior or authorize mutation in another.

## Example Command Map

These are sample interfaces a project might provide, not scripts shipped by Velocity.
Replace them with commands that exist in your repository and document their targets.

| Purpose | Illustrative command |
| --- | --- |
| Start local services | `npm run dev:up` |
| Check local health | `npm run dev:health` |
| Run local static checks | `npm run check` |
| Run local smoke tests | `npm run test:smoke` |
| Run staging smoke tests | `npm run test:smoke:staging` |
| Read production health | `npm run ops:prod:health` |

Mark whether each real command reads or mutates state. Keep credentials outside this
document. The existence of a command or access credential does not grant promotion authority.

## Local Approval and Proof Details

The overlay identifies who may approve each live action, the exact approval wording or
delegation required, the target environment, and the promotion mechanism. Apply the existing
[role authority](../../docs/ROLE-AUTHORITY.md#criticality-does-not-grant-mutation-authority)
and [proof requirements](../../docs/PROOF-MODEL.md) to those local details.

For a reported workflow defect, define the scenario, expected result, and appropriate proof
before claiming it is fixed. For an architecture change, link the project's ADR and its
enforcement evidence. Populated records remain in the consuming project.

## Migration Sequence

1. Inventory the project's lifecycle documents and map them with the
   [policy and project mapping](policy-mapping.md).
2. Pin Velocity and link it from the local agent guide.
3. Define the project's artifact locations, lane map, commands, and approval details.
4. Apply the overlay to one bounded change and review its proof and closeout.
5. Retire duplicate process text only after the replacement references are adopted and usable.
