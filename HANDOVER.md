# Markets & Mandates — session handover

Updated 25 September 2026. Read AGENTS.md first, then this file and docs/backlog.md. The current user overrides older plans.

## Current objective and accepted changes

The user **aborted the interactive walkthrough** and requested all necessary development documentation, researched rather than assumed, for mobile/web with JavaScript/TypeScript, OO and an efficient process across sessions.

Latest explicit answers:
- **Phones only.** Desktop gameplay is not a product target.
- **Normal TypeScript project with multiple source files.** The older single physical HTML output constraint is superseded.
- **Phone-browser delivery via a web link.** The user selected option 1. Do not ask this choice again. Native app-store packaging is outside the selected scope; installation/offline support remain proposals.
- **Carbon-emissions and climate-change challenges excluded throughout the game.** No related accounting, policy tools, mandates, events, scores or hidden rewards/penalties. This is not deferred expansion work. Other environmental topics are not selected by this decision.
- **Complete game design requested; prototype rejected.** Latest option 1 authorizes drafting a coherent campaign design with recommended defaults for review. It does not approve those defaults or game implementation.
- **Broad 2010 research accepted.** The earlier research option 1 selected broad profiles for all six nations, one researcher per nation in two batches, before choosing the first playable nation and policy family. No sector focus is required. This supersedes the electricity prerequisite, and explicitly authorizes these sub-agents. 1 January 2010 is the shared editorial institutional snapshot, not a selected exact gameplay start date.

Do not resume the paper exercise or ask the user to choose housing option B. No nation, mandate, policy or outcome was selected in that exercise. It is aborted, not completed.

## Current work and exact next action

**P0 — development documentation foundation is complete.** Nine new engineering/product chapters plus a development hub are published with primary-source research, requirements, OO boundaries, model/data contracts, phone UX, saves, tests and session workflow. No game implementation, dependency installation or quantitative calibration has been produced. Broad nation research is now published and verified under P2a.

Verification: documentation commit `be68d69`; Pages run `36184371335` succeeded. Local checks passed: git diff --check and 24 documentation pages with 127 route/file references. Live checks passed: 24 pages, 840 internal links/anchors, 24 page-source links, 24 feedback-link sets and the shared stylesheet. These are documentation checks, not economic or device tests. A temporary live checker is at `/tmp/markets-docs-live-check.py`; do not assume that temporary file survives another environment/session.

**Completed bounded packet: record the accepted carbon/climate exclusion.** Concepts, regulation examples, outcome reporting, requirements, content/research boundaries, decisions and overview now reflect it. Electricity remains a candidate focused on affordability, reliability, ownership, investment, financing, fuel supply and delivery. Commit `76b2973` published through successful Pages run `36206310487`. `git diff --check` passed; local validation checked 24 pages and 77 Liquid route/file references. Live verification checked the new scope wording, 24 pages, 842 internal links/anchors, 24 source links, 24 feedback-link sets and the stylesheet. The former systems-section anchor is retained for existing links. These are documentation checks only. This follow-up checkpoint records the verified publication; no game implementation or nation research was performed.

**P2a — six broad 2010 nation profiles is complete.** Draft 0.5 contains the US, UK, Germany, Russia, China and Japan profiles, a shared institutional comparison, source registers, dated observations and explicit feature-specific gaps. No sector or first playable nation is selected. Three workers handled one nation at a time across two batches because the runtime caps total child threads. All six profiles were self-reviewed and parent-reviewed; source-provenance, historical timing, source-table/anchor and executive-role issues were corrected.

**Publication evidence:** research commit `3dd2fd0`, successful Pages run `36209286984`. Local checks passed: git diff --check, six profile structures, 31 pages, 107 Liquid route/file references and reproduction of all 12 displayed WDI values. Live checks passed: 31 pages, 1,207 internal links/anchors, 31 source links, 31 feedback-link sets, stylesheet and exact CSV content; no duplicate anchors or unrendered templates. Source authors checked their references; parent independently spot-checked consequential sources and read every profile. These checks do not certify all policy routes, calibrated economics or phone usability.

**Data checkpoint:** the shared comparison uses retrospective 2010 WDI population/GDP-growth observations, API update 2026-07-13, retrieval 2026-09-25. `docs/assets/data/nation-comparison-2010.csv` preserves 12 values with provenance. They are comparison evidence, not opening-known forecasts or runnable game data. Each profile labels legal-version, data and rights gaps; Russia/Japan budget-detail gaps and China executive/Party boundaries remain visible.

**Current packet: P1-design — complete campaign proposal for review.** The user rejected a prototype and selected an assistant-authored design after challenging the lack of a concrete end-to-end game. `docs/campaign-design.md` now recommends a UK campaign, ten annual turns (2010–2019), income/employment, productive enterprises and England housing. It specifies actions, actor motives/decisions, progress, recovery, end conditions, comparison and coding milestones. `simulation.md` owns C01–C11 and their remaining inputs; `interface.md` owns the screen sequence. These are proposed defaults, not accepted nation/mechanics, calibrated data or game code.

**Current validation checkpoint:** draft 0.6 authored; git diff --check and local validation passed for 32 pages, 123 Liquid route/file references, navigation, table columns and required campaign sections. Publication and live verification pending. A–E in the campaign chapter identify the remaining concrete data, authority, model, fixtures and release artifacts. Do not claim implementation readiness while their dependent inputs remain absent. No new broad research or sub-agents were used.

**Exact next action after publication:** present the campaign-design link and two concrete review options. Preferred: adopt the proposed campaign direction, then complete its named model dependencies for authorized coding. Alternative: revise specific nation, scope or gameplay defaults. Do not return to an abstract nation/policy questionnaire, propose a prototype, resume the paper exercise, or treat design-authoring approval as implementation approval.

## Repository and publication

- Local directory: /home/bpfurtado/codex-area/devel/central-planned-economy-game
- Repository: https://github.com/ghostsysoutnull/markets-and-mandates
- Documentation: https://ghostsysoutnull.github.io/markets-and-mandates/
- Branch: main; origin is the repository above.
- Current publication: GitHub Pages, main:/docs, Jekyll.
- Documentation package: draft 0.5 published; draft 0.6 campaign proposal being published. Original concept chapters retained.
- The worktree was clean at P2a start. Research is committed and pushed; this follow-up records verified completion. No unrelated edits were found. All research workers finished their assignments.
- GitHub authentication was checked in this session and available for the owner. Check again when needed; never retain tokens in documentation.
- No game scripts or model tests exist. Proposed npm commands in delivery.md are future contracts, not executed checks.

## Read only what the packet needs

| Path | Owns |
| --- | --- |
| docs/campaign-design.md | Complete recommended campaign for review; policy catalogue, actors, ending and remaining artifacts |
| docs/development.md | Documentation map, readiness and scope |
| docs/requirements.md | Requirement IDs, accepted D1/D2 and remaining decisions D3–D8 |
| docs/architecture.md | OO design, module responsibilities, proposed stack and ADRs |
| docs/simulation.md | State, ordering, accounting, transactions and rule-sheet contract |
| docs/data-content.md | Nation evidence, content contracts and versioning |
| docs/nation-research.md | Shared 2010 method, links to six profiles, comparison and data provenance |
| docs/interface.md | Phone screen flows, accessibility and interruption |
| docs/delivery.md | Saves, migrations, offline and deployment |
| docs/verification.md | Software/model/device acceptance and evidence |
| docs/development-research.md | Dated primary-source findings and limitations |
| docs/workflow.md | Session startup, packets, checkpoints and handoffs |
| docs/backlog.md | P0–P9, dependencies, completion and aborted B1 |
| docs/decisions.md | Product decision history and remaining choices |

Original game/government/systems/interest-rates/actors/regulation/trade/nations/learning chapters remain the concept sources. Worked scenarios are illustrative branches, not interactive outcomes or quantitative evidence.

## Accepted game direction to preserve

Educational turn-based nation simulation; executive leadership constrained by actual institutions; distinct ownership/allocation/competition/public provision/redistribution/regulation/trade dimensions; active banks and corporations; separate monetary/borrowing rates and refinancing delays; real resources and delivery constraints; lawmakers, courts and partners with their own roles; distributional and delayed consequences; historical facts, assumptions and results visibly separated.

The intended roster remains US, UK, Germany, Russia, China and Japan. 2010 is the accepted broad research year; no first playable nation or exact opening date has been chosen. The current recommendation is ten annual turns (2010–2019), two initiatives plus an annual budget, fictional composite commercial actors and executive continuity; all await review. It supersedes the earlier 15-turn recommendation for this proposed release. The proposed toolchain, rule scheduling, storage scheme and first-slice scope are also recommendations, not blanket user approvals. Carbon-emissions and climate-change challenges are excluded from all future nation briefs and gameplay; historical sources must still be represented accurately, with omissions disclosed.

## Completion and publishing checks

For documentation: review changes, run git diff --check, verify links/navigation and stale plan references, commit and push the authorized changes, wait for the actual new Pages run, then inspect live pages, anchors, assets and source links. Preserve the current documentation site when planning the later game build.

Do not describe a documentation check as an economic test or claim device results without hardware/browser evidence. Keep progress summaries concise; long specifications belong in the owning chapters. End handoffs with concrete next-step options and mark the preferred one.

## Continuation prompt

> Read AGENTS.md, HANDOVER.md and docs/backlog.md. P2a broad research is complete. The user rejected a prototype and requested a complete campaign design with recommended defaults for review. Read docs/campaign-design.md and respond to their review; do not restart broad research or ask them to design the game. UK, ten turns and three policy areas are recommendations, not accepted choices. Keep exact outstanding model/data inputs visible. Preserve phone-only browser delivery, modular TypeScript/OO, the carbon/climate exclusion and the aborted paper exercise. Do not start implementation without an authorized packet.
