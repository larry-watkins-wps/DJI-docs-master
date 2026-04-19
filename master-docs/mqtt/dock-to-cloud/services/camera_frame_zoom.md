# `camera_frame_zoom` — subject-frame zoom

Cloud command that selects a rectangular target within the camera's field of view. The camera auto-zooms to frame the target and the gimbal adjusts so the target is centered.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `camera_frame_zoom` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `camera_frame_zoom` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration (`{type}-{subtype}-{gimbalindex}`, e.g. `39-0-7`). |
| `camera_type` | enum string | Lens. `ir` = infrared, `wide` = wide-angle, `zoom` = zoom. |
| `locked` | boolean | Heading-gimbal lock. `false` = only gimbal turns; `true` = aircraft heading locked with gimbal so both turn together. |
| `x` | float | Target-frame upper-left x, normalized `[0, 1]`, step `0.000001`. |
| `y` | float | Target-frame upper-left y, normalized `[0, 1]`, step `0.000001`. |
| `width` | float | Target-frame width, normalized `[0, 1]`, step `0.000001`. |
| `height` | float | Target-frame height, normalized `[0, 1]`, step `0.000001`. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "camera_type": "zoom",
    "height": 0.2,
    "locked": true,
    "payload_index": "39-0-7",
    "width": 0.2,
    "x": 0.5,
    "y": 0.5
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "camera_frame_zoom"
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": { "result": 0 },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "camera_frame_zoom"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
