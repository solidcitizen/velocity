# Velocity Agent Guide

Velocity is the reusable lifecycle-policy repo for AI-assisted SDLC governance.

## Core Rule

Shared context, separated write authority.

Agents may read broadly and propose lifecycle changes. They may not directly mutate core lifecycle governance unless the operator has explicitly asked for process evolution work in this repo. The canonical statement is [Artifact Authority Boundaries](docs/ARTIFACT-AUTHORITY-BOUNDARIES.md); this file restates it for agents working in this repository.

## Modes

Use `Process evolution mode` for changes to Velocity policy, governance, templates, or examples.

Do not treat work in this repo as product delivery. There is no product implementation lane here.

## Protected Paths

The following paths define reusable lifecycle policy and require explicit process-change intent:

- `docs/`
- `governance/`
- `templates/`
- `adrs/`
- `AGENTS.md`

The `examples/` directory may contain project overlays, but edits there must not silently change Velocity core policy.

## Required Closeout

For any repo mutation, closeout must state:

- affected protected artifacts
- authority basis for the change
- whether the change is reusable policy, template support, or project overlay/example
- proof run
- branch disposition

## Branch Hygiene

Use a feature branch for substantive changes. Keep project-specific migration work separate from Velocity core-policy changes unless the operator explicitly requests a combined tranche.

## Velocity's Own Work Records

Velocity's own trial of the experimental decision-level and portable-records profile, as recorded
on 2026-09-21, is kept as a worked example in
[examples/velocity-self-adoption](examples/velocity-self-adoption/README.md). It is a dated
snapshot, not a work queue, and it binds no agent working in this repository. Velocity's live
work is tracked by the maintainer outside this public repository. No task closure, board view,
or draft pull request approval substitutes for Maintainer acceptance and release authority.
