# Project Artifact Index

Complete this index before operational use. It is the shared entry point for every authorized
human and AI tool. Store it in the project-owned operational workspace. Link it from the
project overlay and each supported agent entry file; those files do not maintain their own
work lists or decision ledgers.
Resolve template-relative links to the adopting project's records or its pinned Velocity
checkout; a copied template's links do not automatically become valid at its new location.

## Ownership and access

- Stable project identity: `<retain through renames and migrations; match records.json if used>`
- Operational workspace: `<project-owned location; use a private locator where appropriate>`
- Responsible delivery role: `<role>`
- Operator and decision authority: `<owner; delegation record if applicable>`
- Audience: `<local/private team/public; publication destinations and allowed content>`
- Access and write enforcement: `<OS/service identities, protected wrapper or access rules>`
- History/backup: `<what is backed up, where, retention, restore command, last rehearsal>`
- Velocity tool pin: `<released version or explicitly recorded pilot revision>`
- Supported integrations: `<tool, version/model, entry point, access, qualification evidence>`
- Decision context: `<purpose, selection/initiative owners, capacity, escalation and review;
  use decision-records.md or link equivalent records>`
- Work binding and scope: `<Markdown / structured JSON / external tracker; one authority per scope>`

Actor and authority fields in update requests are audit context, not authentication. Give
writers only the authority their role holds. The file helper coordinates cooperating writers;
direct editors bypass it. Use protected host/service controls when stronger enforcement is
required. Back up source records, this index, and their history together; include `records.json`
and `.records/operations/` when using the JSON helper.

## Authoritative records and views

Choose the Work row that matches the declared binding; remove the unused alternatives.
`records.json` is the machine-readable binding only for the supplied JSON helper. If its paths
change, update it and this index in a coordinated maintenance window with no pending operation.

| Record | Authoritative location | Responsible role | Generated view | Update procedure |
| --- | --- | --- | --- | --- |
| Operator asks and decisions | `checkin/desk.json` | `<delivery lead; operator owns decisions>` | `views/desk.html` | Shared guarded update; retain approval evidence |
| Work items (Markdown option) | `TODO.md` | `<coordinator>` | Source Markdown; optional qualified view | Serialized edit, semantic review, version history and read-back |
| Work items (structured JSON option) | `work/board.json` | `<coordinator>` | `views/board.html` | Shared guarded update; preserve IDs and proof |
| Work items (external option) | `<system/project + binding record>` | `<coordinator>` | `<native or qualified derived view>` | `<authorized adapter / native procedure>` |
| Portfolio / initiative decisions, if separate | `<canonical records; may be outside this workspace>` | `<named selection and initiative owners>` | `<optional>` | Preserve rulings and revisions; revalidate affected work |
| Requirements and plans | `<canonical document paths>` | `<owners>` | `<optional>` | `<document review and acceptance procedure>` |

After an external-tracker cutover, the old work file is an archive. Label any continuing board
as a derived view with its collection time and source revision. Do not leave both locations
writable as independent queues.

## Commands and recovery

For Markdown, document the [manual update discipline](work-tracker.md), coordinating editor,
revision/history mechanism, and recovery path. For an external tracker, document its binding.
The following commands apply **only to the structured JSON helper**. Record the
**absolute local path to the pinned** `templates/project-records.py` and these
invocations for this workspace. The commands below use `<tool>` and `<workspace>` placeholders:

```text
python3 <tool> status <workspace>
python3 <tool> apply <workspace> <request.json>
python3 <tool> recover <workspace> <operation-id>
python3 <tool> refresh <workspace>
python3 <tool> export <workspace> <new-snapshot-outside-workspace.json>
```

- Open/refresh: `<how each supported environment opens views/desk.html and views/board.html>`
- Additional publication: `<optional host, access, exact command and read-back procedure>`
- Evidence preflight: `<project-specific checks before requests are applied, if applicable>`
- External handoff binding: `<tracker-binding.md, cutover state and mapping>`
- Incomplete-operation handling: run `status`, preserve the journal and source, then recover
  the named operation with the same pinned tools/configuration. If the source diverged, route
  to the owning role for reconciliation before recovery. Do not delete journals to unblock work.

The file helper refreshes local HTML and records byte/source hashes in `.records/views.json`.
It does not open a panel or publish to a remote service. Verify those steps through the named
integration. A local current view does not establish that a remote panel has refreshed.
