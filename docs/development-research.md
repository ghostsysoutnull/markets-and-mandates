---
title: Development research and evidence
intro: Verified platform capabilities, reasoned recommendations, and the work that evidence has not yet settled.
permalink: /development-research/
---

**On this page**

* Contents
{:toc}

## Research scope and method

Research checked on **25 September 2026** against official platform/tool documentation, W3C material, original simulation research and primary economic sources. This supports the development documentation package. It does not constitute a nation baseline, package compatibility test, performance benchmark or economic calibration.

Technical recommendations below are our design judgments based on the game's needs. A source establishes a capability or constraint, not that a tool is necessarily the best choice. Exact runtime/package versions must be selected together and checked at scaffolding time. The user has now specified phones only and a normal modular TypeScript project; the user subsequently selected phone-browser delivery through a web link. Native-store delivery is outside the selected scope.

## Evidence register

| ID | Source checked | Supported finding | Project implication and limit |
| --- | --- | --- | --- |
| E01 | [TypeScript classes](https://www.typescriptlang.org/docs/handbook/2/classes.html) | Classes and typed object relationships are supported | Use OO for domain responsibility; composition and layering are our design choices |
| E02 | [TypeScript strict mode](https://www.typescriptlang.org/tsconfig/strict) | Strict enables a group of stronger checks; compiler upgrades can introduce new errors | Pin and validate compiler upgrades; this does not validate economic logic |
| E03 | [Type assertions](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions) | Assertions are removed and do not perform runtime checking | Validate saves and content before treating them as domain objects |
| E04 | [Vite TypeScript support](https://vite.dev/guide/features#typescript) | Transpilation and type checking are separate | Add an explicit type-check command; no scaffold or compatibility test has run |
| E05 | [Vitest features](https://vitest.dev/guide/features) | Offers test facilities integrated with Vite configuration | Candidate domain/contract test runner; choice remains proposed |
| E06 | [Playwright emulation](https://playwright.dev/docs/emulation) | Emulates viewport, user agent, touch and other conditions | Useful reproducible phone-shaped browser tests; not real-phone evidence |
| E07 | [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) | Asynchronous structured browser storage with transactions | Candidate save adapter; application recovery semantics remain our responsibility |
| E08 | [Storage quotas and eviction](https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria) | Quota and retention behavior depend on the browser; stored data can be removed | Provide recovery/export; never promise permanent local storage |
| E09 | [PWA installation](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable) | Installation involves application metadata and platform-specific support | Browser play, installation and offline availability are distinct requirements |
| E10 | [Service workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers) | Service workers have installation/activation and fetch handling | Version asset caches and plan updates; don't confuse a worker with reliable saves |
| E11 | [Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers) | Background workers communicate by messages without direct DOM manipulation | Optional performance boundary after profiling; not required merely because this is a simulation |
| E12 | [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Defines accessibility success criteria | Proposed AA target requires automated and human checks, not a claim of existing conformance |
| E13 | [Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) | Explains narrow/zoomed content requirements and two-dimensional exceptions | Test the decision flow at 320 CSS pixels; preserve access to detailed tables |
| E14 | [Target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) | AA criterion uses 24 CSS pixels with specified exceptions | Proposed 44-pixel primary controls are a project usability target, not an AA rule |
| E15 | [Capacitor](https://capacitorjs.com/docs) | A native runtime can host web-first applications | Candidate only if phone app-store delivery is wanted; native QA/release work still exists |
| E16 | [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) | Hosts static HTML, CSS and JavaScript from a repository/build | Existing documentation hosting can continue; final game deployment is a distinct choice |
| E17 | [ODD protocol, Grimm et al. 2020](https://www.jasss.org/23/2/7.html) | Describes model documentation, rationale and evaluation for reproducibility | Organize entities, scheduling, initialization and rules explicitly; not a ready-made economics model |
| E18 | [UN national accounts](https://unstats.un.org/unsd/nationalaccount/sna.asp) | Provides coherent concepts and accounting rules for flows and stocks | Reconcile a declared model boundary; preserve each dataset's historical standard/vintage |
| E19 | [Bank of England: money creation, 2014](https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy) | Explains commercial-bank money creation and constraints | Separate loan/deposit creation, transfers and public expenditure; no game coefficients supplied |

The existing [sources chapter]({{ '/sources/' | relative_url }}) supports conceptual discussions of institutions, monetary transmission, regulation and trade. These sources do not cover every claim needed for a selected historical nation.

## Decisions informed by this research

Recommend a browser-independent TypeScript domain, serializable state, explicit persistence boundaries, semantic interface and deterministic model inputs. These follow from the need to test economics separately from phone interaction and to resume interrupted play. Research supports the relevant capabilities; the architectural combination is a proposal.

Recommend a modest build/test toolchain rather than a specialized game engine for the first policy-and-report interface. This is an inference from the intended interaction, not a measured comparison of engines. Reassess if the selected slice requires continuous spatial simulation, rich animation or other rendering needs not present in the current concept.

Do not equate package maturity with an evidence-based model. Behavioral coefficients, institutional facts, update order and explanatory validity need separate investigation. Likewise, published WCAG requirements cannot prove this future interface is accessible before implementation and testing.

## Open research work

| Question | Evidence needed | Dependency / completion |
| --- | --- | --- |
| Supported phone browsers | Delivery choice D1 is resolved as a phone-browser web link; verify exact supported versions and any optional installation/offline behavior | Phone device matrix and release obligations documented |
| Compatible toolchain | Actual chosen TypeScript/build/test versions, runtime requirements and lockfile experiment | Scaffold packet; commands pass in local and CI environments |
| Historical nation | Dated primary institutions, budget/sector/household/financial data and transformations | D3; certified initial pack per data contract |
| Economic closure | Explicit price, production, finance and resource-allocation rules for the selected slice | D4; reconciled fixtures and uncertainty register |
| Model sensitivity | Justified parameter ranges, alternative policy runs and failure cases | Model packet; recorded results and limitations |
| Phone usability/performance | Actual screens, device/OS/browser versions, task observations and timings | UI slice; measurements rather than assumed capability |
| Save/update reliability | Supported-browser quota, lifecycle, migration and failure tests | Persistence packet; recoverable checkpoint demonstrated |
| Licensing | Chosen game/code license and redistribution conditions for every shipped asset/data source | Release dependency; reviewed license register |

Research should continue in these bounded packets, not as an undirected survey of all economics or all JavaScript frameworks. Record negative or conflicting evidence. Keep dated observations, model assumptions and user preferences separate throughout.
