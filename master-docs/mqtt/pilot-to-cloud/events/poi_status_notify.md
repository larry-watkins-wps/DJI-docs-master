# `poi_status_notify` — POI circle status

RC-side notification reporting the current state of a Point-of-Interest circle flight, including live radius, circle speed, maximum circle speed, and entry/exit reason. Emitted periodically while POI mode is active and at state transitions (entry, exit, error).

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.** No v1.11 counterpart (RC Plus 2 is a v1.15 addition; POI mode is not exposed on RC Pro's pilot-to-cloud MQTT surface).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `poi_status_notify` |

`need_reply: 1` — cloud must reply with `{"result": 0}` on `/events_reply`.

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `status` | enum_string | `{"failed": "Failed", "in_progress": "In Progress", "ok": "Success"}`. |
| `reason` | integer enum | Entry/exit reason. `0` = Normal (in-progress, no exit). Values `1..12` are in-progress status causes; values `160..168` are exit reasons. See full enum below. |
| `circle_radius` | float | Current circle radius, in meters. |
| `circle_speed` | float | Current circle speed, in meters/second. Sign: negative = clockwise, positive = counterclockwise. |
| `max_circle_speed` | float | Maximum allowed circle speed at the current radius/height/payload combination, in meters/second. Used as the upper bound for [`poi_circle_speed_set`](../services/poi_circle_speed_set.md). |

### `reason` enum (full)

In-progress causes (status stays `in_progress`):

| Value | Meaning |
|---|---|
| 0 | Normal |
| 1 | Too close to subject |
| 2 | Too far from subject |
| 3 | Reached min altitude |
| 4 | Reached max altitude |
| 5 | Reached max distance |
| 6 | Approaching GEO Zone |
| 7 | Gimbal movement reached limit |
| 8 | Aircraft yaw reached limit for POI (±80°) |
| 9 | Obstacle too close |
| 10 | Positioning source switched (from GPS to RTK), POI Paused |
| 11 | Positioning source switched (from RTK to GPS) |
| 12 | Obstacle sensing unavailable |

Exit reasons (status `failed` or session end):

| Value | Meaning |
|---|---|
| 160 | Normal exit |
| 161 | Payload not compatible |
| 162 | Camera mode not supported (Panorama, High-Res Grid, AI Spot-Check, etc.) |
| 163 | Illegal command |
| 164 | Positioning unavailable |
| 165 | Aircraft not taken off |
| 166 | Flight mode error. Only N mode available |
| 167 | Not available in this mode (RTH, landing, attitude mode) |
| 168 | Lost remote control or video transmission signal |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "circle_radius": 10.1,
    "circle_speed": 100.1,
    "max_circle_speed": 200.2,
    "reason": 0,
    "status": "in_progress"
  },
  "need_reply": 1,
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 16540709686556,
  "method": "poi_status_notify"
}
```

### Source inconsistencies flagged by DJI's own example

- **14-digit timestamp.** DJI's example ships `"timestamp": 16540709686556` (14 digits) instead of 13-digit epoch-ms. Matches the 4f pervasive 14-digit pattern across CFA / AirSense. Cloud implementations should emit/accept 13-digit ms.
- **`status: "in_progress"` paired with `circle_speed: 100.1`** in the example — while `max_circle_speed: 200.2`. In a real POI the circle speed should be well within the max; the literal values here are illustrative only.
- **Example `reason: 0` paired with `in_progress`** is consistent with the enum (`0` = Normal).

## Relationship to other methods

- Paired with [`poi_mode_enter`](../services/poi_mode_enter.md) (start POI about a lat/lon/height), [`poi_mode_exit`](../services/poi_mode_exit.md) (leave POI), and [`poi_circle_speed_set`](../services/poi_circle_speed_set.md) (tune circle speed). A cloud orchestrating POI should subscribe to this event to know when the aircraft is actually in circle state vs transitioning vs constrained.
- `reason` values 1–12 overlap semantics with the dock-to-cloud in-flight-wayline `break_reason` enum; treat as advisory rather than normative.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Flight-Controls.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |
