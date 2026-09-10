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

## Evaluating Automation Changes

Product proof and automation proof answer different questions: whether the delivered system
works, and whether the agent configuration still performs its assigned work correctly. Projects
can use the [Agent Evaluation Pack](../templates/agent-evaluation-pack.md) to compare model,
prompt, skill, hook, permission, and runtime changes against representative tasks and incidents.
This is recommended qualification guidance, not a new universal evaluation requirement.

Keep the evaluated configuration separate from the authority that accepts its results. Apply
the existing artifact-authority rules to expected outcomes and evaluation criteria. A passing
evaluation does not change lane authority or authorize a lifecycle-rule modification. Runtime
adapters, CI jobs, fixtures, and populated results belong to the consuming project.

For automated handoffs, the [Transition Contract](../templates/automation-transition-contract.md)
records the accepted artifact, direct proof, existing authorization, permitted next action,
and recovery route. A trigger initiates evaluation of that contract; it does not grant authority.
The [Measured Pilot](../templates/automation-pilot.md) connects those contracts to observed
delivery time, human effort, quality, and resource use.

## Change Disposition Labels

Use these labels when recommending or making process changes:

- `automation memory only` - useful for future automation runs, not policy.
- `Velocity repo proposal` - should be reviewed by a Velocity Maintainer.
- `project overlay proposal` - belongs in a consuming project's local adapter.
- `coordinator-owned project change` - belongs in the product repo under Coordinator control.
- `branch/commit/push requested` - operator has asked for a concrete repo mutation lifecycle.
