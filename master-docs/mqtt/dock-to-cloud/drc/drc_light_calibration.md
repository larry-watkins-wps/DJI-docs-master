# `drc_light_calibration` — trigger PSDK spotlight gimbal calibration

DRC command that starts gimbal calibration on a PSDK spotlight payload. Calibration status / progress is reported back via [`drc_psdk_state_info.light.calibration_status`](drc_psdk_state_info.md) and `light.calibration_progress`.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — PSDK spotlight payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_light_calibration` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_light_calibration` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `psdk_index` | int | PSDK payload device index. |

### Example

```json
{
  "data": {
    "psdk_index": 1
  },
  "method": "drc_light_calibration",
  "seq": 1
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

## Relationship to other methods

- Progress / result visible via [`drc_psdk_state_info`](drc_psdk_state_info.md) `light.calibration_status` (`0` Complete / `1` Calibrating / `2` Failed) and `light.calibration_progress`.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — only source. |
