# Public Reference Cleanup

- Status: Proposed; awaiting maintainer merge and release approval
- Date: 2026-09-09
- Authority owner: Mike, Velocity Maintainer
- Mode: Process evolution — editorial publication cleanup
- Source: Mike identified references to private consuming repositories as out of place in
  the public Velocity repository and asked that the public material stand on its own.
- Disposition: Velocity repo proposal; prepare branch, commit, and pull request
- Proposed version: v1.5.1 (patch)

## Change

Replace the private-project adoption list and examples with an illustrative application
overlay and a policy/project mapping. Both examples are self-contained, explicitly
non-normative, and linked to the public Velocity rules they explain. Commands and local
paths are examples to adapt, not scripts or artifacts supplied by an inaccessible repository.

Generalize private project names and internal PR, ADR, invariant, and artifact identifiers
in three historical proposals and the changelog. Preserve the original acceptance dates,
proposed policy text, and substantive lessons. Qualify the historical evidence as
maintainer-reported experience whose source artifacts are private; do not present the new
illustrative examples as reproductions of those implementations or proof of their results.

Use the approved public domain for the field-guide link. DNS activation is a separate
publication concern; changing this link does not assert that propagation has completed.

## Scope and Authority

- Protected artifact: `docs/INDEX.md`, for two example links only.
- Other artifacts: README, changelog, historical proposals, and `examples/`.
- Classification: project-overlay examples and explanatory publication edits; no reusable
  policy or template changes.
- Authority basis: the maintainer's request to correct private-project references in the
  public presentation. This authorizes preparation; merge and release remain subject to the
  existing explicit-maintainer-approval rule.

No lifecycle stage, role, approval boundary, proof obligation, template, or conformance rule
changes. No consuming project is migrated. No historical tag or Git history is rewritten.
Earlier releases retain their original contents, including project context.

## Publication Follow-Through

After acceptance, merge and release v1.5.1, then update the separate website's pinned
reference and download bundle to that release. Until then, v1.5.0 remains the released
canon and the site's existing archive is unchanged. Do not silently rewrite that archive
while retaining its v1.5.0 label.

## Proof and Disposition

Validation passed: 37 Markdown files and 141 internal links/anchors checked; no removed
private project names or implementation identifiers remain in the proposed tree.
The proposed-policy sections of all three edited historical proposals match `origin/main`
exactly. The protected-file diff is limited to the two example links in `docs/INDEX.md`;
core policy and templates are unchanged. `git diff --check` passed.

Branch: `codex/public-reference-cleanup`; commit and push for pull-request review.
