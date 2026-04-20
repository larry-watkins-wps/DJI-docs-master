# Device Properties — DJI Matrice 4TD (M4TD)

**Gateway role**: aircraft sub-device. Same gateway model as M4D — reported through a Dock 3 (dock-path) or RC Plus 2 Enterprise (pilot-path).
**Cohort**: Dock 3 / M4-series cohort. **Thermal variant** of M4D — same airframe and flight-control surface, with a thermal-capable payload bay as the default factory configuration.

**Source**: [`DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt`](../../DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt) co-documents M4D and M4TD in a single dock-path catalog; [`DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt) co-documents them on the pilot-path. There is no separate M4TD file. DJI's v1.15 extract treats M4TD as an M4D with a different payload configuration.

## 1. Relationship to M4D

At the **thing-model property catalog level**, M4TD is indistinguishable from M4D:

- Same 42 top-level dock-path properties, same 7 pilot-path extensions, same writable surface, same enum bodies. See [`m4d.md`](m4d.md) for the full catalog.
- Same topic names (`thing/product/{m4td_sn}/osd`, `/state`, `/property/set`, `/property/set_reply`).

The M4TD designation distinguishes the aircraft at the device-model-key level (`{domain-type-subtype}`), **not** at the property level. See [`m3td.md`](m3td.md) §1 for the full model-branching guidance — identical pattern applies.

## 2. Payload-level differences

Same as M3TD vs M3D (see [`m3td.md`](m3td.md) §2): the operational difference surfaces via `cameras.»payload_index` and the per-payload `{type-subtype-gimbalindex}` struct. M4TD ships thermal-capable gimbal as factory default; the thermal sub-bundle (`thermal_current_palette_style`, `thermal_gain_mode`, isotherm keys, global min/max) is meaningfully populated on M4TD and on any M4D retrofitted with a thermal payload.

## 3. Out-of-scope devices in shared enums

Same out-of-scope considerations as [`m4d.md`](m4d.md): `cameras.»payload_index` enum references payloads shared across DJI's drone lineup including out-of-scope families. `mode_code` max value `21` is shared across the M4 cohort.

## 4. DJI-source inconsistencies

Same as [`m4d.md`](m4d.md) §4 — M4TD is co-documented. Key carryovers:
- `{_{type-subtype-gimbalindex}__aembLbhPpc}` garbled struct-name cell in both dock-path and pilot-path extracts. Authoritative name: `{type-subtype-gimbalindex}`.
- Pilot-path extract is a delta spec; baseline properties are inherited.

None rise to [`OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) level.

## 5. Drift

- **M4TD vs M4D**: None at the property level.
- **M4TD vs M3TD**: same as M4D vs M3D drift (see [`m4d.md`](m4d.md) §5): `mode_code` value `21` added on M4 cohort; `remaining_power_for_return_home` note references Dock 3 (vs Dock 2 on M3 cohort); all pilot-path extensions (`commander_*`, `offline_map_enable`, `current_rth_mode`, `rth_mode`, `current_commander_flight_mode`) are M4-cohort-only and absent from M3TD/M3D pilot-path.
- **v1.11 → v1.15 drift**: **none** — M4TD postdates v1.11, same as M4D.

## 6. Source provenance

| Source | Role |
|---|---|
| [`DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt`](../../DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt) | v1.15 dock-path primary. Co-documents M4D + M4TD. |
| [`DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`](../../DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt) | v1.15 pilot-path delta spec. Co-documents M4D + M4TD. |
| [`m4d.md`](m4d.md) | Full catalog. M4TD property behaviour is M4D's verbatim. |
| [`_aircraft-pilot-base.md`](_aircraft-pilot-base.md) | Pilot-path baseline. |

Per-payload quirks (if any become relevant for M4TD specifically) will be documented in [`device-annexes/m4td.md`](../device-annexes/m4td.md) *(pending Phase 10)*.
