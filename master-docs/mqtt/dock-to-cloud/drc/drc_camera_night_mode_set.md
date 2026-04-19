# `drc_camera_night_mode_set` — set M4D / M4TD camera night mode

DRC command that sets the night-mode state on the M4D / M4TD camera. In auto mode, the camera switches between day and night modes automatically based on ambient light.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — M4D / M4TD cameras.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_camera_night_mode_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_night_mode_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration. DJI recommends `98-0-0` (M4D) or `99-0-0` (M4TD). |
| `mode` | enum int | `0` = Disabled (see [Source inconsistencies](#source-inconsistencies-flagged-by-djis-own-example)); `1` = Enabled; `2` = Auto. |

### Example

```json
{
  "seq": 1,
  "method": "drc_camera_night_mode_set",
  "data": {
    "payload_index": "99-0-0",
    "mode": 0
  }
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

## Source inconsistencies flagged by DJI's own example

- **`mode` enum lists `{"0":"Enabled","1":"Enabled","2":"Auto"}`** — two keys both labeled "Enabled". Almost certainly a DJI typo: key `0` should read "Disabled" (matching the `is_working` / `night_mode` conventions elsewhere). Treat `0` as Disabled, `1` as Enabled, `2` as Auto.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — only source. |
