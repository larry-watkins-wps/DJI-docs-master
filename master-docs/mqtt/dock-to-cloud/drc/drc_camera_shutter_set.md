# `drc_camera_shutter_set` — set camera shutter speed

DRC command that sets the shutter speed on the selected lens. Integer-keyed enum where keys `0`–`59` map to shutter speeds from `1/8000 s` to `8.0 s`, plus an Auto value. The key used for Auto diverges between cohorts — see [Source differences](#source-differences).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload shape; Auto-value key diverges.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_camera_shutter_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_shutter_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration. |
| `camera_type` | enum string | `wide` = Wide-angle; `zoom` = Zoom. |
| `shutter_value` | enum int | Keys `0`–`59` map to `1/8000 s` → `8.0 s` in the declared order (see DJI source for the full table — too long to restate). Cohort-dependent Auto value: **Dock 3** uses `60` = Auto; **Dock 2 + v1.11** use `65534` = Auto. |

### Example (Dock 3)

```json
{
  "data": {
    "shutter_value": 5,
    "camera_type": "zoom",
    "payload_index": "39-0-7"
  },
  "method": "drc_camera_shutter_set",
  "seq": 1
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

### Example

```json
{
  "data": {
    "result": 0
  },
  "method": "drc_camera_shutter_set",
  "seq": 1
}
```

## Source differences

- **Auto-value enum key diverges**: Dock 2 + v1.11 use `65534` = Auto; Dock 3 uses `60` = Auto. A server targeting both cohorts must emit the cohort-correct value.

## Source inconsistencies flagged by DJI's own example

- **Dock 2 v1.15 example carries `method: drc_camera_aperture_value_set`** in the down-side example (at L922 of `DJI_CloudAPI-Dock2-Remote-Control.txt`) despite the section being for `drc_camera_shutter_set`. Copy-paste error. Dock 3 example has the correct `method` name.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/180.remote-control.md]` | v1.11 canonical (Dock 2) — Auto = `65534`. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Control.txt]` | v1.15 (Dock 2) — Auto = `65534`; wrong method name in down example. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — Auto = `60`. |
