# `drc_force_landing` — force the aircraft to land

DRC command that commands the aircraft to descend to the ground **regardless of obstacles**. Cancellable via [`drone_emergency_stop`](drone_emergency_stop.md). After forced landing the aircraft can only be recovered manually — DJI documents this method with an explicit "use with caution" warning.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload. `Data: null`.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_force_landing` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_force_landing` |

## Down — `data`

`Data: null`.

### Example

```json
{
  "data": {},
  "method": "drc_force_landing",
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
  "method": "drc_force_landing",
  "seq": 1
}
```

## Relationship to other methods

- Cancelled by [`drone_emergency_stop`](drone_emergency_stop.md) (landed in 4c).
- Contrast [`drc_emergency_landing`](drc_emergency_landing.md) — which pauses on obstacle detection rather than ignoring obstacles.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/180.remote-control.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Control.txt]` | v1.15 (Dock 2) — identical. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — identical. |
