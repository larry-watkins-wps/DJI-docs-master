# Shared Aircraft Properties — Pilot-to-Cloud baseline

**Gateway role**: aircraft device (aircraft SN is `{device_sn}` on all topics below). The gateway — the RC — relays these via the pilot-to-cloud path; see [`rc-plus-2.md`](rc-plus-2.md) / [`rc-pro.md`](rc-pro.md) *(pending Phase 6c)* for the RC-level gateway properties.
**Cohort**: shared baseline for every in-scope aircraft when reported through the **pilot-to-cloud** path (RC Plus 2 Enterprise or RC Pro Enterprise as gateway). Per-aircraft files cite this baseline and enumerate only the deltas.

**Source**: [`DJI_Cloud/DJI_CloudAPI_Aircraft-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_Aircraft-Properties.txt) (1,124 lines, v1.15). DJI publishes this as the generic pilot-to-cloud aircraft catalog at [developer.dji.com/.../pilot-to-cloud/mqtt/others/aircraft/properties](https://developer.dji.com/doc/cloud-api-tutorial/en/api-reference/pilot-to-cloud/mqtt/others/aircraft/properties.html). Per-aircraft extensions (M3D / M3TD via v1.11 `10.m3-series/` subtree; M4D / M4TD via `DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`) layer on top of this baseline.

Published **42 top-level properties** — 34 OSD, 8 state — plus the `{type-subtype-gimbalindex}` payload struct that uses the payload index as the key. `camera_watermark_settings` is the only rw property at the top level; `height_limit` and `night_lights_state` are rw scalars. All other properties are r.

Topic mapping (see Phase 2 [`mqtt/README.md`](../mqtt/README.md) for envelope; pilot-to-cloud shares the same 13-topic taxonomy as dock-to-cloud, verified envelope-identical):

| Topic | Push mode | Carries |
|---|---|---|
| `thing/product/{aircraft_sn}/osd` | 0 — stable frequency (~0.5 Hz) | OSD properties — §1 below. |
| `thing/product/{aircraft_sn}/state` | 1 — on-change | State properties — §2 below. |
| `thing/product/{aircraft_sn}/property/set` | — | Cloud writes one of the 3 settable top-level keys (plus nested watermark fields) — §3. |
| `thing/product/{aircraft_sn}/property/set_reply` | — | Per-key `result` echo from the aircraft. |

The `{gateway_sn}` topic family is owned by the RC, not the aircraft — see the RC doc for its own properties. This doc catalogs only the aircraft's `{device_sn}` topics.

Cross-references:
- [`mqtt/pilot-to-cloud/osd/README.md`](../mqtt/pilot-to-cloud/osd/README.md) — pilot-path OSD shell; carries the [`OQ-002`](../OPEN-QUESTIONS.md#oq-002--pilot-to-cloud-osd-struct-example-appears-to-be-a-copy-paste-of-the-dock-osd-example) callout that DJI's pilot-OSD struct example is a copy of the dock example. **This file — not the copy-paste example — is canonical for pilot-path aircraft OSD content.**
- [`mqtt/pilot-to-cloud/state/README.md`](../mqtt/pilot-to-cloud/state/README.md) — pilot-path state shell.
- [`mqtt/pilot-to-cloud/property-set/README.md`](../mqtt/pilot-to-cloud/property-set/README.md) — pilot-path property-set shell.

---

## 1. OSD properties — `pushMode: 0`

34 top-level properties push on `thing/product/{aircraft_sn}/osd` at ~0.5 Hz.

| Property | Description | Type | Constraint | Access |
|---|---|---|---|---|
| `country` | Country area code | `text` | | `r` |
| `mode_code` | Aircraft state | `enum_int` | `{"0":"Standby","1":"Takeoff preparation","2":"Takeoff preparation completed","3":"Manual flight","4":"Automatic takeoff","5":"Wayline flight","6":"Panoramic photography","7":"Intelligent tracking","8":"ADS-B avoidance","9":"Auto returning to home","10":"Automatic landing","11":"Forced landing","12":"Three-blade landing","13":"Upgrading","14":"Not connected","15":"APAS","16":"Virtual stick state","17":"Live flight Controls","18":"Airborne RTK fixing mode"}` — M3/M4 cohorts extend this enum; see the per-aircraft docs | `r` |
| `cameras` | Aircraft camera information | `array` of `struct` | `{"size": -, "item_type": struct}` | `r` |
| `»remain_photo_num` | Remaining number of photos to take | `int` | | |
| `»remain_record_duration` | Remaining recording time | `int` | `{"unit_name":"Seconds / s"}` | |
| `»record_time` | Video recording duration | `int` | `{"unit_name":"Seconds / s"}` | |
| `»payload_index` | Payload index | `text` | format `{type-subtype-gimbalindex}`; Camera enumeration values per [Product Supported](https://developer.dji.com/doc/cloud-api-tutorial/en/overview/product-support.html) | |
| `»camera_mode` | Camera mode | `enum_int` | `{"0":"Capturing","1":"Recording","2":"Smart Low-Light","3":"Panoramic photography"}` | |
| `»photo_state` | Photo capturing status | `enum_int` | `{"0":"Idle","1":"Capturing photo"}` | |
| `»screen_split_enable` | Is split screen enabled | `bool` | `{"0":"Disable split screen","1":"Enable split screen"}` | |
| `»recording_state` | Recording state | `enum_int` | `{"0":"Idle","1":"Recording"}` | |
| `»zoom_factor` | Zoom factor | `int` | `{"max":200,"min":2,"unit_name":null}` — type declared `int` in the generic baseline; the M3/M4 dock-path catalogs report `float`. See §4.1 | |
| `»ir_zoom_factor` | Infrared zoom factor | `float` | `{"max":20,"min":2,"unit_name":null}` | |
| `»liveview_world_region` | Field of view (FOV) region in liveview | `struct` | coordinate origin is upper-left corner of lens | |
| `»»left` | X-axis starting point in the top-left corner | `float` | | `r` |
| `»»top` | Top-left corner's starting point on the y-axis | `float` | | `r` |
| `»»right` | Starting point of the x-axis in the bottom right corner | `float` | | `r` |
| `»»bottom` | Y-axis starting point in the lower right corner | `float` | | `r` |
| `»photo_storage_settings` | Photo storage settings collection | `array` of `enum_string` | value range `{current, wide, zoom, ir}` | |
| `»video_storage_settings` | Collection of video storage settings | `array` of `enum_string` | value range `{current, wide, zoom, ir}` | |
| `»wide_exposure_mode` | Wide-angle lens exposure mode | `enum_int` | `{"1":"Auto","2":"Shutter Priority","3":"Aperture Priority","4":"Manual"}` | |
| `»wide_iso` | Wide-angle lens ISO | `enum_int` | `{"0":"Auto","1":"Auto(High Sense)","2":"50","3":"100","4":"200","5":"400","6":"800","7":"1600","8":"3200","9":"6400","10":"12800","11":"25600","255":"FIXED"}` | |
| `»wide_shutter_speed` | Wide-angle lens shutter speed | `enum_int` | 60-value enum `{"0":"1/8000 s", ..., "59":"8.0 s", "65534":"Auto"}` — full range from `1/8000 s` through `8.0 s` in fine-grained stops, plus `"Auto"` sentinel at 65534 | |
| `»wide_exposure_value` | Wide-angle lens exposure value | `enum_int` | 32-value enum `{"1":"-5.0EV", ..., "31":"5.0EV", "255":"FIXED"}` — range −5.0 EV to +5.0 EV in 1/3-stop increments | |
| `»zoom_exposure_mode` | Zoom lens exposure mode | `enum_int` | same 4-value enum as `wide_exposure_mode` | |
| `»zoom_iso` | Zoom lens ISO | `enum_int` | same 13-value enum as `wide_iso` | |
| `»zoom_shutter_speed` | Zoom lens shutter speed | `enum_int` | same 60-value enum as `wide_shutter_speed` | |
| `»zoom_exposure_value` | Zoom lens exposure value | `enum_int` | same 32-value enum as `wide_exposure_value` | |
| `»zoom_focus_mode` | Zoom lens focus mode | `enum_int` | `{"0":"MF","1":"AFS","2":"AFC"}` | |
| `»zoom_focus_value` | Zoom lens focus value | `int` | | |
| `»zoom_max_focus_value` | Zoom lens maximum focus value | `int` | | |
| `»zoom_min_focus_value` | Zoom lens minimum focus value | `int` | | |
| `»zoom_calibrate_farthest_focus_value` | Zoom lens calibrated farthest focus value | `int` | farthest position with the clearest focus | |
| `»zoom_calibrate_nearest_focus_value` | Zoom lens calibrated nearest focus value | `int` | nearest position with the clearest focus | |
| `»zoom_focus_state` | Zoom lens focus state | `enum_int` | `{"0":"Idle","1":"Focusing","2":"Focus successful","3":"Focus failed"}` | |
| `»ir_metering_mode` | Infrared metering mode | `enum_int` | `{"0":"Temperature measurement off","1":"Spot temperature measurement","2":"Area temperature measurement"}` — dock-path catalogs use the short labels `"Ir metering off" / "Spot metering" / "Area metering"`; semantics identical | |
| `»ir_metering_point` | Infrared metering point | `struct` | | |
| `»»x` | Metering point coordinate x | `double` | `{"max":1,"min":0}` | `r` |
| `»»y` | Metering point coordinate y | `double` | `{"max":1,"min":0}` | `r` |
| `»»temperature` | Temperature of the metering point | `double` | | `r` |
| `»ir_metering_area` | Infrared metering area | `struct` | | |
| `»»x` | Top-left corner coordinate x of the metering area | `double` | `{"max":1,"min":0}` | `r` |
| `»»y` | Top-left corner coordinate y of the metering area | `double` | `{"max":1,"min":0}` | `r` |
| `»»width` | Width of the metering area | `double` | `{"max":1,"min":0}` | `r` |
| `»»height` | Height of the metering area | `double` | `{"max":1,"min":0}` | `r` |
| `»»aver_temperature` | Average temperature of the metering area | `double` | | `r` |
| `»»min_temperature_point` | Lowest temperature point in the metering area | `struct` | | `r` |
| `»»»x` | Coordinate x of the lowest temperature point | `double` | `{"max":1,"min":0}` | `r` |
| `»»»y` | Coordinate y of the lowest temperature point | `double` | `{"max":1,"min":0}` | `r` |
| `»»»temperature` | Temperature of the lowest temperature point | `double` | | `r` |
| `»»max_temperature_point` | Highest temperature point in the metering area | `struct` | | `r` |
| `»»»x` | Coordinate x of the highest temperature point | `double` | `{"max":1,"min":0}` | `r` |
| `»»»y` | Coordinate y of the highest temperature point | `double` | `{"max":1,"min":0}` | `r` |
| `»»»temperature` | Temperature of the highest temperature point | `double` | | `r` |
| `obstacle_avoidance` | Aircraft obstacle sensing state | `struct` | | `r` |
| `»horizon` | Horizontal obstacle sensing state | `enum_int` | `{"0":"Disable","1":"Enable"}` | |
| `»upside` | Upward obstacle sensing state | `enum_int` | `{"0":"Disable","1":"Enable"}` | |
| `»downside` | Downward obstacle sensing state | `enum_int` | `{"0":"Disable","1":"Enable"}` | |
| `is_near_area_limit` | Whether approaching the GEO Zone | `enum_int` | `{"0":"Not reaching the GEO Zone","1":"Approaching the GEO Zone"}` | `r` |
| `is_near_height_limit` | Whether approaching the set height limit | `enum_int` | `{"0":"Not reaching the set height limit","1":"Approaching the set height limit"}` | `r` |
| `height_limit` | Aircraft height limit | `int` | `{"max":"1500","min":"20","step":"1","unit_name":"Meters / m"}` | `rw` |
| `night_lights_state` | Aircraft night lights state | `enum_int` | `{"0":"Disable","1":"On"}` | `rw` |
| `activation_time` | Aircraft activation time | `int` | `{"unit_name":"Seconds / s"}` — Unix epoch | `r` |
| `maintain_status` | Maintenance information | `struct` | | `r` |
| `»maintain_status_array` | Maintenance entries | `array` of `struct` | | |
| `»»state` | Maintenance state | `enum_int` | `{"0":"No maintenance","1":"With maintenance"}` | |
| `»»last_maintain_type` | Last maintenance type | `enum_int` | `{"1":"Basic maintenance of the aircraft","2":"Regular maintenance of the aircraft","3":"Deep maintenance of the aircraft"}` | |
| `»»last_maintain_time` | Last maintenance time | `date` | `{"unit_name":"Seconds / s"}` | |
| `»»last_maintain_flight_time` | Last maintenance flight hours | `int` | `{"unit_name":"Hours / h"}` | |
| `»»last_maintain_flight_sorties` | Last maintenance flight sorties | `int` | `{"max":"2147483647","min":"0","step":"1"}` | |
| `total_flight_sorties` | Accumulated total sorties of the aircraft | `int` | `{"max":"2147483647","min":"0","step":"1"}` | `r` |
| `track_id` | Track ID | `text` | `{"length":"64"}` | `r` |
| `position_state` | Satellite search state | `struct` | | `r` |
| `»is_fixed` | Whether is Fixed | `enum_int` | `{"0":"Not started","1":"Fixing","2":"Fixing successful","3":"Fixing failed"}` | |
| `»quality` | Satellite acquisition mode | `enum_int` | `{"1":"Gear 1","2":"Gear 2","3":"Gear 3","4":"Gear 4","5":"Gear 5"}` — the dock-path catalog adds `"10":"RTK fixed"` as a sixth value; the pilot-path generic baseline omits it | |
| `»gps_number` | Number of GPS satellites | `int` | | |
| `»rtk_number` | Number of RTK satellite acquisitions | `int` | | |
| `storage` | Storage capacity | `struct` | kb | `r` |
| `»total` | Total capacity | `int` | `{"unit_name":"Kilobytes / KB"}` | |
| `»used` | Used capacity | `int` | `{"unit_name":"Kilobytes / KB"}` | |
| `battery` | Aircraft battery information | `struct` | | `r` |
| `»capacity_percent` | Total remaining battery capacity | `int` | `{"max":100,"min":0}` | |
| `»remain_flight_time` | Remaining flight time | `int` | `{"unit_name":"Seconds / s"}` | |
| `»return_home_power` | Percentage of power required for return home | `int` | `{"max":100,"min":0}` | |
| `»landing_power` | Forced landing battery percentage | `int` | `{"max":100,"min":0}` | |
| `»batteries` | Battery details | `array` of `struct` | | |
| `»»capacity_percent` | Remaining battery capacity | `int` | `{"max":100,"min":0}` | |
| `»»index` | Battery bay index | `int` | `{"min":"0"}` | |
| `»»sn` | Battery serial number | `text` | | |
| `»»type` | Battery type | `enum_int` | `{}` — empty enum in source; populated at runtime per battery model | |
| `»»sub_type` | Battery subtype | `enum_int` | `{}` — empty enum in source | |
| `»»firmware_version` | Firmware version | `text` | | |
| `»»loop_times` | Battery cycle count | `int` | | |
| `»»voltage` | Voltage | `int` | `{"unit_name":"Millivolts / mV"}` | |
| `»»temperature` | Temperature | `float` | `{"unit_name":"Celsius / °C"}` — retain one decimal place | |
| `»»high_voltage_storage_days` | High voltage storage days | `int` | `{"unit_name":"Days / day"}` | |
| `total_flight_distance` | Accumulated total mileage of the aircraft | `float` | `{"unit_name":"Meters / m"}` | `r` |
| `total_flight_time` | Accumulated total flight time of the aircraft | `float` | `{"unit_name":"Seconds / s"}` — M4D pilot-path catalog (Matrice4-Enterprise) declares this as `int`; see §4.1 | `r` |
| `wind_direction` | Current wind direction | `enum_int` | `{"1":"True North","2":"Northeast","3":"East","4":"Southeast","5":"South","6":"Southwest","7":"West","8":"Northwest"}` — M4D pilot-path catalog labels value `1` as `"North"` (not `"True North"`); see §4.1 | `r` |
| `wind_speed` | Wind speed | `float` | `{"unit_name":"0.1 Meters per second / m/s"}` — estimated, based on aircraft attitude; reference only | `r` |
| `home_distance` | Distance from the Home point | `float` | | `r` |
| `attitude_head` | Yaw axis angle | `int` | with true north angle (longitude). Positive values from 0 to 6 o'clock direction, negative values from 6 to 12 o'clock | `r` |
| `attitude_roll` | Roll axis angle | `float` | | `r` |
| `attitude_pitch` | Pitch axis angle | `float` | | `r` |
| `elevation` | Relative takeoff-point altitude | `float` | | `r` |
| `height` | Absolute height | `float` | relative to Earth ellipsoid; `height = height_above_takeoff + ellipsoid_height_of_takeoff` | `r` |
| `latitude` | Current latitude | `float` | `{"max":"3.4028235E38","min":"-1.4E-45","step":"0.1"}` — dummy max/min (float range); real value is `[-90, 90]` | `r` |
| `longitude` | Longitude of the current position | `float` | `{"max":"3.4028235E38","min":"-1.4E-45","step":"0.1"}` — dummy max/min; real value is `[-180, 180]` | `r` |
| `vertical_speed` | Vertical speed | `float` | `{"unit_name":"Meters per second / m/s"}` | `r` |
| `horizontal_speed` | Horizontal speed | `float` | | `r` |
| `gear` | Gear | `enum_int` | `{"0":"A","1":"P","2":"NAV","3":"FPV","4":"FARM","5":"S","6":"F","7":"M","8":"G","9":"T"}` | `r` |
| `{type-subtype-gimbalindex}` | Per-payload property bag | `struct` | key is the payload index (matches the `cameras.»payload_index` value); pushes nested gimbal attitude + laser-ranging + thermal sub-fields | `r` |
| `»gimbal_pitch` | Gimbal pitch axis angle | `double` | `{"max":"180","min":"-180","step":0.1,"unit_name":"Degrees / deg"}` | `r` |
| `»gimbal_roll` | Gimbal roll axis angle | `double` | `{"max":"180","min":"-180","step":0.1,"unit_name":"Degrees / deg"}` | `r` |
| `»gimbal_yaw` | Gimbal yaw axis angle | `double` | `{"max":"180","min":"-180","step":0.1,"unit_name":"Degrees / deg"}` | `r` |
| `»measure_target_longitude` | Laser ranging target longitude | `double` | `{"max":"180","min":"-180","unit_name":"Degrees / deg"}` | `r` |
| `»measure_target_latitude` | Laser ranging target latitude | `double` | `{"max":"90","min":"-90","unit_name":"Degrees / deg"}` | `r` |
| `»measure_target_altitude` | Laser ranging target altitude | `double` | `{"unit_name":"Meters / m"}` | `r` |
| `»measure_target_distance` | Laser ranging distance | `double` | `{"unit_name":"Meters / m"}` | `r` |
| `»measure_target_error_state` | Laser ranging state | `enum_int` | `{"0":"NORMAL","1":"TOO_CLOSE","2":"TOO_FAR","3":"NO_SIGNAL"}` | `r` |
| `»payload_index` | Payload index in the format `{type-subtype-gimbalindex}` | `text` | | `r` |
| `»zoom_factor` | Zoom factor | `double` | | `r` |
| `»thermal_current_palette_style` | Palette style | `enum_int` | `{"0":"WHITE_HOT","1":"BLACK_HOT","2":"RED_HOT","3":"GREEN_HOT","5":"RAINBOW","6":"IRONBOW1","8":"ICE_FIRE","11":"COLOR1","12":"COLOR2","13":"RAIN"}` — note gaps at `4`, `7`, `9`, `10` (reserved by DJI) | `rw` |
| `»thermal_supported_palette_styles` | Collection of supported palette styles by the device | `array` of `enum_int` | capability varies per device; parent `pushMode` is 1 despite sibling 0 — the supported-styles set changes only on firmware/payload replacement | `r` |
| `»thermal_gain_mode` | Gain Mode | `enum_int` | `{"0":"Auto","1":"Low Gain. Temperature Range is from 0°C to 500°C","2":"High Gain. Temperature Range is from -20°C to 150°C"}` | `rw` |
| `»thermal_isotherm_state` | Whether isotherm is enabled | `enum_int` | `{"0":"Disable","1":"Enable"}` — highlights temperature range of interest in image | `rw` |
| `»thermal_isotherm_upper_limit` | Upper limit of the temperature range for isotherm | `int` | `{"unit_name":"Celsius / °C"}` — effective only when isotherm enabled | `rw` |
| `»thermal_isotherm_lower_limit` | Lower limit of the temperature range for isotherm | `int` | `{"unit_name":"Celsius / °C"}` — effective only when isotherm enabled | `rw` |
| `»thermal_global_temperature_min` | Minimum temperature measured in the overall view | `float` | `{"unit_name":"Celsius / °C"}` | `r` |
| `»thermal_global_temperature_max` | Maximum temperature measured in the overall view | `float` | `{"unit_name":"Celsius / °C"}` | `r` |

## 2. State properties — `pushMode: 1`

8 top-level properties push on `thing/product/{aircraft_sn}/state` on change.

| Property | Description | Type | Constraint | Access |
|---|---|---|---|---|
| `mode_code_reason` | The reason the aircraft entered the current state | `enum_int` | 23-value enum `{"0":"No meaning","1":"Insufficient battery power (return, landing)", ..., "22":"Encountered obstacles during the return (landing)"}` — the M3/M4 dock-path catalogs extend to value 23 (`"Triggered by strong winds in the dock scene (return)"`); pilot-path baseline stops at 22 | `r` |
| `dongle_infos` | 4G Dongle information | `array` of `struct` | same shape as the dock-level `dongle_infos` (Dock 2 / Dock 3 §2) | `r` |
| `»imei` | Dongle IMEI | `text` | unique per dongle | `r` |
| `»dongle_type` | Dongle type | `enum_int` | `{"6":"Old Dongle","10":"New Dongle with eSIM support"}` | `r` |
| `»eid` | Dongle EID | `text` | unique eSIM ID | `r` |
| `»esim_activate_state` | eSIM activation state | `enum_int` | `{"0":"Not activated","1":"Activated"}` — 2-value form (Dock 3 pilot extends with `"0":"Unknown"` at 0, shifting labels; see M4D / M3D docs) | `r` |
| `»sim_card_state` | SIM card state | `enum_int` | `{"0":"Not inserted","1":"Inserted"}` | `r` |
| `»sim_slot` | SIM card slot enable state | `enum_int` | `{"0":"Unknown","1":"Physical SIM card","2":"eSIM"}` | `r` |
| `»esim_infos` | eSIM information | `array` of `struct` | | `r` |
| `»»telecom_operator` | Supported operators | `enum_int` | `{"0":"Unknown","1":"Mobile","2":"China Unicom","3":"Telecommunications"}` — Dock 3 catalogs fully-qualify to `"China Mobile"` / `"China Telecom"`; pilot-path baseline uses short labels | `r` |
| `»»enabled` | eSIM enable state | `bool` | `{"false":"Not in use","true":"In use"}` — only one eSIM can be enabled at a time | `r` |
| `»»iccid` | SIM ICCID | `text` | | `r` |
| `»sim_info` | Physical SIM card | `struct` | | `r` |
| `»»telecom_operator` | Supported operators | `enum_int` | same 4-value enum as `esim_infos.telecom_operator` | `r` |
| `»»sim_type` | SIM card type | `enum_int` | `{"0":"Unknown","1":"Other regular SIM card","2":"Three-network card"}` | `r` |
| `»»iccid` | SIM ICCID | `text` | | `r` |
| `serious_low_battery_warning_threshold` | Critical low battery warning | `int` | user-set % | `r` |
| `low_battery_warning_threshold` | Low battery warning | `int` | user-set % | `r` |
| `control_source` | Current control source | `text` | device (A / B) or browser-generated UUID | `r` |
| `home_latitude` | Home point latitude | `float` | | `r` |
| `home_longitude` | Home point longitude | `float` | | `r` |
| `firmware_upgrade_status` | Firmware upgrade state | `enum_int` | `{"0":"Not upgraded","1":"Upgrading"}` | `r` |
| `compatible_status` | Firmware consistency | `enum_int` | `{"0":"No consistency upgrade required","1":"Consistency upgrade required"}` — consistent firmware update required when some aircraft modules' firmware versions are inconsistent with the system's compatible set (e.g., battery not yet updated after aircraft + RC updated) | `r` |
| `firmware_version` | Firmware version | `text` | `{"length":"64"}` | `r` |
| `camera_watermark_settings` | Camera watermark settings | `struct` | user config for watermarks on photos + video; live-stream watermarks not supported | `rw` |
| `»global_enable` | Watermark display global enable switch | `enum_int` | `{"0":"Disable","1":"Enable"}` | `rw` |
| `»drone_type_enable` | Aircraft model display switch | `enum_int` | `{"0":"Disable","1":"Enable"}` | `rw` |
| `»drone_sn_enable` | Aircraft serial number display switch | `enum_int` | `{"0":"Disable","1":"Enable"}` | `rw` |
| `»datetime_enable` | Date/time display switch | `enum_int` | `{"0":"Disable","1":"Enable"}` — time zone defaults to local | `rw` |
| `»gps_enable` | Latitude/longitude/altitude display switch | `enum_int` | `{"0":"Disable","1":"Enable"}` | `rw` |
| `»user_custom_string_enable` | Custom text display switch | `enum_int` | `{"0":"Disable","1":"Enable"}` | `rw` |
| `»user_custom_string` | Custom text content | `text` | up to 250 bytes | `rw` |
| `»layout` | Position of the watermark in the frame | `enum_int` | `{"0":"Top-left","1":"Bottom-left","2":"Top-right","3":"Bottom-right"}` | `rw` |

Note: the `{type-subtype-gimbalindex}` struct's nested `»payload_index` child has `pushMode: 1` in the source (odd — the parent struct is OSD with `pushMode: 0`). Treat as a source-table defect; the whole `{type-subtype-gimbalindex}` payload rides the OSD topic with the parent's mode.

## 3. Settable via `property/set` — `accessMode: rw`

Three top-level properties plus the `camera_watermark_settings` substructure.

| Property | Push mode | Value domain | Notes |
|---|---|---|---|
| `height_limit` | osd | `int` in `[20, 1500]` m | Cloud-set max altitude. |
| `night_lights_state` | osd | `enum_int {0: Disable, 1: On}` | |
| `camera_watermark_settings` | state | `struct` (all 9 sub-fields are `rw`) | Global switch + per-field toggles + custom string + layout. |
| `»thermal_current_palette_style` | osd *(nested)* | `enum_int` 10-value palette set | Only applicable to the thermal payload struct; written via the payload-indexed `{type-subtype-gimbalindex}` key. |
| `»thermal_gain_mode` | osd *(nested)* | `enum_int {0: Auto, 1: Low, 2: High}` | See above — payload-indexed. |
| `»thermal_isotherm_state` | osd *(nested)* | `enum_int {0: Disable, 1: Enable}` | Payload-indexed. |
| `»thermal_isotherm_upper_limit` | osd *(nested)* | `int` (°C) | Payload-indexed. |
| `»thermal_isotherm_lower_limit` | osd *(nested)* | `int` (°C) | Payload-indexed. |

Aircraft flight operations (takeoff / land / waypoint delivery / DRC) are exposed as **services** under [`mqtt/pilot-to-cloud/services/`](../mqtt/pilot-to-cloud/services/) and [`mqtt/pilot-to-cloud/drc/`](../mqtt/pilot-to-cloud/drc/) — not as writable properties.

## 4. DJI-source inconsistencies (flagged, not escalated)

### 4.1 Type and label drift between pilot-path and dock-path catalogs

- **`cameras.»zoom_factor` type** — pilot-path baseline declares `int`, the M3D / M4D dock-path catalogs declare `float`. The actual wire value carries a fraction (e.g., `2.1`), so `float` is authoritative.
- **`total_flight_time` type** — baseline + v1.11 generic pilot declare `float`; the M4D pilot-path `Matrice4-Enterprise-Properties.txt` extract declares `int`. Wire value is integer-valued in observed examples; both types parse correctly.
- **`wind_direction` value 1 label** — baseline uses `"True North"`; M4D pilot-path (Matrice4-Enterprise) uses `"North"`. Enum code `1` is the same; label only.
- **`position_state.»quality` enum** — pilot-path baseline ends at `"5":"Gear 5"` (5 values). Dock-path M3D / M4D catalogs add `"10":"RTK fixed"`. An RTK-fixed aircraft reports `10` regardless of which path is relaying.
- **`»ir_metering_mode` labels** — baseline uses long form (`"Temperature measurement off"` / `"Spot temperature measurement"` / `"Area temperature measurement"`); dock-path catalogs use short form (`"Ir metering off"` / `"Spot metering"` / `"Area metering"`). Codes `{0, 1, 2}` are identical.
- **Camera exposure-mode label drift** — baseline uses `"Auto" / "Shutter Priority" / "Aperture Priority" / "Manual"`; dock-path catalogs use `"Auto" / "Shutter priority exposure" / "Aperture priority exposure" / "Manual exposure"`. Same 4 codes.
- **Camera ISO `"Auto(High Sense)"` capitalisation** — baseline caps "High Sense"; dock-path uses lowercase `"high sense"`.
- **Camera EV unit case** — baseline uses `"EV"` / `"FIXED"`; dock-path uses `"ev"` / `"Fixed"`. Enum codes identical.
- **Camera zoom-focus-state value `2` label** — baseline `"Focus successful"`; dock-path `"Focus succeeded"`. Same code.

None of the above are semantic — codes match across the two paths. Cloud implementations that decode by integer code are safe; implementations that string-match labels must handle both forms.

### 4.2 Other inconsistencies

- **`cameras.»zoom_factor` and `»ir_zoom_factor` constraints include `"unit_name":null`** — null is a JSON null, not the string `"null"`. Cloud parsers should treat this constraint as absent.
- **`»»type` and `»»sub_type` in `battery.batteries`** — the enum is empty (`{}`) in the source. DJI populates these at runtime based on the battery model; the cloud cannot validate against a fixed enum.
- **`latitude` / `longitude` constraint uses float-range dummy max/min** (`3.4028235E38` / `-1.4E-45`). Actual valid ranges are `[-90, 90]` for latitude and `[-180, 180]` for longitude. Source-table cosmetic.
- **`{type-subtype-gimbalindex}` struct-name cell** in source uses the literal placeholder string — not a field name but the dynamic key that carries the payload index. DJI's M4D pilot-path extract garbles this as `{_{type-subtype-gimbalindex}__aembLbhPpc}` (copy-paste artifact). Authoritative is the baseline's literal `{type-subtype-gimbalindex}` usage.

None rise to [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) level.

## 5. v1.11 → v1.15 drift

The v1.11 canonical counterparts for the pilot-path aircraft catalog are:

- Generic: [`Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/30.others/10.aircraft/00.properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/30.others/10.aircraft/00.properties.md)
- M3-series: [`Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/10.m3-series/00.properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/10.m3-series/00.properties.md)

Both v1.11 docs carry the same property set as this v1.15 baseline with **no semantic drift**. Observed drift is cosmetic:

| Field | v1.11 | v1.15 | Classification |
|---|---|---|---|
| `cameras.»zoom_factor` type | `int` (generic v1.11) / `float` (M3-series v1.11) | `int` (baseline) / `float` (dock-path, M4D pilot) | Inconsistent across even the v1.11 extracts; dock-path and M4D pilot agree on `float`. |
| `»»telecom_operator` carrier labels | `"Mobile" / "China Unicom" / "Telecommunications"` | Same | No drift. |
| `mode_code_reason` max value | `22` | `22` | No drift on the pilot-path baseline. M3/M4 dock-path catalogs add `23`. |

No drift escalations. This baseline is stable across v1.11 → v1.15 in the pilot-path direction.

## 6. Property Set — request / reply

Same envelope as [`mqtt/pilot-to-cloud/property-set/README.md`](../mqtt/pilot-to-cloud/property-set/README.md). Aircraft example:

**Request** on `thing/product/{aircraft_sn}/property/set`:

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1643268212187,
  "data": {
    "height_limit": 200
  }
}
```

**Reply** on `thing/product/{aircraft_sn}/property/set_reply`:

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1643268212187,
  "data": {
    "height_limit": {
      "result": 0
    }
  }
}
```

`result` codes per [`mqtt/pilot-to-cloud/property-set/README.md`](../mqtt/pilot-to-cloud/property-set/README.md) — `0` success, `1` failure, `2` timeout, other = refer to [`error-codes/`](../error-codes/) (Phase 8).

For nested writes (e.g., a single watermark field), the request nests the substructure:

```json
{
  "data": {
    "camera_watermark_settings": {
      "user_custom_string": "Patrol 42"
    }
  }
}
```

The reply echoes the nested shape keyed at the same path.

## 7. Source provenance

| Source | Lines | Role |
|---|---|---|
| [`DJI_Cloud/DJI_CloudAPI_Aircraft-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_Aircraft-Properties.txt) | 1,124 | v1.15 primary. Generic pilot-to-cloud aircraft catalog. |
| [`Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/30.others/10.aircraft/00.properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/30.others/10.aircraft/00.properties.md) | — | v1.11.3 cross-check. Same schema. |
| [`Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/10.m3-series/00.properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/10.m3-series/00.properties.md) | — | v1.11.3 M3-series specifically; same schema as generic. |
| [`DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt`](../../DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt) | — | Pilot-to-Cloud envelope shape. Note the OSD struct example in this file is [`OQ-002`](../OPEN-QUESTIONS.md#oq-002--pilot-to-cloud-osd-struct-example-appears-to-be-a-copy-paste-of-the-dock-osd-example) — do not cite it for aircraft OSD content. |

Per-aircraft extension sources are cited in the per-aircraft docs ([`m3d.md`](m3d.md), [`m3td.md`](m3td.md), [`m4d.md`](m4d.md), [`m4td.md`](m4td.md)).
