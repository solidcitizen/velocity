# Lineage And Adjacent Work

> This document is positioning, not policy. It explains where Velocity sits relative to adjacent work; it defines no authority boundary, proof obligation, or lifecycle rule.

Velocity is a method-level governance framework for AI-assisted software delivery. It can be
used with agent runtimes and with other delivery methods after their authority rules are mapped.

Agent frameworks answer questions such as:

- how agents call tools
- how agents hand off work
- how state moves through a graph or workflow
- how guardrails, tracing, memory, and retries are implemented
- how multiple agents or subagents are orchestrated

Velocity concentrates on these questions, which some newer playbooks and methods also address:

- who may change the requirement, acceptance criteria, proof mapping, architecture decision, or lifecycle rule
- what proof class is required for the claim being made
- which lane can support the closeout claim
- when a fluent agent pass must stop instead of absorbing another role
- whether a change belongs in product delivery, project overlay, ADR, automation memory, or reusable lifecycle policy

Velocity can be implemented with a manual checklist, a coding-agent session, OpenAI Agents SDK, LangGraph, CrewAI, Microsoft Agent Framework, Claude-style subagents, or a custom workflow engine. The runtime is replaceable. The authority model is the point.

## Adjacent Agent Work

Velocity intentionally overlaps with common agent patterns:

- specialist agents and subagents
- orchestrator-worker routing
- plan-then-execute workflows
- evaluator-optimizer or judge/critic loops
- handoff packets and shared state
- guardrails and human-in-the-loop checkpoints

Those patterns are useful, but their presence alone does not establish compatible SDLC authority.
A workflow graph can route from Fixer to Tester; its actual rules must still specify whether the
Fixer may rewrite acceptance criteria, whether a unit test can close a workflow claim, and who
accepts prompt/process changes. Compare documented mechanisms, not just role names.

## Imported Lineage

Velocity borrows deliberately from older software and governance traditions:

- ADRs for durable architecture decisions
- V-model thinking for mapping requirement level to proof level
- separation of duties from security, accounting, and audit practice
- change-control discipline for protected lifecycle rules
- SRE and platform-engineering lane discipline for local, staging, host-qualified, and promotion claims
- branch hygiene as a control surface for delivery state

Velocity does not claim novelty for these pieces. Its contribution is integrating them for one human working with fluent agents, where the main failure is not lack of automation but loss of role separation.

## What Velocity Does Not Provide

Velocity does not provide:

- a runnable agent runtime
- prompt orchestration code
- model selection rules
- subagent communication protocols
- a universal benchmark, project-specific graders, or measured performance guarantees
- tracing, telemetry, or observability infrastructure
- planning cadence, estimation, or roadmap process

Those belong to the project overlay, the chosen toolchain, or the team's delivery method.
Velocity v1.4.0 adds optional evaluation and measurement templates, not an execution engine.

## Development History And Historical Claims

Velocity was created to capture practices developed in the founder's own AI-assisted work
(owner account, 2026-09-09). The repository's first commit, `5dba1cc` (2026-05-11), and
[ADR-0001](adrs/0001-independent-lifecycle-repo.md) document extraction of an existing
product-embedded method into an independent lifecycle repository. They establish the date of
that extraction, not the beginning of the underlying practices or a claim of historical priority.
The manifesto entered this repository on 2026-06-27 in `77f286a`.

Earlier manifesto language described the gap in absolute terms, including claims that nobody
else addressed it. The founder suggests this may have reflected the landscape as understood
during initial development. Preserve that context in history without turning it into an
unverified assertion that Velocity was first. The reviewed public record contains earlier
related work:

| Dated primary source | What the date establishes |
| --- | --- |
| [AWS AI-DLC introduction](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/), 2025-07-31 | A published AI-centered lifecycle with human decisions and persistent artifacts predates Velocity's repository extraction. |
| [GitHub Spec Kit introduction](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/), 2025-09-02 | A published specification-driven agent workflow predates that extraction. |
| [OpenAI harness engineering](https://openai.com/index/harness-engineering/), 2026-02-11 | A published account of mechanically enforced architecture and agent feedback loops predates that extraction. |

These dates establish related prior publications, not identity with Velocity's complete method,
influence on its author, or a first-ever claim for any framework. The original start date of the
founder's practices remains unestablished by this repository. Current positioning rests on
Velocity's integration and usefulness rather than exclusivity.

## Comparison Reviewed 2026-09-09

This is a bounded review of first-party documentation, not an exhaustive market survey or an
execution benchmark. The comparison column is Velocity's analysis of the cited sources. A
described feature is not proof it is enforced in a particular installation. Living documentation
can change; the date above is the observation date. Do not backdate current features to a
framework's introduction. The Anthropic course pages reviewed do not establish a publication
date, so this record does not assign one.

| Playbook or framework / primary sources | Relevant documented practice | Implication for Velocity |
| --- | --- | --- |
| **Anthropic AI-Native SDLC Playbook** — [artifact flow](https://academy.claude.com/courses/ai-native-sdlc-playbook/introduction), [agent evals](https://academy.claude.com/courses/ai-native-sdlc-playbook/continuous-evals-in-ci), [hooks](https://academy.claude.com/courses/ai-native-sdlc-playbook/hooks-as-approval-gates), [maintenance](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-the-loop-on-metrics) | Accepted artifacts trigger subsequent stages; configuration changes get agent evaluations; deterministic controls bound actions; monitoring feeds new work. Detailed [PR review](https://academy.claude.com/courses/ai-native-sdlc-playbook/ai-in-the-pr-review-loop) and [deployment](https://academy.claude.com/courses/ai-native-sdlc-playbook/ci-cd-integration-and-deployment) plays retain human approval. | Strong convergence on governed automation. Adopt evaluation and transition templates and measured feedback loops. Preserve Velocity's claim-specific proof and artifact ownership. A hook example still needs complete route coverage and qualification. |
| **AWS AI-DLC Workflows** — [repository](https://github.com/awslabs/aidlc-workflows), [current README](https://raw.githubusercontent.com/awslabs/aidlc-workflows/main/README.md) | A harness-neutral method and deterministic engine, multiple workflow profiles, human gates, persistent state, and source-bound review evidence. | A close peer spanning methodology and execution, not merely a tool runtime. Learn from workflow qualification and adapters. Map approval ownership and proof semantics before combining methods; do not import its role count or cadence as Velocity policy. |
| **GitHub Spec Kit** — [repository and workflow](https://github.com/github/spec-kit) | Constitution, specification, plan, tasks, implementation, and convergence; cross-artifact analysis and reusable presets/extensions. | Useful intent-to-plan structure and consistency checks. Map the constitution's amendment authority to Velocity's protected artifacts. Synchronizing a spec to code cannot authorize weakening the original acceptance criteria. Tool-agnostic operation is shared ground. |
| **BMad Method** — [overview](https://docs.bmad-method.org/), [review](https://docs.bmad-method.org/build/review-a-change/), [autonomous loops](https://docs.bmad-method.org/build/autonomous-development-loops/) | Scoped unattended workers, explicit terminal state, immutable intent blocks, layered independent review, and a separate orchestration responsibility. | Strong overlap with bounded tranches and role separation. Borrow inspectable handoff state and recovery records. Map deferred findings to named successor obligations under Velocity; a generic deferred list cannot close a touched load-bearing invariant. |
| **Kiro specifications** — [specs](https://kiro.dev/docs/specs/) | Requirements or bug analysis, design, and task artifacts; feature and bugfix paths; dependency-aware task execution. | A useful implementation of intent refinement and task tracking. Map spec acceptance to the project authority model; task completion or a quick generation mode does not establish scenario acceptance or authorize promotion. |
| **Superpowers** — [method and workflow](https://github.com/obra/superpowers), [README](https://raw.githubusercontent.com/obra/superpowers/main/README.md) | Composable skills for design, isolated worktrees, small plans, test-first development, spec-compliance and code-quality review, and branch closeout. | A practical delivery adapter with substantial overlap. Preserve Velocity's lane and protected-artifact semantics; its universal test-first prescription is not adopted as a new Velocity requirement for every kind of artifact. |
| **OpenAI harness engineering** — [engineering account](https://openai.com/index/harness-engineering/) | Short repository entry instructions, navigable knowledge, agent-visible feedback, and structural enforcement. It also describes a throughput-oriented approach with minimal blocking merge gates. | Learn from executable constraints and context maintenance. Treat the merge policy and reported performance as context-specific experience; any reduced gate must fit a project's explicit authority, risk, and recovery contract. This is an experience report, not a portable conformance standard. |

## What This Review Changes

### Attribution For The September Additions

Anthropic's playbook directly prompted the September review and informed the new support
for development-agent evaluations, accepted-artifact handoffs, and measurement feedback.
These are adaptations with attribution, not claims that Velocity originated those practices.
The other methods above supplied comparisons and compatibility checks; their publication
does not establish influence on Velocity's earlier work.

In particular, the `intent.md` → `spec.md` → `plan.md` artifact convention is described in
[Anthropic's introduction](https://academy.claude.com/courses/ai-native-sdlc-playbook/introduction).
The v1.4.0 adoption section carried those filenames into Velocity without attribution beside
them. The v1.5.0 clarification removes that convention from the adoption guidance and uses
Velocity's established Capture, Decision, Tranche, and issue-record vocabulary. This is a
provenance correction, not a renamed import or a claim that recording requirements is novel.

The three optional templates apply the reviewed automation ideas to Velocity's existing
artifact owners, claim-specific proof, lane boundaries, and recovery obligations. They are
not copies of Anthropic's plays and do not reproduce its artifact convention.

The shared direction is artifact-based work, executable feedback, explicit agent configuration,
and bounded autonomy. Those ideas are increasingly represented across delivery methods.
Velocity's useful contribution is the combination of protected acceptance criteria, proof
matched to claims and lanes, enforcement of touched invariants, and separately governed process
evolution. None of these comparisons proves exclusive ownership of that combination.

Velocity v1.4.0 translates the review into three optional reusable supports:

- [Agent Evaluation Pack](templates/agent-evaluation-pack.md): compare the development agent's
  configuration against protected expected outcomes, including incidents and denied actions.
- [Automation Transition Contract](templates/automation-transition-contract.md): bind an
  accepted artifact revision, evidence, and existing authority to a bounded next action.
- [Measured Pilot](templates/automation-pilot.md): establish a baseline and observe delivery,
  human effort, quality, and resource use before widening automation.

Qualification fixtures, actual skills/hooks, monitoring thresholds, and installations belong
in consuming projects. The [synthetic example](examples/measured-automation/README.md) supplies
starting cases, not measured success. Retain the existing source of truth for each artifact
when adopting an adjacent method; do not create two independently editable rulebooks.

Refresh this comparison when evaluating a new adapter, changing authority policy, or preparing
a release whose positioning depends on it. Recheck the specific feature and source before
claiming equivalence, superiority, historical priority, or measured gains.

## Positioning Rule

Velocity can govern work executed through different runtimes and can overlap with other full
delivery methods. Combining them requires an explicit authority and artifact mapping. Evaluate
Velocity by whether its proof and governance improve trustworthy delivery at an acceptable
cost in human attention, rather than by whether another framework uses similar vocabulary.
