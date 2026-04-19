# `drc_light_mode_set` — set PSDK spotlight operating mode

DRC command that sets the PSDK spotlight's operating mode. Only one mode is currently documented (`1 = Constant`).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — PSDK spotlight payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_light_mode_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_light_mode_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `psdk_index` | int | PSDK payload device index. |
| `group` | enum int | `0` = Main light; `1` = Auxiliary light. |
| `mode` | enum int | `1` = Constant (the only defined mode). Future modes may be added. |

### Example

```json
{
  "data": {
    "group": 0,
    "mode": 1,
    "psdk_index": 1
  },
  "method": "drc_light_mode_set",
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
