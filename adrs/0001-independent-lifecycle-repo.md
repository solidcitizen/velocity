# ADR-0001: Independent Lifecycle Repository

- Status: Accepted
- Date: 2026-05-11

## Context

The initial lifecycle rules were embedded in a product repository. That made them useful immediately, but it mixed reusable SDLC governance with project-specific commands, environments, issue records, and promotion paths.

The same project roles that perform delivery could also edit the process documents that evaluate delivery. That weakens artifact authority and makes it harder to reuse the method in other projects.

## Decision

Velocity is the independent repository for reusable AI-assisted SDLC lifecycle rules.

Product repositories consume Velocity through project overlays. Project-specific details remain in the product repo. Reusable lifecycle rules live in Velocity.

Velocity adopts the core invariant:

> Shared context, separated write authority.

## Consequences

- Process evolution can proceed independently from any one product.
- Project roles can read and propose lifecycle changes, but cannot directly modify lifecycle governance during ordinary delivery.
- Project adoption requires a local overlay that maps Velocity concepts to project commands, lanes, and issue artifacts.
- Existing product-embedded lifecycle docs should eventually be reduced to project overlays and references.

