# Markets & Mandates — session handover

Updated 25 September 2026. Read AGENTS.md first, then this file and docs/backlog.md. The current user overrides older plans.

## Current objective and accepted changes

The user **aborted the interactive walkthrough** and requested all necessary development documentation, researched rather than assumed, for mobile/web with JavaScript/TypeScript, OO and an efficient process across sessions.

Latest explicit answers:
- **Phones only.** Desktop gameplay is not a product target.
- **Normal TypeScript project with multiple source files.** The older single physical HTML output constraint is superseded.
- **Phone-browser delivery via a web link.** The user selected option 1. Do not ask this choice again. Native app-store packaging is outside the selected scope; installation/offline support remain proposals.
- **Continue in a fresh session.** The user's latest option 1 selects a fresh nation-research session, not the earlier UK/2010 suggestion. No nation or year has been selected.

Do not resume the paper exercise or ask the user to choose housing option B. No nation, mandate, policy or outcome was selected in that exercise. It is aborted, not completed.

## Current work and exact next action

**P0 — development documentation foundation is complete.** Nine new engineering/product chapters plus a development hub are published with primary-source research, requirements, OO boundaries, model/data contracts, phone UX, saves, tests and session workflow. No game implementation, dependency installation, quantitative calibration or nation profile has been produced.

Verification: documentation commit `be68d69`; Pages run `36184371335` succeeded. Local checks passed: git diff --check and 24 documentation pages with 127 route/file references. Live checks passed: 24 pages, 840 internal links/anchors, 24 page-source links, 24 feedback-link sets and the shared stylesheet. These are documentation checks, not economic or device tests. A temporary live checker is at `/tmp/markets-docs-live-check.py`; do not assume that temporary file survives another environment/session.

**Exact next action, in a fresh session: P1 — first-slice decisions.** D1 (phone-browser web link) and D2 (modular TypeScript) are accepted. Help the user select the first nation/year, then establish the policy scope needed for focused P2 research. The assistant recommended the UK in 2010 because existing notes include Bank of England references and 2010 was the proposed campaign start; this is a recommendation, not an accepted baseline or completed nation research. Preserve the phone-only player target. Ask for campaign detail only when its feature needs it. Do not continue nation research in the closing session or ask again whether to use a fresh session.

## Repository and publication

- Local directory: /home/bpfurtado/codex-area/devel/central-planned-economy-game
- Repository: https://github.com/ghostsysoutnull/markets-and-mandates
- Documentation: https://ghostsysoutnull.github.io/markets-and-mandates/
- Branch: main; origin is the repository above.
- Current publication: GitHub Pages, main:/docs, Jekyll.
- Documentation package: draft 0.4; original concept chapters retained.
- The worktree was clean before recording the fresh-session choice. No unrelated user edits were found.
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

The intended roster remains US, UK, Germany, Russia, China and Japan. No first nation or date has been chosen. 2010–2025, 15 annual turns, two initiatives, fictional visible actors and continuation across successive executives remain proposals. The proposed toolchain, rule scheduling, storage scheme and first-slice scope are also recommendations, not blanket user approvals.

## Completion and publishing checks

For documentation: review changes, run git diff --check, verify links/navigation and stale plan references, commit and push the authorized changes, wait for the actual new Pages run, then inspect live pages, anchors, assets and source links. Preserve the current documentation site when planning the later game build.

Do not describe a documentation check as an economic test or claim device results without hardware/browser evidence. Keep progress summaries concise; long specifications belong in the owning chapters. End handoffs with concrete next-step options and mark the preferred one.

## Continuation prompt

> Read AGENTS.md, HANDOVER.md and docs/backlog.md. This is the fresh session selected for Markets & Mandates nation research. Continue P1: help me select the first nation and starting year, establish the necessary first-slice policy scope, then research the baseline under P2. UK/2010 was recommended but has not been selected. Phone-browser delivery via a web link, phones only, modular TypeScript and OO are accepted. Do not resume the aborted walkthrough or begin game implementation. Use primary sources and distinguish facts from model proposals. Always provide concrete next-step options and mark your preference.
