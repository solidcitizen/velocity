# Decision-Scope Walkthrough

Synthetic, public examples for the proposed [decision scopes](../../docs/DECISION-SCOPES.md)
and [work contract](../../docs/WORK-MANAGEMENT.md). These are documentary walkthroughs, not
executed management decisions, independent acceptance, or runtime authorization tests.
No private project records are needed to inspect them.

## Scenarios

| Case | Context and event | Expected disposition under the contract |
| --- | --- | --- |
| Small software project retains TODO | One owner sets purpose/priorities; existing maintainer capacity covers a bounded documentation fix. | One inherited context block and a `doing` item with completion conditions suffice. No business case, JSON conversion, separate portfolio tool, or new approval is required. Evidence closes only the fix. |
| Existing TODO has uncertain history | An imported checkbox says a migration was completed, without date or proof. | Preserve its wording and source; label completion historical/operator-reported and date unknown. Do not invent closure evidence or count it as a newly proven completion. |
| Capacity boundary crossed | A selected task now requires an unapproved external service commitment. | Existing safe preparation can continue. Block the commitment on the named authority decision; task priority is not spend approval. |
| Capital program reaches a gate | Design work is done; the next stage would commit funds and contractors. | Retain task proof, prepare the investment case/options for the declared owner, and record its ruling and next envelope. “Design done” alone does not start construction. |
| Delegated work within an envelope | An accepted discovery envelope permits interviews and analysis up to a declared limit. | Execute within that mandate without asking for each internal task. Revalidate at a limit/expiry/change trigger; separate protected actions still follow their authority rules. |
| Parent decision is put on hold | A portfolio owner pauses one initiative; another operational obligation remains authorized. | Link the new parent revision and hold/block affected next actions. Preserve their history. Continue the unrelated obligation; do not mark every task dropped. |
| Recurring function | The monthly assurance occurrence completes with evidence. | Record that occurrence and next due/result; leave the ongoing obligation active. A failed/missing occurrence is not healthy or complete by inference. |
| Desk routes an upstream ruling | A portfolio committee owns a gate decision in its system; a project Desk asks for it. | Close the ask with the canonical ruling pointer. Do not create a second editable approval or release dependencies beyond its scope. |
| Two AI tools use the same TODO | Both discover the same index and record revision; one changes an item. | Serialize editing or detect and reconcile the stale version. Reading Markdown is possible, but that alone does not prove actual two-tool continuation. No runtime claim from this walkthrough. |
| Tracker has only Open/Closed | A migration would otherwise lose held/dropped meanings and parent context. | Add mapped native fields/linked records and preserve identity/history before cutover. A matching item count or JSON export is insufficient proof. |
| Future strategic opportunity | The Maintainer wants goal-setting considered later at portfolio scope. | Capture a candidate with owner, purpose, unknowns, no execution envelope, and a next selection decision. No committed task, delivery date, or automatic start is inferred. |
| Agent proposes a new goal | An agent recommends broader scope after seeing promising evidence. | Record the proposal and route it to the declared goal owner. It cannot adopt its own mandate or weaken outcome evidence to declare success. |

## Velocity's own application

[ARTIFACTS.md](../../ARTIFACTS.md) declares the inherited context, scope, authority, Markdown
binding, and recovery procedure. [TODO.md](../../TODO.md) tracks the bounded implementation
and its proof obligations. [PORTFOLIO.md](../../PORTFOLIO.md) records the currently authorized
foundation separately from future strategic goal-setting. `VEL-PF-2` is a candidate with no
execution capacity, date, or corresponding committed task. The proposal branch's source files
are its current view; the earlier local HTML snapshot is not an adopted source for this queue.

[INITIATIVES.md](../../INITIATIVES.md) now carries `VEL-INI-1`'s outcome brief, plan, assessment,
risks and review trigger. Portfolio selection and work execution remain in their respective
sources. The artifact index maps all three levels to the existing proposal/PR decision route.

These records exercise discovery and representation in a real repository. They do not prove
portfolio decision quality, business benefit, stage-gate enforcement, or a cross-vendor runtime.

## Architecture and proof review

Reviewed on 2026-09-21 as named Architect and Tester responsibilities within this implementation
session; Maintainer acceptance remains separate. Each of the twelve cases above was checked
against the proposed contract and its record shapes. No separate reviewer, management pilot,
or permission-enforcement test is implied.

Architecture findings and disposition:

- The four decision scopes are an additional context axis. Existing L0–L5, lanes, modes,
  control planes, and protected acceptance authority retain their meanings.
- Markdown and JSON bind the same work semantics, but their enforcement differs. The manual
  procedure now explicitly records request identity, actor, revisions, retry reconciliation,
  and writer coordination; the JSON helper is not represented as protecting direct edits.
- TODO remains authoritative without conversion. A selected migration preserves context and
  history; native state labels alone cannot collapse investment, stage, and work decisions.
- Desk/upstream references retain one ruling. Parent changes require an impact review;
  routine delegated work can continue without new per-task approvals.
- Optional profile adoption carries the new requirements. No previously conformant closeout
  is re-judged, and the separately owned Entity Development Lifecycle proposal is not accepted.
- Velocity's future goal-setting entry is at portfolio scope with no execution envelope or
  committed task. Its next gate is selection of bounded discovery, not an automatic start.

Local verification:

- `python3 -m unittest discover -s tests -v`: **17 passed** on 2026-09-21. This includes the
  copied artifact-index startup and existing JSON update/recovery/export behavior. The
  decision additions change documentation and record shapes, not the helper/renderer code.
- Local Markdown link/anchor check over changed and new documents: passed. This checks
  source navigation, not the truth of a linked ruling or the quality of a management decision.
- `git diff --check`: passed. Public-source review found no copied private operational data
  or local user paths in the additions. Primary-source attribution is retained in the contract.

The completion claim is local preparation for review. The current implementation does not
prove the live or management outcomes listed below.

Remaining qualifications: live AI-tool continuation, actual role denial at a project boundary,
an external tracker migration, and measured decision acceleration. Automatic Markdown
rendering is not implemented; the existing JSON support keeps its separately documented
[qualification scope](../portable-records/QUALIFICATION.md).

## Reference-method review

The standing-method follow-up is a documentary Architect/Tester review on 2026-09-21, not an
executed committee, operational Desk migration, or independent acceptance. It uses the
[reference method](../../docs/MANAGEMENT-REFERENCE.md) and the scoped Velocity records.

| Case | Reviewed disposition |
| --- | --- |
| One owner and lead across all three levels | One shared decision surface can route work, initiative and portfolio asks. Three readable management views may be sections of existing files; no three-Desk requirement. |
| Same operator, distinct project leads | Existing desks keep their own writers and identities. Cross-desk references follow ownership/pointer rules; shared readership does not grant shared write authority. |
| Initiative sponsor and portfolio authority differ | Local scope/stage choices remain within delegation; resource/priority exceptions reach the portfolio authority. Store one owning ruling per question. |
| One action requires scope and funding approval | Preserve two linked decisions for the genuinely separate authorizations. Answering one does not release the action while the other remains unmet. |
| Confidential portfolio material and public work queue | Keep the ruling at its authorized source; provide an access-appropriate reference or summary. A consolidated view does not expose restricted details or silently grant access. |
| Work done, benefit unmeasured | TODO closure remains valid for its bounded work. Initiative outcome and portfolio value remain unverified until their own evidence is available. |
| Agent performs work or proposes a decision | Execution identity is separate from the accountable human role. Its tools or assignment do not expand decision rights. |
| Future goal-setting candidate | `VEL-PF-2` stays outside initiative execution. PMI AI coverage remains an explicit research consideration; no claim that PMI lacks the proposed capability. |

Source review: current official PMI publication overviews for project, program, portfolio,
governance and AI; PMI's human–agent RACI guidance. Full standards were not inspected. The
references support the stated comparison, not a certification/compliance claim or the claim
that PMI prescribes Velocity's filenames, review cadence, or Desk layout.

The follow-up changes only Markdown contracts, templates and trial records. Local links/anchors,
whitespace, artifact coverage and public-source hygiene were checked successfully before closing
`VEL-WI-6`. The coverage pass confirmed that work state/proof stays in TODO, initiative
outcome/plan/assessment has its own record, and portfolio selection/capacity remains separate;
the same proposal/PR decision route serves this scoped trial. The eight cases above were
reviewed against the contract, including separate authorizations and ownership boundaries.
These are Class D documentary checks. The prior 17 runtime test results remain scoped to the
unchanged JSON implementation and were not rerun for this documentation-only follow-up;
they do not prove this new management method or a new UI capability.
