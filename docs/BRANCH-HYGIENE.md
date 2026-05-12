# Branch Hygiene

Branch state is part of tranche control.

Before starting a new implementation, verification, promotion, or process-doc tranche, report and resolve:

- current branch and whether it is based on current mainline
- uncommitted files
- unpushed commits
- whether the current work is committed, intentionally parked, abandoned, merged, or still active
- whether the next tranche is on the same issue
- open PR or no-PR status when a branch is meant to continue
- stale or prunable worktrees that could confuse checkout or merge decisions

Do not start a new unrelated tranche from a dirty branch or from a branch that already contains unrelated work.

If an interruption forces a priority switch, first park the current branch by committing or stashing with an explicit label, then switch from clean mainline unless the new work is intentionally on the same branch.

Formal issue records and process notes are not background residue. Commit them to the active issue branch when they belong to that tranche, or split them to a docs/process branch when independent.

## Closeout Disposition

Closeout must include one branch disposition:

- `merged`
- `ready for PR`
- `pushed and parked`
- `docs-only follow-up required`
- `stale branch/worktree retained intentionally`
- `stale branch/worktree pruned`
- `no repo mutation`

## Worktrees

Run worktree inspection during meta-cleanup or before consolidation work.

Prune only stale metadata or branches whose disposition is known. Do not delete active worktrees or ahead-only branches without an explicit decision.

