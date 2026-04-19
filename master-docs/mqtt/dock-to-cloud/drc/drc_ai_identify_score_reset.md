# `drc_ai_identify_score_reset` — reset AI confidence to default

DRC command that resets the AI recognition confidence threshold to its default (whatever the selected score mode's default is). `Data: null`.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — AI identify subsystem.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_ai_identify_score_reset` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_ai_identify_score_reset` |

## Down — `data`

`Data: null`.

### Example

```json
{
  "seq": 1,
  "method": "drc_ai_identify_score_reset",
  "data": {
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
