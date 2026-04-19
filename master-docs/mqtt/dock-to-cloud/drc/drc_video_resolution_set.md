# `drc_video_resolution_set` — set video resolution (Dock 2 legacy)

DRC command that sets the visible-light camera resolution (1920×1080 or 3840×2160) on Dock 2 aircraft. Infrared resolution is fixed at 640×512 and cannot be set.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 only**.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_video_resolution_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_video_resolution_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration. |
| `video_resolution` | enum string | `0` = `1920_1080`, `1` = `3840_2160`. |

### Example

```json
{
  "data": {
    "payload_index": "81-0-0",
    "video_resolution": 0
  },
  "method": "drc_video_resolution_set",
  "seq": 1
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/180.remote-control.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Control.txt]` | v1.15 (Dock 2) — identical. |
