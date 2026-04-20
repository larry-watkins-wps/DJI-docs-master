# DJI Cloud Docs Corpus

Curated, LLM-digestible documentation of the **DJI Cloud API wire contract and workflows** needed by two parallel device cohorts:

**Current generation** (Dock 3 cohort):
- **DJI Dock 3**
- **Matrice 4D** (M4D)
- **Matrice 4TD** (M4TD)
- **RC Plus 2 Enterprise** running DJI Pilot 2 (the RC paired with the M4D)

**Older generation** (Dock 2 cohort):
- **DJI Dock 2**
- **Matrice 3D** (M3D)
- **Matrice 3TD** (M3TD)
- **RC Pro Enterprise** running DJI Pilot 2 (the RC paired with the M3D / M3TD)

Dock 1, M30 / M30T, M300 / M350 RTK, and Mavic 3 Enterprise families are out of scope.

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
| `http/` | [`README.md`](http/README.md) — URI form, `X-Auth-Token`, response envelope, status-code behavior + Phase 3 catalog of 16 endpoints across wayline / media / map / storage / device |
| `mqtt/` | [`README.md`](mqtt/README.md) — topic taxonomy, 13-topic list, envelope, per-family payloads + Phase 4a–4g [`dock-to-cloud/`](mqtt/dock-to-cloud/README.md) catalog (197 methods) + Phase 4h [`pilot-to-cloud/`](mqtt/pilot-to-cloud/README.md) catalog (94 methods across RC Plus 2 Enterprise + RC Pro Enterprise) + Phase 4i property-family shells (`osd/`, `state/`, `property-set/` per path — thin pointers to Phase 6) |
| `websocket/` | [`README.md`](websocket/README.md) — session lifecycle, envelope, push-and-fetch pattern + Phase 5 per-message catalog: [`map-elements/`](websocket/map-elements/) (4 push messages) + [`situation-awareness/`](websocket/situation-awareness/) (4 push messages) |
| `device-properties/` | [`README.md`](device-properties/README.md) — master matrix + narrative + Phase 6a dock-gateway entries: [`dock2.md`](device-properties/dock2.md) (48 properties, 3 writable) + [`dock3.md`](device-properties/dock3.md) (49 properties, 3 writable) + Phase 6b aircraft entries: [`_aircraft-pilot-base.md`](device-properties/_aircraft-pilot-base.md) (shared pilot-path baseline, 42 properties) + [`m3d.md`](device-properties/m3d.md) (dock-path 42 + pilot-path baseline) + [`m3td.md`](device-properties/m3td.md) (thermal-variant annex) + [`m4d.md`](device-properties/m4d.md) (dock-path 42 + pilot-path baseline + 7 M4 extensions) + [`m4td.md`](device-properties/m4td.md) (thermal-variant annex) + Phase 6c RC entries: [`rc-plus-2.md`](device-properties/rc-plus-2.md) (11 properties, 0 writable) + [`rc-pro.md`](device-properties/rc-pro.md) (11 properties, 0 writable) |
| `wpml/` | *(pending Phase 7)* |
| `livestream-protocols/` | *(pending Phase 7)* |
| `hms-codes/` | *(pending Phase 8)* |
| `error-codes/` | *(pending Phase 8)* |
| `workflows/` | *(pending Phase 9)* |
| `device-annexes/` | *(pending Phase 10)* |

## Authoring rules (quick reference)

- **Real payloads only** — verbatim from DJI source, never fabricated. Cite provenance.
- **English corpus** — translate from CN only when EN is missing/inadequate; flag translated passages.
- **Transport catalog owns schemas** — workflows link; they don't duplicate schema bodies.
- **Flag ambiguity** — add to `OPEN-QUESTIONS.md`; don't guess.
- **Update this README** every time a new doc lands.
