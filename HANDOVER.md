# Markets & Mandates — session handover

Prepared 25 September 2026. This is the resumption guide for the project, not a substitute for the detailed concept spec. Read `AGENTS.md` first; use the current user request if it changes this recorded plan.

## Immediate state and next action

The user requested a durable handover before continuing concept work, and asked to list all three latest session options as backlog. That backlog is in [docs/backlog.md](docs/backlog.md), with the complete annual-turn walkthrough selected next. Do not begin implementation or nation research merely because they are listed.

The walkthrough has **not started**. Existing worked examples are explanatory documentation, not a completed interactive playthrough. The user has not selected a nation or made gameplay choices for the next exercise.

When the user is ready to continue, proceed with B1: prepare one interactive annual-turn exercise, present a concise briefing and meaningful choices, and let the user decide. Do not ask again whether they want B1. Explain any illustrative starting assumptions and offer alternatives where a choice materially affects the experience.

## Project and publishing locations

| Item | Location or value |
| --- | --- |
| Project | Markets & Mandates |
| GitHub owner/repository | `ghostsysoutnull/markets-and-mandates` |
| Repository URL | https://github.com/ghostsysoutnull/markets-and-mandates |
| Live documentation | https://ghostsysoutnull.github.io/markets-and-mandates/ |
| Local working directory used in this session | `/home/bpfurtado/codex-area/devel/central-planned-economy-game` |
| Branch and remote | `main`, `origin` → `https://github.com/ghostsysoutnull/markets-and-mandates.git` |
| Visibility | Public |
| Pages source | `main` branch, `/docs` folder; built-in Jekyll publication |
| Current game spec edition | 0.3 |

The local folder name predates the chosen project name; no rename is necessary to continue. Do not recreate the repository or replace the publishing configuration.

## What the game is

An educational, turn-based nation simulation exploring free markets, central planning, and combinations between them. The player chooses a real nation, learns its starting economic and institutional arrangements, then changes policy and observes actors and systems respond.

The intended roster is the United States, United Kingdom, Germany, Russia, China, and Japan, with room to expand. Recent history is the main focus; a separate 1980s scenario is a possible later addition. Use period-appropriate entities and institutions.

The eventual delivery should be mobile-friendly, as a single HTML and JavaScript page. **There is no playable game or simulation implementation yet.** The current Jekyll site is documentation, not the game architecture.

## Accepted concept direction

- The player controls the nation's executive leadership—the government and cabinet—with powers that fit the nation and period. The player is not every institution or necessarily one named politician.
- Ownership, allocation, competition, public provision, redistribution, regulation, and international openness are distinct dimensions. Avoid one ideological slider deciding everything.
- Central banks act under their mandates and independence arrangements. Distinguish policy rates, private borrowing rates, government financing costs, and relevant deposit rates. Existing contracts and refinancing create delays.
- Large corporations and private banks are active NPCs. Their investment, employment, pricing, lending, negotiations, and risk-taking reflect resources, objectives, and constraints.
- Public enterprises and development banks also need financing, management, inputs, and accountability. Changing ownership does not instantly remove physical or institutional problems.
- Domestic regulation and enforcement are core tools. Rules have scope, authority, implementation needs, compliance, review, and possible unintended effects.
- Trade decisions include tariffs, agreements, industrial support, investment conditions, and strategic dependencies, subject to national authority and commitments. Foreign partners respond and can reject deals.
- Lawmakers can amend, delay, or reject proposals. Courts review measures within their legal powers. Political support, legal validity, funding, and delivered results are distinct.
- Consequences unfold over time and differ across households, regions, and enterprises. Explain mechanisms, tradeoffs, uncertainty, and who benefits or bears costs.
- Facts about the starting nation, model assumptions, and simulated results must remain distinguishable. No automatic ideological winner or permanent national stereotypes.

## Working proposals, not settled rules

- A main campaign beginning in 2010 with 15 annual turns, concluding in 2025.
- Two major initiatives per year, with budgets and encounters; no unlimited actions hidden inside a policy package.
- An accessible strategy game with optional deeper explanations rather than a highly granular sandbox.
- A small visible cast of fictional organizations grounded in researched economic structures, plus aggregated smaller actors.
- A player-selected public mandate and a multidimensional final assessment rather than a universal score.
- Replay under comparable external shocks, allowing domestic events to diverge when policy changes their causes.
- Continue playing across successive executives. A new administration changes mandates and coalitions while inheriting assets, obligations, laws, and unfinished projects. Succession and accountability rules remain unresolved.
- Surface consequential votes, cases, and negotiations; avoid requiring detailed procedural management for every action.

The user accepted the broad direction and requested documentation updates. That does not mean every illustrative mechanism, date, effect size, or open proposal has been approved as a final rule.

## What still needs decisions or research

- Session length, exact turn structure and initiative budget, visible dashboard, and first playable scope.
- Nation selection for the first exercise and for the first researched baseline.
- Election/succession triggers, changing mandates, consequences of losing office, and whether any crisis ends a campaign.
- Historical versus randomized external events and the treatment of history that could change under player decisions.
- NPC cast size, real versus fictional names, private information, negotiation depth, and policy-package customization.
- Sourced, dated country profiles, including formal and effective executive powers, legislature, judiciary, monetary institutions, trade commitments, and starting economic data.
- Quantitative model rules, calibration, accounting, feedback effects, uncertainty, and validation. None have been completed.

The sources chapter contains initial institutional references, mainly from the Bank of England, ECB, IMF, BIS, OECD, WTO, and EU Council. They support selected mechanisms, not complete national profiles or numerical policy predictions.

## Reading map

| File | Purpose |
| --- | --- |
| [docs/index.md](docs/index.md) | Overview and chapter navigation |
| [docs/game.md](docs/game.md) | Player role, yearly loop, policy commitments, outcomes, and reports |
| [docs/government.md](docs/government.md) | Executive powers, legislative blocs, courts, central-bank tension, and succession |
| [docs/systems.md](docs/systems.md) | Fiscal policy, production, households, information, institutions, and transitions |
| [docs/interest-rates.md](docs/interest-rates.md) | Rate setting, lending, refinancing, fiscal exposure, and distribution |
| [docs/actors.md](docs/actors.md) | Corporate, banking, and other NPC behavior |
| [docs/regulation.md](docs/regulation.md) | Regulatory choices, enactment, enforcement, and review |
| [docs/trade.md](docs/trade.md) | International choices, commitments, negotiation, and partner responses |
| [docs/scenarios.md](docs/scenarios.md) | Four fictional multi-turn examples; no calibrated outputs |
| [docs/nations.md](docs/nations.md) | Profile requirements and historical methodology; not completed country profiles |
| [docs/learning.md](docs/learning.md) | Explanations, experiments, conceptual distinctions, and bias checks |
| [docs/decisions.md](docs/decisions.md) | Accepted direction, proposals, open questions, and decision log |
| [docs/backlog.md](docs/backlog.md) | Three queued session options, order, prerequisites, and completion criteria |
| [docs/sources.md](docs/sources.md) | Supporting bibliography and research gaps |

For B1, begin with `docs/backlog.md`, `docs/game.md`, `docs/government.md`, `docs/interest-rates.md`, and the relevant example in `docs/scenarios.md`. Read other chapters as needed; do not reread everything indiscriminately.

## User collaboration preferences

- Focus on concepts now. The user explicitly corrected premature attention to implementation files and technology setup.
- Substantial detail belongs in the spec. The user found the initial site too compressed relative to the discussion; keep the overview short and develop supporting chapters fully.
- Keep conversational handoffs concise and actionable. **Always offer concrete next-step options and mark the preferred option.** Do not leave the conversation without a next step.
- Preserve selections already made. B1 is queued after the handover; do not reopen that choice as if undecided.
- When the user asks a question or explicitly says not to act, discuss it without modifying files or publishing changes.
- When the user asks to update the docs, they expect the GitHub Pages site to be updated and verified, not just local edits.
- Mark new assumptions and proposals clearly. Explain institutional variation without inventing nation-specific powers or data.

The latest three session options were: continue here with a full turn; use a fresh session for focused nation research; use a fresh session for implementation once ready. The earlier question about government continuity remains an open design prerequisite, not a lost or silently resolved decision.

## Recent work and validation

Before this handover addition, the published design history was:

- `f25aa72`: initial concept and documentation site.
- `ae2e290`: draft 0.2, corporate/banking NPCs, regulation, trade, and scenarios.
- `2bb8082`: draft 0.3, executive role, institutions, interest rates, and a fourth scenario.

The draft 0.3 Pages run `36161555924` completed successfully. The live check passed for 13 pages and 306 internal links, including section anchors, navigation, source links, feedback links, and shared CSS. This predates the new backlog page; verify the latest deployment separately.

There are no game tests because there is no game implementation. Checks so far cover documentation publication and link integrity, not economic model correctness or browser-based visual testing.

At preparation, the worktree was clean before adding the handover and backlog. Always check it again at resumption. Do not assume these historical commit IDs are the latest head.

## How to publish and verify documentation

1. Read current changes with `git status --short` and inspect relevant files; preserve unrelated edits.
2. Edit Markdown with `apply_patch`. Update links, navigation, and the decision log when appropriate.
3. Keep internal Jekyll links compatible with `/markets-and-mandates`, using `relative_url`. Longer pages use Kramdown contents lists and stable heading anchors.
4. Run `git diff --check`, review the diff, and commit/push the authorized changes to `main`.
5. Check `gh run list --repo ghostsysoutnull/markets-and-mandates`, then watch the actual new Pages run to completion. Do not reuse a historical run ID.
6. Fetch the live affected pages and validate HTTP success, expected content, generated navigation, internal links and anchors, source links, and feedback URLs. Confirm the latest content rather than a cached prior draft.
7. Report the live links and relevant verification, then provide the next-step options with a preference.

Configuration is `docs/_config.yml`; shared layout is `docs/_layouts/default.html`; styling is `docs/assets/style.css`. Feedback uses `.github/ISSUE_TEMPLATE/design-feedback.md`. The CSS supports narrow screens and a scrollable long sidebar. Use `cgi_escape` for feedback query titles containing ampersands.

`gh` was authenticated for the repository owner in this session, and `node` was available for HTTP/link checks. Check access afresh when needed. Do not store tokens, assume old sandbox permissions, or introduce a new toolchain just for prose edits. No scheduled jobs, unresolved deployment failures, or required background processes were left by the completed design work.

## Copy-paste resumption prompt

> Continue Markets & Mandates in this repository. Read AGENTS.md, HANDOVER.md, and docs/backlog.md, then the relevant concept chapters. We are designing the game, not implementing it. The handover is complete; continue with B1, the interactive walkthrough of one annual turn. Use clearly labeled illustrative assumptions until a nation baseline is researched, present decisions for me to make, and do not claim the walkthrough is complete before I have chosen and reviewed outcomes. Keep accepted direction separate from proposals. At each handoff, give concrete next-step options and mark your preference. B2 nation research and B3 implementation remain deferred.
