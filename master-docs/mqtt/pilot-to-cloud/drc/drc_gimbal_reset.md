# `drc_gimbal_reset` — reset gimbal (DRC channel)

RC-Plus-2-specific DRC variant of [`../../dock-to-cloud/services/gimbal_reset.md`](../../dock-to-cloud/services/gimbal_reset.md). Same semantics — reset gimbal orientation to one of four preset modes — delivered on the lightweight DRC channel.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.**

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_gimbal_reset` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_gimbal_reset` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | text | Camera enumeration `{type-subtype-gimbalindex}`. |
| `reset_mode` | enum_int | `{0: "Reset", 1: "Downward", 2: "Gimbal pan recenter", 3: "Gimbal pitch downward"}`. |

### Example

```json
{
  "data": {
    "payload_index": "89-0-0",
    "reset_mode": 1
  },
  "method": "drc_gimbal_reset",
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
  "method": "drc_gimbal_reset",
  "seq": 1
}
```

### Source inconsistencies flagged by DJI's own example

- **Garbled `payload_index` schema cell** — DJI source reads `{_{type-subtype-gimbalindex}__aembLbhPpc}` as the `Name` column value. Clearly a copy-paste artifact; the field semantic is the standard `{type-subtype-gimbalindex}` enumeration documented in the dock-to-cloud parallel.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Remote-Control.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |
