# Strategic Goal-Setting: Discovery Charter (VEL-PF-2)

- Status: Proposed
- Date: 2026-10-04
- Authority owner: Mike, Velocity Maintainer
- Mode: Process evolution
- Source: The maintainer selected strategic goal-setting for bounded discovery on 2026-10-04,
  with a consuming organization's planning practice as the system it is proven on. Issue #20 asked
  for that selection and its contract to be recorded here, so the pilot and the canon read the
  same. The opportunity was captured as `VEL-PF-2` on 2026-09-21 with no execution commitment,
  and its entry names what a charter must state: decision rights, exclusions, capacity and time
  limits, research questions, proof, and a review gate.
- Disposition: Velocity repo proposal; pending the maintainer's approval.
- Proposed version: planned v1.11.0 (minor)

## Why

The maintainer's framing, 2026-10-04: most AI delivery practice optimizes delivery to a goal
someone has already stated. Velocity's direction goes a step further and improves how goals are
set in the first place. It starts from a vision, a high-level understanding of the environment,
and hypotheses that must be tested, then learns continuously to deliver the vision's value. Most
businesses today work as a mix of disciplines, people, and agents, and the method has to hold
across all of them.

That is direction, not a capability Velocity has today. Velocity currently governs delivery
toward accepted goals and keeps authority over goals with a human. This charter is how the
broader claim gets earned: on a real system, with evidence, before anything enters the canon
(manifesto, "What earns a place in the core", test 3).

## The system under study

A consuming organization runs a planning cascade with seven rungs: charter and destination,
annual business plan, quarterly company objectives, functional commitments, initiatives, weekly
execution, and operating reviews. Its key results are recorded on the initiative record's
benefit-review fields (measure, baseline, target, evidence, owner), with no new field. The
organization's own records stay with the organization. This repository receives only what the
evidence contract below asks for, with nothing that identifies the organization.

The maintainer holds two seats here: the organization's plan is his, and so is Velocity's
acceptance. Velocity's solo-operator rule applies: separate the moment of doing from the moment
of accepting. The trial runs in the organization. Nothing it produces enters Velocity except
through the review gate, after the evidence period, by the normal proposal path.

## Decision rights

- **The organization's goals.** Each goal names one accountable human; a group owns nothing.
  Agents gather evidence, draft registers, propose goals and alternatives, and tag decision
  levels. They may propose a ranking when it is labeled as proposed. They never adopt, set, or
  score a goal, never rewrite a goal or its success criteria, and never change the criteria a
  proposal is ranked by.
- **The goal-setting method under trial** belongs to the organization's chief executive.
- **What Velocity absorbs** belongs to the Velocity Maintainer, decided at the review gate through
  the proposal path. The CPO session drafts proposals; reviewers propose; the maintainer decides.
- **Every ruling names its hat.** The maintainer rules here both as the organization's chief
  executive and as Velocity's maintainer, sometimes on the same day. Each ruling in the trial says
  which hat it was made under. A session that sequences work across hats does not weigh one hat's
  decided agenda against another hat's priorities.
- None of these transfers write authority over goals, criteria, or rules to an agent (manifesto,
  "One Core, Two Lifecycles"; [decision levels](../templates/decision-levels.md#ai-participation-and-future-goal-setting)).

## Research questions

1. How does the cascade map onto Velocity's four decision levels (strategy, portfolio,
   initiative, work)? Two artifacts with different cadences may share one level; do not invent a
   level to fill a hierarchy.
2. What does the strategy level need to hold so that "what are we trying to do" has an answer on
   day one: destination, objective, owner, and evidence source?
3. How are values and competing objectives drawn out, and alternatives compared under
   uncertainty, without an agent choosing among them?
4. Who may adopt, change, or retire a goal, and how is a challenge to a goal raised and decided
   without anyone rewriting their own criteria?
5. What counts as outcome evidence, as distinct from delivered output? A milestone met is not a
   key result achieved.
6. What does an initiative record carry when naming its accountable owner is itself an open
   decision (issue #19)? The `Blocked:` owner form is already in use, and one blocked owner has
   cleared. Observe whether the rest clear, and how long they take.
7. **Who classifies?** The party closest to the work may classify first: a decision's level, how
   much freedom a piece of work gets, or the measure a function is judged by. Test that every
   classification is recorded with the classifier's name and can be reviewed by a party it does
   not benefit, and that a classification widening the classifier's own autonomy takes effect only
   after that review. Component measures derive from the organization's goals, never the reverse.
8. **Does declaring the situation help?** Where the organization chooses to, each initiative
   declares its situation: settled (apply the accepted procedure), analyzable (find the answer by
   expert analysis), emergent (run small, safe-to-fail probes and amplify what works), unstable
   (stabilize within existing authority), or unclassified (decompose until it can be classified).
   The declaration sets how much experimentation is allowed. It is made at initiative level only,
   by the organization's chief executive, and is optional for each initiative. Test whether it
   changes any posture, and how often situations are misclassified.
9. **What earns more authority?** Test that only observed behavior counts as evidence for giving
   any party more authority: a denied action declined, or a self-correction placed on the record.
   What a party says about its own intent, deference, or confidence counts for nothing toward more
   authority. A reviewer may still read a party's stated reasoning as information.
10. **What can we afford?** How does a capacity envelope (people, money, runway, and AI usage)
    attach to each level, and how is a goal's affordability tested before the goal is adopted?
11. **What are we not doing?** How are explicit holds, declined candidates, and the order in which
    things get cut held as goal artifacts, each with an owner?
12. **What forces closure?** What ageing rule and closing cadence apply to an open goal decision,
    and who owns the silence while it sits?
13. **Who must be told?** What communication obligation comes with adopting, changing, or retiring
    a goal, and who owns it?

Questions 7 to 9 come from a proposal the maintainer requested from a separate research thread.
They enter the trial as questions, not rules. Question 8 draws on Dave Snowden's Cynefin framework
(Snowden and Boone, *Harvard Business Review*, 2007); Velocity uses its own names for the
situations and implements none of Cynefin's methods. Questions 10 to 13 come from the outside
methodology review of this charter.

## Exclusions

- No new mass under `docs/`, and no new role.
- No goal-setting method enters the canon before the review gate, whatever the interim results.
- No agent adopts, sets, scores, or rewrites a goal or its criteria at any point in the trial. A
  ranking may be proposed only when it is labeled as proposed.
- No new Check-in Desk sections, filters, or synchronization.
- No acceleration or benefit claim without measured evidence.
- No organization-identifying information in this repository.

## Capacity and time

- Discovery runs from the day the organization ratifies its plan to the review gate. The gate is
  the first monthly operating review after ratification has been followed by at least one full
  month of weekly reviews and one monthly operating review. It is never earlier than December
  2026. The date follows from that rule, so if ratification comes late, the gate moves with it.
- Velocity capacity: the CPO session's drafting and review time. There is no other budget,
  staffing, or delivery date.

## Evidence contract

Before the first operating review, the organization pre-declares the following, using the
[measured pilot](../templates/automation-pilot.md) template:

- **Baseline:** how goals were set before the cascade, including how many planning schemes were
  running and whether they were reconciled.
- **Measures, at minimum:** time from vision to an approved plan; the share of initiatives with a
  named accountable owner; the share of key results with a baseline, target, and evidence source;
  the number of decisions re-opened without new evidence; goal rework; work items that carry no
  initiative; and time from an ask to its ruling on the operator's desk. Active human effort on
  planning is measured once it is defined. Until then the organization reports agent effort from
  its spend logs, labeled as a proxy.
- **What is not measured yet:** realized benefit. It is reported only when its evidence source
  produces it.
- **Reporting:** a summary to the maintainer at each operating review, through the private
  channel the maintainer designates. At the gate, an anonymized evidence summary is added to this
  record.

## Review gate

At the gate, the maintainer decides one of four outcomes:

- **Promote:** specific template changes, each through its own proposal.
- **Revise and continue:** a further bounded cycle.
- **Retain as an overlay:** the practice stays in the organization and the canon is unchanged.
- **Decline.**

Inputs to the decision are the evidence summary, the first evidence from the organization's own
records pilot (its desk and board, which start after ratification), an outside methodology
review, and the manifesto's five admission tests.

The gate also takes up a deeper question raised in drafting: whether authority over a goal rests
on who bears the consequences if the goal is wrong, together with having no conflict of interest,
rather than on whether the party is a person or an agent. If so, the prohibition on agents holding
goal authority has a stated ground, and any future path to shared goal authority would run through
coupling an agent's consequences to the organization's. The test would also need accountability
for the outcome joined to exposure to it, since exposure alone would give standing to anyone whose
livelihood depends on the goal. The standard cannot express that today.
Until the gate decides, the rule stands: people own goals.

Stop conditions: the organization stops running the cascade; an agent is found setting or
rewriting a goal; or the evidence cannot be summarized without identifying the organization.

## Changes in this proposal

- This charter record.
- `MANIFESTO.md`: the sentence placing strategic goal-setting beyond the emerging scope records
  the selection and links this charter.
- `templates/decision-levels.md`: the strategy row and the AI-participation section point to this
  charter instead of describing goal-setting as uncommitted future work.

No lifecycle rule, role, approval boundary, proof obligation, or schema changes.

## Proof and Disposition

To be completed at acceptance: links checked, `git diff --check` clean, and no organization
named anywhere in the repository.

Branch disposition: `proposal/goal-setting-charter`, via pull request.
