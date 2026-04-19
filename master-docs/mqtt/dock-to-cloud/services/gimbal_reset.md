# `gimbal_reset` — reset gimbal

Cloud command that recenters / resets the gimbal on the selected payload mount. Supports four modes: full reset, pitch-downward, pan-recenter, and pitch-downward (alias).

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `gimbal_reset` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `gimbal_reset` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Payload enumeration (`{type}-{subtype}-{gimbalindex}`). |
| `reset_mode` | enum int | `0` = reset, `1` = downward, `2` = gimbal pan recenter, `3` = gimbal pitch downward. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "payload_index": "39-0-7",
    "reset_mode": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "gimbal_reset"
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
  "method": "gimbal_reset"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
