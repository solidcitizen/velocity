# Check-in Desk Repeatability

- Status: Proposed; awaiting maintainer review and merge approval
- Date: 2026-09-19
- Authority owner: Mike, Velocity Maintainer
- Mode: Process evolution
- Source: The maintainer's observation, one day after v1.6.0, that the Executive Check-in Desk
  had been adopted by every one of his projects and that their pages had already diverged. A
  maintainer-reported audit of five private consuming desks against the v1.6.0 contract followed
  the same day. The maintainer's direction: templates must be simple to use, repeatable, and need
  no reinvention per project; a real gap in a Velocity template is fixed by a proposal to
  Velocity, never by rolling your own. Approved for drafting as desk ask CK-22, option A.
- Disposition: Velocity repo proposal; branch and pull request prepared for maintainer review;
  not merged.
- Proposed version: v1.7.0 (minor)

## Change

Replace the hand-built desk with a desk built from a data file. Add
`templates/executive-checkin-desk.schema.json` (field definitions),
`templates/executive-checkin-desk.example.json` (a placeholder desk to copy), and
`templates/render-checkin-desk.py` (a Python 3.9+, standard-library-only renderer that validates
the data file against the contract, refuses to render a violating desk, and computes the header
stamp, the three totals, the ordering of every section, and the reply examples).
`templates/executive-checkin-desk.html` becomes the renderer's output for the example and is no
longer edited by hand.

Revise `templates/executive-checkin-desk.md` so that everything the first revision implied is
stated: exact section headings and field labels; the `CK` prefix everywhere; the time of day in
the header stamp; a maintainer slot in the stamp; an ID on every team decision; and the rule that
only the project name, operator, maintainer, time-zone label, and color tokens vary per project.
Close three gaps the audit found: an ask that stops needing an answer closes as withdrawn with a
reason and keeps its ID; one question open on two of the operator's desks has one owning desk and
a pointer entry on the other; and a team decision's status opens with one of `done`, `in motion`,
`blocked`, `reversed`. Add migration steps for desks built before this revision.

Extend the "Executive Check-in Discipline" section of `docs/PROJECT-ADOPTION-GUIDE.md` with the
shared-surface rule: an operator who runs several projects meets several desks, so a project
that needs something the data file cannot express raises a Velocity proposal rather than building
a local variant. Note the new files in `docs/INDEX.md`.

## Why

The audit found three kinds of divergence across five desks, all within one day of adoption.
Rules the contract stated were broken outright: a header total that did not match the page, an
extra section, decisions filed as actions, improvised field names, team decisions without IDs,
and a different ID prefix. Rules the contract only implied were drifted: the wording of the
stamp, the project name in the title, the ruling label. And three needs the contract did not
address were met locally three different ways: an ask dropped without record, one question
tracked under two IDs on two desks, and status words invented per project.

Every one of these is a cost borne by the operator, who reads all five pages, and none of them
was unreasonable on the part of the project that made it. The template left too much to
judgment, and it offered a starter without requiring it. Two projects independently built a data
file and a renderer to cope, which is precisely the reinvention the maintainer wants to end. This
revision moves that work into Velocity once, states every label, and makes the renderer the
single way to build the page, so the desk reads the same on every project and a gap surfaces as
a proposal instead of a fork.

## Scope and Authority

- Protected artifacts changed: `templates/executive-checkin-desk.md` (revised),
  `templates/executive-checkin-desk.html` (now generated), `docs/PROJECT-ADOPTION-GUIDE.md` (one
  paragraph extended), `docs/INDEX.md` (one line).
- Protected artifacts added: `templates/executive-checkin-desk.schema.json`,
  `templates/executive-checkin-desk.example.json`, `templates/render-checkin-desk.py`.
- Classification: reusable template support and adoption guidance. No role, approval boundary,
  proof obligation, or lifecycle stage changes. No automation is authorized or enabled; the
  renderer is a local tool that produces a page from a file the project already owns.
- Authority basis: the maintainer's direction of 2026-09-19 and his approval to draft ("CK-22
  A"). This authorizes preparing the branch and pull request; merge and release remain subject to
  the existing explicit-maintainer-approval rule (see `governance/GOVERNANCE.md` Process Change
  Flow).
- Compatibility: MINOR. Additive files and a tightened optional template. No delivery closeout
  is re-judged. Desks instantiated before this release should be migrated; the migration keeps
  every existing ID, so no operator reference breaks.
- Provenance: the audited desks belong to private consuming projects and are described here only
  in aggregate. No project name, data, or secret appears in the shipped artifacts.

## Publication Follow-Through

After acceptance, merge and release v1.7.0. The publication site's download bundle and toolkit
page then include the schema, example, and renderer alongside the contract; that is a separate
site change on the pinned tag.

## Proof and Disposition

The example data file validates and renders; the committed HTML starter is byte-for-byte the
renderer's output for it. Seven negative tests each fail validation as intended: a gap in the ID
sequence, a duplicated ID, a non-date in `needed_by`, a Decide without a lean, a team status
outside the fixed set, an unknown theme token, and a withdrawn ask without a reason. The rendered
page parses with balanced tags in both standalone and fragment modes, carries light and dark
tokens with the theme guards, prints the five headings in order, and contains no silence-as-consent
wording. Relative links and anchors in the changed Markdown were re-checked by script.
`git diff --check` passed. The Velocity project's own desk was migrated to the data file and
rendered with this renderer as the first real instance.

Branch: `proposal/checkin-desk-repeatability`, prepared in an isolated worktree. Opened as a pull
request for review; not merged.
