---
name: Phase 4 sub-phasing + RESUME-NOTES handoff pattern
description: Phase 4 of the DJI docs corpus is too large for one session; it's split into 4a–4i sub-drops with per-sub-phase review gates, and cross-session continuity lives in master-docs/RESUME-NOTES.md
type: project
---

Phase 4 of the DJI Cloud docs corpus (MQTT topic catalog) spans ~240 methods across dock-to-cloud and pilot-to-cloud paths. It is too large for a single session drop, so it is being landed in feature-area sub-phases **4a–4i**, each with its own user-review gate.

**Why**: a single drop would exceed context comfortably and invite quality drift. Smaller sub-phases (5–40 methods each) preserve the doc template refined during 4a.

**How to apply**: when the user says "Continue at 4X" (e.g. "Continue at 4c"), the fresh Claude session should:

1. Read the standard session-start files (CLAUDE.md, README.md, PLAN.md, TODO.md, _memory/MEMORY.md, SOURCES.md).
2. Read `master-docs/RESUME-NOTES.md` — contains per-sub-phase kick-off context including sources, method inventory, doc template, and known gotchas from the prior session.
3. Read the dock-to-cloud (or pilot-to-cloud) path-level README to see sub-phase status.
4. Pick two exemplar method docs as template references before drafting new ones.
5. Stop at each sub-phase review gate — don't push through.

**Sub-phase landing pattern**: draft the method docs, update `mqtt/dock-to-cloud/README.md`, update `mqtt/README.md` + corpus `README.md`, append a new entry at the top of `RESUME-NOTES.md` with the next sub-phase's kick-off context, tick `TODO.md` checkboxes, commit.

**File naming convention**: method docs use the verbatim DJI `method` string with underscores (e.g. `flighttask_prepare.md`, not `flighttask-prepare.md`) for grep-ability. Every doc carries a Cohort line (Dock 2 + Dock 3 / Dock 3 only / v1.15 addition) so divergences are explicit.
