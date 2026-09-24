# Adopt Velocity 2.0 Experimental

`v2.0.0-experimental.1` is an opt-in prerelease of the decision-aware work and portable-records
profile. [Release notes](https://github.com/solidcitizen/velocity/releases/tag/v2.0.0-experimental.1)
identify the fixed source tag. `codex/2.0-experimental` is the evolving channel; pin the tag or
its commit in a project. Stable canon remains `v1.8.0`. A finalized 2.0 compatibility contract
and automatic migration are not supplied.

## Get a fixed copy

For a new project integration, from the consuming repository root (choose an unused path):

```sh
git submodule add https://github.com/solidcitizen/velocity.git vendor/velocity
git -C vendor/velocity fetch origin tag v2.0.0-experimental.1
git -C vendor/velocity checkout --detach v2.0.0-experimental.1
git -C vendor/velocity rev-parse HEAD
git add .gitmodules vendor/velocity
```

Commit the submodule pin with the project's overlay and entry-point changes after review.
Use the project's established dependency location if it already has one. To update an
existing clean Velocity submodule, first record its current commit and preserve local edits,
then fetch the tag and check it out detached:

```sh
git -C vendor/velocity rev-parse HEAD
git -C vendor/velocity fetch origin tag v2.0.0-experimental.1
git -C vendor/velocity checkout --detach v2.0.0-experimental.1
git add vendor/velocity
```

A project without submodules can clone the same fixed release into an unused location:

```sh
git clone --branch v2.0.0-experimental.1 --depth 1 \
  https://github.com/solidcitizen/velocity.git velocity-standard
```

Record the resolved commit. Reuse the whole pinned `templates/` directory; mixing helper,
renderer, schema, and contract revisions is unsupported.

## Adopt the smallest useful records

1. Read the [standing method](MANAGEMENT-REFERENCE.md), [decision scopes](DECISION-SCOPES.md),
   and [work contract](WORK-MANAGEMENT.md). Record opt-in scope, accountable owner, executing
   lead, authority/capacity, review triggers, and the pin in the project's lifecycle overlay.
2. Create a project-owned artifact index from [the template](../templates/artifact-index.md).
   Declare one authoritative work binding: existing `TODO.md`, structured JSON, or an external
   tracker. Keep TODO when it already does the job. Preserve existing identities and history.
3. Cover the three levels using the [decision-record baseline](../templates/decision-records.md):
   a work queue; initiative purpose/plan/outcome evidence; portfolio direction, selected work,
   capacity assumptions, and decisions. These can be sections in existing files. Small efforts
   can name one owner and an assumed capacity; they need no invented business case or budget.
4. Use one [Check-in Desk](../templates/executive-checkin-desk.md) within its ownership/access
   scope. Qualify each open decision as `work`, `initiative`, or `portfolio` and retain that
   field with its ruling. Qualify existing open asks on adoption; leave unknown historical
   levels unknown. Use `--require-decision-levels` when validating/rendering a standalone Desk.
5. Point every AI entry file or integration at the same artifact index and overlay. Use the
   [agent fragment](../templates/AGENTS.fragment.md) as guidance. Sessions read the current
   source and revision before writing; model-specific memory and panels are optional views.
6. Rehearse one bounded workflow: create work, route a decision, record an actual authorized
   ruling, release only its covered dependency, and verify history and view freshness. Name
   the actual tools and proof. Do not call a fixture run a cross-vendor qualification.

If selecting JSON, the [file helper](../templates/project-records.md) initializes an empty
project-owned workspace and provides cooperating-writer safeguards on a local POSIX filesystem.
Python 3.9+ is required; local qualification used Python 3.14.6 on macOS. The helper does not
parse or render Markdown and does not enforce real role/approval authority. The standalone
HTML can be displayed in a browser or any AI tool that supports a local web view.

Keep operational/private records in their declared audience boundary. Publishing the standard
does not require publishing a project's work records. Adopting the standard does not adopt
Velocity's own `ARTIFACTS.md`, TODO, initiative, or portfolio data.

## Upgrade, handoff, and recovery

Keep the prior pin and a versioned snapshot/backup of operational records before adoption.
Resolve pending helper operations using the exact tool/configuration revision that created
them before upgrading. Qualify changed contracts and renderers, then regenerate views and
verify their receipts. Never repoint a project's dependency to the moving branch as an
unreviewed automatic upgrade.

To roll back, preserve all new rulings and work history, restore the prior tool pin, and
reconcile record compatibility before resuming writes. Do not restore an old record snapshot
over decisions made since adoption. If the project selects a larger tracker later, use the
[binding and handoff contract](../templates/tracker-binding-and-handoff.md) and qualify that
destination before retiring the file as writable authority.

See [qualification](../examples/portable-records/QUALIFICATION.md) for tested scope. Actual
two-vendor continuation, live tracker integration, distributed writers, automated Markdown
views, committee workflow, and measured decision acceleration remain unqualified or unsupplied.
Strategic goal-setting is a future portfolio candidate, not an experimental runtime capability.
