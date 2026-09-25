---
title: Backlog & session plan
intro: Develop in small verified steps, preserving decisions and exposing the dependencies that remain.
permalink: /backlog/
---

## Current direction

The user aborted the interactive paper walkthrough on 25 September 2026 and requested the documents needed to develop the game with researched decisions, TypeScript/JavaScript, object-oriented architecture and an efficient process across sessions. Subsequent clarification: **phones only; a normal TypeScript project with multiple source files**. Desktop gameplay and the single-file output requirement are superseded.

Phone browser versus app-store distribution remains open. The documentation package is the current task; its existence does not authorize arbitrary game implementation or invent the missing economic model.

## Work queue

| Packet | Result | Status / dependencies |
| --- | --- | --- |
| P0 | Development documentation package and researched technical baseline | In progress — chapters and local consistency checks complete; publication/live verification pending |
| P1 | First-slice decision record | Next — resolve D1 and D3–D8 only as needed; D2 already accepted |
| P2 | One sourced nation/year and authority map | Blocked on D3 and model scope from D4 |
| P3 | Explicit first-slice rules, accounting and fixtures | Blocked on D4/D5 and required P2 inputs |
| P4 | Modular TypeScript scaffold and verification commands | Future implementation; needs authorized scope, A05/D8 and compatible tool versions |
| P5 | Deterministic domain slice | Future implementation; needs P3/P4 |
| P6 | Durable saves, import/export and recovery | Future implementation; needs domain schema and delivery decision |
| P7 | Phone interface connected to the slice | Future implementation; needs P1/P5 and persistence contract |
| P8 | Model, usability and device evaluation | Future verification; needs integrated P5–P7 |
| P9 | First playable release | Future; needs chosen distribution, required evidence and compatibility/rollback plan |

Read [Development specification]({{ '/development/' | relative_url }}) for document ownership, [requirements]({{ '/requirements/' | relative_url }}) for decision IDs, and [workflow]({{ '/workflow/' | relative_url }}) for the packet format. Tasks below are substantive outputs, not placeholders for more planning.

## P0 — Development documentation foundation

**Objective:** Give subsequent sessions the product contracts, OO architecture, model/data requirements, phone interaction, save/release behavior, validation strategy, evidence and exact work sequence.

**Acceptance:** Current decisions agree across AGENTS, handover, overview, requirements and backlog; sources support technical claims; proposed mechanics are labeled; the aborted exercise is not a prerequisite; navigation and links work; publication is verified when complete. This does not claim the model or country content is implementation-ready.

**Validation:** Review the diff, search stale plan language, check links and navigation, commit/push documentation, wait for Pages, inspect actual live content. Record exact outcome in the handover.

## P1 — Select a coherent first slice

**Objective:** Resolve the decisions that determine the first playable result.

**Read:** Requirements D1–D8, architecture ADRs, game concepts.
**Output:** Accepted distribution path, one nation/year, one policy family and alternatives, bounded turn/campaign scope, actor/event treatment and chosen UI baseline. Preserve the settled phone-only/modular-TS decisions.
**Acceptance:** Every first-slice feature maps to a requirement and every excluded major subsystem has an explicit simplification. A successor or end-of-campaign feature has defined behavior before being included.
**Next action:** Obtain phone browser versus store preference; then ask for the first nation/year and policy focus in plain language. Do not resume the housing exercise.

The user may prefer to inspect the architecture before settling product scope. That review is a valid alternative, not a reason to silently choose the nation.

## P2 — Research the selected baseline

**Objective:** Produce a dated, sourced authority map and the smallest initial dataset needed for P3.
**Read:** Nations, data/content, government, interest rates and the relevant sector chapter.
**Output:** Evidence records, institutional routes, raw/derived definitions, limitations and rights to use the data.
**Acceptance:** Formal versus effective powers distinguished; values have observation periods and units; gaps block their dependent feature instead of becoming invented defaults. No parameter calibration claimed from a descriptive profile.

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
**Acceptance:** All required checks for the declared slice pass, actual live delivery works, saves survive the supported update path, and phone-device coverage is stated honestly. Native-store work is conditional on D1.

## Superseded and deferred work

| Earlier item | Disposition |
| --- | --- |
| B1: interactive annual-turn paper walkthrough | **Aborted by user.** No policy selected, no outcomes resolved. Do not resume or mark complete. |
| B2: focused nation research | Replaced by P2 after explicit nation/year selection |
| B3: implementation after design | Replaced by P4–P9 with concrete dependencies |
| Six-nation expansion, 1980s scenario, detailed electoral/military/world systems | Deferred until the first slice is evaluated |
| Full desktop experience, accounts, cloud sync, multiplayer, telemetry | Outside current accepted scope; add only through an explicit decision |

**Preferred next step after P0:** P1, settle the smallest set of dependent product choices. Alternative: review the proposed OO architecture before selecting the first simulation slice.
