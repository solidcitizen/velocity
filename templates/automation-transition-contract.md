# Automation Transition Contract — `<from state>` to `<to state>`

> Optional template for an automated handoff within **existing, explicitly granted authority**.
> Instantiate in the project and repoint canon links. This record does not grant itself authority,
> adopt manifesto delegation grades, or make silence count as acceptance. It operationalizes
> [Lifecycle Model](../docs/LIFECYCLE-MODEL.md),
> [Role Authority](../docs/ROLE-AUTHORITY.md), and
> [Artifact Authority Boundaries](../docs/ARTIFACT-AUTHORITY-BOUNDARIES.md).

## Input and acceptance

- Contract ID / version / owner / approving authority / acceptance record:
- Source and destination lifecycle state / role / lane / mode:
- Trigger: accepted artifact, event, schedule, or measured condition:
- Authoritative artifact location and immutable revision; event identity:
- Required acceptance record, accepting role, and exact accepted revision:
- Evidence required: claim, proof class, lane, freshness, and direct check:
- Protected artifacts touched and their authoritative owners:

Artifact creation, a `done` label, a commit, and a passing check are distinct from authorized
acceptance. Resolve the actual acceptance record before dispatch. A model reviewer can supply
evidence within its role; it cannot confer powers its role does not hold.

## Action boundary

- Allowed next action / tool and resource scope / maximum attempts and budget:
- Explicit authorization or delegation record covering this action and this work item:
- Validity window / revocation source / person who can stop the automation:
- Enforcement mechanism and location; who can change the mechanism:
- Check at dispatch and again before the consequential action:
- Required output artifact / terminal states / next owner:

For a live mutation, attach the existing
[Review Pack promotion-authority fields](review-pack-template.md#promotion-authority),
including the action, target, approval, and exact commit/ref. A rollback is also a live mutation:
its permitted circumstances, target, and mechanism need explicit authority. Readiness is not
authorization. Changes outside the accepted scope return to the relevant owner.

## Failure, replay, and recovery

- Missing, rejected, stale, revoked, or mismatched acceptance: halt the transition and name owner:
- Duplicate event / retry key: identify by contract version, artifact revision, and action:
- Durable record of pending, attempted, completed, or uncertain action:
- Concurrent updates: isolated worktree or serialized ownership of shared writes:
- Interrupted or uncertain side effect: read back actual state before retry; no blind replay:
- Recovery action / its authority / last rehearsal evidence in an appropriate lane:
- Escalation destination / actionable reason / successor obligation:

Fail closed at the affected boundary when proof or authority is missing. A timer expiring or
a human not responding does not create approval. Use a single predicate shared by gate and
action guard where possible; check all mutation routes and keep mandatory enforcement outside
the evaluated agent's write scope. See [binding quality](../docs/PROOF-MODEL.md#a-gate-must-run-the-guard-it-fronts).

## Qualification before enabling

| Probe | Expected disposition | Actual evidence / exact tested revision |
| --- | --- | --- |
| Accepted, current artifact; allowed action | Dispatch exactly the authorized action | `<not run>` |
| Missing approval; forged status; expired or revoked delegation | Stop and route to owner | `<not run>` |
| Changed artifact after acceptance | Require acceptance of the changed scope/revision | `<not run>` |
| Replayed event or concurrent dispatcher | No duplicate consequential action | `<not run>` |
| Interrupted action; outcome unknown | Reconcile state before any retry | `<not run>` |
| Authorized recovery; recovery fails | Verify restored state or escalate visibly | `<not run>` |

- Enablement decision / approving owner / evidence link:
- Monitoring and disablement trigger:

Keep `proposed`, `tabletop reviewed`, `runtime qualified`, and `enabled` distinct. Qualifying
a contract does not prove a later product change works; that change retains its own proof gate.
