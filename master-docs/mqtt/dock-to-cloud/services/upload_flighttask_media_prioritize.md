# `upload_flighttask_media_prioritize` — cloud bumps a flight task to the top of the media-upload queue

Cloud command that tells the dock which flight task's media files should be uploaded first. Used when an operator wants to view a recent task's results ahead of any backlog. Cloud-initiated counterpart to the dock-initiated event [`highest_priority_upload_flighttask_media`](../events/highest_priority_upload_flighttask_media.md).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `upload_flighttask_media_prioritize` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `upload_flighttask_media_prioritize` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `flight_id` | string | ID of the flight task whose media should move to the top of the upload queue. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "flight_id": "xxx"
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "upload_flighttask_media_prioritize"
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero represents an error. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "result": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "upload_flighttask_media_prioritize"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/40.file.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Media-Management.txt]` | v1.15 (Dock 2) — identical to v1.11. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Media-Management.txt]` | v1.15 (Dock 3) — identical payload. |
