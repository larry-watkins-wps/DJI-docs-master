# `flighttask_prepare` — issue (prepare) a mission

Cloud command that delivers a wayline mission to the device. The device downloads the KMZ file from the provided URL, validates it against `ready_conditions` (for conditional missions) and `executable_conditions`, then either fires [`flighttask_ready`](../events/flighttask_ready.md) (for conditional missions) or awaits [`flighttask_execute`](flighttask_execute.md) (for immediate / timed missions).

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload. Dock 3 adds an `altitude` field to `simulate_mission` (v1.11 Dock 2 did not document this).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `flighttask_prepare` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `flighttask_prepare` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `flight_id` | string | Task ID. |
| `task_type` | enum int | `0` immediate, `1` timed, `2` conditional. |
| `execute_time` | integer (ms) | Start time. Required when `task_type=0` or `task_type=1`; optional for `task_type=2`. |
| `file` | struct | `{url, fingerprint}` — wayline KMZ location + MD5. |
| `ready_conditions` | struct | Required when `task_type=2`. `{battery_capacity, begin_time, end_time}`. Device periodically checks; fires `flighttask_ready` when all met. |
| `executable_conditions` | struct | Pre-execution check. `{storage_capacity}` — minimum free storage required. |
| `break_point` | struct | Optional. `{index, state, progress, wayline_id}` — resume from breakpoint. |
| `rth_altitude` | integer (m) | Return-home altitude. Range: `20`–`1500`. |
| `rth_mode` | enum int | `0` optimal, `1` preset. |
| `out_of_control_action` | enum int | `0` return, `1` hover, `2` land. Current fixed value is `0`. |
| `exit_wayline_when_rc_lost` | enum int | `0` continue wayline, `1` exit wayline and execute RC-lost action. |
| `wayline_precision_type` | enum int | `0` GPS mission, `1` high-precision RTK mission. |
| `simulate_mission` | struct | Optional. `{is_enable, latitude, longitude, altitude}` — run mission in indoor simulator (propellers should be removed). |
| `flight_safety_advance_check` | boolean (0/1) | Pre-check flight-safety files vs cloud. `0` disabled (default), `1` enabled — pulls updated files if local differs. |

### Full enum / range notes

- `task_type` semantics: immediate tasks execute at `execute_time`; timed tasks also wait for `execute_time`; conditional tasks execute as soon as `ready_conditions` are all met within the `begin_time` / `end_time` window. Media upload priority differs: immediate = highest, timed/conditional = equal (lower).
- `rth_mode`: DJI Dock currently supports only Preset mode (`1`). Optimal is listed but not selectable on dock.

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "flighttask_prepare",
  "timestamp": 1234567890123,
  "data": {
    "flight_id": "xxxxxxx",
    "task_type": 2,
    "execute_time": 1234567890123,
    "file": {
      "url": "https://xxx.com/xxxx",
      "fingerprint": "xxxx"
    },
    "ready_conditions": {
      "battery_capacity": 90,
      "begin_time": 1234567890123,
      "end_time": 1234567890123
    },
    "executable_conditions": {
      "storage_capacity": 1000
    },
    "break_point": {
      "index": 1,
      "state": 0,
      "progress": 0.34,
      "wayline_id": 0
    },
    "rth_altitude": 100,
    "out_of_control_action": 0,
    "exit_wayline_when_rc_lost": 0,
    "wayline_precision_type": 0,
    "simulate_mission": {
      "is_enable": 1,
      "latitude": 22.1223,
      "longitude": 113.2222,
      "altitude": 66.6
    },
    "flight_safety_advance_check": 1
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
  "method": "flighttask_prepare",
  "timestamp": 1234567890123,
  "data": { "result": 0 }
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/50.wayline.md]` | v1.11 canonical (Dock 2) — no `simulate_mission.altitude` field in v1.11. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Wayline-Management.txt]` | v1.15 (Dock 2) — adds `simulate_mission.altitude`. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-WaylineManagement.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
