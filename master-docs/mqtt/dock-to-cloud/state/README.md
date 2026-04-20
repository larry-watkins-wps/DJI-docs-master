# `state/` — on-change property push (dock-to-cloud)

The state topic carries **on-change property push** — properties reported by the device only when they change. Per DJI's property-catalog header convention (`[DJI_Cloud/DJI_CloudAPI-Dock2-Properties.txt]` line 7): "pushMode 1 — State data. It is reported when the state changes."

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, request-reply pattern) live in [`../../README.md`](../../README.md).

This file is a **shell** — the actual property catalog lives in Phase 6 [`device-properties/`](../../../device-properties/). The shell records the wire-level topic + push semantics + source files + forward pointer to Phase 6.

---

## Topic

| Direction | Topic | Push semantic |
|---|---|---|
| Device → Cloud | `thing/product/{device_sn}/state` | No `method`; `data` carries only the properties that changed (delta push, not a full state snapshot). |

`{device_sn}` = same `device_sn` dispatch rule as [`../osd/`](../osd/README.md).

## In-scope devices on the dock-to-cloud path

Same set as [`../osd/`](../osd/README.md#in-scope-devices-on-the-dock-to-cloud-path). Each property in the catalog carries a `pushMode` column; only `pushMode: 1` properties ride this topic.

| Device | Property source | Phase 6 doc |
|---|---|---|
| **DJI Dock 2** | [`DJI_Cloud/DJI_CloudAPI-Dock2-Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI-Dock2-Properties.txt) | [`device-properties/dock2.md`](../../../device-properties/dock2.md) |
| **DJI Dock 3** | [`DJI_Cloud/DJI_CloudAPI-Dock3-DeviceProperties.txt`](../../../../DJI_Cloud/DJI_CloudAPI-Dock3-DeviceProperties.txt) | [`device-properties/dock3.md`](../../../device-properties/dock3.md) |
| **Matrice 3D (M3D)** | [`DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt) | [`device-properties/m3d.md`](../../../device-properties/m3d.md) |
| **Matrice 3TD (M3TD)** | same as M3D (co-documented) | [`device-properties/m3td.md`](../../../device-properties/m3td.md) |
| **Matrice 4D (M4D)** | [`DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt`](../../../../DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt) | [`device-properties/m4d.md`](../../../device-properties/m4d.md) |
| **Matrice 4TD (M4TD)** | same as M4D (co-documented) | [`device-properties/m4td.md`](../../../device-properties/m4td.md) |

## Representative envelope

From the Dock-to-Cloud topic-definition extract (same envelope as [`../../README.md`](../../README.md) §5.2):

```json
{
  "tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
  "bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
  "timestamp": 1598411295123,
  "gateway": "sn",
  "data": {}
}
```

`data` in real traffic holds only the delta — e.g., `{"wireless_link_state": 2}` when the dock-aircraft wireless link state transitions from `1` to `2`. DJI's generic example shows `{}` to illustrate the envelope; real-wire payloads always carry at least one property key.

## Relationship to `osd/` and `property-set/`

- Properties with `pushMode: 0` ride [`../osd/`](../osd/README.md).
- Properties with `pushMode: 1` ride this topic.
- Properties with `accessMode: rw` (regardless of pushMode) are settable via [`../property-set/`](../property-set/README.md) — the cloud publishes a set request and the device replies.

Most dock properties split between OSD and state in a predictable way: high-frequency telemetry (environmental sensors, drone-in-dock status, mode code) lives on OSD; configuration and rare-change state (silent mode, user-experience plan, topology links, battery-maintenance info) lives on state.

## Open questions affecting this shell

- [`OQ-001`](../../../OPEN-QUESTIONS.md#oq-001--v111-vs-v115-source-version-mismatch) — v1.11 vs v1.15 property enum drift.
- [`OQ-003`](../../../OPEN-QUESTIONS.md#oq-003--mqtt-qos-retain-and-clean-session-settings-are-not-specified-in-djis-published-documentation) — QoS / retain unspecified.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/20.mqtt.md]` | Topic-prefix semantics (push mode). |
| `[DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt]` | Envelope shape + representative state example. |
| Per-device property files listed above | Property catalog inputs for Phase 6. |
