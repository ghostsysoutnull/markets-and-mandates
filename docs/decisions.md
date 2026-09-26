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

The current campaign direction is explicitly adopted below. Detailed numerical and technical proposals remain labeled separately.

## Accepted campaign and timing

The user selected **option 1: adopt the design**, with **12 turns per year**. The [campaign design]({{ '/campaign-design/' | relative_url }}) now specifies UK, January 2010–December 2019, **120 monthly turns**, income/employment, enterprises and England housing. Executive continuity, counterfactual future, deterministic composite commercial actors, mandate assessment, saves and replay are adopted directions. Numerical/legal implementation details still need completion.

The annual budget and two major reforms per calendar year are retained while routine decisions and consequences resolve monthly. This is the stated pacing interpretation of the timing amendment. Do not silently multiply annual resources or initiative opportunities by twelve.

| Choice | Status | Remaining work |
| --- | --- | --- |
| UK opening and three policy areas | Accepted | Reconciled January inputs and exact package authority |
| Twelve turns per year for ten years | Accepted: 120 monthly turns | Implement clock, saves and monthly resolution against M01–M12 |
| Budget and major initiatives | Annual fiscal authority; retain two major reforms/year | Monthly management, dated fiscal rules and pacing evaluation |
| Composite firms/banks and real institutions | Accepted direction | Balance sheets, motives, legal boundaries and behavioral evidence |
| Mandates, continuity and recovery | Accepted direction | Fixed metric definitions, successor procedure and tested end conditions |
| Saves, export/import and comparable replay | In adopted campaign | Storage schema, recovery and reproducibility implementation |
| UI libraries, precise runtime/browser versions | Engineering proposals | Choose compatible versions when implementation is authorized |

## Next work

The user has already authorized completing starting data, authority routes and economic rules. [Monthly rules]({{ '/monthly-rules/' | relative_url }}) and [UK implementation inputs]({{ '/uk-implementation-inputs/' | relative_url }}) record progress and exact gaps. Do not ask again to adopt the design, select a nation or authorize that evidence work. This is not blanket authorization to skip dependencies or implement six campaigns.

## Current development path

Use the [development specification]({{ '/development/' | relative_url }}) and P0–P9 [backlog]({{ '/backlog/' | relative_url }}). The documentation foundation is complete. Broad six-nation research is complete. Complete the adopted campaign’s named dependent data and rules, then implement authorized production milestones toward the complete phone game.

The [requirements decision sheet]({{ '/requirements/' | relative_url }}) owns open delivery and first-slice questions. The [architecture records]({{ '/architecture/' | relative_url }}) distinguish accepted TypeScript/OO constraints from proposed libraries and boundaries. Research cannot silently accept a product preference.

A paper playthrough is no longer the selected route. The user also rejected a prototype deliverable. Review the complete specification and evaluate the actual game during implementation.

## What to defer

Detailed electoral simulation, military strategy, a full world economy, granular financial markets, elaborate technology trees, and the 1980s scenario can wait until the main experience works. Their relevant effects can still appear through carefully chosen constraints or events.

Deferring a full world simulation does not remove trade negotiation or partner responses. Deferring granular financial markets does not remove private-bank lending choices or distress. Simplification should preserve the mechanisms that make the player's choices meaningful.

Likewise, deferring detailed election campaigns and litigation procedure does not remove legislative bargaining, legal review, or changes of government. The first design should represent the authority and consequences clearly with a manageable number of encounters.

## Review workflow and next options

Each review handoff should provide concrete next-step options and explicitly mark the preferred option. A recommendation is an invitation to choose the next task, not a decision that silently settles an unresolved game rule.

The user replaced the walkthrough-first plan with researched development documentation. The [backlog and session plan]({{ '/backlog/' | relative_url }}) records P0–P9 and the aborted B1 for continuity. Preserve the accepted phone-only and modular TypeScript choices.

Executive continuity and recovery are accepted. The exact successor algorithm, authority deadlines and numerical political conditions still need their rule records before implementation.

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
| 2026-09-25 | Selected option 1 to adopt the UK campaign design, amended to 12 turns per year: monthly turns, 120 over 2010–2019. Authorized completing starting data, authority routes and economic rules. Preserve annual fiscal authority and the existing two-major-reforms-per-year pace as the explicit timing interpretation. Prototype remains rejected; no claim of completed numerical model or blanket game-code authorization. |
