# Device Properties — DJI Matrice 4D (M4D)

**Gateway role**: aircraft sub-device. Reported through a Dock 3 (dock-path) or RC Plus 2 Enterprise (pilot-path).
**Cohort**: Dock 3 / M4-series cohort. M4TD is the thermal variant of this aircraft — property catalog is identical; see [`m4td.md`](m4td.md).

**Sources**:

| File | Version | Authority |
|---|---|---|
| [`DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt`](../../DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt) | v1.15 | Dock-path primary. Covers M4D + M4TD co-documented. |
| [`DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt) | v1.15 | Pilot-path primary. M4D pilot-path extends the generic aircraft baseline with dock-scheduling + offline-map + RTH surfaces. |
| [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md) | v1.15 | Pilot-path baseline that M4D pilot-path extends. |
| — | — | M4D postdates v1.11; no v1.11 canonical counterpart exists for either path. |

M4D reports **42 top-level properties** on the **dock-path** (24 OSD + 18 state) + the `{type-subtype-gimbalindex}` dynamic struct; **6 are writable**. On the **pilot-path**, M4D reports the generic aircraft baseline **plus 7 M4D-specific extensions** — see §B.

Topic mapping (see Phase 2 [`mqtt/README.md`](../mqtt/README.md) for envelope):

| Topic | Push mode | Carries |
|---|---|---|
| `thing/product/{m4d_sn}/osd` | 0 — ~0.5 Hz | OSD properties (same topic used on both paths — aircraft SN is the publisher, gateway differs) |
| `thing/product/{m4d_sn}/state` | 1 — on-change | State properties |
| `thing/product/{m4d_sn}/property/set` | — | Cloud writes one of the writable keys |
| `thing/product/{m4d_sn}/property/set_reply` | — | Per-key `result` echo |

---

## A. Dock-path properties (via Dock 3 gateway)

M4D dock-path catalog is structurally identical to M3D's, with two cohort-specific deltas (see §5). The complete dock-path property table is the same as [`m3d.md`](m3d.md) §A — readers should consult that table for the full enumeration. The rest of §A here documents only the **M4D-specific divergences** and the re-iterated writable surface.

### A.1 Cohort deltas vs M3D dock-path

| Property | M3D value | M4D value | Classification |
|---|---|---|---|
| `mode_code` enum | max `20` — `{..., "19":"Dock address selecting","20":"POI"}` | max `21` — `{..., "19":"Dock address selecting","20":"POI","21":"during the inbound and outbound flight procedures"}` | **Enum extension** — M4D adds value `21`. Upward compatible: an M3D-trained cloud ignoring unknown codes will handle M4D correctly; a cloud that has not added `21` to its parser will see "unknown mode" during the M4D-specific inbound/outbound flight phase. |
| `remaining_power_for_return_home` description | "For DJI Dock 2, we recommend configuring this value in the 25%–50% range to provide a safer RTH power margin." | "For DJI Dock 3, we recommend configuring this value in the 15%–50% range to provide a safer RTH power margin." | Cosmetic — recommended range text only. Wire range `[0, 100]` identical. |
| `type_subtype_gimbalindex` source schema-cell | `type_subtype_gimbalindex` (clean) | `{_{type-subtype-gimbalindex}__aembLbhPpc}` (garbled — DJI source extraction artifact) | Source-defect. The intent is still the same per-payload dynamic struct; cloud implementations should key on the actual `{type-subtype-gimbalindex}` string. |

All other dock-path properties (`cameras` struct + subordinate fields, obstacle_avoidance, flight state, position, battery, maintain, FlySafe, dongle_infos, commander_*, RTH settings, PSDK state, watermark settings, distance limits) are identical in shape and semantics to M3D. See [`m3d.md`](m3d.md) §A.1 (OSD) and §A.2 (state) for the full tables.

### A.2 `{type-subtype-gimbalindex}` payload struct (dock-path)

Same fields as [`m3d.md`](m3d.md) §A.3 and [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md) §1 — gimbal attitude (`gimbal_pitch` / `gimbal_roll` / `gimbal_yaw`), laser ranging (`measure_target_*`), `payload_index`, `zoom_factor`, thermal cluster (`thermal_*`).

M4D's payload-index enum extends M3D's to cover M4D-compatible factory payloads (the exact enum is payload-level, not aircraft-level, and lives in the [Product Supported](https://developer.dji.com/doc/cloud-api-tutorial/en/overview/product-support.html) reference). An M4D fitted with an M3-compatible post-factory payload will emit the M3 payload_index; the `{type-subtype-gimbalindex}` struct schema accommodates both.

---

## B. Pilot-path properties (via RC Plus 2 Enterprise gateway)

When an RC Plus 2 Enterprise is the gateway, M4D publishes the **generic aircraft pilot-path baseline** (see [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md)) **plus the 7 M4D-specific extensions** enumerated below.

M4D pilot-path source: [`DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt) (117 lines). This extract does not include the shared aircraft properties that are carried in the baseline (`country`, `mode_code_reason`, `cameras` struct, `position_state`, `wind_direction`, etc.) — those are inherited from [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md).

### B.1 M4D pilot-path extensions (beyond baseline)

7 top-level properties published on pilot-path only when the aircraft is M4D or M4TD:

| Property | Description | Type | Constraint | Access | pushMode |
|---|---|---|---|---|---|
| `offline_map_enable` | Offline map switch | `bool` | `{"0":"Disable","1":"Enable"}` — when disabled, offline map sync is not automatic | `r` | 1 — state |
| `current_rth_mode` | Actual RTH altitude mode | `enum_int` | `{"0":"Optimal","1":"Preset"}` — labels differ from M3D dock-path (`"Intelligent altitude"`/`"Preset altitude"`); same codes `{0, 1}` | `r` | 1 — state |
| `rth_mode` | RTH altitude mode setting | `enum_int` | `{"0":"Optimal","1":"Preset"}` — "Optimal" mode is not settable from the cloud; only "Preset" is usable | `r` | 1 — state |
| `commander_flight_height` | FlyTo task altitude | `float` | `{"max":3000,"min":2,"step":0.1,"unit_name":"Meters / m"}` — relative to takeoff point | `rw` | 1 — state |
| `commander_flight_mode` | FlyTo task mode (setting value) | `enum_int` | `{"0":"Optimal height flight","1":"Preset height flight"}` | `rw` | 1 — state |
| `current_commander_flight_mode` | Current FlyTo task mode (read-back) | `enum_int` | `{"0":"Optimal height flight","1":"Preset height flight"}` | `r` | 1 — state |
| `commander_mode_lost_action` | FlyTo signal-lost action | `enum_int` | `{"0":"Continue with the to-point flight mission","1":"Exit the to-point flight mission and perform normal loss of control behavior"}` | `rw` | 1 — state |

Note: `current_commander_flight_mode` is a **read-back companion** to the `commander_flight_mode` setter. The setter reports the user-set intent; the read-back reports the mode currently active. Both exist in the M4D pilot-path catalog; the dock-path catalog has only `commander_flight_mode` without the read-back sibling.

### B.2 M4D pilot-path overrides (baseline properties with different enum or type)

| Property | Baseline | M4D pilot-path | Classification |
|---|---|---|---|
| `mode_code` | max `18` (`"Airborne RTK fixing mode"`) | max `19` — adds `"19":"Dock site evaluation in progress"` with description "Dock site selection refers to the process where the aircraft hovers in the air to select a location for the dock and check the RTK signal quality" | **Enum extension** — pilot-path gains one value for dock-scheduled pre-flight site evaluation. |
| `wind_direction` value `1` label | `"True North"` | `"North"` | Cosmetic. Same code. |
| `total_flight_time` type | `float` | `int` | Type drift. Wire value is integer-valued in practice; both parse. |
| `home_latitude` / `home_longitude` type | `float` | `float` | No drift. |
| `obstacle_avoidance` access mode | `r` | `r` | No drift — pilot-path is read-only on both M3D and M4D. |
| `firmware_version` push mode | `1` — state | `0` — osd | **Push-mode drift** — baseline ships `firmware_version` as state; M4D pilot-path ships it as osd. Neither is wrong; cloud implementations subscribe to both osd and state topics and accept either. |

### B.3 Properties in the baseline but absent from the M4D pilot-path extract

The M4D pilot-path extract (117 lines) is shorter than the generic baseline (1,124 lines) because DJI listed only the M4D-unique + the M4D-overridden set. Properties present in the baseline but not re-listed in the M4D pilot-path file — `country`, `mode_code_reason`, the full `cameras` struct, `position_state`, `storage`, `battery` struct and battery details, `wind_speed`, `home_distance`, `attitude_*`, `elevation`, `height`, `latitude`, `longitude`, `vertical_speed`, `horizontal_speed`, `gear`, `camera_watermark_settings`, the `{type-subtype-gimbalindex}` struct, `serious_low_battery_warning_threshold`, `low_battery_warning_threshold`, `control_source`, `dongle_infos` struct — **are still published by M4D on the pilot path** per the baseline semantics.

The M4D pilot-path extract is a **delta specification**, not a full catalog. Authoritative reading: baseline for shared properties; M4D extract for the 7 extensions + 6 overrides.

### B.4 `{type-subtype-gimbalindex}` payload struct (pilot-path)

M4D pilot-path `{type-subtype-gimbalindex}` is **identical in shape** to dock-path. Same fields as [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md). The M4D pilot-path extract's struct-name cell is the garbled `{_{type-subtype-gimbalindex}__aembLbhPpc}` — same DJI source extraction artifact as the dock-path. Use the baseline's literal `{type-subtype-gimbalindex}` name.

### B.5 Baseline properties that the M4D pilot extract override-differs vs dock-path M4D

Where the pilot-path baseline, the M4D pilot-path extract, and the M4D dock-path extract all disagree, dock-path wins for the dock-scheduled use case; pilot-path wins for operator-in-the-loop. Most cases are enum-label cosmetic (`"Auto(high sense)"` vs `"Auto(High Sense)"`, etc., already tracked in [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md) §4.1). No semantic disagreements.

---

## 3. Settable via `property/set` — `accessMode: rw`

Dock-path writable surface (6 top-level properties) — same as M3D dock-path, see [`m3d.md`](m3d.md) §3.

Pilot-path writable surface:

| Property | Push mode | Value domain | Notes |
|---|---|---|---|
| `height_limit` | osd | `int ∈ [20, 1500]` m | From baseline. |
| `night_lights_state` | osd | `enum_int {0: Disable, 1: On}` | From baseline. |
| `camera_watermark_settings` | state | `struct` with 9 rw sub-fields | From baseline. |
| `commander_flight_height` | state | `float ∈ [2, 3000]` m (step 0.1) | M4D pilot-path extension. |
| `commander_flight_mode` | state | `enum_int {0: Optimal, 1: Preset}` | M4D pilot-path extension. |
| `commander_mode_lost_action` | state | `enum_int {0: Continue, 1: Normal LoC}` | M4D pilot-path extension. |

Plus the thermal cluster on the `{type-subtype-gimbalindex}` struct — see [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md) §3.

`offline_map_enable`, `current_rth_mode`, `rth_mode`, `current_commander_flight_mode` are **not** writable on M4D pilot-path (`r` only in the source).

Aircraft flight operations are exposed as **services**, not property writes. See [`mqtt/dock-to-cloud/services/`](../mqtt/dock-to-cloud/services/) / [`mqtt/pilot-to-cloud/services/`](../mqtt/pilot-to-cloud/services/) / [`mqtt/dock-to-cloud/drc/`](../mqtt/dock-to-cloud/drc/) / [`mqtt/pilot-to-cloud/drc/`](../mqtt/pilot-to-cloud/drc/).

## 4. DJI-source inconsistencies (flagged, not escalated)

1. **`{_{type-subtype-gimbalindex}__aembLbhPpc}` garbled struct-name cell** — DJI's v1.15 extract (both dock-path [`DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt`](../../DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt) line 49 and pilot-path [`DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt) line 49) renders the struct name with a hash suffix. This is an MHTML-to-text extraction artifact. Authoritative name: literal `{type-subtype-gimbalindex}`. Same field body in both extracts; only the cell header is corrupted.
2. **Pilot-path extract is a delta, not a full catalog** — shorter than the baseline. Cloud implementations must **not** treat "absent from M4D pilot-path extract" as "not published by M4D on pilot-path." The baseline fields are all published.
3. **`current_rth_mode` / `rth_mode` labels** — M4D pilot-path uses `"Optimal"` / `"Preset"`, while M3D dock-path uses `"Intelligent altitude"` / `"Preset altitude"`. Same codes `{0, 1}`; label difference only.
4. **`firmware_version` push mode drift between baseline and M4D pilot extract** — baseline `1` (state); M4D `0` (osd). No semantic impact — the version rarely changes during a session, so either topic suffices.
5. **`mode_code` value `19` description** in M4D pilot-path is `"Dock site evaluation in progress"`, while the M3D dock-path uses `"Dock address selecting"` for the same code. Same code; description wording differs.
6. **`zoom_factor` under `{type-subtype-gimbalindex}` lacks `max`/`min` constraints** in the M4D dock-path extract (constraint cell reads `{"max":"","min":"","step":"","unit_name":null}`). Use the baseline's absent-constraints as authoritative.
7. **Pilot-path `cameras` subtree is omitted from M4D extract.** DJI presumably inherits from the baseline. Cloud implementations should use the baseline `cameras` shape for M4D pilot-path traffic.
8. **`mode_code_reason` is absent from M4D pilot-path extract.** Same inheritance note; the baseline's 23-value enum (stopping at `22`) is authoritative for M4D pilot-path. Dock-path adds value `23`.

None rise to [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) level.

## 5. Drift vs M3D

Dock-path drift — already captured in §A.1 above:
- `mode_code` max `20` (M3D) vs `21` (M4D) — enum extension.
- `remaining_power_for_return_home` recommendation text.
- `type_subtype_gimbalindex` schema-cell source artifact.

Pilot-path drift — M3D uses the generic baseline verbatim (via v1.11 M3-series catalog); M4D uses the baseline + 7 extensions + 6 overrides (see §B). The pilot-path divergence between M3D and M4D is substantially larger than the dock-path divergence — cloud implementations handling both cohorts need to branch on aircraft model key when parsing pilot-path aircraft OSD / state, especially for `commander_*`, `offline_map_enable`, and the RTH-mode state keys.

## 6. v1.11 → v1.15 drift

**None** — M4D postdates v1.11.3; no v1.11 canonical counterpart exists for either path. Source of truth for M4D is the v1.15 extracts cited above.

The absence of a v1.11 baseline means cloud implementations that were coded against M3-series pilot-path v1.11 will gracefully miss the M4D pilot-path extensions (`commander_*`, `offline_map_enable`, `current_rth_mode`/`rth_mode`, `current_commander_flight_mode`) but will still correctly parse the baseline properties. Add-only surface change.

## 7. Source provenance

| Source | Lines | Role |
|---|---|---|
| [`DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt`](../../DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt) | 218 | v1.15 dock-path primary. Covers M4D + M4TD co-documented. |
| [`DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt) | 117 | v1.15 pilot-path delta spec (extensions + overrides beyond the generic baseline). |
| [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md) | — | Generic aircraft pilot-path baseline inherited by M4D. |
| [`m3d.md`](m3d.md) | — | Dock-path full catalog — M4D dock-path references the M3D property table for shared shape. |
| [`dock3.md`](dock3.md) | — | Dock 3 gateway catalog — cross-referenced for context on paired dock properties (`sub_device`, air_transfer_enable scope, etc.). |
| [`m4td.md`](m4td.md) | — | Thermal variant annex. |
