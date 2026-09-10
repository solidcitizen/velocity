# Agent Evaluation Pack — `<configuration change>`

> Optional template for evaluating the **development agent and its configuration**.
> Instantiate in the consuming project; repoint canon links to its pinned Velocity version.
> Product tests remain necessary. A passing agent evaluation grants no delivery or promotion
> authority; apply [Proof Model](../docs/PROOF-MODEL.md) and
> [Artifact Authority Boundaries](../docs/ARTIFACT-AUTHORITY-BOUNDARIES.md).

## Candidate and authority

- Owner / reviewer / decision date:
- Trigger: model, prompt, skill, hook, permission, runtime, or policy-adapter change:
- Baseline and candidate configuration revisions, including model identifier and settings:
- Pinned Velocity version / project overlay revision:
- Evaluation fixture revision / environment / permitted tools and writes:
- Budget: maximum runs, elapsed time, tokens or cost; authority for any spend:
- Evidence access / redaction / retention rules:

## Cases and acceptance

Use representative project tasks, prior incidents, and boundary cases. A small starter set is
useful for qualification; it is not evidence of broad reliability. Expand with real failures.
Record expected outcomes **before** running the candidate; protect fixtures, expected results,
graders, and thresholds from writes by the agent under evaluation. The authorized owner reviews
changes to those artifacts separately from the candidate's attempt to satisfy them.

| Case / provenance | Prompt and initial fixture | Expected outcome and forbidden action | Proof class / lane / direct check | Severity |
| --- | --- | --- | --- | --- |
| `<ID; real incident or synthetic>` | `<immutable input; clean start state>` | `<observable behavior, including correct escalation>` | `<tool evidence and checker>` | `<blocking or advisory>` |

Include successful authorized work as well as denied work: an agent that refuses everything
is not a useful pass. Exercise weakened acceptance criteria, stale evidence, missing authority,
missing telemetry, duplicate events, and recovery. Incident-derived cases preserve the original
operator scenario. See the [worked example](../examples/measured-automation/README.md).

- Trials per case / prompt variants / sampling settings:
- Baseline and candidate use the same fixture, tools, limits, and trial policy:
- Reset strategy: isolated checkout and fresh state per trial; no shared mutable fixture:
- Deterministic checks / any model-graded rubric / independent reviewer:
- Required coverage / blocking cases / acceptable quality and resource regression:
- Treatment of flaky, timed-out, skipped, or infrastructure-blocked runs:

Predeclare decision criteria. Report every attempted run; do not select the best of several
unreported retries. Record passes, failures, and inconclusive runs separately, with denominators.
An aggregate score cannot compensate for a blocking authority or acceptance failure. A model's
confidence score is supporting evidence, not permission or a replacement for required proof.

## Results and disposition

| Case / trial | Configuration revision | Outcome: pass / fail / inconclusive | Direct evidence | Duration / resource use | Finding / owner |
| --- | --- | --- | --- | --- | --- |
| `<ID>` | `<revision>` | `<observed result>` | `<logs, checks, trace, exact artifact>` | `<measured or unknown>` | `<disposition>` |

- Coverage and baseline-to-candidate differences, including failed and inconclusive trials:
- Proven capability / untested capability / limitations:
- Decision: accept candidate, revise, retain baseline, or evidence insufficient:
- Authorized decision owner / acceptance record:
- Rollback configuration / recovery check / outstanding obligations:
- Next evaluation trigger and owner:

An empty pack is `not run`, never green. A tabletop review supports a document-consistency claim;
only an execution with captured evidence can establish agent or runtime behavior. Run the pack
on relevant configuration changes, and on a project-chosen cadence where model or runtime drift
matters. Put the runner and CI integration in the project overlay, not Velocity core.
