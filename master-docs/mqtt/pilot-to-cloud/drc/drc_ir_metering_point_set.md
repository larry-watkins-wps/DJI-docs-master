# `drc_ir_metering_point_set` — IR metering point (DRC channel)

RC-Plus-2-specific DRC variant of [`../../dock-to-cloud/services/ir_metering_point_set.md`](../../dock-to-cloud/services/ir_metering_point_set.md). Same semantics — set a single temperature-measurement point on the IR camera — delivered on the lightweight DRC channel.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.**

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_ir_metering_point_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_ir_metering_point_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | text | Camera enumeration `{type-subtype-gimbalindex}`. |
| `x` | double | Point coord x, `[0,1]`, upper-left origin, horizontal axis. |
| `y` | double | Point coord y, `[0,1]`, upper-left origin, vertical axis. |

### Example

```json
{
  "data": {
    "payload_index": "89-0-0",
    "x": 0.5,
    "y": 0.5
  },
  "method": "drc_ir_metering_point_set",
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
  "method": "drc_ir_metering_point_set",
  "seq": 1
}
```

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Remote-Control.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |
