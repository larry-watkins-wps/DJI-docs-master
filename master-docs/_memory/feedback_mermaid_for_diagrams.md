---
name: Mermaid for all diagrams, chosen for plaintext audit-ability
description: Every corpus diagram uses Mermaid — sequence, flowchart, state — because plaintext lets diagrams be grep-ed, parsed, and validated programmatically
type: feedback
---

Every diagram in `master-docs/` uses **Mermaid** inside fenced ` ```mermaid ` blocks. No PNGs, no ASCII-art boxes, no other diagramming formats.

**Why**: User chose Mermaid during Phase 1 review (*"Mermaid is perfect, lets use that for all workflow and sequence diagrams"*) and explicitly asked about audit-ability. Mermaid source lives inline in markdown, parses cleanly with `@mermaid-js/mermaid-cli`, is regex-searchable for cross-checks (e.g., "every sequence-diagram message label must match a topic in the MQTT catalog"), and renders in every major markdown viewer.

**How to apply**:
- Sequence diagrams (workflows, auth handshakes, binding flows) → `sequenceDiagram`.
- Topology diagrams (device-edge-cloud, gateway wiring) → `flowchart`.
- State diagrams (device online / offline, mission lifecycle) → `stateDiagram`.
- If a diagram type is not supported in Mermaid, ask the user before reaching for another format.
- Keep individual diagrams small enough that the plaintext source is readable on its own. Long Mermaid blocks should be broken into multiple smaller diagrams that each tell one story.
