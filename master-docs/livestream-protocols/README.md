# `livestream-protocols/` — media-transport protocol reference

Per-protocol wire specifics for the four media-transport protocols DJI devices use to push a live video stream to a cloud-hosted streaming server. The entry point from the signaling plane is the MQTT `live_start_push` command, whose `url_type` + `url` fields pick the protocol and its endpoint parameters. This directory documents what each `url` shape means and what the cloud must host or terminate for each protocol.

The signaling — how a livestream is started, switched, qualified, and stopped over MQTT — lives in [`../mqtt/dock-to-cloud/services/live_start_push.md`](../mqtt/dock-to-cloud/services/live_start_push.md) (+ `live_stop_push`, `live_set_quality`, `live_lens_change`, `live_camera_change`). This directory's docs cross-reference those but do not duplicate them.

## Docs

| Protocol | Doc | `url_type` (MQTT) | In-scope devices |
|---|---|---|---|
| RTMP | [`rtmp.md`](rtmp.md) | `1` | Dock 2, Dock 3, RC Plus 2 Enterprise, RC Pro Enterprise |
| GB28181 | [`gb28181.md`](gb28181.md) | `3` | Dock 2, Dock 3, RC Plus 2 Enterprise, RC Pro Enterprise |
| WebRTC (WHIP) | [`webrtc.md`](webrtc.md) | `4` | Dock 2, Dock 3, RC Plus 2 Enterprise (**not** RC Pro Enterprise) |
| Agora | [`agora.md`](agora.md) | `0` | Dock 2, RC Plus 2 Enterprise, RC Pro Enterprise (**not** Dock 3) |

---

## 1. Device support matrix

| `url_type` | Protocol | Dock 3 | Dock 2 | RC Plus 2 Enterprise | RC Pro Enterprise |
|---|---|---|---|---|---|
| `0` | Agora | — | ✓ | ✓ | ✓ |
| `1` | RTMP | ✓ | ✓ | ✓ | ✓ |
| `3` | GB28181 | ✓ | ✓ | ✓ | ✓ |
| `4` | WebRTC (WHIP) | ✓ | ✓ | ✓ | — |

Notable asymmetries:

- **Dock 3 drops Agora** — v1.15 [`DJI_CloudAPI-Dock3-LiveStream.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock3-LiveStream.txt) `url_type` enum lists only `{1: RTMP, 3: GB28181, 4: WebRTC}`. The v1.15 example payload in that file still uses `url_type: 0`, which appears to be a copy-paste defect from Dock 2 — see [`../mqtt/dock-to-cloud/services/live_start_push.md`](../mqtt/dock-to-cloud/services/live_start_push.md) §Source inconsistencies.
- **RC Pro Enterprise drops WebRTC** — v1.15 [`DJI_CloudAPI_RC-Pro-Enterprise-Live-Stream.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Live-Stream.txt) `url_type` enum lists only `{0: Agora, 1: RTMP, 3: GB28181}`.
- **`url_type` value `2` is skipped** — never used in any v1.15 MQTT source. Historical note: v1.11 pilot-feature-set prose mentioned RTSP; the JSBridge pilot-webview API (see §3) uses a separate type enum that includes RTSP at position `3`. The MQTT wire contract does not expose RTSP.

---

## 2. Scope rules

Each per-protocol doc covers:

1. **The DJI `url` parameter shape** — what the cloud must parse out of the `url` string to identify the stream destination. Real examples from v1.15 source.
2. **Device support notes** — which cohorts emit which protocol; DJI source inconsistencies where relevant.
3. **Cloud-side responsibility** — what server component must be available on the cloud (e.g. "an RTMP ingest server", "a GB28181 SIP server", "a WHIP endpoint").
4. **Links to the underlying external standards** — RFC / GB/T / W3C / vendor docs — without restating them. These protocols are established standards; the corpus is not a protocol-reference compendium.

Each doc does **not** redocument the MQTT envelope, the `live_start_push` signaling sequence, the per-cohort enum details of `video_quality`, or anything else that lives in [`../mqtt/dock-to-cloud/services/live_start_push.md`](../mqtt/dock-to-cloud/services/live_start_push.md). Those docs cross-reference back to this directory for `url` shape details.

---

## 3. Pilot-side JSBridge layer (cross-transport context)

DJI Pilot 2's webview hosts a JavaScript bridge (`window.djiBridge.liveshareGetConfig` / `liveshareSetConfig`) that lets a Pilot-embedded webview page interact with the Pilot app's live-streaming subsystem. This layer uses a **different `type` enum** from MQTT:

| JSBridge `type` | Meaning |
|---|---|
| `0` | Unknown |
| `1` | Agora |
| `2` | RTMP |
| `3` | RTSP |
| `4` | GB28181 |

The JSBridge `type` is not directly compatible with the MQTT `url_type`. A cloud operating a Pilot webview that also signals livestreams over MQTT must translate between the two (JSBridge `type=1 Agora` → MQTT `url_type=0`; `type=2 RTMP` → MQTT `url_type=1`; etc.) and must not forward `type=3 RTSP` to MQTT (MQTT does not expose RTSP). JSBridge is pilot-only and a secondary integration path; the corpus treats MQTT as the primary livestream signaling plane. See [`DJI_Cloud/DJI_CloudAPI_Pilot-JSBridge.txt`](../../DJI_Cloud/DJI_CloudAPI_Pilot-JSBridge.txt) for the JSBridge definition (lines 107–145 in v1.15).

---

## 4. Related

- [`../mqtt/dock-to-cloud/services/live_start_push.md`](../mqtt/dock-to-cloud/services/live_start_push.md) — MQTT entry point for starting a livestream.
- [`../mqtt/dock-to-cloud/services/live_stop_push.md`](../mqtt/dock-to-cloud/services/live_stop_push.md) — stop a livestream.
- [`../mqtt/dock-to-cloud/services/live_set_quality.md`](../mqtt/dock-to-cloud/services/live_set_quality.md) — mid-stream quality adjustment.
- [`../mqtt/dock-to-cloud/services/live_camera_change.md`](../mqtt/dock-to-cloud/services/live_camera_change.md) — switch between dock FPV cameras (dock-to-cloud only).
- [`../mqtt/dock-to-cloud/services/live_lens_change.md`](../mqtt/dock-to-cloud/services/live_lens_change.md) — switch lens (wide / zoom / IR / normal).
- Workflow: deferred to Phase 9 `workflows/livestream-start-stop.md`.
