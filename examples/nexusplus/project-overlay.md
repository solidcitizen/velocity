# Nexusplus Velocity Overlay

This overlay shows how Nexusplus should consume Velocity.

Nexusplus remains the authority for product architecture, product issue records, local commands, environments, and production promotion paths. Velocity owns reusable lifecycle policy.

## Local Source Of Truth

Nexusplus keeps:

- `AGENTS.md` - local agent and developer guide
- `docs/SYSTEM-ISSUE-LOG.md` - issue queue and triage
- `docs/SYSTEM-ISSUE-DETAILS.md` - detailed issue records
- `docs/agent-packets/` - handoff packets
- `docs/agent-missions/` - issue-indexed mission ledger
- `docs/review-packs/` - operator-facing review artifacts
- `docs/ARCHITECTURE.md` and ADRs - project architecture authority

Velocity keeps:

- lifecycle roles and state model
- artifact authority boundaries
- proof taxonomy and V-model mapping
- branch hygiene model
- process-change governance
- reusable templates

## Nexusplus Lanes

- `repo` - code/docs reading and editing, local tests, tranche shaping.
- `local implementation` - local dev server, browser/E2E, integration tests.
- `staging` - `.env.staging`, staging app/database, production-like non-prod verification.
- `host-qualified verification` - readonly production host checks and production identity/readback.
- `promotion` - approved production deploys, migrations, restarts, recovery actions.
- `architecture decision` - project invariants, authority boundaries, proof contracts.

## Nexusplus Commands

Representative commands stay in the Nexusplus project overlay, not Velocity core:

- `npm run dev:up`
- `npm run dev:health`
- `npm run check`
- `npm run test:smoke`
- `npm run test:smoke:staging`
- `npm run test:integration:core`
- `npm run ops:prod:health`
- `npm run ops:prod:db:identity`

## Nexusplus-Specific Constraints

- Production promotion is approval-gated.
- Production mutation is not implied by deploy scripts, local env files, or GitHub auth.
- Host-qualified proof requires explicit host-qualified lane access.
- Operator-reported workflow defects require scenario-shaped Class A proof.
- Issue capture mode stays lightweight unless the operator explicitly exits capture mode.

## Migration Recommendation

Reduce Nexusplus lifecycle docs over time to:

- a pointer to Velocity
- the Nexusplus lane map
- project commands
- project-specific issue and promotion rules

Do not delete existing Nexusplus process docs until the project overlay has been adopted and linked from `AGENTS.md`.

