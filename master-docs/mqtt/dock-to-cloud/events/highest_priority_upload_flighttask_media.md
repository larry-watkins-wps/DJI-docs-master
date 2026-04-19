# `highest_priority_upload_flighttask_media` — dock announces the top-priority media-upload flight task

Event pushed by the dock when a flight task changes to the highest upload priority — that is, when the dock has re-ordered its internal queue and now intends to upload this task's media first. The cloud acknowledges with `need_reply: 1`. Companion to [`upload_flighttask_media_prioritize`](../services/upload_flighttask_media_prioritize.md), which is the cloud-initiated counterpart.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, events-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `highest_priority_upload_flighttask_media` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `highest_priority_upload_flighttask_media` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `flight_id` | string | ID of the flight task whose media now has the highest upload priority. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "flight_id": "xxx"
  },
  "gateway": "xxx",
  "need_reply": 1,
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "highest_priority_upload_flighttask_media"
}
```

## Down (reply) — `data` fields

Standard events_reply envelope: `data.result` (integer; `0` = success).

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/40.file.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Media-Management.txt]` | v1.15 (Dock 2) — identical to v1.11. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Media-Management.txt]` | v1.15 (Dock 3) — identical payload. |
