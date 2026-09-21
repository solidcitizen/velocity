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
3. **Work in hand belongs to bounded work.** A *doing* or *done* item names the tranche or issue
   record it belongs to.
4. **Done cites proof; it does not judge it.** An item reaches *done* only with a proof artifact
   in Velocity's terms: a review pack, a handoff packet, a closeout disposition, a receipt id, or
   a record path. The board shows the citation and nothing more.
5. **Controls recur.** Recurring assurance work (a reconcile, an audit, a periodic package) is a
   *control* with a cadence and its last completion's proof. A control never leaves the board;
   its next due date is computed, and an overdue control is marked.
6. **Operator decisions never live on the board.** Anything that needs the operator's decision or
   action is a [Check-in Desk](executive-checkin-desk.md) ask. The board item that waits on it is
   *blocked* with `waits_on.ask` naming `<project> CK-n`. The board never carries a lean, a
   needed-by for the operator, or a ruling.
7. **Peer-originated work is marked.** An item that exists because another entity asked carries
   `origin` (their project and their id). Work whose normal path runs without an agent carries
   `automated: true`, so the project can count it.
8. **The header is computed.** Four totals: in motion (doing + committed), waiting (blocked +
   held), backlog, and due this week (needed-by dates, held-until dates, and control due dates
   inside seven days). Nobody types them.
9. **Republished the same turn** an item is added, moved, closed, or dropped, with the `updated`
   stamp changed in the same edit.
10. **One way to build it.** The board is the renderer's output from the project's data file,
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

Only these vary per project: `project`, `maintainer`, `tz_label`, `desk`, and the color tokens
under `theme` and `theme_dark`.
