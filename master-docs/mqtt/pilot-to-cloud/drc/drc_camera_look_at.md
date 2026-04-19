# `drc_camera_look_at` — camera look-at (DRC channel)

RC-Plus-2-specific DRC variant of [`../../dock-to-cloud/services/camera_look_at.md`](../../dock-to-cloud/services/camera_look_at.md). Same semantics — orient the aircraft toward a latitude/longitude/height target — delivered on the lightweight DRC channel.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.**

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_camera_look_at` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_look_at` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | text | Camera enumeration `{type-subtype-gimbalindex}`. |
| `locked` | bool | `false` = gimbal only; `true` = lock aircraft heading. |
| `latitude` | double | Target latitude degrees. `[-90, 90]`. 6 decimal places. |
| `longitude` | double | Target longitude degrees. `[-180, 180]`. 6 decimal places. |
| `height` | float | Target ellipsoid height in meters. `[2, 10000]`, step `0.1`. |

### Example

```json
{
  "data": {
    "height": 24.838796976545467,
    "latitude": 22.908061229971967,
    "locked": false,
    "longitude": 113.70510712582023,
    "payload_index": "89-0-0"
  },
  "method": "drc_camera_look_at",
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
  "method": "drc_camera_look_at",
  "seq": 1
}
```

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Remote-Control.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |
