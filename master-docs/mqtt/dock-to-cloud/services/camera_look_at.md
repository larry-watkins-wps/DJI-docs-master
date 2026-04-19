# `camera_look_at` — look at geographic point

Cloud command that rotates the aircraft and gimbal so the selected camera points at a geographic target (latitude, longitude, height). DJI notes: for the M30 / M30T (out of scope for this corpus — documented here because the method is shared with in-scope cohorts), it is recommended to lock the heading; if the gimbal rotates only to its limit, an exception may occur.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `camera_look_at` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `camera_look_at` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration (`{type}-{subtype}-{gimbalindex}`). |
| `locked` | boolean | Heading-gimbal lock. `false` = only gimbal turns; `true` = aircraft heading locked with gimbal so both turn together. |
| `latitude` | double | Target latitude, range `[-90, 90]`, 6-decimal precision. |
| `longitude` | double | Target longitude, range `[-180, 180]`, 6-decimal precision. |
| `height` | float (m) | Target point ellipsoid height (WGS84). Range `2`–`10000`, step `0.1`. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "height": 100,
    "latitude": 12.23,
    "locked": true,
    "longitude": 12.23,
    "payload_index": "39-0-7"
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "camera_look_at"
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
  "method": "camera_look_at"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
