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

