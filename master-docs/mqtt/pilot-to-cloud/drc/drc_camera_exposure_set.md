# `drc_camera_exposure_set` — set exposure value (DRC channel)

RC-Plus-2-specific DRC variant of [`../../dock-to-cloud/services/camera_exposure_set.md`](../../dock-to-cloud/services/camera_exposure_set.md). Same semantics — set EV value on the selected camera — delivered on the lightweight DRC channel. Full `exposure_value` enum is 1..31 (mapping to `-5.0EV` .. `5.0EV` in 0.3–0.4 EV steps) plus `255` for `FIXED`.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.** See the [dock-to-cloud parallel](../../dock-to-cloud/services/camera_exposure_set.md) for the full EV enum table.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_camera_exposure_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_exposure_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | text | Camera enumeration `{type-subtype-gimbalindex}`. |
| `camera_type` | enum_string | `{"wide", "zoom"}`. |
| `exposure_value` | enum_string / int | EV step, `1..31` + `255` = FIXED. DJI declares `enum_string` but sends as integer in the example (same inconsistency as dock-to-cloud 4c). |

### Example

```json
{
  "data": {
    "camera_type": "zoom",
    "exposure_value": 8,
    "payload_index": "89-0-0"
  },
  "method": "drc_camera_exposure_set",
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
  "method": "drc_camera_exposure_set",
  "seq": 1
}
```

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Remote-Control.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |
