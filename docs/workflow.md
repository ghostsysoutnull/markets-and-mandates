---
title: Development across sessions
intro: Small verifiable work packets, a durable checkpoint, and focused reading keep progress efficient.
permalink: /workflow/
---

**On this page**

* Contents
{:toc}

## Working agreement

This is a project process, independent of a particular coding tool. The current user's instructions override stale notes. The interactive walkthrough is aborted and must not be resumed as a prerequisite. Current work prepares development documentation; implementation starts with a concrete authorized packet, not merely because code appears in the backlog.

Use one active packet at a time by default. Parallel agents are not assumed or required; delegate only when the user or applicable instructions authorize it and responsibilities can be separated. Avoid creating tasks whose only output is another generic plan.

## Source of truth

| Record | Owns | Keep out |
| --- | --- | --- |
| `AGENTS.md` | Stable collaboration rules and startup instructions | Long design explanations and rapidly changing status |
| `HANDOVER.md` | Current task, checkpoint, blockers, exact next action, checks and working-tree state | A duplicate of every chapter |
| Backlog | Ordered packets, dependencies, state and completion criteria | Unselected ideas masquerading as approved work |
| Requirements and decision log | Product intent, acceptance and accepted choices | Tool output and temporary debugging notes |
| Architecture/ADRs | Technical boundaries and consequential tradeoffs | Nation facts without evidence |
| Model/content docs | Rules, units, parameters, sources and limitations | Unreviewed numbers hidden as implementation constants |
| Git history | Reviewable changes and rationale | Secrets, generated dependency folders or unexplained bulk formatting |

## Session startup

1. Read `AGENTS.md`, `HANDOVER.md` and the backlog. Check the current request for changes in direction.
2. Inspect `git status --short`, current branch and relevant recent commits. Identify user edits and preserve them.
3. Select the authorized packet and read only its linked requirements, rules, decisions and files. Do not reread the full site by default.
4. State the concrete intended result and any unsettled dependency. Ask only for information that blocks a material decision, in plain language; continue independent work while awaiting it.
5. Check actual tools and permissions before relying on them. Do not assume a previous session's server, authentication, build or installed dependency still exists.

## Work packet template

Use this compact record in the backlog or a linked task file; do not create an empty directory of templates.

```text
ID / title / status:
Objective: one observable result
Requirements and decisions:
Dependencies: IDs and whether satisfied
Read: owning chapters and relevant source/code paths
Change: intended files or module boundary
Out of scope: only meaningful adjacent work
Acceptance: observable success plus important failure behavior
Validation: exact commands/manual evidence once available
Checkpoint: completed work, current state and next action
Completion evidence: commit/artifact/checks and remaining limitations
```

A packet should be resumable from a checkpoint and end with something reviewable: a sourced authority map, reconciled fixture, working save adapter, accessible policy form, or passing feature slice. Avoid arbitrary hours or token estimates without evidence. Split when a packet contains unrelated outcomes or cannot be validated independently.

## Research loop

Name the question and the feature it blocks. Search official technical documentation, primary institutional sources, datasets or original research as appropriate. Record exact claim, source/date, interpretation and limitation in the owning research record. Stop once the next decision has adequate evidence; collect further sources only for unresolved claims or contradictions.

Do not repeat a previous search merely because a new session started. Recheck when information is volatile, a version changes, a historical reference is mismatched, or the recorded source no longer supports the claim. Product preferences are answered by the user, not by more browsing.

## Implementation loop when authorized

Resolve the packet's dependencies, implement the smallest complete behavior, run relevant checks, and review the diff. Keep economic rules separate from UI and storage. Add meaningful tests for changed behavior and failure modes, not assertions that mirror private implementation.

Do not broaden into another nation, framework migration, visual overhaul or generalized engine while completing a narrow feature. Record useful future work in the backlog. Do not substitute a scaffold for the accepted feature outcome.

If new evidence invalidates the plan, state the conflict, update the decision/rule and affected checks, then continue. If a user answer is necessary, finish independent work and preserve the exact dependency. Silence is not a product decision.

## Checkpoints and handoff

Before a session ends or context becomes tight, update the checkpoint with active packet, decisions made, files changed, checks actually run, failures, uncommitted work, running processes and next executable action. Keep it concise; link to detailed contracts. Never report an unrun command as passed.

Preferred handoff format: result; verification; remaining dependency; two concrete next actions with one preferred. Do not reopen choices already accepted. If the user has already authorized a full task, continue to its completion rather than offering a halfway stop.

Use task states `ready`, `in progress`, `blocked on <specific dependency>`, `done`, `deferred`, or `aborted`. “Done” requires acceptance evidence. An aborted walkthrough remains aborted, not completed or queued under a new name.

## Version control and publication

Use reviewable commits with a concrete purpose. Preserve unrelated changes; stage specific paths when sharing a worktree. Never reset user work to obtain a clean branch. A branch or isolated checkout is useful for concurrent changes when needed, not mandatory ceremony for a prose edit.

When documentation publication is in scope, update affected chapters/navigation and state records consistently, run diff/link checks, commit and push the authorized changes, watch the actual Pages deployment, then verify live content and links. Record the new build, not a historical successful run. Game release follows the separate [delivery contract]({{ '/delivery/' | relative_url }}).

## Copyable continuation brief

> Continue Markets & Mandates. Read AGENTS.md, HANDOVER.md and docs/backlog.md, then only the chapters linked by the active packet. The paper walkthrough was aborted. The current direction is researched development documentation for mobile/web with TypeScript and OO. Preserve accepted decisions; distinguish recommendations from requirements. Complete the authorized packet and its checks, update the checkpoint, and give concise next-step options. Do not fabricate nation data, calibrated outcomes, user approvals, or test results.
