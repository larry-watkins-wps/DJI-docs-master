# `drc_camera_photo_take` — take photo (DRC channel)

RC-Plus-2-specific DRC variant of [`../../dock-to-cloud/services/camera_photo_take.md`](../../dock-to-cloud/services/camera_photo_take.md). Same semantics — take a photo on the selected payload camera; persistent modes (panorama) stream further progress on [`camera_photo_take_progress`](../../dock-to-cloud/events/camera_photo_take_progress.md) — delivered on the lightweight DRC channel.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.**

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_camera_photo_take` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_photo_take` |

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
  "method": "drc_camera_photo_take",
  "seq": 1
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success. |
| `status` | enum_string | `{"in_progress": "Executing"}`. Present when the capture is a persistent mode (panorama etc.); progress reported via the [`camera_photo_take_progress`](../../dock-to-cloud/events/camera_photo_take_progress.md) event. |

### Example

```json
{
  "data": { "result": 0 },
  "method": "drc_camera_photo_take",
  "seq": 1
}
```

## Relationship to other methods

- Companion to [`drc_camera_photo_stop`](drc_camera_photo_stop.md) (stops an in-progress persistent capture).
- Progress for persistent captures is reported via the standard-envelope event [`camera_photo_take_progress`](../../dock-to-cloud/events/camera_photo_take_progress.md) on `/events`, not on the DRC channel.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Remote-Control.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |
