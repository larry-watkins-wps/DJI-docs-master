# `in_flight_wayline_cancel` — cancel an in-flight Virtual Cockpit route

Cloud command that cancels a Virtual Cockpit flight route entirely. After cancellation the aircraft exits the route and typically enters its configured lost-control / default behavior. Distinct from [`in_flight_wayline_stop`](in_flight_wayline_stop.md) which pauses but preserves the route for resumption.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **v1.15 addition** — no v1.11 counterpart.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `in_flight_wayline_cancel` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `in_flight_wayline_cancel` |

## Down — `data` fields

DJI's v1.15 sample shows an empty `data` object. The method is scoped by the outer envelope's `bid` / `tid` correlating to the delivery.

### Example

```json
{
  "tid": "b3a76306-2576-4bc5-9a55-77e4f8f3b17c",
  "bid": "8fd307b9-6a70-465c-aeb7-5edac860017b",
  "method": "in_flight_wayline_cancel",
  "timestamp": 1731136244583,
  "data": {}
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
