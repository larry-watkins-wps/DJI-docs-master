# Device Properties — DJI RC Pro Enterprise

**Gateway role**: RC gateway. The RC serial is `{gateway_sn}` for the pilot-to-cloud path and `{device_sn}` for the RC's own property topics. For properties published by the paired **aircraft** (M3D / M3TD) when relayed by this RC, see [`m3d.md`](m3d.md) §B and [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md).
**Cohort**: Dock 2 cohort RC — pairs with Matrice 3D / Matrice 3TD. The dock sibling in this cohort is [`dock2.md`](dock2.md); the RC sibling in the current cohort is [`rc-plus-2.md`](rc-plus-2.md).

**Sources**:

| File | Version | Authority |
|---|---|---|
| [`DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt) | v1.15 | Primary. 68 lines, tab-separated row-per-line layout. |
| [`Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/00.properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/00.properties.md) | v1.11.3 | Drift cross-check. v1.11 carries 10 top-level properties; v1.15 adds `cloud_control_auth`. See §5. |
| [`DJI_Cloud/DJI_CloudAPI_RC-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Properties.txt) | v1.15 | **Out-of-scope sibling** — the plain-RC (non-Enterprise) property file is byte-equivalent in content; DJI ships the same 11-property catalog for both plain RC and RC Pro Enterprise. See §4. |

RC Pro Enterprise reports **11 top-level properties** (6 OSD + 5 state) on the RC gateway topics. **0 are writable via `property/set`** — the RC itself exposes no writable gateway-level properties; the `thing/product/{rc_sn}/property/set` topic is used exclusively to reach writable properties on the paired aircraft (see [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md) §3 — M3D / M3TD on pilot path uses the baseline-only writable surface with no M3-specific extensions).

Topic mapping (see Phase 2 [`mqtt/README.md`](../mqtt/README.md) for envelope):

| Topic | Push mode | Carries |
|---|---|---|
| `thing/product/{rc_sn}/osd` | 0 — stable frequency (~0.5 Hz) | OSD properties — §1 below. |
| `thing/product/{rc_sn}/state` | 1 — on-change | State properties — §2 below. |
| `thing/product/{rc_sn}/property/set` | — | No RC-owned writable keys; topic routes to paired-aircraft writable properties only — see §3. |

Cross-reference: for the current-gen cohort RC, see [`rc-plus-2.md`](rc-plus-2.md) §5 for the full drift table. Briefly: RC Pro has `country` (absent on RC Plus 2); RC Plus 2 has `drc_state` (absent on RC Pro); the two RCs carry incompatible `live_status.»video_quality` enums.

---

## 1. OSD properties — `pushMode: 0`

6 top-level properties push on `thing/product/{rc_sn}/osd` at ~0.5 Hz.

| Property | Description | Type | Constraint | Access |
|---|---|---|---|---|
| `country` | Country area code | `text` | — | `r` |
| `capacity_percent` | Remaining capacity — RC battery level | `int` | `{"max":"100","min":"0","step":"1","unit_name":"Percentage / %"}` | `r` |
| `height` | Ellipsoid height | `double` | `{"unit_name":"Meters / m"}` | `r` |
| `wireless_link` | Image-transmission link | `struct` | | `r` |
| `»dongle_number` | Number of dongles on the aircraft | `int` | — source copy-pastes aircraft-side wording; see §4 | |
| `»4g_link_state` | 4G link connection state | `enum_int` | `{"0":"Disconnected","1":"Connected"}` | |
| `»sdr_link_state` | SDR link connection state | `enum_int` | `{"0":"Disconnected","1":"Connected"}` | |
| `»link_workmode` | Video-transmission link mode | `enum_int` | `{"0":"SDR Mode","1":"4G Fusion Mode"}` — labelled "Dock's video transmission link mode" in source; see §4 | |
| `»sdr_quality` | SDR signal quality | `int` | `{"max":"5","min":"0","step":"1"}` | |
| `»4g_quality` | Overall 4G signal quality | `int` | `{"max":"5","min":"0","step":"1"}` | |
| `»4g_uav_quality` | Sky-side 4G signal quality | `int` | `{"max":"5","min":"0","step":"1"}` — aircraft-to-4G-server | |
| `»4g_gnd_quality` | Ground-side 4G signal quality | `int` | `{"max":"5","min":"0","step":"1"}` — RC-to-4G-server | |
| `»sdr_freq_band` | SDR frequency band | `float` | | |
| `»4g_freq_band` | 4G frequency band | `float` | | |
| `latitude` | Latitude | `double` | `{"max":"90","min":"-90","step":"0.01"}` | `r` |
| `longitude` | Longitude of the gateway device | `double` | `{"max":"180","min":"-180","step":"0.01"}` | `r` |

RC Pro Enterprise does **not** publish `drc_state` on its OSD. DRC lifecycle on this cohort is observed via Phase 4h pilot-to-cloud services (`cloud_control_auth_request` / `cloud_control_auth_notify` / `cloud_control_release`). See [`mqtt/pilot-to-cloud/events/cloud_control_auth_notify.md`](../mqtt/pilot-to-cloud/events/cloud_control_auth_notify.md) and [`mqtt/pilot-to-cloud/services/cloud_control_auth_request.md`](../mqtt/pilot-to-cloud/services/cloud_control_auth_request.md).

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
| `»eid` | eSIM EID | `text` | Unique per eSIM | `r` |
| `»esim_activate_state` | eSIM activation state | `enum_int` | `{"0":"Not activated","1":"Activated"}` — 2-value form | `r` |
| `»sim_card_state` | Physical SIM insertion | `enum_int` | `{"0":"Not inserted","1":"Inserted"}` | `r` |
| `»sim_slot` | Active SIM slot | `enum_int` | `{"0":"Unknown","1":"Physical SIM card","2":"eSIM"}` | `r` |
| `»esim_infos` | eSIM records | `array` of `struct` | | `r` |
| `»»telecom_operator` | Carrier | `enum_int` | `{"0":"Unknown","1":"Mobile","2":"China Unicom","3":"Telecommunications"}` — Dock-2-style short labels (see §4) | `r` |
| `»»enabled` | Active eSIM | `bool` | `{"false":"Not in use","true":"In use"}` | `r` |
| `»»iccid` | ICCID | `text` | | `r` |
| `»sim_info` | Physical SIM card info | `struct` | | `r` |
| `»»telecom_operator` | Carrier | `enum_int` | Same enum as `esim_infos.telecom_operator` | `r` |
| `»»sim_type` | Physical SIM card type | `enum_int` | `{"0":"Unknown","1":"Other regular SIM card","2":"Three-network card"}` | `r` |
| `»»iccid` | ICCID | `text` | | `r` |
| `live_status` | Per-stream live-streaming state | `array` of `struct` | | `r` |
| `»video_id` | Stream identifier | `text` | format `{sn}/{camera_index}/{video_index}` where `{sn}` is the video-source device SN, `{camera_index}` is `{type-subtype-gimbalindex}`, `{video_index}` is the camera-level stream index | |
| `»video_type` | Video lens type | `text` | `{"length":"24"}` — normal / wide / zoom / infrared / etc. | |
| `»video_quality` | Live-stream quality | `enum_int` | `{"0":"Adaptive","1":"Smooth","2":"Standard definition","3":"High definition","4":"Ultra-high definition"}` — **5-value form, differs from RC Plus 2's 4-value enum**; see §5 and [`rc-plus-2.md`](rc-plus-2.md) §5 | |
| `»status` | Streaming state | `enum_int` | `{"0":"Not live streaming","1":"In live streaming"}` | |
| `»error_status` | Error code | `int` | `{"length":6}` | |
| `firmware_version` | Firmware version | `text` | `{"length":"64"}` | `r` |
| `cloud_control_auth` | Cloud control authorization list | `array` of `string` | size `-` — identifies which control permissions are granted to the cloud | `r` |

## 3. Settable via `property/set` — `accessMode: rw`

**None.** RC Pro Enterprise exposes **no writable properties** at the RC gateway level. Every row in §1 and §2 is `accessMode: r`.

The topic `thing/product/{rc_sn}/property/set` **is still used** on the pilot path — it carries cloud writes that target writable properties on the paired **aircraft** (M3D / M3TD): `height_limit`, `night_lights_state`, `camera_watermark_settings` (9-field struct), and the thermal cluster on the `{type-subtype-gimbalindex}` payload struct. M3-series pilot-path exposes the baseline writable surface only — no M3-specific extensions (M4D is the only cohort with pilot-path `commander_*` extensions). See:

- [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md) §3 — baseline aircraft writable surface on pilot path.
- [`mqtt/pilot-to-cloud/property-set/README.md`](../mqtt/pilot-to-cloud/property-set/README.md) — envelope + reply semantics.

RC-configurable preferences (livestream quality, DRC authorization, etc.) do not flow through `property/set` on this RC — they use services / DRC methods instead. See [`mqtt/pilot-to-cloud/`](../mqtt/pilot-to-cloud/README.md) Phase 4h.

## 4. DJI-source inconsistencies (flagged, not escalated)

1. **RC descriptions copy-paste dock-source text** — same pattern as [`rc-plus-2.md`](rc-plus-2.md) §4. Three cosmetic leakages in the `wireless_link` sub-struct:
   - `»dongle_number` — labelled `"Number of Dongles on the aircraft"`; the RC has its own dongle bay.
   - `»link_workmode` — labelled `"Dock's video transmission link mode"`; the RC is not a dock.
   - `live_capacity` header says `"Gateway device live streaming capability"` — correct "gateway" wording but inherits dock-oriented sub-field text.

   Treat as v1.15-extract cosmetic defects inherited from DJI's shared gateway-property template.

2. **`dongle_infos.»esim_infos.»telecom_operator` / `dongle_infos.»sim_info.»telecom_operator` use Dock-2-style short labels** (`"Mobile"`, `"Telecommunications"`). Enum codes `{1, 2, 3}` are authoritative — China Mobile / China Unicom / China Telecom. Same label drift [`rc-plus-2.md`](rc-plus-2.md) §4 flags.

3. **`dongle_infos.»esim_activate_state` is 2-value on RC Pro** (`{"0":"Not activated","1":"Activated"}`) — no `"Unknown"` value. Matches RC Plus 2 and diverges from Dock 3's 3-value form.

4. **RC Pro Enterprise file is byte-equivalent to plain RC** at the property-catalog level. [`DJI_Cloud/DJI_CloudAPI_RC-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Properties.txt) (68 lines, plain-RC, out-of-scope sibling) enumerates the same 11 top-level properties with the same enums and descriptions. This is expected: DJI's plain-RC property schema is a subset of Enterprise-class capabilities, and for the Pilot-2-running RCs that subset covers the full gateway-level surface. Cloud implementations that ingest the plain-RC file should land on the same shape as this doc. Plain RC itself is **out of scope** per [`/CLAUDE.md`](../../CLAUDE.md) — we do not document it as a separate device, we only note the near-equivalence.

5. **No OSD example in the source file.** Same pattern as RC Plus 2; the extract is a property-list only. Cloud implementations should assume the shared pilot-to-cloud envelope from [`mqtt/pilot-to-cloud/osd/README.md`](../mqtt/pilot-to-cloud/osd/README.md).

None rise to [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) level.

## 5. Drift — v1.11 → v1.15 and vs RC Plus 2

### v1.11 → v1.15

v1.11 canonical ([`Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/00.properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/00.properties.md)) carries **10 top-level properties**; v1.15 carries **11**.

| Property | v1.11 | v1.15 | Classification |
|---|---|---|---|
| `cloud_control_auth` | absent | `array` of `string` (state, `r`) | **New property** — v1.15 adds publication of the cloud-control authorization list. Cloud implementations that only read the v1.11 catalog will not see this. Non-breaking for existing integrations — adding a state field is backward-compatible on the wire. |

All other properties (`live_capacity`, `country`, `capacity_percent`, `height`, `dongle_infos`, `live_status`, `wireless_link`, `firmware_version`, `latitude`, `longitude`) are present in v1.11 with identical shape, including the `live_status.»video_quality` 5-value enum. No enum values removed; no type changes; no description semantic shifts.

Drift is purely additive. Per 6a / 6b policy, no [`OQ-001`](../OPEN-QUESTIONS.md#oq-001--source-version-mismatch-between-cloud-api-doc-v1113-and-dji_cloud-v115) escalation.

### vs RC Plus 2 Enterprise

See [`rc-plus-2.md`](rc-plus-2.md) §5 for the full drift table. Summary:

| Property | RC Pro | RC Plus 2 | Classification |
|---|---|---|---|
| `drc_state` | absent | present (osd) | Cohort delta — RC Plus 2 adds DRC state publication at the RC level. |
| `country` | present (osd) | absent | Cohort delta — RC Pro publishes a country area code; RC Plus 2 does not. |
| `live_status.»video_quality` | 5-value enum | 4-value enum | Incompatible enum; cloud implementations must branch on RC cohort. |

## 6. Property Set — envelope

RC Pro has no RC-owned writable properties, but it is the `{gateway_sn}` owner for pilot-path `property/set` routing to paired M3D / M3TD aircraft. For envelope shape and reply semantics see:

- [`mqtt/pilot-to-cloud/property-set/README.md`](../mqtt/pilot-to-cloud/property-set/README.md) — pilot-path shell.
- [`mqtt/dock-to-cloud/property-set/README.md`](../mqtt/dock-to-cloud/property-set/README.md#envelope--set-request) — canonical envelope + `result` code enum.

A representative call that rides `thing/product/{rc_pro_sn}/property/set` but targets a paired-aircraft key:

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1643268212187,
  "data": {
    "night_lights_state": 1
  }
}
```

The `{gateway_sn}` is the RC serial; the property key belongs to the aircraft. Reply rides `thing/product/{rc_pro_sn}/property/set_reply`.

## 7. Source provenance

| Source | Lines | Role |
|---|---|---|
| [`DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt) | 68 | v1.15 primary. Tab-separated row-per-line layout; 11 top-level properties enumerated. No example payload block. |
| [`Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/00.properties.md`](../../Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/00.properties.md) | — | v1.11.3 drift cross-check. Carries 10 top-level properties — no `cloud_control_auth`. |
| [`DJI_Cloud/DJI_CloudAPI_RC-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_RC-Properties.txt) | 68 | Plain-RC sibling (out-of-scope). Byte-equivalent to the Enterprise file at the catalog level; see §4. |
| [`DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt`](../../DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt) | — | Pilot-to-Cloud envelope shape. Note [`OQ-002`](../OPEN-QUESTIONS.md#oq-002--pilot-to-cloud-osd-struct-example-appears-to-be-a-copy-paste-of-the-dock-osd-example). |
| [`rc-plus-2.md`](rc-plus-2.md) | — | Cohort sibling; §5 drift table references RC Plus 2 values verbatim. |
