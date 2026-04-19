# `drc_camera_photo_format_set` — set infrared photo format

DRC command that sets the infrared photo format on the Dock 3 camera. Only takes effect when the live camera is switched to infrared mode.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — M4TD IR camera.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_camera_photo_format_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_photo_format_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration. |
| `photo_format` | enum int | `7` = RJPEG (radiometric JPEG with embedded temperature data); `16` = DLT664. |

### Example

```json
{
  "seq": 1,
  "method": "drc_camera_photo_format_set",
  "data": {
    "payload_index": "81-0-0",
    "photo_format": 16
  }
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

## Relationship to other methods

- The current photo format is readable from [`drc_camera_state_push.camera_state.photo_format`](drc_camera_state_push.md).

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — only source. |
