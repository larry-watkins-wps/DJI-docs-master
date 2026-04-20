# Device Properties — DJI Matrice 3D (M3D)

**Gateway role**: aircraft sub-device. Reported through two distinct gateway SNs depending on the path — the Dock 2 gateway reports the **dock-path** catalog below, and an RC Pro Enterprise reports the **pilot-path** catalog.
**Cohort**: Dock 2 / M3-series cohort. M3TD is the thermal variant of this aircraft — the property catalog is identical; payload-specific differences (TD's infrared gimbal) are expressed through the `cameras.»payload_index` and `{type-subtype-gimbalindex}` key values, not through distinct properties. See [`m3td.md`](m3td.md) for the thermal-variant annex.

**Sources**:

| File | Version | Authority |
|---|---|---|
| [`DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt) | v1.15 | Dock-path primary. Covers M3D + M3TD co-documented. |
| [`Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/10.aircraft/10.m3d-properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/10.aircraft/10.m3d-properties.md) | v1.11.3 | Dock-path drift cross-check. |
| [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md) | v1.15 | Pilot-path baseline (generic aircraft). M3D pilot-path inherits this baseline. |
| [`Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/10.m3-series/00.properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/10.m3-series/00.properties.md) | v1.11.3 | Pilot-path M3-series canonical. Matches the pilot-path baseline; no v1.15 M3-series-specific extract exists. |

M3D reports **42 top-level properties** on the **dock-path** (24 OSD + 18 state) + the per-payload `{type-subtype-gimbalindex}` dynamic struct; **6 are writable**. On the **pilot-path**, M3D reports the generic aircraft baseline (42 top-level properties + `{type-subtype-gimbalindex}`) — see §B.

Topic mapping (see Phase 2 [`mqtt/README.md`](../mqtt/README.md) for envelope):

| Topic | Push mode | Carries |
|---|---|---|
| `thing/product/{m3d_sn}/osd` | 0 — ~0.5 Hz | OSD properties (same topic used on both paths — the push originates from the aircraft SN, but the relaying gateway differs) |
| `thing/product/{m3d_sn}/state` | 1 — on-change | State properties |
| `thing/product/{m3d_sn}/property/set` | — | Cloud writes one of the writable keys |
| `thing/product/{m3d_sn}/property/set_reply` | — | Per-key `result` echo |

---

## A. Dock-path properties (via Dock 2 gateway)

When a Dock 2 is the gateway (dock-scheduled mission flight), the M3D publishes the following 42 top-level properties + the payload struct.

### A.1 OSD properties — `pushMode: 0`

24 top-level properties push on `thing/product/{m3d_sn}/osd` at ~0.5 Hz.

| Property | Description | Type | Constraint | Access |
|---|---|---|---|---|
| `cameras` | Aircraft camera information | `array` of `struct` | `{"size": -, "item_type": struct}` | `r` |
| `»remain_photo_num` | Remaining number of photos to take | `int` | | |
| `»remain_record_duration` | Remaining recording time | `int` | `{"unit_name":"Seconds / s"}` | |
| `»record_time` | Video recording duration | `int` | `{"unit_name":"Seconds / s"}` | |
| `»payload_index` | Payload index | `text` | format `{type-subtype-gimbalindex}` — identifies the physical payload (H20N, H30T, etc.) | |
| `»camera_mode` | Camera mode | `enum_int` | `{"0":"Capturing","1":"Recording","2":"Smart Low-Light","3":"Panoramic photography"}` | |
| `»photo_state` | Capturing state | `enum_int` | `{"0":"Idle","1":"Capturing photo"}` | |
| `»screen_split_enable` | Is split screen enabled | `bool` | `{"0":"Disable split screen","1":"Enable split screen"}` | |
| `»recording_state` | Recording state | `enum_int` | `{"0":"Idle","1":"Recording"}` | |
| `»zoom_factor` | Zoom factor | `float` | `{"max":200,"min":2,"unit_name":null}` | |
| `»ir_zoom_factor` | Infrared zoom factor | `float` | `{"max":20,"min":2,"unit_name":null}` | |
| `»liveview_world_region` | FOV region in liveview | `struct` | coordinate origin is upper-left corner of lens | |
| `»»left` / `»»top` / `»»right` / `»»bottom` | FOV corner coordinates | `float` | | `r` |
| `»photo_storage_settings` | Photo storage settings | `array` of `enum_string` | value range `{current, wide, zoom, ir}` | |
| `»video_storage_settings` | Video storage settings | `array` of `enum_string` | value range `{current, wide, zoom, ir}` | |
| `»wide_exposure_mode` | Wide lens exposure mode | `enum_int` | `{"1":"Auto","2":"Shutter priority exposure","3":"Aperture priority exposure","4":"Manual exposure"}` | |
| `»wide_iso` | Wide lens sensitivity | `enum_int` | 13-value enum `{"0":"Auto","1":"Auto(high sense)","2":"50", ..., "11":"25600","255":"Fixed"}` | |
| `»wide_shutter_speed` | Wide lens shutter speed | `enum_int` | 60-value enum `{"0":"1/8000 s", ..., "59":"8.0 s","65534":"Auto"}` | |
| `»wide_exposure_value` | Wide lens exposure value | `enum_int` | 32-value enum `{"1":"-5.0ev", ..., "31":"5.0ev","255":"Fixed"}` | |
| `»zoom_exposure_mode` / `»zoom_iso` / `»zoom_shutter_speed` / `»zoom_exposure_value` | Zoom lens exposure set | `enum_int` | mirror the wide-lens enums with `"65534":"auto"` (lowercase) for shutter | |
| `»zoom_focus_mode` | Zoom lens focus mode | `enum_int` | `{"0":"MF","1":"AFS","2":"AFC"}` | |
| `»zoom_focus_value` / `»zoom_max_focus_value` / `»zoom_min_focus_value` / `»zoom_calibrate_farthest_focus_value` / `»zoom_calibrate_nearest_focus_value` | Zoom focus scalars | `int` | | |
| `»zoom_focus_state` | Zoom lens focus state | `enum_int` | `{"0":"Idle","1":"Focusing","2":"Focus succeeded","3":"Focus failed"}` | |
| `»ir_metering_mode` | Ir metering mode | `enum_int` | `{"0":"Ir metering off","1":"Spot metering","2":"Area metering"}` — short-form labels; pilot-path uses long form (see [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md) §4.1) | |
| `»ir_metering_point` | Ir metering point | `struct` with `»»x, »»y, »»temperature` | `x, y ∈ [0, 1]` normalised to lens | `r` |
| `»ir_metering_area` | Ir metering area | `struct` with `»»x, »»y, »»width, »»height, »»aver_temperature, »»min_temperature_point, »»max_temperature_point` | area bounded by top-left + size, all coords normalised | `r` |
| `obstacle_avoidance` | Aircraft obstacle sensing state | `struct` | | `rw` |
| `»horizon` / `»upside` / `»downside` | Per-direction sensing enable | `enum_int` | `{"0":"Disable","1":"Enable"}` | |
| `is_near_area_limit` | Whether approaching the GEO Zone | `enum_int` | `{"0":"Not reaching the GEO Zone","1":"Approaching the GEO Zone"}` | `r` |
| `is_near_height_limit` | Whether approaching the set height limit | `enum_int` | `{"0":"Not reaching the set height limit","1":"Approaching the set height limit"}` | `r` |
| `height_limit` | Aircraft height limit | `int` | `{"max":"1500","min":"20","step":"1","unit_name":"Meters / m"}` | `rw` |
| `night_lights_state` | Aircraft night lights state | `enum_int` | `{"0":"Disable","1":"On"}` | `rw` |
| `activation_time` | Aircraft activation time | `int` | `{"unit_name":"Seconds / s"}` — Unix epoch | `r` |
| `maintain_status` | Maintenance information | `struct` | | `r` |
| `»maintain_status_array` | Maintenance entries | `array` of `struct` with `»»state, »»last_maintain_type, »»last_maintain_time, »»last_maintain_flight_time, »»last_maintain_flight_sorties` | `last_maintain_type {"1":"Basic maintenance","2":"Regular maintenance","3":"Deep maintenance"}` | |
| `total_flight_sorties` | Accumulated total sorties | `int` | `{"max":"2147483647","min":"0","step":"1"}` | `r` |
| `type_subtype_gimbalindex` | Per-payload property bag — see §A.3 | `struct` | key = payload index | `r` |
| `track_id` | Track ID | `text` | `{"length":"64"}` | `r` |
| `position_state` | Satellite search state | `struct` | | `r` |
| `»is_fixed` | Whether is fixed | `enum_int` | `{"0":"Not started","1":"Fixing","2":"Fixing successful","3":"Fixing failed"}` | |
| `»quality` | Satellite acquisition mode | `enum_int` | `{"1":"Gear 1","2":"Gear 2","3":"Gear 3","4":"Gear 4","5":"Gear 5","10":"RTK fixed"}` — dock-path adds `"10":"RTK fixed"` not in the pilot-path baseline | |
| `»gps_number` / `»rtk_number` | Satellite counts | `int` | | |
| `storage` | Storage capacity | `struct` with `»total, »used` | `int` kilobytes | `r` |
| `battery` | Aircraft battery information | `struct` | | `r` |
| `»capacity_percent` | Total remaining battery capacity | `int` | `{"max":100,"min":0}` | |
| `»remain_flight_time` | Remaining flight time | `int` | `{"unit_name":"Seconds / s"}` | |
| `»return_home_power` | % power required for return home | `int` | `{"max":100,"min":0}` | |
| `»landing_power` | Forced landing battery % | `int` | `{"max":100,"min":0}` | |
| `»batteries` | Per-battery details | `array` of `struct` with `»»capacity_percent, »»index, »»sn, »»type, »»sub_type, »»firmware_version, »»loop_times, »»voltage, »»temperature, »»high_voltage_storage_days` | voltage mV, temperature °C (one decimal) | |
| `total_flight_distance` | Accumulated total mileage | `float` | `{"unit_name":"Meters / m"}` | `r` |
| `total_flight_time` | Accumulated total flight time | `float` | `{"unit_name":"Seconds / s"}` | `r` |
| `wind_direction` | Current wind direction | `enum_int` | `{"1":"True North","2":"Northeast","3":"East","4":"Southeast","5":"South","6":"Southwest","7":"West","8":"Northwest"}` | `r` |
| `wind_speed` | Wind speed | `float` | `{"unit_name":"0.1 Meters per second / m/s"}` — estimated from aircraft attitude; reference only | `r` |
| `home_distance` | Distance from the Home point | `float` | | `r` |
| `attitude_head` | Yaw axis angle | `int` | with true-north reference; positive values 0→6 o'clock, negative 6→12 | `r` |
| `attitude_roll` / `attitude_pitch` | Roll / pitch angles | `float` | | `r` |
| `elevation` | Relative takeoff-point altitude | `float` | | `r` |
| `height` | Absolute (ellipsoid) height | `double` | `height = height_above_takeoff + ellipsoid_height_of_takeoff` — dock-path uses `double`; pilot-path baseline uses `float` | `r` |
| `latitude` | Current latitude | `double` | `{"max":"3.4028235E38","min":"-1.4E-45","step":"0.1"}` — dummy float range in source; real range `[-90, 90]`. Dock-path uses `double`, pilot-path `float` | `r` |
| `longitude` | Longitude of the current position | `double` | `{"max":"3.4028235E38","min":"-1.4E-45","step":"0.1"}` — real range `[-180, 180]` | `r` |
| `vertical_speed` | Vertical speed | `float` | `{"unit_name":"Meters per second / m/s"}` | `r` |
| `horizontal_speed` | Horizontal speed | `float` | | `r` |
| `gear` | Gear | `enum_int` | `{"0":"A","1":"P","2":"NAV","3":"FPV","4":"FARM","5":"S","6":"F","7":"M","8":"G","9":"T"}` | `r` |
| `mode_code` | Aircraft state | `enum_int` | `{"0":"Standby","1":"Takeoff preparation","2":"Takeoff preparation completed","3":"Manual flight","4":"Automatic takeoff","5":"Wayline flight","6":"Panoramic photography","7":"Intelligent tracking","8":"ADS-B avoidance","9":"Auto returning to home","10":"Automatic landing","11":"Forced landing","12":"Three-blade landing","13":"Upgrading","14":"Not connected","15":"APAS","16":"Virtual stick state","17":"Live flight Controls","18":"Airborne RTK fixing mode","19":"Dock address selecting","20":"POI"}` — M3D dock-path adds values `19` + `20` beyond the pilot-path baseline. Description for `19`: "Dock address selection, indicating the aircraft hovers in the air for dock address selection and checking RTK signal quality" | `r` |
| `distance_limit_status` | Aircraft distance limit state | `struct` | | `rw` |
| `»state` | Whether distance limit is enabled | `enum_int` | `{"0":"Not set","1":"Already set"}` | |
| `»distance_limit` | Limited distance | `int` | `{"max":"8000","min":"15","step":"1","unit_name":"Meters / m"}` | |
| `»is_near_distance_limit` | Approaching distance limit | `enum_int` | `{"0":"Not reaching","1":"Approaching"}` | `r` |
| `rth_altitude` | Return home altitude | `int` | `{"max":500,"min":20,"unit_name":"Meters / m"}` | `rw` |

### A.2 State properties — `pushMode: 1`

18 top-level properties push on `thing/product/{m3d_sn}/state` on change.

| Property | Description | Type | Constraint | Access |
|---|---|---|---|---|
| `best_link_gateway` | Best-connected gateway SN | `text` | In the multi-dock scenario, after frequency matching with two docks, the aircraft pushes the SN of the best-connected dock | `r` |
| `wireless_link_topo` | Image transmission topology | `struct` | | `r` |
| `»secret_code` | Encryption code | `array` | `{"size": 28, "item_type": int}` | |
| `»center_node` | Aircraft frequency matching info | `struct` with `»»sdr_id, »»sn` | | |
| `»leaf_nodes` | Connected dock / RC frequency matching info | `array` of `struct` with `»»sdr_id, »»sn, »»control_source_index` | `control_source_index ∈ [1, 2]` | |
| `flysafe_database_version` | FlySafe database version | `text` | `{"length":"64"}` | `r` |
| `offline_map_enable` | Offline map switch | `bool` | `{"0":"Disable","1":"Enable"}` — when disabled, offline map sync is not automatic | `r` |
| `dongle_infos` | 4G Dongle information | `array` of `struct` | same shape as the baseline dongle catalog (see [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md) §2) with one difference — dock-path `»esim_activate_state` enum is `{"0":"Unknown","1":"Not activated","2":"Activated"}` (3 values), pilot-path baseline is 2-value | `r` |
| `current_rth_mode` | Actual RTH altitude mode | `enum_int` | `{"0":"Intelligent altitude","1":"Preset altitude"}` | `r` |
| `rth_mode` | RTH altitude mode setting | `enum_int` | `{"0":"Intelligent altitude","1":"Preset altitude"}` — Dock does not support setting `0`; only `"Preset altitude"` (`1`) is usable | `r` |
| `serious_low_battery_warning_threshold` | Critical low battery warning % | `int` | user-set | `r` |
| `low_battery_warning_threshold` | Low battery warning % | `int` | user-set | `r` |
| `control_source` | Current control source | `text` | device A/B or browser UUID | `r` |
| `home_latitude` | Home point latitude | `double` | dock-path uses `double`; pilot-path `float` | `r` |
| `home_longitude` | Home point longitude | `double` | | `r` |
| `firmware_upgrade_status` | Firmware upgrade state | `enum_int` | `{"0":"Not upgraded","1":"Upgrading"}` | `r` |
| `compatible_status` | Firmware consistency | `enum_int` | `{"0":"No consistency upgrade required","1":"Consistency upgrade required"}` | `r` |
| `firmware_version` | Firmware version | `text` | `{"length":"64"}` | `r` |
| `mode_code_reason` | Reason aircraft entered current state | `enum_int` | 24-value enum `{"0":"No meaning", ..., "22":"Encountered obstacles during the return (landing)","23":"Triggered by strong winds in the dock scene (return)"}` — M3D dock-path adds value `23` beyond the pilot-path baseline (which stops at `22`) | `r` |
| `commander_flight_height` | FlyTo task height | `float` | `{"max":3000,"min":2,"step":0.1,"unit_name":"Meters / m"}` — relative to dock takeoff point | `rw` |
| `commander_flight_mode` | FlyTo task mode | `enum_int` | `{"0":"Optimal height flight","1":"Preset height flight"}` | `rw` |
| `commander_mode_lost_action` | FlyTo signal-lost action | `enum_int` | `{"0":"Continue with the to-point flight mission","1":"Exit the to-point flight mission and perform normal loss of control behavior"}` | `rw` |
| `camera_watermark_settings` | Camera watermark settings | `struct` | same 9-field shape as baseline (see [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md) §2) | `rw` |
| `psdk_ui_resource` | PSDK UI resource package | `array` of `struct` | | `r` |
| `»psdk_index` | PSDK payload device index | `int` | `{"min":0}` | `r` |
| `»psdk_ready` | PSDK readiness state | `enum_int` | `{"0":"Not ready","1":"Ready"}` | `r` |
| `»object_key` | OSS object key | `text` | Resource file key for PSDK UI payload | `r` |
| `psdk_widget_values` | PSDK payload device attribute values | `array` of `struct` | | `r` |
| `»psdk_index` / `»psdk_name` / `»psdk_sn` / `»psdk_version` / `»psdk_lib_version` | PSDK identity and version info | `int` / `text` | | `r` |
| `»speaker` | Speaker state | `struct` | | `r` |
| `»»work_mode` | Speaker working mode | `enum_int` | `{"0":"TTS payload mode","1":"Recording and speaking"}` | `r` |
| `»»play_mode` | Speaker playback mode | `enum_int` | `{"0":"Single play","1":"Loop play (single track)"}` | `r` |
| `»»play_volume` | Speaker volume | `int` | `{"max":100,"min":0,"step":1}` | `r` |
| `»»system_state` | Speaker system state | `enum_int` | `{"0":"Idle","1":"Transmitting (from dock to aircraft)","2":"Playing","3":"Abnormal","4":"TTS text conversion in progress","99":"Downloading (from dock to cloud)"}` | `r` |
| `»»play_file_name` | File name of last-played file | `text` | `{"length":128,"unit_name":"Bytes / B"}` | `r` |
| `»»play_file_md5` | MD5 of file last played | `text` | | `r` |
| `»values` | PSDK widget value list | `array` of `struct` with `»»index, »»value` | | `r` |
| `remaining_power_for_return_home` | Return reserve battery % | `int` | `{"max":100,"min":0}` — note: "For DJI Dock 2, we recommend configuring this value in the 25%–50% range to provide a safer RTH power margin." M4D differs — see [`m4d.md`](m4d.md) §5 | `rw` |

### A.3 `{type-subtype-gimbalindex}` payload struct (dock-path)

M3D emits a per-payload property struct keyed by `{type-subtype-gimbalindex}` (e.g., `"52-0-0"` for the H30T payload). Same fields as the [pilot-path baseline `{type-subtype-gimbalindex}` struct](_aircraft-pilot-base.md#1-osd-properties--pushmode-0) — gimbal attitude (`gimbal_pitch` / `gimbal_roll` / `gimbal_yaw`), laser ranging (`measure_target_longitude` / `_latitude` / `_altitude` / `_distance` / `_error_state`), `payload_index`, `zoom_factor`, and the thermal cluster (`thermal_current_palette_style` — `rw` with the same 10-value palette enum; `thermal_supported_palette_styles`; `thermal_gain_mode` — `rw`; `thermal_isotherm_state` / `_upper_limit` / `_lower_limit` — `rw`; `thermal_global_temperature_min` / `_max`).

The source table cell at line 49 of [`DJI_CloudAPI_M3D_M3DT_Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt) — wait, actually the M3D/M3DT file uses the placeholder cell without garble — the schema cell reads `type_subtype_gimbalindex` (underscored) cleanly. The DJI M4D dock-path copy garbles this to `{_{type-subtype-gimbalindex}__aembLbhPpc}` instead; see [`m4d.md`](m4d.md) §4.

---

## B. Pilot-path properties (via RC Pro Enterprise gateway)

When an RC Pro Enterprise is the gateway (operator-in-the-loop flight), the M3D publishes the pilot-path generic aircraft catalog verbatim. See [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md) for the complete property list.

**Cross-path property overlap — dock vs pilot on the same M3D:**

| Property class | Dock-path exclusive | Pilot-path baseline shares | Shape difference |
|---|---|---|---|
| Topology | `best_link_gateway`, `wireless_link_topo` | — | Dock-path only; pilot-path aircraft has no topology surface (the RC owns that). |
| RTH settings | `current_rth_mode`, `rth_mode`, `rth_altitude`, `remaining_power_for_return_home` | — | Dock-scheduled return policy; pilot-controlled flight does not publish these on the aircraft's topic — the operator controls RTH through the RC. |
| FlyTo commander | `commander_flight_height`, `commander_flight_mode`, `commander_mode_lost_action` | — | Dock-scheduled FlyTo; not a pilot-path property. |
| Wayline database | `flysafe_database_version` | — | State property on the aircraft when dock is relaying. |
| FOV / camera subsystem | (shared; same `cameras` struct) | ✓ | Same shape — label drift (`"Shutter priority exposure"` vs `"Shutter Priority"`, `"Ir metering off"` vs `"Temperature measurement off"`, `"Auto(high sense)"` vs `"Auto(High Sense)"`, `"ev"` vs `"EV"`) — see `_aircraft-pilot-base.md` §4.1 |
| Obstacle avoidance | — | ✓ | `obstacle_avoidance` is `rw` on dock-path, `r` on pilot-path baseline. |
| PSDK state | `psdk_ui_resource`, `psdk_widget_values`, `»speaker` | — | Pilot-path aircraft does not expose PSDK property state — the operator queries PSDK via the RC. |
| Maps | `offline_map_enable` | — | Dock-path only. |
| Country code | — | ✓ `country` | Pilot-path exposes `country`; dock-path does not. |
| Mode code | Different max value | | Dock-path max `20` ("POI"); pilot-path max `18` ("Airborne RTK fixing mode"). |
| `mode_code_reason` | Dock-path max `23`; pilot-path max `22`. | | |

All other properties (battery / position / attitude / firmware / gimbal struct / watermarks / maintain_status) are present on both paths with identical semantics.

---

## 3. Settable via `property/set` — `accessMode: rw`

Dock-path writable surface (6 top-level properties):

| Property | Push mode | Value domain | Notes |
|---|---|---|---|
| `obstacle_avoidance` | osd | `struct {horizon, upside, downside} ∈ {0, 1}` | Three-direction sensor enable. |
| `height_limit` | osd | `int ∈ [20, 1500]` m | |
| `night_lights_state` | osd | `enum_int {0: Disable, 1: On}` | |
| `distance_limit_status` | osd | `struct {state, distance_limit}` where `distance_limit ∈ [15, 8000]` m | |
| `rth_altitude` | osd | `int ∈ [20, 500]` m | |
| `commander_flight_height` | state | `float ∈ [2, 3000]` m (step 0.1) | Dock-scheduled FlyTo. |
| `commander_flight_mode` | state | `enum_int {0: Optimal, 1: Preset}` | |
| `commander_mode_lost_action` | state | `enum_int {0: Continue mission, 1: Normal loss-of-control behavior}` | |
| `camera_watermark_settings` | state | `struct` with 9 rw sub-fields | Same shape as baseline. |
| `remaining_power_for_return_home` | state | `int ∈ [0, 100]` | Dock 2 recommends 25–50%. |

Plus the thermal cluster on the `{type-subtype-gimbalindex}` struct (`thermal_current_palette_style`, `thermal_gain_mode`, `thermal_isotherm_state`, `thermal_isotherm_upper_limit`, `thermal_isotherm_lower_limit`) — written via the payload-indexed key.

Pilot-path writable surface matches the baseline: `height_limit`, `night_lights_state`, `camera_watermark_settings`, and the thermal cluster. Dock-path exclusives (obstacle_avoidance, commander_*, distance_limit_status, rth_altitude, remaining_power_for_return_home) are not writable on the pilot path — they are not exposed there.

Aircraft flight operations (takeoff / land / waypoint delivery / DRC) are exposed as **services** under [`mqtt/dock-to-cloud/services/`](../mqtt/dock-to-cloud/services/) (dock-path) or [`mqtt/pilot-to-cloud/services/`](../mqtt/pilot-to-cloud/services/) (pilot-path) — not as writable properties.

## 4. DJI-source inconsistencies (flagged, not escalated)

1. **Type drift `latitude`/`longitude`/`height`** — dock-path uses `double` for these properties; pilot-path baseline uses `float`. Same wire value precision matters for long flights — cloud implementations parsing both paths should retain double precision internally.
2. **`obstacle_avoidance` access mode** — dock-path declares `rw`; pilot-path baseline declares `r`. Dock-scheduled missions need to toggle obstacle avoidance pre-flight; pilot-flown aircraft toggle it via the RC UI (not via property-set).
3. **`cameras.»zoom_factor` type** — dock-path `float`; pilot-path baseline `int`. Dock-path authoritative (values include fractions).
4. **Camera enum label drift between dock-path and pilot-path** — exposure mode: `"Shutter priority exposure"` (dock) vs `"Shutter Priority"` (pilot base). ISO: `"Auto(high sense)"` (dock) vs `"Auto(High Sense)"` (pilot base). EV: `"-5.0ev"` lowercase (dock) vs `"-5.0EV"` uppercase (pilot base). Shutter `"Auto"` sentinel (value `65534`): dock uses `"Auto"` for wide and `"auto"` for zoom inconsistently within the same file. Enum codes stable across drift.
5. **`mode_code` value 19 description** — DJI's M3D dock-path source uses `"Dock address selecting"` for value `19`, with description "Dock address selection, indicating the aircraft hovers in the air for dock address selection and checking RTK signal quality." M4D dock-path uses same code but description wording differs cosmetically.
6. **`psdk_ui_resource.»object_key`** has no description field in the source. Context: this is the OSS object key for the PSDK UI resource file uploaded via 4g's `psdk_ui_resource_upload_result` event and consumed via 4g's `storage_config_get` (module=1). See [`mqtt/dock-to-cloud/events/psdk_ui_resource_upload_result.md`](../mqtt/dock-to-cloud/events/psdk_ui_resource_upload_result.md).
7. **`best_link_gateway` is the first property in the dock-path source** (line 31 of [`DJI_CloudAPI_M3D_M3DT_Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt)) — cloud implementations that key on the first property name for source detection should anchor on this.

None rise to [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) level.

## 5. Drift vs M4D

M3D and M4D share the same dock-path catalog shape with a handful of cohort-specific deltas:

| Property | M3D | M4D | Classification |
|---|---|---|---|
| `mode_code` max value | `20` ("POI") | `21` ("during the inbound and outbound flight procedures") | **Enum extension** — M4D adds a value. Cloud implementations targeting both must handle the 22-value form. |
| `remaining_power_for_return_home` recommended note | "For DJI Dock 2, 25%–50%" | "For DJI Dock 3, 15%–50%" | Cosmetic — recommendation text only; wire range identical. |
| `type_subtype_gimbalindex` schema-cell | `type_subtype_gimbalindex` (clean) | `{_{type-subtype-gimbalindex}__aembLbhPpc}` (garbled in DJI source) | Source extraction artifact on M4D; schema intent identical. |

All other dock-path properties are identical in shape and semantics. `mode_code_reason` goes to `23` on both cohorts.

Pilot-path: M3D uses the generic aircraft baseline verbatim. M4D uses the generic baseline plus the pilot-path extensions in [`m4d.md`](m4d.md) (`offline_map_enable`, `current_rth_mode`, `rth_mode`, `commander_flight_*`, `current_commander_flight_mode`, `commander_mode_lost_action`, `mode_code` extension to value 19 `"Dock site evaluation in progress"`). M3D does not have those pilot-path extensions in any DJI-published extract.

## 6. v1.11 → v1.15 drift

Dock-path v1.11 canonical: [`Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/10.aircraft/10.m3d-properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/10.aircraft/10.m3d-properties.md) carries the same 42 top-level properties as v1.15. Observed drift:

| Field | v1.11 | v1.15 | Classification |
|---|---|---|---|
| `mode_code` | max `20` `"POI"` | max `20` `"POI"` | No drift. |
| `mode_code_reason` | max `22` `"Encountered obstacles during the return (landing)"` | max `23` adds `"Triggered by strong winds in the dock scene (return)"` | **Enum extension** — v1.15 adds one value. Upward compatible. |
| `»payload_index` in `type_subtype_gimbalindex` | `text` formatted `*{type-subtype-gimbalindex}*` (italicized) | same text | Cosmetic (italics are Markdown-level; wire value identical). |
| Camera enum labels | `"Auto(high sense)"` / `"1/8000 s"` / `"-5.0ev"` / `"Fixed"` / `"Focus succeeded"` | Same | No drift on dock-path. |
| `rth_altitude` | not published at aircraft level (Dock 2 v1.11 lists only at dock level) | published on M3D aircraft OSD | **Source-coverage gap** — v1.15 is more complete. |
| `distance_limit_status` | not in v1.11 M3D doc | published | **New property** — added in v1.15. |
| `commander_*` trio | present | present | No drift. |

Pilot-path v1.11 M3-series canonical: same as generic aircraft baseline. No M3D-specific drift.

No semantic escalations.

## 7. Source provenance

| Source | Lines | Role |
|---|---|---|
| [`DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt) | 2,373 | v1.15 dock-path primary. Covers M3D + M3TD co-documented; per-model splits live at the `cameras.»payload_index` enum level. |
| [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md) | — | v1.15 pilot-path canonical. M3D pilot-path is this baseline verbatim. |
| [`Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/10.aircraft/10.m3d-properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/10.aircraft/10.m3d-properties.md) | — | v1.11.3 dock-path M3D cross-check. |
| [`Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/10.m3-series/00.properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/10.m3-series/00.properties.md) | — | v1.11.3 pilot-path M3-series cross-check. Matches the pilot-path baseline. |
| [`dock2.md`](dock2.md) | — | Dock 2 gateway catalog — for cross-referenced context on the dock's properties that pair with M3D-reported properties (e.g., `sub_device`). |
| [`m3td.md`](m3td.md) | — | Thermal variant annex. |
