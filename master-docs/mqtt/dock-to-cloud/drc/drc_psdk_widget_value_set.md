# `drc_psdk_widget_value_set` — set PSDK generic widget value

DRC command that sets the value of a generic PSDK widget (switch, slider, etc.) identified by its widget index. The semantics of the integer `value` are defined by the PSDK developer (a switch might use `0/1`, a slider `0`–`100`, etc.).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — PSDK payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_psdk_widget_value_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_psdk_widget_value_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `psdk_index` | int | PSDK payload device index. |
| `index` | int | Widget number (assigned by the PSDK developer). |
| `value` | int | Widget value — semantics defined by the PSDK developer (switch state, slider position, etc.). |

### Example

```json
{
  "data": {
    "index": 1,
    "psdk_index": 1,
    "value": 60
  },
  "method": "drc_psdk_widget_value_set",
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
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — only source. |
