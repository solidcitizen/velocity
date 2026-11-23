# Your First Hour With Velocity

For one person or a small team building software with an AI coding agent. In about an hour you make
one real change the Velocity way, without a reading list first. At the end:

- your agent knows the rules it works under
- one small change is built, and you have proof it does what you asked
- a short closeout says what was proven, what was not, and whether the target moved

The rest of the standard explains why each step is there. This page only gets you started.

## Before You Start

- A repository where you already work with an AI coding agent, with commands that build, test, and
  run it locally.
- One small real change whose effect a user can see: a bug fix or a small feature. Choose one you
  could explain in a single sentence.

## 1. Pin Velocity (5 minutes)

Add Velocity to your repository at a released version, never a moving branch. Use the latest tag
from the [releases page](https://github.com/solidcitizen/velocity/releases):

```sh
git submodule add https://github.com/solidcitizen/velocity.git vendor/velocity
git -C vendor/velocity checkout --detach <tag>
git add .gitmodules vendor/velocity
```

No submodules? Clone the tag instead. Both routes are in [Pin a Release](PROJECT-ADOPTION-GUIDE.md#pin-a-release).

## 2. Tell Your Agent (10 minutes)

Copy [`templates/AGENTS.fragment.md`](../templates/AGENTS.fragment.md) into the instruction file your
agent reads (often `AGENTS.md`). Under it, write your project's *overlay*. One line per item is
enough to start, and "none yet" is an honest answer:

```md
## This Project (Velocity overlay)
- Lanes and authority: repo and local only. Nothing touches staging or production.
- Commands: build `<cmd>`, test `<cmd>`, run `<cmd>`. No deploy command for agents.
- Production approval: only my sentence "Deploy <sha> to production." "Ship it" does not count.
- Proof harness: the test command, plus running the app locally and using it.
- Issues: numbered ISSUE-1, ISSUE-2, … in docs/issues.md, Minimal profile by default;
  Standard for anything touching data or security.
- Branches: `<your naming>`. One branch per change.
- Roles: I am Operator, Coordinator, and Tester. The building agent is Fixer.
- Cadence: none; changes are taken one at a time.
- Incidents: stop and tell me.
- Local exceptions to Velocity: none.
```

Each line answers one of the [overlay requirements](PROJECT-ADOPTION-GUIDE.md#overlay-requirements).
Grow the answers as the project needs them.

## 3. Frame The Change Before Any Code (10 minutes)

Write the target down before the agent starts, in your words. This is the step that keeps the agent
from quietly testing what it built instead of what you asked for. Start a file from the
[tranche template](../templates/tranche-template.md) and fill in at least:

```md
- Goal: Saving a profile with an empty name shows "Name is required" and keeps the form.
- Lane: local implementation
- Mode: Patching
- Done: the behavior below works in the running app, and existing tests still pass.
- Proof class: A (a user-visible scenario)
- Acceptance criteria:
  - Empty name, press Save: the message appears, the other fields keep their values.
  - Valid name, press Save: saves as before.
- Proof mapping: each criterion above is shown by running it in the app, not only by a unit test.
- Authority owner: me
```

The acceptance criteria and the proof mapping are yours. The agent may propose a change to them.
It does not make that change itself.

## 4. Let The Agent Build (20 minutes)

Hand the agent the tranche. Within it the agent owns the code and its own tests. It works under
four rules:

- Stay inside the scope. Bigger ideas are proposals, not extra work.
- Propose, never apply, a change to the goal, the acceptance criteria, or the proof mapping. If the
  target looks wrong, the agent stops and says why.
- Claim only what its lane proves. Local proof is not staging or production proof.
- Report what it ran and what it saw, not a summary of success.

## 5. Accept It Wearing A Different Hat (10 minutes)

Switch from directing to checking. Do not accept the agent's summary as proof.

- Run each acceptance scenario yourself in the running app. Or start a separate agent session, tell
  it that it is the Tester, and give it the tranche alone, without the builder's notes.
- The agent's unit tests are *mechanism* proof: useful, but they show the parts work, not that the
  user sees the right thing. The scenario you ran is the *scenario* proof.
- Check whether the acceptance criteria or the proof mapping changed during the work, and who agreed.

Implementation and acceptance are separate moments even when one person does both. See
[Scaling The Role Split](PROJECT-ADOPTION-GUIDE.md#scaling-the-role-split).

## 6. Close It Out (5 minutes)

Fill the closeout section of the tranche, and add the two lines on target changes that
[the closeout requirement](ARTIFACT-AUTHORITY-BOUNDARIES.md#closeout-requirement) asks for:

```md
## Closeout
- Original invariant/operator sentence: Saving a profile with an empty name shows "Name is required" and keeps the form.
- Scenario proof: ran both criteria in the local app; screenshots attached.
- Supporting mechanism proof: two new unit tests on the validator.
- Missing proof: none at local lane; not verified on staging.
- Acceptance criteria or proof mapping changed: no.
- Authority for any change: none needed; the target is mine and did not move.
- Branch disposition: ready for PR
- Process-change disposition: none
```

If you could not run the scenario, write that under *Missing proof* and do not call the work done.
Work without its scenario proof is not behavior-proven.

## What You Just Practiced

- **Shared context, separated write authority.** The agent saw everything but changed only what it
  owns. The target stayed yours.
- **Proof matched to the claim.** A user-visible claim needed a user-visible scenario, not only a
  passing unit test.
- **Doing and accepting are separate moments.** You switched hats before you accepted.

## Next

- When something breaks, record it with the [issue record](../templates/issue-record-template.md)
  (its *Minimal signal* profile is enough at first).
- When you have a quiet hour, read the Delivery documents in this order:
  [Artifact Authority Boundaries](ARTIFACT-AUTHORITY-BOUNDARIES.md),
  [Role Authority](ROLE-AUTHORITY.md), [Proof Model](PROOF-MODEL.md),
  [Lifecycle Model](LIFECYCLE-MODEL.md), [Branch Hygiene](BRANCH-HYGIENE.md).
- When an agent's output starts reaching places you would otherwise check by hand, read
  [Choose Your Scope](PROJECT-ADOPTION-GUIDE.md#choose-your-scope).
- Questions or something unclear: open a
  [GitHub issue](https://github.com/solidcitizen/velocity/issues/new/choose). That is where the
  standard is maintained.
