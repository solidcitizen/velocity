# Peer Exchange — Notice, Gate, Read-back, All-clear

> The protocol between two delivery leads whose entities share something: infrastructure, a
> data store, a dependency, a person's attention. Either lead may be a human or an agent, from
> any vendor. Optional project-overlay artifact; companion to the
> [Executive Check-in Desk](executive-checkin-desk.md) (asks to an Operator) and the
> [Handoff Packet](handoff-packet.md) (work moving to its next owner inside one entity). This
> template covers the third case: two entities coordinating as peers, with no shared Operator
> in the loop except for decisions that are genuinely an Operator's.
>
> Generalized from a protocol that emerged, unwritten, between two consuming projects sharing a
> storage host, and held through an operating-system upgrade and a mid-day change of plan.
> Fill the placeholders, delete this quote block, and repoint the canon links to your project's
> pinned Velocity reference.

## Why this exists

Peers sharing infrastructure fail in three ways: one acts without the other knowing (a reboot
under a running job), one reports a state it inferred rather than observed (the backup "should"
still cover the folder), and one asks the other to do what its own Operator refused (permission
laundering). A fourth failure appears across vendors: the exchange lives in a channel only one
side's tooling can read, so when the channel drops or the counterpart changes, the record is
gone. This template gives every exchange a type, required fields, a basis label, an id on each
side, and a home in the record.

## Contract

1. **The record is the transport; the channel is an accelerator.** An exchange counts when it
   exists in a durable record both parties can read, at an agreed location, independent of any
   one vendor's channel: a file at an agreed path, an issue or ticket in a shared tracker, or a
   row in a shared log. Live channels (session messages, chat, direct messages) speed delivery
   and never replace the record. A project names its peer record location in its overlay.
2. **Five message types, each with required fields** (below): *Notice*, *Gate*, *Read-back*,
   *All-clear*, *Ask-to-peer*. A *Handoff* between entities uses the Handoff Packet with a peer
   origin line.
3. **Every claim carries a basis label:** `observed` (seen by the sender, say where and when),
   `vendor-documented`, `inferred` (say from what), or `unchecked`. A read-back that carries no
   basis is not a read-back.
4. **Ids on both sides.** Each party cites its own id for the exchange (the desk id, work item id,
   or a peer-exchange id `PX-<n>`) and the counterpart's id when known, so either record can be
   followed from the other.
5. **Notice before, all-clear after.** No action on shared infrastructure without a Notice
   naming the window, the expected effect, and what the peer should not start; no resumption
   without an All-clear that says what was observed afterwards.
6. **A gate is observed, not assumed.** If a peer's action depends on a state (a snapshot exists,
   a backup scope covers a folder), the dependent peer names it as a Gate and the other reads it
   back with basis. "The upgrade does not touch stored config" is `inferred`; the gate waits for
   `observed` unless the dependent peer explicitly accepts the inference and says so in its record.
7. **Never launder permission.** A peer never performs an action that the other's Operator denied
   or that the other's own rules block, and never asks a peer to. Such an action goes back to the
   Operator who owns it, through that entity's Desk.
8. **Operator decisions travel by Desk, not by relay.** When a peer needs the other entity's
   Operator to decide, the ask is placed on that Operator's Desk with `origin: peer`, and the
   answer is read back to the peer. Operators are not transport layers.
9. **Any party may decline, and must leave a resumable state.** A decline says which step, why,
   the exact state left behind, and what a different party would need to continue. Plan, apply,
   and verify are separate phases with markers so that another party (or vendor) can resume.
10. **Vendor-neutral by construction.** Nothing load-bearing depends on one vendor's channel,
    tool, or memory. Files, ids, and basis labels are the contract; the rest is convenience.

## Policy, not implementation

The contract states what must be true of an exchange, not which tool carries it. Two projects on
an issue tracker may run the whole protocol as linked issues with the five types as labels and
the required fields as a description template; two projects on plain repositories may use the
file skeleton below; a mixed pair may use both, one record on each side, cross-referenced by id.
What is not negotiable: a durable record, a basis label on every fact, an id on each side, and no
laundering.

## Message types and required fields

**Notice** — *from, to, id, window (start, expected end, time zone), action, shared resource,
expected effect on the peer, what the peer must not start, all-clear promised (yes, and how),
file path.*

**Gate** — *from, to, id, the action waiting, the state required (named precisely), who can
observe it, deadline if any, what happens if the gate is not met by then.*

**Read-back** — *from, to, id, the gate or question answered, each fact with its basis label and
where/when observed, anything not verified and why, file path.*

**All-clear** — *from, to, id, what was done, what was observed afterwards (with basis), what
changed for the peer, what remains held and until what event, file path.*

**Ask-to-peer** — *from, to, id, the ask, why it is the peer's to answer, needed-by and what
waits, whether the peer's Operator must decide (then it goes on that Desk).*

## Skeleton (one record per exchange, here as a file; a tracker issue carries the same fields)

```md
# PX-<n> — <type>: <one-line subject>
- From: <entity / lead>   To: <entity / lead>   Sent: <date time tz>
- Ids: ours <id>; theirs <id or "none yet">
- Type: Notice | Gate | Read-back | All-clear | Ask-to-peer
<required fields for the type, one per line>
## Basis
- <fact>: observed <where, when> | vendor-documented <source> | inferred <from what> | unchecked
## State left behind (if declining or stopping)
- <phase, marker, exact state, what a resumer needs>
```

---
### Template rules (load-bearing — keep them true in every instance)
- **No record, no exchange.** A message that exists only in a channel has not happened yet.
- **No basis, no read-back.** Label every fact.
- **No action on shared ground without Notice; no resumption without All-clear.**
- **No laundering.** Denied by one Operator means denied; it does not become a peer's job.
- **Decline with a resumable state.** The next party may be a different vendor's agent.
