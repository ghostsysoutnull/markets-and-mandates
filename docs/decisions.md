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
- The eventual game should be mobile-friendly and delivered as a single HTML and JavaScript page.
- Current work is on game concepts and documentation, before implementation.

The detailed mechanisms in this notebook are an initial proposal for review. Positive reception of the concept does not settle every design choice below.

## Working proposals

| Proposal | Why it is attractive | What needs review |
| --- | --- | --- |
| 15 annual turns from 2010 | A manageable recent historical window with room for delayed effects | Desired session length and preferred start date |
| Two major initiatives per turn | Keeps choices readable and creates priorities | Whether this feels restrictive or artificial |
| Several policy dimensions | Represents mixed arrangements and sector differences | How much complexity players want to control |
| Actors respond independently | Gives institutions, firms, and households meaningful behavior | How much influence the player expects |
| A chosen mandate | Supports different definitions of success | Which objectives make satisfying campaigns |
| Replay under comparable shocks | Makes policy comparisons educational | How much replay support belongs in the first game |

## Questions for the next discussion

1. **Depth:** Should this feel like an accessible strategy game or a detailed economic sandbox? The current recommendation is accessible strategy with optional depth.
2. **Player identity:** A continuing national policy program, or a government that can lose office?
3. **History:** Recognizable historical shocks, a randomized world, or both?
4. **Success and failure:** Mandate-based assessment, survival pressure, or a campaign that always permits recovery?
5. **First playable scope:** Which two or three nations would provide the most interesting initial contrasts before expanding to the intended roster?

These questions can be answered gradually. Feedback on a specific dilemma may be more useful than settling every rule in advance.

## Recommended path

### First: refine the player experience

Agree on the role, one annual turn, the outcome dashboard, and several representative dilemmas. Walk through a short paper scenario to check whether the choices feel meaningful and the explanations make sense.

### Then: define a focused first simulation

Retain enough of the economy to connect decisions to consequences: a few sectors and household groups, budgets, credit and central-bank responses, trade exposure, implementation delays, and distributional outcomes.

The full set of topics in this notebook is a design map. Some can initially be represented through simple constraints or events rather than detailed subsystems.

### Then: research and specify

Create sourced starting profiles, define the model's relationships, document disputed assumptions, and check whether the rules produce plausible behavior across different institutional arrangements.

### Later: prototype and compare

Build the smallest playable campaign that tests the core loop. Evaluate clarity, interesting tradeoffs, and unintended ideological bias before adding countries or deeper systems.

## What to defer

Detailed electoral simulation, military strategy, a full world economy, granular financial markets, elaborate technology trees, and the 1980s scenario can wait until the main experience works. Their relevant effects can still appear through carefully chosen constraints or events.

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
