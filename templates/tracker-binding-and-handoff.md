# Tracker Binding and Handoff — `<project>`

Use with [Portable Project Records](../docs/PORTABLE-PROJECT-RECORDS.md). This record describes
an existing tracker binding or a bounded migration. Filling it out does not approve cutover.

## Authority, scope, and discovery

- Status: `<proposed / rehearsed / verified / cut over / rolled back>`
- Stable project ID and artifact-index location:
- Current authority and proposed destination (including exact organization/project scope):
- Migration owner, decision authority, and authorized execution scope:
- Audience/access before and after; publication/spend approvals if relevant:
- Tool/model/adapter versions, canonical query/update commands, and credential mechanism:
- Source revision/export hash, destination read-back identity, and history/evidence inventory:
- Snapshot, backup/restore procedures, and retention owner:

## Meaning and identity mapping

Document actual native fields and conversion rules. A generic "Open" status is insufficient
if it loses the distinction among backlog, committed, doing, blocked, and held.

| Source meaning | Destination field/state or durable linked record | Reverse/read-back rule |
| --- | --- | --- |
| Project identity and stable WI ID | `<native key + permanent legacy reference>` | `<crosswalk>` |
| Title, owner, bounded scope and provenance | | |
| Inherited decision context, parent initiative/investment references and revisions | `<linked authoritative records; no duplicate approvals>` | |
| Backlog / committed / doing | | |
| Blocked / held, blocker and review/date information | | |
| Done / dropped, completion proof / reason, closed date | | |
| Dependencies and Desk CK references | | |
| Unknown/uncertain data and historical reported completion | | |
| Optional initiative, size, benefit, due date and origin | | |
| Controls: cadence, history, last proof, next due, planned/suspended state | | |
| Control execution and evidence availability | `<execution stays or separately migrates>` | |

Every source item gets a destination identity or immutable archive reference. Active work and
controls are imported. Done/dropped history can be retained in an accessible archive with a
crosswalk. Stable references survive renumbering in the destination. Explicitly list any
unmapped semantics; owner acceptance cannot remove Velocity authority or proof requirements.

A Markdown TODO is a valid source and can remain the tracker until the owner chooses cutover.
Record its actual state/field mapping; the supplied JSON helper is not a Markdown importer.
Preserve the distinction among work state, development stage, investment posture, and decision
status even if the destination offers only one status field. Linked records may supply the
missing context. A tracker migration does not delegate portfolio or stage-gate authority.

## Rehearsal and reconciliation

- Test scope and isolation from live records:
- Import command and retry/idempotency behavior:
- Per-record crosswalk and field comparison (counts alone are insufficient):
- Evidence/attachment paths verified under destination readers' permissions:
- Desk links and dependency behavior verified in both directions:
- Real destination read and authorized update, exact tested record and result:
- Export and restoration rehearsal, including comments/history and control dispositions:
- Failures and unresolved gaps, with owner and next action:

The supplied `handoff-check` compares a normalized destination snapshot to the file export.
Its `snapshot_verified` result is local comparison evidence only. Record how the adapter
obtained that snapshot from the destination; a hand-authored match does not prove an import.

## Cutover and recovery

- Owner's cutover decision and exact approved scope/revision:
- Write freeze or final-delta procedure, last source revision, destination revision/time:
- New authoritative index/binding and every agent integration updated:
- Old queue archived, local writes disabled, old views labeled archived:
- Post-cutover operator check and one authorized update:
- Recovery trigger and owner; preserve/reconcile destination changes before rollback:
- Restoration result and evidence, or named remaining obligation:

For the supplied local helper, after verification and with no pending operation, set
`records.json` to `mode: external-tracker` and provide `tracker_binding`. Run `refresh` to
label the local Work view archived. This configuration is a record of the authorized cutover,
not evidence that it occurred. Desk operations remain available; external work updates use
the destination's qualified adapter. The file helper supplies no external connector.
