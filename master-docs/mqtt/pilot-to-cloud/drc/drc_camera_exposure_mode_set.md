# `drc_camera_exposure_mode_set` — set exposure mode (DRC channel)

RC-Plus-2-specific DRC variant of [`../../dock-to-cloud/services/camera_exposure_mode_set.md`](../../dock-to-cloud/services/camera_exposure_mode_set.md). Same semantics — switch exposure mode among auto / shutter priority / aperture priority / manual — delivered on the lightweight DRC channel.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.**

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_camera_exposure_mode_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_exposure_mode_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | text | Camera enumeration `{type-subtype-gimbalindex}`. |
| `camera_type` | enum_string | `{"wide", "zoom"}`. |
| `exposure_mode` | enum_int | `{1: "Auto", 2: "Shutter priority", 3: "Aperture priority", 4: "Manual exposure"}`. |

### Example

```json
{
  "data": {
    "camera_type": "zoom",
    "exposure_mode": 1,
    "payload_index": "89-0-0"
  },
  "method": "drc_camera_exposure_mode_set",
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
  "method": "drc_camera_exposure_mode_set",
  "seq": 1
}
```

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Remote-Control.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |
