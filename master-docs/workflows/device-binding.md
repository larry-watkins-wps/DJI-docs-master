# Device binding and topology lifecycle

What the cloud and devices do, on the wire, after pairing completes and while the workspace is active. Covers the topology-maintenance loop (pair / unpair, online / offline), OSD telemetry, state-change events, and writable property sets. This is the always-on traffic every cohort produces — dock path and pilot path alike.

Part of the Phase 9 workflow catalog. Schema bodies live in Phase 4 (MQTT) / Phase 5 (WebSocket) / Phase 6 (device properties).

---

## Scope

| Aspect | Value |
|---|---|
| Cohorts | **All in-scope cohorts** — Dock 2 cohort (dock-path), Dock 3 cohort (dock-path), RC Pro Enterprise (pilot-path), RC Plus 2 Enterprise (pilot-path). |
| Direction | Mostly device-initiated push. `property/set` is the one cloud-initiated path. |
| Transports | **MQTT** for wire traffic. **WebSocket** for cloud → Pilot-2 change signals. **HTTP** for Pilot-2 topology read-back. |
| Preceding workflow | [`dock-bootstrap-and-pairing.md`](dock-bootstrap-and-pairing.md) for docks. RC pairing runs a JSBridge-driven flow — see [`remote-control-handoff.md`](remote-control-handoff.md) *(pending Phase 9c)*. |
| Related catalog entries | [`update_topo` dock-path](../mqtt/dock-to-cloud/status/update_topo.md), [`update_topo` pilot-path](../mqtt/pilot-to-cloud/status/update_topo.md), [`osd/` dock](../mqtt/dock-to-cloud/osd/README.md) / [pilot](../mqtt/pilot-to-cloud/osd/README.md), [`state/` dock](../mqtt/dock-to-cloud/state/README.md) / [pilot](../mqtt/pilot-to-cloud/state/README.md), [`property-set/` dock](../mqtt/dock-to-cloud/property-set/README.md) / [pilot](../mqtt/pilot-to-cloud/property-set/README.md), [`device-properties/`](../device-properties/README.md), [WebSocket situation-awareness](../websocket/situation-awareness/), [HTTP topology](../http/device/topology.md) |

## Overview

Once a gateway (dock or RC) has paired against the cloud, it assumes responsibility for four ongoing duties:

1. **Topology maintenance.** Any time the sub-device composition changes — aircraft attached, aircraft detached — the gateway re-publishes a full `update_topo` snapshot.
2. **OSD telemetry.** High-rate (0.5 Hz) push of flight-envelope / battery / position / camera telemetry on the `osd` topic. Lossy by design; no reply expected.
3. **State-change events.** Lower-rate push on the `state` topic when a property changes value (mode code, firmware version, SIM-slot switch, etc.).
4. **Property-set response.** When the cloud writes to a writable property (accessMode `rw`), the gateway routes the change to the device and returns a result envelope.

The cloud's responsibility is to consume these feeds, reconcile its workspace view, and push change signals to any attached Pilot 2 UI so it can re-read topology via HTTP.

## Actors

| Actor | Role |
|---|---|
| **Gateway** | Dock 2 / Dock 3 for dock-path; RC Plus 2 / RC Pro for pilot-path. Owns `{gateway_sn}` on every topic. |
| **Sub-device** | Aircraft (M3D / M3TD / M4D / M4TD). Reports telemetry through the gateway under `{device_sn}` = aircraft SN on the `osd` / `state` topics; does not own any MQTT topic directly. |
| **Cloud Server** | Consumes push; publishes property-set commands; relays change signals to any WebSocket clients (Pilot 2). |
| **Pilot 2 (optional)** | WebSocket subscriber (pilot-path only — the WebSocket surface is Pilot-to-Cloud only per [`websocket/README.md`](../websocket/README.md)). Receives `device_*` change signals; reads current topology via HTTP. |

## Sequence

### Dock-path

```mermaid
sequenceDiagram
    participant aircraft as Aircraft
    participant dock as DJI Dock
    participant cloud as Cloud Server

    note over aircraft,cloud: Pairing complete (see dock-bootstrap-and-pairing.md)

    note over aircraft,dock: Aircraft connects / is powered
    aircraft ->> dock: internal link up
    dock ->> cloud: sys/product/{gateway_sn}/status<br/>method: update_topo<br/>{ sub_devices: [{ sn: drone_sn, ... }] }
    cloud -->> dock: status_reply { result: 0 }

    loop OSD at 0.5 Hz
        aircraft ->> dock: internal telemetry
        dock ->> cloud: thing/product/{device_sn}/osd<br/>(aircraft OSD payload)
        dock ->> cloud: thing/product/{device_sn}/osd<br/>(dock OSD payload)
    end

    opt State change (discrete)
        aircraft ->> dock: property value changed
        dock ->> cloud: thing/product/{device_sn}/state<br/>(changed property delta)
    end

    opt Cloud writes a writable property
        cloud ->> dock: thing/product/{gateway_sn}/property/set<br/>{ property_key: value }
        dock ->> aircraft: route to aircraft if aircraft-owned
        aircraft -->> dock: internal ack
        dock -->> cloud: thing/product/{gateway_sn}/property/set_reply<br/>{ result: 0 }
    end

    note over aircraft,dock: Aircraft disconnects
    aircraft --x dock: internal link down
    dock ->> cloud: sys/product/{gateway_sn}/status<br/>method: update_topo<br/>{ sub_devices: [] }
    cloud -->> dock: status_reply { result: 0 }
```

### Pilot-path

```mermaid
sequenceDiagram
    participant aircraft as Aircraft
    participant rc as RC
    participant cloud as Cloud Server
    participant pilot as Pilot 2 (WebSocket)

    note over rc,cloud: Pairing complete (RC-side JSBridge flow)

    note over aircraft,rc: Aircraft paired to RC
    rc ->> cloud: sys/product/{gateway_sn}/status<br/>method: update_topo<br/>{ sub_devices: [{ sn: drone_sn, ... }] }
    cloud -->> rc: status_reply { result: 0 }

    cloud ->> pilot: WS device_update_topo push
    pilot ->> cloud: HTTP GET /manage/api/v1/workspaces/{workspace_id}/devices/topologies
    cloud -->> pilot: topology snapshot

    loop OSD at 0.5 Hz
        aircraft ->> rc: internal telemetry
        rc ->> cloud: thing/product/{device_sn}/osd<br/>(aircraft OSD payload)
        cloud ->> pilot: WS device_osd push
    end

    opt State change (discrete)
        aircraft ->> rc: property value changed
        rc ->> cloud: thing/product/{device_sn}/state<br/>(changed property delta)
    end

    opt Cloud writes a writable aircraft property
        cloud ->> rc: thing/product/{gateway_sn}/property/set<br/>{ property_key: value }
        rc ->> aircraft: route to aircraft
        aircraft -->> rc: internal ack
        rc -->> cloud: thing/product/{gateway_sn}/property/set_reply<br/>{ result: 0 }
    end

    note over aircraft,rc: Aircraft unpaired
    rc ->> cloud: sys/product/{gateway_sn}/status<br/>method: update_topo<br/>{ sub_devices: [] }
    cloud -->> rc: status_reply { result: 0 }
    cloud ->> pilot: WS device_offline or device_update_topo
```

## Step-by-step

### 1. Topology push on pair / unpair

- **Topic:** `sys/product/{gateway_sn}/status`. **Method:** `update_topo`.
- **Full-snapshot semantics.** Every `update_topo` is the complete current topology, not a delta. An empty `sub_devices` array means no aircraft paired.
- **Dock vs RC.** Payload schema is identical; only `{gateway_sn}` and `sub_devices[0].sn` differ. Schema body: [dock-path](../mqtt/dock-to-cloud/status/update_topo.md) · [pilot-path](../mqtt/pilot-to-cloud/status/update_topo.md).
- **Cloud fan-out.** The cloud converts each `update_topo` into one or more situation-awareness WebSocket pushes for any Pilot 2 subscribers: [`device_online`](../websocket/situation-awareness/device_online.md), [`device_offline`](../websocket/situation-awareness/device_offline.md), [`device_update_topo`](../websocket/situation-awareness/device_update_topo.md). Pilot 2 uses these as triggers to re-read [HTTP topology](../http/device/topology.md) rather than parsing the WebSocket body.

### 2. OSD telemetry at 0.5 Hz

- **Topic:** `thing/product/{device_sn}/osd`. No method key; raw struct in `data`.
- `{device_sn}` is the **reporting** device's SN — a dock reports both its own dock OSD under the dock SN and the aircraft's OSD under the aircraft SN; the two streams are on separate topics.
- **No reply.** OSD is fire-and-forget. The cloud's default subscribe QoS is 1 per [OQ-003](../OPEN-QUESTIONS.md#oq-003--mqtt-qos-retain-and-clean-session-settings-are-not-specified-in-djis-published-documentation), meaning the broker caps delivery at QoS 1 even if devices publish higher.
- **Payload catalog.** Per Phase 6: dock-path property set differs from pilot-path for the same aircraft (17 dock-path-exclusive properties, 1 pilot-path-exclusive, occasional type drift on shared properties). Full matrix: [`device-properties/README.md`](../device-properties/README.md). Per-device payload bodies: [`device-properties/dock2.md`](../device-properties/dock2.md), [`dock3.md`](../device-properties/dock3.md), [`m3d.md`](../device-properties/m3d.md), [`m3td.md`](../device-properties/m3td.md), [`m4d.md`](../device-properties/m4d.md), [`m4td.md`](../device-properties/m4td.md), [`rc-plus-2.md`](../device-properties/rc-plus-2.md), [`rc-pro.md`](../device-properties/rc-pro.md).
- **Cloud fan-out.** For pilot-path OSD, the cloud pushes [`device_osd`](../websocket/situation-awareness/device_osd.md) to WebSocket subscribers.

### 3. State-change events (push on change)

- **Topic:** `thing/product/{device_sn}/state`. Direction: up.
- Published when a `state` property (pushMode `1`) changes value. Not all properties participate — the `device-properties/` per-device files mark each property's pushMode.
- State pushes carry only the changed field(s), not the full state snapshot. Cloud should treat the payload as a delta applied over last known state.
- Per Phase 6a: Dock 2 state: 12 properties; Dock 3 state: 12 (same). Per Phase 6b: aircraft state (pilot-path baseline): 8 properties; dock-path adds 10 more. Per Phase 6c: RC state: 5 properties each.

### 4. Writable property sets (cloud-initiated)

- **Topic (down):** `thing/product/{gateway_sn}/property/set`. **Reply (up):** `thing/product/{gateway_sn}/property/set_reply`.
- Writable property surface per Phase 6 (Phase 4i speculative lists were corrected at 6a/6c):
  - **Dock gateway (Dock 2 + Dock 3):** 3 writable properties — `silent_mode`, `user_experience_improvement`, `air_transfer_enable`.
  - **Aircraft dock-path:** 6 writable — `height_limit`, `night_lights_state`, `distance_limit_status`, `obstacle_avoidance`, `rth_altitude`, `rth_mode`.
  - **Aircraft pilot-path (baseline):** 3 writable — `height_limit`, `night_lights_state`, `camera_watermark_settings`. **M4D adds 3 more pilot-path writable:** `commander_flight_height`, `commander_flight_mode`, `commander_mode_lost_action` (per Phase 6b).
  - **RC gateway (RC Plus 2 + RC Pro):** **0 writable.** The `property/set` topic on an RC SN is only used for aircraft-targeted writes (the aircraft's writable surface travels with the aircraft regardless of gateway).
- **Single-field writes only.** DJI's feature-set page calls this out: writing a nested struct (e.g., `distance_limit_status` has `state` and `distance_limit` fields) requires two separate `property/set` commands, one per field.
- Schema shells: [dock-path `property-set/`](../mqtt/dock-to-cloud/property-set/README.md) · [pilot-path `property-set/`](../mqtt/pilot-to-cloud/property-set/README.md).

### 5. Cloud → Pilot 2 change fan-out

- Applies to pilot-path only (WebSocket is Pilot-to-Cloud only).
- Every `update_topo` that represents a topology delta converts to `device_online` / `device_offline` / `device_update_topo` WebSocket messages ([`websocket/situation-awareness/`](../websocket/situation-awareness/)).
- Pilot 2 treats WebSocket push as a **change signal** (trigger), then re-reads authoritative topology from HTTP [`/manage/api/v1/workspaces/{workspace_id}/devices/topologies`](../http/device/topology.md). The WebSocket body carries enough to identify which device changed, not the full topology.

## Variants

### Dock 2 cohort vs Dock 3 cohort

- No divergence in topology / OSD / state wire shape. Property content differs slightly — Dock 3 adds `self_converge_coordinate` (OSD); aircraft mode-code and position-quality enums extend on newer firmware (see Phase 6a / 6b drift sections). The choreography itself is unchanged.

### Dock-path vs pilot-path for the same aircraft

- Not a symmetric view. Per Phase 6b: the same aircraft under a dock reports 17 dock-path-exclusive OSD properties that never appear on the pilot-path feed, plus 1 pilot-path-exclusive. Type drift on a handful of shared fields (e.g. `latitude` / `longitude` `double` vs `float`). A cloud handling both surfaces should treat them as two independent feeds of the same aircraft identity.

### RC writable surface is zero

- Per Phase 6c: neither RC Plus 2 nor RC Pro owns any gateway-level writable property. The `property/set` topic on an RC SN exists only as a route for aircraft-targeted writes (the aircraft's writable surface travels with the aircraft).

## Error paths

| Failure | Signal | Handling |
|---|---|---|
| Missed OSD messages | No wire-level signal — fire-and-forget | Cloud tolerates gaps; next OSD cycle recovers state. |
| Unknown property in `property/set` | `set_reply.result: <non-zero>` | Treat as rejected. Likely a client bug or firmware drift. |
| Write to read-only property | `set_reply.result: <non-zero>` (error) | Caller bug — check Phase 6 `accessMode` before issuing. |
| Topology reported without binding | Cloud receives `update_topo` but no matching org binding | Cloud should reject / log — indicates a misconfigured dock that skipped [`dock-bootstrap-and-pairing.md`](dock-bootstrap-and-pairing.md). |

## Provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/30.feature-set/20.dock-feature-set/20.dock-device-management.md]` | v1.11 DJI feature-set page — workflow narrative + Mermaid sequence this doc tracks for the dock path. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Device-Management.txt]` · `[DJI_Cloud/DJI_CloudAPI-Dock3-DeviceManagement.txt]` | v1.15 dock-path `update_topo`. |
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Device-Management.txt]` · `[DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Device-Management.txt]` | v1.15 pilot-path `update_topo`. |
| `[DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt]` · `[DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt]` | v1.15 topic-level definitions (OSD / state / property-set). Pilot OSD example copy-paste flagged as [OQ-002](../OPEN-QUESTIONS.md#oq-002--pilot-to-cloud-osd-struct-example-appears-to-be-a-copy-paste-of-the-dock-osd-example). |
| [`master-docs/device-properties/`](../device-properties/) | Phase 6 authoritative per-device property surfaces (dock gateway / aircraft / RC). |
| [`master-docs/mqtt/`](../mqtt/) | Phase 4 wire schema. |
| [`master-docs/websocket/situation-awareness/`](../websocket/situation-awareness/) | Phase 5 cloud → Pilot-2 change signals. |
| [`master-docs/http/device/topology.md`](../http/device/topology.md) | Phase 3 topology read-back endpoint. |
