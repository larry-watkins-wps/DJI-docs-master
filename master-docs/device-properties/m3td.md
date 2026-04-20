# Device Properties — DJI Matrice 3TD (M3TD)

**Gateway role**: aircraft sub-device. Same gateway model as M3D — reported through a Dock 2 (dock-path) or RC Pro Enterprise (pilot-path).
**Cohort**: Dock 2 / M3-series cohort. **Thermal variant** of M3D — same airframe and flight-control surface, with a thermal-capable payload bay as the default factory configuration.

**Source**: [`DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt) co-documents M3D and M3TD in a single catalog — there is no separate M3TD file. DJI's v1.15 extract treats M3TD as an M3D with a different payload configuration.

## 1. Relationship to M3D

At the **thing-model property catalog level**, M3TD is indistinguishable from M3D:

- Same 42 top-level dock-path properties (24 OSD + 18 state), same writable surface, same enum bodies, same drift vs pilot-path baseline. See [`m3d.md`](m3d.md) for the full catalog.
- Same pilot-path properties (cites [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md)).
- Same topic names (`thing/product/{m3td_sn}/osd`, `/state`, `/property/set`, `/property/set_reply`).

The M3TD designation distinguishes the aircraft at the device-model-key level (`{domain-type-subtype}`), **not** at the property level. Cloud implementations that need to branch on aircraft model should use:

- `sub_device.device_model_key` on the dock gateway's `osd` topic (dock-path discovery).
- `update_topo` method payload (both paths) — the sub-device entry carries the model key.
- The `domain-type-subtype` triple decoded against DJI's [Product Support](https://developer.dji.com/doc/cloud-api-tutorial/en/overview/product-support.html) enumeration — M3TD has a distinct `(type, subtype)` pair from M3D.

Do **not** branch on the property surface; it will not tell M3D and M3TD apart.

## 2. Payload-level differences

The operational difference between M3D and M3TD surfaces via the `cameras` array and the per-payload `{type-subtype-gimbalindex}` struct:

- **`cameras.»payload_index`** — the payload index string identifies the physical payload attached. The default M3TD factory configuration ships a thermal-capable gimbal with a distinct `payload_index` enum value from the M3D's default RGB-only gimbal. An M3D fitted with a thermal payload post-factory will emit the same `payload_index` as an M3TD — i.e., the payload_index reflects payload, not airframe.
- **Thermal fields in `{type-subtype-gimbalindex}`** — `thermal_current_palette_style`, `thermal_supported_palette_styles`, `thermal_gain_mode`, `thermal_isotherm_state`, `thermal_isotherm_upper_limit`, `thermal_isotherm_lower_limit`, `thermal_global_temperature_min`, `thermal_global_temperature_max`. These fields are present in the schema for every M3D/M3TD aircraft but only populated when the attached payload is thermal-capable. An M3D without a thermal payload will emit the schema keys with default / zero / empty values; an M3TD (or M3D-with-thermal-payload) will emit real values.
- **`cameras.»ir_zoom_factor` / `»ir_metering_*` / thermal sub-bundle** — same visibility rule: present in schema always, meaningful only when thermal payload is attached.

## 3. Out-of-scope devices in shared enums

M3D/M3TD dock-path enums referencing `compatible_device_type` or similar cross-device enumerations include out-of-scope devices for completeness:

| Enum | Out-of-scope references |
|---|---|
| `cameras.»payload_index` | Payload indices for H20N / H20T / P1 / L1 / L2 / XT2 / Z30 payloads that are M3D-compatible but also appear on out-of-scope airframes (M30 / M350 / M300). Cloud implementations should not reject unknown payload indices. |
| `mode_code` | No out-of-scope rows — the 21-value enum is M3D/M3TD/M4D-shared. |

No M3TD-specific enum value is unique to the thermal variant — all thermal-related enums (palette, gain, isotherm) are defined in the shared `{type-subtype-gimbalindex}` struct schema and referenced identically from M3D and M3TD.

## 4. DJI-source inconsistencies

Same as [`m3d.md`](m3d.md) §4 — M3TD is co-documented. None rise to [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) level.

## 5. Drift

- **M3TD vs M3D**: None at the property level.
- **M3TD vs M4TD**: same as M3D vs M4D drift (see [`m3d.md`](m3d.md) §5): `mode_code` value `21` added on M4D cohort; `remaining_power_for_return_home` note references different Dock version; `type_subtype_gimbalindex` schema-cell garbled only on M4D source.
- **v1.11 → v1.15 drift**: same as M3D drift (see [`m3d.md`](m3d.md) §6).

## 6. Source provenance

| Source | Role |
|---|---|
| [`DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt) | v1.15 primary. Co-documents M3D + M3TD. |
| [`m3d.md`](m3d.md) | Full catalog. M3TD property behaviour is M3D's verbatim. |
| [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md) | Pilot-path baseline. |

Per-payload quirks (if any become relevant for M3TD specifically) will be documented in [`device-annexes/m3td.md`](../device-annexes/m3td.md) *(pending Phase 10)*.
