# `drc_camera_focus_value_set` — set focus value (DRC channel)

RC-Plus-2-specific DRC variant of [`../../dock-to-cloud/services/camera_focus_value_set.md`](../../dock-to-cloud/services/camera_focus_value_set.md). Same semantics — set manual-focus value (valid range per `zoom_min_focus_value` / `zoom_max_focus_value` aircraft properties) — delivered on the lightweight DRC channel.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.**

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_camera_focus_value_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_focus_value_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | text | Camera enumeration `{type-subtype-gimbalindex}`. |
| `camera_type` | enum_string | `{"wide", "zoom"}`. |
| `focus_value` | int | Focus value. Range from aircraft properties `zoom_min_focus_value` .. `zoom_max_focus_value`. |

### Example

```json
{
  "data": {
    "camera_type": "zoom",
    "focus_value": 11,
    "payload_index": "89-0-0"
  },
  "method": "drc_camera_focus_value_set",
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
  "method": "drc_camera_focus_value_set",
  "seq": 1
}
```

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Remote-Control.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |
