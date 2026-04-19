# `drc_ai_identify_score_mode_set` — set AI recognition confidence mode

DRC command that selects how the AI identifies calibrate their confidence score — counting, search-and-rescue, or a user-defined custom mode (where [`drc_ai_identify_score_set`](drc_ai_identify_score_set.md) is needed to set the threshold).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — AI identify subsystem.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_ai_identify_score_mode_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_ai_identify_score_mode_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `score_mode` | enum int | `0` = Invalid, `1` = Counting Mode, `2` = Search and Rescue Mode, `3` = Custom Mode. |

### Example

```json
{
  "seq": 1,
  "method": "drc_ai_identify_score_mode_set",
  "data": {
    "score_mode": 1
  }
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

## Relationship to other methods

- When `score_mode = 3` (Custom), the actual confidence threshold is set by [`drc_ai_identify_score_set`](drc_ai_identify_score_set.md). Reset with [`drc_ai_identify_score_reset`](drc_ai_identify_score_reset.md).

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — only source. |
