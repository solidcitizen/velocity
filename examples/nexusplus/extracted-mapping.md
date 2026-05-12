# Nexusplus Extraction Mapping

This file records where the initial Velocity rules came from and what should remain project-specific.

## Generalized Into Velocity

| Nexusplus concept | Velocity destination |
| --- | --- |
| AI engagement by abstraction layer | `docs/LIFECYCLE-MODEL.md` |
| AI tranche template | `templates/tranche-template.md` |
| Deterministic proof policy | `docs/PROOF-MODEL.md` |
| Coordinator operating brief | `docs/ROLE-AUTHORITY.md`, templates |
| Tester/Fixer/Coordinator protocol | `docs/ROLE-AUTHORITY.md`, templates |
| SDLC artifact authority boundaries | `docs/ARTIFACT-AUTHORITY-BOUNDARIES.md` |
| Branch hygiene gate | `docs/BRANCH-HYGIENE.md` |
| Automation vs delivery governance distinction | `docs/CONTROL-PLANES.md` |

## Stays In Nexusplus Overlay

- concrete npm scripts and Codex actions
- port numbers, hosts, and database names
- production promotion workflow names
- Nexusplus issue IDs and issue logs
- pdlcache, pgvpd, Supabase, Outlook, iCloud, and contact-domain-specific contracts
- Nexusplus architecture and ADRs
- Nexusplus stabilization plan and product roadmap

## Migration Guardrail

Do not copy Nexusplus host, database, provider, or product-specific details into Velocity core docs unless they are clearly labeled as examples.

