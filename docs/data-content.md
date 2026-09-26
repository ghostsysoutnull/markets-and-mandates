---
title: Data, scenarios and authored content
intro: Give every baseline and rule an origin, a date, a definition, and a version.
permalink: /data-content/
---

**On this page**

* Contents
{:toc}

## Status and ownership

This is the proposed content contract. Broad 2010 research across the United States, United Kingdom, Germany, Russia, China and Japan is accepted; see the [research hub]({{ '/nation-research/' | relative_url }}). These descriptive profiles are separate from a validated playable nation pack or calibrated parameter set, neither of which exists. The first playable nation and policy scope remain open. [Nations and history]({{ '/nations/' | relative_url }}) owns the conceptual profile requirements.

Keep human-readable evidence notes in documentation and future validated machine-readable content in a dedicated content directory. Do not extract economic data by scraping prose at runtime. Do not fetch changing live statistics during a campaign; a scenario needs a reproducible, dated baseline.

## Nation research method

For the accepted broad 2010 research, identify the actual executive, monetary regime, legislative route, budget fallback, court powers, regulator, trade commitments and succession rules. Separate formal legal authority from evidence of effective practice. A current institutional website is not sufficient evidence for a historical arrangement if the law changed.

For each required variable, record definition, units, currency, nominal/real basis, price year, population coverage, geography, period, source series/table, retrieval date, revision vintage and transformation. Prefer primary statistical agencies, central banks, budget documents and legislation. Comparable international datasets are useful when their definitions and coverage fit. Explain discrepancies instead of averaging incompatible figures.

Select the smallest dataset that can initialize the chosen model. A variable that does not affect a rule, displayed learning outcome, or validation check should not become a research dependency merely because it is available. Conversely, a missing debt maturity distribution cannot be replaced with an invented national stereotype.

Apply the accepted exclusion of carbon-emissions and climate-change challenges to every nation brief: do not collect emissions inventories or climate parameters for gameplay, or author related policies, mandates, events or scores. An electricity study should focus on affordability, reliability, ownership, investment, financing, fuel supply and delivery constraints. A source may combine those subjects with climate policy. Extract only evidence supporting included mechanisms, record relevant omissions, and do not present the resulting simplified model as a complete historical reconstruction. Do not reuse an estimate combining included and excluded policy effects as a standalone coefficient without a justified separation.

## Evidence records

| Field | Contract |
| --- | --- |
| `sourceId` | Stable ID used by facts, model notes and player explanations |
| `title`, `publisher`, `url` | Exact supporting document or table, not a search result |
| `observationPeriod`, `publishedAt`, `retrievedAt` | Distinguish when measured, released and checked |
| `locator`, `definition`, `unit` | Section/table/series and precise interpretation |
| `license`, `attribution` | Redistribution conditions; absence of a paywall is not permission |
| `status`, `limitations` | Verified claim, provisional interpretation, gap or superseded value |
| `transform` | Reproducible conversion/aggregation and input references |

Country statistics and economic research still require focused source work. Technical documentation researched for this package cannot establish historical nation values. Preserve small source excerpts only when needed and permitted; retain links and reproducible retrieval instructions rather than copying entire publications.

## Scenario pack contract

A future scenario manifest identifies `scenarioId`, `contentVersion`, required schema/rules versions, nation, starting date, currency/units, source register, initial-state reference, policy/actor/event catalogues, and limitations. It declares whether actors or encounters are historical, composite, or fictional.

Validate references, unique IDs, allowed value ranges, authority owners, accounting initialization, event dates and source coverage before starting a campaign. A referenced actor or source that does not exist is a content error. Required unknown values block pack certification; optional unknown values must be visibly unavailable rather than displayed as zero.

Parameter records are separate from historical facts: `parameterId`, rule ID, value/range, unit, evidence basis, status (empirical estimate/design choice/illustrative fixture), calibration notes, sensitivity range and version. A historical observation is not automatically a causal coefficient. Avoid fitting all parameters to a single nation's realized path and calling that validation.

## Policy and encounter authoring

| Content type | Minimum authored fields |
| --- | --- |
| Policy | ID/version, objective, eligible scope, authority route, funding options, present/future costs, physical/administrative needs, transition timing, rule references, beneficiaries, risks, cancellation terms |
| Actor | ID, kind, ownership, resources, objectives, information access, institutional constraints, decision-policy reference, fictional/historical label |
| Encounter | Trigger, participants, player-visible evidence, offer, permitted responses, deadlines, amendment effects, refusal/delay branch, explanation |
| External event | ID, period or trigger, fixed/exogenous/conditional classification, affected variables, rule effects, evidence or fictional label |
| Mandate | Objective, measures, time horizon, distribution criteria, wider consequences to report; no hidden universal score |
| Report entry | Structured effect references, plain-language explanation, uncertainty, affected groups, sources/assumptions |

Illustrative authoring example: a public construction proposal reserves money only after authorization, pays contractors by milestone, and adds usable housing only on completion. Required worker and input constraints refer to rules, not narrative promises. The record must name funding, ownership, allocation to households and maintenance obligations. Exact numbers and national authority remain unspecified until researched and designed.

An encounter may ask for a regional allocation, but its accepted response must update the actual allocation, resources and schedule. A text-only promise is a content defect. Each authored option needs a valid refusal or failure path. A compromise cannot introduce unbounded additional initiatives without costs.

## Historical events and fiction

Classify every event before authoring effects. An external shock may be shared across replays; a domestic failure caused by earlier choices should be conditional. A real historical administration change cannot simultaneously be guaranteed and freely preventable by the player. Scenario rules must state the treatment.

Fictional named organizations can make motives legible, but their balance sheets and actions are model constructs. Do not attribute fictional misconduct to a real organization. Real organization names require sourced, period-specific treatment and a clear separation between starting fact and counterfactual behavior.

## Content release and localization

Review content independently of engine code: validate schema, sources, authority, resource availability, explanation, alternatives, and ideological symmetry. Publish a content version and changelog. Changes to starting values or policy effects must not silently modify an ongoing campaign.

Keep user-facing strings separate from identifiers and logic. Use stable message keys and locale-aware formatting for money, rates, dates and quantities. English is the current documentation language; additional game languages and translation scope are open. Do not concatenate translated sentence fragments around economic values.

Record licenses for fonts, icons, audio, datasets and illustrations in an asset register before shipping them. Art and audio are optional for the first proposed slice; they must not block readable, accessible decisions. No asset generation or paid licensing is authorized by this document.

## Research completion checklist

A nation pack is ready only when every initial field needed by the slice is traceable, the authority map is checked for its date, transformations are reproducible, initial accounts reconcile, uncertainty is disclosed, and source licenses permit the proposed use. Have a second review pass compare player-facing claims with the evidence. Record unresolved gaps and which features they block; do not mark a profile researched because its template is filled with qualitative guesses.
