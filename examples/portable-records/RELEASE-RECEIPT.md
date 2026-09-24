# Experimental Publication Receipt

Operation: `VEL-PF-1-20260921-experimental-release-closeout`.
Recorded by Codex in the Coordinator responsibility on 2026-09-21 PT.

- Release: [v2.0.0-experimental.1](https://github.com/solidcitizen/velocity/releases/tag/v2.0.0-experimental.1).
- GitHub publication time: `2026-09-22T02:35:53Z` (2026-09-21 PT).
- Published state read back: `isDraft: false`, `isPrerelease: true`.
- Target branch: `codex/2.0-experimental`; published from the reviewed `codex/portable-project-records` snapshot.
- Annotated tag object: `55e69dd8959b3733c44ef7c9e8359d3aefbf3551`.
- Fixed source commit: `aa9462b784416f1db1e743e0f0a8f5041d95d0d4`.
- Remote experimental branch matched that commit at publication. This receipt advances the
  branches as closeout documentation; it does not move the fixed release tag.
- Remote main retained `3af4bf88b81dabe4fe71a425f3818e506efe4861`; GitHub's latest stable
  release remained `v1.7.2`.
- A fresh public HTTPS clone at the tag resolved the expected source commit. Six key files
  matched local bytes: experimental adoption guide, management reference, guarded helper,
  both renderers, and the generated three-level Desk example.

The release candidate passed 25 local tests, the synthetic fresh-process workflow, JSON and
Python 3.9 syntax checks, legacy render compatibility apart from the version footer, 318 local
links/anchors across 34 Markdown files, whitespace checks, and desktop browser inspection.
See [qualification](QUALIFICATION.md) for scope and remaining integration gaps.

Authority: Mike as Velocity Maintainer explicitly requested publication and permitted an
experimental 2.0 release branch. Protected artifacts affected by the release are under
`docs/`, `templates/`, `adrs/` (ADR-0002), and `AGENTS.md`. The release contains reusable
experimental policy/template support, synthetic examples, and scoped Velocity trial records.
The experimental branch and fixed prerelease are published; [draft PR #14](https://github.com/solidcitizen/velocity/pull/14)
retains the stable-integration review. No consuming-project migration, stable-main merge,
unrelated proposal acceptance, or live capability qualification is claimed.
