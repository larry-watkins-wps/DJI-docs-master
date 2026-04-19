# `flight_areas_update` — tell the device to refresh its custom-flight-area set

Cloud command that asks the dock to resynchronize its custom flight areas against the cloud's current file inventory. The command itself carries no parameters (`data: null`); upon receipt the dock reaches back to the cloud via [`flight_areas_get`](../requests/flight_areas_get.md), downloads any new / changed files, and then publishes [`flight_areas_sync_progress`](../events/flight_areas_sync_progress.md) events as the sync completes.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `flight_areas_update` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `flight_areas_update` |

## Down — `data` fields

`data: null`. The command carries no parameters beyond the envelope's `method`, `tid`, `bid`, `timestamp`.

### Example (down)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": null,
  "method": "flight_areas_update",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success (command accepted); non-zero represents an error. |

### Example (reply)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "result": 0
  },
  "method": "flight_areas_update",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655
}
```

## Relationship to other methods

- The dock responds to this command by fetching the file inventory via [`flight_areas_get`](../requests/flight_areas_get.md).
- Sync outcome is reported via [`flight_areas_sync_progress`](../events/flight_areas_sync_progress.md) (with `need_reply: 1`, so the cloud acknowledges).
- Once loaded, per-area aircraft geometry is pushed via [`flight_areas_drone_location`](../events/flight_areas_drone_location.md).
- Full Custom-Flight-Area choreography will be documented in Phase 9 workflow `workflows/flysafe-custom-flight-area-sync.md`.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/130.custom-flight-area.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Custom-Flight-Area.txt]` | v1.15 (Dock 2) — identical. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Custom-Flight-Area.txt]` | v1.15 (Dock 3) — identical. |
