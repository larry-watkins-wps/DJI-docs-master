# `drc_camera_dewarping_set` — enable / disable lens dewarp

DRC command that enables or disables lens-distortion correction (dewarp) on the wide-angle lens (M3D / M4D). When enabled, eliminates vignetting in wide-angle view.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_camera_dewarping_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_dewarping_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration. |
| `camera_type` | enum string | `wide` = Wide-angle (only supported camera type). |
| `dewarping_state` | enum int | `0` = Disabled; `1` = Enabled. |

### Example

```json
{
  "data": {
    "camera_type": "wide",
    "dewarping_state": 1,
    "payload_index": "39-0-7"
  },
  "method": "drc_camera_dewarping_set",
  "seq": 1
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/180.remote-control.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Control.txt]` | v1.15 (Dock 2) — identical. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — identical. |
