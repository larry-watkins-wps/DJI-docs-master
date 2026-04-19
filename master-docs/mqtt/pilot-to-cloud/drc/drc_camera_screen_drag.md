# `drc_camera_screen_drag` — gimbal screen-drag control (DRC channel)

RC-Plus-2-specific DRC variant of [`../../dock-to-cloud/services/camera_screen_drag.md`](../../dock-to-cloud/services/camera_screen_drag.md). Same semantics — continuous pitch/yaw gimbal drive, optionally locking aircraft heading — delivered on the lightweight DRC channel for reduced latency.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.** RC Pro uses the non-prefixed [`camera_screen_drag`](../../dock-to-cloud/services/camera_screen_drag.md) on `/services`.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_camera_screen_drag` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_screen_drag` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | text | Camera enumeration `{type-subtype-gimbalindex}`. |
| `locked` | bool | `false` = only gimbal turns; `true` = lock aircraft heading so gimbal + body turn together. |
| `pitch_speed` | double | Gimbal pitch speed (rad/s). |
| `yaw_speed` | double | Gimbal yaw speed (rad/s). Effective only when `locked == false`. |

### Example

```json
{
  "data": {
    "locked": false,
    "payload_index": "89-0-0",
    "pitch_speed": 0.6,
    "yaw_speed": -0.6
  },
  "method": "drc_camera_screen_drag",
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
  "data": {
    "result": 0
  },
  "method": "drc_camera_screen_drag",
  "seq": 1
}
```

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Remote-Control.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |
