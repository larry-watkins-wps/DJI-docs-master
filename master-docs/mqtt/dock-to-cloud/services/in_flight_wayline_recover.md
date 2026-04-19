# `in_flight_wayline_recover` — resume a paused in-flight Virtual Cockpit route

Cloud command that resumes a Virtual Cockpit flight route paused via [`in_flight_wayline_stop`](in_flight_wayline_stop.md).

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **v1.15 addition** — no v1.11 counterpart.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `in_flight_wayline_recover` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `in_flight_wayline_recover` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `in_flight_wayline_id` | string | Flight route task ID to resume. |

### Example

```json
{
  "tid": "b3a76306-2576-4bc5-9a55-77e4f8f3b17c",
  "bid": "8fd307b9-6a70-465c-aeb7-5edac860017b",
  "method": "in_flight_wayline_recover",
  "timestamp": 1731136244583,
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
