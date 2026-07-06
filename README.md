# Velocity

Velocity is a reusable software delivery lifecycle for AI-assisted engineering.

It is intentionally project-independent. Product repositories consume Velocity through a project overlay; they do not own the general lifecycle rules.

## Purpose

Velocity exists to make agent-assisted delivery repeatable across projects while preserving human authority over goals, risk, and process evolution.

Core goals:

- manage SDLC best practices independent of any one product repo
- separate delivery authority from lifecycle-rule authority
- let specialist roles share context without allowing them to rewrite the criteria that judge their work
- make proof expectations explicit and portable across local, staging, host-qualified, and production lanes
- provide templates that projects can adopt with project-specific overlays

## Authority

The core invariant is:

> Shared context, separated write authority.

Delivery roles may read Velocity rules and propose changes. They may not directly modify Velocity governance during ordinary product delivery.

Lifecycle-rule changes are owned by the Velocity maintainer role and require explicit process-change disposition.

## Documents

- [Lifecycle Model](docs/LIFECYCLE-MODEL.md)
- [Role Authority](docs/ROLE-AUTHORITY.md)
- [Artifact Authority Boundaries](docs/ARTIFACT-AUTHORITY-BOUNDARIES.md)
- [Control Planes](docs/CONTROL-PLANES.md)
- [Proof Model](docs/PROOF-MODEL.md)
- [Branch Hygiene](docs/BRANCH-HYGIENE.md)
- [Project Adoption Guide](docs/PROJECT-ADOPTION-GUIDE.md)
- [Governance](governance/GOVERNANCE.md)

## Direction & Positioning

Not lifecycle policy, and not part of the governed `docs/` set:

- [Manifesto](MANIFESTO.md) — direction, not policy: where Velocity should evolve next.
- [Lineage and Adjacent Work](LINEAGE-AND-ADJACENT-WORK.md) — positioning, not policy: where Velocity sits relative to agent frameworks and prior art.

## Adoption Pattern

Each product repo should keep only:

- a short local `AGENTS.md` reference to Velocity
- project-specific lane, command, environment, and risk details
- project-specific issue logs, packets, missions, and review packs

Reusable lifecycle policy belongs here.

## Adoption in Practice

Velocity is validated by use beyond the repo it was born in:

- **Nexusplus** — the originating project (multi-tenant contact intelligence); the invariant-binding doctrine (`proposals/2026-06-27`) was piloted here before it was canonized.
- **smart** — a personal / home-operations framework (home automation as its first domain), and the first non-product-software adopter. Working the method in a new domain independently re-derived Velocity's core disciplines — adversarial verification, pin-to-reviewed-artifact, "a prose invariant is not a force," criticality-is-not-mutation-authority — evidence that the principles are discoverable and transfer beyond software delivery. It contributed the role-brief template (`proposals/2026-07-05`).

