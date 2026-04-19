# DJI Cloud Docs Corpus — Plan

**Status**: Setup complete. Ready for Phase 1 pending initial commit.
**Last updated**: 2026-04-18.

## Objective

Produce a clean, concise, LLM-digestible documentation corpus in `master-docs/` that captures the **DJI Cloud API wire contract and workflows** needed by two parallel device cohorts to function against a DJI-Cloud-compatible server:

- **Current gen**: DJI Dock 3, Matrice 4D, Matrice 4TD, RC Plus 2 Enterprise paired with M4D.
- **Older gen**: DJI Dock 2, Matrice 3D, Matrice 3TD, RC Pro Enterprise paired with M3D / M3TD.

Server-side implementation (databases, brokers, auth backends, business logic, framework code) is **not** in scope. Dock 1 and other DJI drone families (M30/M30T, M300/M350 RTK, Mavic 3 Enterprise) are also out of scope.

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
├── wpml/                   # wayline file format reference (DJI WPML)
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

### Phase 1 — Architecture overview *(complete)*
`architecture/README.md` landed in commit `b732963`; review-gate principles captured as memory in commit `ff6d2bc`; scope expanded to Dock 2 cohort in `ca8e259`.

### Phase 2 — Transport protocol references *(current)*
Three shared-conventions docs, one per transport:
- `http/README.md` — base URL conventions, `X-Auth-Token`, error envelope, pagination, common headers. Single doc — the HTTP surface is not path-split in DJI's material (the Pilot-HTTPS endpoints live in a dedicated section but share the same envelope conventions with other HTTP traffic).
- `mqtt/README.md` — topic taxonomy, message envelope (tid / bid / timestamp / gateway / data / method), `{device_sn}` vs `{gateway_sn}` parameterization, QoS, retain, request-reply pattern, status lifecycle. **Single doc** — the dock-to-cloud and pilot-to-cloud paths are envelope-identical at the transport level. Verified by direct file comparison of `DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt` (dock-to-cloud) and `DJI_CloudAPI-PilotToCloud-Topic-Definition.txt` (pilot-to-cloud) — same 13 topics, same shapes, same common-fields table, same example envelopes. Divergence between the two paths is at the method / event / property content level, which is Phase 4 territory.
- `websocket/README.md` — handshake, session lifecycle, push message envelope (biz_code / version / timestamp / data). Pilot-to-Cloud only; the Dock path does not use WebSocket.

No catalog entries in Phase 2 — just the protocol rules.

### Phase 3 — HTTP endpoint catalog
`http/<resource>/<endpoint>.md` — one doc per endpoint with method, path, request schema, response schema, error responses, real examples. Grouped by resource (device, workspace, wayline, media, livestream, map, user, auth). Pilot-HTTPS endpoints (17 captured in `DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-*.txt`) are part of this catalog — under their appropriate resource groups, not a separate Pilot subtree, since the HTTP conventions are shared.

### Phase 4 — MQTT topic catalog
Per-path subtrees because topic content diverges between paths even though envelopes are shared:
- `mqtt/dock-to-cloud/<family>/<topic-or-method>.md` — Dock 2 and Dock 3 services / events / requests / DRC content.
- `mqtt/pilot-to-cloud/<family>/<topic-or-method>.md` — RC Plus 2 Enterprise, RC Pro Enterprise, and sub-device aircraft content.

Each subtree is organized by topic family: `osd/`, `state/`, `services/`, `events/`, `property-set/`, `requests/`, `drc/`. Shared conventions (envelope, QoS, retain) live in `mqtt/README.md` (Phase 2) and are not restated in the subtrees.

### Phase 5 — WebSocket message catalog
`websocket/<family>/<message>.md` — push message catalog with payload schema and real examples.

### Phase 6 — Device properties
`device-properties/README.md` (master support matrix of properties × devices) plus per-device files for all in-scope devices: `dock2.md`, `dock3.md`, `m3d.md`, `m3td.md`, `m4d.md`, `m4td.md`, `rc-plus-2.md`, `rc-pro.md`. Properties drawn from the `DJI_Cloud/` v1.15 device-properties and aircraft-properties catalogs (see [`SOURCES.md`](SOURCES.md) §3 for the full file inventory); out-of-scope device rows (Dock 1, M30/M30T, M400, Mavic 3 Enterprise, plain RC) included in the support matrix only for enum completeness per user direction. Verified against `Cloud-API-Doc/` where v1.11 counterparts exist.

### Phase 7 — WPML (wayline file format)
`wpml/` — overview, template KML, waylines, common elements. "WPML" is DJI's wayline planning markup language (format as used in the `.wpml` file extension and the official docs URL path). Sourced from `DJI_Cloud/DJI_CloudAPI_WPML-*.txt` and `Cloud-API-Doc/`.

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
`device-annexes/` — per-device deltas, quirks, and anything that differs meaningfully across the in-scope devices (Dock 2, Dock 3, M3D, M3TD, M4D, M4TD, RC Plus 2 Enterprise, RC Pro Enterprise). Informed by `dji_cloud_dock3/` (non-authoritative, Dock-3-specific) and anything flagged during earlier phases.

### Phase 13 — Final review pass
Consistency sweep: all cross-links resolve, README is up to date, `OPEN-QUESTIONS.md` either resolved or explicitly deferred, provenance citations spot-checked.

## Standing items (throughout)

- Update `master-docs/README.md` whenever a new doc is created.
- Update `master-docs/TODO.md` before ending any session.
- Append to `master-docs/OPEN-QUESTIONS.md` whenever ambiguity is encountered.
- Append to `master-docs/RESUME-NOTES.md` only if mid-phase context must survive a session break.

## Deferred (not started without explicit user approval)

**Phase 2 (project-level, distinct from phase numbers above)** — an implementation spec for a DJI-Cloud-compatible server, OR an audit of an existing implementation. Decided after corpus completion.
