# WPML — DJI wayline file format

**WPML** (WayPoint Markup Language) is DJI's open file format for drone wayline missions. It is an XML dialect that extends KML (Keyhole Markup Language), packaged as a ZIP archive with a `.kmz` extension.

WPML is how a wayline mission reaches the drone. For cloud workflows, the wayline file:

- Is uploaded by the operator to the cloud (or produced by DJI Pilot 2 / FlightHub 2 locally).
- Is delivered to the dock via the HTTPS wayline endpoints cataloged in [`../http/wayline/`](../http/wayline/).
- Is referenced by the dock when scheduled for execution via MQTT `flighttask_prepare` / `flighttask_execute` (see [`../mqtt/dock-to-cloud/services/flighttask_prepare.md`](../mqtt/dock-to-cloud/services/flighttask_prepare.md)).

A DJI-Cloud-compatible server must therefore accept, store, and relay these files byte-faithfully. Understanding their internal shape is optional — a pass-through implementation can treat the KMZ as an opaque blob — but any server that validates, templates, or transforms waylines needs the schema.

---

## 1. Name and extension

- **Format name**: WPML (WayPoint Markup Language).
- **Outer archive**: `.kmz` — a ZIP-compressed archive, one per mission. The archive's filename (minus extension) is the **route name** (e.g. `new_waypoints.kmz` → route name `new_waypoints`).
- **XML namespace**: `xmlns:wpml="http://www.dji.com/wpmz/1.0.2"` — note the namespace authority uses `wpmz` (not `wpml`). DJI versions the namespace inline (`1.0.2` as of v1.15); a mismatched namespace version may not parse on a given drone model.
- **Inner files**: `.kml` for the template file and `.wpml` for the executable-waylines file — see §2.

**Inconsistency flag**: The DJI overview page calls WPML a "route file format standard" with extension `.kmz`, then describes the inner execution file with extension `.wpml`. The `.wpml` extension applies only to the inner `waylines.wpml`; the archive itself is `.kmz`. All external references to "a WPML file" mean the `.kmz` archive.

---

## 2. Archive contents

A standard WPML archive, after `unzip`, has this layout:

```
<route-name>.kmz  (unzip →)
├── wpmz/
│   ├── template.kml       ← the "template file" — business parameters
│   ├── waylines.wpml      ← the "execution file" — detailed drone commands
│   └── res/               ← auxiliary resources (optional)
│       └── ...            ← e.g. AI Spot-Check reference photos
```

*Note: The `wpmz/` directory is implied by DJI's namespace and by actual Pilot 2 output; the v1.15 overview page does not describe the archive's internal directory layout explicitly. The same page says "its file structure is as follows" but the illustration that follows is missing from the v1.15 extract — verify against the live site if the layout matters for your implementation.*

### 2.1 `template.kml` — the template file

Defines the **business parameters** of the mission — what kind of route (waypoint / mapping / oblique / linear), survey area polygons, overlap rate, flight speed, payload, etc. DJI Pilot 2 / FlightHub 2 / third-party software reads the template to generate the executable-waylines file.

Template fields are documented in [`template-kml.md`](template-kml.md).

### 2.2 `waylines.wpml` — the execution file

Defines the **concrete drone commands** — waypoint coordinates, altitude, heading, action groups, and actuator functions. One `Folder` element per executable wayline. Generators (Pilot 2, FlightHub 2, or the user's own templating) read `template.kml` parameters and produce this file.

Execution fields are documented in [`waylines.md`](waylines.md).

**Multi-wayline templates**: When a template generates multiple waylines (e.g. `mapping3d` produces 5 routes per DJI's convention), `waylines.wpml` contains 5 `Folder` elements.

### 2.3 `res/` — resources

Auxiliary files referenced by wayline actions — typically reference images for AI Spot-Check (`accurateShoot`) and PSDK-widget resources. Nothing to parse server-side; these are passed through to the drone.

---

## 3. Common vs per-file fields

Elements fall into three groups:

| Group | Where | Documented in |
|---|---|---|
| Template-only | `template.kml` | [`template-kml.md`](template-kml.md) |
| Execution-only | `waylines.wpml` | [`waylines.md`](waylines.md) |
| Shared (template + execution) | both files | [`common-elements.md`](common-elements.md) |

The shared/common-elements doc carries the large schemas that appear in both files: `<wpml:droneInfo>`, `<wpml:payloadInfo>`, `<wpml:payloadParam>`, `<wpml:waypointHeadingParam>`, `<wpml:waypointTurnParam>`, `<wpml:actionGroup>`, `<wpml:actionTrigger>`, `<wpml:action>`, and the 15+ actuator functions (`takePhoto`, `gimbalRotate`, `orientedShoot`, etc.).

---

## 4. Device support

The WPML source lists the following drone cohorts in every `Product Support` column: **M300 RTK, M350 RTK, M30/M30T, M3E/M3T/M3M, M3D/M3TD, M4E/M4T**.

In-scope cohorts for this corpus:

- **M3D / M3TD** — covered directly under the M3D/M3TD cohort label.
- **M4D / M4TD** — covered under the M4E/M4T cohort label (see inconsistency note).

Out-of-scope cohorts listed by DJI for enum completeness only: M300 RTK, M350 RTK, M30/M30T, M3E/M3T/M3M.

### 4.1 Labeling inconsistency — M4E/M4T vs M4D/M4TD

The v1.15 WPML sources label all Matrice 4 Enterprise cohorts as **M4E/M4T** with no separate entry for M4D/M4TD. The Phase 6 device-property sources, however, document **M4D/M4TD** as a dock-pairing variant of the Matrice 4 Enterprise platform — same drone, different deployment pattern (physically installed in a dock).

Treat every WPML "M4E/M4T" line as also applying to M4D/M4TD. The wayline file travels with the mission and the Matrice 4 aircraft — regardless of whether a human operator or a dock launches it — and DJI has never published separate WPML features for M4D/M4TD.

### 4.2 Per-cohort feature gates

A few WPML elements are gated to newer cohorts only. In-scope examples:

| Element | Gated to | Meaning |
|---|---|---|
| `wpml:autoRerouteInfo` | M3D/M3TD, M4E/M4T | Wayline reroute on obstruction — not in older cohorts. |
| `wpml:isRisky` (on Placemark) | M30/M30T, M3D/M3TD, M4E/M4T | Flag a waypoint as risky for operator review. |
| `wpml:useStraightLine` | M30/M30T, M3E/M3T/M3M, M3D/M3TD, M4E/M4T | Curve-through vs stop-at-point turn override. |
| `wpml:quickOrthoMappingEnable` | M4E only (per source) | Orthophoto smart-oblique shortcut. |
| `wpml:realTimeFollowSurface` (executeHeightMode) | M3E/M3T/M3M only | Real-time follow-surface altitude mode. |

Non-exhaustive — see per-element `Product Support` columns in [`template-kml.md`](template-kml.md), [`waylines.md`](waylines.md), and [`common-elements.md`](common-elements.md) for full gating.

### 4.3 Existing route change

For existing M300 RTK route files in older formats, DJI's guidance is to import into a newer DJI Pilot 2 and re-save to upgrade to WPML. DJI does not ship a conversion library; developers needing one must implement against the WPML spec directly.

---

## 5. File-read rules

- **Filename casing matters**: `template.kml`, `waylines.wpml`, `res/` — DJI warns that misnamed files or folders may cause the route to fail to read.
- **Namespace version matters**: `xmlns:wpml="http://www.dji.com/wpmz/1.0.2"` is the v1.15 namespace. Mismatches may not parse on some cohorts.
- **Monotonic IDs**: `wpml:templateId`, `wpml:waylineId`, and `wpml:index` are advised to start at `0` and increment monotonically within the archive.

---

## 6. Related corpus docs

- [`../http/wayline/`](../http/wayline/) — HTTP endpoints for wayline upload / download / list / favorites. A cloud accepts a KMZ file here.
- [`../mqtt/dock-to-cloud/services/flighttask_prepare.md`](../mqtt/dock-to-cloud/services/flighttask_prepare.md) — how the cloud schedules a wayline mission for execution on the dock.
- [`../mqtt/dock-to-cloud/services/flighttask_execute.md`](../mqtt/dock-to-cloud/services/flighttask_execute.md) — execution trigger.
- [`../mqtt/dock-to-cloud/events/flighttask_progress.md`](../mqtt/dock-to-cloud/events/flighttask_progress.md) — in-flight progress stream.

Workflow-level choreography (pairing KMZ upload → schedule → execute → progress) is deferred to Phase 9 `workflows/wayline-upload-and-execution.md`.

---

## 7. Source provenance

| Source | Role |
|---|---|
| [`DJI_Cloud/DJI_CloudAPI_WPML-Overview.txt`](../../DJI_Cloud/DJI_CloudAPI_WPML-Overview.txt) | v1.15 primary — WPML overview, archive layout, file-read rules. |
| [`DJI_Cloud/DJI_CloudAPI_WPML-Template-KML.txt`](../../DJI_Cloud/DJI_CloudAPI_WPML-Template-KML.txt) | v1.15 primary — template file element catalog ([`template-kml.md`](template-kml.md)). |
| [`DJI_Cloud/DJI_CloudAPI_WPML-Waylines.txt`](../../DJI_Cloud/DJI_CloudAPI_WPML-Waylines.txt) | v1.15 primary — execution file element catalog ([`waylines.md`](waylines.md)). |
| [`DJI_Cloud/DJI_CloudAPI_WPML-Common-Elements.txt`](../../DJI_Cloud/DJI_CloudAPI_WPML-Common-Elements.txt) | v1.15 primary — shared schemas ([`common-elements.md`](common-elements.md)). |

v1.11 `Cloud-API-Doc/` has an older WPML reference at [`Cloud-API-Doc/docs/en/60.api-reference/00.dji-wpml/`](../../Cloud-API-Doc/docs/en/60.api-reference/00.dji-wpml/) — retained in-repo per [OQ-001](../OPEN-QUESTIONS.md#oq-001--source-version-mismatch-between-cloud-api-doc-v1113-and-dji_cloud-v115) for drift cross-check only; v1.15 is authoritative.
