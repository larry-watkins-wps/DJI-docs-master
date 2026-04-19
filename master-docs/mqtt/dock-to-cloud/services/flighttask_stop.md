# `flighttask_stop` — task termination

Cloud command that terminates a flight task. In multi-dock scenarios, used to notify the other dock when one dock reports task termination so both docks converge to a consistent state.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `flighttask_stop` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `flighttask_stop` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `flight_id` | string | Task ID to terminate. |
| `reason` | enum int | `0` = normal termination, `1` = state machine of the other dock is abnormal. |

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "flighttask_stop",
  "timestamp": 1234567890123,
  "data": {
    "flight_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
    "reason": 0
  }
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success. |

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "flighttask_stop",
  "timestamp": 1695634358385,
  "data": { "result": 0 }
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/50.wayline.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Wayline-Management.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-WaylineManagement.txt]` | v1.15 (Dock 3). |
