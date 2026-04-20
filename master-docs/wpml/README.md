# `wpml/` — WPML wayline file format reference

**WPML** (WayPoint Markup Language) is DJI's open wayline file format — an XML dialect extending KML, packaged as a `.kmz` ZIP archive. This directory covers the file format itself; transport-layer mechanics (uploading a wayline via HTTPS, scheduling it via MQTT) are in [`../http/wayline/`](../http/wayline/) and [`../mqtt/dock-to-cloud/`](../mqtt/dock-to-cloud/).

See **[`overview.md`](overview.md)** first — it introduces the format, the archive layout, and device-support conventions.

## Docs

| Doc | Covers |
|---|---|
| [`overview.md`](overview.md) | WPML format, `.kmz` archive contents (`template.kml` + `waylines.wpml` + `res/`), device support (M3D/M3TD/M4D/M4TD), labeling inconsistencies, existing-route upgrade path. |
| [`template-kml.md`](template-kml.md) | `template.kml` — business parameters. Four template types (`waypoint` / `mapping2d` / `mapping3d` / `mappingStrip`), coordinate/heightMode parameters, overlap rates, mapping-heading params. |
| [`waylines.md`](waylines.md) | `waylines.wpml` — executable commands. Mission config, Folder-per-wayline, Placemark-per-waypoint, `wpml:executeHeightMode`. |
| [`common-elements.md`](common-elements.md) | Shared schemas — `<wpml:droneInfo>` / `<wpml:payloadInfo>` / `<wpml:payloadParam>` / heading & turn params / reroute / action chain + **16 actuator functions** (`takePhoto`, `gimbalRotate`, `orientedShoot`, `panoShot`, `megaphone` (M4D/M4TD), `searchlight` (M4D/M4TD), etc.). |

## Scope

- Captures DJI's v1.15 WPML spec per [OQ-001](../OPEN-QUESTIONS.md#oq-001--source-version-mismatch-between-cloud-api-doc-v1113-and-dji_cloud-v115).
- Focuses on the two in-scope cohorts — **M3D/M3TD** and **M4D/M4TD** (under the WPML "M4E/M4T" cohort label; see [overview §4.1](overview.md#41-labeling-inconsistency--m4em4t-vs-m4dm4td)).
- Out-of-scope cohorts (M300 RTK, M350 RTK, M30/M30T, M3E/M3T/M3M) are documented in the product-support cells for enum completeness only.
- DJI-source inconsistencies are flagged inline in each doc's `§N — DJI-source inconsistencies` section.

## Related

- [`../http/wayline/`](../http/wayline/) — wayline upload / download / list HTTPS endpoints.
- [`../mqtt/dock-to-cloud/services/flighttask_prepare.md`](../mqtt/dock-to-cloud/services/flighttask_prepare.md) — cloud-initiated wayline scheduling.
- [`../mqtt/dock-to-cloud/services/flighttask_execute.md`](../mqtt/dock-to-cloud/services/flighttask_execute.md) — execution trigger.
- [`../mqtt/dock-to-cloud/events/flighttask_progress.md`](../mqtt/dock-to-cloud/events/flighttask_progress.md) — in-flight progress stream.
- End-to-end choreography is deferred to Phase 9 `workflows/wayline-upload-and-execution.md`.
