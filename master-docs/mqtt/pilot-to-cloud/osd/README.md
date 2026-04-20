# `osd/` — high-frequency property push (pilot-to-cloud)

The OSD topic carries **high-frequency property push** — stable-frequency properties reported by the device at ~0.5 Hz. Identical wire semantics as the dock-to-cloud shell ([`../../dock-to-cloud/osd/README.md`](../../dock-to-cloud/osd/README.md)) — the OSD topic is `thing/product/{device_sn}/osd` regardless of which gateway the device is paired with.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

This file is a **shell** — the actual property catalog lives in Phase 6 [`device-properties/`](../../../device-properties/). Aircraft catalogs (landed in Phase 6b): [`m3d.md`](../../../device-properties/m3d.md), [`m3td.md`](../../../device-properties/m3td.md), [`m4d.md`](../../../device-properties/m4d.md), [`m4td.md`](../../../device-properties/m4td.md); pilot-path baseline: [`_aircraft-pilot-base.md`](../../../device-properties/_aircraft-pilot-base.md). RC catalogs (landed in Phase 6c): [`rc-plus-2.md`](../../../device-properties/rc-plus-2.md), [`rc-pro.md`](../../../device-properties/rc-pro.md).

---

## Topic

| Direction | Topic | Push semantic |
|---|---|---|
| Device → Cloud | `thing/product/{device_sn}/osd` | No `method`; `data` carries properties directly. |

On pilot-to-cloud, `{device_sn}` is:
- The **aircraft** serial for aircraft-owned OSD (attitude, battery, location, camera state, GNSS).
- The **RC** serial for RC-owned OSD. Both in-scope RCs publish 6 OSD properties (Phase 6c): RC Plus 2 Enterprise publishes `capacity_percent`, `height`, `wireless_link`, `latitude`, `longitude`, `drc_state`; RC Pro Enterprise publishes `capacity_percent`, `height`, `wireless_link`, `latitude`, `longitude`, `country` (`drc_state` is RC-Plus-2-only; `country` is RC-Pro-only). SIM / 4G dongle inventory rides [`../state/`](../state/README.md), not OSD.

## In-scope devices on the pilot-to-cloud path

| Device | `device_sn` role | Property source | Phase 6 pointer |
|---|---|---|---|
| **RC Plus 2 Enterprise** | RC serial | [`DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt) | [`device-properties/rc-plus-2.md`](../../../device-properties/rc-plus-2.md) |
| **RC Pro Enterprise** | RC serial | [`DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt) · v1.11 [`Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/00.properties.md`](../../../../Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/00.properties.md) | [`device-properties/rc-pro.md`](../../../device-properties/rc-pro.md) |
| **M3D / M3TD** (when paired with RC Pro) | Aircraft serial | [`_aircraft-pilot-base.md`](../../../device-properties/_aircraft-pilot-base.md) ← [`DJI_Cloud/DJI_CloudAPI_Aircraft-Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI_Aircraft-Properties.txt) (generic baseline); v1.11 canonical [`Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/10.m3-series/00.properties.md`](../../../../Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/10.m3-series/00.properties.md) | [`device-properties/m3d.md`](../../../device-properties/m3d.md) §B, [`m3td.md`](../../../device-properties/m3td.md) |
| **M4D / M4TD** (when paired with RC Plus 2) | Aircraft serial | [`_aircraft-pilot-base.md`](../../../device-properties/_aircraft-pilot-base.md) + M4D delta spec [`DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt) | [`device-properties/m4d.md`](../../../device-properties/m4d.md) §B, [`m4td.md`](../../../device-properties/m4td.md) |

## Aircraft OSD is NOT gateway-agnostic — updated 6b

**Correction to earlier 4i language**: the aircraft OSD **topic name** is the same on both paths (`thing/product/{aircraft_sn}/osd`) but the **set of properties published** differs between dock-path and pilot-path. Phase 6b discovered (see [`m3d.md`](../../../device-properties/m3d.md) §B and [`m4d.md`](../../../device-properties/m4d.md) §B):

- **Dock-path only** (published on OSD when a dock is relaying): `best_link_gateway`, `wireless_link_topo`, `flysafe_database_version`, `psdk_ui_resource`, `psdk_widget_values`, `distance_limit_status`, `rth_altitude`, `remaining_power_for_return_home`, and (for M3D/M3TD cohort) the `commander_*` trio and `offline_map_enable` / `current_rth_mode` / `rth_mode`.
- **Pilot-path only**: `country`. M4D pilot-path additionally publishes `current_commander_flight_mode` which has no dock-path counterpart.
- **Both paths**: all `cameras` / `{type-subtype-gimbalindex}` / position / attitude / battery / maintain / firmware properties — with occasional type drift (e.g., `latitude` is `double` on dock-path and `float` on pilot-path).

The topic name and envelope are gateway-agnostic; the content is not. Phase 6 per-device docs capture the dock-path vs pilot-path split property-by-property.

See [`../README.md` §Cohort conventions](../README.md#cohort-conventions) for the RC-to-aircraft pairing matrix.

See [`../README.md` §Cohort conventions](../README.md#cohort-conventions) for the RC-to-aircraft pairing matrix.

## Known documentation issue — DJI's pilot OSD example

The pilot-to-cloud topic-definition extract ([`DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt`](../../../../DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt)) ships an OSD struct example that is byte-identical (modulo whitespace) to the dock-to-cloud example — i.e., DJI's pilot-to-cloud OSD example literally shows **dock OSD content** (`drone_in_dock`, `cover_state`, environmental sensors) which the pilot path does not actually publish. This is a DJI documentation copy-paste bug tracked as [`OQ-002`](../../../OPEN-QUESTIONS.md#oq-002--pilot-to-cloud-osd-struct-example-appears-to-be-a-copy-paste-of-the-dock-osd-example).

**Implication**: do not rely on the OSD example in the pilot-to-cloud topic-definition file for pilot-path content. Rely on the per-aircraft property files ([`DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt), [`DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt)) and the RC property files.

## Open questions affecting this shell

- [`OQ-001`](../../../OPEN-QUESTIONS.md#oq-001--v111-vs-v115-source-version-mismatch) — v1.11 vs v1.15 property enum drift.
- [`OQ-002`](../../../OPEN-QUESTIONS.md#oq-002--pilot-to-cloud-osd-struct-example-appears-to-be-a-copy-paste-of-the-dock-osd-example) — pilot OSD copy-paste issue (see above).
- [`OQ-003`](../../../OPEN-QUESTIONS.md#oq-003--mqtt-qos-retain-and-clean-session-settings-are-not-specified-in-djis-published-documentation) — QoS / retain unspecified.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/20.mqtt.md]` | Topic-prefix semantics (push mode). |
| `[DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt]` | Pilot envelope shape (note OQ-002 copy-paste issue). |
| Per-device property files listed above | Property catalog inputs for Phase 6. |
