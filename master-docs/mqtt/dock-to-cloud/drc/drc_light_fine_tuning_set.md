# `drc_light_fine_tuning_set` — fine-tune PSDK spotlight per-side brightness

DRC command that fine-tunes the left- or right-light value on a PSDK spotlight (independent of the `drc_light_brightness_set` overall brightness). The `saved` flag controls whether the change persists through reboot.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — PSDK spotlight payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_light_fine_tuning_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_light_fine_tuning_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `psdk_index` | int | PSDK payload device index. |
| `position` | enum int | `0` = Left light; `1` = Right light. |
| `value` | int | Light value, `1`–`100`. |
| `saved` | bool | `true` = persist through reboot; `false` = session-only. |

### Example

```json
{
  "data": {
    "position": 0,
    "psdk_index": 1,
    "saved": false,
    "value": 1
  },
  "method": "drc_light_fine_tuning_set",
  "seq": 1
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

## Source inconsistencies flagged by DJI's own example

- **`saved` declared as `bool` with constraint `{"0":"No","1":"Yes"}` (int-keyed enum) but the example sends a literal JSON `false`.** Mixed-type declaration — same class of inconsistency seen in other `drc_*` bool fields. Accept either form.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — only source. |
