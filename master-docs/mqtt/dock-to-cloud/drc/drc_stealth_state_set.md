# `drc_stealth_state_set` — enable / disable stealth mode

DRC command that engages stealth (discreet) mode — turns off **all** aircraft lights, suppresses the beacon, and lowers the aircraft's light signature for covert ops.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_stealth_state_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_stealth_state_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `stealth_state` | enum int | `0` = Disabled; `1` = Enabled. |

### Example

```json
{
  "data": {
    "stealth_state": 0
  },
  "method": "drc_stealth_state_set",
  "seq": 1
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

### Example

```json
{
  "data": {
    "result": 0
  },
  "method": "drc_stealth_state_set",
  "seq": 1
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/180.remote-control.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Control.txt]` | v1.15 (Dock 2) — identical. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — identical. |
