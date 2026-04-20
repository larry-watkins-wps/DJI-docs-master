# RTMP livestream transport

**Real-Time Messaging Protocol** (RTMP) — TCP-based streaming protocol used for pushing live audio/video from the DJI device to a cloud-hosted RTMP ingest server. RTMP is the broadest-support protocol across DJI's device cohorts: every in-scope device can emit RTMP.

See [`README.md`](README.md) for the device-support matrix across all four protocols and scope rules. MQTT signaling to start / stop / qualify a stream lives in [`../mqtt/dock-to-cloud/services/live_start_push.md`](../mqtt/dock-to-cloud/services/live_start_push.md).

---

## 1. MQTT selector

- `url_type` = **`1`** in all in-scope MQTT `live_start_push` enums (Dock 2, Dock 3, RC Plus 2 Enterprise, RC Pro Enterprise).

---

## 2. `url` shape

DJI source description (verbatim, v1.15): `rtmp://xxxxxxx`.

DJI source example (verbatim, v1.15): `rtmp://192.168.1.1:8080/live`.

Shape: a standard RTMP URL —

```
rtmp://{host}[:{port}]/{app}[/{stream}]
```

- `{host}` — the cloud's RTMP ingest endpoint (IP or DNS name).
- `{port}` — typically `1935` (RTMP default); the DJI example uses `8080`. Any TCP port the cloud binds its ingest to.
- `{app}` — the RTMP application name. DJI's example uses `live`.
- `{stream}` — the stream key. DJI's example omits this (which means a default stream-key convention must be negotiated elsewhere — likely the cloud's RTMP server infers it from connection metadata).

DJI does not expand on `{app}` / `{stream}` semantics. Clouds typically derive both from the `video_id` MQTT field (`{sn}/{camera_index}/{video_index}`) so that each stream lands on a distinct RTMP path.

### 2.1 RTMP variants

DJI prose in the v1.11 feature-set page describes RTMP as a protocol family including `RTMPT` (HTTP-tunnelled), `RTMPS` (TLS), and `RTMPE` (encrypted). The v1.15 `url_type` enum does not distinguish between these — `url_type = 1` accepts any URL whose scheme is `rtmp://`. Whether DJI devices support `rtmps://`, `rtmpt://`, or `rtmpe://` URLs is not documented by DJI and should be verified on hardware if TLS is required.

---

## 3. Device support

| Device | RTMP (`url_type = 1`) | Source |
|---|---|---|
| Dock 3 | ✓ | [`DJI_Cloud/DJI_CloudAPI-Dock3-LiveStream.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock3-LiveStream.txt) |
| Dock 2 | ✓ | [`DJI_Cloud/DJI_CloudAPI-Dock2-Live-Stream.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock2-Live-Stream.txt) |
| RC Plus 2 Enterprise | ✓ | [`DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Stream.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Stream.txt) |
| RC Pro Enterprise | ✓ | [`DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Live-Stream.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Live-Stream.txt) |

RTMP is the **only** protocol supported by all in-scope cohorts — a cloud implementing just RTMP covers every device.

---

## 4. Cloud-side responsibility

The cloud must host an **RTMP ingest server** reachable from the DJI device over the network. DJI's reference integrations commonly use:

- [nginx-rtmp-module](https://github.com/arut/nginx-rtmp-module) — nginx-based RTMP ingest + HLS/DASH transcode.
- [SRS](https://github.com/ossrs/srs) — Simple Realtime Server; RTMP / HLS / WebRTC / GB28181 gateway.
- Any commercial streaming platform that accepts `rtmp://` publish (AWS IVS, Cloudflare Stream, Wowza, Ant Media, Twilio Live, etc.).

**What the cloud does with the stream** after ingest (transcode, store, re-serve over HLS/DASH/WebRTC for browser playback, record for archival) is out of scope for the DJI wire contract and out of scope for this corpus.

The MQTT `live_set_quality` command allows the cloud to request a different resolution/bitrate mid-stream — the cloud receives the new encode from the device over the same RTMP connection without reconnection; see [`../mqtt/dock-to-cloud/services/live_set_quality.md`](../mqtt/dock-to-cloud/services/live_set_quality.md).

---

## 5. Worked example — complete `live_start_push` payload

MQTT message (Cloud → Device on `thing/product/{gateway_sn}/services`):

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "url_type": 1,
    "url": "rtmp://192.168.1.1:8080/live",
    "video_id": "1ZNDH1D0010098/39-0-7/normal-0",
    "video_quality": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "live_start_push"
}
```

The device accepts the command (`services_reply` with `result: 0`), connects to `rtmp://192.168.1.1:8080/live`, and begins pushing the H.264-encoded video stream identified by `video_id`. The cloud's RTMP ingest receives the stream on the `/live` application and relays / stores it per the cloud's video-delivery architecture.

See [`../mqtt/dock-to-cloud/services/live_start_push.md`](../mqtt/dock-to-cloud/services/live_start_push.md) for the full envelope spec and reply semantics.

---

## 6. External references

DJI does not include its own RTMP protocol reference. For external standards, a cloud implementer should consult:

- [Adobe RTMP spec (PDF, 2012)](https://rtmp.veriskope.com/pdf/rtmp_specification_1.0.pdf) — the canonical RTMP 1.0 document.
- [RFC 7385](https://www.rfc-editor.org/rfc/rfc7385) — HTTP-based streaming alternatives (informational).

---

## 7. Source provenance

| Source | Role |
|---|---|
| [`DJI_Cloud/DJI_CloudAPI-Dock3-LiveStream.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock3-LiveStream.txt) | v1.15 primary — Dock 3 `url_type = 1` documentation + URL example. |
| [`DJI_Cloud/DJI_CloudAPI-Dock2-Live-Stream.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock2-Live-Stream.txt) | v1.15 primary — Dock 2 `url_type = 1` documentation + URL example. |
| [`DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Stream.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Stream.txt) | v1.15 primary — RC Plus 2 Enterprise `url_type = 1`. |
| [`DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Live-Stream.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Live-Stream.txt) | v1.15 primary — RC Pro Enterprise `url_type = 1`. |
| [`../mqtt/dock-to-cloud/services/live_start_push.md`](../mqtt/dock-to-cloud/services/live_start_push.md) | Phase 4d — MQTT signaling spec that invokes this protocol. |
