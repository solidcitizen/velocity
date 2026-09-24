# Executive Check-in Desk — `<project>`

> A **living page**, not a chat thread: the single, standing list of everything this project's
> [Operator](../docs/ROLE-AUTHORITY.md#operator) — the executive sponsor who owns mission,
> priority, and go/no-go — must decide or do right now. Optional project-overlay artifact; a
> companion to the [Handoff Packet](handoff-packet.md) and [Review Pack Template](review-pack-template.md),
> which carry one piece of work to its next owner. The Check-in Desk is the cross-cutting
> surface instead: every open ask to the one person whose decision is a hard gate, in one place,
> so none of them live only in chat history.
>
> **Build it from the data file and the renderer, never by hand.** The page is derived from
> `desk.json` by [`render-checkin-desk.py`](render-checkin-desk.py), which validates the file
> against this contract and marks every violation at the top of the page. Only the project name, the
> operator, the maintainer, the time-zone label, and the color tokens vary from one project to
> the next. Start from [`executive-checkin-desk.example.json`](executive-checkin-desk.example.json);
> the field definitions are in [`executive-checkin-desk.schema.json`](executive-checkin-desk.schema.json).

## Why this exists

The failure this template closes: an ask made once, mid-session, and later referred to only as
"the earlier message" — the operator then has no durable way to find what they ruled, what is
still open, or what is waiting on them, without searching chat scrollback. Velocity already holds
that a [Coordinator](../docs/ROLE-AUTHORITY.md#coordinator) must not bury operator decisions
inside long narrative updates; an ask that lives only in a transcript does exactly that, even
when no one intends it. The Check-in Desk gives every ask a stable identity and one page the
operator can open cold and act on without asking anyone to re-explain it.

A second failure this revision closes: an operator who runs several projects meets several
desks. When each project rebuilds the page its own way, the operator relearns the page every
time, and the differences are pure cost. The desk is a shared surface across all of an
operator's projects, so it has one shape, and a real gap in that shape is fixed here, by a
[process-change proposal](process-change-proposal.md), never by a local variant.

## Contract

The rules below make the page work. A project overlay may not weaken, extend, or restyle them
beyond the five things that vary. The renderer enforces every rule it can check.

1. **Stable IDs, never renumbered.** Every entry gets an ID `CK-<n>` the first time it appears:
   positive integers, unique, contiguous from 1, never reused. The prefix is always `CK`; a
   project never invents another. An ask that stops needing an answer is not deleted or
   renumbered: it closes as **withdrawn**, with the reason, and keeps its ID. Team decisions
   carry IDs from the same sequence.
2. **Every ask is self-contained.** Title; what it is (assume the reader has read nothing else);
   for a Decide, the options and the delivery lead's **lean** with a one-line reason; **needed
   by**, as a date and time in the operator's own time zone or "no date"; and what waits, or
   stays blocked, until the operator answers. Never "the ruling from an earlier message" or a
   pointer back into chat.
3. **Five sections, fixed order, exact headings.** *Decide* — decisions only the operator can
   make. *Do* — actions only the operator can take: entering credentials, approving a purchase,
   authorizing a host-level or production change, making a phone call. *Decided by the team* —
   decisions the delivery lead made within its own authority and owns. *Already answered* — every
   closed ask, newest first. *How to reply* — reply-by-ID examples. No other section exists.
   Status narrative never appears on the desk; a status message may cite an ask's ID and must
   never re-explain what the page already holds.
4. **The header is computed.** The H1 is `<Project> Check-in Desk`. The stamp reads
   `Last updated: <day date time tz> · operator <name> · maintained by <role>`. Three totals
   follow: decisions waiting, actions only the operator can take, deadlines landing in the next
   seven days. The renderer counts them; nobody types them.
5. **Republished the same turn.** The page is republished the same turn an ask is added,
   answered, withdrawn, or closed, and the `updated` stamp changes in the same edit as the
   content — never batched, never left stale.
6. **Decisions are made and owned, never parked.** A decision within the delivery lead's own
   authority is made by the lead, who owns the outcome, and is recorded under *Decided by the
   team* with the date, the owner, the decision, **why**, and a **status** whose first word is one
   of `done`, `in motion`, `blocked`, `reversed`, followed by any detail. It is never listed under
   Decide with a veto window. When the lead is unsure whether a decision is theirs to make, that
   uncertainty *is* the ask: put it under Decide as a question about the authority boundary.
   Those asks teach both sides where the line is, and they are worth the operator's time.
7. **Silence is never consent.** An open ask stays open until it is answered. "Needed by" says
   when the decision is needed and what waits until then; it never converts a non-answer into a
   yes. Urgency and a chosen lean are not the operator's approval either, per [Criticality Does
   Not Grant Mutation Authority](../docs/ROLE-AUTHORITY.md#criticality-does-not-grant-mutation-authority).
8. **One ask, one owner, and each desk is written only by its own lead.** When the same
   question is open on two desks — two of one operator's desks, or the desks of two entities whose
   leads work together — one desk owns it and the other carries a pointer entry (`owned_by`)
   naming the owning project and its ID, rendered as "Owned by *project* CK-n. Answer it there."
   Pointers keep their own ID and are excluded from the totals. When the owning ask closes, the
   pointer closes with it: same `answered_on`, state `answered` or `withdrawn`, a ruling that names
   the owner's decision, and `owned_by` kept, so the pointer is a pointer for its whole life and the
   closed entry reads "owned by *project* CK-n".
   Cross-references in prose are written as `<project> CK-n`. A desk's data file is written only
   by that project's own delivery lead. An ask that originates elsewhere arrives as a record the
   lead can cite (a handoff packet, a peer message, an issue) and is filed by that lead as an
   ordinary entry; nobody writes into another entity's desk.
9. **Decide vs. Do is a hard boundary.** If a delivery role could do it, it does not belong in
   Do. If a delivery role could decide it, it does not belong in Decide either: decide it, own
   it, and record it under *Decided by the team*.
10. **One way to build it.** The desk is the renderer's output from the project's data file,
    unmodified. Where the page is hosted — a private artifact, a static host, a file in the
    project repository — is the project's choice; what it contains is not. A need the data file
    cannot express is a template gap: raise it as a Velocity proposal, and keep the desk
    conformant meanwhile.
11. **A broken file still shows every ask.** Validation lists every violation and the renderer
    exits non-zero, but the page is still produced with a **Needs repair** block at the top and
    each missing field marked where it belongs, so one bad field never hides the other open asks
    from the operator. An entry the page cannot place at all (no usable id, kind, title, state, or
    date) is counted in that block, never guessed. `--check` alone reports and stops. The
    maintainer fixes the file, never the page.

## Data file and renderer

| Path | Role |
|---|---|
| `templates/executive-checkin-desk.schema.json` | Field definitions for `desk.json` (JSON Schema, documentation grade). |
| `templates/executive-checkin-desk.example.json` | Placeholder desk: copy it, rename it, replace every angle-bracket placeholder. |
| `templates/render-checkin-desk.py` | Validates and renders. Python 3.9+, standard library only. |
| `templates/executive-checkin-desk.html` | What the example renders to. Generated; do not edit. |

Keep populated data in the consuming project's operational workspace, separate from reusable
templates. Under the optional [Portable Project Records profile](portable-project-records.md),
declare that location in the shared artifact index, outside agent session/cache storage.

**Decision levels (optional).** A Decide entry may carry `decision_level`: `work`, `initiative`,
or `portfolio`. It names the level of the ruling requested, not the originating task or execution
lane. It is an optional tag: a desk without levels is complete, and a level appears as a row only
on the entries that carry one. Every supplied level is validated. State the affected record, the
decision owner's hat, and the authority basis in `what`; the desk's declared operator remains the
decision owner. Do and team entries may carry a level too. One desk can hold decisions at every
level within its ownership and access boundary; see the
[management reference](../examples/management-reference/README.md) example.

A project that wants every open decision labeled declares that in its overlay. Its checks then run
the renderer with `--require-decision-levels`, which covers open Decide entries including
pointers; a project that uses the [file helper](project-records.md) also sets
`"desk_requires_decision_levels": true` in its `records.json`. The requirement is the project's
declared choice, so a desk's validity never depends on who happens to run the check. Keep a level
when an ask is answered or withdrawn; a pointer uses the owning ask's level; do not infer a level
for historical rulings. The file helper refuses to drop an existing level or change it while
closing; to correct an open ask's classification, record the reason and retain the earlier
revision before answering it.

Separate desks require ownership/access boundaries that prevent a shared source; a change of
level, hat, or cadence alone does not create another board. Use the existing `owned_by` pointer
contract where separate desks are necessary. This introduces no new sections, level filter,
automatic synchronization, or committee approval mechanism.

An empty `entries` list is valid for a new Desk. The
[shared file helper](project-records.md) provides coordinated updates and recovery. Render with:

```
python3 render-checkin-desk.py desk.json --check              # validate; exit code 1 lists every violation
python3 render-checkin-desk.py desk.json --out desk.html      # standalone page for any static host (best-effort, exit 1, if the file breaks the contract)
python3 render-checkin-desk.py desk.json --fragment           # title, style, and main only, for artifact hosting
python3 render-checkin-desk.py desk.json --check --require-decision-levels  # management profile
```

What the renderer prints, so every desk reads the same:

| Where | Labels |
|---|---|
| Header | `Last updated:` · `operator` · `maintained by` · three totals |
| Decide entry | `What it is` · `Options` · `Lean` · `Needed by` |
| Do entry | `What it is` · `Needed by` |
| Team entry | `(date, owner)` · `Why:` · `Status:` |
| Answered entry | `(date)` · `Ruling:` (withdrawn entries read `Ruling: withdrawn — reason`) |
| Any entry with `decision_level` | `Decision level` · `Work`, `Initiative`, or `Portfolio`; retained with the ruling |
| How to reply | examples computed from the open asks, e.g. `CK-2 fine`, `CK-2 no, use <alternative>`, `CK-4 done`, `CK-3 revisit` |

Every date and time in the data file is the operator's local time; `tz_label` names the zone.
Write it without a UTC offset. If a value carries one, the renderer reads the time as written
and ignores the offset, so `2026-10-09T17:00-07:00` and `2026-10-09T17:00` show the same on
the page.

Only these vary per project: `project`, `operator`, `tz_label`, `maintainer`, and the color
tokens under `theme` and `theme_dark`. The renderer rejects any other token.

## Migrating a desk built before this revision

1. Copy every existing entry into `desk.json`, keeping its number. Rename any other prefix to
   `CK`. Fill a gap in the sequence with a `withdrawn` entry that says why it was dropped.
2. Give every team decision an ID if it lacks one, and pick its `status` first word from the
   fixed set; the rest of the old status text goes in `status_text`.
3. Move anything that is not an ask or a team decision off the desk: status narrative into the
   status message, invariants into the [System Invariant Register](system-invariant-register.md).
4. If another desk carries the same question, decide which desk owns it and turn the other entry
   into a pointer; if the owner has already answered, the pointer is a closed entry that keeps
   `owned_by`.
5. Run `--check` until it passes, render, and republish at the desk's existing address so the
   operator's link does not change.

---
### Template rules (load-bearing — keep them true in every instance)
- **No renumbering, ever.** An ID identifies a decision, not a position in a list. Reassigning
  `CK-3` to a different ask after the fact breaks every past reference to it.
- **Self-contained, no back-references.** "See the earlier message" is exactly the failure this
  template exists to remove. If an entry needs chat context to be actable, it is not ready to post.
- **Same-turn republish, same-edit stamp.** A page that is added to but not republished, or
  republished with a stale stamp, stops being the single source of truth.
- **Silence is never consent.** An open ask stays open until it is answered. "Needed by" says
  when the decision is needed and what waits until then; it never converts a non-answer into a
  yes. If the team must move before an answer arrives, the team makes the call within its own
  authority, owns it, and records it under *Decided by the team*.
- **Decide vs. Do is a hard boundary, not a tone choice.** If a delivery role could do it, it
  does not belong in Do. If a delivery role could decide it, it does not belong in Decide either.
- **One shape across every project.** The renderer's output is the desk. A local variant is not
  a customization; it is a gap report that has not been filed yet.
