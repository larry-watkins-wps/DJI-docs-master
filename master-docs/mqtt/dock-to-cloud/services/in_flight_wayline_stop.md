# `in_flight_wayline_stop` — pause an in-flight Virtual Cockpit route

Cloud command that pauses a Virtual Cockpit flight route previously dispatched via [`in_flight_wayline_deliver`](in_flight_wayline_deliver.md). The aircraft holds position; resume with [`in_flight_wayline_recover`](in_flight_wayline_recover.md).

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **v1.15 addition** — no v1.11 counterpart.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `in_flight_wayline_stop` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `in_flight_wayline_stop` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `in_flight_wayline_id` | string | Flight route task ID to pause. |

### Example

```json
{
  "tid": "9da675b5-0a87-4b89-9813-4fb2e3aac4ec",
  "bid": "bf1d9985-5077-4ea5-9f2b-44edbcde9a11",
  "method": "in_flight_wayline_stop",
  "timestamp": 1731136137237,
  "data": {
    "in_flight_wayline_id": "36747381-4886-4ed0-9b2b-2919d6d4863c"
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
| `[DJI_Cloud/DJI_CloudAPI-Dock3-WaylineManagement.txt]` | v1.15 (Dock 3) — primary. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Wayline-Management.txt]` | v1.15 (Dock 2). |
