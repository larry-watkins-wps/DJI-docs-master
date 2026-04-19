# `flight_areas_sync_progress` — custom-flight-area file sync state

Event pushed by the dock reporting the status of a custom-flight-area (CFA) file synchronization — typically triggered by a [`flight_areas_update`](../services/flight_areas_update.md) command. The event reports one of five status values, an optional error-reason code, and the file descriptor currently being synced.

`need_reply: 1` — cloud must acknowledge with `{"result": 0}` on `events_reply`.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, events-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `flight_areas_sync_progress` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `flight_areas_sync_progress` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `status` | enum string | Synchronization state. `wait_sync` = queued; `synchronizing` = in progress; `synchronized` = finished OK; `fail` = sync failed (see `reason`); `switch_fail` = enabling the new area set failed after sync. |
| `reason` | enum int | Failure reason when `status` is `fail` or `switch_fail`. Enumerated below. Omitted on success. |
| `file` | struct | Descriptor of the CFA file being synced. |
| `file.name` | string | File name (typically `geofence_{fileMD5}.json`). |
| `file.checksum` | string | SHA-256 digest of the file contents. |

### `reason` enum

| Value | Meaning |
|---|---|
| `1` | Failed to parse file information returned from the cloud. |
| `2` | Failed to get file information on the aircraft side. |
| `3` | Failed to download file from the cloud. |
| `4` | Link flip failed. |
| `5` | File transfer failed. |
| `6` | Disable failed. |
| `7` | Failed to delete custom flight area. |
| `8` | Failed to load job area data on the aircraft side. |
| `9` | Enable failed. |
| `10` | Dock enhanced image transmission cannot be turned off — job-area data sync failed. |
| `11` | Aircraft startup failed, unable to synchronize job-area data. |
| `12` | Checksum verification failed. |
| `13` | Synchronization exception — timeout. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "file": {
      "checksum": "sha256",
      "name": "geofence_xxx.json"
    },
    "reason": 0,
    "status": "synchronized"
  },
  "method": "flight_areas_sync_progress",
  "need_reply": 1,
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 16540709686556
}
```

## Down (reply) — `data` fields

Standard events_reply envelope: `data.result` (integer; `0` = success).

## Relationship to other methods

- The sync is usually triggered by [`flight_areas_update`](../services/flight_areas_update.md); the dock follows up by fetching the file list via [`flight_areas_get`](../requests/flight_areas_get.md) and then publishes progress events of this method.
- Area-loaded aircraft then report their geometric relationship to the loaded areas via [`flight_areas_drone_location`](flight_areas_drone_location.md).
- Full Custom-Flight-Area choreography will be documented in Phase 9 workflow `workflows/flysafe-custom-flight-area-sync.md`.

## Source inconsistencies flagged by DJI's own example

- **Timestamp width.** Example shows `"timestamp": 16540709686556` — 14 digits. See [`flight_areas_drone_location`](flight_areas_drone_location.md#source-inconsistencies-flagged-by-djis-own-example) for the shared note — pervasive across this family.
- **`reason` in the success example.** DJI's example sends `"reason": 0` alongside `"status": "synchronized"`. The documented enum starts at `1` (all failure codes). `0` in context appears to mean "no error" rather than any documented reason; treat as an informational value and rely on `status` for the authoritative outcome.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/130.custom-flight-area.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Custom-Flight-Area.txt]` | v1.15 (Dock 2) — identical. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Custom-Flight-Area.txt]` | v1.15 (Dock 3) — identical. |
