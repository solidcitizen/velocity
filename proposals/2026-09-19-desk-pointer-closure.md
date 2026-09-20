# Check-in Desk Pointer Closure

- Status: Accepted
- Date: 2026-09-19
- Authority owner: Mike, Velocity Maintainer
- Mode: Process evolution — patch
- Source: During the same-day migration of a private consuming desk to v1.7.0, its delivery lead
  found that the schema described a pointer entry (an ask owned by another desk) as open-only, so
  a question the owning desk had already answered would show as open forever. The lead used a
  conformant interim (a closed ask whose ruling names the owner) and reported the gap to Velocity
  instead of building a local variant, which is the path the 1.7.0 adoption rule asks for.
- Disposition: Velocity repo proposal; branch and pull request prepared for maintainer review;
  not merged.
- Accepted version: v1.7.1 (patch)

## Change

State in contract rule 8 that a pointer closes with its owner: same `answered_on`, state
`answered` or `withdrawn`, a ruling naming the owner's decision, `owned_by` kept. Allow
`owned_by` on a closed entry in the schema and the renderer's validation, and render a closed
pointer under Already answered with "owned by *project* CK-n". Tolerate a withdrawn ruling that
already begins with "withdrawn". Update the migration step for shared questions.

## Why

One ask, one owner is the rule; the pointer is how the non-owning desk shows the question. If the
pointer cannot close, the operator sees a decided question listed as open, which the desk must
never do. The fix keeps pointers pointers for their whole life instead of forcing a shape change
at closure.

## Scope and Authority

- Protected artifacts changed: `templates/executive-checkin-desk.md` (rule 8 and one migration
  step), `templates/executive-checkin-desk.schema.json`, `templates/render-checkin-desk.py`.
- Classification: reusable template support; a clarification of an existing rule. No role,
  approval boundary, proof obligation, or lifecycle stage changes.
- Authority basis: the maintainer's 2026-09-19 direction that template gaps are fixed by
  proposals to Velocity; the CPO session owns the template. Merge and release remain subject to
  explicit maintainer approval.
- Compatibility: PATCH. No new required field; every desk that validates under 1.7.0 validates
  and renders identically under 1.7.1.

## Proof and Disposition

The example data file validates and renders unchanged. A closed pointer (state `answered` with
`owned_by`) validates and renders under Already answered with the owner note; a closed pointer
without a ruling is rejected; an open pointer still renders under Decide and is excluded from
totals; a withdrawn ruling beginning "Withdrawn —" renders the word once. Two consuming desks
migrated the same day re-validate unchanged. `git diff --check` clean; relative links re-checked.

Accepted by Mike as Velocity Maintainer on 2026-09-19: "CK-32 A", answering the Velocity Check-in Desk
ask to approve PR #12. Merged by the CPO session under that approval and stamped `v1.7.1` on this
acceptance commit, per the stamping delegation.

Branch disposition: `proposal/desk-pointer-closure` merged via PR #12.
