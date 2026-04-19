# `drc_ai_model_select` — select which AI model to use

DRC command that selects the active AI model from the list published in [`drc_ai_info_push.ai_model_list`](drc_ai_info_push.md). The index is the model's `index` value from that list.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — AI identify subsystem.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_ai_model_select` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_ai_model_select` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `index` | int | Model index taken from [`drc_ai_info_push.ai_model_list[].index`](drc_ai_info_push.md). Third-party model indexes are ≥ 128 (DJI adds an offset to distinguish them). |

### Example

```json
{
  "seq": 1,
  "method": "drc_ai_model_select",
  "data": {
    "index": 0
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
