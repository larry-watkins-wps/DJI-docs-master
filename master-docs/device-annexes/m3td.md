# Device Annex — DJI Matrice 3TD (M3TD)

**Cohort**: Dock 2 / M3-series cohort — M3TD is the **thermal variant of M3D**.
**Gateway role**: aircraft sub-device — identical to M3D. Dock 2 (dock-path) or RC Pro Enterprise (pilot-path).
**Primary sources**: same as M3D — [`DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt) (v1.15, M3D + M3TD co-documented) + [`_aircraft-pilot-base.md`](../device-properties/_aircraft-pilot-base.md).

---

## 1. Relation to M3D

**M3TD is a property-level duplicate of M3D.** The two aircraft share every gateway-level property, every MQTT method surface, every workflow participation, and the same WPML action catalog. DJI co-documents them in a single source extract (`M3D_M3DT_Properties.txt`) because the schema is byte-equivalent.

**Read [`m3d.md`](m3d.md) first.** The M3D annex covers everything that applies to M3TD verbatim; this annex only calls out the thermal-variant deltas.

---

## 2. Thermal-variant deltas

The M3D / M3TD distinction is expressed on the wire through **payload identity**, not through distinct properties:

### 2.1 Payload classification

- **M3D** — optical-first enterprise aircraft. Compatible factory payloads include the Zenmuse H20N (multi-sensor with low-light) and H30T (multi-sensor thermal+optical).
- **M3TD** — thermal-first enterprise variant. Ships with the H30T as the primary payload; the aircraft model key identifies M3TD specifically via the device-topology `domain-type-subtype` triple.

On the wire, the distinction surfaces at:

| Field | Where | What changes |
|---|---|---|
| `domain-type-subtype` model key | In `update_topo` ([Phase 4a](../mqtt/dock-to-cloud/status/update_topo.md)) and in `sub_device.»device_model_key` (on Dock 2 OSD) | Different subtype byte between M3D and M3TD — cloud identifies the SKU here. |
| `»payload_index` under `cameras` | M3D and M3TD OSD | Different `type-subtype-gimbalindex` string — identifies which physical payload is mounted. M3TD ships H30T; M3D may ship H20N, H30T, or other Zenmuse enterprise payloads. |
| `{type-subtype-gimbalindex}` per-payload dynamic struct | M3D and M3TD OSD | Struct **shape** is identical; struct **key** differs by payload. M3TD's thermal cluster (`thermal_*` sub-fields) is populated; optical-only M3D mounts may report them as empty / default. |

The gateway-level property catalog does **not** change between the two SKUs — every property listed in [`../device-properties/m3d.md`](../device-properties/m3d.md) is published by M3TD with identical schema.

### 2.2 Thermal-specific camera surface

The thermal gimbal is controlled by the same DRC methods as any other payload on the Dock 2 cohort. Thermal-specific methods surface under:

- **`drc_ir_metering_mode_set` / `drc_ir_metering_point_set` / `drc_ir_metering_area_set`** — IR metering control (Phase 4h, pilot-path). These target thermal-capable payloads and are used with M3TD / M4TD / any H30T-equipped aircraft.
- **`drc_camera_photo_format_set`** — Dock-3-only service; M3TD on Dock 2 does not use this.
- Camera-state push (`cameras.»ir_zoom_factor`, `cameras.»ir_metering_*`) — documented in [`../device-properties/m3d.md`](../device-properties/m3d.md) §A.1 and applies to M3TD.

### 2.3 HMS coverage

Thermal-specific HMS codes in [`../hms-codes/0x14-payload-imu.md`](../hms-codes/0x14-payload-imu.md) (payload IMU), [`../hms-codes/0x1C-camera.md`](../hms-codes/0x1C-camera.md) (camera, including H30T-specific), and [`../hms-codes/0x1D-gimbal.md`](../hms-codes/0x1D-gimbal.md) apply to M3TD's thermal gimbal. The H30T camera alarms (thermal overheat, thermal calibration) target M3TD primarily among the Dock 2 cohort.

### 2.4 Livestream video type

M3TD's `live_capacity.»device_list.»camera_list.»video_list.»video_type` includes `"ir"` / `"infrared"` stream types alongside `"wide"`/`"zoom"`. Cloud implementations selecting a stream source on M3TD should expect the thermal option in the selectable set; M3D (non-thermal SKU) may not report it depending on which payload is mounted.

---

## 3. Implementation gotchas

Beyond the full M3D gotcha list (see [`m3d.md`](m3d.md) §3):

1. **Do not treat "M3D source extract covers M3TD" as "M3D and M3TD are interchangeable on the wire."** They share schema but differ on payload identity — a cloud doing SKU-specific business logic (e.g., thermal-only analytics) must branch on the `domain-type-subtype` model key in the topology snapshot, not on the aircraft's SN or hostname.
2. **M3TD's thermal gimbal exposes stream types not present on non-thermal mounts** — `"ir"` / `"infrared"`. Cloud implementations should enumerate `live_capacity.video_list` at stream-start time rather than assuming a fixed video-type set.
3. **M3TD HMS alarm surface is richer on `0x14` and `0x1C` prefixes** than non-thermal M3D mounts — the cloud should expect thermal-overheat / thermal-calibration alarms that may never fire on an M3D without an H30T.

---

## 4. Features this device lacks

- Same "lacks" list as M3D (see [`m3d.md`](m3d.md) §4): no M4D pilot-path extensions, no WPML megaphone/searchlight, no Dock 3 / M4 cohort methods.
- Additionally, M3TD is a **thermal-first SKU** — implementations assuming an M3TD has every optical payload may find only thermal-capable modes available. This is payload-level, not aircraft-level.

---

## 5. Cross-reference map

| Phase | Doc | What's covered |
|---|---|---|
| 3–9 | *See [`m3d.md`](m3d.md) §5.* | Identical cross-reference surface. |
| 7 WPML | [`../wpml/common-elements.md`](../wpml/common-elements.md) | Same action catalog as M3D; no M4D-only actions. |
| 8 HMS | [`../hms-codes/0x14-payload-imu.md`](../hms-codes/0x14-payload-imu.md), [`../hms-codes/0x1C-camera.md`](../hms-codes/0x1C-camera.md), [`../hms-codes/0x1D-gimbal.md`](../hms-codes/0x1D-gimbal.md) | Thermal-payload-specific alarm coverage. |

## 6. Source provenance

| File | Role |
|---|---|
| [`DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt) | v1.15 dock-path primary. Covers M3TD in the same extract as M3D; schema byte-equivalent. |
| [`../device-properties/m3d.md`](../device-properties/m3d.md) | M3D per-device property catalog — M3TD inherits verbatim. |
| [`m3d.md`](m3d.md) | M3D device annex — read first. |
