# Project Artifact Index

Complete this index before operational use. It is the shared entry point for every authorized
human and AI tool. Store it in the project-owned operational workspace. Link it from the
project overlay and each supported agent entry file; those files do not maintain their own
work lists or decision ledgers.

## Ownership and access

- Stable project identity: `<records.json project_id; retain through renames and migrations>`
- Operational workspace: `<project-owned location; use a private locator where appropriate>`
- Responsible delivery role: `<role>`
- Operator and decision authority: `<owner; delegation record if applicable>`
- Audience: `<local/private team/public; publication destinations and allowed content>`
- Access and write enforcement: `<OS/service identities, protected wrapper or access rules>`
- History/backup: `<what is backed up, where, retention, restore command, last rehearsal>`
- Velocity tool pin: `<released version or explicitly recorded pilot revision>`
- Supported integrations: `<tool, version/model, entry point, access, qualification evidence>`

Actor and authority fields in update requests are audit context, not authentication. Give
writers only the authority their role holds. The file helper coordinates cooperating writers;
direct editors bypass it. Use protected host/service controls when stronger enforcement is
required. Back up source records, `records.json`, this index, and `.records/operations/` together.

## Authoritative records and views

`records.json` is the machine-readable binding for the supplied file helper. If paths change,
update it and this index in a coordinated maintenance window with no pending operation.

| Record | Authoritative location | Responsible role | Generated view | Update procedure |
| --- | --- | --- | --- | --- |
| Operator asks and decisions | `checkin/desk.json` | `<delivery lead; operator owns decisions>` | `views/desk.html` | Shared guarded update; retain approval evidence |
| Work items (file mode) | `work/board.json` | `<delivery lead>` | `views/board.html` | Shared guarded update; preserve IDs and proof |
| Requirements and plans | `<canonical document paths>` | `<owners>` | `<optional>` | `<document review and acceptance procedure>` |

For external-tracker mode, replace the Work row's authority with the tracker and its binding
record. The old file is an archive. Label any continuing board as a derived view with its
collection time and source revision. Do not leave both locations writable as independent queues.

## Commands and recovery

Record the **absolute local path to the pinned** `templates/project-records.py` and these
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
