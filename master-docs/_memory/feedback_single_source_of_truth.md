---
name: Single source of truth — no content duplication across corpus docs
description: Every fact in the corpus lives in exactly one canonical location; other docs link. Driven by audit integrity — duplicated facts drift out of sync.
type: feedback
---

Any given fact in `master-docs/` — a device enum, a payload schema, a topic name, a file inventory, a workflow step — must live in **exactly one canonical location**. Other docs that reference that fact must link to the canonical location rather than restate it.

**Why**: User stated explicitly during Phase 1 review: *"We should have only a single source of truth, if we have the same information in multiple places, they will eventually get out of date. No shortcuts, we do not want to simplify or summarize, this is for audit purposes."* The corpus is audit-grade; duplicated content drifts and makes audits unreliable.

**How to apply**:
- Identify the canonical location for each fact a new doc references. If you would restate a schema / enum / topic list / file inventory, link to its canonical home instead.
- Transport catalogs own schemas; workflows link to them. `device-properties/` owns device enums. `SOURCES.md` §3 owns the source-file inventory. Architecture overview links forward; it does not restate.
- When a fact has no canonical home yet, pick a home, write it there, and have other docs link — do not duplicate-and-defer the cleanup.
- Do not "simplify" or "summarize" canonical content for other contexts. A summary is a second version that can diverge.
