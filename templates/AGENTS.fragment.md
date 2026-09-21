# Velocity Lifecycle

This project uses Velocity for AI-assisted SDLC governance.

Velocity owns reusable lifecycle policy:

- lifecycle model
- role authority
- artifact authority boundaries
- proof model
- branch hygiene
- process evolution governance

Project-specific commands, lanes, environments, issue records, and promotion paths are defined by this repository's local overlay.

Core rule:

> Shared context, separated write authority.

Delivery roles may read Velocity rules and propose changes. They may not directly modify Velocity lifecycle governance during ordinary product delivery.

## Required Local Overlay

Before substantive work, read the project overlay and identify:

- target lane
- operating mode
- branch hygiene state
- proof class required
- protected artifacts affected
- whether lifecycle-rule changes are only recommendations or requested repo mutations

If the project adopts Portable Project Records, read the artifact index linked from its
overlay before locating or updating work and Desk records. Use its authoritative locations,
role boundaries, pinned shared commands, current revisions, and recovery procedure. Agent
memory is not the authority. Do not create a second backlog, bypass a pending operation, or
report a view current without checking the selected display. External-tracker mode routes work
to its declared binding; the retained local board is an archive. Changing models/tools does
not change role authority.
