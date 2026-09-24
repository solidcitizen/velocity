# Times Read as Written: the UTC-Offset Crash Fix

- Status: Proposed
- Date: 2026-09-24
- Authority owner: Mike, Velocity Maintainer
- Mode: Process evolution — patch
- Source: On 2026-09-24, hours after v1.9.0 shipped, a pilot project added seventeen asks whose
  `needed_by` carried a UTC offset while its desk's `updated` did not. `--check` passed; the
  render crashed comparing the two kinds of time, wrote no page, and never reached the repair
  block. The project normalized its own file and reported the defect to Velocity rather than
  working around it locally. The Work Board renderer had the same defect.
- Disposition: Velocity repo proposal; pending the maintainer's approval.
- Proposed version: v1.9.1 (patch)

## Change

Both renderers read every date and time as written, in the operator's zone, and ignore a UTC
offset if one is present. The desk and board contracts, and their schemas, state it: times are
the operator's local time, named by `tz_label`; write them without an offset; an offset, if
present, is ignored. The CHANGELOG also records the one expected difference in rendered pages
for a project moving from `v2.0.0-experimental.1`: the footer's version line.

## Why this fix, not the stricter one

Rejecting offsets in `--check` was considered. It would make a working desk fail: another
consuming project writes its desk's `updated` with an offset today, and that desk renders
correctly under v1.9.0. Rejecting it would turn a crash fix into a compatibility break. Reading
the time as written matches what both renderers already display for an offset-bearing value, so
the fix changes nothing that rendered before and ends the crash. Its limit: a time written with a
different zone's offset (for example UTC) shows its own wall-clock time, not the operator's. The
contracts tell writers to use local time; `tz_label` is a label, not a zone database name, so the
renderer cannot convert.

## Scope and Authority

Affected protected artifacts: `templates/render-checkin-desk.py`, `templates/render-work-board.py`,
`templates/executive-checkin-desk.md`, `templates/work-board.md`, and both schemas. Also
`CHANGELOG.md` and `tests/`. Template support; no lifecycle rule, role, approval boundary, or
proof obligation changes.

## Proof and Disposition

- The reported case (naive `updated`, offset `needed_by`) reproduced on v1.9.0 in both renderers:
  `--check` exit 0, render `TypeError`. With the fix, both render and exit 0.
- 37 of 37 tests pass, including new tests: an offset time renders identically to the same local
  time without one, in both renderers; an offset on `updated` alone renders; and the
  fault-injection suite now includes an offset value in every field.
- Every real project desk and board on this machine (six desks, three boards) and every example
  renders byte-identical to v1.9.0, and every one that passed `--check` still passes.

Branch disposition: `proposal/naive-local-times`, via pull request.
