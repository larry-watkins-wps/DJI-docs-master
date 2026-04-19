# `drc_ai_spotlight_zoom_select` — box-select a target region for AI tracking

DRC command that draws a bounding box on the liveview and begins AI box-select tracking of whatever is inside. Coordinates are normalized 0–1 and scaled by 10000 (i.e. sent as `int(fraction × 10000)`).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — AI identify subsystem.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_ai_spotlight_zoom_select` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_ai_spotlight_zoom_select` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `center_x` | double | Center X coordinate of the bounding box, in units of `1/10000` of the screen width. |
| `center_y` | double | Center Y coordinate of the bounding box, in units of `1/10000` of the screen height. |
| `width` | double | Box width, in units of `1/10000` of the screen width. |
| `height` | double | Box height, in units of `1/10000` of the screen height. |

Schema column names in DJI source are `center_x` / `center_y` / `height` / `width` (note the Z-order `height` before `width` in the schema listing).

### Example (DJI source — not valid JSON, see [Source inconsistencies](#source-inconsistencies-flagged-by-djis-own-example))

```json
{
  "seq": 1,
  "method": "drc_ai_spotlight_zoom_select",
  "data": {
    "center_x":0.0*10000,
    "center_y":0.0*10000,
    "height":1.0*10000,
    "width":1.0*10000
  }
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

## Relationship to other methods

- Box-select confirms via [`drc_ai_spotlight_zoom_confirm`](drc_ai_spotlight_zoom_confirm.md); cancel via [`drc_ai_spotlight_zoom_stop`](drc_ai_spotlight_zoom_stop.md).

## Source inconsistencies flagged by DJI's own example

- **Example uses literal arithmetic expressions** (`0.0*10000`, `1.0*10000`) that are not valid JSON — JSON parsers reject this. The constraint column also writes `{"max":1,"min":0}*10000`. DJI's intent is that the integers on the wire equal `fraction × 10000`; the example is pseudo-code, not a real JSON payload. Treat as instructional notation.
- **Field labels copy-pasted from IR metering.** The schema description for `center_x` reads "Coordinate x of the left and upper corner of the temperature measurement area" — copied from the IR metering service and clearly wrong for this method. The field is the bounding-box center, not a corner, and unrelated to temperature.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — only source. |
