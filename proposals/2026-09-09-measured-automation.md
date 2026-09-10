# Process Change Proposal — Measured Automation And Adjacent Methods

- Status: accepted by Mike as Velocity Maintainer on 2026-09-09.
- Accepted version: **v1.4.0** (additive MINOR).
- Source: operator request on 2026-09-09 following comparison with Anthropic's AI-Native SDLC
  Playbook: "Please incorporate the updates as you recommend, this deserves an updated
  versioning of Velocity, a check for other playbook/frameworks that are relevant for comparison."
- Authority basis: explicit process-evolution intent in this repository. The agent prepares
  the change under Velocity Maintainer responsibility; Mike subsequently approved merge and
  release under [Governance](../governance/GOVERNANCE.md), as recorded below.
- Affected control plane: Automation, with Shared Control Plane references.
- Affected protected artifacts: `docs/CONTROL-PLANES.md`, `docs/PROJECT-ADOPTION-GUIDE.md`,
  `docs/INDEX.md`, and three new files under `templates/`.
- Other affected artifacts: `README.md`, `MANIFESTO.md`, `LINEAGE-AND-ADJACENT-WORK.md`,
  `CHANGELOG.md`, this proposal, and `examples/measured-automation/README.md`.
- Disposition: reusable template support and optional adoption guidance; non-policy research
  and positioning; a synthetic project-overlay example. No consuming-project migration.
- Compatibility: existing authority, proof classes, lifecycle states, and conformance remain
  unchanged. Templates are opt-in. No automatic acceptance, timeout approval, or new delegation
  grade is enacted. Prior closeouts do not need re-judgment, so the changelog's MINOR rule applies.

## Evidence And Design

The [dated comparison](../LINEAGE-AND-ADJACENT-WORK.md#comparison-reviewed-2026-09-09) reviews
Anthropic, AWS AI-DLC, GitHub Spec Kit, BMad, Kiro, Superpowers, and OpenAI harness engineering
using first-party sources. It distinguishes publication dates from current capabilities and
documented practices from executed evidence. Repository history supports extraction of the
method on 2026-05-11; it does not establish the first date of the underlying practices or a
first-ever claim. Historical positioning remains in Git, while current wording acknowledges
related earlier work and present convergence.

The concrete change consists of:

1. An [Agent Evaluation Pack](../templates/agent-evaluation-pack.md) for model/configuration
   changes, immutable criteria, comparable trials, direct evidence, and failure disposition.
2. An [Automation Transition Contract](../templates/automation-transition-contract.md) that
   binds accepted revisions, proof, existing authority, action scope, replay, and recovery.
3. A [Measured Pilot](../templates/automation-pilot.md) with baseline, quality/effort/resource
   measures, deterministic monitoring, and a decision gate before expansion.
4. A [worked example](../examples/measured-automation/README.md) with twelve synthetic cases
   and an explicitly unexecuted tabletop trace.

Fold the small amount of adoption/control-plane guidance into existing documents and link the
templates from the index. Keep actual adapters, hooks, evaluators, cohorts, and commands in
consuming projects. The release supplies practical support without coupling core policy to a
specific toolchain or adding another lifecycle document.

## Review And Proof

- Claim: the additive documents form a coherent, source-backed adoption package under existing
  governance; not that an agent, runtime adapter, or production system has been qualified.
- Proof class: Class D/document review, appropriate to policy/template design; no Class A–C
  behavioral or environment claim.
- Required checks: internal file/anchor links; Markdown structure and whitespace; source
  attribution and historical wording; template/example consistency; compatibility and authority
  review against the unchanged core rules; exact candidate commit and branch disposition.
- Adversarial document scenarios: missing or stale approval, unauthorized fixture edits,
  duplicate/interrupted actions, missing telemetry, and valid already-authorized work.
- Runtime evaluation and a real project pilot: not run; explicitly outside this repo tranche.

Document validation on 2026-09-09 checked 34 Markdown files, 103 internal file/anchor links,
and 16 tables without a broken reference or unbalanced code fence. Whitespace validation passed.
The author also reviewed the twelve synthetic cases against the unchanged authority/proof
rules and corrected template placeholders for Markdown rendering. This is an author document
review, not independent agent verification or execution of those cases. The reviewed candidate
is `0a816bb83f77dd0d59315fd0c863af90f0cfb999` in PR #5. The acceptance amendment changes only
release labels, the changelog release link, and this decision record; it does not change the
approved templates or adoption guidance.

## Decision And Rollout

- Implementation requested: Mike, 2026-09-09, in the instruction quoted above.
- Maintainer merge/release acceptance: Mike, 2026-09-09, replied "yes please merge" to the
  explicit request to merge PR #5 and publish v1.4.0.
- Release disposition: merge the reviewed candidate with this acceptance amendment and create
  `v1.4.0` on the merged canon. Existing release tags remain unchanged.
- Consumer action: optional adoption through the existing overlay-experiment process; pin an
  accepted release when ready. This tranche does not change any consumer's pin or enable a job.
- Evidence to collect next: a real project's evaluation and pilot results, with named owners,
  authorized limits, and measured outcomes rather than inferred gains.
