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

Agent memory is not the authority, and changing models or tools does not change role authority.

## Checks And Corrections

Adding a test or check is ordinary work. Deleting, skipping, loosening, or suppressing a check that carries acceptance or proof evidence is a protected change: propose it with evidence, and do not apply it yourself. A comment explaining why some code may skip a check is not an exemption.

When the operator corrects you, prefer a design change or an automatic check over a new line of instructions, and say which one you made.
