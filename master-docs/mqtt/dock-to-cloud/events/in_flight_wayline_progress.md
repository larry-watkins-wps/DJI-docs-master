# `in_flight_wayline_progress` — Virtual Cockpit route progress

Event pushed by the dock reporting progress of a flight route that was distributed in-flight via Virtual Cockpit (see the `in_flight_wayline_*` services family). Used to track lightweight, ad-hoc flight routes dispatched while the aircraft is already airborne — distinct from the main `flighttask_progress` event which covers pre-planned KMZ waylines.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, request-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** (likely). This method appears in v1.15 DJI_Cloud extracts for both Dock 2 and Dock 3 but has no counterpart in v1.11 Cloud-API-Doc/. The in-flight wayline / Virtual Cockpit feature as a whole was added in a v1.15-era release; Dock 2 may or may not have support depending on firmware. Flagged for Phase 10 annex if cohort confirmation differs.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `in_flight_wayline_progress` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `in_flight_wayline_progress` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `in_flight_wayline_id` | string | Flight route task ID — unique identifier for the in-flight wayline. |
| `progress` | object | Task progress block. |
| `progress.percent` | integer | Completion percent, `0`–`100`. |
| `status` | integer | Status code: `1` uploading, `2` uploaded, `3` in progress, `4` paused, `5` canceled, `6` ok, `7` failed, `8` timeout. |
| `result` | integer | Error reason code when `status=7`. |
| `way_point_index` | integer | Current waypoint index. |

### Example

```json
{
  "in_flight_wayline_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "progress": {
    "percent": 100
  },
  "status": 0,
  "result": 0,
  "way_point_index": 0
}
```

> **Note on envelope.** DJI's v1.15 example for this method is shown bare (without the outer `{tid, bid, timestamp, method, data}` envelope). Treat it as the `data` body; the standard envelope fields still wrap it on the wire.

## Down (reply) — `data` fields

Standard events_reply envelope: `data.result` (integer; `0` = success).

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-WaylineManagement.txt]` | v1.15 (Dock 3) — only source documenting this method. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Wayline-Management.txt]` | v1.15 (Dock 2) — documents the same method. No v1.11 Dock 2 counterpart. |
