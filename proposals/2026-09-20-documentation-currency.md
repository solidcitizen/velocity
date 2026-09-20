# Documentation Currency

- Status: Accepted
- Date: 2026-09-20
- Authority owner: Mike, Velocity Maintainer
- Mode: Process evolution — patch
- Source: The maintainer's observation on 2026-09-20 that the repository's documentation carried
  stale references, followed the same day by two independent read-only audits (one commissioned
  by this session, one by a consuming project's lead at the maintainer's request) that agreed on
  a narrow set of findings.
- Disposition: Velocity repo proposal; merged via PR #13 and released as v1.7.2 on 2026-09-20
  (see Proof and Disposition).
- Accepted version: v1.7.2 (patch)

## Change

Write down two things practice already does. First, the mechanics the maintainer may delegate:
merging a proposal the maintainer has explicitly approved, and release stamping. Every acceptance
record since v1.5.1 names a delegate acting on the maintainer's approval, but governance never
said such delegation exists. Second, protected paths as directories, matching `AGENTS.md` and the
way every proposal since v1.4.0 has counted `docs/INDEX.md` as protected.

Correct three accepted proposals whose header still read "not merged", and add the rule that the
header is updated at acceptance. Complete the changelog's release link definitions, which stopped
at v1.4.0. Replace the issue form's version placeholder with a form that does not go stale. State
the core invariant once in the README and link to its canonical statement instead of a fourth
paraphrase; point the README's adoption note at the adoption guide's definition instead of a
second list.

## Why

Stale text in a standard is a conformance problem: a reader who finds a merged proposal marked
"not merged", or a governance document that omits the actor who tagged the last four releases,
cannot tell which document to trust. Each item here is small; together they are the difference
between a repository that reads as maintained and one that reads as drifting.

## Scope and Authority

- Protected artifacts changed: `governance/GOVERNANCE.md` (two additions, one list restated),
  `AGENTS.md` (one sentence).
- Other artifacts: `README.md`, `CHANGELOG.md`, three proposal records, one issue form.
- Classification: clarifications and corrections of existing rules and records. No lifecycle
  rule, role, approval boundary, proof obligation, or prior conformance changes. The delegation
  text describes existing practice and creates no new authority.
- Authority basis: the maintainer's observation and the standing direction that documentation
  gaps are fixed by proposals. Merge and release remain subject to explicit maintainer approval.
- Compatibility: PATCH.

## Proof and Disposition

Relative links and anchors across all changed Markdown re-checked by script, including the new
governance anchor and the adoption-guide anchor the README now uses. The issue form parses as
YAML. `git diff --check` clean. Two audits' findings (changelog link definitions, proposal
dispositions, issue-form placeholder, protected-path contradiction, undocumented delegation,
core-rule duplication, adoption-pattern duplication) are each addressed by a change in this
proposal or recorded as intentionally unchanged: `templates/AGENTS.fragment.md` restates the core
rule on purpose, because it is pasted into project repositories where links do not resolve.

Accepted by Mike as Velocity Maintainer on 2026-09-20: "CK-37 A", answering the Velocity Check-in Desk
ask to approve PR #13. Merged by the CPO session as delegate under that approval (governance,
Delegated Mechanics) and stamped `v1.7.2` on this acceptance commit.

Branch disposition: `proposal/documentation-currency` merged via PR #13.
