# Velocity Agent Guide

Velocity is the reusable lifecycle-policy repo for AI-assisted SDLC governance.

## Core Rule

Shared context, separated write authority.

Agents may read broadly and propose lifecycle changes. They may not directly mutate core lifecycle governance unless the operator has explicitly asked for process evolution work in this repo.

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

