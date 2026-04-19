# DJI Cloud Docs Corpus

Curated, LLM-digestible documentation of the **DJI Cloud API wire contract and workflows** needed by:

- **DJI Dock 3**
- **Matrice 4D** (M4D)
- **Matrice 4TD** (M4TD)
- **RC paired with the M4D** (specifically **RC Plus 2 Enterprise** running DJI Pilot 2)

For repo-level scope, directives, and session-start instructions, see [`/CLAUDE.md`](../CLAUDE.md).

## Orientation

| File | Purpose |
|---|---|
| [`PLAN.md`](PLAN.md) | Phased plan with review gates |
| [`TODO.md`](TODO.md) | Cross-session fine-grained checklist |
| [`SOURCES.md`](SOURCES.md) | Source directory authority ranking |
| [`OPEN-QUESTIONS.md`](OPEN-QUESTIONS.md) | Standing gaps tracker |
| [`_memory/MEMORY.md`](_memory/MEMORY.md) | In-repo Claude memory index |

## Corpus table of contents

New docs are added to the table below as they land.

| Area | Docs |
|---|---|
| `architecture/` | [`README.md`](architecture/README.md) — transports, device-edge-cloud model, thing model, topic taxonomy, in-scope topologies |
| `http/` | *(pending Phase 2–3)* |
| `mqtt/` | *(pending Phase 2 + 4)* |
| `websocket/` | *(pending Phase 2 + 5)* |
| `device-properties/` | *(pending Phase 6)* |
| `wpml/` | *(pending Phase 7)* |
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
