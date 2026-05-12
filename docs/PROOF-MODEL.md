# Proof Model

Velocity requires proof to be explicit, comparable, and mapped to the claim being made.

## Core Rule

No change may be marked complete or green without explicitly stating its proof class coverage.

Lower-order proof may not silently substitute for higher-order proof.

For operator-reported workflow defects, implementation-mechanism proof may not substitute for acceptance proof. The first regression proof should replay the operator's reported workflow sentence from observable start state to expected observable outcome.

## Proof Classes

### Class A - Scenario / Browser / End-User Proof

Proves:

- UI behavior and rendering
- user interaction flows
- enabled and disabled states
- end-to-end wiring across visible surfaces
- operator usability and affordances

For workflow claims, Class A must be scenario-shaped.

### Class B - HTTP / API / Runtime Contract Proof

Proves:

- server behavior and sequencing
- status transitions and API contracts
- data mutations observable via API
- coordination behavior visible at runtime

### Class C - Logs / Database / Trace Proof

Proves:

- internal state transitions
- execution traces
- data-level correctness
- migration or repair effects

### Class D - Code Reasoning / Static Proof

Proves intended logic only.

Class D is not sufficient on its own.

## Minimum Proof by Claim

| Claim type | Minimum proof |
| --- | --- |
| UI, product, or operator behavior | Class A |
| Workflow requirement | Scenario-shaped Class A |
| Server/control-plane/sequencing behavior | Class B |
| Data repair or migration result | Class C plus lane-appropriate runtime proof |
| End-to-end system behavior | Class A plus Class B |
| Architecture intent only | Class D may support design, but not behavioral completion |

## V-Model Mapping

Use the V-model to map requirement level to proof level:

| Requirement level | Proof level |
| --- | --- |
| Operator sentence / user workflow | scenario acceptance proof |
| Cross-component system contract | system/API/runtime proof |
| Component behavior | integration proof |
| Mechanism or helper behavior | unit/static/design proof |

Mechanism proof cannot close a workflow requirement.

Example:

- Requirement: `switch to main -> logout -> login -> main is selected`
- Scenario proof: browser switches list through the UI, logs out, logs in, and asserts `main` is selected.
- Mechanism proof only: preseed recent-list storage and assert boot selection.

## Proof Mapping

Every closeout should include:

```md
Proof mapping:
- <invariant or operator sentence> -> <direct test/check/evidence>
- <unmapped invariant> -> residual / blocked
```

Do not describe SHA, health, or DB identity proof as behavior validation. Those are deployment or environment proof, not operator-behavior proof.

