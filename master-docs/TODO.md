# DJI Cloud Docs Corpus — TODO

Cross-session source of truth. Update checkboxes as work completes. Before ending any session, reconcile this file against actual work done.

**Current phase**: Phase 8 content-complete 2026-04-19. Review gate pending. Phase 9 (Workflows) is next.

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
- [x] **Review gate** closed (implicit — user directed Phase 1 start). Reconciled 2026-04-19.
- [x] Initial commit landed. Commit `f6a63eb` (chore: initialize repo with setup, plan, memory, and source snapshot). Reconciled 2026-04-19.

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
- [x] **Review gate** closed 2026-04-18. Landing commit `aa0c590` (16 endpoint docs + catalog index).

## Phase 4 — MQTT topic catalog

**Scope decision (2026-04-18):** Phase 4 is being landed in feature-area sub-drops because the full method count (~240 methods across dock-to-cloud + pilot-to-cloud) is too large for a single drop. Each sub-phase has its own review gate. Property families (`osd/`, `state/`, `property-set/`) will be thin shells that link to Phase 6 `device-properties/` — they do not duplicate the property catalog. Dock 2 vs Dock 3 (and RC Plus 2 vs RC Pro) are co-documented per method with a **Cohort** field; per-cohort quirks larger than a note go to Phase 10 annexes. File names are the verbatim DJI `method` string (e.g., `airport_organization_bind.md`) for grep-ability.

Also adds an 8th family directory, `status/`, for the `sys/product/{gateway_sn}/status` topic which doesn't fit the PLAN's seven thing-model families.

### Sub-phase 4a — DeviceManagement + Organization + Configuration (dock-to-cloud)

- [x] Enumerate methods across `DJI_CloudAPI-Dock3-DeviceManagement.txt`, `DJI_CloudAPI-Dock3-Organization-Management.txt`, `DJI_CloudAPI-Dock3-Configuration-Update.txt`, and their Dock 2 counterparts. 5 methods total.
- [x] Write `mqtt/dock-to-cloud/status/update_topo.md`.
- [x] Write `mqtt/dock-to-cloud/requests/config.md`.
- [x] Write `mqtt/dock-to-cloud/requests/airport_bind_status.md`.
- [x] Write `mqtt/dock-to-cloud/requests/airport_organization_get.md`.
- [x] Write `mqtt/dock-to-cloud/requests/airport_organization_bind.md`.
- [x] Write `mqtt/dock-to-cloud/README.md` as path-level index with sub-phase status table.
- [x] Update `mqtt/README.md` to link the new dock-to-cloud index.
- [x] Update corpus `README.md`.
- [x] **Review gate 4a** closed 2026-04-18. Landing commit `8059992` (5 method docs + dock-to-cloud path index).

### Sub-phase 4b — WaylineManagement (dock-to-cloud)

Re-scoped 2026-04-18 to cover WaylineManagement only (the original 4b-plus-Live-Flight-Controls plan was 63 methods — split into 4b and 4c).

- [x] Enumerate across `DJI_CloudAPI-Dock3-WaylineManagement.txt`, `DJI_CloudAPI-Dock2-Wayline-Management.txt`, v1.11 `50.wayline.md`. 21 methods.
- [x] Draft 5 event docs: `return_home_info`, `flighttask_ready`, `flighttask_progress`, `device_exit_homing_notify`, `in_flight_wayline_progress`.
- [x] Draft 14 service docs: `flighttask_prepare`, `flighttask_execute`, `flighttask_pause`, `flighttask_recovery`, `flighttask_stop`, `flighttask_undo`, `flighttask_create` (deprecated), `return_home`, `return_home_cancel`, `return_specific_home`, `in_flight_wayline_deliver`, `in_flight_wayline_stop`, `in_flight_wayline_recover`, `in_flight_wayline_cancel`.
- [x] Draft 2 request docs: `flighttask_progress_get`, `flighttask_resource_get`.
- [x] Update `mqtt/dock-to-cloud/README.md` with events/services/requests sections.
- [x] Update `mqtt/README.md` and corpus `README.md`.
- [x] **Review gate 4b** closed (implicit — user instructed "Continue at 4c"). Landing commit `7742419` (Phase 4b — WaylineManagement, 21 methods). Reconciled 2026-04-19.

### Sub-phase 4c — Live-Flight-Controls (dock-to-cloud)

**Resume from**: [`RESUME-NOTES.md`](RESUME-NOTES.md) — contains full 4c kick-off context (sources, method inventory, doc template, and handoff gotchas). A fresh session starting with "Continue at 4c" should read RESUME-NOTES first, then [`mqtt/dock-to-cloud/README.md`](mqtt/dock-to-cloud/README.md), then sample docs like [`mqtt/dock-to-cloud/services/flighttask_prepare.md`](mqtt/dock-to-cloud/services/flighttask_prepare.md) before drafting.

**Sources**: `DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt` (4277 lines) + `DJI_CloudAPI-Dock2-Live-Flight-Controls.txt` (2189 lines) + `Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md` for v1.11 DRC reference.

**42 methods** split across three families:
- `events/` (5): `fly_to_point_progress`, `takeoff_to_point_progress`, `drc_status_notify`, `joystick_invalid_notify`, `camera_photo_take_progress`.
- `services/` (~30): `flight_authority_grab`, `payload_authority_grab`, `drc_mode_enter`, `drc_mode_exit`, `takeoff_to_point`, `fly_to_point`, `fly_to_point_stop`, `fly_to_point_update`, and ~22 camera/gimbal/IR setters.
- `drc/` (7): `stick_control`, `drone_control`, `drone_emergency_stop`, `heart_beat`, `hsi_info_push`, `delay_info_push`, `osd_info_push`.

Estimated 3500–4200 lines of doc output — at the edge of a single-drop budget. If context pressure is high, consider splitting into `4c-1` (authority + DRC mode + flight commands + events, ~15 methods) and `4c-2` (camera/gimbal/IR + drc-family, ~27 methods).

- [x] Enumerate + draft 42 methods (5 events + 30 services + 7 drc).
- [x] Update `mqtt/dock-to-cloud/README.md` with events/services/drc sections.
- [x] Update `mqtt/README.md` + corpus `README.md`.
- [x] Append to `RESUME-NOTES.md` with a 4c-close handoff entry.
- [x] **Review gate 4c** closed 2026-04-18 (implicit — user instructed "Continue at 4d").

### Sub-phase 4d — LiveStream + Media-Management (dock-to-cloud)

- [x] Enumerate + draft 9 methods (2 events + 6 services + 1 request). Actual count was smaller than the ~20 estimate because Dock 3 dropped Agora from `live_start_push` and the v1.15 tables collapsed several Dock 2 v1.11 flight-task progress counters into `file_upload_callback`'s optional `flight_task` struct.
  - Events: `highest_priority_upload_flighttask_media`, `file_upload_callback`.
  - Services: `live_start_push`, `live_stop_push`, `live_set_quality`, `live_camera_change`, `live_lens_change`, `upload_flighttask_media_prioritize`.
  - Requests: `storage_config_get`.
- [x] Update `mqtt/dock-to-cloud/README.md` with 4d-sourced entries under events/services/requests and mark 4d landed in the sub-phase status table.
- [x] Update `mqtt/README.md` + corpus `README.md` with the new method count (77 total).
- [x] Append to `RESUME-NOTES.md` with a 4d-close handoff entry.
- [x] **Review gate 4d** closed (implicit — user instructed "Continue at 4e"). Landing commit `debf5f8` (Phase 4d — LiveStream + Media-Management, 9 methods). Reconciled 2026-04-19.

### Sub-phase 4e — Firmware-Upgrade + Remote-Log + Remote-Debugging + Remote-Control (dock-to-cloud)

Re-scoped 2026-04-19 after enumeration — the four source files together contain ~90 methods (not the ~30 estimated in the 4d handoff). Remote-Control alone is 53 methods, so 4e is split into two sub-drops.

#### Sub-phase 4e-1 — Firmware-Upgrade + Remote-Log + Remote-Debugging

- [x] Enumerate + draft 42 methods (2 firmware + 4 log + 13 debug events + 23 debug services).
  - Firmware events: `ota_progress`. Firmware services: `ota_create`.
  - Log events: `fileupload_progress`. Log services: `fileupload_list`, `fileupload_start`, `fileupload_update`.
  - Debug events (13): `esim_operator_switch`, `esim_activate`, `device_format`, `drone_format`, `charge_close`, `charge_open`, `cover_open`, `cover_close`, `device_reboot`, `cover_force_close`, `drone_close`, `drone_open`, `rtk_calibration` (Dock 3 only, `need_reply: 1`).
  - Debug services (23): `esim_operator_switch`, `sim_slot_switch`, `esim_activate`, `sdr_workmode_switch`, `charge_close`, `charge_open`, `cover_close`, `cover_open`, `drone_format`, `device_format`, `drone_close`, `drone_open`, `device_reboot`, `battery_store_mode_switch`, `alarm_state_switch`, `air_conditioner_mode_switch`, `battery_maintenance_switch`, `supplement_light_close`, `supplement_light_open`, `debug_mode_close`, `debug_mode_open`, `cover_force_close`, `rtk_calibration` (Dock 3 only).
- [x] Log [OQ-004](OPEN-QUESTIONS.md#oq-004--fileupload_list-log-window-timestamp-unit-is-inconsistent-across-dji-sources) (log-timestamp unit) and [OQ-005](OPEN-QUESTIONS.md#oq-005--fileupload_start--fileupload_progress-correlation-key-is-undocumented) (fileupload bid linkage).
- [x] Update `mqtt/dock-to-cloud/README.md` with 4e-1 rows (events + services) and mark 4e-1 landed in the sub-phase status table.
- [x] Update `mqtt/README.md` + corpus `README.md` (method count 119).
- [x] Append to `RESUME-NOTES.md` with a 4e-1 close handoff entry.
- [x] **Review gate 4e-1** closed (implicit — user instructed "Continue at 4e-2"). Landing commit `b5c81e3` (Phase 4e-1 — Firmware-Upgrade + Remote-Log + Remote-Debugging, 42 methods). Reconciled 2026-04-19.

#### Sub-phase 4e-2 — Remote-Control (dock-to-cloud)

Source: `DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt` (4611 lines) + `DJI_CloudAPI-Dock2-Remote-Control.txt` (2-file comparison), plus v1.11 Dock 2 `180.remote-control.md`. Estimated 53 methods:

- Events (9, mix of `/events` on Dock 3 and `/drc/up` on Dock 2 — see filing-convention note below): `drc_psdk_floating_window_text`, `drc_speaker_play_progress`, `drc_psdk_state_info`, `drc_psdk_ui_resource`, `drc_drone_state_push`, `drc_camera_state_push`, `drc_camera_osd_info_push`, `drc_ai_info_push`, `drc_camera_photo_info_push` (Dock 2 only; Dock 3 equivalent is 4c's `camera_photo_take_progress`).
- Shared DRC services (10): `drc_force_landing`, `drc_emergency_landing`, `drc_initial_state_subscribe`, `drc_night_lights_state_set`, `drc_stealth_state_set`, `drc_camera_aperture_value_set`, `drc_camera_shutter_set`, `drc_camera_iso_set`, `drc_camera_mechanical_shutter_set`, `drc_camera_dewarping_set`.
- Dock-2-only DRC services (6): `drc_camera_mode_switch`, `drc_linkage_zoom_set`, `drc_video_resolution_set`, `drc_video_storage_set`, `drc_photo_storage_set`, `drc_interval_photo_set`.
- Dock-3-only DRC services (28): `drc_camera_night_mode_set`, `drc_camera_denoise_level_set`, `drc_camera_night_vision_enable`, `drc_infrared_fill_light_enable`, `drc_light_brightness_set`, `drc_light_mode_set`, `drc_light_fine_tuning_set`, `drc_light_calibration`, `drc_speaker_play_mode_set`, `drc_speaker_tts_set`, `drc_speaker_play_volume_set`, `drc_speaker_play_stop`, `drc_speaker_replay`, `drc_speaker_tts_play_start`, `drc_psdk_input_box_text_set`, `drc_psdk_widget_value_set`, `drc_camera_photo_format_set`, `drc_ai_model_select`, `drc_ai_identify_set`, `drc_ai_spotlight_zoom_set`, `drc_ai_spotlight_zoom_track`, `drc_ai_spotlight_zoom_select`, `drc_ai_spotlight_zoom_confirm`, `drc_ai_spotlight_zoom_stop`, `drc_ai_identify_score_mode_set`, `drc_ai_identify_score_set`, `drc_ai_identify_score_reset`, `drc_ai_identify_filter_set`.
- Already covered in 4c: `drone_emergency_stop` — cross-cite, do not re-document.

**Open filing-convention questions** (raise in the resume-notes handoff and decide at 4e-2 kickoff):
1. Several Dock 3 `drc_*` events land on `/events` (standard envelope) while the matching Dock 2 events land on `/drc/up` (lightweight envelope). The method name is identical; only the topic differs. Should these docs live in `events/` or `drc/`? Proposal: file in `drc/` with a prominent topic-divergence note, since the method-name convention (`drc_*` prefix) matches the DRC family rather than the topic.
2. A few Dock 2 services (`drc_camera_mode_switch`) reply on `services_reply` instead of `drc/up`. Filing under `drc/` with the anomaly noted is the simplest option.

- [x] Enumerate + draft 53 methods (9 events + 10 shared services + 6 Dock-2-only services + 28 Dock-3-only services).
  - Events in `drc/`: `drc_psdk_floating_window_text`, `drc_speaker_play_progress`, `drc_psdk_state_info`, `drc_psdk_ui_resource`, `drc_drone_state_push`, `drc_camera_state_push`, `drc_camera_osd_info_push`, `drc_ai_info_push`, `drc_camera_photo_info_push`.
  - Shared DRC services (Dock 2 + Dock 3): `drc_force_landing`, `drc_emergency_landing`, `drc_initial_state_subscribe`, `drc_night_lights_state_set`, `drc_stealth_state_set`, `drc_camera_aperture_value_set`, `drc_camera_shutter_set`, `drc_camera_iso_set`, `drc_camera_mechanical_shutter_set`, `drc_camera_dewarping_set`.
  - Dock-2-only services: `drc_camera_mode_switch`, `drc_linkage_zoom_set`, `drc_video_resolution_set`, `drc_video_storage_set`, `drc_photo_storage_set`, `drc_interval_photo_set`.
  - Dock-3-only services: camera (5) + light (4) + speaker (6) + PSDK widgets (2) + AI identify (11). Full list in [`mqtt/dock-to-cloud/README.md`](mqtt/dock-to-cloud/README.md).
  - `drone_emergency_stop` already in 4c — cross-cited, not re-documented.
- [x] Update `mqtt/dock-to-cloud/README.md` with 4e-2 rows (grouped by sub-area) and the filing-convention note.
- [x] Update `mqtt/README.md` + corpus `README.md` (method count 172).
- [x] Append to `RESUME-NOTES.md` with a 4e-2 / Phase 4e close handoff entry.
- [x] **Review gate 4e** closed (implicit — user instructed "Continue at 4f"). Landing commit `f196c0b` (Phase 4e-2 — Remote-Control, 53 methods + Phase 4e close). Closes the whole 4e sub-phase. Reconciled 2026-04-19.

### Sub-phase 4f — FlySafe + Custom-Flight-Area + AirSense + HMS (dock-to-cloud)

Actual method count was **9** (not ~35). DJI's FlySafe surface is a 3-service tuple (license switch/update/list — no events, no requests); Custom-Flight-Area is 2 events + 1 service + 1 request; AirSense + HMS are 1 event each. The ~35 estimate from the 4e-2 handoff appeared to anticipate distinct per-license-type methods and HMS code-level methods that do not exist at the MQTT transport level (HMS codes are Phase 8 scope).

- [x] Enumerate + draft 9 methods (4 events + 4 services + 1 request).
  - Events: `flight_areas_drone_location` (`need_reply: 0`), `flight_areas_sync_progress` (`need_reply: 1`), `airsense_warning` (`need_reply: 1`), `hms` (no reply).
  - Services: `unlock_license_switch`, `unlock_license_update`, `unlock_license_list`, `flight_areas_update`.
  - Requests: `flight_areas_get`.
- [x] Update `mqtt/dock-to-cloud/README.md` with 4f rows + sub-phase status (landed 2026-04-19) + per-sub-area tables (FlySafe / CFA / AirSense / HMS).
- [x] Update `mqtt/README.md` + corpus `README.md` (method count 181).
- [x] Append to `RESUME-NOTES.md` with a 4f close handoff entry.
- [x] **Review gate 4f** closed 2026-04-19. Landing commit `b186bba` (9 method docs + index updates + session handoff).

### Sub-phase 4g — PSDK + PSDK-Interconnection + ESDK-Interconnection (dock-to-cloud)

Actual method count was **16** (not ~40). PSDK source yields 4 events + 8 services + 1 already-documented request (`storage_config_get`, updated to add `module = 1`). PSDK-Interconnection = 1 event + 1 service. ESDK-Interconnection = 1 event + 1 service. The estimate anticipated payload-state/event methods beyond the transmit passthrough; most of those landed in 4e-2 under `drc/` as their `drc_*` siblings. 4g is the non-DRC counterparts of 4e-2's speaker/widget methods plus the two interconnection passthrough families.

- [x] Enumerate + draft 16 methods (4 events + 8 services from PSDK; 1 event + 1 service each from PSDK-Interconnection + ESDK-Interconnection). Plus `storage_config_get` update.
  - PSDK events: `speaker_tts_play_start_progress`, `speaker_audio_play_start_progress`, `psdk_floating_window_text`, `psdk_ui_resource_upload_result`.
  - PSDK services: `speaker_play_volume_set`, `speaker_play_mode_set`, `speaker_play_stop`, `speaker_replay`, `speaker_tts_play_start`, `speaker_audio_play_start`, `psdk_input_box_text_set`, `psdk_widget_value_set`.
  - PSDK-Interconnection: event `custom_data_transmission_from_psdk`, service `custom_data_transmission_to_psdk`.
  - ESDK-Interconnection: event `custom_data_transmission_from_esdk`, service `custom_data_transmission_to_esdk`.
  - `storage_config_get` updated — `module` enum now documents `0 = Media` (4d) + `1 = PSDK UI resources` (4g); intro + relationship + provenance sections expanded.
- [x] Update `mqtt/dock-to-cloud/README.md` with 4g rows + sub-phase status + new "Sub-phase 4g sub-areas" section grouped by PSDK speaker / PSDK widgets / PSDK-Interconnection / ESDK-Interconnection + filing note for 4g-vs-4e-2 parallel.
- [x] Update `mqtt/README.md` + corpus `README.md` (method count 197).
- [x] Append to `RESUME-NOTES.md` with a 4g close handoff entry.
- [x] **Review gate 4g** closed 2026-04-19. Landing commit `8c24c7b` (16 method docs + `storage_config_get` update + index updates + session handoff).

### Sub-phase 4h — Pilot-to-Cloud (RC Plus 2 Enterprise + RC Pro Enterprise)

Actual method count is **94 unique methods** across the two RC cohorts (est. was ~70). Filing strategy adapted to avoid ~70 thin pointer files: **27 new method docs** for pilot-specific additions (2 events + 5 services + 20 DRC variants + `status/update_topo`), and ~67 parallels covered via cross-reference tables in [`mqtt/pilot-to-cloud/README.md`](mqtt/pilot-to-cloud/README.md) that link directly to their dock-to-cloud counterparts.

- [x] Enumerate methods across `DJI_CloudAPI_RC-Plus-2-Enterprise-*.txt` (4 source files) + `DJI_CloudAPI_RC-Pro-Enterprise-*.txt` (4 source files) + v1.11 Cloud-API-Doc RC Pro subtree. 94 unique methods total.
- [x] Create `mqtt/pilot-to-cloud/` subtree with `status/`, `events/`, `services/`, `drc/` family dirs. No `requests/` dir — RC sources carry no request-family methods.
- [x] Write path-level index [`mqtt/pilot-to-cloud/README.md`](mqtt/pilot-to-cloud/README.md) with filing-convention explainer + five cross-reference tables (status, new events, parallel events, new services, parallel services, new DRC variants, parallel DRC methods) + cohort roll-up + DJI-source inconsistencies section.
- [x] Draft 27 new method docs:
  - `status/update_topo.md` — pilot-specific gateway-sn semantics.
  - Events (2): `events/cloud_control_auth_notify.md`, `events/poi_status_notify.md`.
  - Services (5): `services/cloud_control_auth_request.md`, `services/cloud_control_release.md`, `services/poi_mode_enter.md`, `services/poi_mode_exit.md`, `services/poi_circle_speed_set.md`.
  - DRC variants (20): `drc/drc_live_lens_change.md` + 19 `drc/drc_camera_*.md` / `drc/drc_ir_metering_*.md` / `drc/drc_gimbal_reset.md` (pilot-side lightweight-DRC variants of the dock-to-cloud 4c camera / IR / gimbal services).
- [x] Update `mqtt/README.md` + corpus `README.md` to cite the 94-method count and the 4h landing.
- [x] Append to `RESUME-NOTES.md` with a 4h close handoff entry.
- [x] **Review gate 4h** closed 2026-04-19. Landing commit `2228c33` (27 pilot-specific method docs + cross-reference tables + session handoff).

### Sub-phase 4i — Property-family shells (dock-to-cloud + pilot-to-cloud)

Thin shells per family (not per device). One README per (path × family) — 6 READMEs total. Each shell records wire-level topic + push semantics + in-scope devices + property source files + forward pointer to Phase 6 `device-properties/` (pending). Full per-property catalog deferred to Phase 6.

- [x] Write `mqtt/dock-to-cloud/osd/README.md`, `mqtt/dock-to-cloud/state/README.md`, `mqtt/dock-to-cloud/property-set/README.md` — Dock 2 + Dock 3 + M3D + M3TD + M4D + M4TD coverage.
- [x] Write `mqtt/pilot-to-cloud/osd/README.md`, `mqtt/pilot-to-cloud/state/README.md`, `mqtt/pilot-to-cloud/property-set/README.md` — RC Plus 2 + RC Pro coverage. Pilot OSD shell carries the OQ-002 copy-paste-bug callout.
- [x] Update `mqtt/dock-to-cloud/README.md` + `mqtt/pilot-to-cloud/README.md` to link the new shells.
- [x] Update `mqtt/README.md` + corpus `README.md` to cite the 4i landing.
- [x] Append to `RESUME-NOTES.md` with a 4i close handoff entry.
- [x] **Final Phase 4 review gate** closed 2026-04-19. Phase 4 content-complete.

## Phase 5 — WebSocket message catalog

Enumerated 8 push messages across two families from the v1.15 extracts (`DJI_CloudAPI_Pilot-WebSocket-Map-Elements-Push-Message.txt` + `DJI_CloudAPI_Pilot-WebSocket-Situation-Awareness-Push-Message.txt`) and verified against v1.11 canonical (`Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/20.websocket/`). No divergences between versions.

- [x] Enumerate all push message types. 8 messages total: 4 map-elements + 4 situation-awareness.
- [x] Write 8 per-message docs:
  - `websocket/map-elements/` — `map_element_create.md`, `map_element_update.md`, `map_element_delete.md`, `map_group_refresh.md`.
  - `websocket/situation-awareness/` — `device_osd.md`, `device_online.md`, `device_offline.md`, `device_update_topo.md`.
- [x] Update `websocket/README.md` with per-message catalog links (jump table in §4).
- [x] Update corpus `README.md`.
- [x] Append to `RESUME-NOTES.md` with a Phase 5 close handoff.
- [x] **Review gate** closed 2026-04-19. Landing commit `9f93a3a` (8 WebSocket push messages + catalog index + session handoff).

## Phase 6 — Device properties

**Scope decision (2026-04-19):** Phase 6 is sub-phased because the combined property surface across 8 in-scope devices totals ~1,400 unique property rows (5,676 source lines). Sub-drops:
- **6a** — Master matrix README + Dock 2 + Dock 3 (gateway-level, ~400 lines of output).
- **6b** — Aircraft: M3D, M3TD, M4D, M4TD. Each aircraft doc has two sections — dock-path properties and pilot-path properties — because the same aircraft is reported by two different gateways (dock vs RC) with distinct property subsets. Shared aircraft properties extracted into `_aircraft-pilot-base.md`.
- **6c** — RCs: RC Plus 2 Enterprise + RC Pro Enterprise. Gateway-level properties.

Each sub-phase has its own review gate. Design decisions locked at 6a kickoff (2026-04-19):
- Master matrix layout: property-per-row with device-support columns (✓ / ✓ rw / blank), grouped by semantic family, built incrementally as sub-drops land.
- Per-device doc layout: three sections — OSD (pushMode=0), State (pushMode=1), Settable (accessMode=rw) — with nested struct fields preserved via DJI's `»` prefix.
- v1.11 vs v1.15 drift: flag inline, prefer v1.15, escalate to [`OPEN-QUESTIONS.md`](OPEN-QUESTIONS.md) only when semantic (no 6a escalations; all dock drift is enum-extension or cosmetic).
- Out-of-scope devices (Dock 1, M30/M30T, M300/M350, M400, Mavic 3E, plain RC): noted in enum tables where their values appear; no per-device doc.

### Sub-phase 6a — Master matrix + Dock 2 + Dock 3 (gateway-level)

- [x] Enumerate Dock 2 + Dock 3 gateway properties. Dock 2: 48 top-level (36 OSD + 12 state). Dock 3: 49 top-level (37 OSD + 12 state — adds `self_converge_coordinate`).
- [x] Draft [`device-properties/README.md`](device-properties/README.md) — master matrix + narrative + dock-gateway coverage table.
- [x] Draft [`device-properties/dock2.md`](device-properties/dock2.md) — full property catalog + 6 DJI-source inconsistencies + v1.11 → v1.15 drift table.
- [x] Draft [`device-properties/dock3.md`](device-properties/dock3.md) — full property catalog + 5 DJI-source inconsistencies + drift-vs-Dock-2 table.
- [x] Update 4i dock-to-cloud shells ([`mqtt/dock-to-cloud/osd/`](mqtt/dock-to-cloud/osd/README.md), [`state/`](mqtt/dock-to-cloud/state/README.md), [`property-set/`](mqtt/dock-to-cloud/property-set/README.md)) to link the real Phase 6 docs. Corrected the 4i property-set shell's speculative writable-property list — actual Dock 2/3 writable surface is just 3 properties (`silent_mode`, `user_experience_improvement`, `air_transfer_enable`), not the 7 the 4i shell guessed.
- [x] Update corpus [`README.md`](README.md).
- [x] Append to [`RESUME-NOTES.md`](RESUME-NOTES.md) with a 6a close handoff.
- [x] **Review gate 6a** closed 2026-04-19 (implicit — user instructed "Continue at 6b"). Landing commit `0715951` (Phase 6a master matrix + Dock 2 + Dock 3).

### Sub-phase 6b — Aircraft properties (M3D, M3TD, M4D, M4TD)

- [x] `device-properties/_aircraft-pilot-base.md` — shared pilot-path aircraft property catalog (34 OSD + 8 state top-level + `{type-subtype-gimbalindex}` struct, from `DJI_CloudAPI_Aircraft-Properties.txt`).
- [x] `device-properties/m3d.md` — dock-path (42 top-level, from `DJI_CloudAPI_M3D_M3DT_Properties.txt`) + pilot-path (inherits `_aircraft-pilot-base.md`; M3-series has no M3D-specific pilot-path extensions in v1.11 canonical).
- [x] `device-properties/m3td.md` — thermal-variant annex; same property catalog as M3D, difference expressed via `payload_index` enum.
- [x] `device-properties/m4d.md` — dock-path (42 top-level, from `DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt`) + pilot-path (baseline + 7 M4D-specific extensions from `DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`: `offline_map_enable`, `current_rth_mode`, `rth_mode`, `commander_flight_height`, `commander_flight_mode`, `current_commander_flight_mode`, `commander_mode_lost_action` + `mode_code` enum extension to value 19).
- [x] `device-properties/m4td.md` — thermal-variant annex.
- [x] Extend master matrix README §4.2 (aircraft-level coverage table — 56-property-row grid across dock-path / pilot-path / M3 / M4 cohorts).
- [x] Update 4i dock-to-cloud + pilot-to-cloud shells (`osd/`, `state/`, `property-set/`) to link the real Phase 6b docs.
- [x] Update corpus `README.md`.
- [x] Append to `RESUME-NOTES.md`.
- [x] **Review gate 6b** closed 2026-04-19. Landing commit `defcbb3` (5 new device-properties docs + master matrix §4.2 + 6 shell updates + session handoff).

### Sub-phase 6c — RC properties (RC Plus 2 Enterprise, RC Pro Enterprise)

Actual shape confirmed 2026-04-19: each RC carries 11 top-level properties (6 OSD + 5 state). **Both are fully read-only at the gateway level** — no `accessMode: rw` properties on either RC. The two RCs are not delta-of-each-other: RC Pro has `country` (absent on RC Plus 2); RC Plus 2 has `drc_state` (absent on RC Pro). `live_status.»video_quality` enums are incompatible (RC Pro 5-value vs RC Plus 2 4-value).

- [x] [`device-properties/rc-plus-2.md`](device-properties/rc-plus-2.md) — RC Plus 2 Enterprise full catalog. 11 top-level properties (6 OSD + 5 state), 0 writable. 5 DJI-source inconsistencies flagged. §5 drift vs RC Pro (3 rows: `drc_state` add, `country` absent, `video_quality` enum swap). No v1.11 counterpart.
- [x] [`device-properties/rc-pro.md`](device-properties/rc-pro.md) — RC Pro Enterprise full catalog. 11 top-level properties (6 OSD + 5 state), 0 writable. 5 DJI-source inconsistencies flagged (includes near-equivalence note vs out-of-scope plain-RC file). §5 v1.11 → v1.15 drift (adds `cloud_control_auth`; no other changes) plus vs-RC-Plus-2 summary.
- [x] Update 4i pilot-to-cloud shells — [`osd/`](mqtt/pilot-to-cloud/osd/README.md), [`state/`](mqtt/pilot-to-cloud/state/README.md), [`property-set/`](mqtt/pilot-to-cloud/property-set/README.md). Corrected the 4i `property-set` shell's speculative writable list — actual RC writable surface is **zero** (not SIM-slot / DRC-preferences / livestream-toggles as the shell guessed).
- [x] Extend master matrix README §4.3 — 12-row RC coverage table + unique-property summary + out-of-scope plain-RC note.
- [x] Update corpus [`README.md`](README.md).
- [x] Append to [`RESUME-NOTES.md`](RESUME-NOTES.md).
- [x] **Final Phase 6 review gate** closed 2026-04-19. Landing commit `bed52f8` (Phase 6c — RC Plus 2 Enterprise + RC Pro Enterprise + session handoff). Phase 6 content-complete.

## Phase 7 — Auxiliary specs (WPML + livestream protocols)

Single-drop phase (no sub-phases). All 4 WPML files + 4 livestream-protocol files delivered together in one review gate, matching the PLAN.md Phase 7 intent.

WPML:
- [x] [`wpml/overview.md`](wpml/overview.md) — format intro, `.kmz` archive layout, device-support conventions, labeling inconsistency (M4E/M4T vs M4D/M4TD), existing-route upgrade note.
- [x] [`wpml/template-kml.md`](wpml/template-kml.md) — `template.kml` catalog. Covers create info + mission config + 4 template types (`waypoint` / `mapping2d` / `mapping3d` / `mappingStrip`) + waypoint info + coordinate params + overlap rates + mapping heading param. 5 DJI-source inconsistencies flagged.
- [x] [`wpml/waylines.md`](wpml/waylines.md) — `waylines.wpml` catalog. Covers mission config + wayline Folder + waypoint Placemark + `executeHeightMode` vs template `heightMode` distinction + `startActionGroup`. Cross-links to `common-elements.md` for shared structs.
- [x] [`wpml/common-elements.md`](wpml/common-elements.md) — shared schemas. Covers `<wpml:droneInfo>` / `<wpml:payloadInfo>` / `<wpml:payloadParam>` / heading & turn params / `<wpml:autoRerouteInfo>` (new-gen only) / action chain + **16 actuator functions** with full parameter tables. Includes M4D/M4TD-only `megaphone` + `searchlight` actions. 9 DJI-source inconsistencies flagged (enum completeness, typos, translation artifacts including Chinese char in `megaphoneOperateLoop` label).
- [x] [`wpml/README.md`](wpml/README.md) — path-level index.

Livestream protocols:
- [x] [`livestream-protocols/rtmp.md`](livestream-protocols/rtmp.md) — `url_type 1`. All 4 in-scope cohorts. URL shape `rtmp://host:port/app/stream`. Cloud-side requirement: RTMP ingest server (nginx-rtmp, SRS, commercial).
- [x] [`livestream-protocols/gb28181.md`](livestream-protocols/gb28181.md) — `url_type 3`. All 4 in-scope cohorts. URL shape: 7 kv pairs amp-joined. SIP registration + PS-over-RTP media. Cloud-side requirement: GB28181 SIP server + 20-digit ID allocation.
- [x] [`livestream-protocols/webrtc.md`](livestream-protocols/webrtc.md) — `url_type 4` / WHIP only. **Not on RC Pro.** URL shape: HTTP endpoint `http://host:port/{whip-path}?app=...&stream=...`. Cloud-side requirement: WHIP ingest + STUN/TURN.
- [x] [`livestream-protocols/agora.md`](livestream-protocols/agora.md) — `url_type 0`. **Not on Dock 3.** URL shape: `channel=...&sn=...&token=...&uid=...`. URL-encoding-once rule for `+` in tokens flagged. Cloud-side requirement: Agora App ID + App Certificate + viewer subscriber / Cloud Recording.
- [x] [`livestream-protocols/README.md`](livestream-protocols/README.md) — path-level index with cross-cohort protocol matrix + JSBridge `type` enum cross-transport context note.

- [x] Update corpus [`README.md`](README.md).
- [x] Append to [`RESUME-NOTES.md`](RESUME-NOTES.md).
- [x] **Review gate** closed 2026-04-19. Landing commit `03a5006` (Phase 7 — WPML + livestream protocols, 10 docs + session handoff).

## Phase 8 — Codes (HMS + error codes)

Single-drop phase (no sub-phases). HMS codes + error codes delivered together. Reproducible generator pipeline under [`_build/`](_build/) — [`_translations.json`](_build/_translations.json) + two Python generators consume [`DJI_Cloud/HMS.json`](../DJI_Cloud/HMS.json) and [`DJI_Cloud/DJI_CloudAPI-HMS-Codes.txt`](../DJI_Cloud/DJI_CloudAPI-HMS-Codes.txt) and emit the catalog on re-run.

HMS codes:
- [x] Inspect [`DJI_Cloud/HMS.json`](../DJI_Cloud/HMS.json) structure — 1,769 entries; distribution by first-byte prefix identified 14 natural buckets (0x11 payload / 0x12 battery station / 0x14 payload IMU / 0x15 mmWave / 0x16 flight-control 921× / 0x17 transmission / 0x19 system-overload / 0x1A vision / 0x1B navigation / 0x1C camera / 0x1D gimbal / 0x1E PSDK payload / 0x1F cellular / 0x20 takeoff tags), plus 1 non-hex outlier (`unknown`).
- [x] Propose recommended layout to user (14 per-prefix files + README + outliers; 0x16 sub-sectioned by second byte for navigability). **Approved** 2026-04-19.
- [x] **531 CJK-in-`tipEn` entries translated.** DJI leaked Chinese developer-debug strings under the "English" copy key. Curated EN translations stored in [`_build/_translations.json`](_build/_translations.json); display flagged with trailing **+**; CN source preserved verbatim under collapsible blocks.
- [x] Generate 14 per-prefix files + [`hms-codes/README.md`](hms-codes/README.md) + [`hms-codes/outliers.md`](hms-codes/outliers.md) via [`_build/generate_hms_codes.py`](_build/generate_hms_codes.py). All 1,769 entries preserved verbatim.

Error codes:
- [x] Catalog 448 codes from [`DJI_Cloud/DJI_CloudAPI-HMS-Codes.txt`](../DJI_Cloud/DJI_CloudAPI-HMS-Codes.txt) (v1.15 authoritative — the filename mentions "HMS" but DJI's preamble clarifies the content is general API error codes, NOT HMS alarms). 20 function modules. v1.11 → v1.15 drift: 5 new codes (`321788`, `327022`, `341002`, `514155`, `514168`), 0 dropped.
- [x] [`error-codes/README.md`](error-codes/README.md) — single doc with grouped tables per BC module + format explanation (`ABCDEF` = source + module + local) + cross-reference to DJI-Cloud-API-Demo enum classes (`FirmwareErrorCodeEnum` / `WaylineErrorCodeEnum` / `LogErrorCodeEnum` / `CommonErrorEnum` / `DebugErrorCodeEnum` / `ControlErrorCodeEnum` / `LiveErrorCodeEnum` / `DrcStatusErrorEnum`). Generator: [`_build/generate_error_codes.py`](_build/generate_error_codes.py).

- [x] Update corpus [`README.md`](README.md).
- [x] Append to [`RESUME-NOTES.md`](RESUME-NOTES.md).
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
