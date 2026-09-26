---
title: Monthly campaign rules
intro: Twelve turns per year, with budgets, contracts and construction keeping their real time scales.
permalink: /monthly-rules/
---

**Accepted timing:** the user adopted the [campaign design]({{ '/campaign-design/' | relative_url }}) with **12 turns per year**. One turn is one calendar month. January 2010 through December 2019 contains **120 turns**. The rules below specify that change without multiplying annual budgets, reform opportunities or physical output. They are model contracts; the numerical economy is not yet calibrated or implemented.

**On this page**

* Contents
{:toc}

## M01 — Calendar and campaign boundaries

Store a zero-based `monthIndex` from 0 through 119. Display turn number as `monthIndex + 1`; year is `2010 + floor(monthIndex / 12)` and calendar month is `1 + monthIndex mod 12`. The active interval includes the first date of that month and excludes the first date of the following month. Use calendar dates independent of the phone's timezone and daylight-saving changes.

After committing month 119, set the campaign phase to `assessment`, with assessment date 1 January 2020. Do not create a playable turn 121. Days inside a month determine deadlines and accrual where required; they are not extra player turns. February 2012 and February 2016 each contain 29 days.

## M02 — Monthly decisions and annual priorities

Each month follows Briefing → Drafting → Authorization/encounters → Resolution → Report. Reopen a pending encounter on resume; do not redo the month or consume another reform slot. Player controls include reviewing a funding gap, negotiating existing proposals, phasing or cancelling commitments and resolving distress.

The adopted design previously allowed two major reforms each year. Retain **two reform submissions per calendar year**, resetting in January without carryover. This is the explicit pacing interpretation of the user's timing amendment, not an additional historical fact. A submitted reform consumes one slot even if rejected. Amendments to the same objective use its existing slot; replacing it with a different structural objective consumes another. Ordinary administration and lawful recovery under existing authority do not consume slots.

A case cannot bypass the limit by calling a new structural reform an emergency. Conversely, an already authorized project does not need twelve new reforms to operate for a year. Negotiations can span months; consuming a slot does not guarantee that legislation, consent or financing arrives in that month.

## M03 — Budget authority, spending and fiscal dates

Maintain fiscal-year authority separately from calendar turns and actual cash. January 2010 inherits the unexpired 2009–10 authority, amounts already used, reservations and liabilities. It does not receive a second full annual budget. An appropriation has a purpose, amount, owner, effective date and expiry, with separate resource and cash limits where the route requires them.

An annual authorization is a ceiling over its covered period. A monthly spending profile schedules payments within it; the profile neither grants authority nor deposits cash. Reallocation must follow its specific route. A rejected new budget cannot grant automatic perpetual use of an expired appropriation.

The contemporary Supply Estimates describe fiscal-year authorizations, Votes on Account and subsequent Main Estimates; the former ordinarily sought 45% of the preceding year's amounts. This is an **advance within the authorized year**, not an additional annual pot or a default after defeat. The July 2010 publication explains the procedure but its July spending amounts are not January information. See [Treasury, Main Supply Estimates 2010–11, sections 2–3](https://www.parliament.uk/globalassets/documents/commons-expenditure/supply-estimates/2010-11-main-supply-estimates-central-govt.pdf).

For a payment: first identify due date and valid authority; check unused cash/resource authority net of reservations; check actual available cash or settled finance; then post payer and recipient entries. If either permission or cash is insufficient, create an explicit financing/authority encounter. A legal liability can remain due even when payment authority is insufficient; record arrears rather than deleting it.

## M04 — Stocks, flows and monthly profiles

Stocks such as debt principal, deposits, population, homes and installed capacity are carried forward. **Never divide a stock by 12.** Monthly changes update the stock exactly once.

An annual flow can be apportioned only if its source and the model permit it. Equal twelfths are an explicit constant-flow assumption, not observed seasonality. Taxes, coupon payments, one-off transfers and construction milestones use their own calendars instead. Annual series cannot certify monthly observations by division.

Store money as integer pence or a declared larger unit with a checked arithmetic bound. If an evenly scheduled annual payment of `A` integer units is appropriate, set `q = floor(A / 12)` and `r = A − 12q`; the first `r` scheduled months receive `q + 1`, the others `q`. The twelve payments exactly equal `A`. For a partial year use the actual authorized schedule, not a fresh twelve-month allocation.

## M05 — Rate conversion and repricing

Every rate field declares its basis: annual effective, annual nominal with payment frequency, simple day-count accrual, or a monthly rate. A quoted annual percentage must not be applied twelve times without conversion.

- An **annual effective rate** `r` converts to equivalent monthly compounding as `(1 + r)^(1/12) − 1`, with `r > −1`.
- An **annual nominal rate convertible monthly** `j` uses `j / 12` per month. Its annual effective rate is `(1 + j/12)^12 − 1`.
- A simple-accrual contract uses `principal × stated annual rate × contract day-count fraction`. The contract supplies the denominator and calendar convention; do not presume all instruments use 365 days.
- Coupon amounts and payment dates follow the instrument, even when accrual is monthly. Accruing interest is not the same as paying it or capitalizing it into principal.

Existing fixed-rate debt retains its terms until a contractual change, maturity or refinancing. A new Bank Rate decision is not a new coupon on every outstanding government bond, mortgage or business loan. The opening Bank Rate observation is retained as an annual quoted policy rate; the [UK input register]({{ '/uk-implementation-inputs/' | relative_url }}) does not turn it into a universal lending rate.

## M06 — Taxes, payroll and transfers

Tax schedules carry effective dates and tax-year boundaries. For UK personal tax, the tax year runs 6 April–5 April; calendar April can contain transactions from two tax years. Preserve each transaction's date. The [HMRC tax-year guidance](https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past) establishes that boundary, not the historical numerical rates.

The researched 2009–10 rate/allowance extract belongs to its own year. Do not reset its full allowance every calendar month or introduce a later announced rate in January. A monthly payroll calculation must declare cumulative or non-cumulative treatment and exact statutory tables/rounding before it becomes a historical payroll implementation. For now, the annual liability fixture in the input chapter verifies the bracket arithmetic only; it does not claim payroll accuracy.

Weekly benefit entitlements and National Insurance thresholds are not monthly figures. Model scheduled eligible payments and separately accrued rights; do not treat four weeks as a calendar month. Household consumption decisions receive the cash available at their dated decision snapshot, with unpaid entitlements represented separately.

## M07 — Production, work and projects

Capacity has a rate basis. An annual production capacity can become monthly capacity only under an explicit availability profile; a stock of 100 machines is still 100 machines. Worker-months represent work used during the month; an employee counted at a monthly snapshot is a person, not a worker-year or twelve new hires.

Each project stage has `earliestStart`, `minimumDurationMonths`, `resourceBill`, `progress`, `paymentMilestones` and legal prerequisites. Preserve sourced elapsed durations in months: a two-year build remains at least 24 months when turns change. Do not convert the old phrase “one stage per turn” into a one-month building program.

For a divisible stage, the maximum fractional progress this month is the minimum of remaining work, the declared time-limited progress cap, funded labour divided by the total stage labour bill, and each allocated material divided by its total stage requirement. Consume all complementary resources in proportion to actual progress; release unused reservations. Delays do not accumulate free future throughput. An indivisible milestone needs all required inputs and prerequisites.

A stage must meet both its work completion and elapsed-time conditions. No subsequent stage uses the same resources in that monthly production pass. Commissioned capacity becomes usable at the next month's opening. A project commissioned in December 2019 is an asset in the ending balance sheet, but its January 2020 production is not an achieved campaign benefit.

## M08 — Intra-month order and interruptions

Within the month, process dated events in chronological order, then phase and stable ID for ties. Rules declare the information snapshot they read. Opening events/repricing precede offers and reservations; production and delivery follow funded input allocation; settlements update the closing state. A later receipt cannot pay an earlier obligation without actual bridge finance.

A material decision saves the month, phase, event cursor, reservations and encounter before returning control to the player. Acceptance resumes the pending action; refusal executes its declared branch. Repeated taps or reloads cannot pay twice, create a second loan, reset the event schedule or refresh reform slots. These extend the [transaction contract]({{ '/simulation/' | relative_url }}#transaction-and-interruption-behavior).

## M09 — Behavioral time scales and external events

Monthly resolution requires a monthly basis for behavioral coefficients. An annual continuous log-adjustment coefficient can be divided by 12 only when that interpretation is part of its rule; it is not a universal conversion for every coefficient. Annual historical growth divided by 12 is not a measured monthly policy effect.

For a constant-hazard event model, a full-year probability `p` would imply `1 − (1 − p)^(1/12)` monthly, not twelve independent draws each with probability `p`. This is a mathematical conversion, not authorization to add random actor decisions: deterministic actors remain the adopted design. First-release external events are a versioned dated path and fire once by event ID.

Training, contract expiration, delivery response and maintenance have explicit durations or due dates. Preserve those when changing the simulation step. No twelvefold increase in productivity, policy response or failures is implied by twelve turns.

## M10 — Monthly, annual and final reports

The normal report explains that month. December also summarizes the calendar year without another resolution pass. Fiscal-year accounts close on their own dates. Use the appropriate aggregation for each variable:

| Kind | Annual/report aggregation | Incorrect alternative |
| --- | --- | --- |
| Flow: wages paid, tax collected, actual construction spending | Sum dated transactions in the period | Sum a displayed year-to-date total twelve times |
| Stock: cash, debt, completed homes | End-of-period value, with opening and changes shown | Sum monthly stocks as if they were new assets |
| Employment rate | Sum employed person-months divided by eligible person-months | Add twelve percentages or count the same employee twelve times as jobs created |
| Inflation | Price-index ratio against the matching prior period | Multiply a monthly percentage by twelve and label it measured annual inflation |
| Real disposable income after housing costs | Deflate each month's flow at the declared monthly price index, then aggregate with cohort weights | Deflate a decade's nominal sum using an arbitrary final price |

The mandate uses January 2017–December 2019, **36 months**. Compare each metric with a commensurate opening baseline and the same-window no-change run. The original final-three-year rule is preserved, not reduced to three turns.

For income, express the 36-month total as an average annual real amount per equivalent member of the fixed opening low-income cohort; annualization is `12 × total real monthly income / total equivalent-member-months`. Eligibility and equivalence scale must be fixed before release. For employment use the person-month ratio above. For housing use the arithmetic mean of the 36 month-end affected-household counts. Show changing population/cohort size; do not reward disappearance of households as improved income.

## M11 — End conditions and future obligations

The game assesses success after December 2019 settlement. No already due public payment may remain unpaid for the mandate-success guard to pass. Future payments remain liabilities and appear in the closing schedule; a January 2020 payment is not falsely called overdue in December. Accrued but not yet due interest/tax remains visible.

Pending proposals, unfinished projects and contracts surviving the campaign keep their final status. No forced completion, debt forgiveness, hidden extra year or later expenditure occurs just to calculate the ending. Voluntary early exit yields an incomplete-term report and no normal full-campaign success award.

## M12 — Independent temporal fixtures

These are **synthetic specification fixtures**, not UK observations, gameplay outcomes or calibrated coefficients. Their inputs are chosen to expose timing/accounting errors. The committed [fixture data]({{ '/assets/data/monthly-rule-fixtures.json' | relative_url }}) are for later implementation tests.

| Fixture | Input | Independently expected result |
| --- | --- | --- |
| F01 Clock | First/last month, then finish | 0 → January 2010; 119 → December 2019; assessment January 2020; 120 playable months |
| F02 Equal-flow rounding | 10,000 pence over 12 scheduled months | Four payments of 834p and eight of 833p; total 10,000p |
| F03 Principal and nominal interest | £1,200 principal, synthetic 12% nominal rate payable monthly; no principal repayment | £12 interest/month; £144 paid over 12 months; principal stays £1,200 |
| F04 Effective rate | Synthetic 12% annual effective rate | Equivalent monthly rate approximately 0.9488792935%; twelve factors recover 1.12, not 1.12 to the twelfth power |
| F05 Stage duration | Start January 2010; minimum duration 24 months; uniform 1/24 work cap and sufficient resources | Stage can finish at December 2011 close, never December 2010; following-stage work starts no earlier than January 2012 |
| F06 End timing | Commission at December 2019 close; first operation next month | Ending asset exists; no operating output inside this campaign |
| F07 Funding shortage | Cash £100; eligible due payments £120; no approved finance | £20 unresolved funding need; no fabricated receipt; payment/recovery decision required |
| F08 Assessment window | Final three years of a ten-year monthly campaign | Indices 84–119 inclusive: exactly 36 months |
| F09 Guard dates | An obligation due 31 December 2019 is unpaid; another due 1 January 2020 is unpaid | First fails the due-payment guard; second is disclosed future liability, not overdue yet |
| F10 Clock/slots | Submit two reforms in 2010, reload, then move to January 2011 | No reset on reload or a new month; January gives two slots, with no carryover |
| F11 Rate basis | 100 homes opening; no completions or retirements for twelve months | Closing homes remain 100, not 8.33 or 1,200 |
| F12 Household annualization | 36 monthly real-income flows of £100 for one fixed equivalent member | Final-window average annual income £1,200, comparable to an annual opening baseline |

The monthly clock, rounding and arithmetic can be checked independently of the uninitialized economy. Production, payroll and national-account fixtures remain dependent on their data and detailed rules; passing F01–F12 does not certify those systems.
