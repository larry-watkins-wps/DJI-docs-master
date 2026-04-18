# DJI Cloud Docs Corpus — Plan

**Status**: Setup complete. Ready for Phase 1 pending initial commit.
**Last updated**: 2026-04-18.

## Objective

Produce a clean, concise, LLM-digestible documentation corpus in `master-docs/` that captures the **DJI Cloud API wire contract and workflows** needed by the **DJI Dock 3**, **Matrice 4D**, **Matrice 4TD**, and the **RC paired with the M4D** to function against a DJI-Cloud-compatible server.

Server-side implementation (databases, brokers, auth backends, business logic, framework code) is **not** in scope.

See `/CLAUDE.md` at repo root for full scope + directives. See `SOURCES.md` for source authority.

## Corpus layout

```
master-docs/
├── README.md               # corpus table of contents (kept in sync with new docs)
├── PLAN.md                 # this file
├── TODO.md                 # cross-session checklist
├── SOURCES.md              # source authority & inventory
├── OPEN-QUESTIONS.md       # standing gaps tracker (created on first gap)
├── _memory/                # in-repo Claude memory
├── architecture/           # cross-transport overview
├── http/                   # HTTP protocol ref + per-endpoint catalog + payload schemas
├── mqtt/                   # MQTT protocol ref + per-topic catalog + payload schemas
├── websocket/              # WebSocket protocol ref + per-message catalog + payload schemas
├── device-properties/      # master matrix + per-device files (Dock 3 / M4D / M4TD / RC)
├── workflows/              # sequenced choreography; links to transport catalogs
├── device-annexes/         # per-device deltas & quirks
├── wmpl/                   # wayline file format reference
├── hms-codes/              # HMS event codes split by category
├── livestream-protocols/   # RTMP / GB28181 / WebRTC / Agora specifics
└── error-codes/            # general API error code reference (not HMS)
```

Directory names are topical (no numeric prefixes) so new topics can be added without renumbering.

## Core directives (from `CLAUDE.md` + memory)

- **Real payloads only.** All wire examples must be verbatim from DJI source — never fabricated or paraphrased. Cite provenance.
- **Ask, don't guess.** When sources are ambiguous or conflict, ask the user and log in `OPEN-QUESTIONS.md`.
- **English-only corpus.** Translate from CN only when EN is missing or inadequate, flagging translated passages.
- **Workflow format.** Numbered sequence with actor, direction, transport, topic/endpoint, intent, real payload (inline) or link to canonical definition in the transport catalog when schema is large.
- **Canonical schema lives in transport catalog only.** Workflows link to it; they don't duplicate schema bodies.

## Phases

Each phase ends at a **user review gate** before the next begins. Phases may be paused or sliced further for context/quota reasons; `TODO.md` is the fine-grained resumable state.

### Phase 0 — Setup *(complete)*
Memory, CLAUDE.md, PLAN, TODO, SOURCES, README, `.gitignore`, `.gitattributes`, `git init`. Initial commit snapshots the source material.

### Phase 1 — Architecture overview
`architecture/` — one short doc explaining the shape of DJI Cloud: which transports exist, what each is used for, how devices connect, how Dock/aircraft/RC relate, authentication model at a glance. Establishes shared vocabulary for later phases.

### Phase 2 — Transport protocol references
`http/README.md`, `mqtt/README.md`, `websocket/README.md` — per-transport conventions: base URLs/auth/error envelope/pagination (HTTP); topic taxonomy/message envelope/QoS/request-reply conventions (MQTT); handshake/session lifecycle/message envelope (WebSocket). No catalog entries yet, just the protocol rules.

### Phase 3 — HTTP endpoint catalog
`http/<resource>/<endpoint>.md` — one doc per endpoint with method, path, request schema, response schema, error responses, real examples. Grouped by resource (device, workspace, wayline, media, livestream, map, user, auth).

### Phase 4 — MQTT topic catalog
`mqtt/<family>/<topic>.md` — one doc per topic with payload schema, direction, real examples. Families: OSD / state / services / events / property-set / requests / DRC.

### Phase 5 — WebSocket message catalog
`websocket/<family>/<message>.md` — push message catalog with payload schema and real examples.

### Phase 6 — Device properties
`device-properties/README.md` (master support matrix of properties × devices) plus per-device files: `dock3.md`, `m4d.md`, `m4td.md`, `rc-m4d.md`. Properties drawn from `DJI_Cloud/DJI_CloudAPI-Dock3-DeviceProperties.txt`, `DJI_CloudAPI-Matrice4-DeviceProperties.txt`, `DJI_CloudAPI_Aircraft-Properties.txt`, `DJI_CloudAPI_RC-Plus-Enterprise-Properties.txt`, verified against `Cloud-API-Doc/`.

### Phase 7 — WMPL (wayline file format)
`wmpl/` — overview, template KML, waylines, common elements. Sourced from `DJI_Cloud/DJI_CloudAPI_WMPL-*.txt` and `Cloud-API-Doc/`.

### Phase 8 — HMS codes
`hms-codes/` — codes split by category (categories TBD after inspecting `HMS.json` structure). Curated markdown must stay consistent with `HMS.json`. Sanity-check script optional future polish.

### Phase 9 — Livestream protocols
`livestream-protocols/` — per-protocol specifics for RTMP, GB28181, WebRTC, Agora. Focused on what the Dock/aircraft sends over the wire and what the cloud must terminate or relay. Pure media-transport layer, separate from the HTTP/MQTT signaling that starts a stream (which lives in `workflows/`).

### Phase 10 — Error codes
`error-codes/` — general API error code reference distinct from HMS. Sourced from DJI demo error definitions and official docs.

### Phase 11 — Workflows
`workflows/<workflow>.md` — choreography docs. Each uses the format in the directives above. Expected workflows (subject to refinement during earlier phases):
- Dock 3 bootstrap & pairing
- Device binding (Dock + aircraft + RC to workspace)
- Firmware / config update (Dock, aircraft)
- Wayline upload & mission execution (Dock-scheduled)
- Live flight controls / DRC (dock-initiated and RC-initiated)
- Livestream start/stop (per media protocol)
- HMS event reporting & acknowledgement
- FlySafe / Custom Flight Area synchronization
- AirSense events
- Media upload from Dock
- Remote control handoff (RC ↔ cloud)

This phase depends on Phases 3–5 being complete so workflow steps can link to canonical transport catalog entries.

### Phase 12 — Device annexes
`device-annexes/` — per-device deltas, quirks, and anything that differs meaningfully between Dock 3 / M4D / M4TD / paired RC. Informed by `dji_cloud_dock3/` (non-authoritative) and anything flagged during earlier phases.

### Phase 13 — Final review pass
Consistency sweep: all cross-links resolve, README is up to date, `OPEN-QUESTIONS.md` either resolved or explicitly deferred, provenance citations spot-checked.

## Standing items (throughout)

- Update `master-docs/README.md` whenever a new doc is created.
- Update `master-docs/TODO.md` before ending any session.
- Append to `master-docs/OPEN-QUESTIONS.md` whenever ambiguity is encountered.
- Append to `master-docs/RESUME-NOTES.md` only if mid-phase context must survive a session break.

## Deferred (not started without explicit user approval)

**Phase 2 (project-level, distinct from phase numbers above)** — an implementation spec for a DJI-Cloud-compatible server, OR an audit of an existing implementation. Decided after corpus completion.
