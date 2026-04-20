# Device Annex — DJI Matrice 4TD (M4TD)

**Cohort**: Dock 3 / M4-series cohort — M4TD is the **thermal variant of M4D**.
**Gateway role**: aircraft sub-device — identical to M4D. Dock 3 (dock-path) or RC Plus 2 Enterprise (pilot-path).
**Primary sources**: same as M4D — [`DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt`](../../DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt) (v1.15, M4D + M4TD co-documented) + [`DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt) + [`../device-properties/_aircraft-pilot-base.md`](../device-properties/_aircraft-pilot-base.md).

---

## 1. Relation to M4D

**M4TD is a property-level duplicate of M4D.** Identical gateway-level property catalog, identical MQTT method surface, identical workflow participation, identical WPML action catalog including the M4D-unique `megaphone` + `searchlight` actions. DJI co-documents them in a single dock-path source extract and a single pilot-path delta extract.

**Read [`m4d.md`](m4d.md) first.** This annex layers on the thermal-variant deltas only.

---

## 2. Thermal-variant deltas

### 2.1 Payload identity

- **M4D** — optical-capable airframe. Compatible factory payloads span the Zenmuse M4 generation (multiple SKUs; the specific payload set is payload-level, not aircraft-level documentation).
- **M4TD** — thermal-first SKU. Ships with a thermal-capable primary payload (H30T-class) as the factory default.

The distinction surfaces on the wire at:

| Field | Where | What changes |
|---|---|---|
| `domain-type-subtype` model key | In `update_topo` ([Phase 4a](../mqtt/dock-to-cloud/status/update_topo.md)) and in Dock 3's `sub_device.»device_model_key` OSD | Different subtype byte between M4D and M4TD. |
| `»payload_index` under `cameras` | M4D and M4TD OSD | Different `type-subtype-gimbalindex` string — thermal payload on M4TD vs optical-first on M4D. |
| `{type-subtype-gimbalindex}` per-payload dynamic struct | M4D and M4TD OSD | Struct shape identical; struct key differs. M4TD's thermal cluster is populated. |

Same inheritance rule as the M3D / M3TD pair: gateway-level property catalog unchanged; SKU identified by model key.

### 2.2 Thermal-specific camera surface

Same as M3TD — thermal IR metering controls via Phase 4h pilot-path DRC variants ([`drc_ir_metering_mode_set`](../mqtt/pilot-to-cloud/drc/drc_ir_metering_mode_set.md) + friends) and the `cameras.»ir_*` / `cameras.»*_photo_storage_settings` OSD fields.

Additionally, M4TD has access to **Dock-3-only camera surface** that M3TD does not:
- `drc_camera_night_vision_enable` — night-vision mode (Dock 3 cohort).
- `drc_camera_denoise_level_set` — thermal denoise level (Dock 3 cohort).
- `drc_camera_photo_format_set` — **Dock 3 + M4TD-relevant**. IR-specific photo format. M3TD on Dock 2 does not have this method.

### 2.3 PSDK megaphone + searchlight

Like M4D, M4TD supports the WPML `megaphone` + `searchlight` actions when the respective PSDK payloads are mounted. The thermal gimbal does not exclude PSDK megaphone / searchlight mounts — the payloads occupy separate gimbal positions.

### 2.4 HMS coverage

Same prefix set as M3TD — the `0x1C` camera prefix includes H30T-class thermal alarms that apply to M4TD. Additional Dock-3-cohort camera SKUs may introduce new codes within the existing `0x1C` / `0x1D` / `0x1E` prefixes; see [`../hms-codes/0x1C-camera.md`](../hms-codes/0x1C-camera.md) for the current catalog.

### 2.5 Livestream video type

M4TD's `live_capacity` surfaces `"ir"` / `"infrared"` stream types. Same rule as M3TD — cloud implementations should enumerate the selectable set at stream-start, not assume a fixed video-type enum.

---

## 3. Implementation gotchas

Beyond the full M4D gotcha list (see [`m4d.md`](m4d.md) §3):

1. **Same "pilot-path extract is a delta" trap** as M4D. The M4TD pilot-path telemetry includes all baseline properties even though the extract lists only the 7 extensions + 6 overrides.
2. **Do not assume M4TD = M3TD thermally.** M4TD has access to Dock-3-only thermal DRC methods (`drc_camera_night_vision_enable`, `drc_camera_denoise_level_set`, `drc_camera_photo_format_set`) that M3TD does not. Cloud implementations supporting both must branch on the dock cohort for these.
3. **WPML `megaphone` / `searchlight` actions require PSDK payload mount.** A wayline authored assuming M4TD automatically has a megaphone will fail if the operator hasn't mounted the payload. Pre-flight validation should check aircraft+payload pairing via the `cameras.»payload_index` enumeration (or equivalent on the topology snapshot) before dispatch.
4. **Thermal DRC methods target the thermal gimbal specifically** — `drc_camera_photo_format_set` payload must specify the payload-index of the thermal mount. An M4TD with multiple payloads must route DRC correctly.

---

## 4. Features this device lacks

Same "lacks" list as M4D (see [`m4d.md`](m4d.md) §4): no Dock 2 cohort methods, no legacy-drone features.

M4TD is a **thermal-first SKU** — optical-only features (if any exist in the M4 generation's WPML or action set that are specific to non-thermal payloads) may be unavailable depending on payload mount.

---

## 5. Cross-reference map

| Phase | Doc | What's covered |
|---|---|---|
| 3–9 | *See [`m4d.md`](m4d.md) §5.* | Identical cross-reference surface. |
| 4 MQTT (thermal-specific DRC) | [`../mqtt/dock-to-cloud/drc/drc_camera_night_vision_enable.md`](../mqtt/dock-to-cloud/drc/drc_camera_night_vision_enable.md), [`../mqtt/dock-to-cloud/drc/drc_camera_denoise_level_set.md`](../mqtt/dock-to-cloud/drc/drc_camera_denoise_level_set.md), [`../mqtt/dock-to-cloud/drc/drc_camera_photo_format_set.md`](../mqtt/dock-to-cloud/drc/drc_camera_photo_format_set.md) | Dock-3-only thermal camera surface applicable to M4TD. |
| 7 WPML | [`../wpml/common-elements.md`](../wpml/common-elements.md) §16 | `megaphone` + `searchlight` actions. |
| 8 HMS | [`../hms-codes/0x14-payload-imu.md`](../hms-codes/0x14-payload-imu.md), [`../hms-codes/0x1C-camera.md`](../hms-codes/0x1C-camera.md), [`../hms-codes/0x1D-gimbal.md`](../hms-codes/0x1D-gimbal.md), [`../hms-codes/0x1E-psdk-payload.md`](../hms-codes/0x1E-psdk-payload.md) | Thermal payload + PSDK (megaphone / searchlight) alarm coverage. |

## 6. Source provenance

| File | Role |
|---|---|
| [`DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt`](../../DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt) | v1.15 dock-path primary (M4D + M4TD co-documented). |
| [`DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt) | v1.15 pilot-path delta (shared with M4D). |
| [`../device-properties/m4d.md`](../device-properties/m4d.md) | M4D per-device property catalog — M4TD inherits verbatim. |
| [`m4d.md`](m4d.md) | M4D device annex — read first. |
