# `live_stop_push` — stop a live video stream

Cloud command that terminates an in-progress live stream on the specified video source. Pairs with [`live_start_push`](live_start_push.md).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `live_stop_push` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `live_stop_push` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `video_id` | string | Identifier of the stream to stop. Format `{sn}/{camera_index}/{video_index}`. Must match the `video_id` supplied to [`live_start_push`](live_start_push.md). |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "video_id": "1ZNDH1D0010098/42-0-0/zoom-0"
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "live_stop_push"
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
  "method": "live_stop_push"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/30.live.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Stream.txt]` | v1.15 (Dock 2) — identical to v1.11. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Stream.txt]` | v1.15 (Dock 3) — identical payload. |
