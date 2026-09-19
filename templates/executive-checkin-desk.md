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
still open, or what is waiting on them, without searching chat scrollback. Velocity
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
   (its **lean**), and the date it is needed by in the operator's own time zone, with what waits
   until then — never "the ruling from an earlier message" or a pointer back into chat. Someone
   who has read nothing else should be able to act on one ask from its own entry alone.
3. **Five sections, fixed order.**
   - **Decide** — decisions only the operator can make, each with the delivery lead's lean. An
     ask stays open until the operator answers it; silence is not an answer.
   - **Do** — actions only the operator can take: entering credentials, approving a purchase,
     authorizing a host-level or production change, making a phone call. Nothing a delivery role
     is equally capable of doing belongs here.
   - **Decided by the team** — a dated ledger of decisions the delivery lead made within its own
     authority and owns, newest first, each with the owner and the reason. This is where the
     operator sees what is being decided in the project's name.
   - **Already answered** — a dated ledger of every ask the operator closed, newest first, IDs intact.
   - **How to reply** — reply by ID, e.g. `CK-2 fine`, `CK-2 no, use <alternative>`, `CK-4 Saturday`.
4. **Header totals.** The page opens with three counts: decisions waiting, actions only the
   operator can take, and deadlines landing this week. The operator should be able to read the
   header alone and know whether anything is urgent.
5. **Republished the same turn.** The page is republished the same turn an ask is added,
   answered, or closed — never batched for later. A status message may cite an ask's ID; it must
   never re-explain what the page already holds.
6. **Decisions are made and owned, never parked.** A decision within the delivery lead's own
   authority is made by the lead, who owns the outcome, and is recorded under *Decided by the
   team* with the date, the owner, and the reason. It is never listed under Decide with a veto
   window: silence is not consent, and a missed deadline is not an approval. Urgency and a chosen
   lean are not the operator's approval either, per [Criticality Does Not Grant Mutation
   Authority](../docs/ROLE-AUTHORITY.md#criticality-does-not-grant-mutation-authority); only an
   explicit answer resolves an ask that is the operator's to answer. When the lead is unsure
   whether a decision is theirs to make, that uncertainty *is* the ask: put it under Decide as a
   question about the authority boundary. Those are the asks that teach both sides where the
   line is, and they are worth the operator's time.

## Skeleton

```md
# <Project> Check-in Desk

_Last updated: <date/time, operator's time zone> · Decisions waiting: <n> · Actions only the
operator can take: <n> · Deadlines this week: <n>_

## Decide

Decisions only you can make. Each stays open until you answer it.

### CK-1 — <short title>
- **What it is:** <one or two sentences; assume no prior context>
- **Options:** <A> / <B> / <C>
- **Lean:** <recommendation> — <one-line reason>
- **Needed by:** <date, time, operator's time zone> — <what waits until then>

## Do

Actions only you can take. Nothing here can be delegated back to a delivery role.

### CK-2 — <short title>
- **What it is:** <what you specifically must do, and why it can't be done for you>
- **Needed by:** <date, time, operator's time zone> — <what stays blocked until then>

## Decided by the team

Decisions made within the team's own authority. Made, owned, and recorded here so you can see
them; reply by ID if you want one revisited.

- **CK-3** (<date>, <owner>): <what was decided> — **Why:** <one-line reason> — **Status:** <done / in motion>

## Already answered

Closed asks, newest first. Dated, kept forever, IDs never reused.

- **CK-0** (<date answered>): <one-line summary of the ask> — **Ruling:** <what was decided>

## How to reply

Reply by ID. Examples: `CK-1 fine` · `CK-1 no, use <alternative>` · `CK-2 Saturday` · `CK-3 revisit`.
```

---
### Template rules (load-bearing — keep them true in every instance)
- **No renumbering, ever.** An ID identifies a decision, not a position in a list. Reassigning
  `CK-3` to a different ask after the fact breaks every past reference to it.
- **Self-contained, no back-references.** "See the earlier message" is exactly the failure this
  template exists to remove. If an entry needs chat context to be actable, it is not ready to post.
- **Same-turn republish.** A page that is added to but not republished stops being the single
  source of truth — it re-creates the "check chat for the latest" problem one layer up.
- **Silence is never consent.** An open ask stays open until it is answered. "Needed by" says
  when the decision is needed and what waits until then; it never converts a non-answer into a
  yes. If the team must move before an answer arrives, the team makes the call within its own
  authority, owns it, and records it under *Decided by the team*.
- **Decide vs. Do is a hard boundary, not a tone choice.** If a delivery role could do it, it
  does not belong in Do. If a delivery role could decide it, it does not belong in Decide either:
  decide it, own it, and record it under *Decided by the team*.
