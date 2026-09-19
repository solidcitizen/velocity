# Process Change Proposal — Role-Brief Template

> ACCEPTED 2026-07-05 by the Velocity Maintainer. `templates/role-brief.md` ships as a reusable core template, linked from `docs/INDEX.md` and the `PROJECT-ADOPTION-GUIDE` template list. Released in Velocity canon v1.3.0. This record is retained for provenance; the canon is the template itself.

- Proposal: Add a reusable `templates/role-brief.md` — a per-role **cold-start onboarding brief** that boots an agent *into* a Velocity role. It fills the gap between `docs/ROLE-AUTHORITY.md` (what a role owns and must not do) and *instantiation* (the artifact you hand an agent so it operates *as* that role from a cold start). The template is status-free and instantiates authority **by reference**; it does not redefine it.
- Source: The maintainer reported that two private consuming projects, one a software application and one an operations framework, converged on per-role operating briefs. The application used Coordinator / Product-Owner briefs; the operations framework used Product-Director / Tactical / Reviewer briefs. This recurring need prompted a shared template.
- Triggering evidence: Velocity defines role **authority** (`ROLE-AUTHORITY`) and role **switching** ("name the current hat", `PROJECT-ADOPTION-GUIDE` §Scaling The Role Split), but ships **no template for the cold-start brief that instantiates a role**. `templates/` has handoff / tranche / issue / review-pack / register templates — nothing for role onboarding. Consuming projects reinvent the brief ad hoc, each risking drift.
- Affected control plane: Automation Control Plane (one new template). References the Shared Control Plane (`ROLE-AUTHORITY`, `PROOF-MODEL`) without modifying it.
- Affected protected artifacts: `templates/` (one new file); on acceptance, a one-line link from `docs/INDEX.md` and the `PROJECT-ADOPTION-GUIDE` template list.
- Proposed disposition: Reusable core template. The **populated** per-role briefs stay project-overlay artifacts (as with the System Invariant Register). Nothing in the template names a host, command, domain, or environment.
- Authority owner: Velocity Maintainer, with Architect review of the authority-boundary wording (a role's brief must not soften the criteria that judge its own work — the core "shared context, separated write authority" invariant).
- Project-specific or reusable: Reusable core policy, informed by maintainer-reported experience in two private projects; the template names no project.
- Compatibility risk: Low — purely additive; no change to lifecycle rules, proof model, or role authority. The one real risk the template must foreclose is **restate-and-drift**: a brief that paraphrases a canon rule (a gate list, an approval phrase) into a second copy that silently diverges. The template mandates **link, don't restate** and **status-free**, so a brief always resolves to current canon and current status, never a frozen paraphrase.
- Rollout plan: Add `templates/role-brief.md`. On acceptance, link it from `docs/INDEX.md` and add "role briefs" to the `PROJECT-ADOPTION-GUIDE` template list. Consuming projects instantiate one brief per active role as overlay artifacts.

## Evidence

Publication note (2026-09-09): this is a maintainer-reported account of private project work.
The source repositories and review records are not public reference material. Project names
and internal artifact identifiers have been generalized; the original acceptance, rationale,
and template text are unchanged.

- **Recurring artifact shape.** Both projects produced briefs containing a role, authority
  references, ordered onboarding, operating boundaries, a cold-start line, and directions for
  finding current status. The reported convergence motivated the reusable template; it is not
  an independent replication study.
- **A reported authority defect.** In the operations project, review found that role briefs
  paraphrased a hard-stop list and omitted safeguards against remote physical actuation and
  following instructions in observed content. The lesson was to link to authoritative rules
  instead of maintaining a second version that can drift.
- **Scope of the contribution.** The role-brief template supplied an onboarding format that
  Velocity had not shipped. The same work also revisited disciplines already present in
  Velocity, including adversarial verification and the separation of criticality from mutation
  authority; those observations did not create additional policy contributions.

## Proposed Text

The full proposed text is `templates/role-brief.md`, carried in this branch. It is a fill-in template with: role (one paragraph, authority by reference to `ROLE-AUTHORITY`); ordered onboarding (overlay/index gatekeeper first); operating non-negotiables (proof model, authority/gate, evidence discipline, separated-write-authority — all by link); boundaries (lanes not owned); a cold-start line; "how you show up each session"; and two load-bearing template rules — **status-free** (point to living status) and **link, don't restate** (never paraphrase a canon rule into a drift-prone second copy).

## Decision

- Accepted: 2026-07-05 — shipped as `templates/role-brief.md`, linked from `docs/INDEX.md` and the `PROJECT-ADOPTION-GUIDE` template list. Acceptance amendment: the fill-in instructions gained a repoint-the-canon-links line (a dead canon link defeats *link, don't restate*). Released in Velocity canon v1.3.0.
- Rejected: —
- Deferred: —
- Owner: Velocity Maintainer
- Date: 2026-07-05
