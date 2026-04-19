# `flighttask_undo` — cancel one or more prepared missions

Cloud command that cancels missions that were previously prepared via [`flighttask_prepare`](flighttask_prepare.md) but have not yet been executed (or have been issued). Operates in batch — accepts a collection of `flight_ids`.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `flighttask_undo` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `flighttask_undo` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `flight_ids` | array of string | Task IDs to cancel. |

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "flighttask_undo",
  "timestamp": 1234567890123,
  "data": {
    "flight_ids": ["aaaaaaa", "bbbbbbb"]
  }
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success. |

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/50.wayline.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Wayline-Management.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-WaylineManagement.txt]` | v1.15 (Dock 3). |
