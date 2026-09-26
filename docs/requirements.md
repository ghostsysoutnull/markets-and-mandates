---
title: Product requirements
intro: Trace the intended experience to observable behavior, with unresolved choices kept explicit.
permalink: /requirements/
---

**On this page**

* Contents
{:toc}

## Product purpose

The player leads a nation's executive, changes economic arrangements, and learns how institutions and actors translate intentions into uneven, delayed outcomes. The game must support both strategic decisions and explanations that can be inspected without interrupting every action. The accepted concept is in [The game]({{ '/game/' | relative_url }}).

The requirements below turn that concept into proposed acceptance contracts. They do not approve every implementation detail or establish numerical economic effects. Requirement IDs remain stable when wording improves; retired IDs stay in the history.

## Player journeys and acceptance

| ID | Journey or behavior | Observable acceptance |
| --- | --- | --- |
| R01 | Start a campaign | Show nation, observation year, institutional limits, scenario version, and disclosed model simplifications before starting. Never substitute unsourced values for missing data. |
| R02 | Read the annual briefing | Show period, mandate, outstanding commitments, material changes, and uncertainties; provide optional actor and household detail. |
| R03 | Develop a policy | Show objective, authority route, current and future costs, funding, resources, affected groups, timing, and alternatives before commitment. Editing a draft does not alter the economy. |
| R04 | Face institutional limits | Reject unauthorized commands with a reason and an available route where one exists. An independent institution remains a separate decision-maker. |
| R05 | Negotiate consequential terms | Show the actor's request, motive, evidence, and feasible responses. Accepted amendments change the actual commitment and budget. Declining is a valid branch. |
| R06 | Advance time | Resolve each confirmed command once, retain ongoing obligations, and distinguish preparation, expenditure, and delivered capacity. Invalid state cannot overwrite the last valid save. |
| R07 | Understand outcomes | Every material reported effect references rule/event evidence, timing, affected groups, and uncertainty. Explain model causation without presenting it as a real-world forecast. |
| R08 | Resume interrupted play | Recover the last committed checkpoint and pending decision after reload. A storage failure is visible; a save is never declared successful before completion. |
| R09 | Play on a phone | All core decisions work with touch and keyboard; readable layout, focus, zoom, and status messages survive orientation and viewport changes. |
| R10 | Compare choices | Proposed replay feature: identical versioned starting state, commands, and random inputs reproduce results. Distinguish fixed external shocks from endogenous responses. |
| R11 | Finish or change government | Report the mandate and wider consequences; preserve obligations across leadership changes if the continuity proposal is accepted. No invented election schedule. |
| R12 | Inspect evidence | Historical facts, model assumptions, and simulation results carry different labels. Open a relevant source or assumption from a detail view. |
| R13 | Recover portable saves | Proposed export/import: validate versions and contents, preview campaign identity, preserve the existing save on failure, and avoid executing imported content. |
| R14 | Play offline | Optional proposal, not implied by accepted browser delivery: after an explicitly completed offline preparation, selected content and saves support a full turn without network access. First-ever offline load may be unavailable and must explain why. |

## Proposed first playable scope

**Accepted scope exclusion (25 September 2026):** no environmental challenges related to carbon emissions or climate change. This applies throughout the game, not only to the first slice. Exclude carbon/emissions accounting, carbon taxes or trading, emissions targets, decarbonisation mandates, climate-change events, and climate-related scores, rewards or penalties. These are excluded features, not a future expansion backlog.

An electricity slice may explore affordability, reliability, ownership, competition, investment, financing, fuel supply, construction and maintenance. Its alternatives must be assessed on those included mechanisms. Historical sources may discuss excluded subjects; disclose the model's boundary without treating historical policies as nonexistent. This decision does not settle unrelated local pollution or other environmental mechanics.

Recommend one researched nation, one starting date, one mandate, and a short repeatable sequence covering policy drafting, an actor or institutional response, delivery, an annual report, and save/resume. Include enough later time to observe at least one delayed obligation. The number of turns is a decision, not an estimate of development effort.

For the selected policy family, represent households, producers, a public budget, relevant financing, and the actual institution with authority. Keep unsupported actions visibly unavailable with an explanation, or omit them from this slice. Do not advertise all six nations as playable while only one has content.

The first slice needs a no-change branch and at least two meaningful policy alternatives. Each must have constraints and an explained outcome; there must be no hardcoded ideological winner. A simplified model should identify what it excludes and why.

## Decisions that research cannot make for the user

| ID | Decision | Status, recommendation and consequence | Dependencies |
| --- | --- | --- | --- |
| D1 | Phone-browser delivery via a web link | **Accepted:** the user selected option 1. Native app-store packaging is outside this scope. PWA installation and offline play are separate optional proposals. | Distribution channel resolved; exact supported browsers remain to be verified |
| D2 | Modular production project | **Accepted:** normal TypeScript project with multiple source files. The old single physical HTML output requirement is superseded. | Resolved; configure the chosen build in P4 |
| D3 | Research year and first playable nation | **2010 accepted for broad research across all six nations.** Select the first playable nation after comparing profiles. The 1 January institutional snapshot is a research convention; exact gameplay start and campaign duration remain open. | Broad P2a research authorized; playable nation still needed for P2b/P3 |
| D4 | First-slice policy family and depth? | Open. Broad nation research comes first and has no selected sector focus. Later choose one connected family with alternatives, an institutional encounter, and delayed effects. | Blocks focused P2b/P3, not broad P2a research |
| D5 | Turn length, initiative limits, campaign duration? | Retain annual reports; evaluate a bounded initiative budget. The earlier two-initiative/15-turn proposal remains unsettled. | Balancing and campaign acceptance |
| D6 | Succession and end conditions? | Continue across executives with mandate-specific assessment; define transitions for D3. | Full campaign release, not basic infrastructure |
| D7 | Historical or experimental events; fictional or real NPCs? | Versioned external events and fictional named actors grounded in evidence, with clear labels. | Content authoring and replay semantics |
| D8 | UI dependency choice? | Start with the semantic DOM/controller proposal; compare a component framework against the actual screen needs before locking it. | UI scaffold; domain work can proceed independently |

The user answered **phones only** and **normal TypeScript project with multiple source files**. The user subsequently selected **phone-browser delivery via a web link**, resolving D1 as well as D2. Recommendations are not user selections. Do not ask the user to reselect D1/D2 or repeat all remaining questions at every session: request only the next dependent decisions and keep settled answers here and in the decision log.

## Quality requirements and proposed budgets

Correctness, readable explanations, recovery, and accessibility take precedence over decorative motion. Target WCAG 2.2 AA as a proposed product acceptance level; automated scans alone cannot establish conformance. Details are in [interface]({{ '/interface/' | relative_url }}) and [verification]({{ '/verification/' | relative_url }}).

For the first performance experiment, propose initial critical compressed assets at or below 500 KiB excluding optional scenario packs, common interaction feedback within 100 ms, and a representative annual resolution within one second on the selected reference phone. These are project targets, not measured results or standards. Select actual hardware, browser, network conditions, scenario size, and sample count before declaring a pass; revise budgets with evidence and an ADR.

The browser matrix is also provisional: automated Chromium/WebKit tests configured for phone viewports, optional Firefox coverage where relevant, plus real Android Chrome and iOS Safari checks. Desktop machines may host development/test tooling; desktop gameplay is not a release target. Record exact supported versions at release. Support ordinary phone-browser play even when installation is unavailable. Native-store runtime testing is outside the selected delivery scope. No device coverage has been tested yet.

## Completion and change control

A feature is done when its required behavior, failure behavior, explanation, save compatibility, and applicable mobile checks pass. Report missing evidence explicitly. A requirements table or passing unit test does not prove the economic model is plausible or the game enjoyable.

Changes to a requirement link to its affected architecture, rule sheets, content, and tests. Changes to campaign promises require a product decision; changes to internal implementation may be recorded as reversible engineering decisions. The [backlog]({{ '/backlog/' | relative_url }}) maps these requirements to ordered work.
