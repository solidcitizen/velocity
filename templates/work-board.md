# Work Board — `<project>`

> **Pilot draft, not canon.** This template is being proven on one consuming project before it is
> proposed for release. Its contract may change on that project's evidence. Until it is accepted,
> nothing here binds any other project.
>
> A **living page** of a project's active work, for projects that have no issue tracker or board of
> their own and want one their delivery agent keeps current. It is the standing answer to "what is
> being done, what is waiting, and on what," the way the [Executive Check-in Desk](executive-checkin-desk.md)
> is the standing answer to "what does the operator need to decide or do." The two are one system:
> operator decisions live only on the desk, and the board names them by `CK` id.
>
> **Build it from the data file and the renderer, never by hand.** The page is derived from
> `board.json` by [`render-work-board.py`](render-work-board.py), which validates the file against
> this contract and refuses to render a board that breaks it. Start from
> [`work-board.example.json`](work-board.example.json); the field definitions are in
> [`work-board.schema.json`](work-board.schema.json).

## Contract

1. **Stable IDs, never renumbered.** Every item gets `WI-<n>` once: positive integers, unique,
   contiguous from 1, never reused. An item that will not be done is not deleted; it closes as
   **dropped**, with the reason, and keeps its id.
2. **Seven states, and the state says what the item waits on.** *backlog* (wanted, not scheduled),
   *committed* (named for a week or a date), *doing*, *blocked* (waits on a desk ask or another
   item, named in `waits_on`), *held* (waits on an external event with a date, named in
   `waits_on`), *done* (closed with proof), *dropped* (closed without doing, with a reason). The
   renderer refuses a blocked or held item that does not name what it waits on. "Blocked on the
   operator" and "held until Monday's read-back" are an ask and a calendar; the board keeps them
   apart.
3. **Work in hand belongs to bounded work.** A *doing* or *done* item names what bounds it: a
   tranche, an issue record, a control document, an ADR, a decision (`CK` id), or an evidence
   folder. A project that adopts the board with history sets `adopted` to the day its discipline
   began; *done* items closed before that date are history and may omit `belongs_to` and proof,
   and the page marks them **operator-reported**. From `adopted` on, the rule holds.
4. **Done cites proof; it does not judge it.** An item reaches *done* only with a proof artifact
   in Velocity's terms: a review pack, a handoff packet, a closeout disposition, a receipt id, or
   a record path. The board shows the citation and nothing more.
5. **Controls recur.** Recurring assurance work (a reconcile, an audit, a periodic package) is a
   *control* with a cadence, its last completion's proof, and `evidence`, the path pattern where
   every completion's proof lives. A control never leaves the board; its next due date is
   computed, an overdue control is marked, a control built but never run reads "due now", and a
   control that is defined but not yet built (`planned: true`) is shown as such and not counted.
6. **Operator decisions never live on the board.** Anything that needs the operator's decision or
   action is a [Check-in Desk](executive-checkin-desk.md) ask. The board item that waits on it is
   *blocked* with `waits_on.ask` naming `<project> CK-n`. The board never carries a lean, a
   needed-by for the operator, or a ruling.
7. **Peer-originated and automated work is marked.** An item that exists because another entity
   asked carries `origin` (their project and their id). `automated` says how an item's normal path
   runs: by software, by an agent on schedule, or when a person triggers it; the page counts each,
   and the software bucket is the measure of a software-owned function. An optional `size`
   (S, M, L) lets a backlog be ranked roughly.
8. **The header is computed.** Five totals: in motion (doing + committed), waiting (blocked +
   held), backlog, due this week (needed-by dates, held-until dates, and non-daily control due
   dates inside seven days), and controls built but never run. Below them, open work by
   initiative, work from peers, and work that runs without an agent. Section headings carry
   their counts; Backlog and Done are grouped by initiative. Nobody types any of it.
9. **Republished the same turn** an item is added, moved, closed, or dropped, with the `updated`
   stamp changed in the same edit.
10. **Provenance has a home; unknown fields do not.** `source` holds where an item came from (a
    queue paragraph, a log line) and is kept, not shown. `uncertain` lists the fields the
    maintainer could not confirm, each exactly `field: why` with a real field name, and the page
    tags the item **unconfirmed** naming only the fields, with the reasons on hover. The source
    shows on hover over the id. Any other field is rejected, so a typo cannot pass silently.
11. **A broken file still shows the board.** Validation lists every violation and the renderer
    exits non-zero, but the page is still produced with a **Needs repair** block at the top, so one
    stale field never hides the other fifty items from the operator. `--check` alone reports and
    stops. The maintainer fixes the file, never the page.
12. **One way to build it.** The board is the renderer's output from the project's data file,
    unmodified. A need the data file cannot express is a gap report to Velocity, not a local
    variant.

## Data file and renderer

| Path | Role |
|---|---|
| `templates/work-board.schema.json` | Field definitions for `board.json`. |
| `templates/work-board.example.json` | Placeholder board: copy it, replace every angle-bracket placeholder. |
| `templates/render-work-board.py` | Validates and renders. Python 3.9+, standard library only. |
| `templates/work-board.html` | What the example renders to. Generated; do not edit. |

```
python3 render-work-board.py board.json --check              # validate; exit code 1 lists every violation
python3 render-work-board.py board.json --out board.html     # standalone page for any static host
python3 render-work-board.py board.json --fragment           # title, style, and main only, for artifact hosting
```

Only these vary per project: `project`, `maintainer`, `tz_label`, `desk`, `adopted`, and the color
tokens under `theme` and `theme_dark`.

## Adoption notes

- **A project's wrapper stamps and publishes; it implements nothing.** A project may automate the
  workflow around the board (set `updated`, run the renderer with `--check` and then `--fragment`,
  publish the output unmodified). It may not validate, order, total, or render on its own; any of
  those in project code is the local variant the standard forbids. Pin the renderer from the
  project's Velocity checkout so the board and the standard move together.
- **The board is kept by the delivery agent.** Every move is an edit to the data file and a
  republish the same turn. That cost is small for an agent-kept queue and heavy for a person;
  a project whose queue is kept by hand should keep its existing tracker and adopt only the desk.
- **Controls trust `last_completed` as entered.** The renderer reads the data file and nothing
  else. A project whose control receipts live at a known path can add a pre-flight to its wrapper
  that compares the newest receipt to `last_completed` and refuses to publish on a mismatch; that
  check belongs to the project, because only the project knows its evidence.

## Pilot record

- 2026-09-21, first hours live: `size` added for ranking; `automated` split into software / agent /
  person because the boolean could not show the software-owned measure; the wrapper rule, the
  maintenance-cost note, and the evidence pre-flight moved from messages into the adoption notes.
  Reported by the pilot: the seven states fit finance work without bending; controls that never
  leave the board and the proof-to-close rule with `adopted` forced an honest split between
  evidenced and remembered work.
- 2026-09-21, round 2, same project, live on the data file: ten findings from the rendered page,
  nine taken into the contract the same day (section counts, grouping by initiative, the due-week
  rules and the never-run count, planned controls, dependencies shown from both sides, unproven
  closes shown lighter, peer and automation counts, source on hover, the strict `uncertain` form);
  the tenth, a by-initiative allocation of committed effort, belongs to the entity layer above the
  board. The board surfaced two stale backlog items the flat queue had hidden; they were dropped
  with reasons.
- 2026-09-21, round 1, one consuming project, 52 items (43 work, 9 controls): the first draft
  failed 8 items and refused the page. Findings taken into the contract the same day: `adopted`
  and history closes (rule 3), `evidence` on controls (rule 5), `source` and `uncertain` with
  unknown fields rejected (rule 10), best-effort rendering with a repair block (rule 11), and the
  schema now declares every rule the renderer enforces. Under the revised draft the same data
  validates with two changes on the project's side (set `adopted`; rename its provenance field to
  `source`) and none to its substance.
