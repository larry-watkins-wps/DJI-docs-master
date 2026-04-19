# `flighttask_create` — create a mission *(deprecated)*

Legacy method for creating a flight mission. **DJI marks this method as deprecated**; new integrations should use [`flighttask_prepare`](flighttask_prepare.md) which supports conditional tasks, multi-dock, break-point resume, simulation, and RTK precision configuration.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload. Retained in both v1.11 and v1.15 documentation for backward compatibility.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `flighttask_create` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `flighttask_create` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `flight_id` | string | Task ID. |
| `type` | string | Mission type, e.g. `"wayline"`. |
| `file` | struct | `{url, sign}` — KMZ URL + MD5 signature. Note `sign` vs `flighttask_prepare`'s `fingerprint`. |

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "flighttask_create",
  "timestamp": 1654070968655,
  "data": {
    "flight_id": "xxxxxxx",
    "type": "wayline",
    "file": {
      "url": "https://xxx.com/xxxx",
      "sign": "xxxx"
    }
  }
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success. |

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/50.wayline.md]` | v1.11 canonical (Dock 2) — labeled "Create a mission (deprecated)". |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Wayline-Management.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-WaylineManagement.txt]` | v1.15 (Dock 3). |
