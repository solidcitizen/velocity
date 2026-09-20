# Executive Check-in Board — `<entity>`

> A **living page** that lets the entity's [Operator](../docs/ROLE-AUTHORITY.md#operator) run a
> complete check-in without reading the repository or the chat: what is theirs to decide or do,
> where the entity is going, what is moving, what is waiting, and what happened. Optional
> project-overlay artifact. It **contains** the [Executive Check-in Desk](executive-checkin-desk.md)
> as its first section, unchanged, and adds the four views a steward needs for allocation and
> direction. The Handoff Packet and Review Pack still carry one piece of work to its next owner;
> this page is the standing surface above them.
>
> Entity-agnostic on purpose: the entity may be a product, a company, an operating function, a
> family, a person, or an AI agent acting for any of them. Fill the placeholders, delete this
> quote block, and repoint the canon links to your project's pinned Velocity reference.
>
> **What the Desk cannot do that the Board does:** the Desk holds only what is the Operator's to
> decide or do; it cannot show direction (initiatives and their posture), allocation (where
> committed effort sits), the uncommitted backlog, or the proof-backed record of what closed. The
> Board adds those four views and embeds the Desk unchanged, rendered by the Desk's own renderer
> from the Desk's own data file. It is not a second operator page; it is the page around the Desk.

## Why this exists

The Desk closes one failure: an ask to the Operator that lives only in chat. Two more failures sit
next to it. First, the Operator has no single place to see where effort is going, so allocation
happens by whoever spoke last. Second, the delivery lead's plan lives in a working file only the
lead can read, so "what is on for next week" has no better answer than a file link. The Board puts
the plan, the intent behind it, and the record of what shipped on the same page as the asks, in
the order a check-in actually runs.

## Contract

The Desk section keeps every rule of the [Desk contract](executive-checkin-desk.md#contract).
The rules below cover the rest of the page. A project overlay may extend them; it must not
weaken them.

1. **Five sections, fixed order.** *Desk* (the Operator's asks), *Initiatives* (direction and
   posture), *In progress* (committed work), *Planned* (wanted but uncommitted work), *Done*
   (dated ledger). A check-in reads top to bottom: what is mine, where are we going, what is
   moving, what is waiting, what happened.
2. **Three id families, never renumbered.** Asks keep the Desk's `CK-<n>`. Initiatives get
   `INI-<n>`. Work items get `WI-<n>` (a project may choose another prefix in its overlay, but
   one prefix per family, assigned once, increasing, never reused, kept after close). Every
   reply, status line, and commit that touches an item cites its id.
3. **One source of record per section; the page is derived from it.** The record may be a file
   in the repository, a board in an issue tracker (Jira, Linear, GitHub Projects), or a database;
   the page is generated or synchronized from that record, never hand-edited, so it cannot drift
   from the record and the record cannot say something the page does not. Which tool holds the
   record is the project's choice; that it is one record per section is the rule.
4. **Every work item carries one initiative.** No orphan items. That is what makes allocation
   visible: the Operator can read where hours went by initiative and say "less here, more there."
5. **Initiatives are the Operator's.** The delivery lead drafts them and proposes changes; a
   change to an initiative's intent, horizon, or posture is an Operator decision, raised and
   answered through the Desk, then applied. The lead may change an initiative's *next milestone*
   and *status* within its own authority and records that under the Desk's *Decided by the team*.
6. **Republish rules.** The Desk section republishes the same turn an ask changes (its own rule).
   The other sections republish whenever an item changes state and at every check-in, never
   batched past a check-in. A status message may cite ids; it never re-explains what the page
   holds.
7. **Done is a ledger, not a trophy case.** Items enter *Done* with the date they closed and the
   proof that closed them (a receipt, a verify line, a record path). The page shows the current
   period (default thirty days); the project's action log or changelog holds the rest.
8. **Peer-origin items are marked.** A work item that exists because another entity's delivery
   lead asked for it (see [Peer Exchange](peer-exchange.md)) carries its origin and the peer's
   own id, so cross-entity dependencies are visible without a relay through the Operator.
9. **Header totals.** The page opens with: decisions waiting, actions only the Operator can take,
   deadlines this week (all from the Desk), items in progress, items done this period.
10. **No second home for asks.** Anything on the Board that needs the Operator to decide or do
    is a Desk entry (a normal ask, or a pointer entry to the desk that owns it). The four Board
    views may cite `CK` ids; they never carry an ask, a lean, a needed-by, or a ruling of their
    own. An initiative's posture change, for instance, is raised on the Desk and reflected on
    the Board after the answer.
11. **The Board reads the Desk data file and never writes it.** The Board's own data
    (initiatives, work items, the closed record) lives in a separate file with its own schema,
    so a Board can be regenerated from the Desk data file plus the Board data file and nothing
    else. A Board renderer that edits desk data is non-conformant.
12. **Done cites proof; it does not judge it.** A closed item names its proof artifact in
    Velocity's existing terms, a review pack, a handoff packet, a closeout disposition, a
    receipt or record path, and links to it. The Board never restates the evidence or reaches
    its own verdict; proof is judged where the [Proof Model](../docs/PROOF-MODEL.md) says it is.

## Policy, not implementation

The contract above states what must be true. The skeleton below is one rendering of it, in
Markdown, for a project with no tracker. A project that runs its work in Jira, Linear, GitHub
Projects, or another platform satisfies the contract by mapping: the tracker's epics or goals as
initiatives, its issues as work items with the initiative as a required field, its statuses to
the five above, its closed-issue view with a proof field as *Done*, and the Desk kept as the
Operator's own surface. Ids may be the tracker's keys as long as they are stable and never
reused. Do not rebuild a tracker in Markdown to satisfy this template.

## Field definitions

**Initiative** (`INI-<n>`): title; *intent* (two or three sentences in the Operator's language:
what changes for the entity when this is achieved); *horizon* (a date or a quarter); *posture*
(`invest` / `sustain` / `wind down` / `hold`); *steward* (the role accountable); *next milestone*
(one line, dated); *risks it retires* (the risks or obligations this initiative addresses);
*measures* (how the Operator will know it is working); *status* (`proposed` / `active` /
`paused` / `done`). An initiative marked `proposed` is the delivery lead's draft awaiting the
Operator's edit; the page says so.

**Work item** (`WI-<n>`): title; *initiative* (exactly one `INI-<n>`); *type* (`feature` /
`defect` / `issue` / `chore` / `control`, where a *control* is recurring assurance work such as a
reconciliation or an audit); *size* (`S` / `M` / `L`, the lead's estimate); *status* (`planned` /
`this week` / `doing` / `blocked` / `done`); *why* (one line); *blocked by* (an id, a person, or
an external event, when blocked; a Desk ask is cited by its `CK` id); *origin*
(`peer:<entity>:<their id>` when it came from a peer, otherwise empty); *proof* (filled at
close: the proof artifact's kind and reference, e.g. `review pack RP-12`, `closeout
disposition 2026-04-01`, `receipt <path>`).

## Skeleton

```md
# <Entity> Check-in Board

_Last updated: <date/time, Operator's time zone> · Decisions waiting: <n> · Actions only the
Operator can take: <n> · Deadlines this week: <n> · In progress: <n> · Done this period: <n>_

## Desk
<the Executive Check-in Desk, rendered from its own source, contract unchanged>

## Initiatives
Where the entity is going. Drafted by the delivery lead, owned by the Operator; reply by id to
change intent, horizon, or posture.

### INI-1 — <title>  ·  <posture>  ·  horizon <date>  ·  <status>
- **Intent:** <what changes for the entity when this is achieved>
- **Steward:** <role>
- **Next milestone:** <one line, dated>
- **Risks it retires:** <list>
- **Measures:** <how the Operator will know>

## In progress
Committed for this period. One initiative per item.

| id | item | initiative | type | size | status | why / blocked by |
|---|---|---|---|---|---|---|
| WI-4 | <title> | INI-1 | feature | M | doing | <why> |

## Planned
Wanted, not yet committed. Grouped by initiative, in order.

### INI-1 — <title>
| id | item | type | size | why |
|---|---|---|---|---|
| WI-7 | <title> | defect | S | <why> |

## Done
Closed this period, newest first, with the proof that closed it. Older entries: <action log>.

- **WI-2** (<date>, INI-1): <title> — **Proof:** <receipt, verify line, or record path>

## How to reply
Reply by id, in your own words. Examples: `CK-3 yes` · `INI-2 hold` · `WI-7 this week` ·
`WI-4 drop` · `INI-1 horizon March`. A reply about an initiative's intent or posture is an
Operator decision and is recorded on the Desk ledger; a reply about a work item's order is
applied directly.
```

---
### Template rules (load-bearing — keep them true in every instance)
- **The Desk is embedded, not copied.** The Desk section is the output of
  `templates/render-checkin-desk.py` over the project's desk data file
  (`templates/executive-checkin-desk.schema.json`); a Board renderer never re-implements it, and
  the Desk's contract, ids, and same-turn rule are untouched. A cross-entity ask uses the Desk's
  pointer entry (one owner, a pointer on the other desk), not a copy.
- **No orphan items, no hand-edited page.** One initiative per item; one source per section.
- **Initiatives are the Operator's to edit; milestones and status are the lead's to move.**
- **Done cites proof and never judges it.** A closed item without a proof-artifact reference
  is not closed; the Board holds the reference, not the evidence or the verdict.
- **No ask lives on the Board.** Decide and Do exist only on the Desk; the Board cites `CK` ids.
- **Desk data is read-only to the Board.** Board data has its own file and schema.
- **Peer origin is visible.** Cross-entity work shows where it came from and the peer's id.
