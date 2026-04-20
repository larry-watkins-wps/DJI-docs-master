# `state/` — on-change property push (pilot-to-cloud)

The state topic carries **on-change property push** — properties reported by the device only when they change. Identical wire semantics as the dock-to-cloud shell ([`../../dock-to-cloud/state/README.md`](../../dock-to-cloud/state/README.md)).

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

This file is a **shell** — the actual property catalog lives in Phase 6 [`device-properties/`](../../../device-properties/). Aircraft catalogs (landed in Phase 6b): [`m3d.md`](../../../device-properties/m3d.md), [`m3td.md`](../../../device-properties/m3td.md), [`m4d.md`](../../../device-properties/m4d.md), [`m4td.md`](../../../device-properties/m4td.md); pilot-path baseline: [`_aircraft-pilot-base.md`](../../../device-properties/_aircraft-pilot-base.md). RC catalogs (landed in Phase 6c): [`rc-plus-2.md`](../../../device-properties/rc-plus-2.md), [`rc-pro.md`](../../../device-properties/rc-pro.md).

---

## Topic

| Direction | Topic | Push semantic |
|---|---|---|
| Device → Cloud | `thing/product/{device_sn}/state` | No `method`; `data` carries only the properties that changed. |

On pilot-to-cloud, `{device_sn}` is the aircraft's serial for aircraft state pushes (DRC-link state, obstacle-sensing enable, AI-identify mode, payload configuration changes) and the RC's serial for RC state pushes (SIM-slot state, remote-controller pairing changes, 4G network-state transitions). Same dispatch rule as [`../osd/`](../osd/README.md).

## In-scope devices on the pilot-to-cloud path

Same set as [`../osd/`](../osd/README.md#in-scope-devices-on-the-pilot-to-cloud-path). Each property in the catalog carries a `pushMode` column; only `pushMode: 1` properties ride this topic.

| Device | Property source | Phase 6 pointer |
|---|---|---|
| **RC Plus 2 Enterprise** | [`DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt) | [`device-properties/rc-plus-2.md`](../../../device-properties/rc-plus-2.md) |
| **RC Pro Enterprise** | [`DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt) | [`device-properties/rc-pro.md`](../../../device-properties/rc-pro.md) |
| **M3D / M3TD** | [`_aircraft-pilot-base.md`](../../../device-properties/_aircraft-pilot-base.md) ← [`DJI_Cloud/DJI_CloudAPI_Aircraft-Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI_Aircraft-Properties.txt) | [`device-properties/m3d.md`](../../../device-properties/m3d.md) §B, [`m3td.md`](../../../device-properties/m3td.md) |
| **M4D / M4TD** | [`_aircraft-pilot-base.md`](../../../device-properties/_aircraft-pilot-base.md) + M4D delta [`DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt) | [`device-properties/m4d.md`](../../../device-properties/m4d.md) §B, [`m4td.md`](../../../device-properties/m4td.md) |

## Representative envelope

Same shape as [`../../README.md`](../../README.md) §5.2:

```json
{
  "tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
  "bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
  "timestamp": 1598411295123,
  "gateway": "sn",
  "data": {}
}
```

`data` in real pilot-path traffic holds only the delta. Aircraft state is the same payload whether the aircraft is dock-attached or RC-attached.

## Relationship to `osd/` and `property-set/`

- `pushMode: 0` properties ride [`../osd/`](../osd/README.md).
- `pushMode: 1` properties ride this topic.
- `accessMode: rw` properties are settable via [`../property-set/`](../property-set/README.md).

## Open questions affecting this shell

- [`OQ-001`](../../../OPEN-QUESTIONS.md#oq-001--v111-vs-v115-source-version-mismatch) — v1.11 vs v1.15 property enum drift.
- [`OQ-003`](../../../OPEN-QUESTIONS.md#oq-003--mqtt-qos-retain-and-clean-session-settings-are-not-specified-in-djis-published-documentation) — QoS / retain unspecified.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/20.mqtt.md]` | Topic-prefix semantics. |
| `[DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt]` | Envelope shape. |
| Per-device property files listed above | Property catalog inputs for Phase 6. |
