# `fly_to_point` — fly to target point

Cloud command that directs an airborne aircraft to fly to a single target point (not a mission; the aircraft must already be in flight). A minimum-altitude safety guarantee is enforced: if the aircraft's altitude relative to the takeoff point is below 20 m, the aircraft first climbs to 20 m. Progress is reported by [`fly_to_point_progress`](../events/fly_to_point_progress.md); the target can be updated mid-flight with [`fly_to_point_update`](fly_to_point_update.md) and cancelled with [`fly_to_point_stop`](fly_to_point_stop.md).

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `fly_to_point` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `fly_to_point` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `fly_to_id` | string | Flyto target-point ID (echoed by `fly_to_point_progress`). |
| `max_speed` | integer (m/s) | Maximum achievable flyto speed. Range `0`–`15`. |
| `points` | array of struct | Target-point list. **Only one point is supported.** |
| `points[].latitude` | double | Latitude, range `[-90, 90]`, 6-decimal precision. |
| `points[].longitude` | double | Longitude, range `[-180, 180]`, 6-decimal precision. |
| `points[].height` | float (m) | Target point ellipsoid height (WGS84). Range `2`–`10000`, step `0.1`. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "fly_to_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
    "max_speed": 12,
    "points": [
      {
        "height": 100,
        "latitude": 12.23,
        "longitude": 12.23
      }
    ]
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "fly_to_point"
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
  "data": { "result": 0 },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "fly_to_point"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
