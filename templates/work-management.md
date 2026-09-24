# Lightweight Work Management

Experimental contract for the opt-in [Portable Project Records](portable-project-records.md)
profile. The contract defines work meaning; a binding defines how it is stored and updated.
`TODO.md` can carry the complete lightweight work-management responsibility indefinitely.
It is not merely an inbox to be emptied into another system.

## Small common record

Each work item has stable identity within a project, a title, a responsible work owner, and an
explicit state. Preserve its source, history, and any uncertainty. The project declares its
[decision context](decision-levels.md) once; items inherit it or link their more specific parent,
outcome, and authority. Known ownership can be a named role. Imported unknown ownership is
marked unconfirmed and must be resolved before making a delivery commitment. For AI-executed
work, the inherited role map also identifies the accountable human owner and escalation path;
an agent assignment does not itself confer accountability or approval authority. See the
[reference method](../examples/management-reference/README.md) for coverage at the other management levels.

Use the existing issue, plan, tranche, or a short inline statement to bound the work and say
what done means. Link dependencies and the decision that governs any protected action. Keep
priority or queue order explicit enough to choose the next work; the coordinator/declared
owner sets it within the governing direction. Optional size and benefit estimates aid judgment;
they do not allocate capacity or constitute a business case.

## State meanings and changes

| State | Meaning and evidence needed |
| --- | --- |
| `backlog` | Wanted, not committed. Record unknowns; order expresses preference, not authorization. |
| `committed` | Selected within the applicable authority/capacity, with an owner and a named date or week. Scope and completion conditions are clear. |
| `doing` | Actively executing bounded, authorized work. Name its scope/completion conditions; a separate committed step is unnecessary for work starting now. |
| `blocked` | Cannot proceed because of a named decision, dependency, or missing authority. Link the ask/item/authority gap and the owner of the next action. |
| `held` | Waiting for a named external event or party. Record the review/date trigger when known; an unknown date stays visibly unknown. |
| `done` | The defined work is complete, with appropriate evidence, closure date, and any required acceptance. This does not claim release, realized benefit, or parent-gate approval. |
| `dropped` | Intentionally closed without doing the work, with reason, deciding authority, and closure date. Preserve identity and history. |

The seven meanings are shared. A binding may use other labels or combine native states only
if durable fields or linked records preserve these distinctions.

- Intake enters backlog unless existing authority supports an immediate commitment/start.
  Read the current context before starting or resuming; an unresolved authorization dependency
  keeps the affected action blocked even if other work can proceed.
- Moving to blocked/held names the wait. Answering one ask or resolving one dependency does
  not automatically resume work: check the remaining dependencies, authority, and capacity.
- A scope, priority, owner, commitment, or state change records its reason and actor. Moving
  committed work back to backlog records the decommitment; moving it to doing retains useful
  commitment history. The file name or checkbox alone is not state management.
- Closing work retains its identity. Reopening records why and preserves the prior proof and
  close date in history. Materially different follow-on scope gets a new linked ID.
- Imported checked items without proof remain explicitly historical/operator-reported. They
  are not evidence-qualified completions. Preserve unknown dates instead of inventing them.

Completion evidence scales with the claim. A short verified result can close a small document
edit; an operator-facing behavior claim needs the applicable scenario proof. A citation's
presence does not establish its adequacy. Existing [proof rules](../docs/PROOF-MODEL.md) still govern.

## File and external bindings

| Binding | Authoritative work source | Update and presentation |
| --- | --- | --- |
| Markdown file | `TODO.md` or an existing named Markdown queue | Use the [work-tracker template](work-tracker.md) or equivalent fields. A serialized editor, version history, and review/read-back maintain the contract. The Markdown itself is a usable view. |
| Structured file | A project-owned Work Board JSON source | The [Work Board pilot](work-board.md) supplies a schema and shared renderer; the [file helper](project-records.md) coordinates local cooperating writers. |
| External tracker | The declared system/project and mapped records | The [tracker binding](tracker-binding-and-handoff.md) preserves meaning, identity, authority, and recovery through qualified native fields or linked records. |

Choose one authoritative work source per declared scope. Different scopes can have different
owners/systems; record their boundaries and cross-references rather than duplicating the same
queue. A chart, HTML board, AI artifact panel, export, or cache is a derived view of that source.
A richer view does not require retiring a sound `TODO.md`.

The supplied JSON helper/renderer **does not parse or write Markdown**. This tranche defines
the Markdown contract and a manual versioned workflow; it does not supply a TODO-to-HTML adapter
or claim automated concurrency protection for direct editors. Adopted renderers keep their
shared content rules. A future Markdown adapter must map these semantics and qualify its
read/write/view behavior before it is claimed as supported automation.

Import is one adoption path, not the definition of TODO. An existing TODO may be clarified
in place, retaining wording and history. Convert it only when the project chooses another
binding, reconcile every item, and retire the old writable queue after authorized cutover.
Do not retire an ongoing queue just because its present tasks are done.

## Operations, initiatives, and decisions

Recurring obligations can live in a separately declared operations register or in a binding's
control records. Each identifies owner, cadence/trigger, evidence for individual occurrences,
last result, next due/review, and active/planned/suspended/retired disposition as applicable.
Completing an occurrence does not complete the obligation. Suspension/retirement needs its
own authority and history. Bindings must disclose unsupported dispositions and preserve them
in a linked record; do not imply the current JSON pilot implements every operations lifecycle.

An initiative's stage, investment posture, and business rationale belong in their authoritative
management records. `TODO.md` links to them; it does not need to implement portfolio selection,
resource allocation, financial accounting, or benefit realization. Similarly, the Check-in
Desk routes human decisions/actions and preserves or references rulings. It is not a second
backlog. Track the exact dependency between a decision and the work it permits.

## Escalating the tracking tool

Concurrent teams, reporting needs, dependencies, integrations, or evidence retention can justify
a dedicated tracker. The user chooses when and which one. Adopt its binding and rehearse the
handoff; preserve IDs/crosswalks, state meanings, decision context, history, uncertainty, and
evidence access. Backup source and destination as appropriate. File mode is a valid long-term
choice, and adopting a larger tracker does not by itself create a portfolio-governance process.
