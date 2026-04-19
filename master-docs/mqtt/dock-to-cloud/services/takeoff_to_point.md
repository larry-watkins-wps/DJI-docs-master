# `takeoff_to_point` — one-key takeoff

Cloud command that tells the aircraft to take off from the dock and fly to a target point in a single compound operation. Unlike a wayline mission, this is an ad-hoc flight initiated from the cloud. Completion / progress is reported by [`takeoff_to_point_progress`](../events/takeoff_to_point_progress.md).

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `takeoff_to_point` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `takeoff_to_point` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `target_latitude` | double | Target latitude. Range `[-90, 90]`, 6-decimal precision. |
| `target_longitude` | double | Target longitude. Range `[-180, 180]`, 6-decimal precision. |
| `target_height` | float (m) | Target point ellipsoid height (WGS84). Range `2`–`1500`, step `0.1`. Default post-arrival behavior is hover. |
| `security_takeoff_height` | float (m) | Safe-takeoff height — relative altitude above the dock the aircraft climbs to before flying to target. Range `20`–`1500`, step `0.1`. |
| `rth_mode` | enum int | **Required.** Return-home mode. `0` = intelligent altitude, `1` = preset altitude. DJI Dock currently supports preset altitude only; intelligent altitude cannot be selected. |
| `rth_altitude` | integer (m) | Return-home altitude relative to the dock. Range `2`–`1500`, step `1`. |
| `rc_lost_action` | enum int | RC-lost action. `0` = hovering, `1` = landing, `2` = returning to home. |
| `commander_mode_lost_action` | enum int | **Required.** To-point flight loss-of-control action. `0` = continue the to-point mission, `1` = exit the to-point mission and perform normal lost-control behavior. |
| `commander_flight_mode` | enum int | **Required.** To-point flight-mode setting. `0` = optimal-height flight, `1` = preset-height flight. |
| `commander_flight_height` | float (m) | **Required.** To-point flight height relative to the dock. Range `2`–`3000`, step `0.1`. |
| `flight_id` | string | One-key takeoff mission UUID. Globally unique; used by the cloud to color-code and distinguish a one-key mission from a regular planned wayline. |
| `max_speed` | integer (m/s) | Maximum achievable speed during one-key takeoff. Range `1`–`15`. |
| `simulate_mission` | struct | Optional. Indoor simulator harness. **Remove propellers before enabling** — the dock cover will close on them. |
| `simulate_mission.is_enable` | enum int | `0` = do not enable, `1` = enable. |
| `simulate_mission.latitude` | double | Simulated latitude, range `[-90.0, 90.0]`. |
| `simulate_mission.longitude` | double | Simulated longitude, range `[-180.0, 180.0]`. |
| `flight_safety_advance_check` | boolean (0/1) | Optional. Pre-check flight-safety files vs cloud. `0` disabled (default), `1` enabled — pulls updated files if local differs. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "flight_id": "ABDEAC21DCADDA",
    "max_speed": 12,
    "rc_lost_action": 0,
    "rth_altitude": 100,
    "security_takeoff_height": 100,
    "target_height": 100,
    "target_latitude": 12.23,
    "target_longitude": 12.32,
    "commander_mode_lost_action": 1,
    "commander_flight_height": 80,
    "flight_safety_advance_check": 1
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "takeoff_to_point"
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
  "method": "takeoff_to_point"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
