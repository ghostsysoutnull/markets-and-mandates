---
title: Backlog & session plan
intro: Develop in small verified steps, preserving decisions and exposing the dependencies that remain.
permalink: /backlog/
---

## Current direction

The user aborted the interactive paper walkthrough on 25 September 2026 and requested the documents needed to develop the game with researched decisions, TypeScript/JavaScript, object-oriented architecture and an efficient process across sessions. Subsequent clarification: **phones only; a normal TypeScript project with multiple source files**. Desktop gameplay and the single-file output requirement are superseded.

**Phone-browser delivery via a web link is now accepted (D1).** The UK campaign and its three policy areas are now accepted, with 12 monthly turns/year over 2010–2019 (120 turns). PWA installation and offline play remain optional proposals. The documentation package does not authorize arbitrary game implementation or invent the missing economic model.

**Completed research packet:** the user selected broad 2010 profiles for all six nations, with one researcher per nation in two batches, before choosing the first playable nation and policy scope. No sector focus is required. This supersedes the proposed electricity prerequisite and splits P2 into broad research (P2a) and later focused model data (P2b). The [research hub]({{ '/nation-research/' | relative_url }}) owns the shared comparison; [HANDOVER.md](https://github.com/ghostsysoutnull/markets-and-mandates/blob/main/HANDOVER.md) records progress.

**Accepted scope change:** carbon-emissions and climate-change challenges are excluded throughout the game, including related policies, mandates, events and scoring. They are not deferred features. Electricity research, if selected, focuses on affordability, reliability, ownership, financing, investment, fuel supply and delivery constraints.

**Current work:** the user adopted the [campaign design]({{ '/campaign-design/' | relative_url }}) with 12 turns per year. Record acceptance and monthly contracts, then complete authorized P2b/P3 inputs. Broad research and campaign selection are settled; a prototype remains rejected.

## Work queue

| Packet | Result | Status / dependencies |
| --- | --- | --- |
| P0 | Development documentation package and researched technical baseline | Done — published draft 0.4; 24 live pages and 840 internal links/anchors verified |
| P1 | First-slice decision record | Campaign direction accepted — D3–D7 adopted with monthly timing; D8 technical choice remains open |
| P2a | Broad sourced 2010 profiles for all six nations and shared comparison | Done — six reviewed profiles and comparison published as draft 0.5; evidence below |
| P2b | Selected nation/policy baseline and model-ready authority map | In progress — UK and policy scope accepted; sourced inputs and authority ledger published incrementally |
| P3 | Explicit first-slice rules, accounting and fixtures | In progress — monthly rules and temporal/tax fixtures specified; integrated economic rules still require listed P2b inputs |
| P4 | Modular TypeScript scaffold and verification commands | Future implementation; needs authorized scope, A05/D8 and compatible tool versions |
| P5 | Deterministic domain slice | Future implementation; needs P3/P4 |
| P6 | Durable saves, import/export and recovery | Future implementation; needs domain schema; phone-browser delivery accepted |
| P7 | Phone interface connected to the slice | Future implementation; needs P1/P5 and persistence contract |
| P8 | Model, usability and device evaluation | Future verification; needs integrated P5–P7 |
| P9 | First playable release | Future phone-browser release; needs required evidence and compatibility/rollback plan |

Read [Development specification]({{ '/development/' | relative_url }}) for document ownership, [requirements]({{ '/requirements/' | relative_url }}) for decision IDs, and [workflow]({{ '/workflow/' | relative_url }}) for the packet format. Tasks below are substantive outputs, not placeholders for more planning.

## P0 — Development documentation foundation

**Objective:** Give subsequent sessions the product contracts, OO architecture, model/data requirements, phone interaction, save/release behavior, validation strategy, evidence and exact work sequence.

**Acceptance:** Current decisions agree across AGENTS, handover, overview, requirements and backlog; sources support technical claims; proposed mechanics are labeled; the aborted exercise is not a prerequisite; navigation and links work; publication is verified when complete. This does not claim the model or country content is implementation-ready.

**Completion evidence:** Commit `be68d69` published through successful Pages run [36184371335](https://github.com/ghostsysoutnull/markets-and-mandates/actions/runs/36184371335). Diff and local route checks passed. Live verification passed for 24 pages, 840 internal links/anchors, 24 page-source links, 24 feedback-link sets and the shared stylesheet. This verifies documentation publication, not model correctness or phone usability. The handover records the next task.

## P1 — Select a coherent first slice

**Objective:** Resolve the decisions that determine the first playable result.

**Read:** Requirements D1–D8, architecture ADRs, game concepts.
**Output:** Accepted distribution path, one nation/year, one policy family and alternatives, bounded turn/campaign scope, actor/event treatment and chosen UI baseline. Preserve the settled phone-browser, phone-only and modular-TS decisions.
**Acceptance:** Every first-slice feature maps to a requirement and every excluded major subsystem has an explicit simplification. A successor or end-of-campaign feature has defined behavior before being included.
**Next action:** complete adopted A–D model artifacts for the monthly UK campaign. P1 product direction is settled; no renewed adoption/nation question, prototype or interactive paper exercise is required.

**Bounded scope-update packet (25 September 2026):** remove carbon/climate gameplay proposals from concepts, policy examples and reports; apply the exclusion to requirements and research contracts; update decisions and handover. Acceptance requires consistent scope wording, valid documentation links, and verified publication. No game implementation or nation research is part of this update.

**Scope-update completion evidence:** done in commit `76b2973`, published through successful Pages run [36206310487](https://github.com/ghostsysoutnull/markets-and-mandates/actions/runs/36206310487). Diff checks and 77 local Liquid route/file references passed. Live verification passed for the changed scope wording, all 24 pages, 842 internal links/anchors, 24 source links, 24 feedback-link sets and the stylesheet. P1's remaining product choices are still open.

The user may prefer to inspect the architecture before settling product scope. That review is a valid alternative, not a reason to silently choose the nation.

## P1-design — Complete campaign proposal

**Objective:** specify a reviewable game from campaign start to ending, with recommended defaults rather than another list of unanswered questions.
**Original authorization:** draft design only. **Later decision:** the user adopted it with 12 turns per year. Prototype rejected.
**Output:** campaign chapter, economic rule inventory, phone screen sequence, consistent requirements/decisions/navigation and resumable handover.
**Acceptance:** actions, authority, actor motives, consequences, progression, ending and remaining numerical/legal inputs are explicit; no invented coefficients or simulated results; publication and links verified.
**Status:** done — design proposal published in `14f2fb4` through successful Pages run [36210726464](https://github.com/ghostsysoutnull/markets-and-mandates/actions/runs/36210726464). Local diff/navigation/structure checks passed (32 pages, 123 Liquid references). Live checks passed for 32 pages, 1,297 internal links/anchors, 32 source links, 32 feedback sets, stylesheet and comparison CSV; campaign/rule/interface content verified. This was the design-authoring checkpoint. The user subsequently adopted its direction with monthly timing; numerical completion and implementation are still uncompleted.
**Next:** carry the later acceptance into monthly timing and the authorized P2b/P3 inputs.


## P2a — Broad six-nation research

**Status:** done; explicitly selected and published 25 September 2026.
**Objective:** Give the user a sourced comparison of all six nations in 2010 before selecting a first playable nation or sector.
**Read:** Nations, data/content, government and interest rates; use the shared method in [Six nations in 2010]({{ '/nation-research/' | relative_url }}).
**Output:** Six substantial profiles, source registers, institutional routes, ownership/public-service/finance/trade descriptions, policy possibilities, data limits and a comparison. One researcher per nation, in two batches of three; parent handles integration and publication.
**Scope:** Research reference year 2010; institutional snapshot 1 January is an editorial convention. Later-year changes and retrospective statistics are labeled. No electricity focus, carbon/climate gameplay, first-nation selection or game implementation.
**Acceptance:** Every profile covers the shared questions, uses dated primary evidence, distinguishes formal powers from practice and historical facts from design hypotheses, and identifies feature-specific gaps. Parent performs a second review, checks cross-profile comparability, publishes and verifies the result. No calibrated baseline claimed.
**Completion evidence:** research commit `3dd2fd0`, successful Pages run [36209286984](https://github.com/ghostsysoutnull/markets-and-mandates/actions/runs/36209286984). All six profiles were self-reviewed and parent-reviewed, including China source-provenance and executive-role corrections. Three workers handled one nation at a time across two batches. Local checks passed for six profiles, 31 pages, 107 Liquid route/file references, table continuity and the 12 displayed WDI values. Live verification passed for 31 pages, 1,207 internal links/anchors, 31 page-source links, 31 feedback-link sets, the stylesheet and exact CSV content. No duplicate anchors or unrendered templates were found. These are research/documentation checks, not model, gameplay or device tests.
**Checkpoint:** broad research is complete. The UK and three campaign policy areas have since been selected; each profile names the narrower evidence gaps for P2b. Do not repeat broad research or require a sector before reading the comparison.

## P1-monthly / P3-time — Accepted timing and temporal specification

**Objective:** apply the user's “12 turns per year, option 1” consistently and make monthly timing reviewable and testable.
**Outputs:** accepted campaign/decision records; M01–M12 calendar, rates, flow/stock, fiscal, project, reporting and end rules; F01–F12 synthetic fixtures; 22 sourced tax/monetary/fiscal observations; ten concrete authority routes with remaining gaps.
**Validation:** `python3 scripts/verify_specification.py` checks documentation arithmetic, not an implemented economy. Publication/link evidence follows after deployment.
**Status:** monthly acceptance/temporal packet done — published in `aaf69ae` through successful Pages run [36212045962](https://github.com/ghostsysoutnull/markets-and-mandates/actions/runs/36212045962). Arithmetic and local diff/structure/navigation checks passed (34 pages, 151 Liquid references). Live checks passed for 34 pages, 1,473 internal links/anchors, 34 source/feedback sets, stylesheet and exact contents of three data artifacts. These are documentation/arithmetic checks, not a completed economic model. P2b/P3 as a whole remain in progress: the input ledger explicitly lists uncaptured accounts, legal details and behavioral evidence.
**Checkpoint:** continue public-account and household initialization under existing authorization; do not ask for another option-1 approval. Keep the next packet bounded and explain its concrete output before starting.

## P2b — Research the selected playable baseline

**Objective:** Produce the precise authority map and smallest reconciled initial dataset required by the selected policy rules.
**Dependencies:** P2a, D3 and D4 are satisfied. Use the [UK implementation input ledger]({{ '/uk-implementation-inputs/' | relative_url }}) for the exact remaining fields. No repeated broad research.
**Read:** Selected profile, data/content, government, interest rates and relevant policy chapters.
**Output:** Focused evidence records, institutional routes, raw/derived definitions, source rights and unresolved inputs.
**Acceptance:** Formal versus effective powers distinguished; every required value has period, unit and vintage; accounts reconcile; gaps block dependent features instead of becoming invented defaults. No causal parameter calibration inferred from descriptive statistics.

## P3 — Specify the economic slice

**Objective:** Turn selected concepts into unambiguous rules and independently checkable examples.
**Read:** Simulation, systems, actors and selected policy chapters.
**Output:** Numbered rule sheets, phase order, initialized reconciled state, funding/price/resource rules, actor objectives and information, parameter register, hand-calculated fixtures and failure branches.
**Acceptance:** No missing unit, counterpart, authority or magic bonus; two meaningful alternatives plus no-change baseline; at least one delayed obligation; report explanations follow structured effects. Synthetic fixtures are labeled.
**Important:** This is specification work. A task can be complete without claiming calibration; unresolved behavioral evidence must remain visible.

## P4 — Establish the development environment

**Objective:** Create the agreed modular TypeScript project and a reproducible verification path when implementation is authorized.
**Read:** Architecture, delivery, verification.
**Output:** Pinned compatible runtime/dependencies, lockfile, module boundaries, minimal entry point, type/lint/test/build scripts and CI.
**Acceptance:** Clean install and checks work; domain imports no browser APIs; production preview works at the chosen base path; documentation publication remains intact. Test the relevant contracts, not the scaffold's existence.
**Scope:** No invented game mechanics and no package installation during P0.

## P5 — Implement the domain slice

**Objective:** Resolve the specified policy/actor/institution sequence deterministically.
**Read:** Approved P3 rule sheets, simulation and architecture.
**Output:** Validated commands, rule effects, coherent ledgers, pending decisions and report data.
**Acceptance:** Matching fixtures, invariants, duplicate-command protection, deterministic replay under compatible versions, meaningful alternative outcomes. No UI-dependent state mutation.

## P6 — Implement persistence and recovery

**Objective:** Resume a campaign through reload and expected failures.
**Read:** Delivery, simulation transaction semantics.
**Output:** Save repository, migration/version policy, recovery and export/import.
**Acceptance:** Atomic revision checks, stale-tab protection, failed-save recovery, rejected bad imports, resumed pending encounter and no rerolled random outcomes. Validate on the selected phone browser/runtime.

## P7 — Deliver the phone interaction

**Objective:** Connect briefing, proposal, encounter, commitments and report to the domain.
**Read:** Interface, requirements R01–R09/R12 and applicable R13/R14.
**Output:** Usable narrow-screen flow with explanations, authority/funding visibility, touch/keyboard access and honest save states.
**Acceptance:** Core task at 320 CSS pixels and under zoom; accessibility/manual evidence; reload resumes correctly; the player can distinguish submission from enactment and spending from delivered capacity.
**Scope:** Desktop may serve as a developer test host, not an accepted player target.

## P8 — Evaluate the integrated slice

**Objective:** Find implementation defects, model weaknesses and confusing interactions before expansion.
**Read:** Verification and learning.
**Output:** Versioned alternative-policy experiments, sensitivity findings, actual phone observations and measured performance.
**Acceptance:** Record successes, failures and missing evidence separately. Fix required defects; revise model/UI documents with rationale. Do not infer real-world prediction accuracy from plausible game outputs.

## P9 — Release the smallest reviewed game

**Objective:** Publish a reproducible, recoverable playable artifact on the selected distribution channel.
**Read:** Delivery and verification.
**Output:** Release identity, compatible content/rules/save versions, license records, known limitations, deployment and rollback evidence.
**Acceptance:** All required checks for the declared slice pass, actual live delivery works, saves survive the supported update path, and phone-device coverage is stated honestly. Native-store work is outside the accepted delivery scope.

## Superseded and deferred work

| Earlier item | Disposition |
| --- | --- |
| B1: interactive annual-turn paper walkthrough | **Aborted by user.** No policy selected, no outcomes resolved. Do not resume or mark complete. |
| B2: focused nation research | Replaced by broad P2a and focused P2b under the accepted 2010 research plan |
| B3: implementation after design | Replaced by P4–P9 with concrete dependencies |
| Six-nation playable expansion, 1980s scenario, detailed electoral/military/world systems | Deferred until the first slice is evaluated; broad six-nation research is authorized now |
| Full desktop experience, accounts, cloud sync, multiplayer, telemetry | Outside current accepted scope; add only through an explicit decision |

**Preferred next work:** continue the already-authorized UK baseline, authority and economic rules, using the exact input ledger. **Alternative:** review the monthly interaction while independent input work continues. Do not ask again to adopt the campaign.
