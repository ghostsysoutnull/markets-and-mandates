---
title: Simulation contract
intro: Specify what changes, in what order, with which evidence and accounting obligations.
permalink: /simulation/
---

**Status:** proposed model architecture and correctness contracts. No behavioral parameters are calibrated. UK, January 2010, three connected policy areas and monthly turns are accepted. Numerical initialization and some behavioral/authority inputs remain incomplete. This chapter does not replace the conceptual mechanisms in [Economic systems]({{ '/systems/' | relative_url }}).

**On this page**

* Contents
{:toc}

## Purpose and model description

The model supports understandable counterfactual policy experiments, not national economic forecasting. Describe each implemented slice using purpose, entities, scheduling, decision concepts, initialization, input data, and submodels. This structure is informed by the [ODD protocol](https://www.jasss.org/23/2/7.html), which emphasizes explicit model descriptions and evaluation; adopting the structure is our recommendation, not evidence that our economics is valid.

Use a hybrid representation: a small number of visible actors and projects, aggregated household groups and sectors, and a limited external environment. The exact aggregation belongs to the first-slice design. Every represented stock has an owner and unit; every transition has an order and rule; omitted processes have a stated boundary.

## Authoritative state

| State group | Required information | Invariant |
| --- | --- | --- |
| Campaign | ID, scenario/version, rules/version, period, phase, revision, mandate | Revision grows only after a committed transition |
| Institutions | Authority map, authorizations, pending votes/cases, applicable mandates | Player commands cannot bypass the required decision owner |
| Treasury | Cash, fiscal flows, appropriations, reservations, debt and guarantees | Budget authorization, cash and contingent exposure stay distinct |
| Households | Group populations, incomes, assets, debt exposures, essential access | Aggregations reconcile with totals and use declared weights |
| Production | Sector capacity, employed resources, inputs, inventories, output | No output or construction beyond the declared resource rule |
| Actors | Balance sheets/resources, objectives, information, obligations, decision policy | No unexplained funds or omniscient future knowledge |
| Commitments | Contract terms, stages, dates, costs, resources, beneficiaries, cancellation terms | Completed assets and liabilities survive policy reversal |
| Financial contracts | Creditor/debtor, principal, currency, rate basis, maturity, repricing | Matching financial claims reconcile within the modeled boundary |
| External conditions | Versioned shock schedule, partner state, exchange-rate assumptions | Fixed external events remain separate from domestic responses |
| Provenance | Source IDs, rule IDs, parameter status, random state, effect journal | Reported changes trace to data and transitions |

Read models and formatted reports are derived. Do not maintain a second independently mutable GDP, welfare, or debt balance in the UI. Unknown observations are missing values with reasons, not zeros.

<a id="proposed-annual-turn-state-machine"></a>

## Monthly turn state machine

The player-facing time unit is one calendar month: 12 turns per year, 120 turns in the campaign. December adds an annual summary. The [monthly rule contract]({{ '/monthly-rules/' | relative_url }}) specifies dates, phases and temporal conversions.

| Phase | Input and output | Allowed interruption |
| --- | --- | --- |
| Briefing | Last committed state → current report and available choices | Player inspects or saves |
| Drafting | Draft policies → feasibility, costs and authority routes | Player edits or discards without economic mutation |
| Authorization | Submitted proposals → accepted/rejected/amended terms or pending encounters | Player answers an encounter; revised terms get revalidated |
| Resolution | Authorized terms and prior obligations → phased actor and resource transitions | Only explicit, persisted decision boundaries |
| Report | Validated result → explained outcomes and new obligations | Player reviews before next turn |
| Transition | Campaign rules → next period, succession or final assessment | Depends on the selected campaign rules |

Each boundary can be checkpointed. Submitting a proposal changes political/process state but does not automatically spend the appropriation. Commitment creation requires the scenario's authorization and funding route. Failed proposals leave existing services and obligations operating according to the researched fallback rules.

Within resolution, propose this explicit order: apply scheduled opening conditions; settle due obligations and expose financing needs; obtain institutional and actor decisions using the designated information snapshot; allocate feasible finance and real inputs; produce and deliver; settle wages, sales, taxes, transfers and contract payments; update inventories, balance sheets, indicators and reports. This ordering is a **candidate**, not a finalized macroeconomic closure.

Every submodel must declare which phase reads opening, intermediate, or closing values. If financing and production require iteration, define convergence, bounds and failure handling rather than looping until an arbitrary result appears. Monthly resolution is accepted. Preserve actual intra-month due dates; do not invent daily player turns. Changes in scheduling can alter outcomes and therefore require a rules version change and regression comparison.

## Transaction and interruption behavior

Resolve against an isolated candidate state. Validate command ID and expected revision; duplicate commands return the recorded result, while stale commands request a refresh. Stage effects in deterministic order, validate invariants, then atomically store the new snapshot, command result, and journal references. Publish the new authoritative state to the UI only after storage succeeds.

If persistence fails, retain the previous checkpoint and the candidate in memory for retry or export. Show the failure and do not resolve the turn again with new random draws. On process termination the last successful checkpoint remains recoverable. A resume uses a persisted cursor, pending encounter and random state; it does not rerun already committed phases.

Use a per-campaign revision check inside the storage transaction to prevent two tabs from silently overwriting one another. A disabled button alone is insufficient. Different campaigns can progress independently. A mid-turn choice is a named state, not a suspended JavaScript call stack that disappears on reload.

## Accounting before behavioral tuning

Use explicit ledgers and flows. National-account definitions are a reference for stocks, flows and reconciliation, not a demand to implement every official account. Consult the [UN System of National Accounts](https://unstats.un.org/unsd/nationalaccount/sna.asp); historical datasets must retain their own accounting-standard vintage rather than mixing revisions without explanation.

The following are bookkeeping contracts, not predictions:

- Closing cash = opening cash + recorded cash receipts − recorded cash payments. Borrowing proceeds and debt principal repayments are financing flows, separate from tax revenue and program spending.
- Closing debt principal = opening principal + issuance − repayments − write-offs + explicitly recorded valuation/other adjustments. Interest is not automatically added to principal unless the contract capitalizes it.
- Closing inventory = opening inventory + production + purchases − use − sales − losses, with units consistent and all counterparts named.
- Closing productive capacity = opening capacity + completed usable capacity − retirement − damage. Authorized or partially built projects are not completed capacity.
- Bank assets = liabilities + equity for the represented balance sheet. Insolvency can mean negative equity; do not hide it with a clamp. Liquidity is separately assessed against payments due.

Financial asset and liability entries must match where both parties are inside the modeled boundary. Use an explicit rest-of-world or residual sector for external counterparts. Valuation changes, depreciation and write-offs need dedicated entries; money is not universally conserved by a simplistic cash-transfer-only rule.

The [Bank of England's explanation of money creation](https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy) supports distinguishing loan/deposit creation from transfers of existing deposits. Our model must specify the associated borrower liability, bank asset and deposit liability, with lending constraints and repayment treatment. That source does not calibrate this game's credit response.

Appropriations authorize expenditure; reservations prevent double commitment; disbursements are actual cash flows. A guarantee records contingent exposure and eligibility first, with realized payment only on its modeled trigger. Cancellation releases only eligible unspent reservations, retaining sunk costs and termination liabilities.

Record money in a declared currency and scale using bounded integer units when feasible. Assert safe arithmetic ranges. If the scale exceeds safe integer precision, adopt a tested decimal or integer representation and explicit serialization. Rates and quantities use declared precision, rounding, and domain-specific tolerances. Never mix percent with decimal fractions or nominal with real values silently.

## Behavioral rule sheets

Before implementing a rule, fill this contract in the task's owning model section or a dedicated linked rule file:

| Field | Required content |
| --- | --- |
| Identity | Stable rule ID, version, owner and requirement IDs |
| Purpose | Player question and observable mechanism |
| Inputs | State variables, units, information date and visibility |
| Preconditions | Authority, funding, counterparties, real resources |
| Calculation | Equation or unambiguous algorithm, order, bounds and rounding |
| Parameters | Values/ranges, source or explicit design assumption, sensitivity plan |
| Outputs | State changes, ledger postings, structured explanation, delays |
| Failure | Rejection, shortage, insolvency, non-convergence or missing input behavior |
| Validation | Hand-calculated fixture, boundary case, alternative branch, evidence limit |

No rule is implementation-ready merely because its output is “growth +2.” A policy alters explicit mechanisms. Actor decisions rank feasible actions under declared motives and information, and explain why an option was chosen. Unknown private information is not exposed to the player as fact. Ownership can change objectives and authority while physical resource requirements remain comparable.

## Randomness and replay

Recommend a pinned pseudorandom algorithm, saved state, stable entity ordering, and named independent streams for external shocks and endogenous actor behavior. Do not use wall-clock time, network responses, unordered iteration, or `Math.random()` inside model resolution. The algorithm and draw schedule are pending engineering choices requiring reference vectors and tests.

For policy comparisons, key shared external shocks by scenario, period, and event identity so an extra domestic decision does not shift the next external draw. Endogenous responses may legitimately diverge. A seed alone is insufficient: content, parameters, rules, ordering and algorithm versions must match. Old saves may resume through migration without promising exact replay under new rules.

## Reporting and validation limits

An effect trace explains what happened inside the model. It is not an econometric estimate of a policy's real-world causal effect. Reports separate authorization, legal status, financing, execution, distribution and aggregate indicators. Show observed simulation values separately from actor promises and projected effects.

Before the first economic slice is ready, resolve allocation/rationing, prices and wages, credit constraints, public financing, external trade and currency treatment at the selected aggregation level. Supply a reconciled initial state, parameter register and alternative-policy fixtures. These remain open work, not results implied by this chapter. See [verification]({{ '/verification/' | relative_url }}) for accounting, sensitivity and plausibility checks.

## Campaign rule specification

The [campaign design]({{ '/campaign-design/' | relative_url }}) specifies the accepted ten-year UK campaign with 120 monthly turns with income/employment, enterprise investment and England housing. The direction is accepted; this is still not a validated runnable nation pack. The following rule inventory replaces vague policy bonuses with identifiable calculations. It is not yet a calibrated numerical model: missing coefficients and input definitions remain release blockers for the dependent rules.

### Units, information and settlement

Use nominal GBP for accounts, price-indexed GBP for comparisons, persons for population/employment, worker-months for monthly labour capacity, homes for housing and declared sector-specific units for output. Money precision and safe bounds follow the accounting contract. Never sum physical units across unlike sectors. Each calculation records its rule version and input snapshot.

Monthly ordering: opening events and contractual repricing → authorization and budget → actor offers based on opening information → finance and resource reservations → production/project stages → cash settlement → closing prices, balance sheets and reports. Closing prices and capacity affect next month's decisions. This deliberately uses lagged information instead of an unspecified simultaneous equilibrium.

Planned household and firm orders use opening information and expected income; actual closing income revises next month's plan. Settlement records realized purchases subject to available balances and authorized credit, with unfulfilled orders retained as unmet demand. A period's production finance must be reserved before output. Wage, input and financing payments have identified payers and recipients; receipts unavailable at the required date cannot fund an earlier payment without bridge finance. Dates within each month preserve legal budget, tax and debt deadlines. Calendar turns do not change the fiscal year or personal tax year. If an unresolved funding failure needs a player decision, persist the encounter before continuing.

### Rule inventory

| ID | Proposed calculation or algorithm | Inputs still required |
| --- | --- | --- |
| C01 Budget and tax | Apply each authored marginal tax schedule to its defined base by household/firm group; multiply per-member results by weights. Benefits use eligibility and amount schedules. Post liabilities, collections, arrears and disbursements separately. Borrowing is financing, never tax revenue. | Matched bases, schedule dates, coverage, collection/processing delays and operating spending outside the catalogue |
| C02 Credit | Evaluate capital, liquidity, collateral and repayment conditions before ranking loan requests by expected net return. Reserve capacity after every accepted offer. Create matching loan asset and borrower debt, with the associated deposit liability and holder's deposit asset; record cross-bank settlement where required. | Bank balance sheets, period-specific constraints, loss assumptions, maturity/rate terms, guarantee eligibility and central-bank settlement treatment |
| C03 Fiscal finance | Due coupons use their contract rates; only repricing/maturing cohorts take new terms. Match proposed issues to modeled investor offers, reserve subscriptions and settle proceeds/redemptions. Uncovered finance creates a financing encounter, never automatic unlimited borrowing. | Investor portfolios, offer/yield behavior, debt schedule, financing authorities and default/restructuring treatment |
| C04 Goods production | Feasible output is the minimum of usable capacity, available labour divided by labour per unit, and each required input divided by its input coefficient. Planned output is limited by expected sales and the inventory target. Actual production cannot exceed feasible output. | Sector units, input coefficients, inventories, capacity, demand expectations and inventory targets |
| C05 Resource allocation | Existing legally binding reservations precede new requests. Remaining units go to feasible funded bids by offered price, then a stable ID tie-break. Publicly controlled inputs may instead follow the authorized priority order. A physical unit can be allocated once only. Partial allocations reduce the corresponding feasible activity. | Reservation dates, bids, common pools, supplier availability and authority to direct public resources. This is an explicit simplifying allocation assumption, not a claim about all UK markets. |
| C06 Projects | Each stage has required labour, materials, legal prerequisites and payments. Progress fraction is capped by the least available required resource fraction and remaining work; all resources consumed follow that progress fraction. Inseparable milestones require full inputs. No new stage starts in the same monthly production pass. Commissioned assets become usable next period. | Bill of resources, stage divisibility, inherited progress, carrying/termination costs and commissioning conditions |
| C07 Households and demand | Disposable income equals wages + distributed income + transfers − direct taxes. Deduct contractual housing/debt payments; allocate available resources to the specified essential basket, then discretionary demand and saving using the registered rule. Unaffordable bills create explicit arrears or reductions in feasible consumption. | Joint group weights, essential basket, consumption/saving response, tenure, credit access and arrears rules. Loan principal repayment is a cash use, not an income expense. |
| C08 Prices and wages | Candidate lagged adjustment: next price = current price × exp(a × normalized excess demand); next wage uses the same form with excess labour demand and a separately registered coefficient. Normalize goods imbalance by max(available supply, one declared unit); normalize labour imbalance by max(available workers, one worker). Contract-fixed prices/wages follow their contract until repricing. | Coefficients, bounds on monthly log changes; annual log-response coefficients convert by division by 12 only under the declared continuous-adjustment interpretation, treatment of administered prices, vacancies and employment matching. These adjustment equations are design hypotheses, not estimated facts. |
| C09 Investment and employment | Private projects require positive expected discounted net cash flow after financing/tax effects and must pass resource/finance checks. Public projects follow their explicit mandate within authorized resources. Labour hires follow feasible production and skill matching; training adds eligible skills only on completion. | Forecast rules, discount basis without double-counting financing cost, horizons, wage offers, training completion and separations. No automatic jobs multiplier. |
| C10 Monetary and external conditions | Monetary committee uses a registered lagged inflation/activity reaction rule; financial contracts then reprice according to their dates. External demand, foreign prices and exchange-rate paths are versioned scenario inputs for the first campaign, with domestic quantities responding through orders and input costs. | Reaction-function form/coefficients, inflation basket, activity reference and external paths. Exogenous exchange rates are a disclosed simplification, not a claim that sterling ignored domestic policy. |
| C11 Distribution and assessment | Derive income and employment from the journal and household weights. Use the fixed mandate definitions and final-three-year comparison specified in the campaign design. Track debt, guarantees, unfinished assets and unpaid obligations separately. | Opening cohort membership, price deflator and housing affordability/suitability definition. Definitions must precede scenario release. |

Sales consume inventory and transfer payments; excess demand is recorded rather than sold twice. Aggregate national output must be derived from value added at a consistent price basis, avoiding intermediate-input double counting. The remaining domestic sector and external accounts must close explicitly; an unexplained balancing transfer is not a model solution. Financial defaults reduce named claims and equity rather than deleting mismatches.

### Finite model completion and checks

Complete every inventory row with values, lawful routes, counterpart postings, failure behavior and independent fixtures before implementing its dependent outcome. A parameter can be an explicit game assumption where evidence cannot identify it, but it must be justified, reviewed and sensitivity-tested, never presented as a measured UK coefficient. Historical starting values cannot be substituted with illustrative numbers in the released campaign.

Required fixtures cover: no policy change with maturing debt; a public project competing with a private project for the same labour; a denied loan despite a guarantee offer; insufficient materials delaying a funded project; cancellation retaining sunk cost and termination liability; and final-year asset sale failing to masquerade as recurring income. Fixtures are test inputs, not gameplay evidence, and have not yet been calculated or executed.

Parameter sensitivity must compare both public and private delivery under common resource rules and external events. The final campaign report must label the no-change comparator as a simulation. No historical causation or phone usability result follows merely from completing these rule sheets.
