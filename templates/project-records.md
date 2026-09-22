# Project Records File Support

Development support for the opt-in [Portable Project Records profile](../docs/PORTABLE-PROJECT-RECORDS.md).
The Work Board remains a pilot. A tool installation does not adopt the profile or migrate a
live project. Pin the whole template directory at a reviewed revision.

This helper implements the structured JSON binding only. A project may instead retain its
authoritative `TODO.md` under the [Markdown work contract](work-tracker.md). These commands
do not parse, synchronize, or render Markdown, manage investment gates, or enforce the
adequacy of a decision context.

## Runtime and trust boundary

`project-records.py` uses Python 3.9+ and the standard library, including POSIX `flock`.
Supported scope: cooperating command-line writers on one local POSIX filesystem. Windows,
network/cloud-synced filesystems, distributed locks, and external tracker APIs are not qualified.
The HTML renderers can be used independently where their own runtime requirements are met.

The project owns the files. Agents use the same commands, regardless of their model/provider.
The helper is **not an authorization service**: `actor` and `authority_reference` are recorded
claims. OS/service access, protected wrappers, and the existing role rules establish authority.
An agent that can directly edit files can bypass this helper, so its lock is not an adversarial
security boundary. The journal is recoverable history, not a tamper-proof audit system.

## Start and discover

Run with an empty, project-owned operational directory outside vendor session/cache storage:

```sh
python3 templates/project-records.py init /path/to/project-records \
  --project-id example-app --project 'Example App' \
  --operator 'Project owner' --maintainer 'Delivery lead' --timezone UTC
python3 templates/project-records.py status /path/to/project-records
```

`init` creates an empty Desk and Work Board, standalone HTML views, `records.json`, a view
receipt, and [ARTIFACTS.md](artifact-index.md). Complete the ownership/access/backup/tool-pin
fields in that index and link it from the overlay and all agent entry files. It does not copy
or infer operational data. Select the structured JSON Work row and remove the alternative
binding rows; declare the inherited decision context before operational use. `records.json`
binds the two sources and views to safe relative paths within the workspace; keep source, view,
and history paths distinct.

## Prepare and apply a change

Read the actual sources and `status` before building a request. Each update value is a complete
candidate document, including unchanged entries. Both base revisions are required because
work may depend on Desk decisions. Revisions are SHA-256 over UTF-8 JSON with sorted object
keys, compact separators, and finite JSON numbers. Array order is significant. Whitespace in
the source file is not. The helper updates the `updated` stamp in the configured IANA time zone.

Request shape (illustrative placeholders, not a runnable request):

```json
{
  "operation_id": "request-unique-id",
  "actor": "Delivery lead through session A",
  "reason": "Record the authorized request",
  "authority_reference": "project role/delegation or specific decision evidence",
  "base_revisions": {"desk": "<status revision>", "work": "<status revision>"},
  "updates": {"work": {"<complete board.json candidate>": "<including unchanged items>"}}
}
```

```sh
python3 templates/project-records.py apply /path/to/project-records /path/to/request.json
```

The helper validates through the shared renderers, checks local Desk references and retention
of assigned IDs, serializes writers, writes a `prepared` journal with before/after snapshots,
saves Desk before Work, rereads the sources, then renders and verifies the local views through
hash receipts. It does not infer whether a human approved a decision, whether proof is adequate,
or whether an existing ID has been semantically reassigned. Those remain role/review duties.

Reuse the same operation ID **and unchanged request** for a retry. A completed retry returns
the prior completion and current status without writing its old snapshot over newer work.
Reusing an ID for a different request fails. A stale base revision fails before any source
change. Missing or malformed fields and deleted old IDs also fail before a journal is created.

## Failure and recovery

All supported readers/writers should use `status` to check pending operations before acting.
Raw file readers can see a partially saved pair after an interrupted update. The journal
records that interruption; this is a recoverable sequence, not a multi-file atomic transaction.

```sh
python3 templates/project-records.py status /path/to/project-records
python3 templates/project-records.py recover /path/to/project-records request-unique-id
python3 templates/project-records.py refresh /path/to/project-records
```

Recovery requires the same configuration/tool revision and sources that still match each
recorded before/after snapshot. It finishes the pending change and local views. Divergent
source content stops recovery for owner reconciliation. While an operation is pending, new
operations and exports are refused. Publication failures retain the journal with an error and
the source-save state. Correct the cause, then recover; never treat the old page as current.

`status` compares source revisions, generated file bytes, configuration, and tool revision against the view
receipt. An edited, missing, stale, or differently rendered view reads `view_current: false`.
Opening a file in an AI panel and remote publication require separate integration read-back.

## Export and rehearse a tracker mapping

```sh
python3 templates/project-records.py export /path/to/project-records /path/to/export-001.json
python3 templates/project-records.py handoff-check /path/to/export-001.json /path/to/readback.json
```

Export writes a new file outside the operational workspace containing the project identity,
configuration, source revisions, full records, and operation history. Existing snapshot files
are never overwritten. This JSON bundle does not copy linked evidence files; the handoff owner
must inventory and preserve their accessibility separately.

The destination adapter produces a normalized read-back with this shape:

```json
{
  "format_version": 1,
  "project_id": "example-app",
  "bundle_revision": "<export receipt bundle_revision>",
  "destination": "<selected tracker and scope>",
  "destination_revision": "<exact read-back revision or snapshot identity>",
  "readback_evidence": "<receipt for real destination queries>",
  "items": [
    {
      "source_id": 1,
      "destination_id": "<destination key or immutable archive reference>",
      "disposition": "imported",
      "normalized_record": {"<all original item fields normalized from destination>": "<values>"}
    }
  ]
}
```

The comparison requires a one-to-one identity mapping and equality of every original item
field, including uncertainties, references, and control metadata. Only done/dropped work can
use `archived`; active work and controls must be imported. No native label mapping or connector
is supplied. `snapshot_verified` proves this comparison only. It does not authenticate the
snapshot or prove remote reads, evidence access, migration of recurring execution, cutover,
or restoration. Use the [Tracker Binding and Handoff](tracker-binding-and-handoff.md) record.

After a verified, owner-authorized cutover, freeze updates, ensure there is no pending operation,
and set `records.json` mode to `external-tracker` with a non-empty `tracker_binding` locator.
The helper then refuses Work updates; Desk updates can continue. Preserve the file binding
as the archive and run `refresh` to label its HTML archived. The helper does not refresh a Work
view from the external tracker. An explicitly qualified external adapter is required for that behavior.
