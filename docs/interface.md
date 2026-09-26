---
title: Mobile and web interface
intro: Make the next decision understandable on a phone, with detail available when it matters.
permalink: /interface/
---

**Status:** proposed interaction specification. Phones accessed through a browser web link are the accepted target. The UK campaign and monthly turns are accepted; exact supported browser versions and visual identity still require verification/design. This chapter describes the game interface, not the existing documentation website.

**On this page**

* Contents
{:toc}

## Information hierarchy

At every decision, answer: what situation am I in, what can I decide, what does it require, who else has authority, and what happens next? Present a short explanation first and deeper evidence on demand. Never require the player to infer whether a button drafts, submits, authorizes, or advances time.

Use four proposed destinations: Briefing, Policies, Commitments, and Report. A persistent campaign header shows nation, month/year, turn number, current phase and save status. Actor, source and system detail opens from relevant content rather than expanding the main navigation indefinitely. The campaign proposal recommends bottom navigation; validate it in the actual phone interface with accessibility checks.

## Screen contracts

| Screen | Contents | Primary action and important states |
| --- | --- | --- |
| Start/resume | Saved campaigns, new campaign, import/export where supported | Resume last checkpoint; distinguish incompatible, corrupted and missing saves |
| Nation briefing | Date, authority map, strengths, constraints, source/assumption labels | Start only with a valid selected scenario; no fabricated data placeholders |
| Monthly briefing | Mandate, most material changes, due obligations, resource limits | Review policies or outstanding decision; no forced action from reading |
| Policy catalogue | Available choices, objective, authority, rough resource demand | Open proposal; explain unavailable actions |
| Policy detail | Adjustable terms, funding, recurring obligations, timing, affected groups | Submit proposal with explicit consequence summary; drafts remain editable |
| Encounter | Actor request, motive, evidence, changed terms, feasible responses | Accept, counter, decline or defer where available; show effect of each response |
| Commitment detail | Authorized funds, spent funds, milestones, physical progress, liabilities | Inspect or request a permitted revision; cannot erase sunk costs |
| Resolution | Current phase, progress/status, no duplicate advance | Preserve last checkpoint; offer recovery on failure |
| Monthly report and December annual summary | Institutional outcomes, delivered results, distribution, finances, delays | Inspect why; acknowledge and continue |
| Campaign assessment | Mandate results, costs, side effects, uncertainty and comparison | Review/replay if supported; no hidden ideological score |

## A proposal interaction

Selecting a policy opens an editable proposal. The first view states its objective and the executive's legal route. Funding and resource needs appear before submission. Expanding “How this might work” shows actor responses, delays and assumptions, with projections labeled as estimates.

The final button should say “Submit for approval” when a vote is needed and “Authorize program” only when the executive already has the necessary power and funding. Submission feedback states whether the proposal is pending, amended, rejected or adopted. A confirmation is appropriate for advancing time, overwriting a save, or another consequential irreversible step; repeated confirmations for harmless inspection are unnecessary.

A negotiated amendment presents changed terms next to the original: cost, eligibility, regional allocation, schedule and oversight. The player must see which promise is being accepted. An explanation that only says “political support +5” is insufficient.

## Reports and charts

Start with three to five proposed report highlights, then expandable detail. This count is a layout hypothesis to test, not a settled game limit. Distinguish authorization from construction, completed homes from affordability, policy rates from borrowing offers, and current expenditure from guarantees.

Any chart needs a text summary and accessible values/table. Label units, time period, baseline and uncertainty. Do not use color alone to indicate improvement, risk or actor identity. Avoid treating higher output or lower spending as universally good; relate changes to the selected mandate and affected groups.

Preserve a coherent reading order when cards rearrange between narrow portrait and wider landscape phone screens. Data tables may use contained scrolling where necessary; the primary page and decision controls must remain usable without horizontal page scrolling. A narrow display should not hide costs or legal limits to save space.

## Accessibility requirements

Recommend WCAG 2.2 AA acceptance with keyboard, screen-reader and touch checks. The [WCAG 2.2 standard](https://www.w3.org/TR/WCAG22/) includes keyboard access, visible focus, contrast, status messages and non-color cues. For ordinary text, use at least 4.5:1 contrast; large text has a 3:1 threshold. Check controls and focus separately rather than inferring usability from text contrast.

The [reflow criterion](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) uses 320 CSS pixels width for vertically scrolling content, with exceptions for inherently two-dimensional content. Verify core screens at that width and under zoom; a desktop screenshot scaled down is not a mobile review.

The [target-size minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) uses 24 by 24 CSS pixels with defined spacing and other exceptions. Our proposed design target is 44 by 44 CSS pixels for primary touch controls; that is a project choice, not the AA minimum.

Use native buttons, links, labeled form controls and semantic headings. Make validation errors associated with their fields and preserve entered values. Announce save failures and completed resolution without flooding assistive technology with every simulation event. After navigation or closing a dialog, restore focus predictably. No core action may depend on hover, dragging, animation, sound, or a timed reaction.

Respect reduced-motion preferences and avoid motion that obstructs reading. Preserve browser zoom. Verify both orientations where available, on-screen keyboard behavior, safe-area overlap, and focus visibility when sticky controls are present.

## Interrupted and offline use

Phones suspend pages and lose connectivity. Save accepted decisions at defined checkpoints; do not depend on a closing-tab event. On return, show the correct pending decision and period. Make “Saved,” “Saving,” and “Save failed” distinct states backed by storage outcomes.

If PWA/offline scope is accepted, explain which scenario content is available offline and when preparation completes. External research links can require a network connection without preventing the local turn; keep a local source title and summary. Update prompts must not reload the application during a decision. Recovery behavior is defined in [delivery]({{ '/delivery/' | relative_url }}).

## Visual and usability review

Before styling a large application, create portrait and landscape phone screen specifications for briefing, proposal, encounter and report using the selected slice's actual information. Review whether a player can explain the action, authority, cost and delayed consequence. The paper walkthrough remains aborted and the user rejected a prototype deliverable; review these specifications and test the actual game interface during implementation.

The initial art direction, typography, sounds and motion remain open. Prefer legible restrained styling while testing the core screens. No final mockups, real-device results or usability findings are claimed in this package.

## Campaign screen sequence

The [accepted campaign]({{ '/campaign-design/' | relative_url }}) gives these screens a concrete job. The user adopted its direction with 12 turns per year and rejected a prototype as the deliverable. Implement these as the actual game screens once authorized. A preliminary interactive walkthrough is not required.

| Screen | Visible controls and information | Transition |
| --- | --- | --- |
| Start | New campaign, Resume; source/scope summary; mandate cards with exact success test | Confirm creates a versioned campaign, or shows why its data pack is unavailable. |
| Briefing | Month/year, turn out of 120, mandate progress, three priority issues, money already committed, due decisions | Open a relevant policy or obligation; no irreversible action from a headline. |
| Annual budget | Existing commitments first; editable supported tax/transfer schedules and operating allocations; financing gap | Save draft or submit through the correct fiscal route. Structural changes link to initiatives. |
| Policy catalogue | Income/employment, Enterprises, England housing; initiative slots remaining | Open a package. Empty unavailable nations and unsupported actions are not advertised as playable. |
| Proposal | Objective, adjustable terms, funding source, authority, earliest delivery, ongoing costs and alternative approaches | Submit after validation. Show whether this consumes an initiative and what is still awaiting another actor. |
| Offer/decision | Named institution or composite actor, motive, original terms beside amended terms | Accept, revise or decline; exact financial changes and obligations appear before confirmation. |
| Commitments | Stage, spent and reserved money, physical progress, next obligation, recorded blocker | Inspect or propose a lawful change; cancellation explicitly lists sunk and termination costs. |
| Advance | Approved budget, pending matters, automatic payments, likely resource conflicts | Confirm resolution. A saved encounter interrupts only when the player's decision is needed. |
| Report | Household results, employment, output/delivery, finance and institutional outcomes | “Why?” opens actual rule/transaction evidence; Continue starts the next month or, after December 2019, the final assessment. |
| Final assessment | Achieved/not achieved with individual tests, comparison run, distribution, outstanding costs and decisions timeline | Review; replay identical external conditions; or start another mandate. |

Use a portrait-first briefing style with bottom navigation and a persistent nation/month/year/turn/save header. No hover-only controls or mandatory drag sliders; numeric terms also have labeled editable inputs. Depth opens in ordinary detail screens with Back preserving drafts and scroll position. Chart values remain available as text.

Incomplete input preserves the draft and focuses the specific field. A rejected proposal shows the blocker and an available revision, without treating refusal as a software error. A failed save leaves the decision recoverable and never shows “Saved.” Pending actor encounters survive reload. The final advance cannot resolve twice from repeated taps.

No visual mockup, implemented screen, accessibility pass or device test is claimed by this specification. UI acceptance is against the real integrated campaign and the accessibility/recovery contracts above.
