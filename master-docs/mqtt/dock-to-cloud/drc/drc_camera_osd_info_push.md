# `drc_camera_osd_info_push` — camera OSD info push

Event pushed by the aircraft carrying the per-camera OSD payload for the pilot HUD — wide lens + zoom lens settings (exposure, ISO, shutter, aperture, focus), IR lens settings (thermal gain, isotherm, palette, zoom ratio), laser-measured target geo-position, and the liveview field-of-view rectangle. The largest event in the Remote-Control surface. The complete enum tables are long — the per-field summary below is a pointer; cite the source file for the full bitmaps.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** with **topic divergence** — see [Source differences](#source-differences).

---

## Topics

| Direction | Cohort | Topic | Method |
|---|---|---|---|
| Device → Cloud | **Dock 3 v1.15** | `thing/product/{gateway_sn}/events` | `drc_camera_osd_info_push` |
| Device → Cloud | **Dock 2 v1.15 + v1.11** | `thing/product/{gateway_sn}/drc/up` | `drc_camera_osd_info_push` |

Same topic divergence as [`drc_drone_state_push`](drc_drone_state_push.md) — Dock 3 demotes this push from the DRC channel to `/events`. A cloud supporting both cohorts must subscribe to both.

## Up — `data` fields (grouped)

### Top-level

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration value. Format `{type-subtype-gimbalindex}`. |
| `wide_lense` | struct | Wide-angle lens configuration. |
| `zoom_lense` | struct | Zoom lens configuration. |
| `measure_target` | struct | Laser-ranged target position + distance. |
| `ir_lense` | struct | IR / thermal configuration. |
| `liveview` | struct | Liveview region of interest. |

### `wide_lense`

| Field | Type | Notes |
|---|---|---|
| `wide_exposure_mode` | enum int | `1`–`4`: Auto / Shutter Priority / Aperture Priority / Manual. |
| `wide_iso` | enum int | `0`–`11`, `255` = FIXED. `0` = Auto, `2` = 50, `3` = 100, `4` = 200, `5` = 400, `6` = 800, `7` = 1600, `8` = 3200, `9` = 6400, `10` = 12800, `11` = 25600. See DJI source for full list. |
| `wide_shutter_speed` | enum int | `0`–`59` values `1/8000 s` through `8.0 s`; `65534` = Auto. Full list in DJI source. |
| `wide_exposure_value` | enum int | `1`–`31` → `-5.0 EV` … `5.0 EV` in 0.3–0.4 EV steps; `255` = FIXED. |
| `wide_aperture_value` | enum int | `0` = F_AUTO; otherwise aperture × 100 (e.g. `200` = F2.0, `280` = F2.8, `25600` = F256). |

### `zoom_lense`

Same enum set as `wide_lense` plus:

| Field | Type | Notes |
|---|---|---|
| `zoom_focus_mode` | enum int | `0` = MF, `1` = AFS, `2` = AFC. |
| `zoom_focus_value` | int | Current focus value. |
| `zoom_max_focus_value` | int | Max focus value. |
| `zoom_min_focus_value` | int | Min focus value. |
| `zoom_calibrate_farthest_focus_value` | int | Calibrated farthest clear position. |
| `zoom_calibrate_nearest_focus_value` | int | Calibrated nearest clear position. |
| `zoom_focus_state` | int | Device-specific focus state. |
| `zoom_factor` | int / float | Current zoom ratio. |
| `zoom_aperture_value` | enum int | e.g. `440` = F4.4. |

### `measure_target`

| Field | Type | Notes |
|---|---|---|
| `measure_target_longitude` | double | ±180°. |
| `measure_target_latitude` | double | ±90°. |
| `measure_target_altitude` | double | Meters. |
| `measure_target_distance` | double | Meters. |

### `ir_lense`

| Field | Type | Notes |
|---|---|---|
| `screen_split_enable` | bool | Split-screen (wide + IR) enabled. |
| `ir_zoom_factor` | float | `2`–`20`. |
| `thermal_supported_palette_styles` | array of enum int | Device-specific palette styles. |
| `thermal_gain_mode` | enum int | `0` = Auto, `1` = Low gain (0°C – 500°C), `2` = High gain (−20°C – 150°C). |
| `thermal_isotherm_state` | enum int | `0` = Disabled, `1` = Enabled. |
| `thermal_isotherm_upper_limit` | int (°C) | Upper limit when isotherm is enabled. |
| `thermal_isotherm_lower_limit` | int (°C) | Lower limit when isotherm is enabled. |
| `thermal_global_temperature_min` | float (°C) | Minimum temperature in view. |
| `thermal_global_temperature_max` | float (°C) | Maximum temperature in view. |

### `liveview.liveview_world_region`

Field-of-view rectangle of the zoom camera relative to the wide-angle or IR camera, normalized with origin at the top-left corner of the lens.

| Field | Type | Notes |
|---|---|---|
| `left` | float | X-axis start, top-left. |
| `top` | float | Y-axis start, top-left. |
| `right` | float | X-axis start, bottom-right. |
| `bottom` | float | Y-axis start, bottom-right. |

### Example

```json
{
  "data": {
    "ir_lense": {
      "ir_zoom_factor": 2,
      "screen_split_enable": false,
      "thermal_current_palette_style": 11,
      "thermal_gain_mode": 2,
      "thermal_global_temperature_max": 40.0373764038086,
      "thermal_global_temperature_min": 31.65154457092285,
      "thermal_isotherm_lower_limit": -20,
      "thermal_isotherm_state": 0,
      "thermal_isotherm_upper_limit": 150
    },
    "liveview": {
      "liveview_world_region": {
        "bottom": 0.5609484910964966,
        "left": 0.43238765001297,
        "right": 0.5639060735702515,
        "top": 0.433199942111969
      }
    },
    "measure_target": {
      "measure_target_altitude": 34.60000228881836,
      "measure_target_distance": 0,
      "measure_target_error_state": 1,
      "measure_target_latitude": 22.907619920797877,
      "measure_target_longitude": 113.70345426744846
    },
    "payload_index": "81-0-0",
    "wide_lense": {
      "wide_aperture_value": 10,
      "wide_exposure_mode": 1,
      "wide_exposure_value": 16,
      "wide_iso": 8,
      "wide_shutter_speed": 45
    },
    "zoom_lense": {
      "zoom_aperture_value": 10,
      "zoom_calibrate_farthest_focus_value": 34,
      "zoom_calibrate_nearest_focus_value": 64,
      "zoom_exposure_mode": 1,
      "zoom_exposure_value": 16,
      "zoom_factor": 6.999994214380596,
      "zoom_focus_mode": 0,
      "zoom_focus_state": 0,
      "zoom_focus_value": 34,
      "zoom_iso": 8,
      "zoom_max_focus_value": 64,
      "zoom_min_focus_value": 33,
      "zoom_shutter_speed": 45
    }
  },
  "method": "drc_camera_osd_info_push",
  "seq": 1
}
```

## Source differences

- **Topic family diverges.** Dock 3 publishes on `/events`; Dock 2 + v1.11 publish on `/drc/up`.
- The field set is otherwise identical across cohorts — the large enums are stable.

## Source inconsistencies flagged by DJI's own example

- **Fields present in the example but not in the schema table:** `thermal_current_palette_style` and `measure_target_error_state`. Both appear in the Dock 3 and Dock 2 examples. Treat as present on the wire; cite the source file when implementing, since DJI's declared schema is incomplete.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/180.remote-control.md]` | v1.11 canonical (Dock 2) — `/drc/up`. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Control.txt]` | v1.15 (Dock 2) — identical to v1.11 shape. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — `/events` topic; full schema mirrors Dock 2. |
