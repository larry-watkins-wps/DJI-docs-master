# `drc_light_brightness_set` — set PSDK spotlight brightness

DRC command that sets the brightness on a PSDK spotlight payload. `group` selects which light (main or auxiliary) the command applies to. The `brightness` field is missing from DJI's schema table but is required by the example — see [Source inconsistencies](#source-inconsistencies-flagged-by-djis-own-example).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — PSDK spotlight payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_light_brightness_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_light_brightness_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `psdk_index` | int | PSDK payload device index. |
| `group` | enum int | `0` = Main light; `1` = Auxiliary light. |
| `brightness` | int | Brightness value. **Not declared in DJI's schema table but required by the example.** Range not documented — treat as `1`–`100` per the other light set-methods. |

### Example

```json
{
  "data": {
    "brightness": 1,
    "group": 0,
    "psdk_index": 1
  },
  "method": "drc_light_brightness_set",
  "seq": 1
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

## Source inconsistencies flagged by DJI's own example

- **`brightness` field missing from schema table.** The Dock 3 schema lists only `psdk_index` and `group`, but the example sends `brightness: 1`. The example is authoritative on the wire shape.
- **Reply example has wrong `method` key.** At L2111 of `DJI_CloudAPI-Dock3-Remote-Control.txt`, the reply example shows `"method": "drc_night_lights_state_set"` instead of `drc_light_brightness_set`. Copy-paste error in DJI's source.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — only source. |
