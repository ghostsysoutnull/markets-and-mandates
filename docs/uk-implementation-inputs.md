---
title: UK implementation inputs
intro: Sourced opening facts, authority routes and the exact dependencies of the accepted monthly campaign.
permalink: /uk-implementation-inputs/
---

**Status:** focused P2b/P3 work is authorized. The user adopted the UK campaign with **12 monthly turns per year**, January 2010–December 2019. This register records actual evidence and completed temporal rules; it does not certify a reconciled national opening state or a calibrated economy. Read the [monthly rules]({{ '/monthly-rules/' | relative_url }}) for time handling and the [UK profile]({{ '/nation-uk-2010/' | relative_url }}) for the established broad research. Do not repeat nation selection.

**On this page**

* Contents
{:toc}

## Opening evidence extract

The downloadable [UK opening evidence CSV]({{ '/assets/data/uk-opening-evidence.csv' | relative_url }}) contains a deliberately separated set of tax rules, a monetary observation and fiscal forecasts. Every row has a period, unit, source, locator, publication date, information status and permitted use. **It is an evidence extract, not a loadable campaign save.** The brief source summaries below do not claim that forecasts were enacted authority or observed outcomes.

### Personal income tax and National Insurance

For 2009–10, the standard under-65 personal allowance is £6,475; the basic taxable band is £37,400, with non-savings rates of 20% and 40%. Standard employee NICs use weekly thresholds £110 and £844, rates 11% and 1%; employer NICs use 12.8% above the £110 secondary threshold. The £95 weekly lower earnings limit affects entitlement treatment. Age allowances and contracted-out schemes differ; these standard values cannot initialize every household. [T01, pp. 7–10](#source-register)

The CSV retains annual and weekly units. Payroll periods, benefit interactions and opening cumulative pay/tax are still needed. Taxing the income of a whole quintile once as if it were one person would be wrong: calculate by supported representative tax unit, then apply its population weight.

### Monetary opening observation

On 10 December 2009 the MPC retained Bank Rate at 0.5%. Its £200 billion announced purchase programme was still being completed; the release reports £188 billion purchased. These are distinct quantities. Neither is a Treasury spending balance, and the stock measured on 10 December is not certified as the stock on 1 January. [T02](#source-register)

### Fiscal information known at opening

The December 2009 Pre-Budget Report's table B13 estimates fiscal 2009–10 receipts at £498.1bn, current expenditure £607.0bn, depreciation £19.2bn, gross investment (net of asset sales in that table) £68.7bn and net borrowing £177.6bn. Its projected £798.9bn net debt is an end-March measure. These are opening-known estimates for a fiscal year, not January cash or realized monthly flows. The table excludes temporary financial-intervention effects; preserve that boundary. [T03, table B13](#source-register)

As an accounting cross-check on the displayed rounded values: net investment is 68.7 − 19.2 = 49.5; current surplus is 498.1 − 607.0 − 19.2 = −128.1; borrowing is 49.5 − (−128.1) = 177.6, all £bn. This reconciles those forecast aggregates only. It cannot recover a debt maturity ladder, bank claims, expenditure already used or monthly Treasury balances.

## Concrete authority routes

The following map binds each adopted package to a real decision route and identifies the missing detail needed to make it executable. “Evidence checked” is deliberately narrower than “all conditions certified.” Legal text as enacted is not automatically the consolidated law at the opening date.

| Route | Owner and sequence | Refusal or delay behavior | Evidence and remaining dependency |
| --- | --- | --- | --- |
| UK-A01 Annual authority and monthly payments | Treasury/department proposal → parliamentary Supply authorization → expenditure within purpose, resource/cash ceiling and dates → actual cash settlement | A refused increase gives no new authority. Retain legally valid existing authority and liabilities; do not renew expired powers automatically. | T04 supports the structure. Still need actual January outstanding appropriations, expenditure-to-date and expiry/contingency rules per account. |
| UK-A02 Income-tax change | Government tax proposal → relevant Finance legislation/resolution → effective dated schedule → HMRC collection process | Maintain the lawful current schedule until a valid change takes effect; a proposal is not a tax receipt. | T01 establishes opening rates, not every parliamentary collection procedure. Finalize authority for interim collection and existing enacted future changes. |
| UK-A03 Benefit/support change | Identify the particular scheme, jurisdiction and administering body → statutory/delegated change where required → funded administration and dated entitlement | Wrong body or unsupported eligibility rule cannot create entitlement; unpaid valid claims remain recorded. | UK profile UK14 identifies schemes and territorial cautions. A single universal “benefit power” is not certified; identify each launch scheme and its 2010 operative rules. |
| UK-A04 Employment/training contract | Relevant minister/agency and lawful program → budget authority → provider contract → funded places → dated completion | Lack of capacity reduces accepted places or delays delivery; grants do not instantly create skills or jobs. | Specific training program, provider capacity and operative power remain to be selected within accepted employment scope. This is a design route awaiting its precise legal record. |
| UK-A05 Conditional industrial assistance | Relevant industrial-support power → Treasury consent/required parliamentary approval → scheme eligibility and applicable subsidy review → grant/loan/guarantee agreement → milestones and monitoring | Ineligible project, withheld consent or unfunded offer creates no support; guarantee liabilities follow the actual contract. | T05 section 8 and T06 establish a concrete route, with limitations below. Scheme and opening statutory headroom still require completion. |
| UK-A06 Public enterprise investment/acquisition or disposal | Identify enterprise and share rights → transaction authority, valuation and funding → shareholder/company consents → competition/subsidy review where applicable → transfer named assets/claims/control | Declined sale leaves ownership unchanged; an accepted price transfers value rather than generating free capacity. | UK profile UK09 plus T05 identify research routes. No generic power to seize or sell any enterprise is asserted. Asset-specific statutes, share rights and counterpart balance sheets remain required. |
| UK-A07 England housing delivery | Housing/program authority → HCA/ministry or local route → land/planning/procurement conditions → delivery agreement → stage payments → landlord/service obligations | Funding alone creates no planning permission. Failure leaves the prior stage, valid commitments and carrying costs intact. | T07 section 19 specifies a financial-assistance route. Opening commencement/amendment coverage, consents, local powers, procurement and applicable social-housing conditions still need certification. |
| UK-A08 Delivery/market rules | Identify rulemaker and jurisdiction → enactment/delegation → staffed enforcement → review/remedy | Unlawful executive order is unavailable; legal delay has a dated effect, not a random popularity penalty. | UK profile UK03/UK10. Each authored reform needs an operative legal test and remedy; do not certify an unspecified regulation. |
| UK-A09 Monetary decision and bank distress | MPC policy decision independent of cabinet; bank intervention uses the distinct Treasury/FSA/Bank route | Fiscal preference cannot set Bank Rate or force a loan. Failed bank obligations require a specific resolution route. | UK profile UK05–UK08 and T02. Detailed bank balance sheets, intervention triggers and applicable powers still required. |
| UK-A10 Confidence and succession | Separate ordinary package defeat from a confidence/authority crisis; follow government-formation route and retain obligations | Rejection is not automatic dissolution; a successor inherits the ledger and negotiates its mandate. | UK profile UK01/UK03. Historical opening chamber composition and authored successor mechanics remain incomplete. |

### Industrial assistance: verified constraints

The 1982 Act's enacted section 8 requires Treasury consent and conditions concerning economic benefit, national interest and the need for ministerial assistance. Its share-acquisition route requires company consent; it excludes acquisition/assistance of banks and insurers under that section. It also provides a Commons-resolution threshold and an urgency exception. **Do not import the original aggregate limit as a 2010 value.** T05 is the original text; the operative amendment chain still needs completion. [T05](#source-register)

The 2009–10 departmental report confirms that the 2009 amendment raised the initial section-8 ceiling to £12bn, with specified further increases possible. That statutory ceiling is not unused January funding. The report also describes regional/devolved exercise and the Enterprise Finance Guarantee, which supported qualifying bank loans rather than instructing banks to lend. Later March totals cannot initialize January commitments. [T06, paragraphs 2 and 12–30](#source-register)

### Housing assistance: verified route, bounded claim

The enacted Housing and Regeneration Act permits the HCA, with Secretary of State consent, to provide financial assistance, including grants, loans, guarantees and investment, on conditions. Housing-specific provisions impose additional conditions. This identifies the institution and instrument; it does not prove that an arbitrary housing package bypasses planning, local delivery, procurement or subsidy constraints. The dated consolidated HTML could not be retrieved through the research tool; its PDF was read, and opening commencement/amendment certification remains explicit work. [T07, sections 19 and 31–35](#source-register)

## Calculation ready now: limited annual income-tax liability

This rule is ready as **a limited numerical specification**, not as a whole payroll or population model. It covers a 2009–10 standard-allowance under-65 tax unit with non-savings income, no special relief and no other tax-category interaction. Let annual gross income be `Y`, allowance `A = 6475` and taxable income `X = max(0, Y − A)` in GBP:

`annualLiability = 0.20 × min(X, 37400) + 0.40 × max(0, X − 37400)`.

Historical inputs come from T01. Keep this function separate from collection dates, NICs and transfers. It cannot establish the tax on aggregated average households without tax-unit distributions; it cannot be silently applied to future tax years. In particular, the opening pack must retain already enacted future changes while distinguishing merely announced measures.

**Synthetic arithmetic fixtures:** gross incomes £6,475, £20,000, £43,875 and £50,000 yield annual liabilities £0, £2,705, £7,480 and £9,930 respectively. These invented incomes test arithmetic and bracket boundaries; they are not UK household observations or a released scenario. Reproduction checks verify the calculation, not HMRC payroll rounding or complete tax coverage.

## Input completion ledger

No empty field is treated as zero or replaced by a plausible national stereotype. This is the concrete remaining work for A–D in the adopted design, with temporal components separated so a future implementation packet can use ready contracts without pretending the whole economy is ready.

| Artifact/component | Current state | Exact missing input or decision |
| --- | --- | --- |
| Calendar, temporal aggregation, final window | Specified in M01–M12; arithmetic fixtures provided | Production implementation and tests remain future work. |
| Standard 2009–10 tax/NI parameters | Source extract checked | Full tax categories, statutory future changes, payroll collection tables, tax-unit distributions and opening cumulative records |
| Opening monetary setting | December rate/programme observations checked | January balance-sheet reconciliation; private lending terms, repricing cohorts and a researched monetary reaction rule |
| Public opening accounts | Opening-known fiscal estimates extracted and cross-checked | Actual dated stocks, debt instruments, creditor/currency/maturity breakdown, authorities used/remaining, due payments and counterpart mappings |
| Household opening groups | Broad source inventory exists | Joint income/employment/tenure groups and weights, tax units, debt/deposits, essential costs, eligibility and fixed cohort/equivalence definitions |
| Production and projects | Three-sector representation and C04–C06/M07 algorithms specified | Consistent sector units, input coefficients, inventories, capacity, existing contracts, stage resource bills and sourced durations |
| Bank and external accounts | Accounting boundaries specified | Reconciled opening assets/liabilities/equity, liquidity/capital constraints, offers/loss assumptions and external counterpart balances |
| Legal routes | Concrete map above; evidence checked within stated scope | Operative versions, package-specific authorities/conditions and dates, opening chamber weights and fiscal fallbacks |
| Behavioral parameters | C07–C10 dependencies identified | Consumption/saving, forecasts, investment discounting, wage/price response, loan risk and monetary-response specification with evidence and sensitivity ranges |
| Household/housing mandates | Direction and monthly aggregation adopted | Complete fixed opening cohort; affordability/suitability definition and source matching; comparable opening and no-change metrics |
| Reconciled policy alternatives | Temporal and limited-tax fixtures calculated | Public/private/no-change trajectories with matched accounts, shortages, cancelled contracts, refused finance and distribution outcomes |

The full P2b/P3 campaign pack is **in progress**, not complete. The next dependent work is reconciling opening public accounts and household tax/transfer inputs; banking and production must also reconcile before an integrated economic run can be certified. Authoring a source list alone does not satisfy that acceptance criterion. Do not request campaign adoption again or start another six-nation research round.

## Source register

Sources checked 25 September 2026. Only facts needed for included mechanics are extracted. Historical sources may discuss excluded subjects; those sections do not become gameplay mechanics. Public access alone does not authorize bulk redistribution. The CSV is a small attributed fact extract, with licensing status recorded; source publications are linked rather than republished.

| ID | Primary source and locator | Applicability and rights |
| --- | --- | --- |
| T01 | Commons Library, [Direct taxes: rates and allowances 2009/10, RP09/38](https://researchbriefings.files.parliament.uk/documents/RP09-38/RP09-38.pdf), 27 April 2009; printed pp. 7–10 and table 1 p. 12 | Contemporary opening-year rates; future announcements distinguished. Parliamentary copyright; small numerical facts attributed, no text/table facsimile redistributed. Full packaged reuse terms still need review. |
| T02 | Bank of England, [10 December 2009 MPC release](https://www.bankofengland.co.uk/-/media/boe/files/news/2009/december/mpc-december-2009.pdf), release and note to editors | Opening-known decision and observation; programme size is not completed holdings. Bank copyright; small attributed observations only. |
| T03 | HM Treasury, [Pre-Budget Report, Cm 7747](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/238510/7747.pdf), December 2009; table B13, printed p. 189 | Fiscal forecasts with their exclusion boundary, not opening balance sheet or appropriation. Crown copyright; document permits accurate attributed reproduction excluding identified third-party material/logos. |
| T04 | HM Treasury, [Main Supply Estimates 2010–11, HC 269](https://www.parliament.uk/globalassets/documents/commons-expenditure/supply-estimates/2010-11-main-supply-estimates-central-govt.pdf), 7 July 2010; sections 2–3 | Later publication describes established procedures; do not backdate July amounts. Crown copyright; document reuse terms with exceptions. |
| T05 | [Industrial Development Act 1982, as enacted](https://www.legislation.gov.uk/ukpga/1982/52/pdfs/ukpga_19820052_en.pdf), sections 7–8 | Original statutory powers/limits; amendments and applicability require dated reconciliation. UK legislation under Crown rights and the site's reuse terms. |
| T06 | BIS/Scottish/Welsh administrations, [Industrial Development Act annual report 2009–10, HC 348](https://assets.publishing.service.gov.uk/media/5a7b91d7e5274a7318b8f853/0348.pdf), 27 July 2010; paragraphs 2, 12–30 | Retrospective evidence of period powers/schemes; later closing totals not opening data. Crown copyright; accurate attributed text reuse permitted with document exceptions. |
| T07 | [Housing and Regeneration Act 2008, as enacted](https://www.legislation.gov.uk/ukpga/2008/17/pdfs/ukpga_20080017_en.pdf), sections 19 and 31–35 | Financial-assistance route; commencement and amendment chain remain to certify for January 2010. UK legislation under Crown rights and site's reuse terms. |

**Preferred next work:** complete the remaining public-account and household inputs, then their reconciled fixtures, under the user's existing option-1 authorization. **Alternative:** review the monthly pacing interpretation while independent evidence work continues. Neither option changes the selected UK campaign or requires a prototype.
