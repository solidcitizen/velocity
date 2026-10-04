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
- Proposed version: planned v1.10.0 (minor)

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

- **The organization's goals** belong to its accountable humans. Agents gather evidence, draft
  registers, propose goals and alternatives, and tag decision levels. They never adopt, set,
  score, rank, or rewrite a goal or its success criteria.
- **The goal-setting method under trial** belongs to the organization's chief executive.
- **What Velocity absorbs** belongs to the Velocity Maintainer, decided at the review gate through
  the proposal path. The CPO session drafts proposals; reviewers propose; the maintainer decides.
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
   decision (issue #19)?

## Exclusions

- No new mass under `docs/`, and no new role.
- No goal-setting method enters the canon before the review gate, whatever the interim results.
- No agent sets, scores, ranks, or rewrites a goal or its criteria at any point in the trial.
- No new Check-in Desk sections, filters, or synchronization.
- No acceleration or benefit claim without measured evidence.
- No organization-identifying information in this repository.

## Capacity and time

- Discovery runs from the organization's plan ratification in mid-October 2026 to the review
  gate. The gate is no earlier than December 2026, after at least one full cycle of operating
  reviews.
- Velocity capacity: the CPO session's drafting and review time. There is no other budget,
  staffing, or delivery date.

## Evidence contract

Before the first operating review, the organization pre-declares the following, using the
[measured pilot](../templates/automation-pilot.md) template:

- **Baseline:** how goals were set before the cascade, including how many planning schemes were
  running and whether they were reconciled.
- **Measures, at minimum:** time from vision to an approved plan; the share of initiatives with a
  named accountable owner; the share of key results with a baseline, target, and evidence source;
  the number of decisions re-opened without new evidence; goal rework; and active human effort on
  planning.
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

Inputs to the decision are the evidence summary, an outside methodology review, and the
manifesto's five admission tests.

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
