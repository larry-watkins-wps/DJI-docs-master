# `drc_psdk_input_box_text_set` — set PSDK widget input-box text

DRC command that sets the text value of a PSDK widget's input box. Used by the cloud to push text into the payload's UI.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — PSDK payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_psdk_input_box_text_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_psdk_input_box_text_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `psdk_index` | int | PSDK payload device index. |
| `value` | string | Text content. Max length 128. |

### Example

```json
{
  "data": {
    "psdk_index": 1,
    "value": ""
  },
  "method": "drc_psdk_input_box_text_set",
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
