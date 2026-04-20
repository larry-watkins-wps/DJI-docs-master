# Workflows

Phase 9 choreography docs. Each describes the wire sequence a cohort runs to accomplish a specific outcome — pairing, mission execution, livestream start, etc. — and links to the Phase 2–8 catalogs for wire-level schemas.

Workflow docs own **choreography only**: who speaks when, in what order, over which topic / endpoint, with which correlation key, and what a terminal state looks like. They never restate schemas — every payload body is in a Phase 4/3/5 catalog entry.

---

## Scope

- In-scope cohorts: **Dock 2**, **Dock 3**, **M3D / M3TD** (under Dock 2 or RC Pro), **M4D / M4TD** (under Dock 3 or RC Plus 2), **RC Pro Enterprise**, **RC Plus 2 Enterprise**.
- Workflows are written once per choreography and call out dock-generation-specific variations inline. A separate doc per dock generation is only used when divergence is large enough (none so far).

## Sub-phase roadmap

Phase 9 is sub-phased to keep each drop reviewable in isolation. Every sub-phase ends at a review gate.

| Sub-phase | Theme | Docs | Status |
|---|---|---|---|
| **9a** | Lifecycle | bootstrap-pairing, device-binding, firmware+config | **Landed 2026-04-19** |
| 9b | Missions & operations | wayline upload+execution, live flight / DRC, livestream start/stop | pending |
| 9c | Events, media & handoff | HMS event reporting, FlySafe + CFA sync, AirSense, media upload, RC handoff | pending |

## Catalog

### Sub-phase 9a — Lifecycle (landed)

| Doc | Scope |
|---|---|
| [`dock-bootstrap-and-pairing.md`](dock-bootstrap-and-pairing.md) | Cold-start sequence: MQTT connect → License verification (`config`) → organization binding (`airport_bind_status` / `airport_organization_get` / `airport_organization_bind`) → first topology push. Dock 2 + Dock 3. |
| [`device-binding.md`](device-binding.md) | Ongoing topology lifecycle: `update_topo` on pair/unpair, OSD telemetry at 0.5 Hz, `state` change events, cloud-initiated `property/set`, and Pilot 2 change-signal fan-out via WebSocket. All cohorts (dock-path + pilot-path). |
| [`firmware-and-config-update.md`](firmware-and-config-update.md) | Maintenance choreographies: firmware OTA (`ota_create` → `ota_progress` loop) and post-bootstrap `config` refresh. Dock 2 + Dock 3. |

### Sub-phase 9b — Missions & operations (pending)

| Doc | Planned scope |
|---|---|
| `wayline-upload-and-execution.md` | Pilot-HTTPS wayline file upload (Phase 3) + `flighttask_prepare` → `flighttask_execute` → `flighttask_progress` (Phase 4b) + immediate / timed / conditional task variants + breakpoint recovery. |
| `live-flight-controls-drc.md` | Authority-grab (`flight_authority_grab`, `payload_authority_grab`) + `drc_mode_enter` → stick / drone-control DRC stream + heartbeat + delay push. Dock DRC (Phase 4c + 4e-2) and pilot DRC (Phase 4h). |
| `livestream-start-stop.md` | `live_start_push` / `live_stop_push` per protocol (RTMP / GB28181 / WebRTC / Agora), pilot-side JSBridge coordination. Cross-references Phase 7 livestream-protocols docs. |

### Sub-phase 9c — Events, media & handoff (pending)

| Doc | Planned scope |
|---|---|
| `hms-event-reporting.md` | `hms` event emission (Phase 4f) + code lookup via Phase 8 hms-codes/. |
| `flysafe-custom-flight-area-sync.md` | License switch / update / list (`unlock_license_*`) + CFA area download (`flight_areas_get` + `flight_areas_update`) + sync progress events. |
| `airsense-events.md` | `airsense_warning` event — ADS-B traffic alerting. |
| `media-upload-from-dock.md` | `file_upload_callback` + `storage_config_get` + Pilot-HTTPS media endpoints + STS credential handshake. |
| `remote-control-handoff.md` | RC Plus 2 + RC Pro `cloud_control_auth_request` / `cloud_control_auth_notify` / `cloud_control_release`. |

## Authoring rules

Inherited from the corpus directives (see [`../CLAUDE.md`](../../CLAUDE.md)) and [`PLAN.md`](../PLAN.md):

- **Choreography only.** Workflow docs describe sequence, correlation keys, and terminal states. Schema bodies live in Phase 4 (MQTT), Phase 3 (HTTP), or Phase 5 (WebSocket) — link, don't duplicate.
- **Real payloads only.** Any payload fragment shown inline is verbatim from DJI source; all schema bodies are linked to canonical catalogs.
- **Mermaid for all diagrams.** `sequenceDiagram`, `flowchart`, or `stateDiagram` — see [memory `feedback_mermaid_for_diagrams`](../_memory/feedback_mermaid_for_diagrams.md).
- **Cite provenance per doc.** Each workflow's `## Provenance` table lists the `Cloud-API-Doc/` feature-set page (authoritative workflow narrative, v1.11 only), v1.15 `DJI_Cloud/` wire-level sources, and the Phase 4 catalog entries it links to.
- **Variants inline, not per-cohort docs.** Dock 2 vs Dock 3, dock-path vs pilot-path, and enum widening are all called out in `## Variants` sections.

## Source-authority note

DJI never shipped v1.15-era workflow-prose equivalents of the `Cloud-API-Doc/` feature-set pages — v1.15 source is wire-level method catalogs only. Per [OQ-001 resolution](../OPEN-QUESTIONS.md#oq-001--source-version-mismatch-between-cloud-api-doc-v1113-and-dji_cloud-v115), v1.15 is the corpus's authoritative wire source, but the Phase 9 workflow narrative relies on the v1.11 feature-set pages because they are the only DJI-authored choreography documentation that exists. Each workflow doc cites both: Cloud-API-Doc for narrative, v1.15 DJI_Cloud for payload-level claims.
