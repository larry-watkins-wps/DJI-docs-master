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
| **9a** | Lifecycle | bootstrap-pairing, device-binding, firmware+config | **Landed 2026-04-19, review gate closed** |
| **9b** | Missions & operations | wayline upload+execution, live flight / DRC, livestream start/stop | **Landed 2026-04-19, review gate closed** |
| **9c** | Events, media & handoff | HMS event reporting, FlySafe + CFA sync, AirSense, media upload, RC handoff | **Landed 2026-04-19** |

## Catalog

### Sub-phase 9a — Lifecycle (landed)

| Doc | Scope |
|---|---|
| [`dock-bootstrap-and-pairing.md`](dock-bootstrap-and-pairing.md) | Cold-start sequence: MQTT connect → License verification (`config`) → organization binding (`airport_bind_status` / `airport_organization_get` / `airport_organization_bind`) → first topology push. Dock 2 + Dock 3. |
| [`device-binding.md`](device-binding.md) | Ongoing topology lifecycle: `update_topo` on pair/unpair, OSD telemetry at 0.5 Hz, `state` change events, cloud-initiated `property/set`, and Pilot 2 change-signal fan-out via WebSocket. All cohorts (dock-path + pilot-path). |
| [`firmware-and-config-update.md`](firmware-and-config-update.md) | Maintenance choreographies: firmware OTA (`ota_create` → `ota_progress` loop) and post-bootstrap `config` refresh. Dock 2 + Dock 3. |

### Sub-phase 9b — Missions & operations (landed)

| Doc | Scope |
|---|---|
| [`wayline-upload-and-execution.md`](wayline-upload-and-execution.md) | Pilot-HTTPS wayline file upload (Phase 3) + `flighttask_prepare` → `flighttask_execute` → `flighttask_progress` (Phase 4b) + immediate / timed / conditional task variants + breakpoint recovery + in-flight-wayline delivery (Dock 3) + RTH controls. |
| [`live-flight-controls-drc.md`](live-flight-controls-drc.md) | Authority-grab (`flight_authority_grab`, `payload_authority_grab`) + `drc_mode_enter` → stick / drone-control DRC stream + heartbeat + HSI/OSD/delay push. Dock DRC (Phase 4c + 4e-2) and pilot DRC (Phase 4h). DRC 2.0 commander_flight_height semantics. |
| [`livestream-start-stop.md`](livestream-start-stop.md) | `live_start_push` / `live_stop_push` per protocol (RTMP / GB28181 / WebRTC / Agora), mid-stream quality / lens / camera changes, pilot-side JSBridge coordination. Cohort × protocol matrix. Cross-references Phase 7 livestream-protocols docs. |

### Sub-phase 9c — Events, media & handoff (landed)

| Doc | Scope |
|---|---|
| [`hms-event-reporting.md`](hms-event-reporting.md) | `hms` event push (Phase 4f) — full-set snapshot semantics, up to 20 alarms per event, Copy Key splicing (`dock_tip_{code}` / `fpv_tip_{code}[_in_the_sky]`), placeholder substitution (`%alarmid` / `%component_index` / `%sensor_index` / `%battery_index` / `%dock_cover_index` / `%charging_rod_index`), lookup into Phase 8 [`hms-codes/`](../hms-codes/README.md). Dock 2 + Dock 3. |
| [`flysafe-custom-flight-area-sync.md`](flysafe-custom-flight-area-sync.md) | **FlySafe**: [`unlock_license_list`](../mqtt/dock-to-cloud/services/unlock_license_list.md) / [`_update`](../mqtt/dock-to-cloud/services/unlock_license_update.md) / [`_switch`](../mqtt/dock-to-cloud/services/unlock_license_switch.md) + 7 unlock types (authorization zone / circle / country / altitude / polygon / power / RID) + online vs offline update modes. **CFA**: [`flight_areas_update`](../mqtt/dock-to-cloud/services/flight_areas_update.md) (trigger) → [`flight_areas_get`](../mqtt/dock-to-cloud/requests/flight_areas_get.md) (manifest) → [`flight_areas_sync_progress`](../mqtt/dock-to-cloud/events/flight_areas_sync_progress.md) (five states, 13 failure reasons) → [`flight_areas_drone_location`](../mqtt/dock-to-cloud/events/flight_areas_drone_location.md) (continuous telemetry). Dock 2 + Dock 3. |
| [`airsense-events.md`](airsense-events.md) | [`airsense_warning`](../mqtt/dock-to-cloud/events/airsense_warning.md) ADS-B proximity warning — 5-level severity (≥3 triggers onboard avoidance), full-snapshot push, `data`-as-array shape, 14-digit timestamp source typo. M3D / M3TD / M4D / M4TD (AirSense-equipped). |
| [`media-upload-from-dock.md`](media-upload-from-dock.md) | Dual-diagram — **Dock path**: [`storage_config_get`](../mqtt/dock-to-cloud/requests/storage_config_get.md) (`module: 0`) → direct OSS/S3/MinIO PUT → [`file_upload_callback`](../mqtt/dock-to-cloud/events/file_upload_callback.md) + optional prioritization ([`upload_flighttask_media_prioritize`](../mqtt/dock-to-cloud/services/upload_flighttask_media_prioritize.md) / [`highest_priority_upload_flighttask_media`](../mqtt/dock-to-cloud/events/highest_priority_upload_flighttask_media.md)). **Pilot path**: JSBridge preload → [`tiny-fingerprint`](../http/media/tiny-fingerprint.md) → [`fast-upload`](../http/media/fast-upload.md) → [`sts-credential`](../http/storage/sts-credential.md) → [`upload-callback`](../http/media/upload-callback.md) → [`group-upload-callback`](../http/media/group-upload-callback.md). All cohorts. |
| [`remote-control-handoff.md`](remote-control-handoff.md) | Pilot-path consent-gated authority — [`cloud_control_auth_request`](../mqtt/pilot-to-cloud/services/cloud_control_auth_request.md) (pop-up) → [`cloud_control_auth_notify`](../mqtt/pilot-to-cloud/events/cloud_control_auth_notify.md) (`ok` / `failed` / `canceled`) → `cloud_control_auth` state push (v1.15 array form / v1.11 `is_cloud_control_auth` narrative) → session → [`cloud_control_release`](../mqtt/pilot-to-cloud/services/cloud_control_release.md) or pilot grab-back. RC Plus 2 + RC Pro. |

## Authoring rules

Inherited from the corpus directives (see [`../CLAUDE.md`](../../CLAUDE.md)) and [`PLAN.md`](../PLAN.md):

- **Choreography only.** Workflow docs describe sequence, correlation keys, and terminal states. Schema bodies live in Phase 4 (MQTT), Phase 3 (HTTP), or Phase 5 (WebSocket) — link, don't duplicate.
- **Real payloads only.** Any payload fragment shown inline is verbatim from DJI source; all schema bodies are linked to canonical catalogs.
- **Mermaid for all diagrams.** `sequenceDiagram`, `flowchart`, or `stateDiagram` — see [memory `feedback_mermaid_for_diagrams`](../_memory/feedback_mermaid_for_diagrams.md).
- **Cite provenance per doc.** Each workflow's `## Provenance` table lists the `Cloud-API-Doc/` feature-set page (authoritative workflow narrative, v1.11 only), v1.15 `DJI_Cloud/` wire-level sources, and the Phase 4 catalog entries it links to.
- **Variants inline, not per-cohort docs.** Dock 2 vs Dock 3, dock-path vs pilot-path, and enum widening are all called out in `## Variants` sections.

## Source-authority note

DJI never shipped v1.15-era workflow-prose equivalents of the `Cloud-API-Doc/` feature-set pages — v1.15 source is wire-level method catalogs only. Per [OQ-001 resolution](../OPEN-QUESTIONS.md#oq-001--source-version-mismatch-between-cloud-api-doc-v1113-and-dji_cloud-v115), v1.15 is the corpus's authoritative wire source, but the Phase 9 workflow narrative relies on the v1.11 feature-set pages because they are the only DJI-authored choreography documentation that exists. Each workflow doc cites both: Cloud-API-Doc for narrative, v1.15 DJI_Cloud for payload-level claims.
