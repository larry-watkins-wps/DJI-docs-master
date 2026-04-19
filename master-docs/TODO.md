# DJI Cloud Docs Corpus — TODO

Cross-session source of truth. Update checkboxes as work completes. Before ending any session, reconcile this file against actual work done.

**Current phase**: Phase 1 — Architecture overview (awaiting user review)

---

## Phase 0 — Setup

- [x] In-repo memory at `master-docs/_memory/`
- [x] `CLAUDE.md` at repo root
- [x] `master-docs/PLAN.md`
- [x] `master-docs/TODO.md` (this file)
- [x] `master-docs/SOURCES.md`
- [x] `master-docs/README.md` (corpus table of contents)
- [x] `.gitignore` (narrow — build outputs, IDE, OS, vendored tools)
- [x] `.gitattributes` (LF normalization)
- [x] `git init` on main
- [ ] **Review gate**: user confirms final plan + layout
- [ ] Initial commit (snapshot of source dirs + setup files)

## Phase 1 — Architecture overview

- [x] Draft `architecture/README.md` — transports, connection model, device relationships, auth model high-level
- [x] Cross-check with `Cloud-API-Doc/` overview pages and `DJI_Cloud/` v1.15 extract
- [x] Update corpus `README.md`
- [x] Record v1.11 vs v1.15 source-version mismatch (`OPEN-QUESTIONS.md` OQ-001) and revise `SOURCES.md` authority ranking
- [ ] **Review gate**

## Phase 2 — Transport protocol references

- [ ] `http/README.md` — base URL conventions, auth, error envelope, pagination, common headers
- [ ] `mqtt/README.md` — topic taxonomy, message envelope (method/tid/bid/timestamp/data), QoS, retain, request-reply conventions
- [ ] `websocket/README.md` — handshake, session lifecycle, push message envelope
- [ ] Update corpus `README.md`
- [ ] **Review gate**

## Phase 3 — HTTP endpoint catalog

- [ ] Enumerate all HTTP endpoints from `Cloud-API-Doc/docs/en/` and `DJI-Cloud-API-Demo/api/`
- [ ] Group by resource (device / workspace / wayline / media / livestream / map / user / auth)
- [ ] One `.md` per endpoint (method, path, request schema, response schema, errors, real example, provenance)
- [ ] Update corpus `README.md`
- [ ] **Review gate**

## Phase 4 — MQTT topic catalog

- [ ] Enumerate all topics from `DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt` + `Cloud-API-Doc/`
- [ ] Group by family (OSD / state / services / events / property-set / requests / DRC)
- [ ] One `.md` per topic
- [ ] Update corpus `README.md`
- [ ] **Review gate**

## Phase 5 — WebSocket message catalog

- [ ] Enumerate all push message types
- [ ] One `.md` per message
- [ ] Update corpus `README.md`
- [ ] **Review gate**

## Phase 6 — Device properties

- [ ] `device-properties/README.md` — master matrix (property × device support, including out-of-scope rows for enum completeness)
- [ ] `device-properties/dock2.md`
- [ ] `device-properties/dock3.md`
- [ ] `device-properties/m3d.md`
- [ ] `device-properties/m3td.md`
- [ ] `device-properties/m4d.md`
- [ ] `device-properties/m4td.md`
- [ ] `device-properties/rc-plus-2.md`
- [ ] `device-properties/rc-pro.md`
- [ ] Update corpus `README.md`
- [ ] **Review gate**

## Phase 7 — WPML

- [ ] `wpml/overview.md`
- [ ] `wpml/template-kml.md`
- [ ] `wpml/waylines.md`
- [ ] `wpml/common-elements.md`
- [ ] Update corpus `README.md`
- [ ] **Review gate**

## Phase 8 — HMS codes

- [ ] Inspect `DJI_Cloud/HMS.json` to determine natural category partition
- [ ] Propose categories to user
- [ ] Generate one `hms-codes/<category>.md` per category
- [ ] Update corpus `README.md`
- [ ] **Review gate**

## Phase 9 — Livestream protocols

- [ ] `livestream-protocols/rtmp.md`
- [ ] `livestream-protocols/gb28181.md`
- [ ] `livestream-protocols/webrtc.md`
- [ ] `livestream-protocols/agora.md`
- [ ] Update corpus `README.md`
- [ ] **Review gate**

## Phase 10 — Error codes

- [ ] Catalog error codes from `DJI-Cloud-API-Demo/` error definitions + `Cloud-API-Doc/`
- [ ] `error-codes/README.md` with grouped table
- [ ] Update corpus `README.md`
- [ ] **Review gate**

## Phase 11 — Workflows

Workflows are written once per choreography and call out dock-generation-specific variations inline (not a separate doc per dock generation, unless the divergence is large enough to warrant it).

- [ ] `workflows/dock-bootstrap-and-pairing.md` (Dock 2 + Dock 3 variants)
- [ ] `workflows/device-binding.md`
- [ ] `workflows/firmware-and-config-update.md`
- [ ] `workflows/wayline-upload-and-execution.md`
- [ ] `workflows/live-flight-controls-drc.md`
- [ ] `workflows/livestream-start-stop.md`
- [ ] `workflows/hms-event-reporting.md`
- [ ] `workflows/flysafe-custom-flight-area-sync.md`
- [ ] `workflows/airsense-events.md`
- [ ] `workflows/media-upload-from-dock.md`
- [ ] `workflows/remote-control-handoff.md` (RC Plus 2 Enterprise and RC Pro Enterprise)
- [ ] Update corpus `README.md`
- [ ] **Review gate**

## Phase 12 — Device annexes

- [ ] `device-annexes/dock2.md`
- [ ] `device-annexes/dock3.md`
- [ ] `device-annexes/m3d.md`
- [ ] `device-annexes/m3td.md`
- [ ] `device-annexes/m4d.md`
- [ ] `device-annexes/m4td.md`
- [ ] `device-annexes/rc-plus-2.md`
- [ ] `device-annexes/rc-pro.md`
- [ ] Update corpus `README.md`
- [ ] **Review gate**

## Phase 13 — Final review

- [ ] Cross-link validation (every link resolves)
- [ ] `README.md` up to date with every doc
- [ ] `OPEN-QUESTIONS.md` — each entry either resolved or explicitly deferred
- [ ] Spot-check provenance citations
- [ ] **Final review gate with user**

---

## Standing items (ongoing, every phase)

- [ ] Update `master-docs/README.md` whenever a new doc is created
- [ ] Append to `master-docs/OPEN-QUESTIONS.md` whenever ambiguity is found
- [ ] Commit at natural breakpoints — small, focused commits

## Session-end checklist

Before ending any session on this project:
1. Reconcile checkboxes in this file against actual work done.
2. Commit in-flight work with a clear phase-referencing message.
3. Update `master-docs/RESUME-NOTES.md` if mid-phase context must survive a break.
