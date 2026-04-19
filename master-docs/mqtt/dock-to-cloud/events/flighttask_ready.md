# `flighttask_ready` — task readiness notification

Event pushed by the dock when one or more previously-prepared flight tasks have satisfied all `ready_conditions` and are eligible to execute. For conditional tasks (submitted via [`flighttask_prepare`](../services/flighttask_prepare.md) with `task_type=2`), the device periodically checks readiness and fires this event when conditions are met.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, request-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `flighttask_ready` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `flighttask_ready` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `flight_ids` | array of string | Task IDs whose readiness conditions are now met. |

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "flighttask_ready",
  "timestamp": 1654070968655,
  "data": {
    "flight_ids": ["aaaaaaa", "bbbbbbb"]
  }
}
```

## Down (reply) — `data` fields

Standard events_reply envelope: `data.result` (integer; `0` = success).

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/50.wayline.md]` | v1.11 canonical (Dock 2) — titled "Mission readiness notification" there. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Wayline-Management.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-WaylineManagement.txt]` | v1.15 (Dock 3). |
