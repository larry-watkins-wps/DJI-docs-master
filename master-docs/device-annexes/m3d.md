# Device Annex — DJI Matrice 3D (M3D)

**Cohort**: Dock 2 / M3-series cohort — M3D + M3TD + Dock 2 + RC Pro Enterprise.
**Gateway role**: aircraft sub-device. Published through two distinct gateway SNs depending on path — Dock 2 (dock-path) or RC Pro Enterprise (pilot-path).
**Primary sources**: [`DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt) (v1.15, dock-path + M3TD co-documented) + [`_aircraft-pilot-base.md`](../device-properties/_aircraft-pilot-base.md) (v1.15, pilot-path baseline inherited verbatim) + [`Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/10.aircraft/10.m3d-properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/10.aircraft/10.m3d-properties.md) (v1.11, drift-only).

---

## 1. Distinctive wire surface

M3D is the **older-generation aircraft in the Dock 2 cohort**. Its wire surface is defined by dual-path reporting — the same aircraft publishes different property subsets depending on which gateway (Dock 2 vs RC Pro) relays its telemetry. M3D pilot-path is the **generic aircraft baseline** (from `_aircraft-pilot-base.md`); no M3-series-specific pilot-path extensions exist. M4D pilot-path, by contrast, extends the baseline with 7 M4D-only properties — that asymmetry is the main cohort line in the aircraft-properties surface.

### Property surface (Phase 6b)

- **Dock-path** (via Dock 2 gateway): **42 top-level properties** (24 OSD + 18 state) + `{type-subtype-gimbalindex}` per-payload dynamic struct. See [`../device-properties/m3d.md`](../device-properties/m3d.md) §A.
- **Pilot-path** (via RC Pro gateway): **42 top-level properties** inherited from [`_aircraft-pilot-base.md`](../device-properties/_aircraft-pilot-base.md). No M3D-specific pilot-path extensions.
- **6 writable properties** on dock-path: `obstacle_avoidance` (struct-level rw; per-direction sub-fields), `height_limit`, `night_lights_state`, `camera_watermark_settings` (9 rw sub-fields), `commander_flight_height`, `commander_flight_mode`, `commander_mode_lost_action`, `remaining_power_for_return_home`, `rth_altitude`, `distance_limit_status`. *Note: the aircraft-property summary counts "top-level properties with any rw field," not individual rw keys.*
- **Pilot-path writables** inherited from baseline: `obstacle_avoidance` is `r` only on pilot-path (`rw` on dock-path). `height_limit`, `night_lights_state`, `camera_watermark_settings` remain `rw`.
- **No pilot-path `commander_*` keys on M3D** — these are M4D-pilot-path extensions. M3D pilot-path cannot be commanded via `commander_flight_height`; cloud implementations doing FlyTo against M3D pilot-path must issue the services equivalents from Phase 4c ([`fly_to_point.md`](../mqtt/dock-to-cloud/services/fly_to_point.md)) against the dock-path instead.
- **Enum drift dock-path vs pilot-path** — same aircraft, different labels:
  - `position_state.quality` adds `"10":"RTK fixed"` on dock-path; pilot-path stops at `"5"`.
  - `ir_metering_mode` uses short labels (`"Ir metering off"`) on dock-path; long labels (`"IR metering disabled"`) on pilot-path — see [`_aircraft-pilot-base.md`](../device-properties/_aircraft-pilot-base.md) §4.1.
  - `latitude`, `longitude`, `height`, `home_latitude`, `home_longitude` — `double` on dock-path, `float` on pilot-path.
  - `total_flight_time` — `float` on both paths (same as baseline).

### MQTT methods (Phase 4)

M3D participates in **all Phase 4 sub-phases** where the dock is Dock 2 (see the Dock 2 annex [`dock2.md`](dock2.md) §1 for the method catalog). Aircraft-specific methods use Dock 2 as the gateway. No M3D-specific MQTT methods exist — Phase 4 catalogs are dock-keyed, not aircraft-keyed.

On the pilot-path (Phase 4h), M3D participates via its paired RC Pro Enterprise. RC Pro handoff / authority-grab methods target the M3D by SN in the payload, not by topic. See the [RC Pro annex](rc-pro.md) §1 for the relevant method surface.

### Workflows (Phase 9)

M3D participates in all 11 workflows as the aircraft role, with these cohort-specific notes:

- [`wayline-upload-and-execution.md`](../workflows/wayline-upload-and-execution.md) — M3D supports Phase 4b's 21-method dock-path wayline surface. M3D does **not** participate in Dock-3-primary `in_flight_wayline_*` family.
- [`live-flight-controls-drc.md`](../workflows/live-flight-controls-drc.md) — dock-path DRC against Dock 2; no Dock-3-only AI / PSDK / speaker / light services. Pilot-path DRC against RC Pro uses dock-canonical `/services` methods (RC Pro does not carry the `drc_*` prefix; see RC Pro annex §1).
- [`airsense-events.md`](../workflows/airsense-events.md) — M3D is AirSense-equipped; publishes `airsense_warning` events via Dock 2. See [`events/airsense_warning.md`](../mqtt/dock-to-cloud/events/airsense_warning.md).
- [`remote-control-handoff.md`](../workflows/remote-control-handoff.md) — participates through RC Pro Enterprise with the Phase 4h consent-gated flow.

### Livestream (Phase 7)

M3D is a source of live video streamed via Dock 2 or RC Pro. Protocol support is **gateway-determined**, not aircraft-determined:
- Via Dock 2: RTMP / GB28181 / WebRTC / Agora.
- Via RC Pro: RTMP / GB28181 / Agora (no WebRTC — RC Pro drops).

The aircraft's `cameras` / `live_capacity` structures describe the selectable stream sources; gateway selects transport.

### WPML (Phase 7)

M3D uses the generic WPML action catalog per [`../wpml/common-elements.md`](../wpml/common-elements.md) §16 actuator functions. M3D does **not** support the M4D/M4TD-only actions:
- `megaphone` — PSDK megaphone playback (M4D/M4TD only).
- `searchlight` — PSDK searchlight control (M4D/M4TD only).

M3D-compatible actions: `takePhoto`, `startRecord`, `stopRecord`, `gimbalRotate`, `orientedShoot`, `panoShot`, `focus`, `hover`, `zoom`, `customDirName`, and the rest of the shared 14-action catalog. See the WPML common-elements doc for the full list.

### HMS + error codes (Phase 8)

M3D emits HMS alarms via its Dock 2 gateway. Copy-key splicing uses `fpv_tip_{code}[_in_the_sky]` for aircraft-tier UI. Alarms are airframe-classified in [`../hms-codes/`](../hms-codes/README.md); M3D participates across the `0x14` payload IMU, `0x15` mmWave radar, `0x1A` vision sensors, `0x1B` navigation, `0x1C` camera (H20N / H30T for M3D), `0x1D` gimbal, `0x1E` PSDK payload, `0x1F` cellular LTE, and `0x20` takeoff-tag prefixes. The `0x16` flight-control prefix (921 codes) is airframe-agnostic and applies fully.

---

## 2. Cohort asymmetries

**vs M4D** (current-gen sibling) — captured in [`../device-properties/m4d.md`](../device-properties/m4d.md) §A.1 + §B:
- `mode_code` enum max `20` on M3D vs `21` on M4D (M4D adds code `21` for inbound/outbound flight phase).
- `remaining_power_for_return_home` recommendation text: "25–50%" on M3D (Dock 2); "15–50%" on M4D (Dock 3).
- `type_subtype_gimbalindex` source schema-cell is clean on M3D; garbled on M4D (`{_{type-subtype-gimbalindex}__aembLbhPpc}`) — extraction artifact, not a semantic difference.
- M3D pilot-path uses the baseline verbatim; M4D pilot-path extends with 7 M4D-specific properties + 6 overrides.

**vs M3TD** (same-cohort thermal variant) — property-level duplicate; see [`m3td.md`](m3td.md).

---

## 3. Implementation gotchas

Carry from Phase 6b [`../device-properties/m3d.md`](../device-properties/m3d.md) "DJI-source inconsistencies" (full enumeration there):

1. **Dock-path vs pilot-path type drift on coordinate fields** — `latitude`, `longitude`, `height`, `home_latitude`, `home_longitude` are `double` on dock-path but `float` on pilot-path. Cloud implementations that store M3D position telemetry should normalize to the wider type (`double`) on ingestion or maintain two storage paths. A cloud relying on `double` precision for RTK-fixed M3D will see reduced precision via the pilot path.
2. **`position_state.quality` enum extension** — dock-path includes `"10":"RTK fixed"`; pilot-path stops at `"5":"Gear 5"`. An RTK-fixed M3D will report `"10"` via Dock 2 but there is no equivalent label via RC Pro; cloud implementations must either treat the pilot-path `"5"` as "highest available" or query the dock-path concurrently for true RTK state.
3. **`obstacle_avoidance` accessMode drift** — `rw` on dock-path (cloud can toggle per-direction); `r` on pilot-path. Attempting to `property/set` this key via RC Pro will fail with a services_reply error.
4. **`camera_watermark_settings` schema is identical on both paths but not documented in M3D-specific extract** — inherits from baseline. Cloud implementations targeting watermark config must use the baseline's 9-sub-field definition.
5. **`ir_metering_mode` label-form divergence** — dock-path short form (`"Ir metering off"`), pilot-path long form. Parse by code; do not branch on label string.

Phase 9 gotchas:

6. **M3D RTH altitude behaviour** — breakpoint resume uses `rth_altitude` (dock-path writable) instead of the WPML `wpml:takeOffSecurityHeight` (wayline-file-level). When resuming a task mid-flight, the dock-path `rth_altitude` wins; the wayline-file value is ignored for the recovery branch. See [`wayline-upload-and-execution.md`](../workflows/wayline-upload-and-execution.md) §Breakpoint recovery.
7. **M3D payload catalog includes H20N (multi-sensor night) and H30T (multi-sensor thermal)** per the Dock 2 DJI product-support reference — M3TD is the thermal-specific SKU with H30T. Cloud implementations discovering the aircraft type should expect the full set of Zenmuse enterprise payloads across both SKUs. The distinction is captured in `»payload_index` enum values, not in aircraft properties.

---

## 4. Features this device lacks

- No `commander_*` pilot-path writable surface (M4D-only).
- No `current_commander_flight_mode` pilot-path read-back (M4D-only).
- No `offline_map_enable` pilot-path state (M4D-only).
- No `current_rth_mode` / `rth_mode` pilot-path state (M4D-only).
- No WPML `megaphone` / `searchlight` actions (M4D/M4TD PSDK payloads only).
- No participation in `in_flight_wayline_*` (Dock 3 / M4 cohort).
- No Dock-3-only DRC surface via Dock 2 gateway.

---

## 5. Cross-reference map

| Phase | Doc | What's covered |
|---|---|---|
| 3 HTTP | [`../http/README.md`](../http/README.md) | 16 endpoints — M3D wayline / media traffic traverses these via Dock 2 or RC Pro. |
| 4 MQTT | [`../mqtt/dock-to-cloud/README.md`](../mqtt/dock-to-cloud/README.md), [`../mqtt/pilot-to-cloud/README.md`](../mqtt/pilot-to-cloud/README.md) | Dock-path via Dock 2; pilot-path via RC Pro (see [`rc-pro.md`](rc-pro.md)). |
| 5 WebSocket | [`../websocket/README.md`](../websocket/README.md) | Pilot-to-Cloud push messages (8 messages) surface M3D telemetry when gateway is RC Pro. |
| 6 Properties | [`../device-properties/m3d.md`](../device-properties/m3d.md) | 42 dock-path top-level + 42 pilot-path (via baseline) + `{type-subtype-gimbalindex}`. |
| 7 WPML + livestream | [`../wpml/`](../wpml/README.md), [`../livestream-protocols/README.md`](../livestream-protocols/README.md) | Shared WPML actions; gateway-determined livestream protocol set. |
| 8 Codes | [`../hms-codes/README.md`](../hms-codes/README.md), [`../error-codes/README.md`](../error-codes/README.md) | Full catalog. |
| 9 Workflows | [`../workflows/README.md`](../workflows/README.md) | Full aircraft participant — dock-path via Dock 2; pilot-path via RC Pro. |

## 6. Source provenance

| File | Role |
|---|---|
| [`DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt) | v1.15 dock-path primary (2,373 lines; M3D + M3TD co-documented). |
| [`../device-properties/_aircraft-pilot-base.md`](../device-properties/_aircraft-pilot-base.md) | v1.15 pilot-path baseline inherited by M3D. |
| [`Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/10.aircraft/10.m3d-properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/10.aircraft/10.m3d-properties.md) | v1.11 canonical — drift cross-check only. |
| [`Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/10.m3-series/00.properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/10.m3-series/00.properties.md) | v1.11 M3-series pilot-path canonical — drift cross-check only. Matches baseline; no v1.15 M3-series extract exists. |
| [`m3td.md`](m3td.md) | Thermal-variant annex. |
