# Device Properties — DJI Dock 3

**Gateway role**: Dock gateway (dock serial is `{device_sn}` for the device's own properties and `{gateway_sn}` for the gateway topic family).
**Cohort**: Dock 3 cohort — Dock 3 + M4D + M4TD + RC Plus 2 Enterprise. Paired aircraft properties live on separate topics under the aircraft's serial; see [`m4d.md`](m4d.md) / [`m4td.md`](m4td.md) *(pending Phase 6b)*.

**Sources**:

| File | Version | Authority |
|---|---|---|
| [`DJI_Cloud/DJI_CloudAPI-Dock3-DeviceProperties.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock3-DeviceProperties.txt) | v1.15 | Primary. |
| — | — | Dock 3 postdates v1.11; no v1.11 canonical counterpart exists. |

Dock 3 reports **49 top-level properties** on the dock gateway topic family. 3 are writable via `property/set`. Dock 3's property surface is a superset of Dock 2 — every Dock 2 property is present on Dock 3, plus `self_converge_coordinate`. Enum labels are often refined (better English, corrected typos).

Topic mapping (see Phase 2 [`mqtt/README.md`](../mqtt/README.md) for envelope):

| Topic | Push mode | Carries |
|---|---|---|
| `thing/product/{dock_sn}/osd` | 0 — stable frequency (~0.5 Hz) | OSD properties — §1 below. |
| `thing/product/{dock_sn}/state` | 1 — on-change | State properties — §2 below. |
| `thing/product/{dock_sn}/property/set` | — | Cloud writes one of the 3 settable keys — §3 below. |
| `thing/product/{dock_sn}/property/set_reply` | — | Per-key `result` echo from dock. |

Cross-reference: for the Dock 2 sibling (older generation), see [`dock2.md`](dock2.md). Most enum-label changes in Dock 3 are rewording with identical semantics; see §5 for the full delta vs Dock 2.

---

## 1. OSD properties — `pushMode: 0`

37 top-level properties push on `thing/product/{dock_sn}/osd` at ~0.5 Hz.

| Property | Description | Type | Constraint | Access |
|---|---|---|---|---|
| `home_position_is_valid` | Home point validity | `enum_int` | `{"0":"Both heading and lat/lon invalid","1":"Both valid","2":"Heading valid, lat/lon invalid","3":"Lat/lon valid, heading invalid"}` — Dock 3 expands from Dock 2's 2-value enum; lets the cloud distinguish partial-calibration states. Pre-calibration, lat/lon fluctuate and should not be used | `r` |
| `heading` | Dock heading angle | `double` | `{"max":"180","min":"-180","unit_name":"Degrees / °"}` | `r` |
| `air_conditioner` | Dock air conditioner working state | `struct` | | `r` |
| `»air_conditioner_state` | Air conditioner state | `enum_int` | `{"0":"Idle","1":"Cooling","2":"Heating","3":"Dehumidification","4":"Cooling exit","5":"Heating exit","6":"Dehumidification exit","7":"Cooling ready","8":"Heating ready","9":"Dehumidification ready"}` — source malformation identical to Dock 2; see §4 | |
| `»switch_time` | Remaining time until the air conditioner transitions to the next state | `int` | `{"unit_name":"Second / s"}` | |
| `drone_battery_maintenance_info` | Aircraft battery maintenance (aircraft powered off in dock) | `struct` | | `r` |
| `»maintenance_state` | Maintenance state | `enum_int` | `{"0":"No maintenance required","1":"Waiting for maintenance","2":"In maintenance"}` | |
| `»maintenance_time_left` | Remaining maintenance time (rounded down) | `int` | `{"unit_name":"Hours / h"}` | |
| `»heat_state` | Battery heating/insulation state | `enum_int` | `{"0":"Heating/insulation not activated","1":"Heating","2":"Insulating"}` | |
| `»batteries` | Battery details | `array` of `struct` | | |
| `»»capacity_percent` | Remaining battery capacity (%) | `int` | `{"max":100}` — range 0.0–100.0, one decimal, `32767` when unavailable | |
| `»»index` | Battery bay | `enum_int` | `{"0":"Left battery","1":"Right battery"}` | |
| `»»voltage` | Voltage | `int` | `{"unit_name":"Millivolts / mV"}` — range 0–28000, `32767` when unavailable | |
| `»»temperature` | Temperature | `float` | `{"unit_name":"Celsius / °C"}` — one decimal, range −40.0 to 150.0, `32767` when unavailable | |
| `maintain_status` | Dock maintenance history | `struct` | | `r` |
| `»maintain_status_array` | Maintenance entries | `array` of `struct` | | |
| `»»state` | Maintenance state | `enum_int` | `{"0":"No maintenance","1":"Maintained"}` | |
| `»»last_maintain_type` | Last maintenance type | `enum_int` | `{"0":"No Maintenance","17":"Dock Standard Service","18":"Dock Premium Service"}` — Dock 3 rebrands from Dock 2's `"Regular maintenance of the dock"` / `"Deep maintenance of the dock"`; same codes | |
| `»»last_maintain_time` | Last maintenance time | `date` | `{"unit_name":"Seconds / s"}` | |
| `»»last_maintain_work_sorties` | Flights since last maintenance | `int` | `{"max":"2147483647","min":"0","step":"1"}` | |
| `position_state` | Satellite / RTK fix state | `struct` | | `r` |
| `»is_calibration` | Whether calibrated | `enum_int` | `{"0":"Not calibrated","1":"Calibrated"}` | |
| `»is_fixed` | Fix state | `enum_int` | `{"0":"Not started","1":"Fixing","2":"Fixing successful","3":"Fixing failed"}` | |
| `»quality` | Signal quality level | `enum_int` | `{"1":"Level 1","2":"Level 2","3":"Level 3","4":"Level 4","5":"Level 5","10":"RTK Fix"}` — Dock 3 relabels from Dock 2's `"Gear 1"` .. `"Gear 5"`, `"RTK fixed"` | |
| `»gps_number` | Number of GPS satellites | `int` | | |
| `»rtk_number` | Number of RTK satellites | `int` | | |
| `emergency_stop_state` | Emergency stop button state | `enum_int` | `{"0":"Released","1":"Pressed Down"}` — Dock 3 relabels from Dock 2's `"Disable" / "Enable"`; same codes | `r` |
| `drone_charge_state` | Aircraft charging state | `struct` | | `r` |
| `»capacity_percent` | Battery percentage | `int` | `{"max":"100","min":"0"}` | |
| `»state` | Charging state | `enum_int` | `{"0":"Idle","1":"Charging"}` | |
| `backup_battery` | Dock backup battery | `struct` | | `r` |
| `»switch` | Backup battery switch | `enum_int` | `{"0":"Disabled","1":"Enabled"}` | |
| `»voltage` | Backup battery voltage | `int` | `{"max":"30,000","min":"0","unit_name":"Millivolts / mV"}` — `0` when the backup battery is off | |
| `»temperature` | Backup battery temperature | `float` | `{"step":"0.1","unit_name":"Celsius / °C"}` — one decimal | |
| `alarm_state` | Sound + light alarm state | `enum_int` | `{"0":"Disabled","1":"Enabled"}` | `r` |
| `battery_store_mode` | Aircraft battery charge-retention mode | `enum_int` | `{"1":"Schedule mode","2":"Standby mode"}` | `r` |
| `activation_time` | Dock activation time | `int` | `{"unit_name":"Seconds / s"}` — Unix epoch | `r` |
| `height` | Dock ellipsoid height | `double` | `{"unit_name":"Meters / m"}` | `r` |
| `alternate_land_point` | Alternate landing site | `struct` | | `r` |
| `»longitude` | Longitude | `float` | | |
| `»latitude` | Latitude | `float` | | |
| `»safe_land_height` | Safe altitude (alternate route) | `float` | | |
| `»is_configured` | Configured | `enum_int` | `{"0":"Not set","1":"Already set"}` | |
| `»height` | Ellipsoid height | `float` | | |
| `first_power_on` | First power-on time | `int` | `{"unit_name":"Milliseconds / ms"}` | `r` |
| `storage` | Dock storage capacity | `struct` | | `r` |
| `»total` | Total capacity | `int` | `{"unit_name":"Kilobytes / KB"}` | |
| `»used` | Used capacity | `int` | `{"unit_name":"Kilobytes / KB"}` | |
| `working_current` | Dock working current | `float` | `{"unit_name":"Milliamps / mA"}` | `r` |
| `working_voltage` | Dock working voltage | `int` | `{"unit_name":"Millivolts / mV"}` | `r` |
| `humidity` | Humidity inside the dock | `float` | `{"max":"100","min":"0","step":"0.1","unit_name":"%RH"}` | `r` |
| `temperature` | Temperature inside the dock | `float` | `{"unit_name":"Celsius / °C"}` | `r` |
| `environment_temperature` | Ambient temperature outside | `float` | `{"unit_name":"Celsius / °C"}` | `r` |
| `wind_speed` | Wind speed | `float` | `{"unit_name":"Meters per second / m/s"}` | `r` |
| `rainfall` | Rainfall level | `enum_int` | `{"0":"No rain","1":"Light rain","2":"Moderate rain","3":"Heavy rain"}` | `r` |
| `wireless_link` | Video transmission link status | `struct` | | `r` |
| `»dongle_number` | Number of dongles on the aircraft | `int` | | |
| `»4g_link_state` | 4G link connection state | `enum_int` | `{"0":"Disconnected","1":"Connected"}` — Dock 3 emits English (Dock 2 source ships Chinese — see Dock 2 §4) | |
| `»sdr_link_state` | SDR link connection state | `enum_int` | `{"0":"Disconnected","1":"Connected"}` | |
| `»link_workmode` | Dock video transmission mode | `enum_int` | `{"0":"SDR Mode","1":"4G Fusion Mode"}` | |
| `»sdr_quality` | SDR signal quality | `int` | `{"max":"5","min":"0","step":"1"}` | |
| `»4g_quality` | 4G overall signal quality | `int` | `{"max":"5","min":"0","step":"1"}` | |
| `»4g_uav_quality` | Sky-end 4G quality | `int` | `{"max":"5","min":"0","step":"1"}` — aircraft-to-4G-server | |
| `»4g_gnd_quality` | Ground-end 4G quality | `int` | `{"max":"5","min":"0","step":"1"}` — dock-to-4G-server | |
| `»sdr_freq_band` | SDR frequency band | `float` | | |
| `»4g_freq_band` | 4G frequency band | `float` | | |
| `media_file_detail` | Media upload detail | `struct` | | `r` |
| `»remain_upload` | Pending upload count | `int` | | |
| `job_number` | Cumulative dock operations | `int` | `{"unit_name":"Times / count"}` | `r` |
| `drone_in_dock` | Aircraft in/out of dock | `enum_int` | `{"0":"Outside the dock","1":"Inside the dock"}` | `r` |
| `network_state` | Network quality | `struct` | | `r` |
| `»type` | Network type | `enum_int` | `{"1":"4G","2":"Ethernet"}` | |
| `»quality` | Network quality | `enum_int` | `{"0":"No signal","1":"Very Poor","2":"Poor","3":"Fair","4":"Good","5":"Excellent"}` — Dock 3 fixes Dock 2's duplicate `"Poor"` labels | |
| `»rate` | Network rate | `float` | `{"unit_name":"Kilobytes per second / KB/s"}` | |
| `supplement_light_state` | Auxiliary light state | `enum_int` | `{"0":"Disabled","1":"Enabled"}` | `r` |
| `cover_state` | Dock cover state | `enum_int` | `{"0":"Closed","1":"Open","2":"Half open","3":"Cover state abnormal"}` — Dock 3 relabels Dock 2's `"Disable" / "On"` to `"Closed" / "Open"` | `r` |
| `sub_device` | Sub-device (aircraft) state on the dock | `struct` | | `r` |
| `»device_sn` | Aircraft serial | `text` | | |
| `»device_model_key` | Aircraft model key | `text` | format `{domain-type-subtype}` | |
| `»device_online_status` | Aircraft power-on state | `enum_int` | `{"0":"Powered off","1":"Powered on"}` — Dock 3 minor relabel | |
| `»device_paired` | Aircraft paired with dock | `enum_int` | `{"0":"Not paired","1":"Paired"}` | |
| `flighttask_step_code` | Dock task-step state | `enum_int` | `{"0":"Task Preparation","1":"Task in Progress","2":"Status Recovery After Task","3":"Updating Custom Flight Area","4":"Updating Obstacle Data","5":"Idle","255":"Aircraft Error","256":"Unknown Status"}` — Dock 3 emits English for value `255` (Dock 2 source ships Chinese) | `r` |
| `mode_code` | Dock overall state | `enum_int` | `{"0":"Idle","1":"On-site debugging","2":"Remote debugging","3":"Firmware update in progress","4":"Task in progress","5":"To be calibrated"}` | `r` |
| `latitude` | Dock latitude | `double` | `{"max":"90","min":"-90","step":"0.01"}` | `r` |
| `longitude` | Dock longitude | `double` | `{"max":"180","min":"-180","step":"0.01"}` | `r` |
| `drc_state` | DRC link state | `enum_int` | `{"0":"Not connected","1":"Connecting","2":"Connected"}` | `r` |
| `self_converge_coordinate` | Self-convergence calibration coordinates | `struct` | **Dock 3 only** — absent from Dock 2 | `r` |
| `»latitude` | Self-convergence latitude | `double` | `{"max":"90","min":"-90","step":"0.01"}` | `r` |
| `»longitude` | Self-convergence longitude | `double` | `{"max":"180","min":"-180","step":"0.01"}` | `r` |
| `»height` | Self-convergence ellipsoid height | `double` | `{"unit_name":"Meters / m"}` | `r` |

## 2. State properties — `pushMode: 1`

12 top-level properties push on `thing/product/{dock_sn}/state` on change. Identical to Dock 2 at the surface level; enum-label refinements mirror the OSD table.

| Property | Description | Type | Constraint | Access |
|---|---|---|---|---|
| `rtcm_info` | Dock RTK calibration source | `struct` | | `r` |
| `»mount_point` | Network RTK mount-point | `text` | | |
| `»port` | Network port | `text` | | |
| `»host` | Network host | `text` | | |
| `»rtcm_device_type` | Device type | `enum_int` | `{"1":"Dock"}` | |
| `»source_type` | Calibration type | `enum_int` | `{"0":"Not calibrated","1":"Auto-convergence calibration","2":"Manual calibration","3":"Network RTK calibration"}` — Dock 3 relabels `"Self convergence calibration"` → `"Auto-convergence calibration"` | |
| `wireless_link_topo` | Wireless link topology | `struct` | | `r` |
| `»secret_code` | Encryption code | `array` | `{"size":28,"item_type":int}` | |
| `»center_node` | Aircraft frequency info | `struct` | | |
| `»»sdr_id` | Scrambling code | `int` | | |
| `»»sn` | Aircraft SN | `text` | | |
| `»leaf_nodes` | Dock/RC pairing nodes | `array` of `struct` | | |
| `»»sdr_id` | Scrambling code | `int` | | |
| `»»sn` | Peer SN | `text` | | |
| `»»control_source_index` | Control source number | `int` | `{"max":"2","min":"1","step":"1"}` | |
| `air_transfer_enable` | Rapid photo upload during flight | `bool` | `{"false":"Disable","true":"Enable"}` — Dock 3 wording extends to FlyTo tasks, and the latest Dock 3 firmware also supports Wayline tasks | `rw` |
| `silent_mode` | Dock silent mode | `enum_int` | `{"0":"Non-silent mode","1":"Silent mode"}` | `rw` |
| `user_experience_improvement` | UX improvement opt-in | `enum_int` | `{"0":"Initial state","1":"Refuse to join","2":"Agree to join"}` | `rw` |
| `dongle_infos` | 4G dongle inventory | `array` of `struct` | | `r` |
| `»imei` | Dongle IMEI | `text` | Unique per dongle | `r` |
| `»dongle_type` | Dongle type | `enum_int` | `{"6":"Old dongle","10":"New dongle with eSIM support"}` | `r` |
| `»eid` | eSIM EID | `text` | | `r` |
| `»esim_activate_state` | eSIM activation state | `enum_int` | `{"0":"Unknown","1":"Not activated","2":"Activated"}` | `r` |
| `»sim_card_state` | Physical SIM insertion | `enum_int` | `{"0":"Not inserted","1":"Inserted"}` | `r` |
| `»sim_slot` | Active SIM slot | `enum_int` | `{"0":"Unknown","1":"Physical SIM card","2":"eSIM"}` | `r` |
| `»esim_infos` | eSIM records | `array` of `struct` | | `r` |
| `»»telecom_operator` | Carrier | `enum_int` | `{"0":"Unknown","1":"China Mobile","2":"China Unicom","3":"China Telecom"}` — Dock 3 fully-qualifies carrier names (Dock 2 shows `"Mobile"` / `"Telecommunications"`) | `r` |
| `»»enabled` | Active eSIM | `bool` | `{"false":"Not in use","true":"In use"}` | `r` |
| `»»iccid` | ICCID | `text` | | `r` |
| `»sim_info` | Physical SIM card | `struct` | | `r` |
| `»»telecom_operator` | Carrier | `enum_int` | Inherited — same enum as `esim_infos.telecom_operator` in the source extract but `sim_info.telecom_operator` reverts to the Dock 2 short labels (`"Mobile"`, `"Telecommunications"`) — see §4 | `r` |
| `»»sim_type` | SIM card type | `enum_int` | `{"0":"Unknown","1":"Other regular SIM card","2":"Three-network card"}` | `r` |
| `»»iccid` | ICCID | `text` | | `r` |
| `live_capacity` | Gateway live streaming capability | `struct` | | `r` |
| `»available_video_number` | Selectable stream count | `int` | | |
| `»coexist_video_number_max` | Max simultaneous streams | `int` | | |
| `»device_list` | Selectable video sources | `array` of `struct` | | |
| `»»sn` | Aircraft SN | `text` | | |
| `»»available_video_number` | Per-aircraft selectable streams | `int` | | |
| `»»coexist_video_number_max` | Per-aircraft max simultaneous | `int` | | |
| `»»camera_list` | Cameras | `array` of `struct` | | |
| `»»»camera_index` | Camera index | `text` | format `{type-subtype-gimbalindex}` | |
| `»»»available_video_number` | Per-camera selectable streams | `int` | | |
| `»»»coexist_video_number_max` | Per-camera max simultaneous | `int` | | |
| `»»»video_list` | Selectable streams | `array` of `struct` | | |
| `»»»»video_index` | Stream index | `text` | | |
| `»»»»video_type` | Stream type | `text` | normal / wide / zoom / infrared etc. | |
| `»»»»switchable_video_types` | Switchable stream types | `array` of `text` | | |
| `live_status` | Per-stream live state | `array` of `struct` | | `r` |
| `»video_id` | Stream identifier | `text` | format `{sn}/{camera_index}/{video_index}` | |
| `»video_type` | Video lens type | `text` | `{"length":"24"}` | |
| `»video_quality` | Live quality | `enum_int` | `{"0":"Adaptive","1":"Smooth","2":"Standard definition","3":"High definition","4":"Ultra-high definition"}` | |
| `»status` | Streaming state | `enum_int` | `{"0":"Not livestreaming","1":"Livestreaming"}` — Dock 3 wording trim ("Not live streaming"/"In live streaming" → "Not livestreaming"/"Livestreaming") | |
| `»error_status` | Error code | `int` | `{"length":6}` | |
| `compatible_status` | Consistency update required | `enum_int` | `{"0":"No consistency update required","1":"Consistency update required"}` — Dock 3 uses `"update"` where Dock 2 said `"upgrade"`; semantics identical | `r` |
| `acc_time` | Dock total running seconds | `int` | `{"unit_name":"Seconds / s"}` | `r` |
| `firmware_upgrade_status` | Firmware update state | `enum_int` | `{"0":"Not updated","1":"Updating"}` — Dock 3 uses `"update"`; Dock 2 says `"upgraded"` / `"Upgrading"` | `r` |
| `firmware_version` | Dock firmware version | `text` | `{"length":"64"}` | `r` |

## 3. Settable via `property/set` — `accessMode: rw`

Same 3 writable gateway properties as Dock 2. No new Dock-3-specific writable property was added at the gateway level.

| Property | Push mode | Value domain | Notes |
|---|---|---|---|
| `air_transfer_enable` | state | `bool {false, true}` | Dock 3 extends behaviour to FlyTo and Wayline tasks (Dock 2 documented only commanded-flight scope). |
| `silent_mode` | state | `enum_int {0: Non-silent, 1: Silent}` | |
| `user_experience_improvement` | state | `enum_int {0: Initial, 1: Refuse, 2: Agree}` | |

Other dock controls (alarm, cover, supplement light, AC mode, battery store mode, night lights, debug mode, RTK calibration) are exposed via **services** under [`mqtt/dock-to-cloud/services/`](../mqtt/dock-to-cloud/services/). In particular, Dock 3 adds `rtk_calibration` (Phase 4e-1, `need_reply: 1`) which has no Dock 2 counterpart.

## 4. DJI-source inconsistencies (flagged, not escalated)

1. **`air_conditioner.air_conditioner_state` source malformation** — same as Dock 2: the v1.15 extract lists values `10`–`15` (`"Preparing for air cooling"` through `"Defogger exiting"`) but the source omits commas and quote-delimiters. The machine-readable enum contains values `0`–`9`; values `10`+ are extract-level defects with no clean parse. Treat the `0`–`9` set as authoritative.

2. **`sim_info.telecom_operator` enum disagrees with `esim_infos.telecom_operator` in the same file.** Dock 3 source uses `"China Mobile"` / `"China Unicom"` / `"China Telecom"` for `esim_infos.telecom_operator` but reverts to Dock-2-style `"Mobile"` / `"China Unicom"` / `"Telecommunications"` for `sim_info.telecom_operator`. Clearly a copy-paste lag in the source — the enum codes are identical; cloud implementations should treat `{1, 2, 3}` as China Mobile / China Unicom / China Telecom regardless of label variant.

3. **Example payload contains three fields not in the property list:**
   - `electric_supply_voltage: 231` (line ~195 of the Dock 3 extract) — appears in the first example block, suggesting a dock-level AC input-voltage reading.
   - `flighttask_prepare_capacity: 1` (second example block) — appears to indicate mission-preparation readiness.
   - `air_conditioner_mode: 0` (third example block) — scalar value not in the list, which instead carries `air_conditioner` as a **struct** with `air_conditioner_state` and `switch_time`.

   These are either list-omission defects or deprecated fields still emitted by firmware. Cloud implementations should accept the keys without failing; do not treat their presence as authoritative. Neither `electric_supply_voltage` nor `flighttask_prepare_capacity` has a documented type.

4. **`putter_state` does not appear in Dock 3 source examples** (it does appear in both v1.11 and v1.15 Dock 2 examples), suggesting DJI removed or renamed it. Cloud implementations should tolerate both presence and absence.

5. **Blank lines and irregular whitespace in the v1.15 extract** (lines ~210–244 of the extract are blank before resuming the second example) — extraction-tool artifact of the MHTML-to-text conversion, not a protocol fact.

None rise to [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) level.

## 5. Drift vs Dock 2

Dock 3 is a **property superset** of Dock 2 at the gateway level. Dock 3 adds `self_converge_coordinate` (3 nested fields) and refines enum labels widely. No property present on Dock 2 is absent from Dock 3. Semantic changes are confined to:

| Property | Dock 2 | Dock 3 | Classification |
|---|---|---|---|
| `home_position_is_valid` | `enum_int {0: Invalid, 1: Valid}` | `enum_int {0: Both invalid, 1: Both valid, 2: Heading valid lat/lon invalid, 3: Lat/lon valid heading invalid}` | **Enum extension** — the 4-value enum is upward-compatible (`0`, `1` values retained), adds richer partial-state semantics. Cloud implementations targeting both docks must handle the 4-value form. |
| `position_state.quality` labels | `"Gear 1"` .. `"Gear 5"`, `"RTK fixed"` | `"Level 1"` .. `"Level 5"`, `"RTK Fix"` | Cosmetic relabel. |
| `maintain_status.»»last_maintain_type` | `"Regular maintenance of the dock"`, `"Deep maintenance of the dock"` | `"Dock Standard Service"`, `"Dock Premium Service"` | Cosmetic relabel. |
| `emergency_stop_state` labels | `{0: Disable, 1: Enable}` | `{0: Released, 1: Pressed Down}` | Cosmetic relabel; Dock 3's labels match the real-world semantics. |
| `cover_state` labels | `{0: Disable, 1: On, 2: Half open, 3: Cover state abnormal}` | `{0: Closed, 1: Open, 2: Half open, 3: Cover state abnormal}` | Cosmetic relabel. |
| `alarm_state` labels | `{0: Disable, 1: Enable}` | `{0: Disabled, 1: Enabled}` | Cosmetic. |
| `supplement_light_state` labels | `{0: Disable, 1: On}` | `{0: Disabled, 1: Enabled}` | Cosmetic. |
| `sub_device.device_online_status` | `{0: Power off, 1: Power on}` | `{0: Powered off, 1: Powered on}` | Cosmetic. |
| `wireless_link.4g_link_state / sdr_link_state` | `{0: 断开, 1: 连接}` (Chinese — extract bug) | `{0: Disconnected, 1: Connected}` | Dock 3 ships the correct English labels; Dock 2 source extract has a known extraction defect. |
| `network_state.quality` | `{0: No signal, 1: Poor, 2: Poor, 3: Moderate, 4: Better, 5: Good}` (duplicate label bug) | `{0: No signal, 1: Very Poor, 2: Poor, 3: Fair, 4: Good, 5: Excellent}` | Dock 3 fixes the Dock 2 source defect. |
| `flighttask_step_code` value `255` | `"飞行器异常"` (Chinese — extract bug) | `"Aircraft Error"` | Dock 3 ships the correct English. |
| `rtcm_info.source_type` value `1` | `"Self convergence calibration"` | `"Auto-convergence calibration"` | Cosmetic. |
| `dongle_infos.»esim_infos.telecom_operator` labels | `{0: Unknown, 1: Mobile, 2: China Unicom, 3: Telecommunications}` | `{0: Unknown, 1: China Mobile, 2: China Unicom, 3: China Telecom}` | Cosmetic; fully-qualifies carrier names. |
| `compatible_status` + `firmware_upgrade_status` labels | "upgrade" wording | "update" wording | Cosmetic. |
| new — `self_converge_coordinate` | absent | `struct {latitude, longitude, height}` | **New property** — Dock 3 adds this to expose the self-convergence calibration result. |

No cohort escalations. Dock 3 drift is enum-extension (`home_position_is_valid`) + new property (`self_converge_coordinate`) + cosmetic everywhere else.

## 6. Property Set — request / reply

Same envelope as [`mqtt/dock-to-cloud/property-set/README.md`](../mqtt/dock-to-cloud/property-set/README.md). Dock 3 example:

**Request** on `thing/product/{dock_sn}/property/set`:

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1643268212187,
  "data": {
    "air_transfer_enable": true
  }
}
```

**Reply** on `thing/product/{dock_sn}/property/set_reply`:

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1643268212187,
  "data": {
    "air_transfer_enable": {
      "result": 0
    }
  }
}
```

`result` codes per [`mqtt/dock-to-cloud/property-set/README.md`](../mqtt/dock-to-cloud/property-set/README.md) §Envelope — set reply: `0` success, `1` failure, `2` timeout, other = refer to [`error-codes/`](../error-codes/) (Phase 8).

## 7. Source provenance

| Source | Lines | Role |
|---|---|---|
| [`DJI_Cloud/DJI_CloudAPI-Dock3-DeviceProperties.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock3-DeviceProperties.txt) | 680 | v1.15 primary. Property table + OSD/state example + property-set example. |
| [`DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt`](../../DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt) | — | Dock-to-Cloud envelope shape (cross-referenced from Phase 2 [`mqtt/README.md`](../mqtt/README.md)). |
| [`dock2.md`](dock2.md) | — | Cross-cohort sibling; §5 drift table references Dock 2 values verbatim. |

No v1.11 canonical counterpart exists (Dock 3 postdates v1.11.3).
