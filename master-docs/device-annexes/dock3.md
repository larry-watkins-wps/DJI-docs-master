# Device Annex — DJI Dock 3

**Cohort**: Dock 3 (current generation) — Dock 3 + M4D / M4TD + RC Plus 2 Enterprise.
**Gateway role**: dock gateway. Serial appears as `{device_sn}` for Dock 3's own telemetry and as `{gateway_sn}` for paired aircraft telemetry.
**Primary sources**: [`DJI_Cloud/DJI_CloudAPI-Dock3-DeviceProperties.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock3-DeviceProperties.txt) (v1.15) + `DJI_CloudAPI-Dock3-*.txt` family (all v1.15) — no v1.11 canonical counterpart (Dock 3 postdates v1.11.3).

---

## 1. Distinctive wire surface

Dock 3 is the **current-generation dock**. Its property surface is a **strict superset of Dock 2** (plus refined enum labels), and it carries the richest MQTT method surface in the corpus — 197 methods on [`../mqtt/dock-to-cloud/README.md`](../mqtt/dock-to-cloud/README.md), many of which are Dock-3-only. Dock 3 is the only dock with `self_converge_coordinate` calibration output, `in_flight_wayline_*` mission choreography, AI identify / spotlight subsystem, and PSDK speaker / light / searchlight control.

### Property surface (Phase 6a)

- **49 top-level gateway properties** (37 OSD + 12 state) — see [`../device-properties/dock3.md`](../device-properties/dock3.md).
- **3 writable via `property/set`**: `air_transfer_enable`, `silent_mode`, `user_experience_improvement` (same keys as Dock 2).
- **`self_converge_coordinate` OSD struct** — **Dock 3 only**. Publishes self-convergence calibration lat/lon/height once the calibration run completes.
- **`home_position_is_valid` 4-value enum** — Dock 3 distinguishes partial-calibration states (`2`: heading valid, lat/lon invalid; `3`: lat/lon valid, heading invalid) that Dock 2 collapses to a 2-value `{0 Invalid, 1 Valid}` form.
- **`air_transfer_enable` scope** — Dock 3 source documents that this writable key now affects FlyTo **and** Wayline tasks (Dock 2 documented only commanded-flight scope).

### MQTT methods (Phase 4) — Dock-3-exclusive surface

| Family | Dock-3-only methods | Phase 4 sub-phase |
|---|---|---|
| Events | `rtk_calibration` (`need_reply: 1`) | [4e-1](../mqtt/dock-to-cloud/events/rtk_calibration.md) |
| DRC services — AI identify | 11 — `drc_ai_model_select`, `drc_ai_identify_set`, `drc_ai_identify_filter_set`, `drc_ai_identify_score_mode_set`, `drc_ai_identify_score_set`, `drc_ai_identify_score_reset`, `drc_ai_spotlight_zoom_set`, `drc_ai_spotlight_zoom_track`, `drc_ai_spotlight_zoom_select`, `drc_ai_spotlight_zoom_confirm`, `drc_ai_spotlight_zoom_stop` | [4e-2](../mqtt/dock-to-cloud/README.md) |
| DRC services — PSDK speaker | 6 — `drc_speaker_play_mode_set`, `drc_speaker_tts_set`, `drc_speaker_play_volume_set`, `drc_speaker_play_stop`, `drc_speaker_replay`, `drc_speaker_tts_play_start` | [4e-2](../mqtt/dock-to-cloud/README.md) |
| DRC services — PSDK widgets | 2 — `drc_psdk_input_box_text_set`, `drc_psdk_widget_value_set` | [4e-2](../mqtt/dock-to-cloud/README.md) |
| DRC services — night / IR / searchlight | 4 — `drc_camera_night_mode_set`, `drc_camera_denoise_level_set`, `drc_camera_night_vision_enable`, `drc_infrared_fill_light_enable` | [4e-2](../mqtt/dock-to-cloud/README.md) |
| DRC services — light control | 4 — `drc_light_brightness_set`, `drc_light_mode_set`, `drc_light_fine_tuning_set`, `drc_light_calibration` | [4e-2](../mqtt/dock-to-cloud/README.md) |
| DRC services — camera photo format | 1 — `drc_camera_photo_format_set` | [4e-2](../mqtt/dock-to-cloud/README.md) |
| PSDK events (standard `/events` envelope) | 4 — `speaker_tts_play_start_progress`, `speaker_audio_play_start_progress`, `psdk_floating_window_text`, `psdk_ui_resource_upload_result` | [4g](../mqtt/dock-to-cloud/README.md) |
| PSDK services | 8 — `speaker_play_volume_set`, `speaker_play_mode_set`, `speaker_play_stop`, `speaker_replay`, `speaker_tts_play_start`, `speaker_audio_play_start`, `psdk_input_box_text_set`, `psdk_widget_value_set` | [4g](../mqtt/dock-to-cloud/README.md) |
| Wayline services (in-flight) | 4 — `in_flight_wayline_deliver`, `in_flight_wayline_stop`, `in_flight_wayline_recover`, `in_flight_wayline_cancel` | [4b](../mqtt/dock-to-cloud/README.md) — Dock-3-primary; Dock 2 source does not document |
| Wayline events (in-flight) | 1 — `in_flight_wayline_progress` | [4b](../mqtt/dock-to-cloud/README.md) |

The Phase 4e-2 index ([`mqtt/dock-to-cloud/README.md`](../mqtt/dock-to-cloud/README.md) §"Sub-phase 4e-2 sub-areas") splits the 28 Dock-3-only DRC services into semantic sub-areas (camera / light / speaker / PSDK widgets / AI identify). Dock 3 does **not** carry the 6 Dock-2-only DRC services (`drc_camera_mode_switch`, `drc_linkage_zoom_set`, `drc_video_resolution_set`, `drc_video_storage_set`, `drc_photo_storage_set`, `drc_interval_photo_set`) — their Dock-3 analogues use different method names and payloads.

### Workflows (Phase 9)

Dock 3 participates in every Phase 9 workflow. Dock-3-specific branches:

- [`firmware-and-config-update.md`](../workflows/firmware-and-config-update.md) — adds `firmware_upgrade_type: 4` PSDK update path not present on Dock 2; v1.11 `step_key` → v1.15 `current_step` field rename on `ota_progress` (Dock 3 uses v1.15 naming throughout).
- [`wayline-upload-and-execution.md`](../workflows/wayline-upload-and-execution.md) — Dock 3 supports the `in_flight_wayline_*` family for mid-flight wayline substitution. No Dock 2 counterpart.
- [`live-flight-controls-drc.md`](../workflows/live-flight-controls-drc.md) — AI identify + spotlight control (11 services) + PSDK speaker / light / searchlight (16 services) are Dock-3-exclusive within the DRC session.
- [`livestream-start-stop.md`](../workflows/livestream-start-stop.md) — **no Agora** (`url_type: 0` dropped from the Dock 3 enum). Live example payload in the Dock 3 source shows `url_type: 0` which is a DJI copy-paste defect (flagged in [`live_start_push.md`](../mqtt/dock-to-cloud/services/live_start_push.md)).

### Livestream protocols (Phase 7)

| Protocol | `url_type` | Supported |
|---|---|---|
| Agora | `0` | — (dropped — see Phase 7 notes) |
| RTMP | `1` | ✓ |
| GB28181 | `3` | ✓ |
| WebRTC (WHIP) | `4` | ✓ |

Dock 3's `url_type` enum in [`DJI_CloudAPI-Dock3-LiveStream.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock3-LiveStream.txt) lists only `{1, 3, 4}`. Cloud implementations must not serve an Agora URL to Dock 3 — Dock 3 firmware will reject.

### HMS + error codes (Phase 8)

Dock 3 emits the full HMS catalog (1,769 alarms in [`../hms-codes/`](../hms-codes/README.md)) — airframe-keyed, not dock-keyed. Copy-key splicing uses `dock_tip_{code}` for dock-tier UI and `fpv_tip_{code}[_in_the_sky]` for FPV-tier. General API error codes — Dock 3 participates across all 20 BC modules.

---

## 2. Cohort asymmetries (Dock 3 vs Dock 2)

Summarized in the Dock 2 annex ([`dock2.md`](dock2.md) §2) and documented in detail in [`../device-properties/dock3.md`](../device-properties/dock3.md) §5. Dock 3 layer:

- **Property-superset** — every Dock 2 property is present on Dock 3. Dock 3 adds `self_converge_coordinate`.
- **Enum-refinement across the board** — Dock 3 silently fixes Dock 2 source defects (duplicate `"Poor"` labels in `network_state.quality`, Chinese leftovers in `wireless_link.*_link_state` and `flighttask_step_code`, short carrier labels in `dongle_infos.»esim_infos.telecom_operator`). Semantics are identical; cloud implementations parsing by code (not label) will not observe these.
- **Method-superset on most families** (Phase 4e-1 `rtk_calibration`, Phase 4e-2 28 DRC services, Phase 4g PSDK family) — Dock 3 adds methods Dock 2 doesn't have.
- **Method-subset on 6 Dock-2-only DRC services** — Dock 3 drops these because the functionality is either subsumed into newer methods (e.g. camera mode is implied by the camera's current config on Dock 3) or replaced with a distinct method name / payload (photo storage is configured by `air_transfer_enable` + HTTP STS, not a DRC service).
- **Livestream asymmetry** — Dock 3 drops Agora; Dock 2 retains it.

Dock 3 is **forward-compatible** with Dock 2 clouds that parse by code and ignore unknown methods. Dock 2 is **not fully backward-compatible** with a Dock-3-aware cloud — a cloud that assumes Dock-3 method surface will observe absent replies on Dock 2 for the Dock-3-only methods.

---

## 3. Implementation gotchas

Carry from Phase 6a [`../device-properties/dock3.md`](../device-properties/dock3.md) §4:

1. **`air_conditioner.air_conditioner_state` malformed enum values `10`–`15`** in the Dock 3 source extract are the same extraction-tool defect as Dock 2. Authoritative range is `0`–`9`. Treat `10`+ as undefined.
2. **`sim_info.telecom_operator` disagrees with `esim_infos.telecom_operator` within the Dock 3 source extract itself.** `esim_infos.telecom_operator` uses fully-qualified names (`"China Mobile"`, etc.); `sim_info.telecom_operator` reverts to Dock-2-style short labels (`"Mobile"`, `"Telecommunications"`). Codes are identical; parse by code.
3. **Dock 3 example payload contains three fields not in the property list**: `electric_supply_voltage`, `flighttask_prepare_capacity`, `air_conditioner_mode`. Treat as list-omission defects; accept but do not rely on.
4. **`putter_state` absent from Dock 3 source examples** (present on Dock 2) — tolerate its absence on Dock 3 telemetry.
5. **`live_start_push` example payload in Dock 3 source uses `url_type: 0`** — invalid per the Dock 3 enum. Ignore the example; trust the enum (`{1, 3, 4}`).

Phase 4 / Phase 9 gotchas:

6. **`ota_progress` v1.11 → v1.15 field rename** — Dock 3 uses `current_step` (v1.15); older implementations may still emit `step_key` during the transition. [`firmware-and-config-update.md`](../workflows/firmware-and-config-update.md) documents the rename.
7. **`firmware_upgrade_type: 4` Dock-3-only PSDK update** — cloud implementations triggering firmware updates on Dock 3 can use this type to target PSDK modules separately. No Dock 2 counterpart.
8. **DRC camera aperture labels use underscores on Dock 3** (`"F2_2"`, `"F2_8"`) vs Dock 2's dot form (`"F2.2"`, `"F2.8"`). Same F-stops, different strings. See [`drc/drc_camera_aperture_value_set.md`](../mqtt/dock-to-cloud/drc/drc_camera_aperture_value_set.md).
9. **Dock 3 HMS `hms` event example shows `"timestamp:"` with a trailing colon** — DJI source typo (example syntax-invalid). Cloud parsers should tolerate or reject at schema validation layer; not indicative of real wire value. Flagged in [`events/hms.md`](../mqtt/dock-to-cloud/events/hms.md).
10. **`flight_areas_drone_location` schema table drops `area_id` on Dock 3** but the example carries it. Treat example as authoritative; `area_id` is required for per-area distance telemetry. Flagged in [`flight_areas_drone_location.md`](../mqtt/dock-to-cloud/events/flight_areas_drone_location.md).

---

## 4. Features this device lacks

- No Agora livestream (`url_type: 0` dropped from enum).
- No Dock-2-only DRC services (6 methods; see Dock 2 annex §1).
- No `drc_camera_photo_info_push` event — Dock 3 uses [`events/camera_photo_take_progress.md`](../mqtt/dock-to-cloud/events/camera_photo_take_progress.md) (Phase 4c) with standard `/events` envelope instead.

---

## 5. Third-party Dock 3 evidence

[`dji_cloud_dock3/`](../../dji_cloud_dock3/) is a non-authoritative third-party reference implementation (Spring Boot 2.7.12 + Vue 3, Java 11) adapted from DJI's v1.10.0 demo to target Dock 3. It is **not** a DJI-authored source; its presence in the repo is context only. Where its behaviour diverges from the v1.15 DJI_Cloud extracts, the DJI source wins.

What's useful from this repo:
- **Dock-3-specific service handler patterns** for airsense, config, device-management, firmware, FlySafe (`source/` backend directory). Corroborates Phase 4 method surface for Dock 3.
- **Postman collection** for API testing — verifies Phase 3 HTTP endpoint shapes.
- **Frontend Vue dashboard** — operator-facing UI; not load-bearing for wire contract.

What is **not** authoritative:
- The repo is based on v1.10.0 demo code, not v1.15 wire contract. QoS / retain / auth defaults in this repo reflect v1.10 demo behaviour — see [OQ-003 resolution](../OPEN-QUESTIONS.md#oq-003--mqtt-qos-retain-and-clean-session-settings-are-not-specified-in-djis-published-documentation) for the canonical demo-code scan.

---

## 6. Cross-reference map

| Phase | Doc | What's covered |
|---|---|---|
| 3 HTTP | [`../http/README.md`](../http/README.md) | 16 endpoints — Dock 3 participates in all 16. |
| 4 MQTT | [`../mqtt/dock-to-cloud/README.md`](../mqtt/dock-to-cloud/README.md) | 197 methods. Dock-3-exclusive surface listed in §1 above. |
| 5 WebSocket | [`../websocket/README.md`](../websocket/README.md) | Pilot-to-cloud only; Dock 3 does not participate. |
| 6 Properties | [`../device-properties/dock3.md`](../device-properties/dock3.md) | 49 top-level properties + v1.11 → v1.15 drift (superset of Dock 2). |
| 7 WPML + livestream | [`../livestream-protocols/README.md`](../livestream-protocols/README.md) | RTMP / GB28181 / WebRTC; no Agora. |
| 8 Codes | [`../hms-codes/README.md`](../hms-codes/README.md), [`../error-codes/README.md`](../error-codes/README.md) | Full catalog. |
| 9 Workflows | [`../workflows/README.md`](../workflows/README.md) | Full participant in all 11 workflows; Dock-3-exclusive branches noted in §1. |

## 7. Source provenance

| File | Role |
|---|---|
| [`DJI_Cloud/DJI_CloudAPI-Dock3-DeviceProperties.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock3-DeviceProperties.txt) | v1.15 property primary (680 lines). |
| [`DJI_Cloud/DJI_CloudAPI-Dock3-*.txt`](../../DJI_Cloud/) (DeviceManagement, Organization-Management, Configuration-Update, WaylineManagement, Live-Flight-Controls, LiveStream, Firmware-Upgrade, Remote-Log, Remote-Debugging, Remote-Control, FlySafe, Custom-Flight-Area, AirSense, HMS-Events, PSDK, PSDK-Interconnection, ESDK-Interconnection) | v1.15 per-feature extracts. |
| [`dji_cloud_dock3/`](../../dji_cloud_dock3/) | Third-party v1.10 reference implementation — non-authoritative context. |
| [`Cloud-API-Doc/docs/en/30.feature-set/20.dock-feature-set/`](../../Cloud-API-Doc/docs/en/30.feature-set/20.dock-feature-set/) | v1.11 choreography narrative — cited by Phase 9 workflows; no v1.15 equivalent. Dock 3 post-dates; used only for shared-with-Dock-2 narrative. |
