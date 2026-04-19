# `return_specific_home` — designate landing dock for multi-dock return

Cloud command that, during a multi-dock task, designates a specific dock as the return destination. Used in scenarios where the takeoff dock and landing dock are different and the cloud must pick which dock the aircraft returns to.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `return_specific_home` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `return_specific_home` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `home_dock_sn` | string | SN of the dock the aircraft should return to. |

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "return_specific_home",
  "timestamp": 1234567890123,
  "data": {
    "home_dock_sn": "xxxxxxxx"
  }
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero = error. |

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "return_specific_home",
  "timestamp": 1695634358385,
  "data": { "result": 0 }
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/50.wayline.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Wayline-Management.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-WaylineManagement.txt]` | v1.15 (Dock 3). |
