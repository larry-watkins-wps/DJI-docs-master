# `drone_emergency_stop` — DRC emergency stop

Low-latency DRC command that brings the aircraft to an immediate hover, cancelling any in-progress DRC-channel motion commands. No payload. Device replies with `result` on `/drc/up`.

Part of the Phase 4 MQTT catalog. Shared conventions (DRC envelope) live in [`../../README.md` §5.8](../../README.md#58-drcup--drcdown--direct-remote-control).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drone_emergency_stop` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drone_emergency_stop` |

## Down — `data` fields

`null` — no payload fields required. Envelope `data` is an empty object.

### Example

```json
{
  "method": "drone_emergency_stop",
  "data": {}
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. `0` = success; non-zero represents an error. |

### Example

```json
{
  "method": "drone_emergency_stop",
  "data": {
    "result": 0
  }
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
