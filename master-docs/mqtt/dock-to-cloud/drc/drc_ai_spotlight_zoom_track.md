# `drc_ai_spotlight_zoom_track` — track a specific recognized target

DRC command that begins AI tracking on a specific target identified by its `target_index` (as published by the live-stream overlay). Used after AI recognition has flagged one or more candidates.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — AI identify subsystem.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_ai_spotlight_zoom_track` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_ai_spotlight_zoom_track` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `target_index` | int | Target index published through the live stream overlay. |

### Example

```json
{
  "seq": 1,
  "method": "drc_ai_spotlight_zoom_track",
  "data": {
    "target_index": 0
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
