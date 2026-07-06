# Project Adoption Guide

Velocity is adopted through a thin project overlay.

## What Stays In Velocity

- reusable role definitions
- lifecycle state model
- proof taxonomy
- artifact authority boundaries
- branch hygiene requirements
- process evolution governance
- templates for packets, tranches, closeout, review packs, and role briefs

## What Stays In The Project Repo

- project architecture
- product issue logs
- project-specific lane map
- environment names and commands
- deployment and promotion runbooks
- project-specific risks and invariants
- current mission, packet, and review-pack artifacts
- product-specific acceptance scenarios

## Recommended Project Files

In the consuming project:

- `AGENTS.md` - short pointer to Velocity plus local commands and constraints.
- `docs/LIFECYCLE-OVERLAY.md` - project-specific overlay.
- `docs/SYSTEM-ISSUE-LOG.md` - project issue index.
- `docs/SYSTEM-ISSUE-DETAILS.md` - detailed issue records.
- `docs/agent-packets/` - project handoff packets.
- `docs/agent-missions/` - project mission ledger if used.
- `docs/review-packs/` - operator-facing project review artifacts.

## Overlay Requirements

A project overlay must define:

- lane names and authority boundaries
- supported dev/test/deploy commands
- production mutation approval path, including the exact approval phrase(s) that authorize production mutation and whether `ship it` qualifies
- project-specific proof harnesses
- issue numbering and issue-doc format
- branch naming conventions
- role map (which roles are distinct owners vs. hats on one person)
- planning or cadence integration (Scrum, Kanban, Shape Up, or a local method)
- issue-record profile default and escalation triggers
- incident escalation path
- local exceptions to Velocity, if any

Project overlays may specialize Velocity. They may not silently override core lifecycle governance.

If a project needs to change a core Velocity rule, open a Velocity process-change proposal.

## Scaling The Role Split

Velocity scales down as well as up; the authority boundaries matter more than the number of people involved. The original use case is a team of one doing high-volume AI-assisted development, where the roles are a self-binding device — deliberate mode switches for one human working with agents, not bureaucracy. For solo or very small teams, roles may be hats rather than people; the session should still name the current hat and never self-approve a protected change in the same breath that produced it. At minimum, separate the moment of implementation from the moment of acceptance.

The practical minimum for solo AI-assisted work:

- frame the work as Coordinator before asking for implementation
- switch to Fixer only after scope, lane, and proof are clear
- switch to Tester or validation mode before accepting operator-facing behavior
- switch to Architect before changing invariants, ownership, or proof contracts
- switch to Velocity Maintainer only when reusable lifecycle policy is explicitly being changed

In a pair or small team, the most valuable real separations are Operator/Coordinator from Fixer (scope and acceptance), Fixer from Tester (operator-visible workflow claims), and project-overlay owner from Velocity Maintainer (reusable policy). In high-risk, regulated, production-critical, or incident-prone contexts, use stronger separation across Coordinator, Fixer, Tester, Architect, and promotion authority.

Velocity governs authority, proof, lifecycle state, role handoff, and process evolution. It does not define sprint length, estimation units, roadmap cadence, team topology, backlog prioritization, or the release calendar — use Scrum, Kanban, Shape Up, incident command, or a local method for those, and let the overlay say how they map in.

## Overlay Experiments

A project may test a local rule in its overlay before proposing a Velocity core change. An overlay experiment should state its name, owner, start date, intended duration or review trigger, the local rule being tested, the Velocity core rule it touches, a compatibility check against shared-context / separated-write-authority, the evidence to collect, and the promotion path if it works. Overlay experiments must not silently contradict core governance: they may specialize commands, issue formats, lane names, proof harnesses, and routing, but they may not remove acceptance-proof-first, erase lane proof boundaries, or let the role being evaluated rewrite its own evaluation criteria.

