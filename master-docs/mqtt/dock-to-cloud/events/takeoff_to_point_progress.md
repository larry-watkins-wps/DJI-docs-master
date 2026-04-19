# `takeoff_to_point_progress` — one-key takeoff result notification

Event pushed by the dock while an aircraft is executing a **one-key takeoff-to-point** mission (started via [`takeoff_to_point`](../services/takeoff_to_point.md)). Reports the task state, remaining distance/time, current waypoint index, and the planned trajectory. Requires reply (`need_reply: 1`).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, request-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `takeoff_to_point_progress` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `takeoff_to_point_progress` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `status` | enum string | Task state. See **status enum** below. |
| `result` | integer | Return code. Non-zero = error. |
| `flight_id` | string | One-key takeoff mission UUID (matches `flight_id` supplied to `takeoff_to_point`). |
| `track_id` | string | Track ID. |
| `way_point_index` | integer | Index of the waypoint currently being executed. |
| `remaining_distance` | float (m) | Remaining mission distance, step `0.1`. |
| `remaining_time` | float (s) | Remaining mission time, step `0.1`. |
| `planned_path_points` | array of struct | Planned trajectory points. |
| `planned_path_points[].latitude` | double | Latitude, range `[-90, 90]`, 6-decimal precision. |
| `planned_path_points[].longitude` | double | Longitude, range `[-180, 180]`, 6-decimal precision. |
| `planned_path_points[].height` | float (m) | Ellipsoid height of the trajectory point, step `0.1`. |

### `status` enum

| Value | Meaning |
|---|---|
| `task_ready` | Ready for takeoff. |
| `wayline_progress` | Executing. |
| `wayline_ok` | Executed successfully, flown to target point. |
| `task_finish` | One-key takeoff mission completed. |
| `wayline_failed` | Execution failed. |
| `wayline_cancel` | Cancel flying to target point. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "flight_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
    "planned_path_points": [
      {
        "height": 123.234,
        "latitude": 13.23,
        "longitude": 123.234
      }
    ],
    "remaining_distance": 0,
    "remaining_time": 0,
    "result": 0,
    "status": "wayline_ok",
    "track_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
    "way_point_index": 1
  },
  "need_reply": 1,
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 16540709686556,
  "method": "takeoff_to_point_progress"
}
```

## Down (reply) — `data` fields

Standard events_reply envelope: `data.result` (integer; `0` = success).

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
