---
title: Saves, offline operation and delivery
intro: Preserve campaigns through interruption, updates and releases without coupling storage to economic rules.
permalink: /delivery/
---

**On this page**

* Contents
{:toc}

## Platform decisions

Phones only, **phone-browser delivery via a web link**, and a normal modular TypeScript project are accepted (D1/D2 in [requirements]({{ '/requirements/' | relative_url }})). A single physical output file is no longer required. Native app-store packaging is outside the selected scope; PWA installation and offline play remain optional proposals. The recommended implementation baseline is a static modular web application for phones. No backend is currently required by an accepted feature.

An ordinary website can support phone play without installation. An installable PWA requires appropriate application metadata and browser support; requirements and installation experiences vary. Offline behavior must be implemented and tested separately. See [MDN's installation guide](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable). A manifest or an install icon is not proof that a campaign works offline.

Native apps are outside the selected scope. If the user later changes that scope, assess [Capacitor](https://capacitorjs.com/docs) as a web-first container against the actual native requirements. Define platform build tooling, signing, store accounts, privacy declarations, save behavior and device tests before scheduling store delivery. Those obligations are not included silently in “mobile.”

## Proposed save contract

Use an asynchronous repository interface, with IndexedDB as the recommended browser adapter. [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) provides structured browser storage with transactions; the game still needs its own schema, validation and recovery logic.

| Save field | Purpose |
| --- | --- |
| Save schema version | Decode and migrate representation |
| App build, model rules and content versions | Determine compatibility and reproducibility |
| Campaign ID, revision, command IDs | Identify the campaign and prevent duplicate or stale writes |
| Snapshot and phase/cursor | Resume the committed state, including a pending encounter |
| Random algorithm/state and stream IDs | Continue deterministic behavior |
| Journal references and scenario identity | Explain effects and verify matching content |
| Created/saved time and integrity metadata | Aid recovery and user identification; timestamps do not drive the economy |

Store plain validated data, not live class instances. Rehydrate through constructors/factories that enforce invariants. Keep a previous valid checkpoint when practical and record autosave success only after the transaction completes. A proposed initial retention policy is the current and previous committed checkpoint per campaign, plus explicitly named saves; finalize quotas after measuring real save sizes.

Saving a revision includes a comparison against the persisted revision inside the same transaction. If another tab advanced the campaign, stop and offer reload or a separately named branch. Do not overwrite it. Quota failures, denied storage, unavailable databases, corrupt data and interrupted migrations have explicit user-visible outcomes.

## Recovery and portability

Browser storage can be evicted and users can clear it. A persistent-storage request may improve retention but is not a backup. [MDN documents browser quotas and eviction](https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria). Therefore recommend validated save export/import and a clear explanation that local saves do not synchronize across devices.

Import into a temporary candidate: enforce file-size limits before parsing, validate schema and references, reject unsupported versions and non-finite values, check accounting and required content, then show campaign identity before replacing or creating a save. The actual size limit is selected after measuring supported campaigns. Never evaluate imported code, load arbitrary remote scripts, or render untrusted strings as HTML.

On failure retain the current campaign and original imported file. Migrate a copy through explicit sequential schema steps, verify it, and commit only on success. Schema compatibility, model compatibility and content compatibility are separate. A schema upgrade does not guarantee replay under changed economic rules. Offer a compatible archived build or a clear incompatibility explanation when deterministic continuation cannot be supported.

## Offline assets and update lifecycle

This section applies only if offline/PWA scope is accepted. Service workers can intercept fetches and cache resources; they require a secure context in normal deployment and have an update lifecycle. See [MDN's service-worker guide](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers). Service workers are not the economic simulation engine.

Cache a complete versioned application shell and selected scenario resources. Keep cache names scoped to this game and base path. Treat external citations as optional online navigation. Display offline readiness only when the required content has been stored successfully. Do not promise a first-ever offline load.

An updated worker should wait for a safe checkpoint and player-controlled reload. Avoid forcing activation that mixes new UI code with an old model or overwrites an active decision. Keep save data outside disposable asset caches. Cleanup must remove only this application's obsolete assets; it must not delete another app's caches or a save database.

Test old and new tabs, pending turns, interrupted downloads, cache eviction, offline reload and rollback. Version the content and rules referenced by saves; decide whether to ship compatibility or require export before removing an older model. A deployment rollback must not make a migrated save unreadable without warning.

## Security and privacy baseline

Treat imported saves, authored text and URLs as untrusted inputs. Render text safely; validate allowed URL schemes and IDs. Avoid executable expressions in content packs. Keep credentials out of client bundles and documentation. A checksum detects accidental corruption; it is not an authenticity guarantee.

Recommend no accounts, analytics, advertising identifiers or telemetry in the first slice. If any is added, define its purpose, collection, consent and retention before implementation. Feedback should let players review diagnostics before sharing; do not upload saves silently. Secrets cannot be protected by embedding them in JavaScript shipped to the browser.

Maintain dependency and asset license records, pin installed versions, review upgrades, and keep development tools out of runtime assets. Determine the repository/game license explicitly before broad distribution; the current documentation task does not choose a license on the user's behalf.

## Build and release contract

Proposed commands after scaffolding: `npm ci`, `npm run typecheck`, `npm run lint`, `npm run test`, `npm run build`, and `npm run test:e2e`. These scripts do not exist yet. The scaffold task must define them and pin a compatible runtime and lockfile. Do not report them as tests run in this documentation session.

Produce immutable versioned release artifacts with a build identifier, rules/content/schema versions, change notes, browser/device evidence and compatibility statement. Deploy from a reproducible build. Verify actual hosted base paths, asset URLs, storage origin and routing rather than only a development server.

The current site is Jekyll documentation published from `main:/docs`. [GitHub Pages serves static sites](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages); this supports a browser-only build, but does not choose the game's final hosting. Preserve the documentation site. Decide a separate game path, repository or deployment artifact before adding a game pipeline, including service-worker scope and save-origin consequences.

Release steps: run required checks, build, preview at the intended base path, verify save compatibility, deploy the authorized artifact, wait for the deployment, check the live build/version and representative flows, and record rollback instructions. Do not publish an untested new model merely because documentation deployment succeeded.
