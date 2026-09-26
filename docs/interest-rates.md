---
title: Interest rates & monetary choices
intro: One monetary decision can change borrowing conditions across the economy, but its effects depend on lenders, borrowers, contracts, and time.
permalink: /interest-rates/
---

**On this page**

* Contents
{:toc}

## Several connected rates

Interest rates belong in the core simulation. The central-bank policy rate should influence financial conditions, while private lenders and the market for government debt respond to their own constraints. Do not give the entire economy one rate that changes every contract immediately.

| Rate | Proposed decision mechanism | Player-visible consequence |
| --- | --- | --- |
| Central-bank policy rate | The monetary institution chooses within its mandate and independence arrangements | Influences financial conditions and the institution's response to inflation or recession |
| Household and business borrowing rates | Lenders price loans using funding costs, expected losses, capital needs, collateral, and competition | Changes affordability, investment, and debt-service pressures |
| Government borrowing costs | Financing arrangements and investor demand, influenced by expected monetary policy and other risks | Changes the cost of new debt and refinancing |
| Deposit rates | Banks compete for funding under their balance-sheet and market conditions | Changes savers' income and banks' funding choices |

The first view can emphasize the first three categories and reveal relevant deposit and loan rates in actor details. These are proposed mechanisms, not calibrated equations. The [Bank of England's account of monetary transmission](https://www.bankofengland.co.uk/quarterly-bulletin/2024/2024/about-a-rate-of-general-interest-how-monetary-policy-transmits) provides the initial evidence base for interest-rate channels and their dependence on economic structure.

## Who makes the decision

The player is the executive leadership. When the central bank is independent, it makes its own rate decision according to its mandate and assessment of conditions. The player can anticipate the response, communicate policy plans, and adjust fiscal or structural policies.

Where the executive has lawful monetary control, represent that authority explicitly. Changing who has control requires a valid institutional route; a disagreement with one rate decision is not enough to change the arrangement.

In a currency union, the monetary institution responds to the wider area. In the modern German scenario, the player cannot set an independent German policy rate. See the [ECB's institutional overview](https://www.ecb.europa.eu/ecb/orga/escb/html/index.bs.html).

## How the central bank responds

Give the institution a mandate, information set, policy stance, and explanation of its decision. Depending on its framework, relevant conditions can include inflation, employment, economic activity, expectations, exchange-rate pressures, and financial stress.

The bank should recognize uncertainty and distinguish a demand expansion from a supply disruption. Interest-rate policy can affect spending and financing; it does not immediately supply missing fuel, homes, or trained workers.

The player should see a conditional assessment before a major decision: a fiscal package may increase pressure for tightening under particular conditions, rather than guaranteeing a precise rate change. After the turn, the monetary report should explain the actual response and the evidence considered.

Avoid an automatic rule that every spending increase causes a hike, every recession causes a cut, or every hike eliminates inflation in one turn. Mandates, starting conditions, and lags matter.

## From the policy rate to actual borrowing

Banks respond through new loan offers, refinancing terms, deposit pricing, and lending standards. A bank with large expected losses may keep lending expensive or restrict credit after the central bank cuts rates. A healthier competitor may behave differently.

Borrowers also decide. A firm may decline an attractive loan if demand is weak; another may continue investing despite higher rates because it has strong orders or internal funds. The game's credit mechanism should include both the willingness to lend and the willingness and ability to borrow.

Loan guarantees can alter a lender's exposure but create public obligations. Subsidized lending changes who pays part of the financing cost; it does not remove the cost of equipment or labor. These tools remain distinct from changing the policy rate.

## Contracts, refinancing, and time

Track broad categories of existing debt and new borrowing. Fixed-rate obligations retain their contracted rates until the relevant refinancing or maturity event; variable-rate obligations change according to their contract terms. A new policy rate should not instantly reprice the entire government's debt stock or every household mortgage.

For each group, report how much debt is exposed soon, the expected payment change, and the timing. The first design can use aggregate maturity groups instead of tracking individual contracts.

A reduction in new lending today may slow future construction and investment. Conversely, lower rates may take time to affect production. The monthly turn and annual summary should explain delayed transmission even if the internal sequence is simplified.

## Inflation and real borrowing conditions

Distinguish the quoted nominal rate from the burden relative to expected inflation when explaining investment and borrowing incentives. Actual household affordability also depends on income and required cash payments; expected inflation does not itself provide cash to meet a repayment.

Reported interest rates, inflation expectations, and observed inflation need separate labels. Do not imply that a precise real borrowing cost is known in advance when future prices are uncertain.

This is an educational distinction to introduce when relevant, not a requirement for the player to solve financial formulas each turn.

## Government borrowing and fiscal tensions

The budget should show interest on existing obligations separately from the estimated cost of new borrowing. Expected policy rates, inflation, maturity, currency, liquidity, and perceived repayment risk can influence financing conditions under the proposed model.

Financing arrangements must fit the national profile. A single universal risk surcharge or debt threshold would obscure the differences between domestic-currency debt, foreign-currency debt, and currency-union membership.

Higher financing costs can constrain a proposed program even when lawmakers support its objective. The executive can revise timing, taxes, spending, or financing terms within its powers. It cannot simply order investors or private banks to accept any desired return without a distinct and available policy mechanism.

## Distribution and the report

Show which households and enterprises are borrowers, savers, or both. A rate change may affect new buyers, existing fixed-rate borrowers, indebted firms, and depositors differently. Banks also face changes on both sides of their balance sheets.

The report should connect policy rates, actual offers, credit volumes, refinancing pressure, investment plans, employment, and prices. Separate the contribution of monetary conditions from simultaneous shocks or fiscal changes; do not assign every outcome to the latest rate decision.

## Example and remaining design work

The [housing authorization scenario]({{ '/scenarios/' | relative_url }}#housing-legislation-courts-and-interest-rates) shows a supported program facing judicial delay and changing finance costs. The [housing and banking scenario]({{ '/scenarios/' | relative_url }}#housing-credit-and-bank-distress) follows lender risk and financial distress.

Open details include the number of visible loan categories, monetary decision timing within a monthly turn, expectation formation, and the treatment of tools beyond the policy rate. The concept commits to distinct rates, institutional authority, actor responses, and delays; exact numerical relationships remain to be researched and tested.
