# Device Annex — DJI RC Pro Enterprise

**Cohort**: Dock 2 cohort RC — pairs with M3D / M3TD.
**Gateway role**: RC gateway. RC serial is `{gateway_sn}` on pilot-to-cloud topics; `{device_sn}` for the RC's own property topics.
**Primary sources**: [`DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt) (v1.15, 68 lines) + `DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-*.txt` family (Remote-Control, Live-Stream, etc.) + [`Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/`](../../Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/) (v1.11 canonical, drift-only).

---

## 1. Distinctive wire surface

RC Pro Enterprise is the **older-generation RC** in the Dock 2 cohort. Its defining wire behaviour is that it uses **dock-canonical non-prefixed methods** on the standard `/services` topic instead of the RC-Plus-2 `drc_*`-prefixed DRC methods on `/drc/down`. This makes RC Pro's pilot-path surface smaller and more alike to the dock-path than RC Plus 2's.

### Property surface (Phase 6c)

- **11 top-level properties** (6 OSD + 5 state) — same top-level count as RC Plus 2 but non-overlapping at two keys. See [`../device-properties/rc-pro.md`](../device-properties/rc-pro.md).
- **0 writable** at the RC gateway level. `property/set` traffic routes to paired M3D / M3TD writable keys (baseline-only; no M3-series-specific extensions on pilot-path).
- **`country` OSD property** — **RC Pro only** among in-scope RCs. Country-area-code text string.
- **No `drc_state`** — RC Plus 2 has this; RC Pro observes DRC link state via Phase 4h services events instead.
- **`live_status.»video_quality` enum is 5-value** (`{0: Adaptive, 1: Smooth, 2: Standard, 3: High, 4: Ultra-high}`) — incompatible with RC Plus 2's 4-value enum.
- **v1.11 → v1.15 drift** — v1.11 canonical carries 10 top-level properties; v1.15 adds `cloud_control_auth` (state property). No other drift.
- **`DJI_CloudAPI_RC-Properties.txt` is byte-equivalent** to the RC Pro Enterprise file — the plain-RC sibling is out-of-scope but the file content is identical. Cloud implementations should treat the two SKU identities by `domain-type-subtype` model key, not by property catalog.

### MQTT methods — Pilot-to-Cloud (Phase 4h)

RC Pro participates in **a narrower subset** of the 94-method pilot-to-cloud surface. The distinctive surface:

- **23 non-prefixed camera / IR / gimbal services** (**RC Pro only** among RCs) on the standard `/services` topic — `camera_mode_switch`, `camera_recording_start/stop`, `camera_screen_drag`, `camera_aim`, `camera_focal_length_set`, `gimbal_reset`, `camera_look_at`, `camera_screen_split`, `photo_storage_set`, `video_storage_set`, `camera_frame_zoom`, `ir_metering_area_set`, `ir_metering_point_set`, `ir_metering_mode_set`, `camera_point_focus_action`, `camera_focus_value_set`, `camera_focus_mode_set`, `camera_exposure_set`, `camera_exposure_mode_set`, `camera_photo_stop`, `camera_photo_take`. Full list in [`../mqtt/pilot-to-cloud/README.md`](../mqtt/pilot-to-cloud/README.md) §"services/ — parallels of dock-to-cloud services." All cross-refer to the dock-to-cloud docs under [`../mqtt/dock-to-cloud/services/`](../mqtt/dock-to-cloud/services/) — shared schema.
- **2 NEW services** (shared with RC Plus 2): `cloud_control_auth_request`, `cloud_control_release`.
- **1 NEW event** (shared with RC Plus 2): `cloud_control_auth_notify`.
- **2 event parallels**: `drc_status_notify`, `camera_photo_take_progress`.
- **2 DRC services** (shared with RC Plus 2): `drc_mode_enter`, `drc_mode_exit`.
- **3 DRC parallels on `/drc/up`** (shared with RC Plus 2): `heart_beat`, `osd_info_push`, `hsi_info_push`, `delay_info_push`, `drc_drone_state_push`, `drc_camera_osd_info_push`, `drc_initial_state_subscribe`.
- **Live streaming** — `live_start_push`, `live_stop_push`, `live_set_quality`, `live_lens_change` (non-DRC form).

### What RC Pro does **not** participate in

- No `stick_control` / `drone_emergency_stop` DRC — RC Plus 2 only.
- No POI services / event — RC Plus 2 only.
- No `drc_*`-prefixed camera / IR / gimbal variants on `/drc/down` — RC Pro uses non-prefixed services instead.
- No `fly_to_point` / `takeoff_to_point` / `return_home_*` / `fly_to_point_stop` / `fly_to_point_update` pilot-path services — RC Plus 2 only.
- No `drc_camera_state_push` / `drc_camera_photo_info_push` — RC Plus 2 only. Photo-progress observed via `camera_photo_take_progress` standard event.
- No `fly_to_point_progress` / `takeoff_to_point_progress` / `joystick_invalid_notify` / `return_home_info` events — RC Plus 2 only.
- No `drc_emergency_landing` / `drc_force_landing` — RC Plus 2 only.
- No 10+ drc_* camera-attitude setters (dewarping, aperture, ISO, shutter, etc.) — RC Plus 2 only.

### Workflows (Phase 9)

RC Pro participates in most workflows as the pilot-path gateway for M3D / M3TD. Specific branches:

- [`remote-control-handoff.md`](../workflows/remote-control-handoff.md) — same Phase 4h consent flow as RC Plus 2: `cloud_control_auth_request` → pop-up → `cloud_control_auth_notify`. But RC Pro lacks the `drc_state` OSD companion — cloud observes DRC session health by tracking the `cloud_control_auth` state property (added in v1.15) + heartbeat / events.
- [`live-flight-controls-drc.md`](../workflows/live-flight-controls-drc.md) — DRC session via `drc_mode_enter` / `drc_mode_exit`. Camera / IR / gimbal control uses dock-canonical non-prefixed methods on `/services`. No pilot-side sticks — cloud-initiated flight commands must route through Dock-path `fly_to_point` via Dock 2 (not a pilot-path service on RC Pro).
- [`livestream-start-stop.md`](../workflows/livestream-start-stop.md) — 3-protocol support (no WebRTC).

### Livestream protocols (Phase 7)

| Protocol | `url_type` | Supported |
|---|---|---|
| Agora | `0` | ✓ |
| RTMP | `1` | ✓ |
| GB28181 | `3` | ✓ |
| WebRTC (WHIP) | `4` | — (dropped) |

**RC Pro is the only in-scope gateway that drops WebRTC.** Cloud implementations serving WHIP streams must not route them through the RC Pro pilot-path.

### HMS + error codes (Phase 8)

Same as RC Plus 2 — HMS is airframe-keyed (M3D / M3TD), relayed through the RC. Copy-key splicing uses `fpv_tip_{code}[_in_the_sky]`.

---

## 2. Cohort asymmetries

See the RC Plus 2 annex ([`rc-plus-2.md`](rc-plus-2.md) §2) for the side-by-side cohort comparison. Summary in RC Pro perspective:

- **Smaller pilot-path method surface** — RC Pro uses non-prefixed services (dock-canonical) for camera / IR / gimbal; RC Plus 2 uses DRC-prefixed methods on `/drc/down`.
- **No POI, no pilot-stick, no pilot-initiated FlyTo, no pilot-initiated return-home**. All pilot-initiated missions on this cohort must go through dock-path (Dock 2) services.
- **`country` unique to RC Pro**; `drc_state` unique to RC Plus 2.

---

## 3. Implementation gotchas

Carry from Phase 6c [`../device-properties/rc-pro.md`](../device-properties/rc-pro.md) §4:

1. **`wireless_link.»dongle_number` description is copy-pasted from aircraft-side** — cosmetic source defect; the field is functionally the RC-side link state.
2. **`wireless_link.»link_workmode` labelled "Dock's video transmission link mode"** — same defect; functionally the RC's link mode.
3. **`DJI_CloudAPI_RC-Properties.txt` (plain-RC, out-of-scope) is byte-equivalent** to the RC Pro Enterprise property file. Identify the actual SKU via `domain-type-subtype` model key; do not rely on property-catalog contents for SKU disambiguation.
4. **`live_status.»video_quality` enum incompatibility with RC Plus 2.** Parse by code; branch on cohort.
5. **DRC session health on RC Pro** — no `drc_state` OSD property. Cloud implementations must derive session health from `cloud_control_auth` state + DRC heartbeat + `drc_status_notify` event (v1.15 abandons `drc_status_notify` per the Phase 4h README note; use the `cloud_control_auth` state property as the current indicator).
6. **`cloud_control_auth` state property is v1.15 addition.** v1.11 RC Pro canonical carries only 10 top-level properties; implementations sourced from v1.11 documentation will lack this key. Update against v1.15.
7. **`cloud_control_auth_notify` reply envelope quirk (`need_reply: 0`, atypical for Phase 4h events).** Cross-cited in [`remote-control-handoff.md`](../workflows/remote-control-handoff.md).

Phase 4 gotchas:

8. **Wording drift between RC Pro and RC Plus 2 source files on `cloud_control_auth_request`.** Same method, different prose. Documented in [OQ-002](../OPEN-QUESTIONS.md#oq-002--pilot-to-cloud-osd-struct-example-appears-to-be-a-copy-paste-of-the-dock-osd-example) context (pilot-source cleanup).
9. **Undocumented `output.status` in the `cloud_control_auth_request` services_reply example.** DJI's example ships `{result: 0, output: {status: "ok"}}` but the schema table doesn't declare `output.status`. Treat `result` as authoritative; tolerate `output.status`. Cross-cited in [`remote-control-handoff.md`](../workflows/remote-control-handoff.md).

---

## 4. Features this device lacks

- No WebRTC livestream (`url_type: 4` dropped).
- No `drc_state` OSD property.
- No POI mode services or event.
- No `stick_control` / `drone_emergency_stop` DRC methods.
- No `fly_to_point_*` / `takeoff_to_point` / `return_home_*` pilot-path services — must use dock-path via Dock 2.
- No `drc_*`-prefixed camera / IR / gimbal variants on `/drc/down` — uses non-prefixed services instead.
- No DRC 2.0 `commander_flight_height` pilot-path writable (paired aircraft M3D has no M4D-style pilot-path extensions).
- No gateway-level writable keys.

---

## 5. Cross-reference map

| Phase | Doc | What's covered |
|---|---|---|
| 3 HTTP | [`../http/README.md`](../http/README.md) | 16 endpoints — wayline / media traffic from RC Pro uses the same endpoints as Dock 2. |
| 4 MQTT | [`../mqtt/pilot-to-cloud/README.md`](../mqtt/pilot-to-cloud/README.md) | ~50 methods RC Pro participates in (subset of the 94-method catalog; see §1 for inclusions and exclusions). |
| 5 WebSocket | [`../websocket/README.md`](../websocket/README.md) | RC Pro + paired M3D / M3TD telemetry on situation-awareness push messages. |
| 6 Properties | [`../device-properties/rc-pro.md`](../device-properties/rc-pro.md) | 11 top-level properties + v1.11 → v1.15 drift (adds `cloud_control_auth`). |
| 7 WPML + livestream | [`../livestream-protocols/README.md`](../livestream-protocols/README.md) | Agora / RTMP / GB28181; no WebRTC. |
| 8 Codes | [`../hms-codes/README.md`](../hms-codes/README.md) | Aircraft-keyed; RC relays only. |
| 9 Workflows | [`../workflows/README.md`](../workflows/README.md) | Pilot-path participant; see [`remote-control-handoff.md`](../workflows/remote-control-handoff.md) + [`live-flight-controls-drc.md`](../workflows/live-flight-controls-drc.md). |

## 6. Source provenance

| File | Role |
|---|---|
| [`DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt) | v1.15 property primary (68 lines). |
| [`DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-*.txt`](../../DJI_Cloud/) (Remote-Control, Live-Stream, etc.) | v1.15 per-feature extracts. |
| [`Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/00.properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/00.properties.md) | v1.11 drift cross-check (10 top-level properties; v1.15 adds `cloud_control_auth`). |
| [`DJI_Cloud/DJI_CloudAPI_RC-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Properties.txt) | Out-of-scope plain-RC sibling (byte-equivalent content). |
| [`../device-properties/_aircraft-pilot-base.md`](../device-properties/_aircraft-pilot-base.md) | Paired-aircraft pilot-path baseline (inherited by M3D / M3TD). |
| [`../device-properties/m3d.md`](../device-properties/m3d.md) | Paired-aircraft full catalog. |
