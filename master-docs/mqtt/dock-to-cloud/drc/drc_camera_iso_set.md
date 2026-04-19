# `drc_camera_iso_set` — set camera ISO

DRC command that sets the ISO value on the selected lens.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_camera_iso_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_iso_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration. |
| `camera_type` | enum string | `wide` = Wide-angle; `zoom` = Zoom. |
| `iso_value` | enum int | `0` = ISO_AUTO, `2` = 50, `3` = 100, `4` = 200, `5` = 400, `6` = 800, `7` = 1600, `8` = 3200, `9` = 6400, `10` = 12800, `11` = 25600, `12` = 51200, `13` = 102400, `255` = ISO_FIXED. Depending on the aircraft model, the supported range varies. |

### Example

```json
{
  "data": {
    "camera_type": "zoom",
    "iso_value": 5,
    "payload_index": "39-0-7"
  },
  "method": "drc_camera_iso_set",
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
