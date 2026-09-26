---
title: Verification and release evidence
intro: Check software correctness, economic consistency and player comprehension as separate obligations.
permalink: /verification/
---

**On this page**

* Contents
{:toc}

## What a passing check means

Type checks establish certain program constraints. Accounting tests establish reconciliation. Scenario checks test stated model behavior. Usability checks test whether players understand decisions. None alone validates real-world policy predictions. This package has no game implementation, executed model tests, device results or calibrated outputs.

Use tests proportional to behavior and risk. Avoid testing private class layout or duplicating an implementation formula as the expected answer. Prefer independent hand calculations, invariants, competing branches and externally visible outcomes.

## Test layers and ownership

| Layer | Evidence | Suggested tooling and timing |
| --- | --- | --- |
| Static | Type boundaries, invalid imports, dead code and conventions | TypeScript and chosen lint tool on changed implementation |
| Domain unit | Debt repricing, commitment transitions, authorization and posting rules | Vitest with explicit fixtures per rule |
| Model invariant | Balanced ledgers, valid resources, bounded calculations | Generated and adversarial state/command sequences |
| Application integration | Revision control, duplicate commands, atomic checkpoints, pending encounters | Repository contract suite with memory and browser adapters |
| Content validation | IDs, sources, versions, authority references, initial accounts | Schema and cross-reference validator per content pack |
| Browser journey | Start, draft, encounter, advance, inspect, reload and import | Playwright across selected engines |
| Mobile/accessibility | Touch, keyboard, screen reader, zoom, interruption and real-device behavior | Automated checks plus manual records |
| Economic evaluation | Sensitivity, no-change baseline, alternative policies, plausibility and bias | Versioned experiment inputs and readable reports |
| Release | Hosted paths, assets, saves, offline/update behavior where supported | Production preview and actual deployment smoke checks |

[Vitest](https://vitest.dev/guide/features) is the proposed unit runner. [Playwright device emulation](https://playwright.dev/docs/emulation) supports viewport, touch and network-condition configuration; report these as emulated tests. Real iOS Safari and Android Chrome checks remain separate evidence.

## Required behavioral cases

| Case | Expected property | Requirements |
| --- | --- | --- |
| Legislature rejects a proposal | No unauthorized disbursement or completed asset; lawful existing commitments continue | R03–R06 |
| An amended bill costs more | Revalidate funding, capacity and terms before adoption | R03, R05 |
| Independent rate change | Only eligible new/refinancing/variable contracts reprice according to terms | R04, R06, R07 |
| A funded project lacks inputs | Record delay or partial feasible progress; do not create missing capacity | R06, R07 |
| Guarantee exists but no default occurs | Report exposure separately from actual public payment | R03, R06 |
| New bank lending | Loan asset, borrower liability and deposit entries follow the declared accounting boundary | R06 |
| Public/private ownership changes | Preserve assets, physical constraints and specified obligations | R06, R07 |
| Same command submitted twice | One economic effect and one committed revision for that command | R06, R08 |
| Two tabs submit against one revision | One wins; stale writer cannot overwrite the new state | R08 |
| Save transaction fails | Last checkpoint intact; failure shown; retry cannot reroll outcomes | R08 |
| Save imported with invalid data | Reject safely without replacing a valid campaign | R13 |
| Same versioned seed/input run twice | Identical structured outputs within the declared numeric contract | R10 |
| UI opens details or previews | Authoritative state and live random streams stay unchanged | R03, R10 |
| National profile lacks authority | Action unavailable or routed to the correct institution; explanation visible | R01, R04, R12 |

For each case, include at least one failure/boundary fixture relevant to the chosen slice. A snapshot of a large result object is insufficient when a targeted accounting assertion explains the requirement better.

## Model evaluation protocol

First reconcile a synthetic small fixture that can be checked by hand. Synthetic fixtures are valid software tests when labeled; they are not historical baselines. Then initialize the chosen nation with sourced data and explicitly documented transformations.

Run a no-new-policy branch and at least two feasible alternatives. Hold external shock inputs comparable while allowing policy-dependent outcomes to diverge. Record parameter set, rules/content version, horizon, seed streams, outcomes by household/sector, public costs and unfulfilled commitments.

Vary uncertain parameters across justified ranges and look for sign reversals, exploding values, implausible stability and a single policy dominating under all conditions. Do not impose a universally favorable growth response to public or private ownership. Check mirrored physical constraints while allowing documented objective and financing differences.

Validation uses qualitative patterns and data appropriate to the model purpose, with explicit limitations. Reserve observations or scenarios from tuning when feasible. Explain conflicting evidence and distinguish accounting truth from behavioral hypothesis. The [ODD research](https://www.jasss.org/23/2/7.html) supports documenting evaluation and rationale; it does not choose success thresholds for this game.

## Accessibility and device protocol

Record screen, task, device, OS/browser version, input method, build, steps, observed result and remaining defect. Check the core sequence at 320 CSS pixels width, zoomed content, keyboard-only operation, visible focus, screen-reader names/order, non-color explanations, and touch targets. Include interruption during a draft and immediately after committing a decision.

Test actual phones for browser suspension, keyboard overlap, orientation and storage behavior. If hardware is unavailable, say “not tested” and retain the release dependency. An automated accessibility scan does not establish WCAG conformance.

## Performance protocol

Select a reference phone and reproducible scenario size first. Measure production assets and runtime, excluding developer tools from the product result. Record network conditions, cold/warm loads, median and tail observations, repetitions, memory where measurable, and turn-resolution duration. Compare with the proposed budgets in [requirements]({{ '/requirements/' | relative_url }}); do not cite a desktop timing as a phone result.

If a turn blocks interaction, profile before optimizing. A worker, chunked processing or smaller representations are candidates with tradeoffs. Re-run determinism and interruption tests after moving execution boundaries.

## Definition of done

Each task provides a requirement/rule reference, observable implementation or document change, applicable checks and results, compatibility impact, and updated checkpoint. A release additionally needs the chosen browser/device matrix, save recovery, content evidence, model evaluation, live deployment verification and known limitations. Open optional enhancements do not block a narrow slice; missing required evidence does.

Documentation-only changes need diff review, stable links/navigation, consistency across current-state records, source support and publication checks if published. Do not install the proposed game toolchain just to check Markdown. No economic test suite can pass before the model exists.

## Monthly specification evidence

The accepted campaign has 120 monthly turns. Before engine implementation, run `python3 scripts/verify_specification.py` to reproduce F01–F12 temporal fixture arithmetic, four limited annual-tax cases and three fiscal forecast identities. It also checks the 22-record evidence extract structure. These are documentation arithmetic checks, not implemented gameplay, comprehensive PAYE, macroeconomic calibration or real-device tests.

Later engine tests must independently exercise duplicate Advance month, a saved mid-month encounter, no January double-budget, no repeated annual allowance, fixed-rate repricing, preserved construction duration, 36-month assessment and the final December-to-assessment transition. See [monthly rules]({{ '/monthly-rules/' | relative_url }}) and [UK implementation inputs]({{ '/uk-implementation-inputs/' | relative_url }}).
