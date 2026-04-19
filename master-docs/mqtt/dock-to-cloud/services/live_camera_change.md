# `live_camera_change` — switch FPV camera between inside-the-dock and outside-the-dock

Cloud command that switches the FPV (first-person-view) camera source — either the camera mounted inside the dock (shows dock internals, used during housekeeping) or the one mounted outside (shows the environment around the dock). Does not affect the aircraft's onboard cameras. Used to pull up the dock's own feed for pre-flight inspection.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `live_camera_change` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `live_camera_change` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `video_id` | string | Identifier of the stream whose source camera is being switched. Format `{sn}/{camera_index}/{video_index}`. |
| `camera_position` | enum int | `0` = Inside the dock, `1` = Outside the dock. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "camera_position": 0,
    "video_id": "1ZNDH1D0010098/165-0-7/normal-0"
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "live_camera_change"
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
  "data": {
    "result": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "live_camera_change"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/30.live.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Stream.txt]` | v1.15 (Dock 2) — identical to v1.11. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Stream.txt]` | v1.15 (Dock 3) — identical payload. |
