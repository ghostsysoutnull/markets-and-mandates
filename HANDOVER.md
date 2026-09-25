# Markets & Mandates — session handover

Updated 25 September 2026. Read AGENTS.md first, then this file and docs/backlog.md. The current user overrides older plans.

## Current objective and accepted changes

The user **aborted the interactive walkthrough** and requested all necessary development documentation, researched rather than assumed, for mobile/web with JavaScript/TypeScript, OO and an efficient process across sessions.

Latest explicit answers:
- **Phones only.** Desktop gameplay is not a product target.
- **Normal TypeScript project with multiple source files.** The older single physical HTML output constraint is superseded.
- Phone browser/web link versus App Store/Google Play distribution is still pending. A plain-language question has been asked; a normal chat answer is sufficient.

Do not resume the paper exercise or ask the user to choose housing option B. No nation, mandate, policy or outcome was selected in that exercise. It is aborted, not completed.

## Current work and exact next action

Active packet: **P0 — development documentation foundation**. Nine new engineering/product chapters plus a development hub have been drafted with primary-source research, requirements, OO boundaries, model/data contracts, phone UX, saves, tests and session workflow. No game implementation, dependency installation, quantitative calibration or nation profile has been produced.

Next within P0: integrate any answer about distribution; publish authorized documentation changes using the existing Pages workflow, and verify actual live content. Local checks passed: git diff --check and 24 documentation pages with 127 route/file references. Update this checkpoint with deployment results before handoff.

After P0, preferred next packet is **P1 — first-slice decisions**. Preserve phone-only and modular TypeScript selections. Ask only remaining dependent choices: distribution, nation/year, first policy family and campaign detail as needed. Architecture review is an alternative. Research cannot choose these preferences for the user.

## Repository and publication

- Local directory: /home/bpfurtado/codex-area/devel/central-planned-economy-game
- Repository: https://github.com/ghostsysoutnull/markets-and-mandates
- Documentation: https://ghostsysoutnull.github.io/markets-and-mandates/
- Branch: main; origin is the repository above.
- Current publication: GitHub Pages, main:/docs, Jekyll.
- Documentation package: draft 0.4; original concept chapters retained.
- At the start of P0, only HANDOVER.md and docs/backlog.md were modified by this assistant's prior walkthrough setup; no unrelated user edits were found.
- GitHub authentication was checked in this session and available for the owner. Check again when needed; never retain tokens in documentation.
- No game scripts or model tests exist. Proposed npm commands in delivery.md are future contracts, not executed checks.

## Read only what the packet needs

| Path | Owns |
| --- | --- |
| docs/development.md | Documentation map, readiness and scope |
| docs/requirements.md | Requirement IDs, accepted D2 and remaining decisions D1/D3–D8 |
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

> Continue Markets & Mandates from P0/P1 as recorded here. The paper walkthrough is aborted. The user wants researched development documentation and an efficient multi-session process; phones only, modular TypeScript and OO are accepted. Read AGENTS.md, HANDOVER.md, docs/backlog.md and only the active packet's chapters. Preserve decisions, ask only for unresolved dependent preferences, and do not invent nation data or calibrated results. Complete the authorized packet, verify it, update the checkpoint, and give concise next-step options.
