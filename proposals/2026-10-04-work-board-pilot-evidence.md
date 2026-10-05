# Work Board: Two Weeks of Pilot Evidence

- Status: Proposed
- Date: 2026-10-04
- Authority owner: Mike, Velocity Maintainer
- Mode: Process evolution
- Source: The Work Board was released in v1.9.0 with a commitment to fold its pilots' evidence into
  the template. Two consuming projects and Velocity itself have run boards since 2026-09-21 to
  2026-09-23. The first project left two findings dated 2026-09-23 for the Velocity CPO session,
  and its board data was read on 2026-10-04 (read-only). The fold was due 2026-09-28, slipped twice,
  and the maintainer asked for it on 2026-10-04.
- Disposition: Velocity repo proposal; pending the maintainer's approval.
- Proposed version: planned v1.10.0 (minor)

## Change

1. **Rule 2.** A held item's `event` names the observable trigger and what brings it, not the work
   that follows; an item waiting on two events is two items. The schema description of
   `waits_on` says the same. The renderer cannot check wording, so this is a contract rule kept
   by the maintainer.
2. **Adoption notes.** A wrapper may refresh a control's `last_completed` and `proof` from the
   newest receipt matching its `evidence` pattern. The note on controls now leads with that
   structural fix and keeps the receipt pre-flight as the backstop. It states the limit: an
   unattended run updates the data and the local page, not the operator's published page.
3. **Pilot record.** Four dated entries: the two 2026-09-23 findings, the v1.9.0 and v1.9.1 renderer
   fixes, and a two-week summary of three boards, including the first project's finding that its
   in-motion count misread its load.

## Why

Both findings came from the operator's reading of a live page or from an unattended day, which are
the conditions the template exists for. Each was fixed on the project's side first, with the
wording proposed back to Velocity rather than kept as a local variant.

## Evidence (as read 2026-10-04)

| Board | Items | Closed | Closed with proof | Dropped | Controls |
|---|---|---|---|---|---|
| First consuming project | 102 (from 52 on 2026-09-21) | 49 | 47 (2 before `adopted`) | 10 | 11, 6 run by software |
| Second consuming project | 26 | 9 | 9 | 0 | 4 |
| Velocity's own board | 42 | 25 | 25 | 1 | 4 |

The first project still carries `uncertain` on 20 items. It showed 29 items in motion (13 doing,
16 committed) against 5 in backlog. Asked on 2026-10-04, its maintainer reported that the count
misread its load. Several "doing" items had finished or been superseded, and a week's substantial
work never reached the board, because the agent moving items did not republish in the same turn
(rule 9). The project names that its own discipline failure, not a template defect. It groomed
the board the same day, using the evidence: 2 items closed with proof, 1 dropped as superseded,
and 7 added for the week's unrecorded work, all done with commit proof. In motion is now 27 (10
doing, 17 committed), mostly genuinely open or awaiting evidence. The table shows the groomed board,
re-read and re-validated on 2026-10-04.

Its suggestion is not in this change because it needs a schema field and a renderer change: show
each in-motion item's age in its state, and count in-motion items untouched for more than seven
days. That would have exposed the drift. It is a candidate for a later release, with the usual
notice to consuming projects.

## Scope and Authority

Affected protected artifacts: `templates/work-board.md` and `templates/work-board.schema.json`
(description text only). Also `CHANGELOG.md`. Template support. No renderer, schema rule, or
validation change, so no consuming board can fail because of this change.

## Proof and Disposition

- 37 of 37 tests pass. The template's example renders byte-identical to its committed page.
- 458 relative links resolve; `git diff --check` is clean; no consuming project is named.
- If PR #21 (the goal-setting charter) merges first, this branch's CHANGELOG block joins its
  `[Unreleased] — planned 1.10.0` block.

Branch disposition: `proposal/work-board-pilot-evidence`, via pull request.
