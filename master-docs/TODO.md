# DJI Cloud Docs Corpus — TODO

Cross-session source of truth. Update checkboxes as work completes. Before ending any session, reconcile this file against actual work done.

**Current phase**: Phase 3 — HTTP endpoint catalog (16 endpoint docs drafted 2026-04-18; review gate pending).

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

## Phase 1 — Architecture overview *(complete)*

- [x] Draft `architecture/README.md` — transports, connection model, device relationships, auth model high-level
- [x] Cross-check with `Cloud-API-Doc/` overview pages and `DJI_Cloud/` v1.15 extract
- [x] Update corpus `README.md`
- [x] Record v1.11 vs v1.15 source-version mismatch (`OPEN-QUESTIONS.md` OQ-001) and revise `SOURCES.md` authority ranking
- [x] **Review gate** closed 2026-04-18. Landing commits: `b732963` (architecture doc), `ff6d2bc` (session-principle memory), `ca8e259` (Dock 2 cohort scope expansion).

## Phase 2 — Transport protocol references *(current)*

**Design decisions locked this session** (see `PLAN.md` Phase 2 for rationale):
- Each transport gets a single shared-conventions doc — no path split at Phase 2 level. The dock-to-cloud and pilot-to-cloud MQTT paths were verified envelope-identical by direct file comparison; path-specific divergence is Phase 4 content, not Phase 2.
- WebSocket is Pilot-to-Cloud only.
- HTTP is not path-split in DJI's material.
- Path-split subtrees land in Phase 4 (`mqtt/dock-to-cloud/` and `mqtt/pilot-to-cloud/`).

Checklist:
- [x] `http/README.md` — URI form, `X-Auth-Token`, response envelope, pagination, status-code-to-Pilot behavior mapping. Cites `[Cloud-API-Doc/.../40.https.md]` canonical + `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-Waypoint-Obtain-Wayline-List.txt]` live v1.15 example.
- [x] `mqtt/README.md` — topic taxonomy, `{device_sn}` vs `{gateway_sn}`, 13-topic list (verified identical across dock/pilot paths), envelope, per-family payload examples, request-reply, status lifecycle. Flags QoS/retain gap as OQ-003 and the pilot OSD copy-paste as OQ-002.
- [x] `websocket/README.md` — Pilot-to-Cloud only; session lifecycle, envelope, 8 observed `biz_code` values in two families (map-elements, situation-awareness), push-and-fetch coordination pattern.
- [x] Update corpus `README.md` TOC.
- [x] Log OQ-003 (MQTT QoS / retain / clean-session not specified by DJI) in `OPEN-QUESTIONS.md`.
- [x] **Review gate** closed 2026-04-18. Landing commit `56455eb` (http/README.md + mqtt/README.md + websocket/README.md + OQ-003 + plan compression).

## Phase 3 — HTTP endpoint catalog

**Scope decision (2026-04-18):** Tier A only — the 18 Pilot-to-Cloud HTTPS endpoints documented by DJI in both v1.11 and v1.15 sources, collapsed to **16 unique endpoints**. The ~70 dock-to-cloud endpoints that appear only in the deprecated demo (`DJI-Cloud-API-Demo/`, v1.10) are deferred to Phase 9 workflow authoring where the demo is citable as wire-behavior evidence.

Checklist:
- [x] Enumerate HTTP endpoints from `Cloud-API-Doc/docs/en/` + `DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-*.txt` + `DJI-Cloud-API-Demo/api/` (via Explore agent).
- [x] Group by resource — `wayline/` (6), `media/` (4), `map/` (4), `storage/` (1 shared STS endpoint), `device/` (1 topology).
- [x] One `.md` per endpoint — method, path, parameters, request body, response body, examples, provenance. All 16 cite both v1.11 canonical + v1.15 corroboration.
- [x] Add catalog index to `http/README.md`.
- [x] Update corpus `README.md` TOC.
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

## Phase 7 — Auxiliary specs (WPML + livestream protocols)

WPML:
- [ ] `wpml/overview.md`
- [ ] `wpml/template-kml.md`
- [ ] `wpml/waylines.md`
- [ ] `wpml/common-elements.md`

Livestream protocols:
- [ ] `livestream-protocols/rtmp.md`
- [ ] `livestream-protocols/gb28181.md`
- [ ] `livestream-protocols/webrtc.md`
- [ ] `livestream-protocols/agora.md`

- [ ] Update corpus `README.md`
- [ ] **Review gate**

## Phase 8 — Codes (HMS + error codes)

HMS codes:
- [ ] Inspect `DJI_Cloud/HMS.json` to determine natural category partition
- [ ] Propose categories to user
- [ ] Generate one `hms-codes/<category>.md` per category

Error codes:
- [ ] Catalog error codes from `DJI-Cloud-API-Demo/` error definitions + `Cloud-API-Doc/`
- [ ] `error-codes/README.md` with grouped table

- [ ] Update corpus `README.md`
- [ ] **Review gate**

## Phase 9 — Workflows

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

## Phase 10 — Device annexes + final review

Device annexes:
- [ ] `device-annexes/dock2.md`
- [ ] `device-annexes/dock3.md`
- [ ] `device-annexes/m3d.md`
- [ ] `device-annexes/m3td.md`
- [ ] `device-annexes/m4d.md`
- [ ] `device-annexes/m4td.md`
- [ ] `device-annexes/rc-plus-2.md`
- [ ] `device-annexes/rc-pro.md`
- [ ] Update corpus `README.md`

Final review pass (closing gate for the corpus):
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
