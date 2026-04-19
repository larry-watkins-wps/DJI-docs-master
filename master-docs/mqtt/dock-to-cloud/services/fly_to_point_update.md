# `fly_to_point_update` — update flyto target point

Cloud command that replaces the current flyto target mid-flight (either a [`fly_to_point`](fly_to_point.md) in progress or a [`takeoff_to_point`](takeoff_to_point.md) in progress). The aircraft reroutes to the updated target without completing the original leg.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `fly_to_point_update` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `fly_to_point_update` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `max_speed` | integer (m/s) | Maximum achievable speed during live flight controls. Range `1`–`15`. |
| `points` | array of struct | Updated target-point list. **Only one point is supported.** |
| `points[].latitude` | double | Latitude, range `[-90, 90]`, 6-decimal precision. |
| `points[].longitude` | double | Longitude, range `[-180, 180]`, 6-decimal precision. |
| `points[].height` | float (m) | Target point ellipsoid height (WGS84). Range `2`–`10000`, step `0.1`. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
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
  "method": "fly_to_point_update"
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
  "method": "fly_to_point_update"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
