# `in_flight_wayline_deliver` — distribute a flight route in-flight (Virtual Cockpit)

Cloud command that pushes a lightweight flight route to the aircraft while it is already airborne. Part of the Virtual Cockpit feature that allows operators to dynamically task an in-air aircraft without returning it to dock. Paired with [`in_flight_wayline_stop`](in_flight_wayline_stop.md), [`in_flight_wayline_recover`](in_flight_wayline_recover.md), [`in_flight_wayline_cancel`](in_flight_wayline_cancel.md); progress is reported on [`events/in_flight_wayline_progress`](../events/in_flight_wayline_progress.md).

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **v1.15 addition** — documented for Dock 2 and Dock 3 in v1.15 extracts; no v1.11 counterpart. Cohort coverage depends on firmware.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `in_flight_wayline_deliver` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `in_flight_wayline_deliver` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `in_flight_wayline_id` | string | Flight route task ID — unique identifier. |
| `file` | object | Flight route file metadata. |
| `file.url` | string | Download URL for the flight route file. |
| `file.fingerprint` | string | File fingerprint for integrity verification. |
| `out_of_control_action` | enum int | RC-lost action: `0` = return to home, `1` = hover, `2` = land. |
| `exit_wayline_when_rc_lost` | enum int | `0` = continue, `1` = perform RC-lost action. |
| `rth_altitude` | integer | RTH altitude, meters. Range: `20`–`1500`. |
| `rth_mode` | enum int | `0` = optimal, `1` = preset. |
| `wayline_precision_type` | enum int | `0` = GPS, `1` = high-precision RTK. |

### Example

```json
{
  "tid": "a5d95abe-e99c-4931-95cc-e2f3fdbc488f",
  "bid": "d26db6b4-3bb0-432c-bdb2-a8e53c827b72",
  "method": "in_flight_wayline_deliver",
  "timestamp": 1731135221528,
  "data": {
    "in_flight_wayline_id": "f2b31c13-3fce-4a7e-b188-87a78ff2f8a6",
    "file": {
      "url": "XXXX",
      "fingerprint": "7a7cea5060c55920b7619a2a981f2223"
    },
    "out_of_control_action": 1,
    "exit_wayline_when_rc_lost": 0,
    "rth_altitude": 120,
    "rth_mode": 1,
    "wayline_precision_type": 1
  }
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success. |

### Example

```json
{ "result": 0 }
```

(DJI's v1.15 example shows the bare result body; standard envelope fields wrap it on the wire.)

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-WaylineManagement.txt]` | v1.15 (Dock 3) — primary. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Wayline-Management.txt]` | v1.15 (Dock 2) — same payload. No v1.11 counterpart. |
