# `unlock_license_switch` — enable or disable a single unlocking license

Cloud command that toggles one of the device's previously-imported FlySafe unlocking licenses on or off. Each license unlocks a specific restriction type (authorization zone, custom circular area, country/region, altitude limit, custom polygon area, power, or RID) — see [`unlock_license_list`](unlock_license_list.md) for the enumeration of types and the list of licenses the cloud can toggle.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `unlock_license_switch` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `unlock_license_switch` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `license_id` | integer | Unique identifier of the unlocking license. Must match an ID previously returned by [`unlock_license_list`](unlock_license_list.md). |
| `enable` | boolean | `true` / `1` = enable; `false` / `0` = disable. |

### Example (down)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "enable": true,
    "license_id": 240330
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero represents an error. |
| `license_id` | integer | Echoes the `license_id` from the command (so multiple in-flight toggles can be correlated). |

### Example (reply)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "license_id": 240330,
    "result": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1234567890123
}
```

## Relationship to other methods

- After a fresh fleet binding, the cloud typically calls [`unlock_license_list`](unlock_license_list.md) to discover which licenses are loaded on the aircraft and dock.
- To push a new license file (rather than toggle an existing one), use [`unlock_license_update`](unlock_license_update.md).
- Full FlySafe choreography will be documented in Phase 9 workflow `workflows/flysafe-custom-flight-area-sync.md`.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/170.flysafe.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-FlySafe.txt]` | v1.15 (Dock 2) — identical payload. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-FlySafe.txt]` | v1.15 (Dock 3, hand-authored). Adds an explicit `enable` enum label `{"0":"Not Enabled","1":"Enabled"}`; payload semantics unchanged. |
