# `drc_ai_identify_filter_set` — set AI recognition label-filter list

DRC command that sets the list of label indexes the AI recognizer should report on. Labels outside the filter are suppressed. For third-party models, the filter value for a label is `label_index + 128` (DJI uses the offset to distinguish third-party models from native ones).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — AI identify subsystem.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_ai_identify_filter_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_ai_identify_filter_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `filters` | array of int | Label indexes to include. For third-party models, add `128` to each label index (e.g. label `1` → filter value `129`). |

### Example

```json
{
  "seq": 1,
  "method": "drc_ai_identify_filter_set",
  "data": {
    "filters": [1, 2, 3]
  }
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

## Relationship to other methods

- Current filter list is readable via [`drc_ai_info_push.selected_ai_model.filters`](drc_ai_info_push.md).

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — only source. |
