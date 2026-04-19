# `drc_ai_identify_score_set` — set custom AI recognition confidence score

DRC command that sets the AI confidence threshold when `score_mode = Custom` (set by [`drc_ai_identify_score_mode_set`](drc_ai_identify_score_mode_set.md)). Ignored in other modes.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — AI identify subsystem.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_ai_identify_score_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_ai_identify_score_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `score` | int | Confidence score, `0`–`100`, step `1`. Only effective when `score_mode = 3` (Custom). |

### Example

```json
{
  "seq": 1,
  "method": "drc_ai_identify_score_set",
  "data": {
    "score": 100
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
