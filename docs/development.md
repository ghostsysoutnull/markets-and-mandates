---
title: Development specification
intro: The entry point for turning Markets & Mandates into a maintainable mobile and web game.
permalink: /development/
---

**On this page**

* Contents
{:toc}

## Current authority and status

On 25 September 2026 the user stopped the interactive walkthrough and requested the documentation needed to develop the game for phones (clarified from the initial mobile/web request), using JavaScript/TypeScript and object-oriented design, with research and an efficient process across sessions. This supersedes the previous walkthrough-first plan. No player policy was selected and no turn was completed.

**Accepted requirements:** phones only, a normal TypeScript project with multiple source files compiled to JavaScript, object-oriented architecture, research before unsupported decisions, and durable session continuity. Desktop gameplay is outside the target. Existing accepted game concepts remain in force.

**Proposed engineering baseline:** a modular TypeScript application, a deterministic simulation core, semantic HTML interface, browser persistence, and automated verification. Phone-browser versus app-store distribution, PWA installation, a UI framework and exact phone/browser support require decisions. The previous single physical HTML output constraint is superseded by the user's modular TypeScript choice.

This package supplies requirements, contracts, decision records, research, and an executable work sequence. It is not a claim that the economic model is calibrated or every product decision is settled. Unresolved dependencies are explicit so implementation does not silently choose them.

## Document ownership

| Document | Owns | Read when |
| --- | --- | --- |
| [Product requirements]({{ '/requirements/' | relative_url }}) | Scope, user journeys, requirement IDs, acceptance criteria | Selecting a feature or reviewing completion |
| [Architecture and decisions]({{ '/architecture/' | relative_url }}) | OO responsibilities, dependencies, proposed stack, ADRs | Changing modules or technical boundaries |
| [Simulation contract]({{ '/simulation/' | relative_url }}) | State transitions, ordering, accounting, reproducibility | Implementing any rule or turn processing |
| [Data and content]({{ '/data-content/' | relative_url }}) | Nation evidence, authored policies, schemas, versioning | Researching a nation or writing scenario content |
| [Mobile and web interface]({{ '/interface/' | relative_url }}) | Screens, interaction, accessibility, responsive behavior | Building or reviewing player-facing flows |
| [Persistence and delivery]({{ '/delivery/' | relative_url }}) | Saves, recovery, offline operation, releases | Touching storage, updates, or deployment |
| [Verification]({{ '/verification/' | relative_url }}) | Test strategy, model checks, release evidence | Planning acceptance tests or releasing |
| [Development research]({{ '/development-research/' | relative_url }}) | Sources, findings, limits, evidence gaps | Revisiting a technical or scientific claim |
| [Session workflow]({{ '/workflow/' | relative_url }}) | Small work packets, startup, checkpoints, handoffs | Every development session |
| [Backlog]({{ '/backlog/' | relative_url }}) | Ordered tasks, dependencies, completion state | Choosing the next packet |
| [Decisions]({{ '/decisions/' | relative_url }}) | Accepted product choices and outstanding questions | Changing scope or interpreting older concepts |

The original game, systems, actor, government, regulation, trade, interest-rate, nation, and learning chapters continue to own conceptual explanations. Engineering pages link to them rather than copying the full narrative. `HANDOVER.md` owns only the current checkpoint; it must not become a second specification.

## How to interpret a statement

Use **accepted** for a user decision; **proposed** for a recommendation; **verified** for a narrowly supported source claim; **illustrative** for invented examples; **open** for a dependency that still needs resolution. Research can establish what a platform supports, but cannot decide which experience the user wants. An implementation task can adopt a reversible engineering detail with a recorded rationale; it cannot quietly settle campaign rules or invent a nation's institutions.

## Readiness gates

| Gate | Evidence required | Current state |
| --- | --- | --- |
| Documentation foundation | Linked requirements, architecture, workflow, research, and work packets | Provided in draft 0.4; subject to review |
| First-slice definition | Distribution, initial nation/year, turn and campaign scope, UI approach | D2 resolved; remaining choices in D1 and D3–D8 |
| Model-ready slice | Versioned rule sheets, initialized state, funding and accounting, expected test outcomes | Not ready; dependencies in simulation and data chapters |
| Implementation-ready packet | Narrow objective, settled dependencies, affected contracts, acceptance checks | Use the workflow template; no game code yet |
| Playable release | Completed implementation plus browser, recovery, economic, usability, and deployment evidence | Not started |

Do not hold all work until every future expansion is specified. Resolve the dependencies of the next slice, then build and measure that slice when authorized. A framework-only scaffold is not evidence of a working economic game.

## Scope discipline

The full vision includes multiple real nations and interacting institutions. The recommended first slice uses one selected nation and a small authored policy catalogue, with other systems represented at the level needed to explain those policies. Nation selection is open. Housing is a candidate feature, not a selection inherited from the aborted exercise.

Accounts, cloud synchronization, multiplayer, native stores, analytics, monetization, and downloaded executable mods are not accepted requirements. Keep them outside the proposed first slice unless the user adds them. This reduces dependencies without denying future extensions.

## Material risks and their controls

| Risk | Control and evidence | Owning packet |
| --- | --- | --- |
| Scope grows to six unfinished nations | Select one researched slice and explicitly defer expansion | P1/P2 |
| Plausible prose hides missing model rules | Require units, ordering, ledgers, parameters and independently checkable fixtures | P3 |
| Ideology is encoded as an automatic bonus | Compare alternatives and symmetrical physical constraints across sensitivity runs | P3/P8 |
| Phone interruption loses decisions | Atomic checkpoints, saved encounters, import/export and actual-device recovery tests | P6/P8 |
| A new release breaks old campaigns | Version schemas, content and rules separately; test migration and rollback | P6/P9 |
| OO becomes unnecessary abstraction | Small responsibility-based classes, composition and tests against behavior | P4/P5 |
| Documentation drifts between sessions | One owning chapter per contract; update handover, backlog and decisions with the change | Every packet |
| Distribution adds unexpected native obligations | Settle phone-browser versus store delivery before its dependent implementation | P1/P9 |

**Preferred next step:** settle the first-slice decision sheet in [requirements]({{ '/requirements/' | relative_url }}), then research the selected nation and specify the initial rules. An alternative is to review the OO architecture first if its boundaries are the immediate concern.
