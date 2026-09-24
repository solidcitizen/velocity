# TODO — `<project>`

Markdown binding for [Lightweight Work Management](work-management.md). Replace these
examples with real work or an empty queue. This file can remain the authoritative tracker;
no JSON conversion, rendered board, or external service is required.

## Binding and context

- Stable project ID / scope covered:
- Accountable coordinator / priority owner:
- Executing role/agent and accountable human owner: `<may inherit the project role map>`
- Decision context: `<project context or governing plan; inherited by items below>`
- History / revisions: `<Git history or equivalent retained versions>`
- Writer coordination: `<one named editor at a time; shared lock/service if used>`
- Update: `<read current revision; edit; review state/authority/proof; save; read back>`
- Change identity: `<unique request/change ID in the commit or retained update log>`
- Display: `<this file; any derived view and its refresh/read-back procedure>`
- Recovery: `<retain conflicting versions and reconcile; never overwrite newer work blindly>`
- State meanings: `backlog`, `committed`, `doing`, `blocked`, `held`, `done`, `dropped`.

Queue order within a state is the declared priority unless a priority field says otherwise.
Stable IDs are never reused. A checkbox, if retained for convenience, cannot replace the state
field or distinguish dropped from done. Preserve unconfirmed imported facts explicitly.

## Work

### `<project>-WI-1` — `<title>`

- State: `backlog`
- Owner: `<responsible work owner; unconfirmed when genuinely unknown>`
- Scope / done when: `<inline bounded action/result, or issue/tranche link>`
- Context: `<inherit project context; optional more specific initiative/decision link>`
- Source / uncertainty: `<origin and unknowns, if any>`

Add only the fields needed for the item's state and claim:

- Commitment: `<date/week for committed work; preserve changes in history>`
- Depends on / waits on: `<specific item, Desk ask, authority gap, event, or party; next owner>`
- Review trigger: `<known date/event for a wait; unknown stays visible>`
- Completion: `<closure date; evidence and required acceptance, or historical reported label>`
- Drop: `<closure date; reason and deciding authority>`
- History: `<dated actor/reason for material state/scope/priority changes; or version-history link>`

Keep closed items here or in a linked retained archive. Reopening preserves the former closure
and proof. Put recurring obligations in a declared control section/register with occurrence
history; a completed occurrence never silently retires the obligation.

## Update discipline

1. Identify the item and current source revision, context, dependencies, and actor's authority.
2. Coordinate ownership before editing. If the source changed, reread and reconcile.
3. Check the proposed change against the state rules and bounded acceptance conditions.
4. Record the change identity, actor/reason, starting/resulting revisions, and governing decision;
   save and read back the result. A Git commit and its parent can identify saved revisions.
5. Refresh declared derived views and record which revision was shown; disclose failed refresh.

For coupled decisions/work, save or verify the authoritative decision first and record any
pending work update durably. After interruption, check the actual source and decision before
resuming. Direct Markdown editing has no supplied atomic-write, lock, or automatic validator
guarantee; qualify additional tooling separately. Git alone does not serialize active editors.
On a retry, use the same request identity and reconcile the saved state/history before writing;
do not create a duplicate task, ruling, or state change because the earlier response was lost.
