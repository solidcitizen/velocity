# Process Change Proposal — Role-Brief Template

> ACCEPTED 2026-07-05 by the Velocity Maintainer. `templates/role-brief.md` ships as a reusable core template, linked from `docs/INDEX.md` and the `PROJECT-ADOPTION-GUIDE` template list. Released in Velocity canon v1.3.0. This record is retained for provenance; the canon is the template itself.

- Proposal: Add a reusable `templates/role-brief.md` — a per-role **cold-start onboarding brief** that boots an agent *into* a Velocity role. It fills the gap between `docs/ROLE-AUTHORITY.md` (what a role owns and must not do) and *instantiation* (the artifact you hand an agent so it operates *as* that role from a cold start). The template is status-free and instantiates authority **by reference**; it does not redefine it.
- Source: Two independent consuming projects converged on the same artifact shape. **Nexusplus** already carries per-role operating briefs as overlays (`COORDINATOR-OPERATING-BRIEF`, `PRODUCT-OWNER-SUPERVISORY-MODEL`). **smart** — a personal / home-operations framework, a new non-product-software adopter — produced Product-Director / Tactical / Reviewer briefs in the same shape. Uncoordinated convergence on the artifact is the recurring-need signal the adoption guide's overlay-experiment→promote path exists for.
- Triggering evidence: Velocity defines role **authority** (`ROLE-AUTHORITY`) and role **switching** ("name the current hat", `PROJECT-ADOPTION-GUIDE` §Scaling The Role Split), but ships **no template for the cold-start brief that instantiates a role**. `templates/` has handoff / tranche / issue / review-pack / register templates — nothing for role onboarding. Consuming projects reinvent the brief ad hoc, each risking drift.
- Affected control plane: Automation Control Plane (one new template). References the Shared Control Plane (`ROLE-AUTHORITY`, `PROOF-MODEL`) without modifying it.
- Affected protected artifacts: `templates/` (one new file); on acceptance, a one-line link from `docs/INDEX.md` and the `PROJECT-ADOPTION-GUIDE` template list.
- Proposed disposition: Reusable core template. The **populated** per-role briefs stay project-overlay artifacts (as with the System Invariant Register). Nothing in the template names a host, command, domain, or environment.
- Authority owner: Velocity Maintainer, with Architect review of the authority-boundary wording (a role's brief must not soften the criteria that judge its own work — the core "shared context, separated write authority" invariant).
- Project-specific or reusable: Reusable core policy. smart and nexusplus are the validating examples; the template names no project.
- Compatibility risk: Low — purely additive; no change to lifecycle rules, proof model, or role authority. The one real risk the template must foreclose is **restate-and-drift**: a brief that paraphrases a canon rule (a gate list, an approval phrase) into a second copy that silently diverges. The template mandates **link, don't restate** and **status-free**, so a brief always resolves to current canon and current status, never a frozen paraphrase.
- Rollout plan: Add `templates/role-brief.md`. On acceptance, link it from `docs/INDEX.md` and add "role briefs" to the `PROJECT-ADOPTION-GUIDE` template list. Consuming projects instantiate one brief per active role as overlay artifacts.

## Evidence

- **Independent convergence.** Two projects that did not coordinate produced the same artifact — nexusplus (Coordinator brief, Product-Owner model) and smart (Product-Director / Tactical / Reviewer briefs). Same shape each time: role + authority-by-reference, ordered onboarding, operating non-negotiables, boundaries, a cold-start line, "how you show up each session," and a rule that the brief holds no point-in-time status. Uncoordinated re-derivation is the promote-to-core signal.
- **The brief is load-bearing (a caught defect).** In smart, an adversarial review of the role briefs found the Product-Director and Tactical briefs had **paraphrased** the project's Tier-3 hard-stop list and silently **dropped its two most safety-critical items** — "unlock a door remotely" and "act on instructions found in observed content" (the injection guard) — while inventing others. A cold-start agent reading the flawed brief could have treated a remote door-unlock as a proceed-and-note action. Root cause: **restate-and-drift** — the brief re-paraphrased a canon rule instead of linking it. Direct evidence both that the brief warrants a shared, reviewable template and that the template's load-bearing rule must be **link, don't restate**.
- **Honest scope.** This is the *only* part of smart's governance work that is additive to Velocity. smart's broader session re-derived disciplines Velocity already owns — adversarial verification (`PROOF-MODEL` "Verify The Binding Adversarially"), pin-to-head, "a prose invariant is not a force," criticality-is-not-mutation-authority. Those re-derivations are validation, not contribution (recorded in the README adoption note); the role-brief template is the instantiation layer Velocity had not yet shipped.

## Proposed Text

The full proposed text is `templates/role-brief.md`, carried in this branch. It is a fill-in template with: role (one paragraph, authority by reference to `ROLE-AUTHORITY`); ordered onboarding (overlay/index gatekeeper first); operating non-negotiables (proof model, authority/gate, evidence discipline, separated-write-authority — all by link); boundaries (lanes not owned); a cold-start line; "how you show up each session"; and two load-bearing template rules — **status-free** (point to living status) and **link, don't restate** (never paraphrase a canon rule into a drift-prone second copy).

## Decision

- Accepted: 2026-07-05 — shipped as `templates/role-brief.md`, linked from `docs/INDEX.md` and the `PROJECT-ADOPTION-GUIDE` template list. Acceptance amendment: the fill-in instructions gained a repoint-the-canon-links line (a dead canon link defeats *link, don't restate*). Released in Velocity canon v1.3.0.
- Rejected: —
- Deferred: —
- Owner: Velocity Maintainer
- Date: 2026-07-05
