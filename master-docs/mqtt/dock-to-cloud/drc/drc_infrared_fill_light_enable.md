# `drc_infrared_fill_light_enable` — enable / disable near-infrared fill light

DRC command that turns the near-infrared fill light on or off on the M4TD camera. Only effective when the zoom ratio is 7× or higher — same constraint as [`drc_camera_night_vision_enable`](drc_camera_night_vision_enable.md).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — M4TD camera.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_infrared_fill_light_enable` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_infrared_fill_light_enable` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration. DJI recommends `99-0-0` (M4TD). |
| `enable` | bool | `true` = enable, `false` = disable. Takes effect only at zoom ≥ 7×. |

### Example

```json
{
  "seq": 1,
  "method": "drc_infrared_fill_light_enable",
  "data": {
    "payload_index": "99-0-0",
    "enable": true
  }
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — only source. |
