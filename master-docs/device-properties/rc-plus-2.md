# Device Properties — DJI RC Plus 2 Enterprise

**Gateway role**: RC gateway. The RC serial is `{gateway_sn}` for the pilot-to-cloud path and `{device_sn}` for the RC's own property topics. For properties published by the paired **aircraft** (M4D / M4TD) when relayed by this RC, see [`m4d.md`](m4d.md) §B and [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md).
**Cohort**: Dock 3 cohort RC — pairs with Matrice 4D / Matrice 4TD. The dock sibling in this cohort is [`dock3.md`](dock3.md); the RC sibling in the older cohort is [`rc-pro.md`](rc-pro.md).

**Sources**:

| File | Version | Authority |
|---|---|---|
| [`DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt) | v1.15 | Primary. 625 lines, column-per-row layout. |
| — | — | RC Plus 2 Enterprise postdates v1.11.3; no v1.11 canonical counterpart. |

RC Plus 2 Enterprise reports **11 top-level properties** (6 OSD + 5 state) on the RC gateway topics. **0 are writable via `property/set`** — the RC itself exposes no writable gateway-level properties; the `thing/product/{rc_sn}/property/set` topic is used exclusively to reach writable properties on the paired aircraft (see [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md) §3 + [`m4d.md`](m4d.md) §3).

Topic mapping (see Phase 2 [`mqtt/README.md`](../mqtt/README.md) for envelope):

| Topic | Push mode | Carries |
|---|---|---|
| `thing/product/{rc_sn}/osd` | 0 — stable frequency (~0.5 Hz) | OSD properties — §1 below. |
| `thing/product/{rc_sn}/state` | 1 — on-change | State properties — §2 below. |
| `thing/product/{rc_sn}/property/set` | — | No RC-owned writable keys; topic routes to paired-aircraft writable properties only — see §3. |

Cross-reference: for the cohort sibling (older gen), see [`rc-pro.md`](rc-pro.md). §5 below enumerates the deltas — two top-level property swaps (`drc_state` ↔ `country`) and a `live_status.»video_quality` enum divergence.

---

## 1. OSD properties — `pushMode: 0`

6 top-level properties push on `thing/product/{rc_sn}/osd` at ~0.5 Hz.

| Property | Description | Type | Constraint | Access |
|---|---|---|---|---|
| `capacity_percent` | Remaining capacity — RC battery level | `int` | `{"max":"100","min":"0","step":"1","unit_name":"Percentage / %"}` | `r` |
| `height` | Ellipsoid height | `double` | `{"unit_name":"Meters / m"}` | `r` |
| `wireless_link` | Image-transmission link | `struct` | | `r` |
| `»dongle_number` | Number of dongles on the aircraft | `int` | — RC source copy-pastes the aircraft-side description; see §4 | |
| `»4g_link_state` | 4G link connection state | `enum_int` | `{"0":"Disconnected","1":"Connected"}` | |
| `»sdr_link_state` | SDR link connection state | `enum_int` | `{"0":"Disconnected","1":"Connected"}` | |
| `»link_workmode` | Video transmission link mode | `enum_int` | `{"0":"SDR Mode","1":"4G Fusion Mode"}` — labelled "Dock's video transmission link mode" in source; see §4 | |
| `»sdr_quality` | SDR signal quality | `int` | `{"max":"5","min":"0","step":"1"}` | |
| `»4g_quality` | Overall 4G signal quality | `int` | `{"max":"5","min":"0","step":"1"}` | |
| `»4g_uav_quality` | Sky-side 4G signal quality | `int` | `{"max":"5","min":"0","step":"1"}` — aircraft-to-4G-server | |
| `»4g_gnd_quality` | Ground-side 4G signal quality | `int` | `{"max":"5","min":"0","step":"1"}` — RC-to-4G-server | |
| `»sdr_freq_band` | SDR frequency band | `float` | | |
| `»4g_freq_band` | 4G frequency band | `float` | | |
| `latitude` | Latitude | `double` | `{"max":"90","min":"-90","step":"0.01"}` | `r` |
| `longitude` | Longitude of the gateway device | `double` | `{"max":"180","min":"-180","step":"0.01"}` | `r` |
| `drc_state` | DRC link state | `enum_int` | `{"0":"Not connected","1":"Connecting","2":"Connected"}` — **RC Plus 2 only** (not present on RC Pro) | `r` |

## 2. State properties — `pushMode: 1`

5 top-level properties push on `thing/product/{rc_sn}/state` on change.

| Property | Description | Type | Constraint | Access |
|---|---|---|---|---|
| `live_capacity` | Gateway live-streaming capability | `struct` | | `r` |
| `»available_video_number` | Selectable streaming bitrate count | `int` | | |
| `»coexist_video_number_max` | Max simultaneous streams | `int` | | |
| `»device_list` | Selectable video-source devices | `array` of `struct` | device layer — aircraft, etc. | |
| `»»sn` | Video-source device SN | `text` | | |
| `»»available_video_number` | Per-aircraft selectable streams | `int` | | |
| `»»coexist_video_number_max` | Per-aircraft max simultaneous | `int` | | |
| `»»camera_list` | Cameras on this aircraft | `array` of `struct` | | |
| `»»»camera_index` | Camera index | `text` | format `{type-subtype-gimbalindex}` | |
| `»»»available_video_number` | Per-camera selectable streams | `int` | | |
| `»»»coexist_video_number_max` | Per-camera max simultaneous | `int` | | |
| `»»»video_list` | Selectable streams for this camera | `array` of `struct` | | |
| `»»»»video_index` | Stream index | `text` | | |
| `»»»»video_type` | Stream type | `text` | normal / wide / zoom / infrared / etc. | |
| `»»»»switchable_video_types` | Switchable stream types | `array` of `text` | | |
| `dongle_infos` | 4G Dongle inventory | `array` of `struct` | | `r` |
| `»imei` | Dongle IMEI | `text` | Unique per dongle | `r` |
| `»dongle_type` | Dongle type | `enum_int` | `{"6":"Old Dongle","10":"New Dongle with eSIM support"}` | `r` |
| `»eid` | eSIM EID | `text` | Unique per eSIM; for carrier plan queries | `r` |
| `»esim_activate_state` | eSIM activation state | `enum_int` | `{"0":"Not activated","1":"Activated"}` — 2-value form (dock Dock 3 has 3-value with `"Unknown"`) | `r` |
| `»sim_card_state` | Physical SIM insertion | `enum_int` | `{"0":"Not inserted","1":"Inserted"}` | `r` |
| `»sim_slot` | Active SIM slot | `enum_int` | `{"0":"Unknown","1":"Physical SIM card","2":"eSIM"}` | `r` |
| `»esim_infos` | eSIM records | `array` of `struct` | | `r` |
| `»»telecom_operator` | Carrier | `enum_int` | `{"0":"Unknown","1":"Mobile","2":"China Unicom","3":"Telecommunications"}` — Dock-2-style short labels (see §4) | `r` |
| `»»enabled` | Active eSIM | `bool` | `{"false":"Not in use","true":"In use"}` — only one eSIM enabled at a time | `r` |
| `»»iccid` | ICCID | `text` | | `r` |
| `»sim_info` | Physical SIM card info | `struct` | | `r` |
| `»»telecom_operator` | Carrier | `enum_int` | Same enum as `esim_infos.telecom_operator` | `r` |
| `»»sim_type` | Physical SIM card type | `enum_int` | `{"0":"Unknown","1":"Other regular SIM card","2":"Three-network card"}` | `r` |
| `»»iccid` | ICCID | `text` | | `r` |
| `live_status` | Per-stream live-streaming state | `array` of `struct` | | `r` |
| `»video_id` | Stream identifier | `text` | format `{sn}/{camera_index}/{video_index}` where `{sn}` is the video-source device SN, `{camera_index}` is `{type-subtype-gimbalindex}`, `{video_index}` is the camera-level stream index | |
| `»video_type` | Video lens type | `text` | `{"length":"24"}` — normal / wide / zoom / infrared / etc. | |
| `»video_quality` | Live-stream quality | `enum_int` | `{"0":"Auto","1":"Smooth","2":"HD","3":"Ultra HD"}` — **4-value form, differs from RC Pro's 5-value enum**; see §5 | |
| `»status` | Streaming state | `enum_int` | `{"0":"Not live streaming","1":"In live streaming"}` | |
| `»error_status` | Error code | `int` | `{"length":6}` | |
| `firmware_version` | Firmware version | `text` | `{"length":"64"}` | `r` |
| `cloud_control_auth` | Cloud control authorization list | `array` of `string` | size `-` — identifies which control permissions are granted to the cloud | `r` |

## 3. Settable via `property/set` — `accessMode: rw`

**None.** RC Plus 2 Enterprise exposes **no writable properties** at the RC gateway level. Every row in §1 and §2 is `accessMode: r`.

The topic `thing/product/{rc_sn}/property/set` **is still used** on the pilot path — it carries cloud writes that target writable properties on the paired **aircraft** (baseline `height_limit`, `night_lights_state`, `camera_watermark_settings`, the thermal cluster on the `{type-subtype-gimbalindex}` struct; M4D adds `commander_flight_height` / `commander_flight_mode` / `commander_mode_lost_action`). The RC acts as the routing envelope owner. See:

- [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md) §3 — baseline aircraft writable surface on pilot path.
- [`m4d.md`](m4d.md) §3 — M4D-specific pilot-path writable additions.
- [`mqtt/pilot-to-cloud/property-set/README.md`](../mqtt/pilot-to-cloud/property-set/README.md) — envelope + reply semantics.

RC-configurable preferences (livestream quality selection, DRC-mode toggles, etc.) do not flow through `property/set` on this RC — they use services / DRC methods instead. See [`mqtt/pilot-to-cloud/`](../mqtt/pilot-to-cloud/README.md) Phase 4h for the service catalog.

## 4. DJI-source inconsistencies (flagged, not escalated)

1. **RC descriptions copy-paste dock-source text** — three places in the RC Plus 2 extract describe RC-owned properties using aircraft- or dock-centric wording:
   - `wireless_link.»dongle_number` is labelled `"Number of Dongles on the aircraft"` — the RC has its own dongle bay; the field counts the **dongles visible on the transmission link**, which on RC Plus 2 Enterprise includes both the RC-side dongle(s) and the paired aircraft's dongles. Description is cosmetic-wrong but field semantic is clear from context.
   - `wireless_link.»link_workmode` is labelled `"Dock's video transmission link mode"` — RC Plus 2 is not a dock. Same enum codes as the dock equivalent; the mode is the RC's own SDR-vs-4G-fusion choice.
   - `live_capacity` header says `"Gateway device live streaming capability"` and `live_status` header says `"Gateway's current overall live streaming state push"` — these are correct since "gateway" covers both dock and RC, but the dock-oriented framing in the rest of the descriptions leaks through.

   None of this affects the wire content; treat as v1.15-extract cosmetic defects inherited from DJI's shared gateway-property template.

2. **`dongle_infos.»esim_infos.»telecom_operator` and `dongle_infos.»sim_info.»telecom_operator` use Dock-2-style short labels** (`"Mobile"`, `"Telecommunications"`) rather than Dock-3-style fully-qualified labels (`"China Mobile"`, `"China Telecom"`). Enum codes `{1, 2, 3}` are identical to Dock 3's resolution: China Mobile / China Unicom / China Telecom. Cloud implementations should treat the codes as authoritative and ignore the label variant — this is the same label-drift [`dock3.md`](dock3.md) §4 flags for its own `sim_info` sub-struct.

3. **`dongle_infos.»esim_activate_state` is 2-value on RC Plus 2** (`{"0":"Not activated","1":"Activated"}`) versus Dock 3's 3-value form (`{"0":"Unknown","1":"Not activated","2":"Activated"}`). Interpreted safely: RC Plus 2 never emits code `2`, so cloud implementations that parse the Dock 3 form are forward-compatible.

4. **`live_status.»video_quality` 4-value enum** on RC Plus 2 diverges from both the dock gateways and RC Pro. See §5 for the full comparison; this is a cohort difference, not a source defect.

5. **No OSD example in the source file.** The RC Plus 2 extract is a property-list only; there is no accompanying `osd` / `state` example payload block (Dock 2, Dock 3 extracts include both). Cloud implementations should assume the same envelope shape as the dock equivalents (see [`mqtt/dock-to-cloud/osd/README.md`](../mqtt/dock-to-cloud/osd/README.md) + [`mqtt/pilot-to-cloud/osd/README.md`](../mqtt/pilot-to-cloud/osd/README.md)).

None rise to [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) level.

## 5. Drift vs RC Pro Enterprise

RC Plus 2 is **not** a superset of RC Pro. There are two top-level swaps and one nested enum divergence.

| Property | RC Pro | RC Plus 2 | Classification |
|---|---|---|---|
| `drc_state` | absent | `enum_int {0: Not connected, 1: Connecting, 2: Connected}` (osd) | **Added on RC Plus 2** — the cohort introduces DRC state publication at the RC level. RC Pro Enterprise does not publish DRC link state on its gateway OSD (DRC lifecycle on the RC Pro cohort is tracked via Phase 4h services only). |
| `country` | `text` (osd) | absent | **Absent on RC Plus 2** — RC Pro publishes a country area code; RC Plus 2 does not. Cloud implementations that rely on this for regional-behaviour gating must source it elsewhere for the RC Plus 2 cohort. |
| `live_status.»video_quality` enum | `enum_int {"0":"Adaptive","1":"Smooth","2":"Standard definition","3":"High definition","4":"Ultra-high definition"}` (5 values) | `enum_int {"0":"Auto","1":"Smooth","2":"HD","3":"Ultra HD"}` (4 values) | **Incompatible enum** — RC Plus 2 drops the 5th value (`4: Ultra-high definition`) and relabels `0: Adaptive → Auto`, `2: Standard definition → HD`, `3: High definition → Ultra HD`. Cloud implementations that emit or parse this field must branch on RC cohort. |

Other properties — `live_capacity`, `capacity_percent`, `height`, `dongle_infos` (including nested eSIM and physical-SIM structs), `wireless_link` (all 10 nested fields), `firmware_version`, `latitude`, `longitude`, `cloud_control_auth` — are shape-identical and enum-identical across the two RCs.

No cohort escalations. RC Plus 2 drift is the cohort-boundary swap (DRC state vs country area code) + the video-quality relabel.

## 6. Property Set — envelope

RC Plus 2 has no RC-owned writable properties, but it is the `{gateway_sn}` owner for pilot-path `property/set` routing. For the envelope shape and reply semantics see:

- [`mqtt/pilot-to-cloud/property-set/README.md`](../mqtt/pilot-to-cloud/property-set/README.md) — pilot-path shell.
- [`mqtt/dock-to-cloud/property-set/README.md`](../mqtt/dock-to-cloud/property-set/README.md#envelope--set-request) — canonical envelope + `result` code enum (`0` success / `1` fail / `2` time exceed / other → [`error-codes/`](../error-codes/) Phase 8).

A representative call that rides `thing/product/{rc_plus_2_sn}/property/set` but targets a paired-aircraft key:

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1643268212187,
  "data": {
    "height_limit": 120
  }
}
```

The `{gateway_sn}` in the topic is the RC serial; the property key (`height_limit` above) belongs to the aircraft. DJI's routing layer propagates the write via the RC → aircraft link. Reply rides `thing/product/{rc_plus_2_sn}/property/set_reply`.

## 7. Source provenance

| Source | Lines | Role |
|---|---|---|
| [`DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt) | 625 | v1.15 primary. Column-per-row layout (one row per cell); 11 top-level properties enumerated. No example payload block. |
| [`DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt`](../../DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt) | — | Pilot-to-Cloud envelope shape (cross-referenced from Phase 2 [`mqtt/README.md`](../mqtt/README.md)). Note [`OQ-002`](../OPEN-QUESTIONS.md#oq-002--pilot-to-cloud-osd-struct-example-appears-to-be-a-copy-paste-of-the-dock-osd-example) — the OSD example in this topic-definition file is dock content, not pilot content. |
| [`rc-pro.md`](rc-pro.md) | — | Cohort sibling; §5 drift table references RC Pro values verbatim. |

No v1.11 canonical counterpart exists (RC Plus 2 Enterprise postdates v1.11.3).
