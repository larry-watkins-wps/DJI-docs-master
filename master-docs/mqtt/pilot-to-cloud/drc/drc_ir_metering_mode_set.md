# `drc_ir_metering_mode_set` — IR metering mode (DRC channel)

RC-Plus-2-specific DRC variant of [`../../dock-to-cloud/services/ir_metering_mode_set.md`](../../dock-to-cloud/services/ir_metering_mode_set.md). Same semantics — switch IR temperature-measurement mode among off / point / area — delivered on the lightweight DRC channel.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.**

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_ir_metering_mode_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_ir_metering_mode_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | text | Camera enumeration `{type-subtype-gimbalindex}`. |
| `mode` | enum_int | `{0: "Close temperature measurement", 1: "Point temperature measurement", 2: "Area temperature measurement"}`. |

### Example

```json
{
  "data": {
    "mode": 1,
    "payload_index": "89-0-0"
  },
  "method": "drc_ir_metering_mode_set",
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
  "method": "drc_ir_metering_mode_set",
  "seq": 1
}
```

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Remote-Control.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |
