# `poi_mode_enter` — enter POI (Point of Interest) circle mode

Cloud command that puts the aircraft into Point-of-Interest circle mode. The aircraft begins circling a latitude / longitude / height point at a pilot-configurable radius and speed. Circle state is reported back via [`poi_status_notify`](../events/poi_status_notify.md).

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.** Not present on RC Pro's pilot-to-cloud surface. No v1.11 counterpart.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `poi_mode_enter` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `poi_mode_enter` |

## Down — `data` fields

| Field | Type | Constraint | Description |
|---|---|---|---|
| `latitude` | double | `{max: 90, min: -90}` | Destination point latitude in degrees. Negative = south, positive = north. Accurate to 6 decimal places. |
| `longitude` | double | `{max: 180, min: -180}` | Destination point longitude in degrees. Positive = east, negative = west. Accurate to 6 decimal places. |
| `height` | float | `{max: 10000, min: 2, step: 0.1, unit: "Meters / m"}` | Destination-point altitude (ellipsoidal height), relative to the takeoff point. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "height": 100,
    "latitude": 12.23,
    "longitude": 12.23
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "poi_mode_enter"
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero = error. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "result": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "poi_mode_enter"
}
```

## Relationship to other methods

- Call sequence: `poi_mode_enter` (set target) → [`poi_status_notify`](../events/poi_status_notify.md) events report entry + live status → [`poi_circle_speed_set`](poi_circle_speed_set.md) adjusts speed mid-circle → [`poi_mode_exit`](poi_mode_exit.md) leaves POI.
- POI mode is mutually exclusive with other flight-control modes (flyto, wayline, DRC stick). The cloud should hold flight authority (see [`cloud_control_auth_request`](cloud_control_auth_request.md)) before issuing `poi_mode_enter`.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Flight-Controls.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |
