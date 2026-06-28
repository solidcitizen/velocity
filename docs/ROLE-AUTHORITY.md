# Role Authority

Velocity uses specialized roles. A project may implement them as separate sessions, agents, or named responsibilities inside one session.

## Operator

Owns:

- mission and priority
- risk tolerance
- go/no-go decisions
- production mutation approval unless explicitly delegated
- acceptance of architecture-significant tradeoffs

Should not be used as a transport layer between specialist roles.

## Coordinator

Owns:

- issue and tranche state
- role assignment
- handoff packet normalization
- stale evidence detection
- branch disposition tracking
- ensuring required fields exist before the next role begins
- routing architecture questions to Architect
- creating review packs when the operator needs product-facing readout

Must not:

- invent architecture direction
- approve production mutations
- substitute chat summary for formal issue records
- bury operator decisions inside long narrative updates
- rewrite lifecycle policy during ordinary delivery work

## Fixer

Owns:

- bounded implementation
- code and test changes
- implementation-supporting docs
- internal verification within the authorized lane
- producing proof packs that make a tranche review-ready

Must not:

- rewrite issue evidence into a more convenient story
- silently broaden scope into architecture change
- claim staging, host-qualified, or production truth from repo/local proof
- directly change Velocity lifecycle policy while fixing product work

## Tester

Owns:

- independent acceptance-oriented validation
- scenario selection for operator-behavior checks
- runtime observation in meaningful validation lanes
- repro tightening when acceptance fails
- final evidence capture for acceptance disposition

Must not:

- collapse observed behavior into root cause without evidence
- rewrite the requirement to fit observed behavior
- act as the default owner of routine local proof that belongs to Fixer
- directly change Velocity lifecycle policy while validating product work

## Architect

Owns:

- invariants
- trust boundaries
- semantic ownership
- durable system contracts
- proof contracts when requirements and implementation layers diverge

Must review work that changes:

- architecture contracts
- authority boundaries
- replay/retry semantics
- durable status truth
- operator-facing state contracts
- lifecycle proof rules

## Process Reviewer

Owns:

- pattern detection across recent work
- recommendations for better skills, prompts, templates, and process
- distinction between memory-only learning and policy-worthy learning

Must not:

- mutate project delivery policy without explicit delegation
- mutate Velocity lifecycle policy directly unless also acting under Velocity Maintainer authority

## Velocity Maintainer

Owns:

- reusable lifecycle policy
- governance rules for this repo
- template evolution
- release/version decisions for consuming projects

Must keep project-specific rules out of the core method unless they generalize.

## Criticality Does Not Grant Mutation Authority

`Critical`, `urgent`, `prod fix`, `production issue`, `ready`, and similar urgency or destination words describe priority, interrupt level, and target relevance. They do not grant authority to mutate production or any other protected live environment. This operationalizes the Operator's `production mutation approval unless explicitly delegated` and the [Lifecycle Model](LIFECYCLE-MODEL.md) `Promotion mode` (live or higher-lane mutation has been *explicitly* approved) on the `promotion` lane: it names what counts, and what does not count, as that explicit approval.

Critical work authorizes the delivery roles to:

- interrupt lower-priority work
- isolate the issue or tranche
- prepare a bounded fix
- run authorized local, staging, and read-only verification
- prepare a promotion candidate
- state the exact production approval needed

Critical work does not authorize:

- production deployment
- workflow dispatch that mutates production
- host-local production recovery deploy
- production database mutation
- provider-side mutation
- secret rotation
- destructive reset or cleanup
- bypassing a project promotion lane

Production mutation requires an explicit operator approval sentence that names the action or an accepted equivalent, such as:

- `Promote this to production.`
- `Deploy SHA <sha> to production.`
- `Run the production promotion workflow for <ref>.`

The following are not sufficient approval:

- `critical`
- `prod fix`
- `production issue`
- `ready`
- `ship it`, unless the project overlay explicitly defines it as production-promotion approval
- prior promotion approval in another tranche
- production being quiescent
- successful staging proof
- the presence of a deploy script or workflow

After staging or host-qualified proof, the default closeout state is the promotion-readiness disposition (see [Branch Hygiene](BRANCH-HYGIENE.md) and [Lifecycle Model](LIFECYCLE-MODEL.md) `Promotion mode`): *Ready for production promotion; awaiting explicit operator approval.*

If an agent is technically capable of production mutation but lacks explicit approval, the correct result is the `Blocked` disposition (see [Handoff Packet](../templates/handoff-packet.md) `Disposition`) with the reason *missing production-mutation authority* — not improvisation.

