# `drc_camera_aim` — double-tap aim (DRC channel)

RC-Plus-2-specific DRC variant of [`../../dock-to-cloud/services/camera_aim.md`](../../dock-to-cloud/services/camera_aim.md). Same semantics — aim the selected camera at a target point within its field of view — delivered on the lightweight DRC channel.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.** RC Pro uses the non-prefixed [`camera_aim`](../../dock-to-cloud/services/camera_aim.md) on `/services`.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_camera_aim` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_aim` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | text | Camera enumeration `{type-subtype-gimbalindex}`. |
| `camera_type` | enum_string | `{"ir": "Infrared", "wide": "Wide-angle", "zoom": "Zoom"}`. |
| `locked` | bool | `false` = only gimbal turns; `true` = lock aircraft heading. |
| `x` | double | Target coord x, `[0,1]`, upper-left origin, horizontal axis. |
| `y` | double | Target coord y, `[0,1]`, upper-left origin, vertical axis. |

### Example

```json
{
  "data": {
    "camera_type": "wide",
    "locked": false,
    "payload_index": "89-0-0",
    "x": 0.8310580204778157,
    "y": 0.32272727272727275
  },
  "method": "drc_camera_aim",
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
  "method": "drc_camera_aim",
  "seq": 1
}
```

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Remote-Control.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |
