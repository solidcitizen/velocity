# Portable Records Qualification

This record distinguishes local template-support proof from live integration acceptance.
It does not qualify every model/provider that can read the files.

## Experimental release qualification

For `v2.0.0-experimental.1` on 2026-09-21, the 25-test suite passes on macOS 26.6.2,
Python 3.14.6. It includes the original 17 file-support scenarios plus eight decision-level
checks: one Decide section and total across three levels; strict qualification including
pointers; invalid values on open/closed/team entries; unclassified legacy history; pointers
excluded from totals; CLI/example reproduction; closure/export retention; and a recorded
correction followed by pointer withdrawal. Failed qualification/retention leaves sources intact.

The synthetic fresh-process workflow and normalized destination comparison pass. Python 3.9
syntax and JSON syntax pass; no Python 3.9 runtime run is claimed. Legacy Desk and Work example
output matches the pre-follow-up renderer byte for byte except for the experimental version
in the footer. The qualified Desk example and shared Work example reproduce from their sources.

The [three-level Desk](../decision-levels/desk.html), rendered unmodified from its JSON source,
was inspected in Codex's in-app browser at its desktop viewport: the shared Decide section
contains Work, Initiative, and Portfolio labels, with a total of three pending decisions.
This is local synthetic UI proof, not a migration of an operational board. No mobile or other
browser qualification is claimed. Static link/anchor and whitespace checks accompany the release.

Architect review: one ruling retains one owner and record; a level label grants no authority.
The opt-in strict check leaves older standalone adopters valid, and closed historical levels
are not fabricated. The helper guards cooperating writers, not hostile edits or real approvals.
Tester review: the named scenarios above address the board, closure, rejection, and history
claims. These are explicit review passes in the same session, not independent review or live
integration acceptance. Remote publication proof is recorded separately under `VEL-WI-8`.

The following foundation results remain as dated evidence, not the final prerelease test count.

## Foundation qualification

Local verification on 2026-09-21: macOS 26.6.2, Python 3.14.6. The shared support declares
Python 3.9+ compatibility; this run did not exercise every supported interpreter version.

| Scope | Disposition | Evidence / limitation |
| --- | --- | --- |
| Local POSIX file contract | Tested locally; 17 tests passed | `python3 -m unittest discover -s tests -v`: fresh processes, stale/concurrent writes, retries, interrupted coupled updates, divergent recovery, view failures, export and mapping negatives. |
| Local synthetic workflow | Tested locally | `examples/portable-records/demo.py`: Desk ask, linked work, synthetic answer in a fresh process, export, exact destination-fixture comparison. |
| TODO adoption | Synthetic example and local test | The source snapshot is retained unchanged; unstated owner/date remain unconfirmed and the historical checkbox remains operator-reported. This is a reviewed fixture mapping, not a general TODO parser. |
| Standalone HTML | Observed locally in Codex's in-app browser | At the default desktop viewport, the synthetic Desk displayed answered CK-1 and zero pending asks; the Work Board displayed committed WI-1, unconfirmed backlog WI-2, and operator-reported historical WI-3. Both pages were readable. Automated checks also compare rendered bytes and empty views. No mobile or other-browser claim. |
| Static compatibility and documentation | Checked locally | Both existing example HTML files reproduce unchanged; JSON syntax, Python 3.9 syntax, 137 local Markdown links, and `git diff --check` pass. Syntax compatibility is not a Python 3.9 runtime test. |
| AI-tool change with fresh session discovery | Not qualified | No two-provider/model workflow has been run. CLI processes are not AI agents. |
| Role/approval enforcement | Project responsibility; not qualified by this helper | Actor/authority fields are attribution. No actual protected host/service boundary is supplied or tested here. |
| External tracker read/write and cutover | Not qualified | No destination connector or live import is supplied. `snapshot_verified` is a local normalized-record comparison. |
| Evidence attachments, control execution, and tracker restoration | Not qualified | JSON export preserves references/metadata, not linked files, schedulers, or remote service history. Project rehearsal required. |
| Windows, shared/network/cloud-synced filesystem, distributed writers | Not qualified | Guarded helper uses local POSIX locks. |

Remaining owner choices: first external destination and pilot project. Qualification must name
the actual AI tools/models, pinned support, access/authority boundary, destination and versions,
source/destination revisions, and observable scenario results. Release claims must stay within
the tested scope. The Desk/Work templates remain usable independently of the guarded helper.

## Architecture review

The 17 local tests were rerun and passed for the decision-context/Markdown-contract additions
on 2026-09-21. The JSON helper and renderer code are unchanged by that tranche. The separate
[decision walkthrough](../decision-levels/README.md) records documentary scenario review and
Velocity's own scoped Markdown adoption. It does not add a Markdown parser/renderer or extend
the live integration qualifications above.

Reviewed on 2026-09-21 as a named Architect responsibility within the implementation session,
as permitted by Role Authority. This records design review, not independent acceptance.

- Record authority stays with the project and its named roles. Actor metadata cannot grant
  authority, and changing a model or display cannot create a new authoritative queue.
- Both source revisions govern a write. A retry retains its operation identity; a coupled
  change saves the Desk first and retains a recoverable journal. Divergence stops recovery.
- View receipts bind the source, configuration, tool revision, and generated bytes. A changed
  mode/binding invalidates the old receipt, and external mode rejects local Work updates.
- Handoff comparison preserves every normalized field and JSON value type. Export creates a
  new snapshot without replacing an existing one. Remote provenance and recovery remain
  destination integration obligations.
- Ordinary Markdown, JSON, and HTML remain readable without the originating session. Local
  POSIX locks coordinate cooperating writers; stronger access controls belong to the host or
  service, and broader filesystem/provider support requires its own evidence.
