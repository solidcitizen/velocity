# Executive Check-in Desk — `<project>`

> A **living page**, not a chat thread: the single, standing list of everything this project's
> [Operator](../docs/ROLE-AUTHORITY.md#operator) — the executive sponsor who owns mission,
> priority, and go/no-go — must decide or do right now. Optional project-overlay artifact; a
> companion to the [Handoff Packet](handoff-packet.md) and [Review Pack Template](review-pack-template.md),
> which carry one piece of work to its next owner. The Check-in Desk is the cross-cutting
> surface instead: every open ask to the one person whose decision is a hard gate, in one place,
> so none of them live only in chat history.
>
> Practiced on a private consuming project since 2026-09-14 under a project-specific name; this
> is the generalized, reusable form. Fill the placeholders, delete this quote block, and repoint
> the canon link above to your project's pinned Velocity reference when instantiating.

## Why this exists

The failure this template closes: an ask made once, mid-session, and later referred to only as
"the earlier message" — the operator then has no durable way to find what they ruled, what is
still open, or what happens if they never answer, without searching chat scrollback. Velocity
already holds that a [Coordinator](../docs/ROLE-AUTHORITY.md#coordinator) must not bury operator
decisions inside long narrative updates; an ask that lives only in a transcript does exactly
that, even when no one intends it. The Check-in Desk gives every ask a stable identity and one
page the operator can open cold and act on — or knowingly leave — without asking anyone to
re-explain it.

## Contract

The rules below make the page work. A project overlay may extend them; it must not weaken them.

1. **Stable IDs, never renumbered.** Every ask gets an ID (`CK-<n>`) the first time it appears,
   assigned once, in increasing order, and never reused or renumbered — including after the ask
   closes. A closed ask keeps its ID and moves to the "Already answered" ledger below, dated, so
   the operator can find what they ruled without searching chat.
2. **Every ask is self-contained.** What it is, the options, the delivery lead's recommendation
   (its **lean**), the deadline in the operator's own time zone, and what happens **if silent**
   — never "the ruling from an earlier message" or a pointer back into chat. Someone who has read
   nothing else should be able to act on one ask from its own entry alone.
3. **Four sections, fixed order.**
   - **Decide** — rulings awaiting the operator's veto or "fine": a lean already chosen, waiting
     to be confirmed or overridden.
   - **Do** — actions only the operator can take: entering credentials, approving a purchase,
     authorizing a host-level or production change, making a phone call. Nothing a delivery role
     is equally capable of doing belongs here.
   - **Already answered** — a dated ledger of every closed ask, newest first, IDs intact.
   - **How to reply** — reply by ID, e.g. `CK-2 fine`, `CK-2 veto, use <alternative>`, `CK-4 Saturday`.
4. **Header totals.** The page opens with three counts: decisions waiting, actions only the
   operator can take, and deadlines landing this week. The operator should be able to read the
   header alone and know whether anything is urgent.
5. **Republished the same turn.** The page is republished the same turn an ask is added,
   answered, or closed — never batched for later. A status message may cite an ask's ID; it must
   never re-explain what the page already holds.
6. **Delegated rulings are decisions, with a default.** When the delivery lead makes a call
   within its own authority but the operator could still veto it, it appears under Decide with
   an explicit **if silent, it stands**. This matches [Criticality Does Not Grant Mutation
   Authority](../docs/ROLE-AUTHORITY.md#criticality-does-not-grant-mutation-authority): urgency
   and a chosen lean are not the operator's approval — only an explicit answer, or an explicit
   silence rule stated in advance, resolves that.

## Skeleton

```md
# <Project> Check-in Desk

_Last updated: <date/time, operator's time zone> · Decisions waiting: <n> · Actions only the
operator can take: <n> · Deadlines this week: <n>_

## Decide

Rulings awaiting your veto or "fine". Each stands as recommended if you say nothing by its
deadline, unless its own entry says otherwise.

### CK-1 — <short title>
- **What it is:** <one or two sentences; assume no prior context>
- **Options:** <A> / <B> / <C>
- **Lean:** <recommendation> — <one-line reason>
- **Deadline:** <date, time, operator's time zone>
- **If silent:** <what happens automatically>

## Do

Actions only you can take. Nothing here can be delegated back to a delivery role.

### CK-2 — <short title>
- **What it is:** <what you specifically must do, and why it can't be done for you>
- **Deadline:** <date, time, operator's time zone>
- **If silent:** <what stays blocked>

## Already answered

Closed asks, newest first. Dated, kept forever, IDs never reused.

- **CK-0** (<date answered>): <one-line summary of the ask> — **Ruling:** <what was decided>

## How to reply

Reply by ID. Examples: `CK-1 fine` · `CK-1 veto, use <alternative>` · `CK-2 Saturday`.
```

---
### Template rules (load-bearing — keep them true in every instance)
- **No renumbering, ever.** An ID identifies a decision, not a position in a list. Reassigning
  `CK-3` to a different ask after the fact breaks every past reference to it.
- **Self-contained, no back-references.** "See the earlier message" is exactly the failure this
  template exists to remove. If an entry needs chat context to be actable, it is not ready to post.
- **Same-turn republish.** A page that is added to but not republished stops being the single
  source of truth — it re-creates the "check chat for the latest" problem one layer up.
- **Silence has a stated consequence.** Every entry names what happens if the operator never
  replies. An entry with no "if silent" is not done.
- **Decide vs. Do is a hard boundary, not a tone choice.** If a delivery role could do it, it
  does not belong in Do — put it in Decide, or handle it without the operator at all.
