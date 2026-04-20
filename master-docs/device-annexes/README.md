# Device annexes

Per-device summaries that aggregate what makes each in-scope device **distinct on the wire** — pulling together facts that are otherwise scattered across Phase 4 (MQTT method catalog), Phase 6 (device properties), Phase 7 (WPML + livestream protocols), Phase 8 (HMS + error codes), and Phase 9 (workflows).

Annexes are **triangulation**, not primary research. Every claim here has its authoritative citation in an earlier phase doc; annexes cross-link rather than restate.

## When to read an annex

Read the annex first when you're starting implementation work scoped to one device. The annex tells you:

1. **What this device actually is** on the wire — gateway role, paired cohort, source files.
2. **What's unique about it** — properties, MQTT methods, workflow variants, protocol support asymmetries.
3. **Implementation gotchas** — source-level quirks, enum-label drift, version-drift specifics that bite cloud implementers.
4. **What this device does not do** — features present on sibling devices but absent here, so you know where to skip effort.

Read the earlier-phase docs second, starting from the links the annex provides.

## Devices

### Dock 3 cohort — current generation

| Device | Role | Annex |
|---|---|---|
| DJI Dock 3 | Dock gateway | [`dock3.md`](dock3.md) |
| Matrice 4D (M4D) | Aircraft, paired with Dock 3 / RC Plus 2 Enterprise | [`m4d.md`](m4d.md) |
| Matrice 4TD (M4TD) | Aircraft — thermal variant of M4D | [`m4td.md`](m4td.md) |
| RC Plus 2 Enterprise | Remote controller, paired with M4D | [`rc-plus-2.md`](rc-plus-2.md) |

### Dock 2 cohort — older generation

| Device | Role | Annex |
|---|---|---|
| DJI Dock 2 | Dock gateway | [`dock2.md`](dock2.md) |
| Matrice 3D (M3D) | Aircraft, paired with Dock 2 / RC Pro Enterprise | [`m3d.md`](m3d.md) |
| Matrice 3TD (M3TD) | Aircraft — thermal variant of M3D | [`m3td.md`](m3td.md) |
| RC Pro Enterprise | Remote controller, paired with M3D / M3TD | [`rc-pro.md`](rc-pro.md) |

Out-of-scope devices (Dock 1, M30 / M30T, M300 / M350 RTK, M400, Mavic 3 Enterprise, plain RC) are referenced where they appear in DJI enums for context but do not get annexes.

## Annex layout

Each annex follows the same shape:

1. **Identity** — cohort, gateway role, paired devices, primary source files.
2. **Distinctive wire surface** — grouped by discipline (properties / MQTT methods / workflows / protocols / codes). Cross-links to Phase 4/6/7/8/9 docs; does not restate schema.
3. **Cohort asymmetries** — what this device has that its same-cohort siblings do not, or vice-versa.
4. **Implementation gotchas** — source-level quirks worth knowing when coding against this device specifically. Usually a subset of the per-device Phase 6 "DJI-source inconsistencies" plus any method-level quirks flagged in Phase 4.
5. **Features this device lacks** — explicit "not applicable" list, so implementers don't go hunting for absent surface.
6. **Cross-reference map** — the five-phase fan-out pointing at the primary docs for this device.

Annexes do **not** duplicate property tables, schema bodies, or full method signatures. Readers looking for "what does field X look like" are redirected to the Phase 4/6 doc.

## Source authority

Per [OQ-001 resolution](../OPEN-QUESTIONS.md#oq-001--source-version-mismatch-between-cloud-api-doc-v1113-and-dji_cloud-v115), **v1.15 `DJI_Cloud/` extracts are primary for every claim**. Where an annex references `Cloud-API-Doc/` v1.11 material, it is for drift cross-check or choreography narrative only. The [`dji_cloud_dock3/`](../../dji_cloud_dock3/) third-party repo is non-authoritative and is cited only in the Dock 3 annex where it materially corroborates Dock-3-specific behaviour not covered elsewhere.

## Related

- [`../device-properties/README.md`](../device-properties/README.md) — master property matrix; anchor for the property cross-cohort view.
- [`../mqtt/dock-to-cloud/README.md`](../mqtt/dock-to-cloud/README.md) — dock-path method catalog (197 methods).
- [`../mqtt/pilot-to-cloud/README.md`](../mqtt/pilot-to-cloud/README.md) — pilot-path method catalog (94 methods).
- [`../workflows/README.md`](../workflows/README.md) — 11 workflow docs.
- [`../SOURCES.md`](../SOURCES.md) — source authority ranking.
