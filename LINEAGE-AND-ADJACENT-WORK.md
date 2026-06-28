# Lineage And Adjacent Work

> This document is positioning, not policy. It explains where Velocity sits relative to adjacent work; it defines no authority boundary, proof obligation, or lifecycle rule.

Velocity is not an agent framework. It is a method-level governance framework for AI-assisted software delivery.

Agent frameworks answer questions such as:

- how agents call tools
- how agents hand off work
- how state moves through a graph or workflow
- how guardrails, tracing, memory, and retries are implemented
- how multiple agents or subagents are orchestrated

Velocity answers different questions:

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

Those patterns are useful, but they do not by themselves define SDLC authority. A workflow graph can route from Fixer to Tester, but it does not automatically answer whether Fixer is allowed to rewrite the acceptance criteria, whether a unit test can close an operator workflow claim, or whether prompt/process changes belong in the delivery branch.

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
- evaluation metrics such as benchmark scores or judge-model rubrics
- tracing, telemetry, or observability infrastructure
- planning cadence, estimation, or roadmap process

Those belong to the project overlay, the chosen toolchain, or the team's delivery method.

## Positioning Rule

Velocity does not compete with agent frameworks. It sits above them.

An agent framework may execute the workflow. Velocity defines the authority boundaries, proof obligations, lifecycle state, and process-change rules that keep the workflow trustworthy.
