# `drc_camera_frame_zoom` — subject zoom / frame select (DRC channel)

RC-Plus-2-specific DRC variant of [`../../dock-to-cloud/services/camera_frame_zoom.md`](../../dock-to-cloud/services/camera_frame_zoom.md). Same semantics — select a rectangular target frame in the camera view and the camera automatically zooms to center on it — delivered on the lightweight DRC channel.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.**

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_camera_frame_zoom` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_frame_zoom` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | text | Camera enumeration `{type-subtype-gimbalindex}`. |
| `camera_type` | enum_string | `{"ir", "wide", "zoom"}`. |
| `locked` | bool | `false` = only gimbal turns; `true` = lock aircraft heading. |
| `x` | float | Target-frame upper-left x, `[0,1]`, step `0.000001`. |
| `y` | float | Target-frame upper-left y, `[0,1]`, step `0.000001`. |
| `width` | float | Target-frame width, `[0,1]`, step `0.000001`. |
| `height` | float | Target-frame height, `[0,1]`, step `0.000001`. |

### Example

```json
{
  "data": {
    "camera_type": "zoom",
    "height": 0.5,
    "locked": true,
    "payload_index": "89-0-0",
    "width": 0.8,
    "x": 0.5,
    "y": 0.5
  },
  "method": "drc_camera_frame_zoom",
  "seq": 1
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success. |

### Example

```json
{
  "data": { "result": 0 },
  "method": "drc_camera_frame_zoom",
  "seq": 1
}
```

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Remote-Control.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |
