# Reconciled Trunk: the 2.0 Experimental Line Released as 1.9.0

- Status: Proposed
- Date: 2026-09-24
- Authority owner: Mike, Velocity Maintainer
- Mode: Process evolution
- Source: Two release lines existed on 2026-09-23: stable `v1.8.0` on `main`, and the
  `v2.0.0-experimental.1` prerelease published on 2026-09-21 from a separate branch, carrying the
  Work Board, portable project records, decision levels, and management records. The maintainer
  ruled on 2026-09-24, on the Velocity Check-in Desk, that the 2.0 line becomes the trunk,
  reconciled with 1.8.0 (CK-45 A), and then ruled on the three questions the reconciliation
  raised (CK-48 A, CK-49 A, CK-50 A).
- Disposition: Velocity repo proposal, PR #16 (`proposal/2.0-trunk` into `main`); pending the
  maintainer's merge.
- Accepted version: planned v1.9.0 (minor)

## Change

Merge the 2.0 experimental line into `main` with 1.8.0's approved text kept, then apply the
maintainer's rulings:

1. **Placement by scope (CK-45 A with the 1.8.0 guard).** The 1.8.0 manifesto says future
   additions belong in templates, examples, overlays, or the manifesto, not in `docs/`. The five
   documents 2.0 added under `docs/` move: decision levels, work management, and portable records
   to `templates/`; the management reference to `examples/management-reference/`; the
   experimental adoption guide is retired into the adoption guide's "Pin a Release" and each
   profile's own adoption section. `docs/` holds exactly the documents it held at 1.8.0. The docs
   index lists templates by adoption scope, and the adoption guide names each experimental
   template inside the scope it serves.
2. **One word, one meaning.** 2.0's "decision scopes" become "decision levels" (work, initiative,
   portfolio), so "scope" means only an adoption scope. The data field was already
   `decision_level`; no data contract changes.
3. **Decision levels are an optional tag (CK-48 A).** A desk without levels is complete. The
   strict check stays, as an opt-in a project declares in its overlay:
   `--require-decision-levels` on the renderer, or `"desk_requires_decision_levels": true` for the
   file helper. The template's example tags one entry, not all of them.
4. **Lineage, not tie-in (CK-49 A).** PMI and Stage-Gate material reviewed on 2026-09-21 is
   credited in the lineage document; governed documents describe Velocity's method in its own
   words and claim no mapping or compatibility.
5. **One statement of direction.** The manifesto keeps one direction section, "One Core, Two
   Lifecycles", with 2.0's additions folded in; the README keeps one opening. Velocity's own
   trial records move from the repository root to a dated example that binds no agent.
6. **The desk renderer shows a broken desk best-effort.** Parity with the Work Board's rule 11:
   every violation is listed in a Needs repair block, missing fields are marked in place, and the
   renderer exits 1. A desk that conformed renders byte-for-byte as before. The Work Board
   renderer, which already promised this, is hardened to keep the promise: a malformed field
   degrades one card, never the page.
7. **Version by rule (CK-50 A).** Nothing here makes prior conformance non-conformant, so the
   release is 1.9.0. The prerelease keeps its 2.0 name as history.

## Why

A second release line splits every adopter's question "which Velocity do I pin?" and lets two
statements of the same direction drift apart. The 2.0 work is the Work Board the maintainer asked
for as the near-term enhancement, piloted on real work, so it belongs on the trunk. The
reconciliation keeps 1.8.0's approved framing where the two lines disagreed: one core, adoption
scopes that hold no rule of their own, a small Delivery path, and no new mass under `docs/`.

## Scope and Authority

Affected protected artifacts: `AGENTS.md` (one section recording where Velocity's own trial
records now live); `docs/` (index rebuilt by scope, adoption guide sections, one paragraph in
Control Planes, trailing whitespace); `templates/` (new experimental templates, schemas,
renderers, helper; desk renderer and contract); `adrs/0002` (accepted for experimental adoption
only). Also `MANIFESTO.md`, `README.md`, `LINEAGE-AND-ADJACENT-WORK.md`, `CHANGELOG.md`,
`examples/`, and `tests/`.

Authority basis: the maintainer's rulings CK-45, CK-48, CK-49, and CK-50, all 2026-09-24; the
2.0 line's own implementation authority (recorded in
[the portable project records proposal](2026-09-21-portable-project-records.md)); stamping under
Delegated Mechanics after the maintainer merges.

Reusable policy or template support: template support and clarified direction. No lifecycle
rule, role, approval boundary, or proof obligation changes.

## Proof and Disposition

On `proposal/2.0-trunk` at the commit that adds this record:

- 34 of 34 tests pass (desk levels, desk repair, file helper, and fault injection: every field of
  every example entry in both renderers removed or mistyped one at a time, and a page still renders).
- All 455 relative links and anchors resolve (checked by script against GitHub's slug rule).
- Both-parents check: every file present in `v1.8.0` or `v2.0.0-experimental.1` is present,
  moved, or retired as listed in the CHANGELOG; every line that differs from 1.8.0's approved
  text is an intentional change listed above.
- The template's example, the decision-level example, and the Work Board example regenerate
  byte-identical to their committed HTML. Six real project desks and three real boards render
  byte-identical under the new renderers; the pilot desk that declares levels passes with `--require-decision-levels`.
- PMI, Stage-Gate, and the Project Management Institute appear only in the lineage document and
  dated records. No proprietary scaled-agile framework name or vocabulary appears.
- `git diff --check` clean.

Branch disposition: `proposal/2.0-trunk` merges via PR #16, which supersedes PR #14.
