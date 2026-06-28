# Project Adoption Guide

Velocity is adopted through a thin project overlay.

## What Stays In Velocity

- reusable role definitions
- lifecycle state model
- proof taxonomy
- artifact authority boundaries
- branch hygiene requirements
- process evolution governance
- templates for packets, tranches, closeout, and review packs

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
- local exceptions to Velocity, if any

Project overlays may specialize Velocity. They may not silently override core lifecycle governance.

If a project needs to change a core Velocity rule, open a Velocity process-change proposal.

