# `property-set/` — cloud-to-device property set (dock-to-cloud)

The property-set topic carries **cloud-initiated writes** to writable device properties. Per DJI's property-catalog header convention (`[DJI_Cloud/DJI_CloudAPI-Dock2-Properties.txt]` line 12): "accessMode rw — Property can be read and written (Topic: thing/product/{sn}/property/set)."

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, request-reply pattern) live in [`../../README.md`](../../README.md).

This file is a **shell** — the actual catalog of writable properties (which keys are writable, their enums, and per-property write semantics) lives in Phase 6 [`device-properties/`](../../../device-properties/) (pending). The shell records the wire-level topic + set/reply pattern + source files + forward pointer to Phase 6.

---

## Topics

| Direction | Topic | Purpose |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/property/set` | Cloud writes one or more properties. |
| Device → Cloud | `thing/product/{gateway_sn}/property/set_reply` | Device reports per-property write result. |

`{gateway_sn}` = gateway device (dock). Even when the writable property lives on the sub-device (aircraft), the topic is scoped to the **gateway**. DJI's routing sends the write through the gateway, which propagates to the right sub-device based on the property name.

## In-scope devices on the dock-to-cloud path

| Device | Representative writable properties (see Phase 6 for full list) |
|---|---|
| **DJI Dock 2** | `silent_mode`, `user_experience_improvement`, `air_transfer_enable`, `alarm_state_switch`, `battery_store_mode`, `night_lights_state`, `air_conditioner_mode`. Per [`DJI_Cloud/DJI_CloudAPI-Dock2-Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI-Dock2-Properties.txt). |
| **DJI Dock 3** | Superset of Dock 2 with additional platform-awareness / custom-flight-area fields. Per [`DJI_Cloud/DJI_CloudAPI-Dock3-DeviceProperties.txt`](../../../../DJI_Cloud/DJI_CloudAPI-Dock3-DeviceProperties.txt). |
| **Matrice 3D / 3TD** | Aircraft-side writable props: RTH height, payload enable flags, obstacle-sensing toggles, etc. Per [`DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt). |
| **Matrice 4D / 4TD** | Superset — more payload-configuration and AI-identify writable props. Per [`DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt`](../../../../DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt) + [`DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt). |

Phase 6 per-device docs will carry the full list of writable keys with their enums and constraints.

## Envelope — set request

Same envelope as [`../../README.md`](../../README.md) §5.6:

```json
{
  "tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
  "bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
  "timestamp": 1598411295123,
  "data": {
    "some_property": "some_value"
  }
}
```

`data` carries one or more `property_key: value` pairs to set. A single request can batch multiple writes; the reply reports `result` per key.

## Envelope — set reply

```json
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

Per-property reply `result` codes (verbatim from [`../../README.md`](../../README.md) §5.6):

- `0` — success
- `1` — fail
- `2` — time exceed
- other — refer to error code (Phase 8 `error-codes/`)

## Relationship to services

Some device controls are reachable via **both** a service method (cataloged under [`../services/`](../services/)) **and** a writable property. When both exist, DJI tends to prefer the service method for stateful operations with multi-step flows and the property-set for simple config toggles. Example: dock cover open/close is a service (`cover_open` / `cover_close` in 4e-1) while dock silent mode is a property set. Phase 9 workflows call out which surface the cloud should use per operation.

## Open questions affecting this shell

- [`OQ-001`](../../../OPEN-QUESTIONS.md#oq-001--v111-vs-v115-source-version-mismatch) — v1.11 vs v1.15 property drift.
- [`OQ-003`](../../../OPEN-QUESTIONS.md#oq-003--mqtt-qos-retain-and-clean-session-settings-are-not-specified-in-djis-published-documentation) — QoS / retain unspecified.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/20.mqtt.md]` | Topic-prefix semantics. |
| `[DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt]` | Envelope shape + reply pattern. |
| Per-device property files listed above | Writable-property catalog inputs for Phase 6. |
