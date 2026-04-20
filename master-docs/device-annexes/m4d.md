# Device Annex — DJI Matrice 4D (M4D)

**Cohort**: Dock 3 / M4-series cohort — M4D + M4TD + Dock 3 + RC Plus 2 Enterprise.
**Gateway role**: aircraft sub-device. Dock 3 (dock-path) or RC Plus 2 Enterprise (pilot-path).
**Primary sources**: [`DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt`](../../DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt) (v1.15 dock-path; M4D + M4TD co-documented) + [`DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt) (v1.15 pilot-path delta) + [`../device-properties/_aircraft-pilot-base.md`](../device-properties/_aircraft-pilot-base.md).

---

## 1. Distinctive wire surface

M4D is the **current-generation aircraft in the Dock 3 cohort**. Its defining wire feature is **pilot-path asymmetry** with M3D — where M3D pilot-path uses the generic baseline verbatim, M4D pilot-path extends the baseline with 7 M4D-specific writable + read-only keys enabling DRC 2.0 elevation-aware FlyTo missions, offline-map sync, and RTH-mode control directly from the pilot-held cloud session. M4D also brings the PSDK payload surface (megaphone + searchlight) into the WPML action catalog.

### Property surface (Phase 6b)

- **Dock-path** (via Dock 3 gateway): **42 top-level properties** — catalog shape is identical to M3D dock-path with two cohort-specific deltas (see §2). See [`../device-properties/m4d.md`](../device-properties/m4d.md) §A.
- **Pilot-path** (via RC Plus 2 gateway): generic aircraft baseline **plus 7 M4D-specific extensions** (listed below) — total 49 top-level properties.
- **Dock-path writables** (same 6 as M3D): `obstacle_avoidance`, `height_limit`, `night_lights_state`, `camera_watermark_settings`, `commander_flight_height`, `commander_flight_mode`, `commander_mode_lost_action`, `rth_altitude`, `distance_limit_status`, `remaining_power_for_return_home`.
- **Pilot-path writables** — M4D adds 3 **pilot-path-writable** commander keys that are **rw on pilot path only**:
  - `commander_flight_height` — FlyTo altitude, `float ∈ [2, 3000]` m, step `0.1`, relative to takeoff point.
  - `commander_flight_mode` — FlyTo mode, `enum_int {0: Optimal height, 1: Preset height}`.
  - `commander_mode_lost_action` — FlyTo signal-lost action, `enum_int {0: Continue to-point, 1: Exit + normal LoC}`.
- **Pilot-path-only read keys** — `current_rth_mode`, `rth_mode`, `offline_map_enable`, `current_commander_flight_mode` (the read-back companion to `commander_flight_mode`).

The pilot-path extract is a **delta specification**, not a full catalog — it documents only the 7 extensions + 6 overrides beyond the baseline. Baseline properties (`country`, `mode_code_reason`, `cameras`, `position_state`, `storage`, `battery`, attitude trio, gear, watermark, etc.) are published by M4D on pilot-path per the baseline semantics.

### MQTT methods (Phase 4) — M4D-relevant surface

No M4D-specific MQTT methods exist at the aircraft level — Phase 4 catalogs are gateway-keyed. However, these method families are specifically exercised by M4D workflows:

- **Phase 4h `cloud_control_auth_request` / `cloud_control_auth_notify` / `cloud_control_release`** — consent-gated authority-grab via RC Plus 2 for M4D pilot-path DRC sessions. See [`../mqtt/pilot-to-cloud/`](../mqtt/pilot-to-cloud/README.md).
- **Phase 4h 20 pilot-path `drc_*` variants** — camera / gimbal / IR metering control. M4D is the paired aircraft; RC Plus 2 is the gateway.
- **Phase 4c `takeoff_to_point`, `fly_to_point`, `fly_to_point_stop`, `fly_to_point_update`** — Dock-3-surface commanders. M4D dock-path executes these via Dock 3.
- **In-flight wayline delivery** (Phase 4b `in_flight_wayline_*`) — Dock-3-primary; M4D on Dock 3 is the primary aircraft for this family.

### Workflows (Phase 9)

All 11 workflows apply. M4D-specific branches:

- [`wayline-upload-and-execution.md`](../workflows/wayline-upload-and-execution.md) — M4D supports `in_flight_wayline_*` mid-flight substitution (Dock 3 family).
- [`live-flight-controls-drc.md`](../workflows/live-flight-controls-drc.md) — DRC 2.0 `commander_flight_height` writable on M4D pilot-path. Cloud-issued FlyTo missions land the altitude as a `property/set` write against the M4D SN, with the RC Plus 2 routing the write to the aircraft. The dock-path path has the same writable key on the M4D but reaches it via Dock 3.
- [`livestream-start-stop.md`](../workflows/livestream-start-stop.md) — M4D gateway-determined protocol support:
  - Via Dock 3: RTMP / GB28181 / WebRTC (no Agora).
  - Via RC Plus 2: RTMP / GB28181 / WebRTC / Agora.
- [`airsense-events.md`](../workflows/airsense-events.md) — M4D is AirSense-equipped; emits `airsense_warning` via Dock 3.
- [`remote-control-handoff.md`](../workflows/remote-control-handoff.md) — paired with RC Plus 2 Enterprise per the Phase 4h consent flow.

### WPML (Phase 7) — M4D-unique actions

M4D and M4TD are the only in-scope aircraft that support the PSDK-payload-driven WPML actions:

- **`megaphone`** — pre-recorded audio playback from the KMZ archive. Parameters: payload position index, playback control, volume `[0, 100]`, loop enable, Opus codec, bitrate enum (currently only `32000` bps documented). See [`../wpml/common-elements.md`](../wpml/common-elements.md) §16.
- **`searchlight`** — attached searchlight control. See [`../wpml/common-elements.md`](../wpml/common-elements.md) §16.

Both actions depend on the PSDK megaphone / searchlight payloads being mounted. WPML wayline files using these actions will fail to execute on M3D / M3TD.

### Livestream (Phase 7)

As aircraft, M4D is a video source; transport is gateway-determined. Dock 3 drops Agora (so M4D via Dock 3 = no Agora); RC Plus 2 drops nothing. Cloud implementations that assume "M4D always Agora" will fail — Agora is reachable only via the RC Plus 2 pilot-path.

### HMS + error codes (Phase 8)

M4D participates across all applicable HMS prefixes (see M3D annex §1 — same prefix set). M4D-specific payloads (new Zenmuse generation for the M4 airframe) map to codes within the existing prefixes — the catalog is payload-classified, not airframe-classified.

---

## 2. Cohort asymmetries

**vs M3D** (older-generation sibling) — captured in [`../device-properties/m4d.md`](../device-properties/m4d.md) §A.1 + §5:

| Area | M3D | M4D |
|---|---|---|
| `mode_code` enum max | `20` | `21` (adds `"21": "during the inbound and outbound flight procedures"`) |
| `remaining_power_for_return_home` recommended range | 25–50% (Dock 2 text) | 15–50% (Dock 3 text) |
| `{type-subtype-gimbalindex}` schema-cell | clean | garbled (`{_{type-subtype-gimbalindex}__aembLbhPpc}` — DJI extraction artifact) |
| Pilot-path `commander_*` writables | absent | **3 keys rw via pilot-path** |
| Pilot-path `current_commander_flight_mode` read-back | absent | present |
| Pilot-path `offline_map_enable` | absent | present |
| Pilot-path `current_rth_mode` + `rth_mode` | absent | present |
| WPML `megaphone` + `searchlight` | unsupported | supported (if payload mounted) |
| `mode_code` pilot-path enum max | `18` | `19` — adds `"Dock site evaluation in progress"` |

M4D is **not a strict superset of M3D on pilot-path** — some pilot-path baseline properties are absent from the M4D delta extract (but still published per baseline semantics; see [`../device-properties/m4d.md`](../device-properties/m4d.md) §B.3 for the inheritance rule).

**vs M4TD** (same-cohort thermal variant) — property-level duplicate; see [`m4td.md`](m4td.md).

---

## 3. Implementation gotchas

Carry from Phase 6b [`../device-properties/m4d.md`](../device-properties/m4d.md) §4:

1. **Pilot-path extract is a delta, not a full catalog.** Cloud implementations must **not** treat "absent from M4D pilot-path extract" as "not published by M4D on pilot-path." The baseline fields (`country`, `cameras`, `position_state`, `storage`, `battery`, `wind_*`, `attitude_*`, etc.) are all published. This is the single biggest source of "I don't see field X" implementation bugs targeting M4D pilot-path.
2. **`{_{type-subtype-gimbalindex}__aembLbhPpc}` struct-name cell is garbled** in both the M4D dock-path and pilot-path extracts. Authoritative key is literal `{type-subtype-gimbalindex}`. Same field body; only the cell header is corrupted.
3. **`firmware_version` push-mode drift** — baseline ships as `state` (pushMode 1); M4D pilot-path ships as `osd` (pushMode 0). Cloud implementations should subscribe to both osd and state topics and accept either.
4. **`current_rth_mode` label drift** — M4D pilot-path labels `{0: Optimal, 1: Preset}`; M3D dock-path labels `{0: Intelligent altitude, 1: Preset altitude}`. Same codes; parse by code.
5. **`current_commander_flight_mode` exists only on pilot-path**, not dock-path. Cloud implementations that want to know the current FlyTo mode via Dock 3 must infer from the last-set `commander_flight_mode` value; there is no read-back companion on dock-path.
6. **`mode_code_reason` absent from M4D pilot-path extract** — inherit from baseline (enum stops at `"22"`). Dock-path adds value `"23"`; pilot-path does not.

Phase 4 / Phase 9 gotchas:

7. **`commander_flight_height` has overlap across paths.** M4D dock-path has the key (writable via Dock 3); M4D pilot-path has the key (writable via RC Plus 2). An operator + cloud-scheduler write race must be prevented — DJI does not specify which wins if both write simultaneously. Observed safe pattern: cloud scheduler holds authority via `flight_authority_grab` (Phase 4c) during dock-scheduled missions; pilot operates within pilot-session handoff boundaries.
8. **Agora unreachable via Dock 3.** M4D launching an Agora stream must do so via RC Plus 2 pilot-path. Cloud implementations that assume "M4D supports all protocols" will 404 on Dock-3-routed Agora.
9. **DRC 2.0 elevation-aware FlyTo is pilot-path-primary.** M4D pilot-path introduces the `commander_*` surface specifically for pilot-held cloud sessions. Dock-path has the keys but they serve dock-scheduled commander missions, not live DRC sessions. Cloud implementations should treat the two surfaces as distinct operational modes even though they share the schema.

---

## 4. Features this device lacks

- No Dock-2-only DRC services (via Dock 3 gateway only, and Dock 3 doesn't carry them either).
- No Dock-1 / M300 / M30 cohort methods (out of scope globally).
- No `»payload_index` values for legacy Zenmuse payloads that never officially paired with M4 (payload-level detail outside this annex).

---

## 5. Cross-reference map

| Phase | Doc | What's covered |
|---|---|---|
| 3 HTTP | [`../http/README.md`](../http/README.md) | 16 endpoints — M4D wayline / media traffic via Dock 3 or RC Plus 2. |
| 4 MQTT | [`../mqtt/dock-to-cloud/README.md`](../mqtt/dock-to-cloud/README.md), [`../mqtt/pilot-to-cloud/README.md`](../mqtt/pilot-to-cloud/README.md) | Dock-path via Dock 3 (197 methods); pilot-path via RC Plus 2 (94 methods incl. 27 new pilot-specific). |
| 5 WebSocket | [`../websocket/README.md`](../websocket/README.md) | M4D telemetry surfaces in 4 situation-awareness push messages when gateway is RC Plus 2. |
| 6 Properties | [`../device-properties/m4d.md`](../device-properties/m4d.md) | 42 dock-path + baseline + 7 M4D pilot-path extensions + `{type-subtype-gimbalindex}`. |
| 7 WPML + livestream | [`../wpml/common-elements.md`](../wpml/common-elements.md), [`../livestream-protocols/README.md`](../livestream-protocols/README.md) | M4D-unique `megaphone` + `searchlight` actions; gateway-determined livestream set. |
| 8 Codes | [`../hms-codes/README.md`](../hms-codes/README.md), [`../error-codes/README.md`](../error-codes/README.md) | Full catalog. |
| 9 Workflows | [`../workflows/README.md`](../workflows/README.md) | Full participant; Dock-3-cohort branches enabled. |

## 6. Source provenance

| File | Role |
|---|---|
| [`DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt`](../../DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt) | v1.15 dock-path primary (218 lines; M4D + M4TD co-documented). |
| [`DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt) | v1.15 pilot-path delta spec (117 lines). |
| [`../device-properties/_aircraft-pilot-base.md`](../device-properties/_aircraft-pilot-base.md) | Pilot-path baseline inherited by M4D. |
| [`../device-properties/m3d.md`](../device-properties/m3d.md) | Dock-path full catalog — M4D dock-path references this shape. |
| [`m4td.md`](m4td.md) | Thermal-variant annex. |

M4D post-dates v1.11.3; no v1.11 canonical counterpart exists. Source of truth is the v1.15 extracts above.
