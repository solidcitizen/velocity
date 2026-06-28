# Velocity Manifesto

This document is direction, not policy.

It records where Velocity should evolve and why. It is not a lifecycle rule, not a protected lifecycle artifact in the sense governed under `docs/` and `governance/`, and not yet tested practice. Velocity policy holds the line today. This manifesto says where the line should move next.

## Thesis

Velocity v1 is governance for AI-assisted delivery.

Velocity v2 is governance for *partially autonomous* AI-assisted delivery.

v1 establishes the substrate: lanes, proof classes, authority boundaries, role separation, lifecycle modes, control planes. It defends against the dominant failure of fluent agents collapsing seven roles into one unreviewed turn.

v2 keeps the line and lets autonomy compound on top of it. The point is to let the agent ship without the human when the proof and authority discipline say it is safe, and to hold the human firmly in the loop when they do not. v1 alone prevents the multiplicative gain AI-assisted teams claim, because every protected boundary requires human attention. v2 turns "human-gated" from the default into one option among several, each with its own proof requirement and recovery path.

## Frontier Velocity Is Built To Address

The wider AI-coding conversation is currently most active and least settled around questions Velocity already has substrate for:

- When is the agent allowed to ship something without a human?
- How much proof is required for which kind of claim?
- Who is allowed to mutate the criteria the agent is being evaluated against?
- What does observability and forensics look like when the developer was an agent?
- How do multiple humans operating their own controllers coordinate over shared protected artifacts?

Most existing frameworks answer the first by guessing — classical CI/CD over-gates everything, autonomous-agent products under-gate everything. Most answer the rest by deferring to whoever shows up first in the conversation.

Velocity's substrate — lanes, proof classes, protected artifacts, authority boundaries, control planes — is unusually well-shaped to give principled answers. The evolution work is deploying that substrate against the frontier questions, not inventing new substrate.

## The Unlock: Delegation Grades

The single highest-leverage move in v2 is making the degree of autonomy an explicit, declared property of work.

Today Velocity says, in effect, that the human gates promotion and other protected actions. Tomorrow it should say which actions, under which proof, in which lane, with which protected-artifact scope, may proceed without explicit human acceptance — and what the recovery path is when that judgment turns out wrong.

A sketch of the levels:

- *Grade 0 — Strict human gate.* Every closeout requires explicit human acceptance. Default for architecture-decision and promotion lanes, and for any tranche that touches protected artifacts.
- *Grade 1 — Human review, default-accept.* Closeout is proposed; human may reject within a declared window; otherwise auto-closes. Default for staging-lane work that does not touch protected artifacts.
- *Grade 2 — Proof-gated auto-close.* Auto-closes if the specified proof class passes and protected-artifact scope is unchanged. Default for local-implementation work on non-protected files.
- *Grade 3 — Continuous auto-close.* Routine tranches — lints, formatting, dependency bumps, generated-doc updates — auto-close on proof. Default for repo-lane changes that touch no logic.

Each grade must declare: required proof class, allowed protected-artifact scope, escalation conditions, and recovery path if the auto-close was wrong (rollback at staging, PR-revert at repo, incident trigger at promotion).

Delegation grades convert Velocity from a methodology that *holds the line* into a methodology that *moves the line deliberately and recoverably*. That is the difference between governance that constrains AI-assisted teams and governance that scales them.

## Secondary Directions

Listed in rough order of leverage. Each is a place where Velocity has unusually well-shaped ingredients to engage with an active frontier in the broader space.

*Proof-as-spec.* Commit to the scenario proof as the primary durable artifact and the implementation as derivative. Velocity is already closer to this than most frameworks because of V-model fidelity in the proof model. The intellectual leap is treating tranches as derivable from proof requirements rather than the reverse.

*Role-aware compute and tool allocation.* Codify the mapping of role → model class → thinking budget → tool scope. Velocity has the authority discipline; modern agent runtimes have the compute primitives; the two have not been formally joined.

*Context provenance as a tranche field.* Record what code the agent committed to reading before acting and surface that in closeout. Addresses the live failure mode where agents confidently extend code they never loaded.

*Lane taxonomy for agent-native runtimes.* Extend the lane vocabulary to name browser-session lane, sandbox lane, MCP-tool runtime lane, and agent-internal-memory lane. Attach authority and proof rules to each.

*Inter-controller protocol.* Define how independent controllers — typically one per human — negotiate over shared protected artifacts. Slot under MCP and A2A transport as those standards stabilize.

*Operations and forensics for agent-merged code.* Extend the Operations lifecycle stage with observability and incident discipline specifically for changes whose author was an agent. Nobody else is doing rigorous methodology here.

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

That is the actual unlock — and it is the unlock Velocity is uniquely positioned to ship, because it is the only governance framework in the AI-assisted-delivery space whose substrate naturally expresses what proof, what authority, and what lane apply to a given action.

The framework should evolve in directions that deploy that substrate against frontier questions. It should not evolve in directions that grow the substrate for its own sake.
