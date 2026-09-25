---
title: Economic systems
intro: Policy changes the rules. Households, enterprises, banks, and public institutions respond.
permalink: /systems/
---

**On this page**

* Contents
{:toc}

## Several dimensions, not one score

Ownership, allocation, competition, public provision, redistribution, and openness should vary independently. Public healthcare does not by itself establish central planning; private ownership does not guarantee competition.

Each sector can combine arrangements. For example, a proposed electricity model could distinguish ownership of generators, regulation of the grid, investment planning, and household subsidies.

The sections below describe proposed model behavior. They establish conceptual relationships and questions to test, not numerical equations or universal estimates of real-world effects.

## Central banks and monetary policy

Each nation begins with a historically grounded monetary arrangement:

- **Mandate:** priorities such as price stability, employment, or exchange-rate stability.
- **Independence:** who has authority over decisions and what influence the government has.
- **Tools:** interest rates, emergency lending, asset purchases, and directed-credit arrangements where appropriate to the country and period.
- **Credibility:** how households, firms, and investors respond to the institution's commitments.

Where the bank is independent, it responds to economic conditions within its mandate. The player must anticipate that response. Changes to its mandate or independence are institutional reforms, subject to the nation's legal and political constraints.

Interest-rate changes should influence borrowing conditions, spending, investment, and eventually inflation, with delays and unequal effects. The [Bank of England's account of monetary transmission](https://www.bankofengland.co.uk/quarterly-bulletin/2024/2024/about-a-rate-of-general-interest-how-monetary-policy-transmits) supports this mechanism; the precise simulation rules remain to be designed.

An inflationary supply shock should create a dilemma. Interest rates influence demand and financial conditions; they do not immediately manufacture missing fuel or equipment. The model must distinguish sources of inflation rather than treating every price increase identically.

Germany requires a special constraint in the modern scenario: monetary policy belongs to the Eurosystem. A German player cannot independently set a national policy rate. See the [ECB's institutional overview](https://www.ecb.europa.eu/ecb/orga/escb/html/index.bs.html).

The player should receive a policy explanation from the monetary institution: which conditions motivated its action, which effects are expected, and where uncertainty remains. Asset purchases, government transfers, and bank rescues should have distinct purposes and costs rather than sharing one generic money-creation action.

Changing independence should alter who decides and how expectations may form. It should not grant an automatic prosperity bonus or trigger an inevitable crisis. The institutional design, fiscal commitments, economic conditions, and record of delivery must matter.

The dedicated [interest-rate chapter]({{ '/interest-rates/' | relative_url }}) distinguishes the policy rate, private loan rates, government financing costs, and deposit rates. It explains lender responses, fixed and variable contracts, refinancing delays, and the executive's limits when monetary decisions are independent.

## Commercial banks and credit

Represent who receives financing: households, small businesses, property developers, productive enterprises, or state enterprises. Lending standards, defaults, public development banks, and banking distress should affect the choices available in the economy.

Modern bank lending can create deposits. Banks should not function as a fixed box of previously saved money, nor should lending be unlimited. The [Bank of England's explanation of money creation](https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy) provides the initial reference.

The conceptual distinction matters: fiscal spending, commercial lending, and central-bank operations are related but different actions. Avoid a universal government “print money” button.

Private banks now have a dedicated [NPC specification]({{ '/actors/' | relative_url }}#private-banks), including lending choices, capital and liquidity constraints, government influence, and distress. Their behavior connects monetary policy to the firms and households that actually seek loans.

## Government finances

Track revenue, recurring expenditure, investment, deficits, accumulated debt, and interest payments. Existing commitments continue into future turns.

Borrowing conditions should depend on the institutional and economic context, including debt currency and maturity. Borrowing in a nation's own currency and owing foreign currency should not be interchangeable. A shared debt-to-GDP threshold should not automatically trigger identical crises in every nation.

Exact financing rules and crisis thresholds require research and calibration. Fiscal constraints should be understandable without turning every decision into accounting work.

Player choices include the tax mix, enforcement resources, spending priorities, borrowing, and the pace of adjustment. Tax design should distinguish rates, coverage, and actual collection; increasing a headline rate does not guarantee a proportional revenue increase.

Show the budget cost and the real-resource requirement of a policy separately. Public borrowing can finance an order, but the project still needs workers and materials. In a downturn, unused capacity may change the effects of additional spending. Under supply constraints, the same nominal spending can instead intensify competition for scarce inputs.

Debt interest should respond as relevant obligations refinance or rates reset, rather than repricing every fixed-rate liability instantly. Guarantees may produce no initial cash outlay but create obligations later. These distinctions keep short-term budget relief from hiding future costs.

## Production and supply chains

Begin with broad sectors: food, energy, manufacturing, housing, and services. They require labor, equipment, infrastructure, and inputs from other sectors or abroad.

Funding becomes output only through an implementation process. A power station takes time to construct; training doctors takes time; a factory cannot meet its target without components.

Scarce inputs create bottlenecks. Both public plans and private investment can encounter them. Investment in capacity can improve future choices while imposing present costs.

The player can support capacity, coordinate public procurement, alter ownership, or impose production priorities where available. Producers then adjust within their equipment, skills, inputs, and financing. Quality, maintenance, and inventories matter alongside headline output: achieving a quantity target by exhausting equipment or producing unusable goods should be visible.

Public service capacity follows the same principle. Expanded eligibility for healthcare is a commitment; staffing and facilities determine how much care is delivered. Track access, quality, and waiting where relevant so a spending increase is not automatically scored as an equal service improvement.

## Labor and households

Use a small set of representative household groups to show wages, employment, access to services, assets, debts, and exposure to prices. The initial categories remain undecided.

Labor policy includes bargaining arrangements, training, worker protections, and mobility. Demographics and migration affect available workers and demand for services over time.

Households should respond to conditions. Their consumption, saving, borrowing, and labor choices help connect policy with production and living standards.

The player can influence disposable income and opportunity through taxes, benefits, services, training, and labor rules. A proposed reporting set includes low-income renters, indebted working households, asset-owning households, and retirees, with overlap handled carefully rather than counting the same people twice.

Reports should use real purchasing power as well as nominal income. A wage increase, tax reduction, or benefit expansion may have different implications when rent, food, or energy costs change. Training and migration effects should respect time, suitable jobs, housing, and public-service capacity.

## Trade, currencies, and external dependence

Imports, exports, exchange rates, foreign financing, and access to strategic inputs connect the nation to the world. Domestic purchasing power does not guarantee access to imported machinery or fuel.

The first game can use an external world model rather than simulating every other nation in full. Commodity shocks, demand changes, trade restrictions, and financing conditions can create distinct exposures for each starting nation.

Currency arrangements and trade obligations belong in the historical profile. Players should not gain mutually incompatible monetary powers through unrelated toggles.

The [trade chapter]({{ '/trade/' | relative_url }}) develops the actual player actions, negotiated agreements, foreign NPC responses, and policy evaluation. Domestic competition, ownership, and international openness remain separate dimensions.

## Institutions and political power

Administrative competence, courts, procurement, corruption, lobbying, unions, and political support shape what gets implemented and who benefits.

Institutional quality should be changeable and specific. Avoid assigning a permanent national “efficiency” trait. Public and private organizations can both suffer from weak oversight or capture.

Political resistance should have an explanation: a group loses income, fears unemployment, faces higher taxes, or distrusts the reform. Support should not be an unexplained penalty for choosing a particular ideology.

Implementation capacity has competing uses. A large ownership reform, a new benefit program, and a major enforcement expansion can strain the same legal, technical, and managerial resources. Hiring and training can improve future capacity, but should also take time and money.

The [regulation chapter]({{ '/regulation/' | relative_url }}) separates rulemaking from enforcement, and describes actor responses and review. Political structure and economic ownership must not be collapsed into one axis: state direction of production is not itself a complete description of a nation's political institutions.

The player controls the executive. Lawmakers can amend or reject proposals, and courts can review measures within their actual powers. The [government chapter]({{ '/government/' | relative_url }}) explains those interactions and the proposed continuity of play across successive governments. These are distinct institutions, not interchangeable sources of an approval penalty.

## Information and incentives

This is central to the educational purpose. Greater planning responsibility raises questions about how needs, capacity, and quality are measured:

- How does the planning authority learn what people need?
- Do managers report capacity accurately?
- Does a quantity target neglect quality or variety?
- What happens when an enterprise repeatedly misses its objectives?
- How can citizens signal unmet demand?

Market arrangements pose their own questions:

- Can dominant firms block competition?
- Does profitable investment address essential needs?
- Who bears pollution costs?
- Can households obtain essentials without enough purchasing power?

Treat these as conditional mechanisms. Better governance, competition, information, and accountability can change outcomes. Neither public nor private ownership should receive an automatic success or failure modifier.

Planning can range from public investment coordination and nonbinding priorities to directed credit, administered prices, and binding production or allocation orders. The spec should explain which powers a selected policy actually changes.

The player can improve information through reporting, inspections, demand surveys, price signals, and local discretion. Each has costs and weaknesses. A manager rewarded only for meeting a target may conceal a problem; a buyer's willingness to pay also reflects purchasing power, not every dimension of social need.

The proposed model should make unmet demand observable through appropriate indicators: prices, inventories, waiting lists, unfilled orders, or rationing. Suppressing a price signal should not erase the underlying scarcity, and a profitable sale should not automatically establish universal access.

## Innovation, environment, and resilience

Research, education, infrastructure, and new enterprises offer delayed and uncertain benefits. Pollution, depleted resources, and climate exposure can create delayed costs.

The core design should include long-term capacity and external costs. Detailed technology trees, resource systems, and climate modeling can remain later expansions.

## Transitions between systems

Changing ownership or allocation should initiate a process:

| Reform | Decisions the player must confront |
| --- | --- |
| Nationalization | Compensation, financing, management, governance, and investment |
| Privatization | Buyers, sale terms, competition, regulation, and service access |
| Stronger production planning | Information, targets, monitoring, managerial incentives, and administrative capacity |
| Market liberalization | Entry conditions, price adjustment, household protection, and competition enforcement |

Gradual reform and rapid restructuring should produce different exposures to disruption and delay. Reversing direction may entail costs and dependencies, rather than instantly restoring a previous state.

## Example: a housing program

The player funds construction. Banks change lending. Builders seek workers, land, and materials. Imports may ease some constraints. The central bank reacts to broader economic conditions. Over several turns, the report distinguishes new homes, affordability, land-price changes, bottlenecks, and public costs.

This is an illustrative causal chain, not a forecast. Its value is that a single understandable decision connects several systems without requiring the player to operate every institution directly.
