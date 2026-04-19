# `flighttask_progress_get` — query task-execution state of another dock

Device-initiated request (dock → cloud) used in multi-dock scenarios. One dock asks the cloud for the task-execution state of the *other* dock participating in the same multi-dock task. The cloud replies with the target dock's latest `flighttask_progress` output.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — v1.11 and v1.15 both document this, but the request body differs slightly between versions (see note).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/requests` | `flighttask_progress_get` |
| Cloud → Device | `thing/product/{gateway_sn}/requests_reply` | `flighttask_progress_get` |

## Up (request) — `data` fields

### v1.11 (Cloud-API-Doc)

| Field | Type | Description |
|---|---|---|
| `target_sn` | string | SN of the other dock whose state is being queried. |
| `flight_id` | string | Target flight route task UUID. |

### v1.15 (DJI_Cloud)

| Field | Type | Description |
|---|---|---|
| `sn` | string | Target device SN (note: renamed from `target_sn`). |

> **Version drift.** v1.11 uses `target_sn` + `flight_id`; v1.15 uses just `sn`. The v1.15 extract may have dropped the `flight_id` field in extraction; or DJI simplified the schema. Both request forms should be tolerated on the server side.

### Example (v1.11 form)

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "gateway": "xxx",
  "method": "flighttask_progress_get",
  "timestamp": 1234567890123,
  "data": {
    "target_sn": "xxx",
    "flight_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx"
  }
}
```

## Down (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success. |
| `output.flight_id` | string | Target device's latest current task ID. |
| `output.progress` | struct | `{current_step, percent}` — same enumeration as [`events/flighttask_progress`](../events/flighttask_progress.md) output fields. |
| `output.status` | string | Task state — same enumeration as `flighttask_progress` status field. |

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "gateway": "xxx",
  "method": "flighttask_progress_get",
  "timestamp": 0,
  "data": {
    "result": 0,
    "output": {
      "flight_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
      "progress": {
        "current_step": 27,
        "percent": 90
      },
      "status": "in_progress"
    }
  }
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/50.wayline.md]` | v1.11 canonical (Dock 2) — request uses `target_sn` + `flight_id`. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Wayline-Management.txt]` | v1.15 (Dock 2) — request shows `sn` only. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-WaylineManagement.txt]` | v1.15 (Dock 3) — matches Dock 2 v1.15. |
