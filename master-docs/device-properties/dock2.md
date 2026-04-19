# Device Properties — DJI Dock 2

**Gateway role**: Dock gateway (dock serial is `{device_sn}` for the device's own properties and `{gateway_sn}` for the gateway topic family).
**Cohort**: Dock 2 cohort — Dock 2 + M3D + M3TD + RC Pro Enterprise. Paired aircraft properties live on separate topics under the aircraft's serial; see [`m3d.md`](m3d.md) / [`m3td.md`](m3td.md) *(pending Phase 6b)*.

**Sources**:

| File | Version | Authority |
|---|---|---|
| [`DJI_Cloud/DJI_CloudAPI-Dock2-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock2-Properties.txt) | v1.15 | Primary. |
| [`Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/00.properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/00.properties.md) | v1.11.3 | Cross-version verification. |

Dock 2 reports **48 top-level properties** on the dock gateway topic family. 3 are writable via `property/set`. Paired aircraft properties are a separate surface (Phase 6b).

Topic mapping (see Phase 2 [`mqtt/README.md`](../mqtt/README.md) for envelope, and Phase 4 [`mqtt/dock-to-cloud/`](../mqtt/dock-to-cloud/README.md) for envelope examples):

| Topic | Push mode | Carries |
|---|---|---|
| `thing/product/{dock_sn}/osd` | 0 — stable frequency (~0.5 Hz) | OSD properties — §1 below. |
| `thing/product/{dock_sn}/state` | 1 — on-change | State properties — §2 below. |
| `thing/product/{dock_sn}/property/set` | — | Cloud writes one of the 3 settable keys — §3 below. |
| `thing/product/{dock_sn}/property/set_reply` | — | Per-key `result` echo from dock. |

---

## 1. OSD properties — `pushMode: 0`

36 top-level properties push on `thing/product/{dock_sn}/osd` at ~0.5 Hz. Nested struct/array fields follow their top-level parent on the wire; the per-row `pushMode: 0` annotation on nested fields is cosmetic.

| Property | Description | Type | Constraint | Access |
|---|---|---|---|---|
| `home_position_is_valid` | Home position validity | `enum_int` | `{"0":"Invalid","1":"Valid"}` | `r` |
| `heading` | Dock heading angle | `double` | `{"max":"180","min":"-180","unit_name":"Degrees / °"}` | `r` |
| `air_conditioner` | Dock air conditioner working state | `struct` | | `r` |
| `»air_conditioner_state` | Air conditioner state | `enum_int` | `{"0":"Idle","1":"Cooling","2":"Heating","3":"Dehumidification","4":"Cooling exit","5":"Heating exit","6":"Dehumidification exit","7":"Cooling ready","8":"Heating ready","9":"Dehumidification ready"}` — Dock 2 source truncates labels and omits commas between values ≥ 10; see §4 | |
| `»switch_time` | Remaining time until the air conditioner transitions to the next state | `int` | `{"unit_name":"Seconds / s"}` | |
| `drone_battery_maintenance_info` | Aircraft battery maintenance information | `struct` | Reported only while aircraft is powered off in the dock | |
| `»maintenance_state` | Maintenance state | `enum_int` | `{"0":"No maintenance required","1":"Waiting for maintenance","2":"In maintenance"}` | |
| `»maintenance_time_left` | Remaining maintenance time (rounded down) | `int` | `{"unit_name":"Hours / h"}` | |
| `»heat_state` | Battery heating/preservation state | `enum_int` | `{"0":"Not heating","1":"Heating","2":"Heat preservation"}` | |
| `»batteries` | Battery details | `array` of `struct` | Inherits the aircraft battery thing-model shape | |
| `»»capacity_percent` | Remaining battery capacity (%) | `int` | `{"max":100,"min":0}` — `32767` when unavailable | |
| `»»index` | Battery bay | `enum_int` | `{"0":"Left battery","1":"Right battery"}` | |
| `»»voltage` | Voltage | `int` | `{"unit_name":"Millivolts / mV"}` — normal 0–28000, `32767` when unavailable | |
| `»»temperature` | Temperature | `float` | `{"unit_name":"Celsius / °C"}` — one decimal, normal −40 to 150, `32767` when unavailable | |
| `maintain_status` | Dock maintenance history | `struct` | | `r` |
| `»maintain_status_array` | Maintenance entries | `array` of `struct` | | |
| `»»state` | Maintenance state | `enum_int` | `{"0":"No maintenance","1":"With maintenance"}` | |
| `»»last_maintain_type` | Last maintenance type | `enum_int` | `{"0":"No maintenance","17":"Regular maintenance of the dock","18":"Deep maintenance of the dock"}` — Dock 3 rebrands these labels (see §5) | |
| `»»last_maintain_time` | Last maintenance time | `date` | `{"unit_name":"Seconds / s"}` | |
| `»»last_maintain_work_sorties` | Work sorties since last maintenance | `int` | `{"max":"2147483647","min":"0","step":"1"}` | |
| `position_state` | Satellite / RTK fix state | `struct` | | `r` |
| `»is_calibration` | Whether calibrated | `enum_int` | `{"0":"Not calibrated","1":"Calibrated"}` | |
| `»is_fixed` | Fix state | `enum_int` | `{"0":"Not started","1":"Fixing","2":"Fixing successful","3":"Fixing failed"}` | |
| `»quality` | Satellite acquisition mode | `enum_int` | `{"1":"Gear 1","2":"Gear 2","3":"Gear 3","4":"Gear 4","5":"Gear 5","10":"RTK fixed"}` — Dock 3 relabels "Gear" to "Level" | |
| `»gps_number` | Number of GPS satellites | `int` | | |
| `»rtk_number` | Number of RTK satellites | `int` | | |
| `emergency_stop_state` | Emergency stop button state | `enum_int` | `{"0":"Disable","1":"Enable"}` | `r` |
| `drone_charge_state` | Aircraft charging state | `struct` | | `r` |
| `»capacity_percent` | Battery percentage | `int` | `{"max":"100","min":"0"}` | |
| `»state` | Charging state | `enum_int` | `{"0":"Idle","1":"Charging"}` | |
| `backup_battery` | Dock backup battery | `struct` | | `r` |
| `»switch` | Backup battery switch | `enum_int` | `{"0":"Disable","1":"Enable"}` | |
| `»voltage` | Backup battery voltage | `int` | `{"max":"30000","min":"0","unit_name":"Millivolts / mV"}` — `0` when the backup battery is off | |
| `»temperature` | Backup battery temperature | `float` | `{"step":"0.1","unit_name":"Celsius / °C"}` — one decimal | |
| `alarm_state` | Sound + light alarm state | `enum_int` | `{"0":"Disable","1":"Enable"}` | `r` |
| `battery_store_mode` | Aircraft battery charge-retention mode | `enum_int` | `{"1":"Schedule mode","2":"Standby mode"}` — Schedule holds 55–60% when idle (longer battery life); Standby holds 90–95% (faster mission readiness, shorter life) | `r` |
| `activation_time` | Dock activation time | `int` | `{"unit_name":"Seconds / s"}` — Unix epoch | `r` |
| `height` | Dock ellipsoid height | `double` | `{"unit_name":"Meters / m"}` | `r` |
| `alternate_land_point` | Alternate landing point | `struct` | | `r` |
| `»longitude` | Longitude | `float` | | |
| `»latitude` | Latitude | `float` | | |
| `»safe_land_height` | Safe landing / transfer altitude | `float` | | |
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
| `»4g_link_state` | 4G link connection state | `enum_int` | `{"0":"Disconnected","1":"Connected"}` — source extract emits Chinese labels; see §4 | |
| `»sdr_link_state` | SDR link connection state | `enum_int` | `{"0":"Disconnected","1":"Connected"}` — source extract emits Chinese labels; see §4 | |
| `»link_workmode` | Dock video transmission mode | `enum_int` | `{"0":"SDR Mode","1":"4G Fusion Mode"}` | |
| `»sdr_quality` | SDR signal quality | `int` | `{"max":"5","min":"0","step":"1"}` | |
| `»4g_quality` | 4G overall signal quality | `int` | `{"max":"5","min":"0","step":"1"}` | |
| `»4g_uav_quality` | Sky-side 4G quality | `int` | `{"max":"5","min":"0","step":"1"}` — aircraft-to-4G-server | |
| `»4g_gnd_quality` | Ground-side 4G quality | `int` | `{"max":"5","min":"0","step":"1"}` — dock-to-4G-server | |
| `»sdr_freq_band` | SDR frequency band | `float` | | |
| `»4g_freq_band` | 4G frequency band | `float` | | |
| `media_file_detail` | Media upload detail | `struct` | | `r` |
| `»remain_upload` | Pending upload quantity | `int` | | |
| `job_number` | Cumulative dock operations | `int` | `{"unit_name":"Times / count"}` | `r` |
| `drone_in_dock` | Aircraft in/out of dock | `enum_int` | `{"0":"Outside the dock","1":"Inside the dock"}` | `r` |
| `network_state` | Network quality | `struct` | | `r` |
| `»type` | Network type | `enum_int` | `{"1":"4G","2":"Ethernet"}` | |
| `»quality` | Network quality | `enum_int` | `{"0":"No signal","1":"Poor","2":"Poor","3":"Moderate","4":"Better","5":"Good"}` — `"1"` and `"2"` duplicate the same label; see §4 | |
| `»rate` | Network rate | `float` | `{"unit_name":"Kilobytes per second / KB/s"}` | |
| `supplement_light_state` | Supplementary light state | `enum_int` | `{"0":"Disable","1":"On"}` | `r` |
| `cover_state` | Dock cover state | `enum_int` | `{"0":"Disable","1":"On","2":"Half open","3":"Cover state abnormal"}` — labels match Dock 2 source; semantically `"Disable"` = closed and `"On"` = open | `r` |
| `sub_device` | Sub-device (aircraft) state on the dock | `struct` | | `r` |
| `»device_sn` | Aircraft serial | `text` | | |
| `»device_model_key` | Aircraft model key | `text` | format `{domain-type-subtype}` | |
| `»device_online_status` | Aircraft power-on state | `enum_int` | `{"0":"Power off","1":"Power on"}` | |
| `»device_paired` | Aircraft paired with dock | `enum_int` | `{"0":"Not paired","1":"Paired"}` | |
| `flighttask_step_code` | Dock task step state | `enum_int` | `{"0":"Operation preparation","1":"In-flight operation","2":"Post-operation state recovery","3":"Custom flight area updating","4":"Terrain obstacle updating","5":"Mission idle","255":"Aircraft error","256":"Unknown state"}` — source extract leaves `255` as Chinese `飞行器异常`; see §4 | `r` |
| `mode_code` | Dock overall state | `enum_int` | `{"0":"Idle","1":"On-site debugging","2":"Remote debugging","3":"Firmware upgrade in progress","4":"In operation","5":"To be calibrated"}` — v1.11 stopped at `4`; see §5 | `r` |
| `latitude` | Dock latitude | `double` | `{"max":"90","min":"-90","step":"0.01"}` | `r` |
| `longitude` | Dock longitude | `double` | `{"max":"180","min":"-180","step":"0.01"}` | `r` |
| `drc_state` | DRC link state | `enum_int` | `{"0":"Not connected","1":"Connecting","2":"Connected"}` | `r` |

## 2. State properties — `pushMode: 1`

12 top-level properties push on `thing/product/{dock_sn}/state` on change.

| Property | Description | Type | Constraint | Access |
|---|---|---|---|---|
| `rtcm_info` | Dock RTK calibration source | `struct` | | `r` |
| `»mount_point` | Network RTK mount-point | `text` | | |
| `»port` | Network port | `text` | | |
| `»host` | Network host | `text` | | |
| `»rtcm_device_type` | Device type | `enum_int` | `{"1":"Dock"}` | |
| `»source_type` | Calibration type | `enum_int` | `{"0":"Not calibrated","1":"Self convergence calibration","2":"Manual calibration","3":"Network RTK calibration"}` | |
| `wireless_link_topo` | Video transmission topology | `struct` | | `r` |
| `»secret_code` | Encryption code | `array` | `{"size":28,"item_type":int}` | |
| `»center_node` | Aircraft pairing node | `struct` | | |
| `»»sdr_id` | Scrambling code | `int` | | |
| `»»sn` | Aircraft SN | `text` | | |
| `»leaf_nodes` | Dock/RC pairing nodes | `array` of `struct` | | |
| `»»sdr_id` | Scrambling code | `int` | | |
| `»»sn` | Peer SN | `text` | | |
| `»»control_source_index` | Control source index | `int` | `{"max":"2","min":"1","step":"1"}` — controller A/B slot | |
| `air_transfer_enable` | Rapid photo upload during flight | `bool` | `{"false":"Disable","true":"Enable"}` | `rw` |
| `silent_mode` | Dock silent mode | `enum_int` | `{"0":"Non-silent mode","1":"Silent mode"}` — silent mode lowers fan / AC performance and disables buzzer + standby light | `rw` |
| `user_experience_improvement` | UX improvement opt-in | `enum_int` | `{"0":"Initial state","1":"Refuse to join","2":"Agree to join"}` | `rw` |
| `dongle_infos` | 4G dongle inventory | `array` of `struct` | | `r` |
| `»imei` | Dongle IMEI | `text` | Unique per dongle | `r` |
| `»dongle_type` | Dongle type | `enum_int` | `{"6":"Old Dongle","10":"New Dongle with eSIM support"}` | `r` |
| `»eid` | eSIM EID | `text` | Unique per eSIM | `r` |
| `»esim_activate_state` | eSIM activation state | `enum_int` | `{"0":"Unknown","1":"Not activated","2":"Activated"}` — v1.11 had only `{"0":"Not activated","1":"Activated"}`; see §5 | `r` |
| `»sim_card_state` | Physical SIM insertion | `enum_int` | `{"0":"Not inserted","1":"Inserted"}` | `r` |
| `»sim_slot` | Active SIM slot | `enum_int` | `{"0":"Unknown","1":"Physical SIM card","2":"eSIM"}` | `r` |
| `»esim_infos` | eSIM records | `array` of `struct` | | `r` |
| `»»telecom_operator` | Carrier | `enum_int` | `{"0":"Unknown","1":"Mobile","2":"China Unicom","3":"Telecommunications"}` | `r` |
| `»»enabled` | Active eSIM | `bool` | `{"false":"Not in use","true":"In use"}` — only one eSIM active at a time | `r` |
| `»»iccid` | ICCID | `text` | | `r` |
| `»sim_info` | Physical SIM card | `struct` | | `r` |
| `»»telecom_operator` | Carrier | `enum_int` | Same enum as `esim_infos.telecom_operator` | `r` |
| `»»sim_type` | SIM card type | `enum_int` | `{"0":"Unknown","1":"Other regular SIM card","2":"Three-network card"}` | `r` |
| `»»iccid` | ICCID | `text` | | `r` |
| `live_capacity` | Gateway live streaming capability | `struct` | | `r` |
| `»available_video_number` | Selectable bitrates | `int` | | |
| `»coexist_video_number_max` | Max simultaneous streams | `int` | | |
| `»device_list` | Selectable video sources | `array` of `struct` | Per aircraft | |
| `»»sn` | Aircraft SN | `text` | | |
| `»»available_video_number` | Per-aircraft selectable bitrates | `int` | | |
| `»»coexist_video_number_max` | Per-aircraft max simultaneous | `int` | | |
| `»»camera_list` | Cameras on the aircraft | `array` of `struct` | | |
| `»»»camera_index` | Camera index | `text` | format `{type-subtype-gimbalindex}` | |
| `»»»available_video_number` | Per-camera selectable bitrates | `int` | | |
| `»»»coexist_video_number_max` | Per-camera max simultaneous | `int` | | |
| `»»»video_list` | Selectable streams | `array` of `struct` | | |
| `»»»»video_index` | Stream index | `text` | | |
| `»»»»video_type` | Stream type | `text` | normal / wide / zoom / infrared etc. | |
| `»»»»switchable_video_types` | Other types this stream can switch to | `array` of `text` | | |
| `live_status` | Per-stream live state | `array` of `struct` | | `r` |
| `»video_id` | Stream identifier | `text` | format `{sn}/{camera_index}/{video_index}` | |
| `»video_type` | Video lens type | `text` | `{"length":"24"}` | |
| `»video_quality` | Live quality | `enum_int` | `{"0":"Adaptive","1":"Smooth","2":"Standard definition","3":"High definition","4":"Ultra-high definition"}` | |
| `»status` | Streaming state | `enum_int` | `{"0":"Not live streaming","1":"In live streaming"}` | |
| `»error_status` | Error code | `int` | `{"length":6}` | |
| `compatible_status` | Consistency upgrade required | `enum_int` | `{"0":"No consistency upgrade required","1":"Consistency upgrade required"}` | `r` |
| `acc_time` | Cumulative operating seconds | `int` | `{"unit_name":"Seconds / s"}` | `r` |
| `firmware_upgrade_status` | Firmware update state | `enum_int` | `{"0":"Not upgraded","1":"Upgrading"}` | `r` |
| `firmware_version` | Dock firmware version | `text` | `{"length":"64"}` | `r` |

## 3. Settable via `property/set` — `accessMode: rw`

Dock 2 exposes **3 writable gateway properties** via `thing/product/{dock_sn}/property/set`. All three ride `state` for their push side, so a successful set is confirmed by both a `property/set_reply` (per-key `result`) and a subsequent on-change push of the new value.

| Property | Push mode | Value domain | Notes |
|---|---|---|---|
| `air_transfer_enable` | state | `bool {false, true}` | Labels `"Disable" / "Enable"`. Rapid photo upload to cloud during a commanded flight. |
| `silent_mode` | state | `enum_int {0: Non-silent, 1: Silent}` | Silent mode reduces fan speed, AC performance, and operation intervals in hot weather; disables buzzer and standby-light indicator. |
| `user_experience_improvement` | state | `enum_int {0: Initial, 1: Refuse, 2: Agree}` | Initial = user has not yet been asked. |

A set request batches multiple keys; the reply carries per-key `result` codes (`0` success, `1` fail, `2` timeout, other = error-code reference, pending [`error-codes/`](../error-codes/) in Phase 8). Envelope per [`mqtt/dock-to-cloud/property-set/README.md`](../mqtt/dock-to-cloud/property-set/README.md).

Other dock controls that a cloud operator might expect to be writable (alarm, cover, supplement light, AC mode, battery store mode, night lights) are exposed via **services** (`alarm_state_switch`, `cover_open` / `cover_close`, `supplement_light_open` / `supplement_light_close`, `air_conditioner_mode_switch`, `battery_store_mode_switch`, etc.) in [`mqtt/dock-to-cloud/services/`](../mqtt/dock-to-cloud/services/), not via property-set. Phase 9 workflows surface the service-vs-property-set decision per operation.

## 4. DJI-source inconsistencies (flagged, not escalated)

Each is a known defect in the DJI source material that the corpus works around. Docs below (and per-property notes above) give the corrected value; the cloud implementation should honour the corrected value.

1. **`air_conditioner.air_conditioner_state` enum is malformed for values ≥ 10.** The DJI source reads `"9":"Dehumidification ready mode"10":"Preparing for air cooling"11":"Air cooling in progress"...` — missing commas and missing quotes around the keys `10`–`15`. The v1.11 canonical has only values `0`–`9`. Cloud implementations should accept both forms: the 10-value v1.11 enum (which is what Dock 2 firmware currently reports in practice) and the extended form captured in the v1.15 extract.

2. **`wireless_link.4g_link_state` and `wireless_link.sdr_link_state` ship Chinese labels.** Source: `{"0":"断开","1":"连接"}`. Translation: `"Disconnected"` / `"Connected"`. The Dock 3 v1.15 source emits the English labels, so this is a Dock 2 extract-level defect (v1.11 has the same Chinese leftover).

3. **`network_state.quality` has duplicate labels for `"1"` and `"2"`**: both read `"Poor"`. Dock 3 v1.15 reads `"1":"Very Poor","2":"Poor","3":"Fair","4":"Good","5":"Excellent"` — clearly the correct label set. Cloud implementations should treat `1` as "Very Poor" and `2` as "Poor" regardless of source label.

4. **`flighttask_step_code` value `"255"` ships Chinese label `飞行器异常`.** Translation: `"Aircraft error"`. The surrounding values (0–5 and 256) are in English. Same pattern in v1.11 and v1.15 — uniform extract defect.

5. **Example payload in the Dock 2 source contains `putter_state` which is not listed in the property catalog.** Both v1.11 and v1.15 examples (lines 276–306 of v1.11, lines 249–306 of v1.15 extract) emit `"putter_state": 0`. The property-list table does not mention `putter_state` at all. This is either a list omission or a deprecated field still emitted by firmware. Treat as undocumented — cloud implementations should accept the key without failing but should not rely on its presence.

6. **`drone_battery_maintenance_info` is listed without `accessMode`** in both v1.11 and v1.15 Dock 2. All other read-only structs use `r`. Default convention: treat it as `r`.

None of these rise to [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) level — they are all doc-level bugs in DJI's source material, with the corrected value either obvious from context or confirmable against Dock 3 v1.15 which has them fixed.

## 5. v1.11 → v1.15 drift

Resolution policy: prefer v1.15 when the two disagree. Drift below is **all cosmetic or enum-extension** — no type changes, no semantic-value changes.

| Property | v1.11 Dock 2 | v1.15 Dock 2 | Classification |
|---|---|---|---|
| `mode_code` | `{0..4}` (missing `5`) | `{0..5}` adds `"5":"To be calibrated"` | Enum extension; new value. |
| `dongle_infos.esim_activate_state` | `{"0":"Not activated","1":"Activated"}` | `{"0":"Unknown","1":"Not activated","2":"Activated"}` | Enum extension; `"0"` reassigned. Cloud implementations reading v1.15 firmware must handle the 3-value form. |
| `maintain_status.last_maintain_type` labels | unchanged between v1.11 and v1.15 Dock 2 (`"Regular maintenance of the dock"`, `"Deep maintenance of the dock"`) | unchanged | Dock 3 rebrands to `"Dock Standard Service"` / `"Dock Premium Service"` — cross-device delta, not version-drift. |
| other enum labels | mostly unchanged | `air_conditioner_state` expanded (see §4.1) | Cosmetic / extract defect. |

No semantic drift escalations. [`OQ-001`](../OPEN-QUESTIONS.md#oq-001--source-version-mismatch-between-cloud-api-doc-v1113-and-dji_cloud-v115) policy applies.

## 6. Property Set — request / reply

Same envelope as documented in [`mqtt/dock-to-cloud/property-set/README.md`](../mqtt/dock-to-cloud/property-set/README.md). Example for Dock 2:

**Request** on `thing/product/{dock_sn}/property/set`, direction `down`:

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1643268212187,
  "data": {
    "silent_mode": 1
  }
}
```

**Reply** on `thing/product/{dock_sn}/property/set_reply`, direction `up`:

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1643268212187,
  "data": {
    "silent_mode": {
      "result": 0
    }
  }
}
```

`result` codes per [`mqtt/dock-to-cloud/property-set/README.md`](../mqtt/dock-to-cloud/property-set/README.md) §Envelope — set reply: `0` success, `1` fail, `2` time exceed, other = refer to [`error-codes/`](../error-codes/) (Phase 8).

## 7. Source provenance

| Source | Lines | Role |
|---|---|---|
| [`DJI_Cloud/DJI_CloudAPI-Dock2-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock2-Properties.txt) | 471 | v1.15 primary. Property table + OSD/state example + property-set example. |
| [`Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/00.properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/00.properties.md) | 492 | v1.11.3 canonical. Cross-checked for drift. |
| [`DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt`](../../DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt) | — | Dock-to-Cloud envelope shape (cross-referenced from Phase 2 [`mqtt/README.md`](../mqtt/README.md)). |
