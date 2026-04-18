# DJI Cloud Docs Corpus

Curated, LLM-digestible documentation of the **DJI Cloud API wire contract and workflows** needed by:

- **DJI Dock 3**
- **Matrice 4D** (M4D)
- **Matrice 4TD** (M4TD)
- **RC paired with the M4D** (RC Plus Enterprise family)

For repo-level scope, directives, and session-start instructions, see [`/CLAUDE.md`](../CLAUDE.md).

## Orientation

| File | Purpose |
|---|---|
| [`PLAN.md`](PLAN.md) | Phased plan with review gates |
| [`TODO.md`](TODO.md) | Cross-session fine-grained checklist |
| [`SOURCES.md`](SOURCES.md) | Source directory authority ranking |
| [`OPEN-QUESTIONS.md`](OPEN-QUESTIONS.md) | Standing gaps tracker *(created when first gap arises)* |
| [`_memory/MEMORY.md`](_memory/MEMORY.md) | In-repo Claude memory index |

## Corpus table of contents

*Empty — Phase 1 not yet started. New docs are added to the table below as they land.*

| Area | Docs |
|---|---|
| `architecture/` | *(pending Phase 1)* |
| `http/` | *(pending Phase 2–3)* |
| `mqtt/` | *(pending Phase 2 + 4)* |
| `websocket/` | *(pending Phase 2 + 5)* |
| `device-properties/` | *(pending Phase 6)* |
| `wmpl/` | *(pending Phase 7)* |
| `hms-codes/` | *(pending Phase 8)* |
| `livestream-protocols/` | *(pending Phase 9)* |
| `error-codes/` | *(pending Phase 10)* |
| `workflows/` | *(pending Phase 11)* |
| `device-annexes/` | *(pending Phase 12)* |

## Authoring rules (quick reference)

- **Real payloads only** — verbatim from DJI source, never fabricated. Cite provenance.
- **English corpus** — translate from CN only when EN is missing/inadequate; flag translated passages.
- **Transport catalog owns schemas** — workflows link; they don't duplicate schema bodies.
- **Flag ambiguity** — add to `OPEN-QUESTIONS.md`; don't guess.
- **Update this README** every time a new doc lands.
