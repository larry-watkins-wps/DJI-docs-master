# `poi_circle_speed_set` — set POI circle speed

Cloud command that adjusts the circle speed during an active POI (Point of Interest) flight. The sign of `circle_speed` selects rotation direction: negative = clockwise, positive = counterclockwise. The upper magnitude bound is whatever the current `max_circle_speed` is (see [`poi_status_notify`](../events/poi_status_notify.md)).

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.** Not present on RC Pro. No v1.11 counterpart.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `poi_circle_speed_set` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `poi_circle_speed_set` |

## Down — `data` fields

| Field | Type | Constraint | Description |
|---|---|---|---|
| `circle_speed` | float | `{max: "max_circle_speed from poi_status_notify", unit: "Meters per second / m/s"}` | Target circle speed. Negative = clockwise, positive = counterclockwise. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "circle_speed": 5.2
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "poi_circle_speed_set"
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero = error (e.g., speed exceeds current `max_circle_speed`, aircraft not in POI mode). |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "result": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "poi_circle_speed_set"
}
```

## Relationship to other methods

- Must be called while in POI mode (after [`poi_mode_enter`](poi_mode_enter.md) and before [`poi_mode_exit`](poi_mode_exit.md)).
- The `max_circle_speed` bound is dynamic — it depends on current circle radius, aircraft height, and payload. Read it from the latest [`poi_status_notify`](../events/poi_status_notify.md) event before issuing this command.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Flight-Controls.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |
