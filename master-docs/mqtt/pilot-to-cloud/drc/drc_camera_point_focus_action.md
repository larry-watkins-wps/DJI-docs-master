# `drc_camera_point_focus_action` — spot AF (DRC channel)

RC-Plus-2-specific DRC variant of [`../../dock-to-cloud/services/camera_point_focus_action.md`](../../dock-to-cloud/services/camera_point_focus_action.md). Same semantics — trigger spot autofocus at a point in the camera frame — delivered on the lightweight DRC channel.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.**

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_camera_point_focus_action` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_point_focus_action` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | text | Camera enumeration `{type-subtype-gimbalindex}`. |
| `camera_type` | enum_string | `{"wide": "Wide-angle", "zoom": "Zoom"}`. On M30 series, zoom-only. |
| `x` | double | Focus point x, `[0,1]`, upper-left origin. |
| `y` | double | Focus point y, `[0,1]`, upper-left origin. |

### Example

```json
{
  "data": {
    "camera_type": "zoom",
    "payload_index": "89-0-0",
    "x": 0.5,
    "y": 0.5
  },
  "method": "drc_camera_point_focus_action",
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
  "method": "drc_camera_point_focus_action",
  "seq": 1
}
```

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Remote-Control.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |
