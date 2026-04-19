# `camera_point_focus_action` — spot autofocus

Cloud command that triggers a spot-AF action at a specific pixel coordinate within the camera's field of view — equivalent to tap-to-focus on the Pilot viewfinder.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `camera_point_focus_action` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `camera_point_focus_action` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration (`{type}-{subtype}-{gimbalindex}`). |
| `camera_type` | enum string | Lens. `wide` = wide-angle, `zoom` = zoom. Note: on Matrice 30 series (out of scope here) this parameter is only settable on the zoom lens. |
| `x` | double | Focus-point x, origin at lens upper-left, horizontal axis. Range `[0, 1]`. |
| `y` | double | Focus-point y, origin at lens upper-left, vertical axis. Range `[0, 1]`. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "camera_type": "zoom",
    "payload_index": "39-0-7",
    "x": 0.5,
    "y": 0.5
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "camera_point_focus_action"
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
  "method": "camera_point_focus_action"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
