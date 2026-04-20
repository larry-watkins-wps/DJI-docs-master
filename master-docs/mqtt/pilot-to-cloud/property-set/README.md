# `property-set/` — cloud-to-device property set (pilot-to-cloud)

The property-set topic carries **cloud-initiated writes** to writable device properties. Identical wire semantics as the dock-to-cloud shell ([`../../dock-to-cloud/property-set/README.md`](../../dock-to-cloud/property-set/README.md)).

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

This file is a **shell** — the catalog of writable properties (which keys are writable, their enums, write semantics) lives in Phase 6 [`device-properties/`](../../../device-properties/). Aircraft catalogs (landed in Phase 6b): [`m3d.md`](../../../device-properties/m3d.md) §3, [`m3td.md`](../../../device-properties/m3td.md), [`m4d.md`](../../../device-properties/m4d.md) §3, [`m4td.md`](../../../device-properties/m4td.md); pilot-path aircraft baseline: [`_aircraft-pilot-base.md`](../../../device-properties/_aircraft-pilot-base.md) §3. RC catalogs (landed in Phase 6c): [`rc-plus-2.md`](../../../device-properties/rc-plus-2.md), [`rc-pro.md`](../../../device-properties/rc-pro.md). **Neither RC owns any writable properties** (confirmed 6c); the `{rc_sn}/property/set` topic carries writes that target aircraft properties exclusively — see correction below.

---

## Topics

| Direction | Topic | Purpose |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/property/set` | Cloud writes one or more properties. |
| Device → Cloud | `thing/product/{gateway_sn}/property/set_reply` | Device reports per-property write result. |

On pilot-to-cloud, `{gateway_sn}` is the **RC** serial. Even when the writable property lives on the sub-device aircraft, the topic is scoped to the RC; DJI's routing propagates the write via the RC → aircraft link.

## In-scope devices on the pilot-to-cloud path

| Device | Writable property surface |
|---|---|
| **RC Plus 2 Enterprise** | **None at the RC level.** All 11 RC Plus 2 gateway properties are `accessMode: r` per [`rc-plus-2.md`](../../../device-properties/rc-plus-2.md) §3. The RC's serial still owns the `{gateway_sn}/property/set` topic that routes writes to the paired aircraft. |
| **RC Pro Enterprise** | **None at the RC level.** All 11 RC Pro gateway properties are `accessMode: r` per [`rc-pro.md`](../../../device-properties/rc-pro.md) §3. Same routing role as RC Plus 2 — the topic is an envelope for paired-aircraft writes. |
| **Aircraft (M3D / M3TD)** | Pilot-path writable surface = baseline: `height_limit`, `night_lights_state`, `camera_watermark_settings` (9-field struct), and the `thermal_*` cluster on the `{type-subtype-gimbalindex}` payload struct. See [`_aircraft-pilot-base.md`](../../../device-properties/_aircraft-pilot-base.md) §3. |
| **Aircraft (M4D / M4TD)** | Baseline writable surface **plus** `commander_flight_height`, `commander_flight_mode`, `commander_mode_lost_action` — the M4D FlyTo scheduling trio is writable over the pilot path. See [`m4d.md`](../../../device-properties/m4d.md) §3. |

### Correction — 4i speculative list (2026-04-19, 6c)

The earlier version of this shell listed "Active SIM-slot selection, DRC-mode-related preferences, livestream config toggles" as RC Plus 2 writable properties and described RC Pro's set as a "subset of RC Plus 2's". **Both were incorrect.** Phase 6c enumeration of [`DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt) and [`DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt) confirmed every gateway-level RC property is `accessMode: r`. Active SIM-slot selection, DRC lifecycle, and livestream configuration are driven by **services and DRC methods** on the pilot-to-cloud path (Phase 4h) — not by `property/set`. The corrected table above stands.

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
