# `osd/` — high-frequency property push (dock-to-cloud)

The OSD topic carries **high-frequency property push** — stable-frequency properties reported by the device at ~0.5 Hz. Per DJI's property-catalog header convention (`[DJI_Cloud/DJI_CloudAPI-Dock2-Properties.txt]` line 4): "pushMode 0 — Stable frequency data. Device will report in the frequency of 0.5HZ."

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, request-reply pattern, QoS/retain gap per OQ-003) live in [`../../README.md`](../../README.md).

This file is a **shell** — the actual property catalog (field names, types, units, enums, v1.11 vs v1.15 drift) lives in Phase 6 [`device-properties/`](../../../device-properties/). The shell records the wire-level topic + push semantics + source files + forward pointer to Phase 6.

---

## Topic

| Direction | Topic | Push semantic |
|---|---|---|
| Device → Cloud | `thing/product/{device_sn}/osd` | No `method`; `data` carries properties directly. |

`{device_sn}` is the thing-model-bearing device — the dock's serial for dock properties, the aircraft's serial for aircraft properties. A dock that pairs with an aircraft emits OSD on **two** separate topics (one per `device_sn`).

## In-scope devices on the dock-to-cloud path

| Device | `device_sn` role | Property source | Phase 6 doc |
|---|---|---|---|
| **DJI Dock 2** | Dock serial | [`DJI_Cloud/DJI_CloudAPI-Dock2-Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI-Dock2-Properties.txt) · v1.11 [`Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/00.properties.md`](../../../../Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/00.properties.md) | [`device-properties/dock2.md`](../../../device-properties/dock2.md) |
| **DJI Dock 3** | Dock serial | [`DJI_Cloud/DJI_CloudAPI-Dock3-DeviceProperties.txt`](../../../../DJI_Cloud/DJI_CloudAPI-Dock3-DeviceProperties.txt) | [`device-properties/dock3.md`](../../../device-properties/dock3.md) |
| **Matrice 3D (M3D)** | Aircraft serial | [`DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt) (dock-path) | [`device-properties/m3d.md`](../../../device-properties/m3d.md) |
| **Matrice 3TD (M3TD)** | Aircraft serial | same as M3D (co-documented) | [`device-properties/m3td.md`](../../../device-properties/m3td.md) |
| **Matrice 4D (M4D)** | Aircraft serial | [`DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt`](../../../../DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt) (dock-path) | [`device-properties/m4d.md`](../../../device-properties/m4d.md) |
| **Matrice 4TD (M4TD)** | Aircraft serial | same as M4D (co-documented) | [`device-properties/m4td.md`](../../../device-properties/m4td.md) |

## Filtering OSD from state

Each property in the catalog is annotated with a `pushMode` column: `0` = OSD, `1` = state. Only `pushMode: 0` properties are pushed on this topic. `pushMode: 1` properties go on [`../state/`](../state/README.md).

## Representative envelope

From the Dock-to-Cloud topic-definition extract (`[DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt]`, same envelope as [`../../README.md`](../../README.md) §5.1):

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

This is a **dock** OSD example (`drone_in_dock`, `cover_state`, environmental sensors). Aircraft OSD payloads live in the same envelope shape but with aircraft-specific property fields (attitude, battery, camera state, GNSS, etc.) — see Phase 6 per-device docs.

## Open questions affecting this shell

- [`OQ-001`](../../../OPEN-QUESTIONS.md#oq-001--v111-vs-v115-source-version-mismatch) — v1.11 vs v1.15 property enum drift. Phase 6 resolves per-property; this shell does not enumerate properties.
- [`OQ-003`](../../../OPEN-QUESTIONS.md#oq-003--mqtt-qos-retain-and-clean-session-settings-are-not-specified-in-djis-published-documentation) — QoS / retain unspecified.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/20.mqtt.md]` | Topic-prefix semantics (push mode). |
| `[DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt]` | Envelope shape + representative OSD example. |
| Per-device property files listed above | Property catalog inputs for Phase 6. |
