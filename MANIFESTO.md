# Velocity Manifesto

This document is direction, not policy.

It records where Velocity should evolve and why. It is not a lifecycle rule, not a protected lifecycle artifact in the sense governed under `docs/` and `governance/`, and not yet tested practice. Velocity policy holds the line today. This manifesto says where the line should move next.

Positioning reviewed 2026-09-09. Earlier exclusivity language reflected the gap Velocity set
out to address; it is preserved in Git history, not asserted as a verified first-ever claim.
See [development history and adjacent methods](LINEAGE-AND-ADJACENT-WORK.md).

## Thesis

Velocity v1 is governance for AI-assisted delivery.

Velocity v2 is governance for *partially autonomous* AI-assisted delivery.

v1 establishes the substrate: lanes, proof classes, authority boundaries, role separation, lifecycle modes, control planes. It defends against the dominant failure of fluent agents collapsing seven roles into one unreviewed turn.

v2 keeps those boundaries and aims to reduce the human work needed to move between them.
The point is to let an agent proceed when accepted proof and explicit authority allow it,
and to seek a human decision when they do not. Existing policy already permits explicit
delegation; how much time it saves must be measured. The v1/v2 framing here describes a
direction, not a released semantic version or an authorization to bypass current policy.

## Frontier Velocity Is Built To Address

The wider AI-coding conversation is currently most active and least settled around questions Velocity already has substrate for:

- When is the agent allowed to ship something without a human?
- How much proof is required for which kind of claim?
- Who is allowed to mutate the criteria the agent is being evaluated against?
- What does observability and forensics look like when the developer was an agent?
- How do multiple humans operating their own controllers coordinate over shared protected artifacts?

Published playbooks and methods now address several of these questions directly. The
[dated comparison](LINEAGE-AND-ADJACENT-WORK.md#comparison-reviewed-2026-09-09) identifies
both related work predating this repository and current convergence. Velocity should learn
from their executable workflows while making compatibility with its authority and proof rules
explicit.

Velocity's substrate — lanes, proof classes, protected artifacts, authority boundaries, control planes — is unusually well-shaped to give principled answers. The evolution work is deploying that substrate against the frontier questions, not inventing new substrate.

## The Unlock: Delegation Grades

The single highest-leverage move in v2 is making the degree of autonomy an explicit, declared property of work.

Today Velocity says, in effect, that the human gates promotion and other protected actions. Tomorrow it should say which actions, under which proof, in which lane, with which protected-artifact scope, may proceed without explicit human acceptance — and what the recovery path is when that judgment turns out wrong.

A sketch of the levels:

**Unadopted design sketch.** These grades are not current defaults. In particular, Grade 1's
timeout-based acceptance is unresolved and is not enabled by the v1.4 templates. A version bump,
an unattended run, or a missing human response grants no new authority.

- *Grade 0 — Strict human gate.* Every closeout requires explicit human acceptance. Default for architecture-decision and promotion lanes, and for any tranche that touches protected artifacts.
- *Grade 1 — Human review, default-accept.* Closeout is proposed; human may reject within a declared window; otherwise auto-closes. Default for staging-lane work that does not touch protected artifacts.
- *Grade 2 — Proof-gated auto-close.* Auto-closes if the specified proof class passes and protected-artifact scope is unchanged. Default for local-implementation work on non-protected files.
- *Grade 3 — Continuous auto-close.* Routine tranches — lints, formatting, dependency bumps, generated-doc updates — auto-close on proof. Default for repo-lane changes that touch no logic.

Each grade must declare: required proof class, allowed protected-artifact scope, escalation conditions, and recovery path if the auto-close was wrong (rollback at staging, PR-revert at repo, incident trigger at promotion).

Delegation grades are one candidate for making changes in autonomy deliberate and recoverable.
They should be adopted only where a measured pilot shows that their proof and recovery contracts
work without weakening protected authority.

## Near-Term Work: Measured Automation

Velocity v1.4.0 supplies optional [evaluation](templates/agent-evaluation-pack.md),
[transition](templates/automation-transition-contract.md), and
[pilot](templates/automation-pilot.md) templates within existing policy. Its next evidence gate
is a project pilot, not a claim of autonomous delivery already achieved.

- Evaluate changes to the development agent with protected fixtures, expected outcomes, and
  both successful and denied-action cases.
- Connect accepted artifacts to bounded next actions through qualified transition contracts.
- Measure delivery time, active human effort, waiting, rework, defects, and resource use.
- Feed observed failures into evaluated process improvements with the correct authority owner.

Keep the method portable. Put runtime adapters and collected results in consuming projects;
bring demonstrated reusable lessons back through process evolution.

## Direction: From Software Lifecycle To Entity Lifecycle

By the maintainer's own report (private consuming projects, not independently reproducible
evidence; see [lineage](LINEAGE-AND-ADJACENT-WORK.md#attribution-for-the-entity-lifecycle-additions)),
Velocity's substrate has been consumed by things that are not software products: an operations
function for an estate, a finance function for a household, and product companies, each with an
Operator, delivery roles, protected artifacts, and proof obligations. The rules held unchanged.
What drifted in those projects was not the substrate but the surfaces around it: the Operator had no single page of what was theirs to decide (closed by the Check-in Desk);
the delivery lead's plan lived where only the lead could read it, so allocation had no Operator
view; and peers sharing infrastructure coordinated by an unwritten protocol whose record was a
file at a known path when the live channel could not be trusted.

The direction this suggests: treat the thing governed as an **entity**. An entity may be a
product, a company, an operating function, a family, a person, or an AI agent acting for any of
them. Every entity has a steward (the Operator), a purpose, obligations, resources, risks, a
cadence, a record, and peers. Its lifecycle is charter, operate, develop, review, evolve, and
transfer; software delivery's stages are one instance of *develop*. "Entity" becomes an axis
the way product lifecycle is an axis. Nothing in the substrate changes: no new roles, no
vocabulary refactor, no new docs mass. What changes is where templates point: at a steward's
check-in rather than a developer's, at exchanges between entities rather than handoffs within
one, and at a record that any vendor's agent can read rather than a channel only one can.

Two consequences have been practiced in those private projects, by the same report, and are
proposed as templates: the Executive Check-in Board (the page around the Desk: initiatives, committed work, backlog, and a proof-backed
record of what closed) and the Peer Exchange (notice, hold, read-back, all-clear, ask-to-peer
between two entities' leads, with the record as the transport). Two further consequences are
direction only, pending practice: a collaborative framework has to say how an entity's
governance composes with its peers' without a shared Operator, and a vendor-neutral one has
to make files, ids, and basis labels the contract while treating any one vendor's channels,
tools, and memories as convenience.

The evidence gate is the same as for measured automation: practiced in consuming projects
across at least one monthly cycle, then judged on whether the Operator can run a check-in from
the page alone and whether peer exchanges leave a record another party can resume from.

## Secondary Directions

Listed in rough order of leverage. Each is a place where Velocity has unusually well-shaped ingredients to engage with an active frontier in the broader space.

*Proof-as-spec.* Explore treating scenario proof as a primary durable artifact from which
implementation tranches are derived. Preserve the operator's intent and its change authority;
a test suite can still be incomplete or wrong.

*Role-aware compute and tool allocation.* Codify the mapping of role → model class → thinking budget → tool scope. Velocity has the authority discipline; modern agent runtimes have the compute primitives; the two have not been formally joined.

*Context provenance as a tranche field.* Record what code the agent committed to reading before acting and surface that in closeout. Addresses the live failure mode where agents confidently extend code they never loaded.

*Lane taxonomy for agent-native runtimes.* Extend the lane vocabulary to name browser-session lane, sandbox lane, MCP-tool runtime lane, and agent-internal-memory lane. Attach authority and proof rules to each.

*Inter-controller protocol.* Define how independent controllers — typically one per human — negotiate over shared protected artifacts. Slot under MCP and A2A transport as those standards stabilize.

*Operations and forensics for agent-merged code.* Connect observed failures to the agent
configuration, accepted artifact, enforcing control, and recovery record. Adjacent playbooks
also address this; Velocity should contribute tested authority and proof mappings.

## Anti-Directions

The following moves look attractive and should be resisted.

- *More lifecycle docs.* The current doc mass is already at the edge of intelligibility. New mass costs adoption. Future additions belong in templates, examples, overlays, or this manifesto — not in `docs/`.
- *More roles.* Seven is at the limit of useful separation. Sub-roles belong in overlays.
- *Vocabulary refactors.* The current vocabulary is one of the framework's strengths. Churning it adds friction without unlocking capability.
- *Specific-framework reference implementations published as Velocity.* Coupling to CrewAI, LangGraph, or any single agent runtime trades the framework's portability for short-term adoption. Substrate-agnostic is the durable position.
- *Scaling claims without measurement.* The autonomy-multiplier argument is real but unproven. Public claims need empirical backing; private use does not.

## Operating Principle for Evolution

The reason to evolve Velocity rather than rest on v1 is that the world is moving fast toward more agent autonomy and away from human-in-every-loop.

v1 holds the line.

v2 holds the line *while letting the autonomy compound*.

Velocity's contribution is making proof, authority, and lane explicit for each consequential
action, then testing whether that discipline enables more useful autonomy with less human work.
Its value should be demonstrated in consuming projects as adjacent methods continue to evolve.

The framework should evolve in directions that deploy that substrate against frontier questions. It should not evolve in directions that grow the substrate for its own sake.
