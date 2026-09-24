# Goal Framing and Adoption Scopes

- Status: Proposed; awaiting maintainer review and merge approval
- Date: 2026-09-23
- Authority owner: Mike, Velocity Maintainer
- Mode: Process evolution
- Source: The maintainer's direction of 2026-09-19, that Velocity should broaden from a software
  delivery lifecycle toward the lifecycle of building a company, and his instruction that the CPO
  session keep that evolution grounded. He approved this framing on 2026-09-23 as the text to
  write down. The scoped-adoption idea is his ("Velocity can offer the user what scope they
  adopt"), with his own constraint that it carry no tie to any proprietary framework.
- Disposition: Velocity repo proposal; branch and pull request prepared for maintainer review.
- Proposed version: v1.8.0 (minor)

## Change

Add one section to `MANIFESTO.md` recording the second axis of Velocity's evolution: not how much
autonomy an agent has, but what kind of system Velocity governs. It states the core rule without
naming software, shows the same five questions recurring from a project to a portfolio, places
the build-measure-learn loop and the question of self-redesign against Velocity's existing
answer, fixes the structure as one core with two lifecycles consuming it, and gives five tests a
candidate must pass to enter the core. It names Portfolio as an emerging position rather than a
supported scope.

Add "Choose Your Scope" to `docs/PROJECT-ADOPTION-GUIDE.md`: Delivery, Automation, Entity, each a
bundle of rules and templates that already exist, each containing the previous one, with Portfolio
named as emerging. Credit the two named influences in `LINEAGE-AND-ADJACENT-WORK.md`.

## Why

The direction exists today only in conversation and in the maintainer's own practice. A standard
whose stated purpose is narrower than its actual use invites two failures: projects outside
software delivery conclude it does not apply to them, and work that does broaden it arrives with
no test for what belongs in the core. The five tests are the guard; the scopes are how a project
takes only what it needs without a second core appearing under a scope's name.

Scoped adoption is a common pattern in delivery frameworks. This proposal takes the pattern only:
no other framework's vocabulary, mapping, or compatibility claim appears here or anywhere in the
repository, at the maintainer's explicit instruction.

## Scope and Authority

- Protected artifacts changed: `docs/PROJECT-ADOPTION-GUIDE.md` (one new section).
- Other artifacts: `MANIFESTO.md` (one new section, direction), `LINEAGE-AND-ADJACENT-WORK.md`
  (one attribution paragraph), `CHANGELOG.md`.
- Classification: additive direction and adoption guidance. No lifecycle stage, role, approval
  boundary, proof obligation, template, or conformance rule changes. Every scope is a view of
  rules that already exist; no scope introduces one.
- Authority basis: the maintainer's direction of 2026-09-19 and his approval of this framing on
  2026-09-23. Merge and release remain subject to explicit maintainer approval.
- Compatibility: MINOR. A project conformant today is conformant at Delivery or Automation scope
  without changing anything.
- Provenance: the practice behind the direction is maintainer-reported private work, qualified as
  such in the manifesto section itself.

## Proof and Disposition

Relative links and anchors across the changed documents re-checked by script, including the two
new cross-document anchors. Every template and document named in the scopes was checked to exist
at the path given. The repository was grepped for any proprietary-framework name or vocabulary;
none appears. `git diff --check` clean.

Branch: `proposal/goal-framing`. Opened as a pull request for review.
