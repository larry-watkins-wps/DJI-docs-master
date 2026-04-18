---
name: Documentation style preferences
description: How the user wants the DJI Cloud documentation corpus written and structured
type: feedback
---

Documentation in `master-docs/` must be **clean, clear, and concise**. LLM-digestibility is the primary consumption criterion — the audience is future Claude Code sessions and other LLMs, not humans browsing a polished docs site.

**Why**: The corpus is intended as a trustworthy knowledge base for future automated work (either building a replacement cloud stack or auditing existing systems). Noise, ambiguity, or unverified assertions degrade that purpose.

**How to apply**:
- Prefer Markdown with a stable hierarchical directory structure so files can be loaded by path.
- Write facts plainly. Avoid marketing language, redundancy, and filler.
- When multiple sources disagree or material is ambiguous, **ask the user** rather than guess. This is an explicit standing instruction.
- Cite which source dir each curated claim came from when the provenance is non-obvious.
- Flag gaps explicitly (e.g., a dedicated "open questions" or "unknown" section) rather than papering over them.
