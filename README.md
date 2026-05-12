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

## Adoption Pattern

Each product repo should keep only:

- a short local `AGENTS.md` reference to Velocity
- project-specific lane, command, environment, and risk details
- project-specific issue logs, packets, missions, and review packs

Reusable lifecycle policy belongs here.

