# `airsense_warning` — ADS-B proximity warning

Event pushed by the aircraft (via the dock) reporting the presence of a nearby crewed airplane detected over ADS-B. Each warning carries the intruder's ICAO identifier, a five-level severity classification, its position, heading, relative altitude, vertical trend, and horizontal distance from the aircraft. Cloud uses this to raise operator alerts and — at levels `3` and above — potentially to trigger avoidance logic.

`need_reply: 1` — cloud must acknowledge with `{"result": 0}` on `events_reply`.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, events-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `airsense_warning` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `airsense_warning` |

## Up — `data` fields

**Note:** `data` is an **array of warning structs**, not a single struct. Each element represents one detected airplane.

| Field | Type | Description |
|---|---|---|
| `icao` | string | ICAO aircraft (civil aviation) address — unique identifier of the detected airplane. |
| `warning_level` | enum int | `0` = No danger; `1` = Level One; `2` = Level Two; `3` = Level Three; `4` = Level Four. Severity rises with the number; levels ≥ `3` should trigger avoidance. |
| `latitude` | float | Detected airplane latitude. Negative = south, positive = north. Precision: 6 decimal places. Range `[-90, 90]`. |
| `longitude` | float | Detected airplane longitude. Negative = west, positive = east. Precision: 6 decimal places. Range `[-180, 180]`. |
| `altitude` | integer | Absolute altitude of the detected airplane (meters). Interpretation: see `altitude_type`. |
| `altitude_type` | enum int | `0` = Ellipsoidal altitude; `1` = Altitude above sea level. |
| `heading` | float | Heading in degrees. `0` = true north, `90` = true east. Precision: 1 decimal place. |
| `relative_altitude` | integer | Relative altitude of the detected airplane above (positive) or below (negative) the aircraft, meters. |
| `vert_trend` | enum int | `0` = relative altitude unchanged; `1` = relative altitude increasing (closing vertically); `2` = relative altitude decreasing. |
| `distance` | integer | Horizontal distance between the detected airplane and the aircraft, meters. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": [
    {
      "altitude": 100,
      "altitude_type": 1,
      "distance": 100,
      "heading": 89.1,
      "icao": "B-5931",
      "latitude": 12.23,
      "longitude": 12.23,
      "relative_altitude": 80,
      "vert_trend": 0,
      "warning_level": 3
    }
  ],
  "need_reply": 1,
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 16540709686556,
  "method": "airsense_warning"
}
```

## Down (reply) — `data` fields

Standard events_reply envelope: `data.result` (integer; `0` = success).

## Source differences

- **`warning_level` name change.** v1.11 Dock 2 and v1.15 Dock 2 label the field "Alarm level"; v1.15 Dock 3 (hand-authored) labels it "Warning level". Enum values (`0`–`4`) are stable; the change is cosmetic.
- **`data` shape is an array, not a struct.** Unusual for this corpus — most events nest their content under a struct. Every source shows the bare array and no example ever ships more than one element, but the shape is a list to allow multi-intruder reporting.

## Source inconsistencies flagged by DJI's own example

- **Timestamp width.** Example shows `"timestamp": 16540709686556` — 14 digits. See [`flight_areas_drone_location`](flight_areas_drone_location.md#source-inconsistencies-flagged-by-djis-own-example) for the shared note — pervasive across the 4f source family.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/120.airsense.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-AirSense.txt]` | v1.15 (Dock 2) — identical payload, "Alarm level" label. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-AirSense.txt]` | v1.15 (Dock 3, hand-authored) — identical payload, "Warning level" label, adds `warning_level` level-`3`-avoidance note. |
