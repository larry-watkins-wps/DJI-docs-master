# Device properties

Per-device property catalogs for all in-scope DJI devices, sourced from DJI's v1.15 thing-model extract (primary) and v1.11 canonical (where it exists) for cross-version verification.

This area of the corpus sits downstream of Phase 4's MQTT catalog. The per-device docs here carry the **content** of what rides the MQTT property topics; the topic wire-level semantics (push mode, envelope, QoS gap) live in the Phase 4 property-family shells: [`mqtt/dock-to-cloud/osd/`](../mqtt/dock-to-cloud/osd/README.md), [`mqtt/dock-to-cloud/state/`](../mqtt/dock-to-cloud/state/README.md), [`mqtt/dock-to-cloud/property-set/`](../mqtt/dock-to-cloud/property-set/README.md), and their pilot-to-cloud counterparts.

---

## 1. Device scope

Two parallel cohorts, four device roles per cohort (dock / aircraft / RC / aircraft-via-RC):

| Role | Current gen (Dock 3 cohort) | Older gen (Dock 2 cohort) |
|---|---|---|
| Dock gateway | [DJI Dock 3](dock3.md) | [DJI Dock 2](dock2.md) |
| Aircraft — via dock gateway | M4D, M4TD *(pending 6b)* | M3D, M3TD *(pending 6b)* |
| RC gateway | [RC Plus 2 Enterprise](rc-plus-2.md) *(pending 6c)* | [RC Pro Enterprise](rc-pro.md) *(pending 6c)* |
| Aircraft — via RC gateway | M4D *(pending 6b)* | M3D, M3TD *(pending 6b)* |

Out-of-scope devices that appear in DJI enum values (Dock 1, M30 / M30T, M300 / M350 RTK, M400, Mavic 3 Enterprise, plain RC) are noted in enum tables on the per-device docs for completeness but do not get their own property doc.

## 2. How a property is published

Every property row in a DJI property catalog carries four fields that determine its wire behaviour:

- **Type** — primitive (`int`, `text`, `float`, `double`, `bool`, `date`), enum (`enum_int`, `enum_string`), or compound (`struct`, `array`). Compound types nest via `»` prefixes in the source tables; one `»` = one level deep.
- **Constraint** — a JSON blob with `{"max", "min", "step", "unit_name", "length"}` or an enum value map `{"0": "Label", "1": "Label", ...}`.
- **accessMode** — `r` (read-only; device pushes but cloud cannot write) or `rw` (read-write; cloud may set via the property-set topic).
- **pushMode** — `0` (high-frequency, ~0.5 Hz stable push on `thing/product/{device_sn}/osd`) or `1` (on-change state push on `thing/product/{device_sn}/state`).

For nested struct fields, the parent's `pushMode` and `accessMode` govern the whole substruct on the wire; the DJI source tables mark nested-row mode cells as `0` or blank cosmetically. A reader can determine wire behaviour by looking at the top-level property only.

Mapped to Phase 4:
- `pushMode: 0` → [`mqtt/.../osd/`](../mqtt/dock-to-cloud/osd/README.md) family.
- `pushMode: 1` → [`mqtt/.../state/`](../mqtt/dock-to-cloud/state/README.md) family.
- `accessMode: rw` → [`mqtt/.../property-set/`](../mqtt/dock-to-cloud/property-set/README.md) family, **in addition to** the push family above.

## 3. How the per-device docs are organized

Each `<device>.md` carries the full property catalog for that device, grouped as:

1. **OSD properties** — `pushMode: 0` — flat table with description, type, constraint, accessMode, nested struct fields via `»`.
2. **State properties** — `pushMode: 1` — same table shape.
3. **Settable summary** — `accessMode: rw` only — compact list of writable keys with their push mode, for operators planning property-set calls.
4. **DJI-source inconsistencies** — per-property notes where the source extract is self-contradictory (examples contain fields not in the list, Chinese leftovers, label typos, etc.).
5. **v1.11 → v1.15 drift** (dock / aircraft only — v1.11 never covered pilot-to-cloud aircraft at property level) — side-by-side of enum or label changes between versions. Drift that is purely cosmetic (label wording, typo fixes) is flagged but not escalated; drift that changes semantics (enum values added, types changed) is called out explicitly and links to [`OQ-001`](../OPEN-QUESTIONS.md#oq-001--source-version-mismatch-between-cloud-api-doc-v1113-and-dji_cloud-v115) for policy.
6. **Source provenance** — the DJI source files consulted.

Per-device docs do **not** duplicate Phase 4 shell content. Readers looking up "what does the dock push" land here; readers looking up "what topic does that ride on" cross-link back to Phase 4.

## 4. Master cross-device index

Properties shared across multiple devices are listed here with their home-device set. This table is built up incrementally as Phase 6 sub-drops land; rows added in 6a cover gateway-level properties for Dock 2 + Dock 3.

### 4.1 Dock gateway properties — Dock 2 / Dock 3 coverage

Every dock-gateway property reported on `thing/product/{dock_sn}/osd` or `thing/product/{dock_sn}/state`. `✓` = present in that device's property list. `✓ rw` = present and writable via property-set. A blank cell = not reported by that device.

| Property | Semantic family | Dock 2 | Dock 3 | Push | Notes |
|---|---|---|---|---|---|
| `home_position_is_valid` | Position / RTK | ✓ | ✓ | osd | Dock 3 expands enum from 2 values to 4 (separate heading and lat/lon validity bits). v1.11 + Dock 2 v1.15: `{0, 1}`. Dock 3 v1.15: `{0, 1, 2, 3}`. |
| `heading` | Position / RTK | ✓ | ✓ | osd | |
| `rtcm_info` | Position / RTK | ✓ | ✓ | state | |
| `self_converge_coordinate` | Position / RTK | | ✓ | osd | Dock 3 only — self-convergence calibration coordinates. |
| `wireless_link_topo` | Comm | ✓ | ✓ | state | |
| `wireless_link` | Comm | ✓ | ✓ | osd | 4G + SDR link status, signal quality. |
| `dongle_infos` | Comm | ✓ | ✓ | state | 4G dongle / eSIM inventory. |
| `network_state` | Comm | ✓ | ✓ | osd | 4G vs Ethernet selection, quality level. |
| `live_capacity` | Livestream | ✓ | ✓ | state | Selectable video sources + per-camera bitrate options. |
| `live_status` | Livestream | ✓ | ✓ | state | Per-stream live state. |
| `air_conditioner` | Environment | ✓ | ✓ | osd | Cooling / heating / dehumidification state. |
| `silent_mode` | Config | ✓ rw | ✓ rw | state | |
| `user_experience_improvement` | Config | ✓ rw | ✓ rw | state | |
| `air_transfer_enable` | Config | ✓ rw | ✓ rw | state | Rapid photo transfer during flight. |
| `battery_store_mode` | Battery | ✓ | ✓ | osd | Schedule vs Standby mode. |
| `backup_battery` | Battery | ✓ | ✓ | osd | Internal backup battery voltage + temperature. |
| `drone_battery_maintenance_info` | Battery | ✓ | ✓ | osd | Battery maintenance + per-battery heat state. |
| `drone_charge_state` | Battery | ✓ | ✓ | osd | |
| `maintain_status` | Maintenance | ✓ | ✓ | osd | Dock maintenance history. Labels differ between Dock 2 and Dock 3. |
| `alarm_state` | Config | ✓ | ✓ | osd | Sound-and-light alarm. |
| `position_state` | Position / RTK | ✓ | ✓ | osd | Satellite / RTK fix state. |
| `emergency_stop_state` | Safety | ✓ | ✓ | osd | |
| `alternate_land_point` | Mission | ✓ | ✓ | osd | Alternate landing coordinates. |
| `activation_time` | Metadata | ✓ | ✓ | osd | Dock activation (Unix seconds). |
| `first_power_on` | Metadata | ✓ | ✓ | osd | First power-on (Unix ms). |
| `acc_time` | Metadata | ✓ | ✓ | state | Cumulative running seconds. |
| `job_number` | Metadata | ✓ | ✓ | osd | Cumulative dock operations. |
| `firmware_version` | Firmware | ✓ | ✓ | state | |
| `firmware_upgrade_status` | Firmware | ✓ | ✓ | state | |
| `compatible_status` | Firmware | ✓ | ✓ | state | Consistency-update flag. |
| `storage` | Storage | ✓ | ✓ | osd | Total / used KB. |
| `media_file_detail` | Media | ✓ | ✓ | osd | Pending upload count. |
| `working_current` | Power | ✓ | ✓ | osd | mA. |
| `working_voltage` | Power | ✓ | ✓ | osd | mV. |
| `humidity` | Environment | ✓ | ✓ | osd | |
| `temperature` | Environment | ✓ | ✓ | osd | Inside dock. |
| `environment_temperature` | Environment | ✓ | ✓ | osd | Ambient. |
| `wind_speed` | Environment | ✓ | ✓ | osd | |
| `rainfall` | Environment | ✓ | ✓ | osd | |
| `supplement_light_state` | Environment | ✓ | ✓ | osd | |
| `cover_state` | Dock physical | ✓ | ✓ | osd | |
| `drone_in_dock` | Dock physical | ✓ | ✓ | osd | |
| `sub_device` | Topology | ✓ | ✓ | osd | Aircraft-on-dock state. |
| `height` | Position / RTK | ✓ | ✓ | osd | Ellipsoid height. |
| `latitude` | Position / RTK | ✓ | ✓ | osd | |
| `longitude` | Position / RTK | ✓ | ✓ | osd | |
| `flighttask_step_code` | Mission | ✓ | ✓ | osd | Dock-side task-step progress. |
| `mode_code` | Mission | ✓ | ✓ | osd | Dock overall state. Dock 3 enum matches Dock 2 v1.15 (`{0..5}`); v1.11 Dock 2 stopped at `4`. |
| `drc_state` | DRC | ✓ | ✓ | osd | |

48 dock-gateway properties shared between Dock 2 and Dock 3. Dock 3 adds 1 unique property (`self_converge_coordinate`). No Dock 2 property is absent from Dock 3.

### 4.2 Aircraft-level properties

*(Pending Phase 6b. M3D, M3TD, M4D, M4TD catalog.)*

### 4.3 RC-level properties

*(Pending Phase 6c. RC Plus 2 Enterprise, RC Pro Enterprise catalog.)*

## 5. Open questions affecting this area

- [`OQ-001`](../OPEN-QUESTIONS.md#oq-001--source-version-mismatch-between-cloud-api-doc-v1113-and-dji_cloud-v115) — v1.11 vs v1.15 drift. Resolved per-property on the device doc; escalated to OQ only when the drift is semantic. Phase 6a dock drift is entirely cosmetic or label-rebranding — no semantic escalations.
- [`OQ-002`](../OPEN-QUESTIONS.md#oq-002--pilot-to-cloud-osd-struct-example-appears-to-be-a-copy-paste-of-the-dock-osd-example) — pilot-to-cloud OSD copy-paste bug in DJI's topic-definition file. Affects 6b/6c only. Dock-path OSD examples (used in 6a) are unaffected.
- [`OQ-003`](../OPEN-QUESTIONS.md#oq-003--mqtt-qos-retain-and-clean-session-settings-are-not-specified-in-djis-published-documentation) — QoS / retain unspecified. No Phase 6 implication — property push uses the same envelope regardless of QoS choice.

## 6. Source provenance

Phase 6a (dock-gateway) sources:

| Source | Version | Role |
|---|---|---|
| [`DJI_Cloud/DJI_CloudAPI-Dock2-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock2-Properties.txt) | v1.15 | Dock 2 primary. |
| [`Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/00.properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/00.properties.md) | v1.11.3 | Dock 2 drift cross-check. |
| [`DJI_Cloud/DJI_CloudAPI-Dock3-DeviceProperties.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock3-DeviceProperties.txt) | v1.15 | Dock 3 primary. Dock 3 has no v1.11 counterpart (Dock 3 postdates v1.11). |

Phase 6b/6c sources are listed in the per-device docs when those sub-phases land.
