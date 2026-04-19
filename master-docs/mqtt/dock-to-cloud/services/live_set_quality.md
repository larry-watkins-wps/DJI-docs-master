# `live_set_quality` — change the quality level of an in-progress stream

Cloud command that adjusts the resolution/bitrate of a live stream already started by [`live_start_push`](live_start_push.md). `video_quality` uses the same enumeration as the start command.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3. Bitrate numbers in DJI's own tables diverge across sources — see [`live_start_push`](live_start_push.md#source-differences).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `live_set_quality` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `live_set_quality` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `video_id` | string | Identifier of the stream to adjust. Format `{sn}/{camera_index}/{video_index}`. Must match the `video_id` supplied to [`live_start_push`](live_start_push.md). |
| `video_quality` | enum int | `0` = Adaptive, `1` = Smooth, `2` = Standard definition, `3` = High definition, `4` = Ultra-high definition. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "video_id": "1ZNDH1D0010098/39-0-7/normal-0",
    "video_quality": 4
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "live_set_quality"
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
  "method": "live_set_quality"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/30.live.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Stream.txt]` | v1.15 (Dock 2) — identical to v1.11 apart from the Smooth bitrate note (`1 Mbps` vs `512 Kbps`). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Stream.txt]` | v1.15 (Dock 3) — identical payload. |
