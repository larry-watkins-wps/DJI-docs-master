# WebSocket Protocol Reference

Conventions for every server-to-client WebSocket push between a DJI-Cloud-compatible server and DJI Pilot 2 (plus any web clients sharing Pilot's workspace context). This document is the canonical home for the WebSocket envelope and session lifecycle.

Per-message catalog is [`map-elements/`](map-elements/) and [`situation-awareness/`](situation-awareness/) — **Phase 5 landed** (8 push messages, pilot-to-cloud only). Jump table below in §4.

---

## 1. Scope

**Pilot-to-Cloud only.** The WebSocket channel is established by DJI Pilot 2 against the third-party cloud. The Dock path (Dock 2, Dock 3) does **not** use WebSocket — dock-side push is delivered over MQTT (`sys/product/{gateway_sn}/status`, `thing/product/{gateway_sn}/events`, etc.). See architecture §5.3 for the cross-transport map.

## 2. Session lifecycle

Verbatim (`[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/50.websocket.md]`):

> For some features, Websocket communication is required, so DJI Pilot 2 and the server need to establish a WebSocket channel. When DJI Pilot 2 logs in and goes online through Webview, the server needs to respond to the URL address of the WebSocket to DJI Pilot 2, and then DJI Pilot 2 will make a WebSocket connection request.

Two-step handshake:

1. **Login over HTTPS Webview.** The server returns the WebSocket URL alongside the `X-Auth-Token` in the login response (or via JSBridge). See [`http/README.md`](../http/README.md) §4 for the auth-header convention.
2. **WebSocket connect.** Pilot 2 opens the WebSocket connection to that URL.

Session lifetime tracks the Pilot Webview login session. On re-login, the server may issue a new WebSocket URL; implementations should not assume URL stability across logins.

## 3. Message envelope

Verbatim (`[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/50.websocket.md]`):

```json
{
    "biz_code": "device_topo_update",
    "version": "1.0",
    "timestamp": 146052438362,
    "data": {
        "operator": "zhangsan"
    }
}
```

Common fields:

| Field | Type | Description |
|---|---|---|
| `biz_code` | string | Business code identifying the push-message type. Determines the shape of `data`. |
| `version` | string | Protocol version, e.g. `"1.0"`. |
| `timestamp` | integer | 13-digit millisecond Unix timestamp at send time. |
| `data` | object | Message-specific payload. Shape varies by `biz_code` — see Phase 5 per-message docs. |

No `sub_biz_code` field appears in the v1.15 Pilot-WebSocket extracts (`[DJI_Cloud/DJI_CloudAPI_Pilot-WebSocket-Map-Elements-Push-Message.txt]`, `[DJI_Cloud/DJI_CloudAPI_Pilot-WebSocket-Situation-Awareness-Push-Message.txt]`). The canonical v1.11 page comments that "the specific content is adjusted with `biz_code` or `sub_biz_code`", but the v1.15 sample bodies are addressed by `biz_code` alone. Phase 5 entries should flag any new observation if `sub_biz_code` appears in future messages.

## 4. Message families in v1.15

The in-repo v1.15 extract documents exactly two WebSocket message families. Per-message payloads are cataloged in Phase 5; this section is inventory only.

### 4.1 Map Elements

Source: `[DJI_Cloud/DJI_CloudAPI_Pilot-WebSocket-Map-Elements-Push-Message.txt]`.

| `biz_code` | Doc | Purpose |
|---|---|---|
| `map_element_create` | [`map-elements/map_element_create.md`](map-elements/map_element_create.md) | A map element was created. `data.resource.content` carries a GeoJSON Feature. |
| `map_element_update` | [`map-elements/map_element_update.md`](map-elements/map_element_update.md) | A map element was updated. Same GeoJSON Feature shape as create. |
| `map_element_delete` | [`map-elements/map_element_delete.md`](map-elements/map_element_delete.md) | A map element was deleted. `data` carries only `id` and `group_id`. |
| `map_group_refresh` | [`map-elements/map_group_refresh.md`](map-elements/map_group_refresh.md) | Batch-refresh signal: `data.ids` is an array of element IDs to re-fetch via HTTP `map/obtain`. |

### 4.2 Situation Awareness

Source: `[DJI_Cloud/DJI_CloudAPI_Pilot-WebSocket-Situation-Awareness-Push-Message.txt]`.

| `biz_code` | Doc | Purpose |
|---|---|---|
| `device_osd` | [`situation-awareness/device_osd.md`](situation-awareness/device_osd.md) | Fixed-frequency telemetry push for all devices in the workspace. `data.host` carries position / altitude / speed; `data.sn` carries the device SN. |
| `device_online` | [`situation-awareness/device_online.md`](situation-awareness/device_online.md) | A workspace device came online. Pilot reacts by calling `Obtain Device Topology List` over HTTPS. |
| `device_offline` | [`situation-awareness/device_offline.md`](situation-awareness/device_offline.md) | A workspace device went offline. Pilot reacts the same way. |
| `device_update_topo` | [`situation-awareness/device_update_topo.md`](situation-awareness/device_update_topo.md) | The device topology changed. Pilot reacts the same way. |

## 5. Push-and-fetch coordination pattern

A specific coordination pattern recurs across the situation-awareness messages. Verbatim (`[DJI_Cloud/DJI_CloudAPI_Pilot-WebSocket-Situation-Awareness-Push-Message.txt]`):

> When the server receives a request for any device in the same workspace to come online, it also broadcasts a push to DJI Pilot 2 via WebSocket, and when DJI Pilot 2 receives the push, it will trigger the "Obtain Device Topology List".

The same mechanism applies to `device_offline` and `device_update_topo`: the WebSocket push does not carry the topology itself — it only signals a change. Pilot then fetches authoritative state via the HTTPS topology-list endpoint.

Implication for a cloud implementation: the two transports must be coordinated. The WebSocket push should fire **after** the MQTT topology update has been reconciled into the server-side workspace state, so that Pilot's follow-up HTTPS fetch returns consistent topology. A naïve implementation that pushes on the WebSocket before persisting topology can cause Pilot to see stale device lists.

The end-to-end choreography (MQTT `update_topo` → server persistence → WebSocket broadcast → Pilot HTTPS fetch) is the business of Phase 9 workflows; this document only states the pattern.

## 6. What this document is not

- Not a per-message catalog. Per-message schemas live in Phase 5.
- Not a workflow reference. The push-and-fetch pattern of §5 is the wire shape only; end-to-end choreography is Phase 9.
- Not a transport for Dock. Dock devices do not use WebSocket — see [`mqtt/README.md`](../mqtt/README.md) §3.

## 7. Source provenance

| Source | Role in this doc |
|---|---|
| `[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/50.websocket.md]` | Canonical WebSocket intro, session-lifecycle quote, envelope example (§2, §3). |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-WebSocket-Map-Elements-Push-Message.txt]` | v1.15 map-elements family inventory (§4.1). |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-WebSocket-Situation-Awareness-Push-Message.txt]` | v1.15 situation-awareness family inventory and push-and-fetch quote (§4.2, §5). |

Verbatim quotations are fenced and cited inline. Nothing is paraphrased where a direct quote carries the same load.
