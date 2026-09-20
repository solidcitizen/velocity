# Process Change Proposal — Entity Development Lifecycle: Board And Peer Exchange

- Proposal: extend Velocity's direction from a software delivery lifecycle to an entity
  development lifecycle, and add two optional reusable templates that consuming projects have
  already practiced under it: the Executive Check-in Board and the Peer Exchange.
- Status: Proposed; awaiting maintainer review. Builds on the Check-in Desk repeatability
  release (v1.7.0); sequencing is the maintainer's and the Velocity CPO's call.
- Date: 2026-09-19
- Mode: Process evolution
- Proposed version: v1.8.0 (minor)
- Source: the maintainer's request on 2026-09-19 to a private consuming project's delivery lead
  (a household-finance function) to "develop that view in a way that can be promoted to an
  enhanced template", widened the same evening: "it needs to be a EDLC (entity development life
  cycle) where that entity may be a product, a company, a human individual, a family, or even an
  AI agent analogy of these things", with the note that the framework must also be collaborative
  across projects and across AI vendors.
- Triggering evidence: three drifts observed across the maintainer's consuming projects in the
  week of 2026-09-14, all outside the substrate and all in the surfaces around it: (1) the
  Operator had no single place to see what was theirs to decide (closed by the Desk, v1.6.0);
  (2) the delivery lead's plan lived in a working file only the lead could read, so allocation
  and "what is on for next week" had no Operator-readable answer; (3) two projects sharing a
  storage host coordinated a multi-hour move across an operating-system upgrade through an
  unwritten protocol of notice, hold, read-back, and all-clear, with a file copy at a known path
  as the fallback when the live channel could not be trusted. The protocol held; it was never
  written down, and one of the two leads was an agent from a different vendor than the other
  project's earlier tooling.
- Affected control plane: Shared (role handoff requirements, issue capture mode) by reference;
  no rule in the Delivery or Automation planes changes.
- Affected protected artifacts: `templates/executive-checkin-board.md` (new),
  `templates/peer-exchange.md` (new), `docs/PROJECT-ADOPTION-GUIDE.md` (one new section, two
  optional overlay bullets, one list addition), `docs/INDEX.md` (three links).
- Other affected artifacts: `MANIFESTO.md` (one direction section), `LINEAGE-AND-ADJACENT-WORK.md`
  (one attribution subsection), `README.md` (one paragraph), `CHANGELOG.md` (one subsection inside
  the planned 1.7.0 block), `examples/entity-stewardship/README.md` (new, synthetic), this proposal.
- Proposed disposition: Velocity repo proposal; direction in the manifesto; reusable templates and
  adoption guidance; a synthetic example. No consuming-project migration is required.
- Authority owner: Mike, Velocity Maintainer. This proposal authorizes the branch and pull
  request; merge and release remain subject to explicit maintainer approval.
- Project-specific or reusable: reusable. The templates name no project, host, command, account,
  or person; the originating practice is described only here and in the lineage note as
  maintainer-reported private work.
- Compatibility risk: low, additive. No role, lane, proof class, authority boundary, or prior
  closeout changes. The Board embeds the Desk unchanged and is rendered from the Desk's own data
  file for that section; it is not a second operator page. The Peer Exchange adds obligations
  only between peers who adopt it.
- Rollout plan: practice in at least two consuming projects for one monthly cycle (a delivery
  function and a product) before any core-doc wording is proposed; renderers and schemas for the
  Board's own sections follow in a later proposal, built the way PR #10 built the Desk's, with
  the practiced instances as evidence.

## Evidence

- The Desk template (v1.6.0) generalized cleanly from one project's practice within a day and was
  adopted by five desks within the week; the maintainer's audit of those desks ruled that operator
  pages must not diverge per project and that gaps are proposals, not local variants (PR #10).
  The Board is designed under that ruling: one shape, the Desk embedded via its canonical renderer.
- The peer protocol was exercised end to end on 2026-09-19 between two consuming projects: a
  notice of a shared-host upgrade window with two reboots; a named hold (a backup selection that
  had to be observed, not inferred, after the upgrade); a partial all-clear scoped to the work
  whose holds were released on observed state, with the rest held; a read-back with basis labels once the
  maintainer signed in; a final all-clear. Every message cited an id on each side and had a file
  copy at a known path in the receiving project's record. One executing agent declined a
  hard-delete step on its own policy and left a resumable state with markers; a different agent
  resumed from the record. These are the exact behaviors the Peer Exchange contract requires.
- The earlier handoff from a different vendor's agent to the current delivery lead in the same
  project succeeded through the repository record alone (documents, queue, action log, evidence
  folders, scripts) and lost only what had lived in the prior agent's session context. That is
  the basis for the "record is the transport" rule.

## Proposed Text

The full text is in the branch: `templates/executive-checkin-board.md`,
`templates/peer-exchange.md`, the manifesto section "Direction: From Software Lifecycle To
Entity Lifecycle", the adoption-guide section "Entity Stewardship: Board And Peer Exchange",
and `examples/entity-stewardship/README.md`. The design points the maintainer is asked to rule
on:

1. **Entity, not product, as the thing governed.** The substrate (authority, proof, lanes,
   protected artifacts, process evolution) is unchanged; "entity" is an axis the way product
   lifecycle is an axis. A steward (the Operator) with purpose, obligations, resources, risks, a
   cadence, a record, and peers. The lifecycle of an entity: charter, operate, develop, review,
   evolve, transfer. Software delivery is one instance.
2. **The Board as the page around the Desk.** Five sections in check-in order (Desk, Initiatives,
   In progress, Planned, Done), three id families never renumbered, one source of record per
   section with the page derived from it, every work item tagged to exactly one initiative,
   initiatives owned by the Operator, Done citing its proof artifact in Velocity's terms without
   judging it, no ask outside the Desk, Desk data read-only to the Board with Board data in its
   own file and schema (terms set by the Velocity CPO session in review, 2026-09-19). Policy, not
   implementation: a project on an issue tracker satisfies it by mapping.
3. **The Peer Exchange as the third artifact family.** Desk for asks to an Operator, Handoff
   Packet for work inside an entity, Peer Exchange between entities. Five message types with
   required fields; the record is the transport and the channel an accelerator; a basis label on
   every fact; ids on both sides; notice before and all-clear after; holds released on observed state;
   no permission laundering; Operator decisions travel by Desk under Desk contract rule 8
   (the receiving lead files the ask on its own Desk citing the exchange record; the originating
   desk carries a pointer entry; nobody writes another entity's desk);
   any party may decline and must leave a resumable state; vendor-neutral by construction.
4. **What ships now versus later.** The Desk section of a Board is the Desk renderer's output.
   The Board's own four sections are hand-maintained Markdown from their records in this
   revision; a Board renderer and data schema are a follow-up proposal once practiced. Claims
   follow proof.
5. **Collaboration and vendor neutrality as a stated direction**, in the manifesto, with the
   evidence gate that both templates are practiced before they are called canon.

## Proof And Disposition

Checked by hand: every relative link in the two templates, the adoption-guide section, the
manifesto section, the example, and the index resolves within this repository; the templates
contain no project names, hosts, commands, accounts, amounts, or people; the example is
synthetic and says so. `git diff --check` clean. The branch is stacked on
`proposal/checkin-desk-repeatability` so the changelog carries one planned-1.7.0 block; if that
proposal ships first, this one becomes the next minor at the maintainer's stamping.

Branch: `proposal/entity-development-lifecycle`, prepared in an isolated worktree so the
maintainer's main checkout is untouched. Opened as a pull request for review; not merged.

## Decision

- Accepted:
- Rejected:
- Deferred:
- Owner: Mike, Velocity Maintainer
- Date:
