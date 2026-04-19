# `osd/` — high-frequency property push (pilot-to-cloud)

The OSD topic carries **high-frequency property push** — stable-frequency properties reported by the device at ~0.5 Hz. Identical wire semantics as the dock-to-cloud shell ([`../../dock-to-cloud/osd/README.md`](../../dock-to-cloud/osd/README.md)) — the OSD topic is `thing/product/{device_sn}/osd` regardless of which gateway the device is paired with.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

This file is a **shell** — the actual property catalog lives in Phase 6 [`device-properties/`](../../../device-properties/) (pending).

---

## Topic

| Direction | Topic | Push semantic |
|---|---|---|
| Device → Cloud | `thing/product/{device_sn}/osd` | No `method`; `data` carries properties directly. |

On pilot-to-cloud, `{device_sn}` is:
- The **aircraft** serial for aircraft-owned OSD (attitude, battery, location, camera state, GNSS).
- The **RC** serial for RC-owned OSD (wireless-link state, SIM / 4G dongle state, remote-controller battery, etc.) — only when the RC publishes OSD. Not every RC publishes OSD; check the per-RC property file below.

## In-scope devices on the pilot-to-cloud path

| Device | `device_sn` role | Property source | Phase 6 pointer (pending) |
|---|---|---|---|
| **RC Plus 2 Enterprise** | RC serial | [`DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt) | `device-properties/rc-plus-2.md` |
| **RC Pro Enterprise** | RC serial | [`DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt`](../../../../DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt) · v1.11 [`Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/00.properties.md`](../../../../Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/00.properties.md) | `device-properties/rc-pro.md` |
| **M3D / M3TD** (when paired with RC Pro) | Aircraft serial | Same sources as [`../../dock-to-cloud/osd/README.md`](../../dock-to-cloud/osd/README.md) — aircraft OSD is payload-identical regardless of gateway | `device-properties/m3d.md`, `m3td.md` |
| **M4D / M4TD** (when paired with RC Plus 2) | Aircraft serial | Same sources as [`../../dock-to-cloud/osd/README.md`](../../dock-to-cloud/osd/README.md) | `device-properties/m4d.md`, `m4td.md` |

## Aircraft OSD is gateway-agnostic

The aircraft OSD topic (`thing/product/{aircraft_sn}/osd`) and its payload schema are identical whether the aircraft is paired with a dock or with an RC. Phase 6 aircraft property docs are the single source of truth; the pilot-to-cloud path just observes the same aircraft-sn-scoped topic.

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
