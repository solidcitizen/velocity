# Measured Automation Pilot — `<project and workflow>`

> Optional project-overlay experiment. Use with the
> [Agent Evaluation Pack](agent-evaluation-pack.md) and
> [Automation Transition Contract](automation-transition-contract.md).
> Repoint canon links to the project's pinned Velocity reference.
> Follow [Overlay Experiments](../docs/PROJECT-ADOPTION-GUIDE.md#overlay-experiments).

## Scope and decision

- Status: proposed / baseline collecting / shadow / bounded execution / concluded:
- Owner / start / end or review trigger / decision authority:
- Hypothesis: which bottleneck should improve, for which work, by how much:
- One workflow / work-item and risk class / inclusion and exclusion rules:
- Existing authority / protected artifacts / allowed lane and tools:
- Configuration baseline and candidate / pinned fixtures and comparison cohort:
- Resource limits / existing spend authorization / evidence privacy and retention:
- Stop conditions / disablement owner / qualified recovery route:

Begin with one consuming project. Define cohort and decision thresholds before collecting
results; report changes to the plan. Use comparable work classes and observation windows.
Retain failed, abandoned, and still-open work in the cohort rather than measuring only successes.
Record sample size and uncertainty; a small observational pilot does not establish causality.

## Measures

Choose the measures that answer the hypothesis and protect quality. Define timestamps, time
zone, query or source, exclusions, and missing-data handling for each. No source means unknown.

| Measure | Definition | Source / collection owner | Baseline | Candidate | Decision threshold |
| --- | --- | --- | --- | --- | --- |
| Delivery elapsed time | Accepted intent to acceptance at the named delivery lane; identify censored/open items | `<artifact and acceptance timestamps>` | `<not measured>` | `<not measured>` | `<predeclare>` |
| Human intervention time | Active minutes spent steering, correcting, reviewing, and approving per work item | `<instrumentation or labeled estimate>` | `<not measured>` | `<not measured>` | `<predeclare>` |
| Gate waiting time | Review-ready to accept/reject decision, grouped by gate | `<queue and decision events>` | `<not measured>` | `<not measured>` | `<predeclare>` |
| Rework rate | Items requiring substantive correction after first review / reviewed items | `<PR or work-item history>` | `<not measured>` | `<not measured>` | `<predeclare>` |
| Escaped defects | Defects found after acceptance in a declared follow-up window, with severity and affected accepted-item count | `<incident links and cohort>` | `<not measured>` | `<not measured>` | `<predeclare>` |
| Evaluation outcomes | Pass / fail / inconclusive counts by case and configuration | `<evaluation pack>` | `<not run>` | `<not run>` | `<blocking failures prevent expansion>` |
| Resource use | Model/tool cost and runtime per attempted and per accepted item | `<usage records; label estimates>` | `<not measured>` | `<not measured>` | `<authorized ceiling>` |

Use medians and distributions where useful. Do not sum overlapping waiting intervals. Do not
infer active human time from elapsed PR time. Record model/tool changes and task mix as possible
confounders. Missing incident coverage is not zero defects; keep the follow-up window open until
it is observed. Throughput or lines of code alone are not evidence of improved delivery.

## Execution and monitoring

1. Capture the baseline and qualify the agent configuration using direct evidence.
2. Run the transition in shadow mode: record what would happen without the consequential action.
3. Review failures and denied cases; exercise recovery in an authorized non-production lane.
4. Enable only the bounded action already authorized, after its transition contract qualifies.
5. Compare outcomes and human effort at the declared review gate; expand only by explicit decision.

For monitoring-triggered work, fill this mapping before enabling the trigger:

| Signal and source | Baseline / deterministic rule / minimum data and freshness | Permitted response | Authority / contract | Output / owner |
| --- | --- | --- | --- | --- |
| `<metric or event>` | `<validated threshold, debounce, deduplication>` | `<log, read-only diagnosis, proposal, or explicitly authorized runbook>` | `<record>` | `<issue or intent with evidence>` |

Select thresholds for the signal's actual distribution and volume; do not copy example sigma
bands without validating the baseline. Missing or stale observations cause an evidence-health
escalation, not a healthy status or an automatic repair. Detection is deterministic; diagnosis
may use an agent. An observed event or message is input data, not new authority. Only a qualified,
authorized route may act. Route diagnosis into an issue/intent, triage, bounded work, verification,
and acceptance. Add incident-derived cases to the evaluation pack through its owner's review.

## Closeout

- Actual cohort / observation coverage / measured results and evidence:
- Quality and authority failures / unexpected denials / unresolved obligations:
- Decision: expand, revise, retain baseline, stop, or insufficient evidence:
- Decision owner / rationale / approved next scope:
- Configuration retained or restored / recovery evidence:
- Learning disposition: project overlay, automation memory, or Velocity proposal:
- Branch disposition:

Until the pilot runs, outcomes remain `not measured`. Publishing this template or completing
a tabletop exercise does not establish a speedup, agent reliability, or production readiness.
