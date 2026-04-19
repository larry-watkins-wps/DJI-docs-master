# `drc_camera_focal_length_set` — set zoom factor (DRC channel)

RC-Plus-2-specific DRC variant of [`../../dock-to-cloud/services/camera_focal_length_set.md`](../../dock-to-cloud/services/camera_focal_length_set.md). Same semantics — set a discrete zoom factor on the selected camera — delivered on the lightweight DRC channel.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.**

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_camera_focal_length_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_focal_length_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | text | Camera enumeration `{type-subtype-gimbalindex}`. |
| `camera_type` | enum_string | `{"ir", "wide", "zoom"}`. |
| `zoom_factor` | double | Zoom factor. Range 2..200 for visible, 2..20 for infrared. |

### Example

```json
{
  "data": {
    "camera_type": "zoom",
    "payload_index": "89-0-0",
    "zoom_factor": 7
  },
  "method": "drc_camera_focal_length_set",
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
  "method": "drc_camera_focal_length_set",
  "seq": 1
}
```

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Remote-Control.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |
