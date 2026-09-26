---
title: Decisions & feedback
intro: A shared direction, a set of working proposals, and a short list of questions worth settling next.
permalink: /decisions/
---

## Established direction

- The project is called **Markets & Mandates**.
- It is an educational, turn-based nation simulation.
- The player selects a real nation and can steer its economic arrangements toward greater market coordination, greater state direction, or combinations.
- Modern national profiles are the primary historical focus, with interest in an earlier 1980s perspective.
- Central banks belong in the design.
- The player controls the executive leadership, with powers that depend on the nation and period.
- Lawmakers and courts are distinct actors; major policies can involve legislative bargaining and judicial review.
- Policy rates, private borrowing rates, and government financing costs are distinct, with contract and refinancing delays.
- Large corporations and private banks act as NPCs with their own objectives and responses.
- Domestic regulation and international trade decisions are core player tools, subject to national institutions and commitments.
- The specification should develop actor motives, player actions, constraints, consequences, and examples beyond an outline.
- The game targets **phones only**, as clarified by the user on 25 September 2026. Desktop gameplay is outside current scope.
- Use a normal **TypeScript project with multiple source files**, compiled to JavaScript, with **object-oriented design**. This supersedes the earlier single-file delivery constraint.
- Prepare researched development documentation and an efficient process across sessions before beginning implementation. Phone-browser delivery via a web link is accepted; native-store packaging is outside the selected scope.
- The user **aborted the interactive paper walkthrough**. It is not a prerequisite for subsequent work.
- Carbon-emissions and climate-change challenges are excluded throughout the game, including related policy tools, mandates, events and scoring. This is a scope exclusion, not a deferred feature.
- Research broad **2010 profiles for all six nations**, with one researcher per nation in two batches, before choosing the first playable nation and policy scope. No electricity or other sector focus is required for this research.

The detailed mechanisms in this notebook are an initial proposal for review. Positive reception of the concept does not settle every design choice below.

## Current campaign proposal

The user rejected a prototype, then selected option 1: draft a complete game design with recommended defaults for review. The [campaign design for review]({{ '/campaign-design/' | relative_url }}) is that deliverable. Its UK campaign, ten annual turns and three connected policy areas are **proposed**, not accepted. Approval to author the design is not authorization to implement it. Review this coherent package instead of restarting a questionnaire or broad research.

**Preferred:** adopt the proposed campaign direction and close its listed model inputs. **Alternative:** revise the parts of this design that do not match the intended game.

## Working proposals

| Proposal | Why it is attractive | What needs review |
| --- | --- | --- |
| Ten annual turns, 2010–2019 | Current complete-campaign recommendation; enough time for delayed effects | Awaiting review; replaces the older 15-turn recommendation |
| Two major initiatives per turn | Keeps choices readable and creates priorities | Whether this feels restrictive or artificial |
| Several policy dimensions | Represents mixed arrangements and sector differences | How much complexity players want to control |
| A small cast of visible actors plus broader groups | Gives corporations, banks, and institutions recognizable behavior without representing every business individually | Cast size, fictional or real identities, and how much information the player sees |
| Negotiated packages and ongoing commitments | Makes investment, trade, and reform unfold over time | How much bargaining and monitoring belongs in each turn |
| Rulemaking followed by enforcement and review | Connects regulation to capacity and actual compliance | How detailed legal and administrative processes should be |
| A chosen mandate | Supports different definitions of success | Which objectives make satisfying campaigns |
| Replay under comparable shocks | Makes policy comparisons educational | How much replay support belongs in the first game |
| Continue across successive executives | Preserves the educational campaign while mandates and coalitions change | Succession triggers, control of a successor agenda, and accountability for each administration |
| Institutions appear at consequential decisions | Makes political and legal limits meaningful without constant procedural management | Which votes and cases deserve player attention |

## Questions for the next discussion

Review the [campaign design for review]({{ '/campaign-design/' | relative_url }}) as a package: adopt its defaults, or identify the experience to change. It already recommends nation, scope, pacing, actor treatment, continuity and success tests. These are review choices, not seven unanswered questions delegated back to the user.

## Current development path

Use the [development specification]({{ '/development/' | relative_url }}) and P0–P9 [backlog]({{ '/backlog/' | relative_url }}). The documentation foundation is complete. Broad six-nation research is complete. Review the complete campaign proposal, finish the named dependent data and rules, then implement authorized production milestones toward the complete phone game.

The [requirements decision sheet]({{ '/requirements/' | relative_url }}) owns open delivery and first-slice questions. The [architecture records]({{ '/architecture/' | relative_url }}) distinguish accepted TypeScript/OO constraints from proposed libraries and boundaries. Research cannot silently accept a product preference.

A paper playthrough is no longer the selected route. The user also rejected a prototype deliverable. Review the complete specification and evaluate the actual game during implementation.

## What to defer

Detailed electoral simulation, military strategy, a full world economy, granular financial markets, elaborate technology trees, and the 1980s scenario can wait until the main experience works. Their relevant effects can still appear through carefully chosen constraints or events.

Deferring a full world simulation does not remove trade negotiation or partner responses. Deferring granular financial markets does not remove private-bank lending choices or distress. Simplification should preserve the mechanisms that make the player's choices meaningful.

Likewise, deferring detailed election campaigns and litigation procedure does not remove legislative bargaining, legal review, or changes of government. The first design should represent the authority and consequences clearly with a manageable number of encounters.

## Review workflow and next options

Each review handoff should provide concrete next-step options and explicitly mark the preferred option. A recommendation is an invitation to choose the next task, not a decision that silently settles an unresolved game rule.

The user replaced the walkthrough-first plan with researched development documentation. The [backlog and session plan]({{ '/backlog/' | relative_url }}) records P0–P9 and the aborted B1 for continuity. Preserve the accepted phone-only and modular TypeScript choices.

Defining campaign continuity and political consequences remains an open design task, not a settled decision. It must be resolved before implementing the corresponding campaign feature.

## Share feedback

Bring a page title and your thoughts back to the conversation, or [open a design-feedback issue](https://github.com/ghostsysoutnull/markets-and-mandates/issues/new?template=design-feedback.md).

Useful feedback includes:

- “I want to make this kind of decision.”
- “This gives the player too much or too little control.”
- “I do not understand why that consequence follows.”
- “This assumption seems biased or needs evidence.”
- “This is interesting, but too much for the first version.”

Accepted changes should update the relevant page. Record significant decisions below so future readers can distinguish a settled choice from an old proposal.

## Decision log

| Date | Decision |
| --- | --- |
| 2026-09-25 | Selected Markets & Mandates as the project name. |
| 2026-09-25 | Publish the concept draft on GitHub Pages for reading and feedback before game implementation. |
| 2026-09-25 | Include large corporations and private banks as active NPCs, with regulation and international trade among the player's tools. |
| 2026-09-25 | Expand the site as draft 0.2 with detailed actor and policy chapters and illustrative multi-turn scenarios. Exact mechanics remain proposals. |
| 2026-09-25 | Define the player as executive leadership and include legislative and judicial interactions. Continuing across successive governments is the preferred working proposal. |
| 2026-09-25 | Publish draft 0.3 with distinct interest rates, institutional authority, and a fourth worked example. Review handoffs will include next-step options and a stated preference. |
| 2026-09-25 | Prepare a durable session handover and record the latest three session options as backlog. The complete-turn walkthrough is selected next; nation research and implementation remain deferred. |
| 2026-09-25 | Aborted B1 without player decisions or outcomes; requested researched development documents for mobile/web, TypeScript/JavaScript, OO and an efficient multi-session process. |
| 2026-09-25 | Clarified phones only and a normal TypeScript project with multiple source files; superseded desktop targeting and the single physical HTML output constraint. Distribution was not yet selected at this checkpoint; resolved in the following entry. |
| 2026-09-25 | Selected option 1: phone-browser delivery via a web link (D1). Native app-store packaging is outside the selected scope; PWA installation and offline play are not implied by this choice. |
| 2026-09-25 | Selected a fresh session for the next nation-selection and research work (P1/P2). This option 1 does not select the earlier UK/2010 recommendation; nation and starting year remain open. |
| 2026-09-25 | Excluded all environmental challenges related to carbon emissions or climate change. Updated concepts, policy examples and research boundaries accordingly. The assistant's proposal to research six nations in two batches using 2010 and electricity remains unselected; the user requested suggestions and then set this exclusion. |
| 2026-09-25 | Selected option 1: broad 2010 profiles for all six nations, one researcher per nation in two batches, followed by choosing the first playable nation and policy scope. Supersedes the proposed electricity prerequisite. Authorizes this parallel research and its documentation, not six game implementations. |
| 2026-09-25 | Rejected a prototype and selected option 1: assistant drafts a complete campaign design for review, recommending defaults and identifying remaining decisions. This authorizes design documentation, not adoption of the UK/ten-turn/three-area proposal or game implementation. |
