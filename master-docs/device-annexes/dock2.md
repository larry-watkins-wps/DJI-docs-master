# Device Annex — DJI Dock 2

**Cohort**: Dock 2 (older generation) — Dock 2 + M3D / M3TD + RC Pro Enterprise.
**Gateway role**: dock gateway. Serial appears as `{device_sn}` for Dock 2's own telemetry and as `{gateway_sn}` for paired aircraft telemetry.
**Primary sources**: [`DJI_Cloud/DJI_CloudAPI-Dock2-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock2-Properties.txt) (v1.15) + [`DJI_CloudAPI-Dock2-*.txt`](../../DJI_Cloud/) family (all v1.15) + [`Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/`](../../Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/) (v1.11 canonical, drift-only).

---

## 1. Distinctive wire surface

Dock 2 is the **older-generation dock** — a subset of Dock 3 at the property level, with a handful of wire-level features that Dock 3 drops or renames. For a wire-level implementation, Dock 2 is essentially "Dock 3 minus a few AI / PSDK methods, plus Agora livestream, plus some source extraction artifacts."

### Property surface (Phase 6a)

- **48 top-level gateway properties** (36 OSD + 12 state) — see [`../device-properties/dock2.md`](../device-properties/dock2.md).
- **3 writable via `property/set`**: `air_transfer_enable`, `silent_mode`, `user_experience_improvement`.
- Dock 2 does **not** carry `self_converge_coordinate` (Dock 3 only).
- `air_transfer_enable` wording on Dock 2 documents **commanded-flight scope only**. Dock 3 extends this to FlyTo + Wayline. Cloud implementations writing this key on Dock 2 should not assume wayline/FlyTo-task applicability.

### MQTT methods (Phase 4)

Dock 2 participates in every Phase 4 sub-phase except the four **Dock-3-only** additions:
- `rtk_calibration` event (Phase 4e-1) — Dock 3 only.
- 28 Dock-3-only DRC services (Phase 4e-2) across camera night / IR / searchlight / speaker / PSDK widgets / AI identify — see [`../mqtt/dock-to-cloud/README.md`](../mqtt/dock-to-cloud/README.md) §"Sub-phase 4e-2 sub-areas" for the enumerated list.
- 8 PSDK services + 4 events (Phase 4g) — Dock 2 does **not** publish `speaker_tts_play_start_progress`, `speaker_audio_play_start_progress`, `psdk_floating_window_text`, `psdk_ui_resource_upload_result`; the parallel `drc_*` forms on Dock 2 land in the Phase 4e-2 `/drc/up` topic with lightweight envelopes.

Dock 2 carries **6 DRC services that Dock 3 does not**:

| Method | Purpose | Phase 4 entry |
|---|---|---|
| `drc_camera_mode_switch` | Switch still / video mode | [`drc/drc_camera_mode_switch.md`](../mqtt/dock-to-cloud/drc/drc_camera_mode_switch.md) |
| `drc_linkage_zoom_set` | Wide-to-zoom linkage | [`drc/drc_linkage_zoom_set.md`](../mqtt/dock-to-cloud/drc/drc_linkage_zoom_set.md) |
| `drc_video_resolution_set` | Video resolution preset | [`drc/drc_video_resolution_set.md`](../mqtt/dock-to-cloud/drc/drc_video_resolution_set.md) |
| `drc_video_storage_set` | Video storage preference | [`drc/drc_video_storage_set.md`](../mqtt/dock-to-cloud/drc/drc_video_storage_set.md) |
| `drc_photo_storage_set` | Photo storage preference | [`drc/drc_photo_storage_set.md`](../mqtt/dock-to-cloud/drc/drc_photo_storage_set.md) |
| `drc_interval_photo_set` | Interval-photo capture | [`drc/drc_interval_photo_set.md`](../mqtt/dock-to-cloud/drc/drc_interval_photo_set.md) |

Dock 2 also emits `drc_camera_photo_info_push` (Phase 4e-2); Dock 3's equivalent is `camera_photo_take_progress` under the standard `/events` envelope (Phase 4c) — not a drop-in replacement, different topic and payload shape.

### Workflows (Phase 9)

- [`dock-bootstrap-and-pairing.md`](../workflows/dock-bootstrap-and-pairing.md) — full participant, identical payloads to Dock 3.
- [`device-binding.md`](../workflows/device-binding.md), [`firmware-and-config-update.md`](../workflows/firmware-and-config-update.md) — full participant.
- [`wayline-upload-and-execution.md`](../workflows/wayline-upload-and-execution.md) — supports the full 21-method Phase 4b surface; does **not** support `in_flight_wayline_*` family (Dock 3 primary per Phase 4b).
- [`live-flight-controls-drc.md`](../workflows/live-flight-controls-drc.md) — DRC participant; note the 6 Dock-2-only DRC services above, absent the 28 Dock-3-only services.
- [`livestream-start-stop.md`](../workflows/livestream-start-stop.md) — **all four protocols supported** including Agora (`url_type: 0`). See §3 below.
- [`hms-event-reporting.md`](../workflows/hms-event-reporting.md) — full participant; copy key `dock_tip_{code}` for Dock-tier alarms.
- [`flysafe-custom-flight-area-sync.md`](../workflows/flysafe-custom-flight-area-sync.md), [`media-upload-from-dock.md`](../workflows/media-upload-from-dock.md) — full participant.

### Livestream protocols (Phase 7)

| Protocol | `url_type` | Supported |
|---|---|---|
| Agora | `0` | ✓ — unique to Dock 2 among docks. See [`../livestream-protocols/agora.md`](../livestream-protocols/agora.md). |
| RTMP | `1` | ✓ |
| GB28181 | `3` | ✓ |
| WebRTC (WHIP) | `4` | ✓ |

Dock 2 is the only dock that preserves Agora support. Cloud implementations targeting Dock 2 must be prepared to host an Agora channel (App ID + App Certificate) or gracefully refuse `url_type: 0` with a user-visible error — Dock 2 will emit it if the cloud serves an Agora URL in response to `live_start_push`.

### HMS + error codes (Phase 8)

Dock 2 emits the full HMS catalog (1,769 alarms in [`../hms-codes/`](../hms-codes/README.md)) — no Dock-2-specific prefix; the catalog is airframe-keyed, not dock-keyed. Copy-key splicing uses `dock_tip_{code}` for alarms routed to dock-tier UI (per [`hms-event-reporting.md`](../workflows/hms-event-reporting.md)).

General API error codes (Phase 8) — Dock 2 participates across all 20 BC modules. No Dock 2-specific error-code exclusions.

---

## 2. Cohort asymmetries (Dock 2 vs Dock 3)

Captured in detail in [`../device-properties/dock2.md`](../device-properties/dock2.md) §5 and [`../device-properties/dock3.md`](../device-properties/dock3.md) §5. Summary:

| Area | Dock 2 | Dock 3 |
|---|---|---|
| Top-level properties | 48 | 49 (adds `self_converge_coordinate`) |
| `home_position_is_valid` enum | 2-value `{0 Invalid, 1 Valid}` | 4-value (adds partial-state codes `2, 3`) |
| `mode_code` enum max | `5` | `5` — Dock 3 aligns with Dock 2 v1.15 |
| `network_state.quality` enum | duplicates `"1"/"2"` label `"Poor"` (source defect) | fixed 6-value `{No signal, Very Poor, Poor, Fair, Good, Excellent}` |
| Carrier labels in `dongle_infos.»esim_infos.telecom_operator` | short form (`"Mobile"`, `"Telecommunications"`) | fully qualified (`"China Mobile"`, `"China Telecom"`) |
| `flighttask_step_code` value `255` label | Chinese leftover (`"飞行器异常"`) in source extract | English (`"Aircraft Error"`) |
| `wireless_link.4g_link_state` / `sdr_link_state` labels | Chinese leftovers in source extract (`"断开"` / `"连接"`) | English (`"Disconnected"` / `"Connected"`) |
| `rtk_calibration` event (Phase 4e-1) | absent | present |
| DRC camera mode / storage / zoom-linkage / interval-photo services (Phase 4e-2) | present (6 services) | absent |
| Dock-3-only AI identify / spotlight / PSDK / speaker / light DRC services | absent | present (28 services) |
| Agora livestream (`url_type: 0`) | supported | dropped |

---

## 3. Implementation gotchas

Carry from Phase 6a [`../device-properties/dock2.md`](../device-properties/dock2.md) §4:

1. **Chinese labels in the v1.15 source extract** for `wireless_link.4g_link_state` / `sdr_link_state` and `flighttask_step_code` value `255` are DJI source-extraction defects, not real protocol values. The **codes** (`0`, `1`, `255`) are authoritative; labels should be treated as per Dock 3's English equivalents.
2. **`network_state.quality` duplicate `"Poor"` labels** for codes `1` and `2` are a Dock 2 source defect. Parse by code; treat codes `1` and `2` as distinct quality levels (Dock 3 resolves them to `"Very Poor"` and `"Poor"` respectively).
3. **`air_conditioner.air_conditioner_state` malformed enum values `10`–`15`** in the v1.15 source extract are extraction-tool defects (missing delimiters). Authoritative range is `0`–`9`. Same defect on Dock 3.
4. **Agora URLs use `+` characters in OAuth-style tokens** — URL-encode once, not twice. Cross-cited in the [livestream workflow](../workflows/livestream-start-stop.md) error paths. Dock 2 emits Agora URLs verbatim; cloud parsers must match.
5. **Source inconsistency ratio higher on Dock 2 than Dock 3** — the Dock 2 doc flags 6 DJI-source inconsistencies where Dock 3 flags 5, and most Dock 2 inconsistencies are label-level defects that Dock 3 silently fixes. Implementations targeting both docks should parse by code, never by label.

Phase 4 method-level gotchas:

6. **DRC camera aperture labels differ between Dock 2 and Dock 3** in `drc_camera_aperture_value_set` ([shared-DRC service](../mqtt/dock-to-cloud/drc/drc_camera_aperture_value_set.md)): Dock 2 uses dot separators (`"F2.2"`, `"F2.8"`); Dock 3 uses underscores (`"F2_2"`, `"F2_8"`). Same F-stop values, different string forms. Cloud implementations must branch on dock model.
7. **`fileupload_list` timestamp-unit label bug** — v1.11 + Dock 2 v1.15 source label `start_time` / `end_time` as `"Seconds / s"`; Dock 3 v1.15 correctly labels them `"Milliseconds / ms"`. Example values are epoch-ms in all sources. [OQ-004 resolution](../OPEN-QUESTIONS.md#oq-004--fileupload_list-log-window-timestamp-unit-is-inconsistent-across-dji-sources): treat as milliseconds on both docks.

---

## 4. Features this device lacks

- No `self_converge_coordinate` property.
- No Dock-3-only AI / PSDK / speaker / light / IR-night DRC services (28 methods, see Phase 4e-2 enumeration).
- No `rtk_calibration` event.
- No PSDK speaker / widget events (Phase 4g) under standard `/events` envelope — the Phase 4e-2 `drc_*` `/drc/up` forms are the closest analogues.
- No `in_flight_wayline_*` choreography — those are primary on Dock 3.
- No on-aircraft `commander_flight_height` writable surface via Dock 2 gateway (pilot-path M4D only carries the pilot-path writable; Dock 2 pairs with M3D which has only dock-path `commander_flight_height`).

---

## 5. Cross-reference map

| Phase | Doc | What's covered |
|---|---|---|
| 3 HTTP | [`../http/README.md`](../http/README.md) | 16 endpoints — Dock 2 participates in all 16 (shared endpoint surface with Dock 3). |
| 4 MQTT | [`../mqtt/dock-to-cloud/README.md`](../mqtt/dock-to-cloud/README.md) | 197 methods. Dock 2-only subset: 6 DRC services in Phase 4e-2; absent Phase 4e-1 `rtk_calibration` + 28 Dock-3-only DRC services + 12 Phase 4g PSDK methods. |
| 5 WebSocket | [`../websocket/README.md`](../websocket/README.md) | Pilot-to-cloud only; Dock 2 does not participate. |
| 6 Properties | [`../device-properties/dock2.md`](../device-properties/dock2.md) | 48 top-level properties + v1.11 → v1.15 drift. |
| 7 WPML + livestream | [`../livestream-protocols/README.md`](../livestream-protocols/README.md) | Agora / RTMP / GB28181 / WebRTC — all supported. No WPML device-specific relevance; wayline choice is per-aircraft not per-dock. |
| 8 Codes | [`../hms-codes/README.md`](../hms-codes/README.md), [`../error-codes/README.md`](../error-codes/README.md) | Full catalog. |
| 9 Workflows | [`../workflows/README.md`](../workflows/README.md) | Full participant in all 11 workflows except any Dock-3-exclusive branches noted in §1 above. |

## 6. Source provenance

| File | Role |
|---|---|
| [`DJI_Cloud/DJI_CloudAPI-Dock2-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock2-Properties.txt) | v1.15 property primary. |
| [`DJI_Cloud/DJI_CloudAPI-Dock2-*.txt`](../../DJI_Cloud/) (Wayline, Live-Flight-Controls, Remote-Control, Remote-Log, Remote-Debugging, etc.) | v1.15 per-feature extracts. |
| [`Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/`](../../Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/) | v1.11 canonical — drift cross-check only. |
| [`Cloud-API-Doc/docs/en/30.feature-set/20.dock-feature-set/`](../../Cloud-API-Doc/docs/en/30.feature-set/20.dock-feature-set/) | v1.11 choreography narrative — cited by Phase 9 workflows. No v1.15 equivalent. |
