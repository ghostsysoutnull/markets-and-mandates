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
- The eventual game should be mobile-friendly and delivered as a single HTML and JavaScript page.
- Current work is on game concepts and documentation, before implementation.

The detailed mechanisms in this notebook are an initial proposal for review. Positive reception of the concept does not settle every design choice below.

## Working proposals

| Proposal | Why it is attractive | What needs review |
| --- | --- | --- |
| 15 annual turns from 2010 | A manageable recent historical window with room for delayed effects | Desired session length and preferred start date |
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

1. **Depth:** Should this feel like an accessible strategy game or a detailed economic sandbox? The current recommendation is accessible strategy with optional depth.
2. **Campaign continuity:** The player is the executive. Should play continue across successors as recommended, and how should changing mandates constrain the new agenda?
3. **History:** Recognizable historical shocks, a randomized world, or both?
4. **Success and failure:** Mandate-based assessment, survival pressure, or a campaign that always permits recovery?
5. **First playable scope:** Which two or three nations would provide the most interesting initial contrasts before expanding to the intended roster?
6. **NPC detail:** Fictional organizations grounded in history, or carefully researched real organizations? How many should be individually visible?
7. **Policy detail:** Authored policy packages, adjustable terms, or a mixture? How much of a trade deal or regulation should the player design?

These questions can be answered gradually. Feedback on a specific dilemma may be more useful than settling every rule in advance.

## Recommended path

### First: refine the player experience

With the executive role established, settle one annual turn, the outcome dashboard, and several representative dilemmas. Walk through a short paper scenario to check whether the choices feel meaningful and the explanations make sense.

### Then: define a focused first simulation

Retain enough of the economy to connect decisions to consequences: a few sectors and household groups, budgets, credit and central-bank responses, trade exposure, implementation delays, and distributional outcomes.

Include meaningful corporate and banking behavior, actual enforcement constraints, and at least one responding foreign partner. These are now part of the core concept, even if their first versions use a small cast and a limited action catalogue.

The full set of topics in this notebook is a design map. Some can initially be represented through simple constraints or events rather than detailed subsystems.

### Then: research and specify

Create sourced starting profiles, define the model's relationships, document disputed assumptions, and check whether the rules produce plausible behavior across different institutional arrangements.

### Later: prototype and compare

Build the smallest playable campaign that tests the core loop. Evaluate clarity, interesting tradeoffs, and unintended ideological bias before adding countries or deeper systems.

## What to defer

Detailed electoral simulation, military strategy, a full world economy, granular financial markets, elaborate technology trees, and the 1980s scenario can wait until the main experience works. Their relevant effects can still appear through carefully chosen constraints or events.

Deferring a full world simulation does not remove trade negotiation or partner responses. Deferring granular financial markets does not remove private-bank lending choices or distress. Simplification should preserve the mechanisms that make the player's choices meaningful.

Likewise, deferring detailed election campaigns and litigation procedure does not remove legislative bargaining, legal review, or changes of government. The first design should represent the authority and consequences clearly with a manageable number of encounters.

## Review workflow and next options

Each review handoff should provide concrete next-step options and explicitly mark the preferred option. A recommendation is an invitation to choose the next task, not a decision that silently settles an unresolved game rule.

1. **Walk through one complete annual turn — preferred.** Choose an illustrative nation setup, review a briefing, select initiatives, negotiate, and inspect the resulting report. This tests whether the growing set of systems remains playable.
2. **Define campaign continuity and political consequences.** Settle how leadership changes affect mandates, coalitions, and the player's choices.
3. **Research one starting nation.** Replace the profile template with a sourced, dated authority map and economic baseline.

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
