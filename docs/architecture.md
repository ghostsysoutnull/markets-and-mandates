---
title: Object-oriented TypeScript architecture
intro: Give objects clear responsibilities, isolate the simulation, and keep implementation choices reversible.
permalink: /architecture/
---

**On this page**

* Contents
{:toc}

## Status and rationale

Phones only, modular TypeScript/JavaScript and OO are user requirements. The boundaries and tool choices below are **proposed engineering decisions**, not installed dependencies. TypeScript supports JavaScript classes and typed relationships; strict checking is available, but compile-time assertions do not validate imported data at runtime. Use [TypeScript classes](https://www.typescriptlang.org/docs/handbook/2/classes.html), [strict mode](https://www.typescriptlang.org/tsconfig/strict), and [type assertions](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions) as implementation references.

Use classes where identity, invariants, or lifecycle matter. Use immutable records for inputs, snapshots, reports, and content. Plain functions remain appropriate for arithmetic and transformations. OO does not require one class per statistic or an inheritance tree of nations.

## Boundaries and dependency direction

The proposed dependency direction is presentation → application → domain. Infrastructure implements ports defined by the application/domain and is connected at a composition root. The domain cannot import the DOM, IndexedDB, fetch, a UI framework, or a service worker. Browser adapters can change without rewriting economic rules.

| Layer | Proposed responsibility | Examples |
| --- | --- | --- |
| Domain | Valid state transitions, institution rules, accounting, actor decisions | `Campaign`, `Treasury`, `Commitment`, `DebtBook`, `AuthorityPolicy` |
| Application | Execute a use case, coordinate rules and checkpoint persistence | `GameSession`, `TurnResolver`, `DraftPolicy`, `ResolveEncounter` |
| Presentation | Screens, input drafts, accessible feedback, formatted read models | `BriefingController`, policy form, report view |
| Infrastructure | Storage, content loading, optional worker and delivery adapters | `IndexedDbSaveRepository`, `JsonContentRepository` |
| Content | Versioned scenario definitions and evidence references | Nation pack, policy catalogue, actor profiles, event definitions |

For the accepted modular project, the proposed source layout is `src/domain`, `src/application`, `src/presentation`, `src/infrastructure`, `src/content`, plus `tests` and `public`. Keep documentation under the existing `docs/`. This is a proposed layout, not directories already created.

## Object responsibilities

| Object or interface | Owns | Must not do |
| --- | --- | --- |
| `Campaign` | Campaign identity, period, phase, revision, validated aggregate snapshot | Directly draw screens or load files |
| `Treasury` | Budget reservations, authorized spending, cash postings and fiscal reports | Treat a guarantee ceiling as current cash expenditure |
| `Commitment` | Approved terms, milestones, disbursement limits and completion state | Erase liabilities when the player cancels future work |
| `DebtBook` | Principal, currency, maturity, fixed/variable terms, scheduled repricing | Reprice every existing loan with the latest policy rate |
| `Institution` with `AuthorityPolicy` | What this actor can decide and what route an action requires | Infer national powers from ownership or an ideology score |
| `ActorDecisionPolicy` | Rank feasible actor actions using objectives and visible information | Read hidden future shocks or manufacture missing resources |
| `TurnResolver` | Ordered phase execution and structured effects | Own every model formula or mutate live UI state |
| `GameSession` | Command validation, revision checking, commit coordination | Promise durability before the repository confirms a write |
| `ReportBuilder` | Read models derived from structured transition records | Invent causal explanations unsupported by emitted effects |
| `SaveRepository` | Atomic revision persistence, load and recovery contract | Resolve economic rules or render HTML |

Prefer composition: a bank has a balance sheet, lending policy, ownership arrangement, and regulatory obligations. Public and private variants share accounting but can have different objectives and authority. A nation supplies institutional and content data; avoid `China extends Country` or overrides that silently encode stereotypes.

Inject dependencies through constructors at the composition root. A general-purpose dependency injection container, plugin engine, or entity-component system is not justified by the current scope. Add one only after a concrete need and a recorded comparison.

## Command and effect contracts

Commands are serializable discriminated records. Each includes a campaign ID, unique command ID, expected revision, kind, and validated payload. Suggested kinds include `SubmitProposal`, `AnswerEncounter`, `WithdrawDraft`, and `AdvanceTurn`; exact payloads belong to the selected slice. The application returns either structured validation issues, a pending decision, or a committed revision with report references.

Policy previews execute against a copy or immutable projection. They must not spend money, consume live random draws, persist decisions, or claim precise forecasts unsupported by the model. A submitted proposal can be pending authorization; it is not automatically an enacted policy.

Effects include stable IDs, rule ID/version, phase, affected entities, units, before/after or delta, and explanation references. Store enough detail to audit the result. Use snapshots plus a command/effect journal for recovery and explanation; full event sourcing is not a requirement. Snapshots are authoritative checkpoints, and replay additionally requires compatible rules, content, and random state.

Use explicit result types for expected conditions such as insufficient authority, rejected import, stale revision, or failed save. Reserve exceptions for unexpected failures; catch them at an application boundary that preserves the last valid checkpoint.

## TypeScript conventions

Recommend `strict`, `noUncheckedIndexedAccess`, and explicit handling of optional data; evaluate `exactOptionalPropertyTypes` when defining schemas. Keep domain imports type-safe, prohibit unexplained `any`, and treat external input as `unknown` until validated. These are proposed project conventions; confirm flags against the pinned compiler when scaffolding.

Represent IDs, money, rates, and physical quantities with explicit types and constructors. Runtime bounds and units are still necessary. Separate DTOs from behavior: serialize data and rehydrate objects through validation, never depend on JSON preserving class methods or private fields.

Keep constructors cheap and free of I/O. Methods enforce local invariants; cross-entity transactions belong to the application/domain service coordinating them. Do not expose mutable internals for a view to change. A getter or snapshot should not offer a back door around authorization.

## Tool selection and alternatives

| Need | Recommendation | Alternative and tradeoff |
| --- | --- | --- |
| Development and build | Vite with strict TypeScript | Direct compiler and static modules reduce build dependencies but require separate asset/distribution work |
| UI | Semantic HTML/CSS with small controllers for the first slice | A component framework can simplify larger reactive screens but must earn its dependency and state complexity |
| Unit and contract tests | Vitest | Another runner is viable if it meets deterministic fixtures, TS integration, and CI requirements |
| Browser tests | Playwright | Manual-only testing misses reproducible regressions; real-device checks are still needed |
| Rendering | DOM for policy forms, tables and reports | Canvas/game engines need extra accessibility work; reconsider for a future spatial or animated interaction |
| Native distribution | Outside accepted phone-browser delivery scope | Capacitor remains a researched future alternative only if the user changes that scope |

Vite transpiles TypeScript without type checking; a production check must include a separate `tsc --noEmit` step. This is documented by [Vite](https://vite.dev/guide/features#typescript). Vitest provides test tooling integrated with Vite's configuration, while [Playwright emulates device parameters](https://playwright.dev/docs/emulation); that does not establish real-device coverage. [Capacitor](https://capacitorjs.com/docs) is a researched native alternative outside the selected phone-browser target.

A worker is an optimization candidate if turn processing blocks interaction under the measured budget. A [Web Worker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers) can exchange messages with the UI but cannot manipulate the DOM directly. Preserve the same serializable command/result boundary so it can be added without new economic semantics.

## Architecture decision records

| ADR | Status | Decision and reopening trigger |
| --- | --- | --- |
| A01 | Accepted constraint | TypeScript/JavaScript and OO, requested 25 September 2026 |
| A02 | Proposed | Domain isolated from browser adapters; reopen only with a demonstrated simpler design preserving testability |
| A03 | Proposed | Composition for actor behavior and nation institutions; avoid country inheritance |
| A04 | Accepted delivery constraints | Phones only, browser access via a web link, and modular TypeScript source (D1/D2). PWA installation and offline support remain optional proposals. |
| A05 | Proposed, D8 | DOM/controller UI and Vite/Vitest/Playwright toolchain; evaluate on actual first-slice screens |
| A06 | Proposed | Snapshots plus journals and versioned schemas; no full event-sourcing platform |
| A07 | Proposed | Main-thread resolver initially; worker only after profiling justifies it |

When accepting or replacing an ADR, record context, chosen option, alternatives, evidence, consequences, affected requirements, and migration implications. Pin actual package and runtime versions only after checking compatibility during the scaffold task. No package versions or performance claims have been validated by this document.
