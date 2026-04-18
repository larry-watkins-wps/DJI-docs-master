---
name: Working style — methodical, phased, resumable
description: User expects methodical phased execution with a persistent cross-session TODO, avoiding context/quota exhaustion in any single session
type: feedback
---

Work must be **methodical and phased**. The project is long enough that no single session should attempt to complete it — we will exhaust context window or tool-use quota.

**Why**: The user has explicitly called out context/quota exhaustion as a real risk and wants resumability across sessions as a first-class property of how we work.

**How to apply**:
- Maintain `master-docs/PLAN.md` (the phased plan) and `master-docs/TODO.md` (the fine-grained checklist) as the durable source of truth for where we are and what's next. Update `TODO.md` as work completes — do not rely on session `TodoWrite` alone.
- At the start of every new session on this project, read `master-docs/PLAN.md` and `master-docs/TODO.md` before doing anything else.
- Break each phase into small independently-committable units. Prefer shipping a small, finished unit over a large, half-done one.
- When approaching a natural break, commit work, update `TODO.md`, and stop — do not push through into a new phase.
- Ask clarifying questions during the work rather than guessing. User prefers pauses for alignment over unilateral decisions.
