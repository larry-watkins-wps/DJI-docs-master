# `drc_ai_spotlight_zoom_confirm` — confirm box-selected AI target

DRC command that commits to tracking whatever target was framed by the most recent [`drc_ai_spotlight_zoom_select`](drc_ai_spotlight_zoom_select.md) box. `Data: null`.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — AI identify subsystem.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_ai_spotlight_zoom_confirm` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_ai_spotlight_zoom_confirm` |

## Down — `data`

`Data: null`.

### Example

```json
{
  "seq": 1,
  "method": "drc_ai_spotlight_zoom_confirm",
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
