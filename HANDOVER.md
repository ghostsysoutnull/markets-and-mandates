# Markets & Mandates — session handover

Updated 25 September 2026. Read AGENTS.md first, then this file and docs/backlog.md. The current user overrides older plans.

## Current objective and accepted changes

The user **aborted the interactive walkthrough** and requested all necessary development documentation, researched rather than assumed, for mobile/web with JavaScript/TypeScript, OO and an efficient process across sessions.

Latest explicit answers:
- **Phones only.** Desktop gameplay is not a product target.
- **Normal TypeScript project with multiple source files.** The older single physical HTML output constraint is superseded.
- **Phone-browser delivery via a web link.** The user selected option 1. Do not ask this choice again. Native app-store packaging is outside the selected scope; installation/offline support remain proposals.
- **Carbon-emissions and climate-change challenges excluded throughout the game.** No related accounting, policy tools, mandates, events, scores or hidden rewards/penalties. This is not deferred expansion work. Other environmental topics are not selected by this decision.
- **Broad 2010 research accepted.** The user's latest option 1 selects broad profiles for all six nations, one researcher per nation in two batches, before choosing the first playable nation and policy family. No sector focus is required. This supersedes the electricity prerequisite, and explicitly authorizes these sub-agents. 1 January 2010 is the shared editorial institutional snapshot, not a selected exact gameplay start date.

Do not resume the paper exercise or ask the user to choose housing option B. No nation, mandate, policy or outcome was selected in that exercise. It is aborted, not completed.

## Current work and exact next action

**P0 — development documentation foundation is complete.** Nine new engineering/product chapters plus a development hub are published with primary-source research, requirements, OO boundaries, model/data contracts, phone UX, saves, tests and session workflow. No game implementation, dependency installation or quantitative calibration has been produced. Broad nation research is now drafted under P2a, with publication verification pending.

Verification: documentation commit `be68d69`; Pages run `36184371335` succeeded. Local checks passed: git diff --check and 24 documentation pages with 127 route/file references. Live checks passed: 24 pages, 840 internal links/anchors, 24 page-source links, 24 feedback-link sets and the shared stylesheet. These are documentation checks, not economic or device tests. A temporary live checker is at `/tmp/markets-docs-live-check.py`; do not assume that temporary file survives another environment/session.

**Completed bounded packet: record the accepted carbon/climate exclusion.** Concepts, regulation examples, outcome reporting, requirements, content/research boundaries, decisions and overview now reflect it. Electricity remains a candidate focused on affordability, reliability, ownership, investment, financing, fuel supply and delivery. Commit `76b2973` published through successful Pages run `36206310487`. `git diff --check` passed; local validation checked 24 pages and 77 Liquid route/file references. Live verification checked the new scope wording, 24 pages, 842 internal links/anchors, 24 source links, 24 feedback-link sets and the stylesheet. The former systems-section anchor is retained for existing links. These are documentation checks only. This follow-up checkpoint records the verified publication; no game implementation or nation research was performed.

**Active packet: P2a — six broad 2010 nation profiles.** All six are drafted, self-reviewed and parent-reviewed; China source-provenance and executive-role clarifications are completed. Runtime limits total child threads, so three workers handled one nation at a time across two batches. Each owns only its `docs/nation-*-2010.md`; parent owns the research hub, comparison, state records and publication. Shared brief: `/tmp/markets-nation-research-brief.md` (temporary; shared method also in `docs/nation-research.md`). No sector scope or first playable nation selected.

**Current parent work:** accepted choices recorded in requirements/decisions/backlog; shared hub created; 12 WDI retrospective 2010 population/GDP-growth observations retrieved, metadata update 2026-07-13, retrieval 2026-09-25. Saved CSV at `docs/assets/data/nation-comparison-2010.csv`, not runnable game data. All six profiles and shared comparison are drafted. Twelve CSV values reproduce the displayed comparison; local routes, profile anchors and table continuity checked. Commit/push and Pages/live checks remain; no P2a publication or completion claimed yet.

**Exact next action:** run final diff/link checks, commit/push the authorized documentation, wait for Pages, verify live pages/assets and record acceptance evidence. Then choose the first playable nation and policy focus for P2b/P3. Do not ask again for the research year or electricity focus; the user explicitly chose broad research first.

## Repository and publication

- Local directory: /home/bpfurtado/codex-area/devel/central-planned-economy-game
- Repository: https://github.com/ghostsysoutnull/markets-and-mandates
- Documentation: https://ghostsysoutnull.github.io/markets-and-mandates/
- Branch: main; origin is the repository above.
- Current publication: GitHub Pages, main:/docs, Jekyll.
- Documentation package: draft 0.5 research update prepared; original concept chapters retained. Previous live publication is draft 0.4 until this packet deploys.
- The worktree was clean at P2a start. Current uncommitted work is the authorized research and integration; preserve each agent’s assigned file.
- GitHub authentication was checked in this session and available for the owner. Check again when needed; never retain tokens in documentation.
- No game scripts or model tests exist. Proposed npm commands in delivery.md are future contracts, not executed checks.

## Read only what the packet needs

| Path | Owns |
| --- | --- |
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

The intended roster remains US, UK, Germany, Russia, China and Japan. 2010 is the accepted broad research year; no first playable nation or exact opening date has been chosen. A 2010–2025 campaign, 15 annual turns, two initiatives, fictional visible actors and continuation across successive executives remain proposals. The proposed toolchain, rule scheduling, storage scheme and first-slice scope are also recommendations, not blanket user approvals. Carbon-emissions and climate-change challenges are excluded from all future nation briefs and gameplay; historical sources must still be represented accurately, with omissions disclosed.

## Completion and publishing checks

For documentation: review changes, run git diff --check, verify links/navigation and stale plan references, commit and push the authorized changes, wait for the actual new Pages run, then inspect live pages, anchors, assets and source links. Preserve the current documentation site when planning the later game build.

Do not describe a documentation check as an economic test or claim device results without hardware/browser evidence. Keep progress summaries concise; long specifications belong in the owning chapters. End handoffs with concrete next-step options and mark the preferred one.

## Continuation prompt

> Read AGENTS.md, HANDOVER.md and docs/backlog.md. Continue the recorded P2a checkpoint: broad 2010 profiles for all six nations, one researcher per nation in two batches, before selection of the first playable nation and policy family. This work is authorized; there is no electricity or other sector prerequisite. Preserve the carbon/climate exclusion, phones only, web-link delivery, modular TypeScript and OO. Review dated sources, finish and publish the documentation, then help select a playable slice. Do not resume the aborted walkthrough or begin implementation.
