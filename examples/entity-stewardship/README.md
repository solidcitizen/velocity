# Entity Stewardship Worked Example

A synthetic illustration of the [Executive Check-in Board](../../templates/executive-checkin-board.md)
and the [Peer Exchange](../../templates/peer-exchange.md) applied to an entity that is not a
software product. Nothing here is drawn from a real household, company, account, or person;
the names, amounts, and dates are invented. It shows the shape, not measured results.

## The entity

A household-finance function: the steward (Operator) is the family's principal, the delivery
lead is an agent acting as the function's controller, and the entity shares a storage host with a
second entity, a home-operations function run by a different agent.

## The Board, at a check-in

```md
# Northwind Finance Check-in Board

_Last updated: 2026-04-03 08:10 ET · Decisions waiting: 1 · Actions only the Operator can take: 1 ·
Deadlines this week: 1 · In progress: 3 · Done this period: 6_

## Desk
<rendered by the Desk renderer from desk.json; one open decision (CK-9, raise the cash floor),
one open action (CK-10, sign in to the lender and save the statement)>

## Initiatives
### INI-1 — A ledger the family can trust  ·  sustain  ·  horizon ongoing  ·  active
- **Intent:** every account reconciles to the bank daily without a person in the loop; surprises
  reach the Operator the same morning.
- **Steward:** controller
- **Next milestone:** 2026-04-10, the weekly exception review runs from the queue, not from chat.
- **Risks it retires:** wrong balances driving decisions; a missed payment.
- **Measures:** accounts tying each day; open exceptions older than seven days.

### INI-2 — Liquidity and debt  ·  invest  ·  horizon 2026-Q4  ·  active
- **Intent:** the variable-rate line is paid down ahead of its repayment period, without breaching
  the cash floor the family agreed.
- **Steward:** controller
- **Next milestone:** 2026-04-15, second paydown sized against the year-end cash view.
- **Risks it retires:** rate exposure on the line; a floor breach in the holiday quarter.
- **Measures:** line balance month over month; lowest projected cash against the floor.

## In progress
| id | item | initiative | type | size | status | why / blocked by |
|---|---|---|---|---|---|---|
| WI-14 | weekly exception review pass | INI-1 | feature | M | doing | new payees stay unreviewed a year without it |
| WI-16 | migrate the desk to the canonical renderer | INI-1 | chore | S | this week | one shape across the Operator's desks |
| WI-12 | quarterly review package: spending vs income | INI-2 | control | M | blocked | CK-9 (floor) |

## Planned
### INI-1 — A ledger the family can trust
| id | item | type | size | why |
|---|---|---|---|---|
| WI-17 | payee-set writer for paper checks | feature | S | checks download without a payee |

## Done
- **WI-11** (2026-04-01, INI-2): lender statement parsed and tied — **Proof:** closeout disposition 2026-04-01, record loan-actuals/2026-03.json
- **WI-9** (2026-03-30, INI-1): daily control closes the file before batch writes — **Proof:** review pack RP-4; receipt 2026-03-30

## How to reply
`CK-9 yes` · `INI-2 hold` · `WI-17 this week` · `WI-12 drop`
```

Points to notice: the Desk is embedded, not copied, and no ask lives outside it; every item names
one initiative; a blocked item cites the Desk ask it waits on; Done entries cite their proof
artifact without restating it; a reply about an initiative's posture is an Operator decision and
would be raised and recorded on the Desk, then reflected here. In this revision the Desk section
is the Desk renderer's output and the four Board sections are hand-maintained from their
records; a Board renderer and schema follow once the Board has been practiced.

## A peer exchange, end to end

The home-operations function needs to upgrade the shared storage host during a window in which
the finance function had planned a file move. Records, one per message, in each side's peer
record location:

```md
# PX-7 — Notice: storage host upgrade today 13:00–15:00
- From: home-ops lead   To: finance lead   Sent: 2026-04-03 12:40 ET
- Ids: ours PX-7; theirs (none yet)
- Window: 13:00–15:00 ET, two reboots expected
- Action: operating-system upgrade on the shared host
- Effect on peer: shares and shell unavailable roughly 10–20 min per reboot
- Do not start: any host-side work until all-clear
- All-clear promised: yes, with a read-back of shares, snapshots, and backup scope
## Basis
- reboot count: vendor-documented (release notes)
```

```md
# PX-8 — Hold: finance move waits on an observed backup scope
- From: finance lead   To: home-ops lead   Sent: 2026-04-03 12:52 ET
- Ids: ours WI-15; theirs PX-7
- Action waiting: move of the history folder into the family share (planned 17:30)
- State required: the backup task's folder selection still includes the family share after the upgrade
- Who can observe it: the Operator, in the host's admin console
- If not met by 17:00: the move waits; nothing runs on inference
```

```md
# PX-9 — All-clear (partial): finance move released; relocation held
- From: home-ops lead   To: finance lead   Sent: 2026-04-03 16:55 ET
- Ids: ours PX-7; theirs WI-15
- Done: upgrade complete, host up 90 min
- Observed afterwards: shell up (observed 16:40); shares served (observed 16:41); snapshots
  intact, baseline of 11:52 present (observed 16:42); backup folder selection: inferred only,
  console session logged out by the upgrade, Operator asked to sign in
- Changed for peer: the move whose holds are all released on observed state may run; the relocation that depends on
  the backup selection stays held until the read-back
```

Points to notice: each message is a record with an id on each side; the hold names an observer;
the all-clear separates observed from inferred and scopes the release to what was observed; the
dependent lead does not act on the inference; the Operator's sign-in is an Operator action, so
the home-operations lead files it on that Operator's Desk as an ordinary ask citing PX-8, and the
finance desk carries a pointer entry to it, not a favor between leads.

## The same shapes for other entities

- **A product company:** initiatives are the roadmap themes; work items are the tracker's issues
  with a required theme field; Done is the closed-issue view with proof; peers are the platform
  teams the product depends on.
- **A person:** initiatives are the year's commitments (health, craft, money); work items are the
  week's tasks; the Desk holds the decisions only the person can make; peers are the people and
  services whose calendars or systems the plan depends on.
- **An AI agent acting for any of the above:** the same Board is the agent's operating page, the
  Operator is the human it acts for, and the Peer Exchange is how it coordinates with other
  agents, from any vendor, without either agent's channel or memory being load-bearing.
