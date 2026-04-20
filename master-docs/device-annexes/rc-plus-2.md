# Device Annex — DJI RC Plus 2 Enterprise

**Cohort**: Dock 3 cohort RC — pairs with M4D / M4TD.
**Gateway role**: RC gateway. RC serial is `{gateway_sn}` on pilot-to-cloud topics; `{device_sn}` for the RC's own property topics. Aircraft telemetry when the RC is the gateway uses the aircraft's SN as `{device_sn}`.
**Primary sources**: [`DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt) (v1.15, 625 lines) + `DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-*.txt` family (Remote-Control, Live-Stream, etc., all v1.15). No v1.11 counterpart — RC Plus 2 Enterprise postdates v1.11.3.

---

## 1. Distinctive wire surface

RC Plus 2 Enterprise is the **current-generation RC** in the Dock 3 cohort. It is the **only in-scope RC that runs DJI Pilot 2 over the new DRC-prefixed pilot-to-cloud surface** — every camera / gimbal / IR-metering / stick-control command routes through `/drc/down` with `drc_*` method names, delivered on the lightweight DRC envelope instead of the standard services topic. RC Pro, by contrast, uses dock-canonical non-prefixed methods on `/services`. This is the defining cohort split within Phase 4h.

### Property surface (Phase 6c)

- **11 top-level properties** (6 OSD + 5 state). See [`../device-properties/rc-plus-2.md`](../device-properties/rc-plus-2.md).
- **0 writable** at the RC gateway level. The `thing/product/{rc_sn}/property/set` topic is used exclusively to route writes to the paired aircraft's writable properties (M4D's 3 pilot-path-writable `commander_*` keys + baseline `height_limit` / `night_lights_state` / `camera_watermark_settings`).
- **`drc_state` OSD property** — **RC Plus 2 only** among in-scope RCs. Publishes DRC link state (`{0: Not connected, 1: Connecting, 2: Connected}`) at ~0.5 Hz. RC Pro does not carry this; cloud observes DRC state on RC Pro via Phase 4h services instead.
- **No `country` property** — present on RC Pro; absent from RC Plus 2.
- **`live_status.»video_quality` enum is 4-value** (`{0: Auto, 1: Smooth, 2: HD, 3: Ultra HD}`) — incompatible with RC Pro's 5-value enum. Cloud implementations must branch on RC cohort when mapping quality.

### MQTT methods — Pilot-to-Cloud (Phase 4h)

RC Plus 2 participates in **93 of the 94 pilot-to-cloud methods** (every method except the RC-Pro-only non-prefixed camera / IR / gimbal services). The distinctive surface:

- **20 pilot-specific `drc_*` variants** on `/drc/down` (RC Plus 2 only in pilot-path) — camera (photo/record/exposure/focus/zoom), gimbal reset, IR metering point/area/mode, live-lens change. Full list in [`../mqtt/pilot-to-cloud/README.md`](../mqtt/pilot-to-cloud/README.md) §"drc/ — new to pilot-to-cloud." The dock-to-cloud parallels are the non-prefixed `camera_*` / `ir_metering_*` services under [`../mqtt/dock-to-cloud/services/`](../mqtt/dock-to-cloud/services/) — payload shapes match.
- **5 NEW services** introduced by pilot-path (RC Plus 2 only among RCs for POI + unified with RC Pro for authority):
  - `cloud_control_auth_request`, `cloud_control_release` — shared with RC Pro.
  - `poi_mode_enter`, `poi_mode_exit`, `poi_circle_speed_set` — **RC Plus 2 only**.
- **2 NEW events**:
  - `cloud_control_auth_notify` — shared with RC Pro.
  - `poi_status_notify` — **RC Plus 2 only**.
- **6 event parallels** of dock-to-cloud: `fly_to_point_progress`, `takeoff_to_point_progress`, `drc_status_notify`, `joystick_invalid_notify`, `camera_photo_take_progress`, `return_home_info`. Most RC-Plus-2-only (RC Pro participates in `drc_status_notify` + `camera_photo_take_progress`).
- **7 service parallels** of dock-to-cloud: `drc_mode_enter`, `drc_mode_exit`, `takeoff_to_point`, `fly_to_point`, `fly_to_point_stop`, `fly_to_point_update`, `return_home`, `return_home_cancel` — all RC-Plus-2-only except the mode-enter / exit pair (shared with RC Pro).
- **`live_lens_change` variants differ by cohort** — RC Plus 2 uses the DRC-prefixed [`drc/drc_live_lens_change.md`](../mqtt/pilot-to-cloud/drc/drc_live_lens_change.md) on `/drc/down`; RC Pro uses the non-prefixed services form on `/services`.
- **Live streaming** — `live_start_push`, `live_stop_push`, `live_set_quality` shared with RC Pro.
- **DRC parallels on `/drc/up`** — RC Plus 2 emits `drc_drone_state_push`, `drc_camera_state_push`, `drc_camera_photo_info_push` (note: `drc_camera_photo_info_push` is shared with Dock 2 and RC Plus 2, not RC Pro), plus 10 camera-attitude DRC setters (`drc_camera_dewarping_set`, `drc_camera_aperture_value_set`, `drc_camera_iso_set`, `drc_camera_shutter_set`, `drc_camera_mechanical_shutter_set`, `drc_stealth_state_set`, `drc_night_lights_state_set`, `drc_camera_mode_switch`, `drc_interval_photo_set`, `drc_photo_storage_set`, `drc_video_storage_set`, `drc_video_resolution_set`, `drc_linkage_zoom_set`) and emergency controls (`drc_emergency_landing`, `drc_force_landing`, `stick_control`, `drone_emergency_stop`). `stick_control` + `drone_emergency_stop` are **RC Plus 2 only** among RCs.

### Workflows (Phase 9)

All 11 workflows participate. RC Plus 2-specific branches:

- [`remote-control-handoff.md`](../workflows/remote-control-handoff.md) — M4D pilot-path consent flow. Cloud issues `cloud_control_auth_request` on `thing/product/{rc_plus_2_sn}/services`; pilot consents via RC UI; `cloud_control_auth_notify` event carries pilot response (`ok` / `failed` / `canceled`); `cloud_control_auth` state property (array form) flips to indicate the session is live. RC Plus 2 also emits `drc_state` OSD at the same time, showing the DRC link state explicitly. Handoff-back is user-initiated; `cloud_control_release` or pilot grab-back.
- [`live-flight-controls-drc.md`](../workflows/live-flight-controls-drc.md) — RC Plus 2 is the pilot-path DRC gateway for M4D. Phase 4h 20 pilot-specific DRC variants are exercised here. Camera / gimbal / IR commands flow RC-side over `/drc/down` rather than the dock-path `/services`.
- [`livestream-start-stop.md`](../workflows/livestream-start-stop.md) — full 4-protocol support (only gateway in the corpus with all 4).

### Livestream protocols (Phase 7)

| Protocol | `url_type` | Supported |
|---|---|---|
| Agora | `0` | ✓ |
| RTMP | `1` | ✓ |
| GB28181 | `3` | ✓ |
| WebRTC (WHIP) | `4` | ✓ |

**RC Plus 2 is the only gateway that supports all 4 livestream protocols.** Dock 3 drops Agora; Dock 2 has all 4; RC Pro drops WebRTC.

### HMS + error codes (Phase 8)

RC Plus 2 does **not** emit HMS alarms itself — HMS is airframe-keyed, published by the aircraft (M4D / M4TD) when the RC is the gateway. The RC relays the aircraft-origin `hms` event unchanged. Copy-key splicing uses `fpv_tip_{code}[_in_the_sky]` for aircraft-tier UI.

---

## 2. Cohort asymmetries

**vs RC Pro** (older-generation RC) — captured in [`../device-properties/rc-plus-2.md`](../device-properties/rc-plus-2.md) §5 + [`../device-properties/rc-pro.md`](../device-properties/rc-pro.md) §5:

| Area | RC Plus 2 | RC Pro |
|---|---|---|
| `drc_state` OSD property | ✓ | absent |
| `country` OSD property | absent | ✓ |
| `live_status.»video_quality` enum | 4-value `{Auto, Smooth, HD, Ultra HD}` | 5-value `{Adaptive, Smooth, Standard, High, Ultra-high}` |
| Pilot-path DRC channel | `drc_*` prefixed on `/drc/down` | dock-canonical non-prefixed on `/services` |
| `stick_control` + `drone_emergency_stop` DRC | ✓ | absent |
| POI services + event (`poi_mode_enter/exit/speed_set/status_notify`) | ✓ | absent |
| `fly_to_point`, `takeoff_to_point`, `return_home_*` services | ✓ | absent |
| WebRTC livestream support | ✓ | — |
| 20 drc_* camera / IR / gimbal variants | ✓ | absent (uses non-DRC services instead) |
| Paired aircraft | M4D / M4TD | M3D / M3TD |

RC Plus 2 has a **substantially richer pilot-path surface** than RC Pro — the combination of DRC 2.0 commander writes + POI mode + pilot-stick-control + full DRC camera/gimbal/IR surface is Plus-2-only. Cloud implementations that want to support both RCs must either implement two separate pilot-path stacks or abstract over the method-name differences.

---

## 3. Implementation gotchas

Carry from Phase 6c [`../device-properties/rc-plus-2.md`](../device-properties/rc-plus-2.md) §4:

1. **Source copy-paste from aircraft-side wording** — `wireless_link.»dongle_number` is described as "Number of dongles on the aircraft" (RC doesn't host the aircraft's dongle). `wireless_link.»link_workmode` is labelled "Dock's video transmission link mode" in source. These are cosmetic description defects; fields are functionally the RC-side wireless-link state.
2. **`property/set` on RC Plus 2 has no RC-owned writable keys.** Cloud writes on this topic always target the paired aircraft's writable surface — the RC is just the routing gateway.
3. **`live_status.»video_quality` enum incompatibility between RC Plus 2 and RC Pro** — do not share a single quality-mapping table across the two cohorts. Parse by code and branch on cohort.
4. **`drc_state` OSD is the RC Plus 2 indicator for DRC session health** — RC Pro does not carry this; cloud implementations targeting both must use Phase 4h services events as the fallback indicator on RC Pro.
5. **RC Plus 2 uses `/drc/down` DRC envelope (lightweight: `method` + `seq` + `data`, no `tid`/`bid`/`timestamp`)** for all camera/gimbal/IR commands. Cloud implementations must build a DRC-specific publisher in addition to the standard services publisher — the envelope is not interchangeable.
6. **DRC 2.0 commander writes target the aircraft SN, not the RC SN.** `commander_flight_height` `property/set` publishes to `thing/product/{m4d_sn}/property/set` — the RC is the gateway in the topology sense but not the target of the write. Standard envelope (not `/drc/down`) for this write, unlike the camera commands.

Phase 4 gotchas:

7. **`drc_camera_photo_info_push` exists on RC Plus 2 but not on RC Pro.** RC Pro inherits the Dock-2-pattern `drc_camera_photo_info_push` on `/drc/up` from the dock path, but the **pilot-to-cloud surface for RC Pro does not carry this method** — cloud implementations observing photo-take progress on RC Pro must use `camera_photo_take_progress` event instead.

---

## 4. Features this device lacks

- No `country` OSD property (RC Pro has).
- No HMS emission (aircraft-keyed, relays only).
- No gateway-level writable keys.
- No dock-path participation (pilot-path only).
- No dock-canonical non-DRC camera services — uses `drc_*` DRC-prefixed forms instead.

---

## 5. Cross-reference map

| Phase | Doc | What's covered |
|---|---|---|
| 3 HTTP | [`../http/README.md`](../http/README.md) | 16 endpoints — wayline / media traffic from RC Plus 2 uses the same endpoints as Dock 3. |
| 4 MQTT | [`../mqtt/pilot-to-cloud/README.md`](../mqtt/pilot-to-cloud/README.md) | 93 methods (27 pilot-specific + 64 dock-parallel; 1 method — `live_lens_change` non-DRC — is RC-Pro-only). |
| 5 WebSocket | [`../websocket/README.md`](../websocket/README.md) | RC Plus 2 + paired M4D telemetry surfaces on situation-awareness push messages. |
| 6 Properties | [`../device-properties/rc-plus-2.md`](../device-properties/rc-plus-2.md) | 11 top-level properties, 0 writable. |
| 7 WPML + livestream | [`../livestream-protocols/README.md`](../livestream-protocols/README.md) | All 4 protocols supported. |
| 8 Codes | [`../hms-codes/README.md`](../hms-codes/README.md) | Aircraft-keyed; RC relays only. |
| 9 Workflows | [`../workflows/README.md`](../workflows/README.md) | Full pilot-path participant; see [`remote-control-handoff.md`](../workflows/remote-control-handoff.md) + [`live-flight-controls-drc.md`](../workflows/live-flight-controls-drc.md) in particular. |

## 6. Source provenance

| File | Role |
|---|---|
| [`DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt) | v1.15 property primary (625 lines). |
| [`DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-*.txt`](../../DJI_Cloud/) (Remote-Control, Live-Stream, etc.) | v1.15 per-feature extracts. |
| [`../device-properties/_aircraft-pilot-base.md`](../device-properties/_aircraft-pilot-base.md) | Paired-aircraft pilot-path baseline (inherited by M4D / M4TD). |
| [`../device-properties/m4d.md`](../device-properties/m4d.md) | Paired-aircraft full catalog. |

No v1.11 canonical counterpart.
