# `live_start_push` — start a live video stream from the dock / aircraft

Cloud command that tells the dock to push a live video stream over one of the supported media-transport protocols (RTMP, GB28181, WebRTC, or Agora on Dock 2). The `url` parameter shape is protocol-dependent; see `livestream-protocols/` (Phase 7) for the per-protocol wire details. Quality can be adjusted mid-stream via [`live_set_quality`](live_set_quality.md) and the stream is terminated with [`live_stop_push`](live_stop_push.md).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3**. The `url_type` enum differs — Dock 3 drops Agora. See [Source differences](#source-differences).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `live_start_push` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `live_start_push` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `url_type` | enum int | Live-streaming protocol. **Dock 2**: `0` = Agora, `1` = RTMP, `3` = GB28181, `4` = WebRTC. **Dock 3**: `1` = RTMP, `3` = GB28181, `4` = WebRTC (Agora removed). WebRTC supports only the WHIP exchange. |
| `url` | string | Protocol-specific stream parameters. RTMP: `rtmp://host:port/app/stream`. GB28181: amp-delimited kv pairs (`serverIP=…&serverPort=…&serverID=…&agentID=…&agentPassword=…&localPort=…&channel=…`). Agora (Dock 2 only): `channel=…&sn=…&token=…&uid=…` — tokens may contain `+` characters that must be URL-encoded once. WebRTC: WHIP endpoint, e.g. `http://host:port/rtc/v1/whip/?app=live&stream=livestream`. |
| `video_id` | string | Identifier for the specific video source. Format `{sn}/{camera_index}/{video_index}`, where `camera_index` is `{type-subtype-gimbalindex}`. |
| `video_quality` | enum int | `0` = Adaptive, `1` = Smooth, `2` = Standard definition, `3` = High definition, `4` = Ultra-high definition. Bitrates vary by cohort — see [Source differences](#source-differences). |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "url": "channel=1ZNDH1D0010098_39-0-7&sn=1ZNDH1D0010098&token=006dca67721582a48768ec4d817b7b25a86IADk%2Fcm%2Fdv%2BHY6qT%2FAKM6y7TcUe4lXNvZpycH7vUMAlM6pFALUKF2zyCIgA82pQE8cCoYAQAAQDxwKhgAgDxwKhgAwDxwKhgBADxwKhg&uid=50000",
    "url_type": 0,
    "video_id": "1ZNDH1D0010098/39-0-7/normal-0",
    "video_quality": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "live_start_push"
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
  "method": "live_start_push"
}
```

## Source differences

- **`url_type` enum**: Dock 3 drops the `0` = Agora entry that Dock 2 still supports. A Dock 3 deployment must not issue `url_type: 0`.
- **Quality bitrates diverge across three sources** (all for `video_quality = 1` / Smooth):
  - v1.11 Dock 2 canonical: `960 * 540, 512 Kbps`.
  - v1.15 Dock 2: `960 * 540, 1 Mbps`.
  - v1.15 Dock 3: `960 * 540, 512 Kbps`.
  - UHD also diverges: v1.11 Dock 2 says `3 Mbps`, v1.15 Dock 2 says `8 Mbps`, v1.15 Dock 3 says `3 Mbps` for `live_start_push` but `8 Mbps` for [`live_set_quality`](live_set_quality.md). Treat as DJI source-table noise — the authoritative bitrate is whatever the device negotiates at run time.

## Source inconsistencies flagged by DJI's own example

- The Dock 3 example sets `url_type: 0`, which is not one of the documented Dock 3 enum values (`1` / `3` / `4`). The example appears to have been copied from Dock 2 without updating the field. Treat the declared enum as authoritative.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/30.live.md]` | v1.11 canonical (Dock 2) — documents all four `url_type` values including Agora. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Stream.txt]` | v1.15 (Dock 2) — same four `url_type` values as v1.11. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Stream.txt]` | v1.15 (Dock 3) — `url_type` reduced to RTMP / GB28181 / WebRTC. |
