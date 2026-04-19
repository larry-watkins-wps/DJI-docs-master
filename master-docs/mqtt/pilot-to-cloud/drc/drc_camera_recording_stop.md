# `drc_camera_recording_stop` — stop recording (DRC channel)

RC-Plus-2-specific DRC variant of [`../../dock-to-cloud/services/camera_recording_stop.md`](../../dock-to-cloud/services/camera_recording_stop.md). Same intent — stop video recording on the selected payload camera — delivered on the lightweight DRC channel.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.** RC Pro uses the non-prefixed [`camera_recording_stop`](../../dock-to-cloud/services/camera_recording_stop.md) on `/services`.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_camera_recording_stop` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_recording_stop` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | text | Camera enumeration `{type-subtype-gimbalindex}`. |

### Example

```json
{
  "data": {
    "payload_index": "89-0-0"
  },
  "method": "drc_camera_recording_stop",
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
  "method": "drc_camera_recording_stop",
  "seq": 1
}
```

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Remote-Control.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |
