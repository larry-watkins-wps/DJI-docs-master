# MQTT Protocol Reference

Conventions for every MQTT interaction between the in-scope gateway devices (Dock 2, Dock 3, RC Plus 2 Enterprise, RC Pro Enterprise) and a DJI-Cloud-compatible broker. This document is the canonical home for the MQTT envelope, the topic taxonomy, the full topic list, and per-family envelope specifics.

Per-topic catalog is Phase 4, split by path:
- [`dock-to-cloud/`](dock-to-cloud/README.md) — Dock 2 and Dock 3 method content. **Phase 4a + 4b + 4c landed** (68 methods total: DeviceManagement + Organization + Configuration + WaylineManagement + Live-Flight-Controls incl. DRC). See the path-level index for sub-phase status.
- `pilot-to-cloud/` — RC Plus 2 Enterprise, RC Pro Enterprise, and Pilot-attached aircraft content. *pending*

Divergence between the two paths is at the `method` / event / property **content** level — not at the envelope or topic level, which is why Phase 2 is a single shared document.

---

## 1. Scope

- Protocol: **MQTT 5.0** (`[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/20.mqtt.md]`).
- Transport: TCP/IP.
- Both dock-to-cloud and pilot-to-cloud paths are covered here. They share an identical topic list, envelope, and common-fields table — verified by direct file comparison of the two DJI topic-definition extracts: `[DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt]` (dock-to-cloud) and `[DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt]` (pilot-to-cloud). Both list the same 13 topics, with the same parameterization, the same common-fields table, and structurally identical payload examples.

Out of scope: the **content** of each topic (properties, services, events, DRC methods) — cataloged in Phase 4. HTTPS plane (`http/README.md`), WebSocket plane (`websocket/README.md`), server implementation.

## 2. Topic taxonomy

Verbatim (`[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/20.mqtt.md]`):

| Category | Topic prefix | Explanation |
|---|---|---|
| Basic Topic | `sys/` | Any device has common cloud functionality, such as device registration, device lifecycle status updates and so on. |
| Thing Model Topic | `thing/` | The Topic that supports the implementation of the functions defined by each device thing model — mainly revolves around Property, Service, and Event. |

### 2.1 `{device_sn}` vs `{gateway_sn}` parameterization

Topic templates use one of two serial-number placeholders (`[DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt]` "Topic Overview" note):

- **`{device_sn}`** — serial of the thing-model-bearing device (e.g. the aircraft when the aircraft is the property source). Used by `thing/product/{device_sn}/osd` and `thing/product/{device_sn}/state`.
- **`{gateway_sn}`** — serial of the network-terminating gateway (Dock or RC). Used by every other thing-model topic and by the `sys/product/{gateway_sn}/status` basic topic.

This distinction matters for a cloud implementation because a single MQTT connection terminates at the gateway while property data can originate from the sub-device. A cloud must know the gateway-to-sub-device mapping to correlate OSD / state messages with the owning gateway. The mapping is maintained by the `update_topo` message on `sys/product/{gateway_sn}/status` (see §5.7).

## 3. Topic list

The full authoritative list — all 13 topics, identical in the dock-to-cloud and pilot-to-cloud sources (`[DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt]` lines 23–39, `[DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt]` lines 12–28):

| Topic | Direction | Purpose |
|---|---|---|
| `thing/product/{device_sn}/osd` | Device → Cloud | High-frequency property push (`pushmode=0`). |
| `thing/product/{device_sn}/state` | Device → Cloud | On-change property push (`pushmode=1`). |
| `thing/product/{gateway_sn}/services` | Cloud → Device | Cloud-issued services / commands. |
| `thing/product/{gateway_sn}/services_reply` | Device → Cloud | Device's reply and processing result for a service. |
| `thing/product/{gateway_sn}/events` | Device → Cloud | Events the device needs the cloud to observe. |
| `thing/product/{gateway_sn}/events_reply` | Cloud → Device | Cloud's acknowledgment of an event. |
| `thing/product/{gateway_sn}/requests` | Device → Cloud | Device-initiated requests (e.g. temporary credentials). |
| `thing/product/{gateway_sn}/requests_reply` | Cloud → Device | Cloud's reply to a request. |
| `sys/product/{gateway_sn}/status` | Device → Cloud | Device online / offline / topology update. |
| `sys/product/{gateway_sn}/status_reply` | Cloud → Device | Platform's reply to a status update. |
| `thing/product/{gateway_sn}/property/set` | Cloud → Device | Cloud-initiated property set. |
| `thing/product/{gateway_sn}/property/set_reply` | Device → Cloud | Device's result for a property set. |
| `thing/product/{gateway_sn}/drc/up` | Device → Cloud | DRC (direct remote control) upward. |
| `thing/product/{gateway_sn}/drc/down` | Cloud → Device | DRC downward (real-time flight control commands). |

Each topic maps to one or more Phase 4 per-topic catalog entries under `mqtt/dock-to-cloud/` or `mqtt/pilot-to-cloud/`. Service / event / request families sub-divide into per-`method` entries.

## 4. Message envelope

Verbatim (`[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/20.mqtt.md]`):

```json
{
  "tid": "xxxx",
  "bid": "xxxx",
  "method": "xxx",
  "data": {
    "properties": {},
    "result": {},
    "output": {},
    "event": {}
  },
  "timestamp": "xxxx"
}
```

Common fields — from `[DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt]` "Common Fields Explanation":

| Field | Type | Description |
|---|---|---|
| `tid` | string (UUID) | **Transaction UUID** — one message exchange (request + response, alarm event). Used to correlate a reply to its request. |
| `bid` | string (UUID) | **Business UUID** — groups transactions that form one business flow (e.g., on-demand / download / playback). Enables multi-step state tracking. |
| `timestamp` | integer | 13-digit millisecond Unix timestamp at send time. |
| `gateway` | string | Serial number of the gateway device sending the message. |
| `data` | object | Message content. Shape varies by topic family — see §5. |
| `method` | string | (Thing-model topics only.) Identifier of the service / event / request in the thing-model spec. Not present on `osd` / `state` / `property/set`. |

## 5. Per-family envelope specifics

All payloads below are verbatim from `[DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt]` (envelope-identical to the pilot-to-cloud source per §1). The examples show envelope shape and field positioning; per-method content lives in Phase 4.

### 5.1 `osd` — `thing/product/{device_sn}/osd`

High-frequency property push. No `method` field; `data` carries properties directly.

Representative payload — **dock-OSD content** (pilot-OSD content has a different property set; see §9 / OQ-002):

```json
{
  "tid": "43d2e632-1558-4c4e-83d2-eeb51b7a377a",
  "bid": "7578f2ac-1f12-4d47-9ab6-5de146ed7b8a",
  "timestamp": 1667220916697,
  "data": {
    "drone_in_dock": 1,
    "rainfall": 0,
    "wind_speed": 0,
    "environment_temperature": 24,
    "latitude": 22.907809968,
    "longitude": 113.703482143,
    "mode_code": 1,
    "cover_state": 0,
    "sub_device": {
      "device_sn": "1581F5BKD225D00BP891",
      "device_model_key": "0-67-0",
      "device_online_status": 0,
      "device_paired": 1
    }
  },
  "gateway": "dock_sn"
}
```

### 5.2 `state` — `thing/product/{device_sn}/state`

On-change property push. Same envelope as `osd`; `data` carries only the properties that changed.

```json
{
  "tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
  "bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
  "timestamp": 1598411295123,
  "gateway": "sn",
  "data": {}
}
```

### 5.3 `services` / `services_reply` — cloud-initiated commands

```json
// services — cloud → device
{
  "tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
  "bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
  "timestamp": 1598411295123,
  "gateway": "sn",
  "method": "some_method",
  "data": {}
}

// services_reply — device → cloud
{
  "tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
  "bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
  "timestamp": 1598411295123,
  "gateway": "sn",
  "method": "some_method",
  "data": {
    "result": 0,
    "output": {}
  }
}
```

Reply `data` fields (`[DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt]`):
- `result` — device's response code. `0` is success; non-zero is an error.
- `output` — optional response payload from the device.

### 5.4 `events` / `events_reply`

Events carry an additional `need_reply` field on the request: `0` = no reply needed, `1` = reply needed.

```json
// events — device → cloud
{
  "tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
  "bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
  "timestamp": 1598411295123,
  "need_reply": 0,
  "gateway": "sn",
  "method": "some_method",
  "data": {}
}

// events_reply — cloud → device (only when need_reply == 1)
{
  "tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
  "bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
  "timestamp": 1598411295123,
  "gateway": "sn",
  "method": "some_method",
  "data": {
    "result": 0
  }
}
```

### 5.5 `requests` / `requests_reply` — device-initiated

Same shape as services but with the direction reversed. The device asks; the cloud answers.

```json
// requests — device → cloud
{
  "tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
  "bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
  "timestamp": 1598411295123,
  "gateway": "sn",
  "method": "some_method",
  "data": {}
}

// requests_reply — cloud → device
{
  "tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
  "bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
  "timestamp": 1598411295123,
  "gateway": "sn",
  "method": "some_method",
  "data": {
    "result": 0,
    "output": {}
  }
}
```

### 5.6 `property/set` / `property/set_reply`

```json
// property/set — cloud → device
{
  "tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
  "bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
  "timestamp": 1598411295123,
  "data": {
    "some_property": "some_value"
  }
}

// property/set_reply — device → cloud
{
  "tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
  "bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
  "timestamp": 1598411295123,
  "data": {
    "some_property": {
      "result": 0
    }
  }
}
```

Per-property reply `result` codes (`[DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt]` property set_reply section):
- `0` — success
- `1` — fail
- `2` — time exceed
- other — refer to error code

A property is settable only if its thing-model `accessMode == 2`. Accessibility is defined in Phase 6 `device-properties/` entries.

### 5.7 `status` / `status_reply` — topology

Both the initial topology publish and all topology updates go on `sys/product/{gateway_sn}/status` with `method: update_topo`.

Gateway device and sub-device online:

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "update_topo",
  "timestamp": 1234567890123,
  "data": {
    "type": 98,
    "sub_type": 0,
    "device_secret": "secret",
    "nonce": "nonce",
    "version": 1,
    "sub_devices": [
      {
        "sn": "drone001",
        "type": 116,
        "sub_type": 0,
        "index": "A",
        "device_secret": "secret",
        "nonce": "nonce",
        "version": 1
      }
    ]
  }
}
```

Sub-device offline — same method, `sub_devices` becomes `[]`:

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "update_topo",
  "timestamp": 1234567890123,
  "data": {
    "type": 98,
    "sub_type": 0,
    "device_secret": "secret",
    "nonce": "nonce",
    "version": 1,
    "sub_devices": []
  }
}
```

Reply carries `data.result` (integer; `0` is success). The `type` / `sub_type` enums resolve to specific device models — canonical enum catalog is in Phase 6 (`device-properties/README.md`).

Gateway offline is inferred by the MQTT-level disconnect (PINGRESP timeout or Last Will message); there is no explicit `update_topo` call for it.

### 5.8 `drc/up` / `drc/down` — direct remote control

Low-latency flight-control channel. Envelope is lighter than the other thing-model families — no `tid` / `bid` / `timestamp` in DJI's examples; a `seq` field sequences commands.

```json
// drc/down — cloud → device
{
  "method": "drone_emergency_stop",
  "seq": 1,
  "data": {}
}

// drc/up — device → cloud
{
  "method": "drone_emergency_stop",
  "seq": 1,
  "data": {
    "result": 0
  }
}
```

Verbatim example of a `drone_control` drc/down command (`[DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt]`):

```json
{
  "method": "drone_control",
  "data": {
    "seq": 1,
    "x": 2.34,
    "y": -2.45,
    "h": 2.76,
    "w": 2.86
  }
}
```

Per-method DRC payloads (`drone_control`, `drone_emergency_stop`, etc.) are cataloged in Phase 4 under `mqtt/.../drc/`.

## 6. Request-reply pattern

Every topic pair ending in `_reply` follows the same rule:

1. The initiator publishes on the base topic with a fresh `tid` (and `bid` grouping any related exchange).
2. The responder publishes on the `_reply` topic carrying the **same** `tid` and `bid`, plus `data.result`.

This is how the cloud matches a response to its outstanding request — `tid` is the correlation key. `bid` groups multiple `tid`-scoped transactions into one business flow (relevant for multi-step choreographies such as wayline upload + execution or firmware distribution + install).

## 7. Status lifecycle

DJI's three-state model (verbatim, `[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/10.proper-noun.md]`):

> Indicates the network status of the device, which can be divided into online, disconnected and offline. Disconnected for the persistent connection of the device without notification, can be understood as the network caused by offline. Offline is triggered by human consciousness, such as task completion, gateway device shutdown and other actions triggered.

Observed transport signals:

- `sys/product/{gateway_sn}/status` with `method: update_topo` — explicit online transitions and topology changes.
- MQTT-level disconnect (PINGRESP timeout or MQTT Last Will) — implicit `disconnected` state.
- Explicit `update_topo` with empty `sub_devices` or cloud-issued shutdown — deliberate `offline`.

## 8. QoS, retain, clean session

DJI's published documentation does **not** specify QoS, `retain`, or clean-session settings per topic. The MQTT-concept page (`[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/20.mqtt.md]`) covers all three QoS levels generically but does not state which DJI uses for which topic family. Neither topic-definition extract (`[DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt]`, `[DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt]`) pins these values either.

Tracked as [`OQ-003`](../OPEN-QUESTIONS.md#oq-003--mqtt-qos-retain-and-clean-session-settings-are-not-specified-in-djis-published-documentation). Phase 4 per-topic entries must not cite QoS or `retain` values unless a concrete source (the deprecated demo code, live packet capture) supports them.

## 9. Known documentation issue — pilot-to-cloud OSD example

The pilot-to-cloud topic-definition file (`[DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt]`) shows an OSD struct example that is byte-identical (modulo whitespace) to the dock-to-cloud example — i.e. the Pilot-path example presents **Dock OSD content** (`drone_in_dock`, `cover_state`, dock environmental sensors, etc.) that a Pilot-attached aircraft does not publish. This is a DJI documentation copy-paste bug: the pilot-to-cloud envelope is correct, but the OSD example payload is not representative of what the Pilot path actually reports.

Tracked as [`OQ-002`](../OPEN-QUESTIONS.md#oq-002--pilot-to-cloud-osd-struct-example-appears-to-be-a-copy-paste-of-the-dock-osd-example). Implication for Phase 4: `mqtt/pilot-to-cloud/osd.md` must cite the per-aircraft property catalogs (e.g. `[DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt]`, `[DJI_Cloud/DJI_CloudAPI_Mavic3-Enterprise_Properties.txt]`, `[DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt]`) rather than the OSD example in this topic-definition file.

## 10. What this document is not

- Not a per-topic catalog. Full per-topic entries (one `.md` per topic or `method`) live in Phase 4 under `mqtt/dock-to-cloud/` and `mqtt/pilot-to-cloud/`.
- Not a property reference. Property names, types, units, and thing-model structure are in Phase 6 (`device-properties/`).
- Not a device-enum reference. `type` / `sub_type` decoding is in Phase 6.
- Not a workflow reference. Binding, wayline execution, DRC, HMS, and other choreographies live in Phase 9 (`workflows/`).

## 11. Source provenance

| Source | Role in this doc |
|---|---|
| `[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/20.mqtt.md]` | Canonical MQTT protocol reference, topic-prefix table, message envelope shape (§2, §4). |
| `[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/10.proper-noun.md]` | Online / disconnected / offline definitions (§7). |
| `[DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt]` | v1.15 dock-to-cloud topic list, common-fields table, per-family payload examples (§2.1, §3, §4, §5). |
| `[DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt]` | v1.15 pilot-to-cloud topic-definition file — used to verify envelope identity with the dock-to-cloud source (§1), and as the origin of the OSD copy-paste issue flagged in §9. |

Verbatim quotations are fenced and cited inline. Nothing is paraphrased where a direct quote carries the same load.
