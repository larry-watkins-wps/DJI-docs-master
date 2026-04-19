# `drc_ai_spotlight_zoom_stop` — stop AI tracking

DRC command that stops any in-progress AI tracking session. `Data: null`.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — AI identify subsystem.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_ai_spotlight_zoom_stop` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_ai_spotlight_zoom_stop` |

## Down — `data`

`Data: null`.

### Example

```json
{
  "seq": 1,
  "method": "drc_ai_spotlight_zoom_stop",
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
