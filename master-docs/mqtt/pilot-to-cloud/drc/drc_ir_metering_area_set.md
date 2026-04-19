# `drc_ir_metering_area_set` — IR metering area (DRC channel)

RC-Plus-2-specific DRC variant of [`../../dock-to-cloud/services/ir_metering_area_set.md`](../../dock-to-cloud/services/ir_metering_area_set.md). Same semantics — set a rectangular temperature-measurement area on the IR camera — delivered on the lightweight DRC channel.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.**

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_ir_metering_area_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_ir_metering_area_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | text | Camera enumeration `{type-subtype-gimbalindex}`. |
| `x` | double | Upper-left x of the area, `[0,1]`. |
| `y` | double | Upper-left y of the area, `[0,1]`. |
| `width` | double | Width of the area, `[0,1]`. |
| `height` | double | Height of the area, `[0,1]`. |

### Example

```json
{
  "data": {
    "height": 0.2,
    "payload_index": "89-0-0",
    "width": 0.2,
    "x": 0.5,
    "y": 0.5
  },
  "method": "drc_ir_metering_area_set",
  "seq": 1
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success. |

### Example

```json
{
  "data": { "result": 0 },
  "method": "drc_ir_metering_area_set",
  "seq": 1
}
```

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Remote-Control.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |
