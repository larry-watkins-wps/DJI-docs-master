# `return_home_info` — return-path planning info

Event pushed by the dock carrying the planned return-home trajectory and, for multi-dock missions, the planning status per candidate landing dock. Clients can use this to visualize the return path and, for multi-dock scenarios, to understand which dock the system plans to land at.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, request-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `return_home_info` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `return_home_info` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `planned_path_points` | array of struct | Planned trajectory points. Size unbounded. |
| `planned_path_points[].latitude` | double | Latitude, angle value, ±90°, 6-decimal precision. |
| `planned_path_points[].longitude` | double | Longitude, angle value, ±180°, 6-decimal precision. |
| `planned_path_points[].height` | float | Ellipsoid height of the trajectory point, meters. |
| `last_point_type` | enum int | Type of the last point: `0` = last point is above return point, `1` = last point is not above return point. |
| `flight_id` | string | Task ID. |
| `home_dock_sn` | string | SN of the dock selected as landing target. Multi-dock tasks only; not applicable in single-dock tasks. |
| `multi_dock_home_info` | array of struct | Per-dock return info. Multi-dock tasks only. Size 2. |
| `multi_dock_home_info[].sn` | string | Dock SN. |
| `multi_dock_home_info[].plan_status` | enum int | `0` = planning failed / in progress, `1` = unreachable, `2` = unreachable due to insufficient battery, `3` = destination reachable. |
| `multi_dock_home_info[].estimated_battery_consumption` | integer | Estimated battery use, percent. |
| `multi_dock_home_info[].home_distance` | float | Distance to home, meters. |

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "return_home_info",
  "timestamp": 1720000266772,
  "gateway": "6QCDL820020041",
  "data": {
    "flight_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
    "home_dock_sn": "6QCDL870020164",
    "last_point_type": 0,
    "multi_dock_home_info": [
      { "sn": "6QCDL870020164", "plan_status": 3, "estimated_battery_consumption": 30, "home_distance": 298.3277282714844 },
      { "sn": "6QCDL820020041", "plan_status": 3, "estimated_battery_consumption": 30, "home_distance": 298.289794921875 }
    ],
    "planned_path_points": [
      { "latitude": 22.755022128112614, "longitude": 114.89828051067889, "height": 60.285194396972656 },
      { "latitude": 22.755022128112614, "longitude": 114.89828051067889, "height": 88.22719192504883 },
      { "latitude": 22.75721542071551, "longitude": 114.89853624254465, "height": 88.22719192504883 }
    ]
  }
}
```

## Down (reply) — `data` fields

Standard events_reply envelope: `data.result` (integer; `0` = success). No additional output fields documented.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/50.wayline.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Wayline-Management.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-WaylineManagement.txt]` | v1.15 (Dock 3). |
