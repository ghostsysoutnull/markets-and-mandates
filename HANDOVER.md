# Markets & Mandates — session handover

Updated 25 September 2026. Read AGENTS.md, this file, docs/backlog.md, then only the chapters needed for the next task. Current user instructions override old checkpoints.

## Session closed — resume here

The user requested a documentation handover and an end to this session. **Do not continue research or implementation as part of closing it.** The last product decision and existing authorization are preserved below.

**Actual state:** no playable game, TypeScript application or calibrated national economy exists. Published work is design, research, source extracts and a documentation arithmetic checker. The monthly campaign change is complete; full P2b/P3 is not.

**Next session, preferred:** complete **P2b-budget — UK opening budget and financing rules**, defined in docs/backlog.md. Read only this handover, that packet, the public-account rows of docs/uk-implementation-inputs.md, C01/C03 in docs/simulation.md and M03–M06 in docs/monthly-rules.md. Use the UK profile only for the linked evidence. Do not reread every chapter.

**Alternative:** review the existing coding blockers with the user before further evidence work. This is an optional change of focus, not a requirement to reauthorize the accepted UK campaign or data/rule work.

## Accepted campaign and current authorization

The latest product decision is **“12 turns per year, option 1”**. This adopts the campaign design and authorizes completing its starting data, authority routes and economic rules, with monthly timing. Do not ask for campaign adoption or nation selection again.

- UK, opening 1 January 2010; end after December 2019: **120 monthly turns**, 12 per year, ten years.
- Income/employment, productive enterprises and England housing; correct UK/devolved authority boundaries.
- Executive continuity, counterfactual future, real institutions and fictional composite firms/lenders; deterministic actor decisions, versioned external event paths, mandate assessment, recovery, saves/export/import and comparable replay.
- Preserve annual budget authority and the existing two-major-reforms-per-calendar-year pace. This is the explicit interpretation of the timing amendment, stated in chat and docs; monthly management and encounters continue between reforms. Do not silently multiply annual initiative allowance or resources by twelve.
- Phones only, phone-browser delivery by web link, modular TypeScript/JavaScript and OO. Native-store packaging is outside scope; PWA/offline remain separate proposals.
- Carbon-emissions and climate-change challenges are excluded entirely, not deferred.
- Prototype rejected. Interactive paper walkthrough aborted; no player decisions or outcomes came from it. Neither is a development prerequisite.
- Broad six-nation research is complete. Its scoped parallel authorization does not authorize unrelated agents or six game implementations. No agents used in the current packet.
- Design adoption does not claim a calibrated numerical pack or authorize arbitrary game implementation. D8 toolchain details remain proposals; use concrete authorized coding packets after their actual dependencies are ready.

## Current packet and exact checkpoint

**P1-monthly / P3-time:** record campaign acceptance, specify monthly timing consistently, and begin the authorized UK model inputs. Draft 0.7 adds:

- `docs/monthly-rules.md`: M01–M12 calendar/slots, fiscal authority, stock/flow conversion, rates, tax dates, project duration, settlement, reports and 36-month final assessment.
- `docs/uk-implementation-inputs.md`: 22 sourced tax/NI/monetary/fiscal observations, ten concrete authority routes with evidence limits, a limited annual income-tax calculation and exact outstanding model inputs.
- `docs/assets/data/uk-opening-evidence.csv`: attributed facts and forecasts, not an initialized state. The forecast table's investment measure is net of asset sales; end-March debt is not January cash.
- `docs/assets/data/monthly-rule-fixtures.json`: synthetic temporal and limited-tax arithmetic fixtures, never national observations or simulated outcomes.
- `scripts/verify_specification.py`: independent documentation arithmetic checks, not a game engine. Covers F01–F12, four tax cases and three fiscal forecast identities.

Campaign/requirements/interface/simulation/decisions/index/development/backlog/AGENTS now record acceptance and monthly timing. Original research profiles have explicit historical-checkpoint notices so their old “no nation selected” wording is not mistaken for current direction. Historical illustrative scenarios stay fictional.

**Validation so far:** `python3 scripts/verify_specification.py` passed for 22 records, temporal arithmetic, four tax cases and three fiscal identities. Local diff/structure/navigation checks also passed for 34 pages and 151 Liquid references. Published as `aaf69ae` through successful Pages run `36212045962`. Live verification passed for 34 pages, 1,473 internal links/anchors, 34 source links, 34 feedback sets, stylesheet and exact contents of all three data artifacts. New acceptance/monthly/input content verified; no duplicate anchors or unrendered templates. This follow-up records that evidence. No game, payroll, calibrated macroeconomic or device tests have run.

**P2b/P3 as a whole are still in progress.** This packet does not complete the full economic baseline. Do not conceal that limitation. The input ledger lists actual missing opening public/bank/household/sector accounts, dated authorities, tax categories/payroll records, project bills/durations, behavioral parameters and reconciled policy alternatives. Only the temporal contracts and limited calculation above have their input-independent arithmetic checked.

**Next bounded output:** one opening public-account record with dated sourced values and explicit missing fields; an executable specification for appropriation versus cash, monthly payments, borrowing/refinancing and rejection/recovery; and independently calculated funded/unfunded/maturing-debt fixtures. Distinguish synthetic test values from the historical opening state. This prepares the budget/financing production feature, not another general design document.

**Scope limit:** do not expand that packet into full household, banking, housing or production research. Keep only counterparts needed to reconcile its transactions and list dependent gaps. Do not invent figures to make it appear ready. If a necessary source is unavailable, name the exact missing field and affected behavior.

**Path to code:** after those dependencies are demonstrably ready, present the concrete budget/financing implementation packet with its inputs and tests. The earlier authorization covers data/authority/rule completion; it is not blanket permission for game implementation. Other campaign areas remain on the ledger, not prerequisites for unrelated infrastructure.

**Process correction:** the user repeatedly challenged long, opaque documentation work and repeated whole-site link checks. Announce one concrete output, keep status concise, and prioritize game readiness. A status-only handover update needs a diff check and one targeted live-content confirmation after deployment. Do not rerun the whole-site crawler, economic checker or unchanged source checks; broaden only when the actual change or a failure justifies it. Do not create a second publication solely to insert the first publication's success into the documents.

## Repository and publishing

- Directory: `/home/bpfurtado/codex-area/devel/central-planned-economy-game`
- Repository: https://github.com/ghostsysoutnull/markets-and-mandates
- Documentation: https://ghostsysoutnull.github.io/markets-and-mandates/
- Branch: main; GitHub Pages main:/docs, Jekyll.
- Draft 0.7 is published and live-verified; this follow-up records completion.
- The monthly work is committed in `aaf69ae`; its evidence checkpoint is `d2acf5b` (Pages `36212147947` succeeded). The worktree was clean before this closing handover. This closing commit changes only handover/backlog/process records; no source data, rules or game code.
- Check tool/authentication availability as needed; never record credentials. Do not assume temporary helper scripts persist.

When documentation is authorized: check the actual diff, commit and push specific changed files, wait for the actual Pages deployment, then verify only affected live content and links. Reuse existing evidence for unchanged pages/assets; do not repeat a whole-site audit for status edits. Preserve this site when game delivery is later implemented.

## Prior completion evidence

| Packet | Publication and checks |
| --- | --- |
| P0 documentation foundation | `be68d69`; Pages `36184371335`; 24 pages/840 internal links |
| Carbon/climate exclusion | `76b2973`; Pages `36206310487`; 24 pages/842 internal links |
| P2a six-nation 2010 research | `3dd2fd0`; Pages `36209286984`; 31 pages/1,207 internal links; 12 WDI comparison observations reproduced; checkpoint `4e993c7` |
| P1 design proposal | `14f2fb4`; Pages `36210726464`; 32 pages/1,297 internal links, 32 source/feedback sets and CSV; checkpoint `e17636e`, Pages `36210802052` also verified |

These are documentation/research checks, not calibrated simulation evidence. WDI observations are retrospective 2010 comparison data, not opening-known forecasts. The latest user acceptance supersedes the old proposal-only status and annual turns.

## Read only relevant ownership

| Path | Owns |
| --- | --- |
| docs/campaign-design.md | Accepted experience, policy scope, actors, ending, coding milestones |
| docs/monthly-rules.md | M01–M12 temporal specification and F01–F12 fixtures |
| docs/uk-implementation-inputs.md | Focused P2b/P3 evidence, authority map, missing inputs |
| docs/nation-uk-2010.md | Broad historical UK source register and institutional facts |
| docs/requirements.md / docs/decisions.md | Accepted choices and remaining engineering decisions |
| docs/simulation.md | C01–C11, state, ledgers, rules and invariants |
| docs/data-content.md | Provenance/content/parameter contracts |
| docs/interface.md / docs/delivery.md | Phone flows and save/release contracts |
| docs/architecture.md / docs/verification.md | OO boundaries, engineering proposals and evidence requirements |
| docs/backlog.md / docs/workflow.md | Work state and session/publication process |

## Continuation prompt

> Read AGENTS.md, HANDOVER.md and the P2b-budget packet in docs/backlog.md. Resume the accepted UK campaign: 120 monthly turns, 2010–2019; income/employment, enterprises and England housing; phones/web link, modular TypeScript and OO; carbon/climate excluded; prototype rejected and paper walkthrough aborted. Complete only the opening budget and financing specification: dated account inputs, C01/C03 authority/cash/debt rules and independent funded/unfunded/refinancing fixtures. Existing research/rule authorization persists. Do not repeat broad research, reopen campaign adoption, invent inputs or start unrelated implementation. Keep checks proportional—no whole-site link crawler for status changes. Report exactly which budget feature can be coded and which necessary inputs remain missing.
