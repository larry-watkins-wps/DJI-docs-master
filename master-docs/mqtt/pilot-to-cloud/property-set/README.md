# `property-set/` — cloud-to-device property set (pilot-to-cloud)

The property-set topic carries **cloud-initiated writes** to writable device properties. Identical wire semantics as the dock-to-cloud shell ([`../../dock-to-cloud/property-set/README.md`](../../dock-to-cloud/property-set/README.md)).

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

This file is a **shell** — the catalog of writable properties (which keys are writable, their enums, write semantics) lives in Phase 6 [`device-properties/`](../../../device-properties/). Aircraft catalogs (landed in Phase 6b): [`m3d.md`](../../../device-properties/m3d.md) §3, [`m3td.md`](../../../device-properties/m3td.md), [`m4d.md`](../../../device-properties/m4d.md) §3, [`m4td.md`](../../../device-properties/m4td.md); pilot-path aircraft baseline: [`_aircraft-pilot-base.md`](../../../device-properties/_aircraft-pilot-base.md) §3. RC catalogs pending Phase 6c.

---

## Topics

| Direction | Topic | Purpose |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/property/set` | Cloud writes one or more properties. |
| Device → Cloud | `thing/product/{gateway_sn}/property/set_reply` | Device reports per-property write result. |

On pilot-to-cloud, `{gateway_sn}` is the **RC** serial. Even when the writable property lives on the sub-device aircraft, the topic is scoped to the RC; DJI's routing propagates the write via the RC → aircraft link.

## In-scope devices on the pilot-to-cloud path

| Device | Representative writable properties (see Phase 6 for full list) |
|---|---|
| **RC Plus 2 Enterprise** | Active SIM-slot selection, DRC-mode-related preferences, livestream config toggles. Per [`DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt). Full list pending Phase 6c. |
| **RC Pro Enterprise** | Subset of RC Plus 2's writable set. Per [`DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt). Full list pending Phase 6c. |
| **Aircraft (M3D / M3TD)** | Pilot-path writable surface = baseline: `height_limit`, `night_lights_state`, `camera_watermark_settings` (9-field struct), and the `thermal_*` cluster on the `{type-subtype-gimbalindex}` payload struct. See [`_aircraft-pilot-base.md`](../../../device-properties/_aircraft-pilot-base.md) §3. |
| **Aircraft (M4D / M4TD)** | Baseline writable surface **plus** `commander_flight_height`, `commander_flight_mode`, `commander_mode_lost_action` — the M4D FlyTo scheduling trio is writable over the pilot path. See [`m4d.md`](../../../device-properties/m4d.md) §3. |

Note: dock-path writable aircraft properties (`obstacle_avoidance`, `distance_limit_status`, `rth_altitude`, `remaining_power_for_return_home`, `commander_*` on M3D) are not writable from the pilot path — that writable surface is dock-path exclusive.

## Envelope — set request and reply

Same shapes as [`../../dock-to-cloud/property-set/README.md`](../../dock-to-cloud/property-set/README.md#envelope--set-request) — see there for the set and set_reply envelope examples plus the per-property `result` code enum (`0` = success, `1` = fail, `2` = time exceed, other = Phase 8 error codes).

## Relationship to pilot-side services and DRC commands

Many pilot-side runtime operations have **both** a service method (see [`../services/`](../services/) and the [`../drc/`](../drc/) camera variants in [`../README.md`](../README.md)) **and** a writable property. Typical split:

- **Services / DRC methods** — stateful actions with multi-step flows or immediate mode changes (take photo, switch camera mode, POI mode enter).
- **Property-set** — simple config toggles and mode preferences that persist across sessions.

Phase 9 workflows will document the recommended surface per operation. For now: when a control appears in both the services catalog and the property-set catalog, the service method is the latency-sensitive path; the property-set is the configuration-persistence path.

## Open questions affecting this shell

- [`OQ-001`](../../../OPEN-QUESTIONS.md#oq-001--v111-vs-v115-source-version-mismatch) — v1.11 vs v1.15 property drift.
- [`OQ-003`](../../../OPEN-QUESTIONS.md#oq-003--mqtt-qos-retain-and-clean-session-settings-are-not-specified-in-djis-published-documentation) — QoS / retain unspecified.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/20.mqtt.md]` | Topic-prefix semantics. |
| `[DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt]` | Envelope shape + reply pattern. |
| Per-device property files listed above | Writable-property catalog inputs for Phase 6. |
