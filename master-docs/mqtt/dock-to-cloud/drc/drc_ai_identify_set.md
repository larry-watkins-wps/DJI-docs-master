# `drc_ai_identify_set` — enable / disable AI recognition globally

DRC command that turns AI recognition on or off globally. When disabled, the device stops running the selected model. The current state is observable via [`drc_ai_info_push.identify_on`](drc_ai_info_push.md).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — AI identify subsystem.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_ai_identify_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_ai_identify_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `on` | enum int | `0` = off; `1` = on. |

### Example

```json
{
  "seq": 1,
  "method": "drc_ai_identify_set",
  "data": {
    "on": 1
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
