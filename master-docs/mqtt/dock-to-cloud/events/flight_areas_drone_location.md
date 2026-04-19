# `flight_areas_drone_location` — aircraft custom-flight-area distance push

Event pushed by the dock reporting the aircraft's geometric relationship to the custom flight areas currently loaded on the aircraft. For every loaded area, the aircraft reports whether it is inside the area and its distance to the nearest boundary. Cloud uses this for geofence visualization and for issuing operator-facing alerts.

`need_reply: 0` — fire-and-forget push.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `flight_areas_drone_location` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `drone_locations` | array&lt;struct&gt; | One entry per loaded custom flight area. |
| `drone_locations[].area_id` | string | Unique ID of the custom flight area. Matches `files[].name` stem returned by [`flight_areas_get`](../requests/flight_areas_get.md) / embedded in the geofence file itself. |
| `drone_locations[].area_distance` | float | Distance (meters) from the aircraft to the nearest point on the area boundary. |
| `drone_locations[].is_in_area` | boolean | `true` = aircraft is inside the area; `false` = outside. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "drone_locations": [
      {
        "area_distance": 100.11,
        "area_id": "d275c4e1-d864-4736-8b5d-5f5882ee9bdd",
        "is_in_area": true
      }
    ]
  },
  "method": "flight_areas_drone_location",
  "need_reply": 0,
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 16540709686556
}
```

## Relationship to other methods

- Areas loaded on the aircraft originate from [`flight_areas_get`](../requests/flight_areas_get.md) (dock fetches the file list + URLs from the cloud).
- The cloud can force a fresh sync by issuing [`flight_areas_update`](../services/flight_areas_update.md); sync progress is reported via [`flight_areas_sync_progress`](flight_areas_sync_progress.md).
- Full Custom-Flight-Area choreography will be documented in Phase 9 workflow `workflows/flysafe-custom-flight-area-sync.md`.

## Source inconsistencies flagged by DJI's own example

- **Dock 3 v1.15 schema table omits `area_id`** from the `drone_locations` struct, yet the example carries it. Dock 2 v1.11 + Dock 2 v1.15 tables both list `area_id`. Treat the field as authoritative on the wire; the Dock 3 omission is a source-extraction bug.
- **Timestamp width.** Every DJI source example shows `"timestamp": 16540709686556` — 14 digits. Canonical MQTT timestamps in the corpus are 13-digit epoch-milliseconds (`1654070968655`); the extra digit is a DJI source typo pervasive across v1.11 and v1.15 Custom-Flight-Area + AirSense + HMS example payloads. Cloud implementations should emit/accept 13-digit ms timestamps.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/130.custom-flight-area.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Custom-Flight-Area.txt]` | v1.15 (Dock 2) — identical payload. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Custom-Flight-Area.txt]` | v1.15 (Dock 3) — identical payload; `area_id` row dropped from the extracted table but present in the example. |
