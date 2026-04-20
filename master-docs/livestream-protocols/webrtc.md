# WebRTC (WHIP) livestream transport

**WebRTC** (Web Real-Time Communication) — low-latency peer-to-peer audio/video/data streaming. DJI devices use WebRTC **only** via the [WHIP](https://datatracker.ietf.org/doc/draft-ietf-wish-whip/) (WebRTC-HTTP Ingestion Protocol) signaling profile, which turns WebRTC into a one-way publish/ingest flow over HTTP instead of the classic bidirectional signaling dance. This is explicit in the DJI v1.15 `live_start_push` description: *"WebRTC only supports WHIP protocol exchange."*

See [`README.md`](README.md) for the device-support matrix across all four protocols and scope rules. MQTT signaling to start / stop / qualify a stream lives in [`../mqtt/dock-to-cloud/services/live_start_push.md`](../mqtt/dock-to-cloud/services/live_start_push.md).

---

## 1. MQTT selector

- `url_type` = **`4`** in the MQTT `live_start_push` enums for Dock 2, Dock 3, and RC Plus 2 Enterprise.
- **Not supported** on RC Pro Enterprise (v1.15 RC Pro enum is `{0: Agora, 1: RTMP, 3: GB28181}` only).

---

## 2. `url` shape

DJI source description (verbatim, v1.15): *"WebRTC only supports WHIP protocol exchange"*.

DJI source example (verbatim, v1.15): `http://192.168.1.1:8080/rtc/v1/whip/?app=live&stream=livestream`.

Shape: a standard HTTP URL pointing to the WHIP endpoint —

```
http(s)://{host}[:{port}]/{whip-path}?app={app}&stream={stream}
```

- `{host}` / `{port}` — WHIP endpoint location on the cloud.
- `{whip-path}` — the HTTP path the WHIP server expects `POST` publish requests on. DJI's example uses `/rtc/v1/whip/` — this is the path served by [SRS](https://ossrs.io/)'s WHIP implementation; other WHIP servers use different defaults (e.g., `/whip/{stream}` on MediaMTX, `/whip` on Janus WHIP plugin).
- `{app}` / `{stream}` — query params identifying the logical application and stream name for the publish. DJI's example uses `app=live` and `stream=livestream`.

### 2.1 WHIP handshake

WHIP turns WebRTC publishing into a simple HTTP request/response:

1. The device generates an SDP offer (the publisher side).
2. The device `POST`s the SDP offer to the WHIP URL with `Content-Type: application/sdp`.
3. The WHIP server responds `201 Created` with the SDP answer in the body and a `Location:` header pointing to a resource URL for the publish session.
4. Device and server complete ICE / DTLS / SRTP handshake directly (not via the WHIP URL).
5. Device pushes RTP media (H.264 / VP8 video + Opus audio) to the negotiated ICE candidate.
6. To end the stream: device sends `DELETE` to the `Location:` resource URL, or just tears down the SRTP session.

DJI does not document which codecs or profiles its WHIP ingest emits. Clouds should assume H.264 Baseline / Main and Opus, consistent with standard WebRTC-publisher defaults. Inspect SDP offers during validation.

---

## 3. Device support

| Device | WebRTC / WHIP (`url_type = 4`) | Source |
|---|---|---|
| Dock 3 | ✓ | [`DJI_Cloud/DJI_CloudAPI-Dock3-LiveStream.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock3-LiveStream.txt) |
| Dock 2 | ✓ | [`DJI_Cloud/DJI_CloudAPI-Dock2-Live-Stream.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock2-Live-Stream.txt) |
| RC Plus 2 Enterprise | ✓ | [`DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Stream.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Stream.txt) |
| RC Pro Enterprise | — | v1.15 enum is `{0, 1, 3}` only — no WebRTC |

This is the sharpest cohort asymmetry across the four livestream protocols. An RC-Pro-only deployment cannot use WebRTC; fall back to RTMP, GB28181, or Agora.

The out-of-scope plain RC (non-Enterprise) also lacks WebRTC — same `{0, 1, 3}` enum — per [`DJI_Cloud/DJI_CloudAPI_RC-Live-Stream.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Live-Stream.txt). Documented here as cross-reference; plain RC is not a corpus-supported device.

---

## 4. Cloud-side responsibility

The cloud must host a **WHIP-capable WebRTC ingest endpoint**. Common implementations:

- [SRS](https://ossrs.io/) (≥ 5.0) — SRS's WHIP server serves the `/rtc/v1/whip/` path DJI's example uses; reflects DJI's likely test environment.
- [MediaMTX](https://github.com/bluenviron/mediamtx) — serves WHIP on `/whip/{stream}` per the WHIP spec.
- [Janus WebRTC Server + WHIP plugin](https://janus.conf.meetecho.com/) — enterprise Janus setups.
- Cloudflare Stream Live, Dolby.io Real-time Streaming, and Daily (via custom WHIP endpoints) — commercial WHIP ingest.

The ingest then re-publishes to viewers via any WebRTC viewing interface (WHEP, the pull-side counterpart), HLS, or LL-HLS as the cloud's architecture dictates. WebRTC's value for DJI operations is **low latency** — sub-second glass-to-glass for live operator view, versus ~3–8 seconds typical for HLS off RTMP ingest.

### 4.1 Port / NAT considerations

- WHIP signaling is HTTP (typically 80 / 443) — firewall-friendly.
- Actual media travels over ICE-negotiated UDP (with TCP fallback). The cloud may need **STUN / TURN** servers if the device and cloud sit behind NATs. DJI does not document whether the device uses STUN/TURN autonomously; assume yes for a well-connected dock on a corporate network.

---

## 5. Worked example — complete `live_start_push` payload

MQTT message (Cloud → Device on `thing/product/{gateway_sn}/services`):

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "url_type": 4,
    "url": "http://192.168.1.1:8080/rtc/v1/whip/?app=live&stream=livestream",
    "video_id": "1ZNDH1D0010098/39-0-7/normal-0",
    "video_quality": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "live_start_push"
}
```

The device `POST`s an SDP offer to `http://192.168.1.1:8080/rtc/v1/whip/?app=live&stream=livestream`. The cloud's WHIP endpoint responds with an SDP answer, ICE/DTLS negotiation completes, and the device begins pushing SRTP media.

---

## 6. External references

- [WHIP draft-ietf-wish-whip](https://datatracker.ietf.org/doc/draft-ietf-wish-whip/) — the canonical WHIP spec (still in draft as of 2024 but widely implemented).
- [WebRTC specs at W3C](https://www.w3.org/TR/webrtc/) — WebRTC 1.0.
- [RFC 8834](https://www.rfc-editor.org/rfc/rfc8834) — WebRTC media transports.
- [SRS WHIP documentation](https://ossrs.io/lts/en-us/docs/v5/doc/whip) — reference implementation DJI's example URL path matches.

---

## 7. Source provenance

| Source | Role |
|---|---|
| [`DJI_Cloud/DJI_CloudAPI-Dock3-LiveStream.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock3-LiveStream.txt) | v1.15 primary — Dock 3 `url_type = 4` documentation + URL example + "WHIP only" note. |
| [`DJI_Cloud/DJI_CloudAPI-Dock2-Live-Stream.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock2-Live-Stream.txt) | v1.15 primary — Dock 2 `url_type = 4` documentation + URL example + "WHIP only" note. |
| [`DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Stream.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Stream.txt) | v1.15 primary — RC Plus 2 Enterprise `url_type = 4`. |
| [`DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Live-Stream.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Live-Stream.txt) | v1.15 primary — RC Pro Enterprise (confirms absence of `url_type = 4`). |
| [`../mqtt/dock-to-cloud/services/live_start_push.md`](../mqtt/dock-to-cloud/services/live_start_push.md) | Phase 4d — MQTT signaling spec that invokes this protocol. |
