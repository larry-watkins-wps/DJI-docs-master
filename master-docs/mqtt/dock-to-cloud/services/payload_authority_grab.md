# `payload_authority_grab` — grab payload-control authority

Cloud command that takes over payload (gimbal + camera) control authority for a specified payload mount point. Must succeed before gimbal/camera methods (`camera_*`, `gimbal_*`, `ir_*`) can drive the payload. Paired with [`flight_authority_grab`](flight_authority_grab.md) and [`drc_mode_enter`](drc_mode_enter.md).

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `payload_authority_grab` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `payload_authority_grab` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Payload enumeration value. Non-standard `device_mode_key`, formatted `{type}-{subtype}-{gimbalindex}` (e.g. `39-0-7`). See Product Supported reference for the full enumeration of camera payloads and mount locations. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "payload_index": "39-0-7"
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "payload_authority_grab"
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero represents an error. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": { "result": 0 },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "payload_authority_grab"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
