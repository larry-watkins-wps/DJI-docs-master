# `flighttask_progress` — report task progress

Event pushed by the dock periodically during flight-task execution. Carries the wayline-mission state, current step within the dock's state machine, execution percentage, current waypoint index, optional breakpoint information (for resumable tasks), and the overall task status.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, request-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `flighttask_progress` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `flighttask_progress` |

## Up — `data` fields

The payload is wrapped by the events envelope in `data.output`, with `data.result` carrying the event-level result code (see [example](#example)).

### `output` fields

| Field | Type | Description |
|---|---|---|
| `status` | enum string | Overall task state. See **Status enum** below. |
| `ext` | struct | Extended progress detail — see **ext fields** below. |
| `progress` | struct | Step / percent progress within the dock's state machine. |
| `progress.current_step` | enum int | Current step. ~50 documented values (see **current_step enum** below). |
| `progress.percent` | integer | Percent complete, `0`–`100`. |

### `ext` fields

| Field | Type | Description |
|---|---|---|
| `flight_id` | string | Task ID. |
| `track_id` | string | Trajectory ID. |
| `current_waypoint_index` | integer | Waypoint index currently being executed. |
| `wayline_id` | integer | Currently-working wayline ID. `0` includes the transition phase into the first wayline. |
| `wayline_mission_state` | enum int | See **wayline_mission_state enum** below. |
| `media_count` | integer | Count of media files produced during the current task. |
| `break_point` | struct | Optional. Current breakpoint details, for resumable tasks. |
| `break_point.index` | integer | Breakpoint number. |
| `break_point.state` | enum int | `0` = on segment, `1` = on waypoint. |
| `break_point.progress` | float | Progress within the current segment, `0`–`1.0`. |
| `break_point.wayline_id` | integer | Wayline ID at breakpoint. |
| `break_point.break_reason` | enum int | Reason the task broke — ~100 enumerated values documented by DJI. See note below. |
| `break_point.latitude` | float | Breakpoint latitude. |
| `break_point.longitude` | float | Breakpoint longitude. |
| `break_point.height` | float | Breakpoint height, meters. |
| `break_point.attitude_head` | float | Breakpoint yaw axis angle, degrees. |

### Status enum

| Value | Meaning |
|---|---|
| `sent` | Issued to the device. |
| `in_progress` | Executing. |
| `paused` | Paused. |
| `ok` | Executed successfully. |
| `partially_done` | Partially completed. |
| `canceled` | Cancelled or terminated. |
| `rejected` | Rejected by device. |
| `failed` | Failed. |
| `timeout` | Timed out. |

### `wayline_mission_state` enum

| Value | Meaning |
|---|---|
| `0` | Disconnected. |
| `1` | This waypoint is not supported. |
| `2` | Wayline preparation state. Can upload files and execute existing files. |
| `3` | Wayline file uploading. |
| `4` | Trigger start command received; aircraft reading the wayline; task not yet started. |
| `5` | Entering the wayline, heading to the first waypoint. |
| `6` | Wayline execution. |
| `7` | Wayline interrupted. Triggered by user pause or flight-control abnormality. |
| `8` | Wayline recovery. |
| `9` | Wayline stopped (v1.15) / Wayline completed (v1.11). |

### `progress.current_step` enum

Approximately 50 values covering the dock's state machine: pre-flight checks, aircraft takeoff parameter setting, home point setting, wayline execution trigger, landing, cover closure, dock mode exit, log retrieval, etc. Full enum table lives in the source files (lines 208 of `DJI_CloudAPI-Dock3-WaylineManagement.txt`). Not restated here to avoid drift; verify against source when a specific value is load-bearing.

### `break_reason` enum

Approximately 100 values spanning protocol errors, aircraft-state errors, environmental conditions (GPS, RTK, wind, obstacle sensing), flight-safety triggers, and resume-from-breakpoint issues. The source file lists them verbatim. Full reference in Phase 8 (`error-codes/`) when that catalog lands.

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "flighttask_progress",
  "timestamp": 1654070968655,
  "data": {
    "result": 0,
    "output": {
      "status": "ok",
      "ext": {
        "flight_id": "flight_id",
        "track_id": "track_id",
        "current_waypoint_index": 3,
        "wayline_id": 0,
        "wayline_mission_state": 9,
        "media_count": 6,
        "break_point": {
          "index": 1,
          "state": 0,
          "progress": 0.34,
          "wayline_id": 0,
          "break_reason": 1,
          "latitude": 23.4,
          "longitude": 113.99,
          "height": 100.23,
          "attitude_head": 30
        }
      },
      "progress": {
        "current_step": 19,
        "percent": 100
      }
    }
  }
}
```

## Down (reply) — `data` fields

Standard events_reply envelope: `data.result` (integer; `0` = success).

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/50.wayline.md]` | v1.11 canonical (Dock 2) — `wayline_mission_state=9` labeled "Wayline completed" in v1.11. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Wayline-Management.txt]` | v1.15 (Dock 2) — `wayline_mission_state=9` labeled "Wayline stopped". Minor enum-label drift. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-WaylineManagement.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
