# Control Planes

Velocity separates delivery governance from automation governance.

## Delivery Control Plane

Delivery governance controls product work:

- issue records
- tranches
- implementation scope
- acceptance criteria
- proof mapping
- verification and promotion gates
- review packs
- closeout

The Delivery Control Plane belongs primarily to the project Coordinator, with Architect involvement for semantic or authority-changing work.

## Automation Control Plane

Automation governance controls how agents run the SDLC:

- role dispatch rules
- automation memory
- process-review prompts
- branch hygiene behavior
- skill/process recommendations
- agent permissions over artifacts
- templates for handoffs and closeout

The Automation Control Plane belongs to Velocity Maintainers, not ordinary project delivery roles.

## Shared Control Plane

Some rules deliberately affect both delivery and automation:

- acceptance-proof-first
- branch hygiene
- artifact authority boundaries
- scenario-vs-mechanism proof separation
- role handoff requirements
- issue capture mode

Shared-control-plane changes need explicit ownership and disposition. Do not rely on the word `durable` without saying whether the target is:

- automation memory only
- Velocity repo policy proposal
- project overlay proposal
- coordinator-owned project repo change
- branch/commit/push requested

## Change Disposition Labels

Use these labels when recommending or making process changes:

- `automation memory only` - useful for future automation runs, not policy.
- `Velocity repo proposal` - should be reviewed by a Velocity Maintainer.
- `project overlay proposal` - belongs in a consuming project's local adapter.
- `coordinator-owned project change` - belongs in the product repo under Coordinator control.
- `branch/commit/push requested` - operator has asked for a concrete repo mutation lifecycle.

