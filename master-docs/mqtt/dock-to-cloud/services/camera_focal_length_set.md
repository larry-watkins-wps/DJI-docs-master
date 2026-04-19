# `camera_focal_length_set` — zoom (set focal length)

Cloud command that sets the zoom factor on the selected camera lens.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `camera_focal_length_set` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `camera_focal_length_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration (`{type}-{subtype}-{gimbalindex}`). |
| `camera_type` | enum string | Lens. `ir` = infrared, `wide` = wide-angle, `zoom` = zoom. |
| `zoom_factor` | double | Zoom factor. Range `2`–`200` for visible light, `2`–`20` for infrared. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "camera_type": "zoom",
    "payload_index": "39-0-7",
    "zoom_factor": 5
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "camera_focal_length_set"
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
  "method": "camera_focal_length_set"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
