# Policy and Project Mapping

This illustrative mapping helps a consuming project separate reusable policy from local
operating details. It is a reading aid for existing Velocity documents, not a new policy
or a claim about a private project's implementation. Pair it with the
[example overlay](README.md).

## Reusable Policy in Velocity

| Concern | Authoritative Velocity reference |
| --- | --- |
| Lifecycle stages, lanes, modes, and abstraction layers | [Lifecycle Model](../../docs/LIFECYCLE-MODEL.md) |
| Bounded work and its closeout | [Tranche Template](../../templates/tranche-template.md) |
| Proof and invariant enforcement | [Proof Model](../../docs/PROOF-MODEL.md) |
| Roles and review authority | [Role Authority](../../docs/ROLE-AUTHORITY.md) |
| Who may change each artifact | [Artifact Authority Boundaries](../../docs/ARTIFACT-AUTHORITY-BOUNDARIES.md) |
| Branch disposition | [Branch Hygiene](../../docs/BRANCH-HYGIENE.md) |
| Delivery, automation, and shared policy | [Control Planes](../../docs/CONTROL-PLANES.md) |

## Details in the Consuming Project

- Real commands and tool configuration.
- Ports, hosts, databases, providers, and environment identities.
- Production promotion procedures and the operator's approval details.
- Issue IDs, issue records, handoffs, and review packs.
- Product-specific data contracts and integration behavior.
- Architecture, ADRs, and the populated invariant register.
- Roadmap, priorities, and current status.

## Applying the Boundary

For example, Velocity defines the proof obligation for a touched invariant. The project
defines the invariant's actual enforcement mechanism, test, target environment, and evidence.
Velocity defines promotion authority; the project names its approver, accepted approval
wording, and deployment procedure.

If a local experiment suggests a reusable improvement, use the existing
[process-change flow](../../governance/GOVERNANCE.md#process-change-flow). An example overlay
does not authorize changes to Velocity policy.
