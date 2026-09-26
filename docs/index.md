---
title: An economy you can reshape.
intro: Choose a real nation. Inherit its institutions. Discover what happens when you change who owns, decides, invests, and benefits.
permalink: /
---

**Markets & Mandates** is a proposed educational, turn-based strategy game about free markets, central planning, and the many arrangements between them.

You take responsibility for a nation's economic direction. You inherit strengths, dependencies, inequalities, and institutions. Over a series of years, you change policies, manage crises, and watch households, businesses, banks, and public agencies respond.

The question at the heart of the game is:

> Which decisions should individuals and businesses make, which should the state make, and how well can each carry them out?

## The design at a glance

| Element | Current direction |
| --- | --- |
| Experience | An accessible strategy game with optional deeper explanations |
| Player role | The nation's executive leadership: government and cabinet, subject to national institutions |
| Starting nations | United States, United Kingdom, Germany, Russia, China, and Japan |
| Main campaign | Proposed: 15 annual turns beginning in 2010, concluding in 2025 |
| Historical perspective | Modern profiles first; an optional 1980s scenario later |
| Main decisions | Ownership, allocation, competition, public services, redistribution, regulation, trade, and institutional reform |
| Excluded subject matter | Carbon-emissions and climate-change challenges, policies, events, and scoring |
| Active counterparts | Lawmakers, courts, central banks, corporations, private banks, public enterprises, worker groups, and foreign partners |
| Success | A chosen public mandate, assessed alongside its wider consequences |
| Intended delivery | Phones only; modular TypeScript/JavaScript with OO design. Phone-browser delivery via a web link is accepted. |
| Current stage | Researched development documentation, draft 0.4; no game implementation yet |

The premise and educational focus come from the initial discussion. Specific turn counts, dates, mechanics, and scope below are **working proposals**, not a finished or calibrated simulation.

## Development documentation

Start with the **[development specification]({{ '/development/' | relative_url }})** for requirements, OO architecture, simulation and data contracts, phone interface, saves, validation, research and the session workflow. Accepted requirements, technical proposals and unresolved product choices are labeled separately.

The interactive paper walkthrough was aborted at the user's request. The next work follows the [development backlog]({{ '/backlog/' | relative_url }}); no paper playthrough is a prerequisite. The existing concept chapters below remain the game's design foundation.

## Read the concept

1. **[The game]({{ '/game/' | relative_url }})** — Your role, the yearly turn, decisions, outcomes, and a sample dilemma.
2. **[The executive, lawmakers & courts]({{ '/government/' | relative_url }})** — Executive powers, legislative bargaining, judicial review, and changes of government.
3. **[Economic systems]({{ '/systems/' | relative_url }})** — Credit, production, households, institutions, and transitions.
4. **[Interest rates & monetary choices]({{ '/interest-rates/' | relative_url }})** — Who sets which rates, how debt reprices, and tensions with the executive.
5. **[Corporations & banks]({{ '/actors/' | relative_url }})** — NPC objectives, investment and lending decisions, negotiation, and public enterprises.
6. **[Regulation & enforcement]({{ '/regulation/' | relative_url }})** — Rules the player can propose, who enforces them, and how actors adapt.
7. **[Trade & the international economy]({{ '/trade/' | relative_url }})** — Tariffs, agreements, industrial support, dependencies, and foreign responses.
8. **[Worked examples]({{ '/scenarios/' | relative_url }})** — Four multi-turn walkthroughs connecting decisions, NPC reactions, and consequences.
9. **[Nations & history]({{ '/nations/' | relative_url }})** — How real countries become distinct, historically grounded starting positions.
10. **[Learning through play]({{ '/learning/' | relative_url }})** — Explanations, experiments, and the limits of the model.
11. **[Decisions & feedback]({{ '/decisions/' | relative_url }})** — The choices still open and a suggested path toward a focused first game.
12. **[Sources]({{ '/sources/' | relative_url }})** — Initial institutional references and the research still required.

For a concrete sense of play, start with the [worked examples]({{ '/scenarios/' | relative_url }}). They are illustrative branches, not predictions or implemented mechanics.

## What changed in draft 0.4

The project now has a researched development documentation package and explicit work packets for future sessions. Phones only, modular TypeScript source and object-oriented design are accepted constraints. Nation baselines, quantitative rules, toolchain implementation and real-device tests remain future work. The documents expose these dependencies rather than treating them as settled.

## Earlier concept draft 0.3

The player is now explicitly the executive leadership. New chapters describe legislative bargaining, judicial review, distinct interest rates, and the preferred proposal for continuing across successive governments. A fourth worked example follows a housing program through a vote, a legal challenge, and changing financing conditions.

This builds on draft 0.2's corporate and banking NPCs, regulation, trade decisions, enforcement, and multi-turn examples. Campaign succession details and country-specific institutional rules still need decisions and research.

The overview remains short. Detailed actor behavior, policy catalogues, examples, and open choices live in the linked chapters. Country statistics and calibrated policy effects still require research; greater detail should not be confused with validation.

## Why this could work

Economic policy creates interesting strategy when immediate relief, long-term capacity, distribution, and political feasibility pull in different directions. Real nations give those choices context. Replaying decisions can turn an abstract argument into an experiment the player understands.

The main risk is scope. A simulation that attempts everything can become difficult to explain and exhausting to play. The design should retain a few important decisions each year while letting the underlying actors and constraints produce meaningful consequences.

The other risk is false authority. A plausible simulation is still a model with assumptions. Historical facts, debated mechanisms, and invented gameplay rules must remain distinguishable.

## How to review

Read whichever chapter interests you, then bring its title and your comments back to our conversation. GitHub issues are also available through the feedback button on every page. The most useful feedback identifies an experience you want: a dilemma you want to face, a concept you want to understand, or a rule that feels unconvincing.

The [backlog and session plan]({{ '/backlog/' | relative_url }}) records the development work packets and their dependencies. A complete [session handover](https://github.com/ghostsysoutnull/markets-and-mandates/blob/main/HANDOVER.md) preserves the project context for a fresh conversation.
