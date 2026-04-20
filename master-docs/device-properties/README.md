# Device properties

Per-device property catalogs for all in-scope DJI devices, sourced from DJI's v1.15 thing-model extract (primary) and v1.11 canonical (where it exists) for cross-version verification.

This area of the corpus sits downstream of Phase 4's MQTT catalog. The per-device docs here carry the **content** of what rides the MQTT property topics; the topic wire-level semantics (push mode, envelope, QoS gap) live in the Phase 4 property-family shells: [`mqtt/dock-to-cloud/osd/`](../mqtt/dock-to-cloud/osd/README.md), [`mqtt/dock-to-cloud/state/`](../mqtt/dock-to-cloud/state/README.md), [`mqtt/dock-to-cloud/property-set/`](../mqtt/dock-to-cloud/property-set/README.md), and their pilot-to-cloud counterparts.

---

## 1. Device scope

Two parallel cohorts, four device roles per cohort (dock / aircraft / RC / aircraft-via-RC):

| Role | Current gen (Dock 3 cohort) | Older gen (Dock 2 cohort) |
|---|---|---|
| Dock gateway | [DJI Dock 3](dock3.md) | [DJI Dock 2](dock2.md) |
| Aircraft — via dock gateway | [M4D](m4d.md), [M4TD](m4td.md) | [M3D](m3d.md), [M3TD](m3td.md) |
| RC gateway | [RC Plus 2 Enterprise](rc-plus-2.md) *(pending 6c)* | [RC Pro Enterprise](rc-pro.md) *(pending 6c)* |
| Aircraft — via RC gateway | [M4D](m4d.md), [M4TD](m4td.md) (shared pilot base: [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md)) | [M3D](m3d.md), [M3TD](m3td.md) (shared pilot base: [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md)) |

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

Every aircraft-level property reported by M3D / M3TD / M4D / M4TD on **either path** (dock-path via Dock 2 / Dock 3 gateway; pilot-path via RC Pro Enterprise / RC Plus 2 Enterprise gateway). M3TD is a property-level duplicate of M3D, and M4TD is a property-level duplicate of M4D — the "M3*" and "M4*" columns collapse each pair.

`✓` = present. `✓ rw` = present and writable via property-set. Blank = not reported by that cohort on that path.

| Property | Semantic family | Dock-path (M3*) | Dock-path (M4*) | Pilot-path (M3*) | Pilot-path (M4*) | Push | Notes |
|---|---|---|---|---|---|---|---|
| `country` | Metadata | | | ✓ | ✓ | osd | Pilot-path only — published by the aircraft when an RC is the gateway. |
| `mode_code` | Mission | ✓ | ✓ | ✓ | ✓ | osd | Max value: M3D dock `20`; M4D dock `21`; M3D pilot `18`; M4D pilot `19`. |
| `mode_code_reason` | Mission | ✓ | ✓ | ✓ | ✓ | state | Max value: dock `23`; pilot `22`. |
| `cameras` | Camera subsystem | ✓ | ✓ | ✓ | ✓ | osd | Same 50+-row struct on all paths; enum-label drift (baseline `"Shutter Priority"` vs dock `"Shutter priority exposure"`). |
| `obstacle_avoidance` | Safety | ✓ rw | ✓ rw | ✓ | ✓ | osd | `rw` on dock-path only; `r` on pilot-path. |
| `is_near_area_limit` | Safety | ✓ | ✓ | ✓ | ✓ | osd | |
| `is_near_height_limit` | Safety | ✓ | ✓ | ✓ | ✓ | osd | |
| `height_limit` | Safety | ✓ rw | ✓ rw | ✓ rw | ✓ rw | osd | `[20, 1500]` m. |
| `night_lights_state` | Config | ✓ rw | ✓ rw | ✓ rw | ✓ rw | osd | |
| `activation_time` | Metadata | ✓ | ✓ | ✓ | ✓ | osd | Unix seconds. |
| `maintain_status` | Maintenance | ✓ | ✓ | ✓ | ✓ | osd | Aircraft maintenance; distinct from dock-gateway `maintain_status`. |
| `total_flight_sorties` | Metadata | ✓ | ✓ | ✓ | ✓ | osd | |
| `track_id` | Metadata | ✓ | ✓ | ✓ | ✓ | osd | |
| `position_state` | Position / RTK | ✓ | ✓ | ✓ | ✓ | osd | Dock-path adds `"10":"RTK fixed"` to `»quality`; pilot-path stops at `"5"`. |
| `storage` | Storage | ✓ | ✓ | ✓ | ✓ | osd | KB total/used. |
| `battery` | Battery | ✓ | ✓ | ✓ | ✓ | osd | Per-battery struct with voltage / temperature / cycle count. |
| `total_flight_distance` | Metadata | ✓ | ✓ | ✓ | ✓ | osd | |
| `total_flight_time` | Metadata | ✓ | ✓ | ✓ | ✓ | osd | M4D pilot declares `int`; all others `float`. |
| `serious_low_battery_warning_threshold` | Battery | ✓ | ✓ | ✓ | ✓ | state | User-set %. |
| `low_battery_warning_threshold` | Battery | ✓ | ✓ | ✓ | ✓ | state | User-set %. |
| `control_source` | Topology | ✓ | ✓ | ✓ | ✓ | state | Device A/B or browser UUID. |
| `wind_direction` | Environment | ✓ | ✓ | ✓ | ✓ | osd | Value `1` label: dock/pilot-baseline `"True North"`; M4D pilot `"North"`. |
| `wind_speed` | Environment | ✓ | ✓ | ✓ | ✓ | osd | 0.1 m/s, estimated from attitude. |
| `home_distance` | Position / RTK | ✓ | ✓ | ✓ | ✓ | osd | |
| `home_latitude` | Position / RTK | ✓ | ✓ | ✓ | ✓ | state | Dock-path `double`; pilot-path `float`. |
| `home_longitude` | Position / RTK | ✓ | ✓ | ✓ | ✓ | state | Dock-path `double`; pilot-path `float`. |
| `attitude_head` | Position / RTK | ✓ | ✓ | ✓ | ✓ | osd | |
| `attitude_roll` | Position / RTK | ✓ | ✓ | ✓ | ✓ | osd | |
| `attitude_pitch` | Position / RTK | ✓ | ✓ | ✓ | ✓ | osd | |
| `elevation` | Position / RTK | ✓ | ✓ | ✓ | ✓ | osd | Relative to takeoff point. |
| `height` | Position / RTK | ✓ | ✓ | ✓ | ✓ | osd | Ellipsoid height. Dock-path `double`; pilot-path `float`. |
| `latitude` | Position / RTK | ✓ | ✓ | ✓ | ✓ | osd | Dock-path `double`; pilot-path `float`. |
| `longitude` | Position / RTK | ✓ | ✓ | ✓ | ✓ | osd | Dock-path `double`; pilot-path `float`. |
| `vertical_speed` | Position / RTK | ✓ | ✓ | ✓ | ✓ | osd | |
| `horizontal_speed` | Position / RTK | ✓ | ✓ | ✓ | ✓ | osd | |
| `firmware_upgrade_status` | Firmware | ✓ | ✓ | ✓ | ✓ | state | |
| `compatible_status` | Firmware | ✓ | ✓ | ✓ | ✓ | state | Consistency-upgrade flag. |
| `firmware_version` | Firmware | ✓ | ✓ | ✓ | ✓ | state (dock) / osd (M4D pilot) / state (M3D pilot) | Push-mode drift on M4D pilot only. |
| `gear` | Metadata | ✓ | ✓ | ✓ | ✓ | osd | A/P/NAV/FPV/FARM/S/F/M/G/T. |
| `camera_watermark_settings` | Config | ✓ rw | ✓ rw | ✓ rw | ✓ rw | state | 9-field struct; global switch + per-field toggles + custom string + layout. |
| `dongle_infos` | Comm | ✓ | ✓ | ✓ | ✓ | state | Dock-path adds `"0":"Unknown"` to `»esim_activate_state`; pilot-path baseline is 2-value. |
| `{type-subtype-gimbalindex}` | Payload subsystem | ✓ | ✓ | ✓ | ✓ | osd | Per-payload struct keyed by payload index. M4D source garbles the schema cell as `{_{type-subtype-gimbalindex}__aembLbhPpc}`. |
| `best_link_gateway` | Topology | ✓ | ✓ | | | state | Dock-path only — best-connected dock SN in multi-dock scenarios. |
| `wireless_link_topo` | Comm | ✓ | ✓ | | | state | Dock-path only — aircraft-side frequency topology. |
| `flysafe_database_version` | Safety | ✓ | ✓ | | | state | Dock-path only. |
| `offline_map_enable` | Config | ✓ | ✓ | | ✓ | state | Dock-path on both cohorts; pilot-path only on M4D. |
| `current_rth_mode` | Mission | ✓ | ✓ | | ✓ | state | Same deal — M3D pilot does not expose; M4D pilot does. |
| `rth_mode` | Mission | ✓ | ✓ | | ✓ | state | |
| `psdk_ui_resource` | PSDK subsystem | ✓ | ✓ | | | state | Dock-path only. |
| `psdk_widget_values` | PSDK subsystem | ✓ | ✓ | | | state | Dock-path only; includes nested speaker state. |
| `distance_limit_status` | Safety | ✓ rw | ✓ rw | | | osd | Dock-path only. `distance_limit ∈ [15, 8000]` m. |
| `rth_altitude` | Mission | ✓ rw | ✓ rw | | | osd | Dock-path only. `[20, 500]` m. |
| `commander_flight_height` | Mission | ✓ rw | ✓ rw | | ✓ rw | state | FlyTo height; dock-path on both cohorts; pilot-path only on M4D. |
| `commander_flight_mode` | Mission | ✓ rw | ✓ rw | | ✓ rw | state | FlyTo mode setter. |
| `current_commander_flight_mode` | Mission | | | | ✓ | state | Read-back companion — **M4D pilot-path only**, no dock-path counterpart. |
| `commander_mode_lost_action` | Mission | ✓ rw | ✓ rw | | ✓ rw | state | FlyTo signal-lost action. |
| `remaining_power_for_return_home` | Mission | ✓ rw | ✓ rw | | | state | Dock-path only. M3D note: Dock 2 recommends 25–50%; M4D note: Dock 3 recommends 15–50%. |

**Summary of unique properties per cohort:**

| Cohort | Top-level count (dock-path) | Top-level count (pilot-path) |
|---|---|---|
| M3D / M3TD | 42 (24 osd + 18 state) | 42 (34 osd + 8 state) — baseline only |
| M4D / M4TD | 42 (same shape as M3D with `mode_code` and `remaining_power_*` deltas) | 49 (baseline 42 + M4D-specific 7 extensions) |

Of the ~56 aircraft-level properties in total, **the dock-path exposes 17 that the pilot-path does not** (best_link_gateway, wireless_link_topo, flysafe_database_version, psdk_ui_resource, psdk_widget_values, distance_limit_status, rth_altitude, commander trio on M3 pilot-path, remaining_power_for_return_home, and offline_map_enable / current_rth_mode / rth_mode on M3 pilot-path). The pilot-path exposes **one** that the dock-path does not: `country`. M4D pilot-path additionally exposes `current_commander_flight_mode`.

### 4.3 RC-level properties

### 4.3 RC-level properties

*(Pending Phase 6c. RC Plus 2 Enterprise, RC Pro Enterprise catalog.)*

The RC Plus 2 Enterprise and RC Pro Enterprise are gateways (`{gateway_sn}`-owning); their properties are distinct from the aircraft-level properties above. The RC emits RC-level state (battery, connection, firmware) on its own topics; when it is relaying an aircraft, the aircraft's SN is the `{device_sn}` for the aircraft's properties.

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

Phase 6b (aircraft) sources:

| Source | Version | Role |
|---|---|---|
| [`DJI_Cloud/DJI_CloudAPI_Aircraft-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_Aircraft-Properties.txt) | v1.15 | Pilot-path generic aircraft baseline (1,124 lines). Used by M3D / M3TD / M4D / M4TD pilot-path sections. |
| [`DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt) | v1.15 | M3D + M3TD dock-path primary (2,373 lines). |
| [`DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt`](../../DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt) | v1.15 | M4D + M4TD dock-path primary (218 lines). |
| [`DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt) | v1.15 | M4D pilot-path delta spec (117 lines). |
| [`Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/10.aircraft/10.m3d-properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/10.aircraft/10.m3d-properties.md) | v1.11.3 | M3D dock-path drift cross-check. |
| [`Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/10.m3-series/00.properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/10.m3-series/00.properties.md) | v1.11.3 | M3-series pilot-path drift cross-check. |
| [`Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/30.others/10.aircraft/00.properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/30.others/10.aircraft/00.properties.md) | v1.11.3 | Generic aircraft pilot-path drift cross-check. |

M4D / M4TD have no v1.11 counterpart (both postdate v1.11.3).

Phase 6c (RC) sources are listed in the per-device docs when that sub-phase lands.
