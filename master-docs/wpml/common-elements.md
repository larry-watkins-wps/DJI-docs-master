# WPML common elements

Schemas shared between [`template.kml`](template-kml.md) and [`waylines.wpml`](waylines.md). See [`overview.md`](overview.md) for format, archive layout, and device support. This document covers:

1. Device info structs — `<wpml:droneInfo>`, `<wpml:payloadInfo>`, `<wpml:payloadParam>`.
2. Heading / turn / reroute structs — `<wpml:waypointHeadingParam>` / `<wpml:globalWaypointHeadingParam>`, `<wpml:waypointTurnParam>`, `<wpml:autoRerouteInfo>`.
3. Action machinery — `<wpml:actionGroup>` → `<wpml:actionTrigger>` → `<wpml:action>` → `<wpml:actionActuatorFuncParam>`.
4. 16 actuator functions — `takePhoto`, `startRecord`, `stopRecord`, `focus`, `zoom`, `customDirName`, `gimbalRotate`, `gimbalEvenlyRotate`, `rotateYaw`, `hover`, `accurateShoot` (deprecated), `orientedShoot`, `panoShot`, `recordPointCloud`, `megaphone`, `searchlight`.

"All" in product-support cells refers to the DJI WPML-wide cohort list: **M300 RTK, M350 RTK, M30/M30T, M3E/M3T/M3M, M3D/M3TD, M4E/M4T**. In-scope for this corpus: M3D/M3TD and M4E/M4T (which covers M4D/M4TD — see [overview §4.1](overview.md#41-labeling-inconsistency--m4em4t-vs-m4dm4td) for the labeling inconsistency note).

---

## 1. Overview of where these elements are used

| Element / struct | Used in | Scope |
|---|---|---|
| `<wpml:droneInfo>` | both files | inside `<wpml:missionConfig>` |
| `<wpml:payloadInfo>` | both files | inside `<wpml:missionConfig>` |
| `<wpml:payloadParam>` | template.kml | inside `<Folder>` |
| `<wpml:waypointHeadingParam>` | both files | per-waypoint |
| `<wpml:globalWaypointHeadingParam>` | template.kml | template-scoped |
| `<wpml:waypointTurnParam>` | both files | per-waypoint |
| `<wpml:autoRerouteInfo>` | both files | inside `<wpml:missionConfig>` |
| `<wpml:actionGroup>` | both files | inside `<Placemark>` |
| `<wpml:actionTrigger>` | both files | inside `<wpml:actionGroup>` |
| `<wpml:action>` | both files | inside `<wpml:actionGroup>` |
| `<wpml:actionActuatorFuncParam>` | both files | inside `<wpml:action>` |

Mission-level fields inside `<wpml:missionConfig>` (`wpml:flyToWaylineMode`, `wpml:finishAction`, `wpml:exitOnRCLost`, `wpml:executeRCLostAction`, `wpml:takeOffSecurityHeight`, `wpml:globalTransitionalSpeed`, `wpml:globalRTHHeight`) are also shared but are tabled in [`waylines.md §3`](waylines.md#3-mission-information--parent-wpmlmissionconfig). This doc does not restate them.

---

## 2. Mission configuration

See [`waylines.md §3`](waylines.md#3-mission-information--parent-wpmlmissionconfig) and [`template-kml.md §4`](template-kml.md#4-mission-information--parent-wpmlmissionconfig) for the mission-config field catalog. Shared structs referenced from both file types are documented below.

---

## 3. Shared structs

### 3.1 `<wpml:droneInfo>`

Identifies the drone model the wayline is authored for.

| Element | Name | Type | Value | Required | Product support |
|---|---|---|---|---|---|
| `wpml:droneEnumValue` | Drone type | int | See DJI's **Enumeration Values of Aircraft, RC and Dock** (`type` field). | yes | all |
| `wpml:droneSubEnumValue` | Drone sub-type | int | See DJI's `sub_type` field. | yes when `droneEnumValue` = `67` (M30/M30T) | all |

Enum values are maintained by DJI externally (Product Support page, "Enumeration Values of Aircraft, RC and Dock"). Corpus does not duplicate — a cloud that needs them should cite the live page.

### 3.2 `<wpml:payloadInfo>`

| Element | Name | Type | Value | Required | Product support |
|---|---|---|---|---|---|
| `wpml:payloadEnumValue` | Payload type | int | See `type` field in `type-subtype-gimbalindex` enum. | yes | all |
| `wpml:payloadPositionIndex` | Payload mount position | int | See `gimbalindex` field in `type-subtype-gimbalindex`. | yes | all |

### 3.3 `<wpml:payloadParam>`

Template-only (parent `<Folder>` in `template.kml`). Carries per-payload operational parameters.

| Element | Name | Type | Unit | Value | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:payloadPositionIndex` | Payload mount position | int | — | See `gimbalindex`. | yes | all |
| `wpml:focusMode` | Focus mode | enum | — | `firstPoint` / `custom` | — | M300 RTK, M350 RTK |
| `wpml:meteringMode` | Metering mode | enum | — | `average` / `spot` | — | M300 RTK, M350 RTK |
| `wpml:dewarpingEnable` | Dewarping | bool | — | `0` / `1` | — | M300 RTK, M350 RTK |
| `wpml:returnMode` | LiDAR return mode | enum | — | `singleReturnStrongest` / `dualReturn` / `tripleReturn` | — | M300 RTK, M350 RTK |
| `wpml:samplingRate` | Sampling rate | int | Hz | `60000` / `80000` / `120000` / `160000` / `180000` / `240000` | — | M300 RTK, M350 RTK |
| `wpml:scanningMode` | Scanning mode | enum | — | `repetitive` / `nonRepetitive` | — | M300 RTK, M350 RTK |
| `wpml:modelColoringEnable` | Model coloring | bool | — | `0` no coloring / `1` true colour | — | M300 RTK, M350 RTK |
| `wpml:imageFormat` | Image format list | enum_string | — | `wide` / `zoom` / `ir` / `narrow_band` / `visible`. Multi-lens combos: `<wpml:imageFormat>wide,ir</wpml:imageFormat>`. | yes | all |

In-scope devices (M3D/M3TD, M4E/M4T) only interact with `wpml:payloadPositionIndex` and `wpml:imageFormat` on this struct — the other fields are M300/M350-specific per DJI source.

### 3.4 `<wpml:waypointHeadingParam>` & `<wpml:globalWaypointHeadingParam>`

Same schema on both the per-waypoint form (`waypointHeadingParam`) and the global form (`globalWaypointHeadingParam`).

| Element | Name | Type | Unit | Value / enum | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:waypointHeadingMode` | Heading mode | enum | — | `followWayline` / `manually` / `fixed` / `smoothTransition` / `towardPOI` | yes | all |
| `wpml:waypointHeadingAngle` | Target yaw angle | float | ° | [-180, 180]. Transitions uniformly to the next waypoint's angle during the segment. | iff `waypointHeadingMode` = `smoothTransition` | all |
| `wpml:waypointPoiPoint` | Point of interest | lat,long,alt | °, °, m | Altitude may be set to `0`; Z-direction POI targeting is not supported. | iff `waypointHeadingMode` = `towardPOI` | all |
| `wpml:waypointHeadingPathMode` | Yaw rotation direction | enum | — | `clockwise` / `counterClockwise` / `followBadArc` (rotate via shortest arc) | yes | all |

**Heading mode semantics** (source-verbatim):

- `followWayline` — nose follows the course direction to the next waypoint.
- `manually` — user manually controls nose orientation during the segment.
- `fixed` — nose keeps the yaw angle of the aircraft leaving the waypoint after the waypoint action completes.
- `smoothTransition` — target yaw given by `wpml:waypointHeadingAngle`; transitions evenly to the next waypoint's target during the segment.
- `towardPOI` — nose faces `wpml:waypointPoiPoint` during the segment to the next waypoint.

*Inconsistency:* DJI lists the path-mode value `followBadArc` literally — "follow bad arc" reads like a translation artifact. Likely means "follow the shortest arc (even if bad/counterintuitive)". The source description does say "Rotation of the aircraft yaw angle along the shortest path." Treat `followBadArc` as "shortest-arc rotation".

### 3.5 `<wpml:waypointTurnParam>`

| Element | Name | Type | Unit | Value / enum | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:waypointTurnMode` | Turn mode | enum | — | `coordinateTurn` / `toPointAndStopWithDiscontinuityCurvature` / `toPointAndStopWithContinuityCurvature` / `toPointAndPassWithContinuityCurvature` | yes | all |
| `wpml:waypointTurnDampingDist` | Turn damping distance | float | m | (0, max segment length]. Distance before the waypoint at which to start turning. The wayline segment length must exceed the sum of damping distances of its two waypoints. | iff `waypointTurnMode` = `coordinateTurn`, or `waypointTurnMode` = `toPointAndPassWithContinuityCurvature` **and** `useStraightLine` = `1`. | all |

Semantics — see [`template-kml.md §6.2`](template-kml.md#62-turn-mode-semantics). DJI Pilot 2's "Turns before waypoint. Flies through." corresponds to `toPointAndPassWithContinuityCurvature` + `useStraightLine=1`.

### 3.6 `<wpml:autoRerouteInfo>`

Wayline reroute on obstruction. **New-generation feature** — only on M3D/M3TD and M4E/M4T.

| Element | Name | Type | Value | Required | Product support |
|---|---|---|---|---|---|
| `wpml:missionAutoRerouteMode` | Mission-phase auto-reroute | bool | `0` disable / `1` enable | yes | M3D/M3TD, M4E/M4T |
| `wpml:transitionalAutoRerouteMode` | Transitional-phase auto-reroute | bool | `0` disable / `1` enable | yes | M3D/M3TD, M4E/M4T |

The two flags separately control reroute behavior during the main mission phase (between waypoints) vs the transitional phase (take-off transition + return to home).

---

## 4. `<wpml:actionGroup>` → `<wpml:actionTrigger>` → `<wpml:action>`

Action groups are how the drone performs payload operations during a mission (take photo, rotate gimbal, start record, etc.). Structure:

```
<wpml:actionGroup>
├── <wpml:actionGroupId>
├── <wpml:actionGroupStartIndex>
├── <wpml:actionGroupEndIndex>
├── <wpml:actionGroupMode>
├── <wpml:actionTrigger> ... </wpml:actionTrigger>
└── <wpml:action>
    ├── <wpml:actionId>
    ├── <wpml:actionActuatorFunc>
    └── <wpml:actionActuatorFuncParam> ... </wpml:actionActuatorFuncParam>
</wpml:actionGroup>
```

Multiple `<wpml:action>` children can live inside one `<wpml:actionGroup>`.

### 4.1 `<wpml:actionGroup>` fields

| Element | Description | Type | Value | Required | Product support |
|---|---|---|---|---|---|
| `wpml:actionGroupId` | Unique within the `.kmz`; monotonic from 0 recommended. | int | [0, 65535] | yes | all |
| `wpml:actionGroupStartIndex` | First waypoint where the group takes effect. | int | [0, 65535] | yes | all |
| `wpml:actionGroupEndIndex` | Last waypoint where the group takes effect. Equal to `StartIndex` means active at that single waypoint only. Must be ≥ `StartIndex`. | int | [0, 65535] | yes | all |
| `wpml:actionGroupMode` | Action sequencing mode. | enum | `sequence` — actions executed sequentially. | yes | all |
| `wpml:actionTrigger` | When the group fires. See §4.2. | struct | — | — | all |
| `wpml:action` | Action list (1 or more). See §4.3. | struct | — | — | all |

### 4.2 `<wpml:actionTrigger>` fields

| Element | Description | Type | Unit | Value / enum | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:actionTriggerType` | Trigger kind. | enum | — | `reachPoint` / `betweenAdjacentPoints` / `multipleTiming` / `multipleDistance` | yes | all |
| `wpml:actionTriggerParam` | Trigger parameter. Interval time (`multipleTiming`) or distance (`multipleDistance`). | float | s or m | > 0 | — | all |

**Trigger semantics**:

- `reachPoint` — fires when the drone arrives at the waypoint.
- `betweenAdjacentPoints` — fires across the wayline segment. Intended to be used with `gimbalEvenlyRotate` (rotates gimbal pitch evenly across the segment).
- `multipleTiming` — fires at equal time intervals. Combine with `takePhoto` for time-lapse capture.
- `multipleDistance` — fires at equal distance intervals. Combine with `takePhoto` for equal-distance capture.

### 4.3 `<wpml:action>` fields

| Element | Description | Type | Value | Required | Product support |
|---|---|---|---|---|---|
| `wpml:actionId` | Unique within this action group; monotonic from 0 recommended. | int | [0, 65535] | yes | all |
| `wpml:actionActuatorFunc` | Actuator function. See §5 for each value's parameter schema. | enum | see §5 | yes | all |
| `wpml:actionActuatorFuncParam` | Actuator parameter struct. Shape depends on `actionActuatorFunc`. See §5. | struct | — | — | all |

**`actionActuatorFunc` enum (source list + extras)**:

DJI's v1.15 enum description lists these values explicitly:

```
takePhoto
startRecord
stopRecord
focus
zoom
customDirName
gimbalRotate
rotateYaw
hover
gimbalEvenlyRotate
accurateShoot      (deprecated; orientedShoot is recommended)
orientedShoot
panoShot           (M30/M30T, M3D/M3TD, M4E/M4T)
```

The source also provides `<wpml:actionActuatorFuncParam>` schemas for three additional actuator functions not in the enum description: `recordPointCloud`, `megaphone`, `searchlight`. Treat the enum in the source as informational — the authoritative list is the set of functions with documented `actionActuatorFuncParam` schemas (see §5).

---

## 5. Actuator function parameter schemas

Parent element in every case: `<wpml:actionActuatorFuncParam>`. Content varies by `<wpml:actionActuatorFunc>`.

"Product support" rows are copied from the DJI source verbatim; the translation to in-scope devices (M3D/M3TD, M4D/M4TD) follows the WPML `M4E/M4T` ≈ `M4D/M4TD` convention except where DJI explicitly distinguishes M4D/M4TD (e.g. `megaphone`, `searchlight`).

### 5.1 `takePhoto`

| Element | Description | Type | Value | Required | Product support |
|---|---|---|---|---|---|
| `wpml:payloadPositionIndex` | Mount position. | int | `gimbalindex` enum. | yes | all |
| `wpml:fileSuffix` | Suffix appended to the generated media filename. | string | — | yes | M300 RTK + M350 RTK (H20/H20T/H20N/H30/H30T), M30/M30T, M3E/M3T/M3M, M3D/M3TD, M4E/M4T |
| `wpml:payloadLensIndex` | Photo storage — which lens's image to store. Values: `zoom` / `wide` / `ir` / `narrow_band` / `visible` (sic — source has `visable`, typo). Multi-lens: `wide,ir,narrow_band`. | enum-string list | see left | yes | M30/M30T, M3D/M3TD, M4E/M4T |
| `wpml:useGlobalPayloadLensIndex` | `0` local / `1` global. | bool | `0` / `1` | yes | all |

### 5.2 `startRecord`

| Element | Description | Type | Value | Required | Product support |
|---|---|---|---|---|---|
| `wpml:payloadPositionIndex` | Mount position. | int | `gimbalindex` enum. | yes | M300 RTK, M30/M30T, M3E/M3T/M3M, M3D/M3TD, M4E/M4T |
| `wpml:fileSuffix` | Suffix. | string | — | yes | M300 RTK + M350 RTK (H20/H20T/H20N/H30/H30T), M30/M30T, M3E/M3T/M3M |
| `wpml:payloadLensIndex` | Video storage lens list. `zoom` / `wide` / `ir` / `narrow_band`. | enum-string list | — | yes | M30/M30T, M3D/M3TD, M4E/M4T |
| `wpml:useGlobalPayloadLensIndex` | `0` local / `1` global. | bool | `0` / `1` | yes | all |

### 5.3 `stopRecord`

| Element | Description | Type | Value | Required | Product support |
|---|---|---|---|---|---|
| `wpml:payloadPositionIndex` | Mount position. | int | `gimbalindex` enum. | yes | all |
| `wpml:payloadLensIndex` | Video storage lens list. `zoom` / `wide` / `ir` / `narrow_band`. | enum-string list | — | yes | M30/M30T |

Per the v1.15 source, only M30/M30T uses `payloadLensIndex` on `stopRecord`. Other cohorts rely on the corresponding `startRecord`'s lens list.

### 5.4 `focus`

| Element | Description | Type | Value | Required | Product support |
|---|---|---|---|---|---|
| `wpml:payloadPositionIndex` | Mount position. | int | `gimbalindex` enum. | yes | all |
| `wpml:isPointFocus` | Area (0) or point (1) focus. | bool | `0` / `1` | yes | all |
| `wpml:focusX` | Focal X-coordinate (normalized, 0 = left, 1 = right). Upper-left of focus region. | float | [0, 1] | yes | all |
| `wpml:focusY` | Focal Y-coordinate (normalized, 0 = top, 1 = bottom). | float | [0, 1] | yes | all |
| `wpml:focusRegionWidth` | Focus area width as proportion of image. | float | [0, 1] | iff `isPointFocus` = 0 | all |
| `wpml:focusRegionHeight` | Focus area height as proportion of image. | float | [0, 1] | iff `isPointFocus` = 0 | all |
| `wpml:isInfiniteFocus` | `1` = focus at infinity. | bool | `0` / `1` | yes | M3E/M3T/M3M, M3D/M3TD, M4E/M4T |

*Note:* The v1.15 source lists the `focusY` description as "X-axis (width) coordinates" — a copy-paste of the `focusX` description. Treat `focusY` as the Y-axis (height) coordinate.

### 5.5 `zoom`

| Element | Description | Type | Unit | Value | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:payloadPositionIndex` | Mount position. | int | — | `gimbalindex` enum. | yes | all |
| `wpml:focalLength` | Focal length. | float | mm | > 0 | yes | all |

### 5.6 `customDirName`

Create a new folder on the camera's storage for subsequent captures.

| Element | Description | Type | Value | Required | Product support |
|---|---|---|---|---|---|
| `wpml:payloadPositionIndex` | Mount position. | int | `gimbalindex` enum. | yes | all |
| `wpml:directoryName` | Folder name. | string | — | yes | all |

### 5.7 `gimbalRotate`

Rotate gimbal to a target attitude (pitch / roll / yaw).

| Element | Description | Type | Unit | Value / enum | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:payloadPositionIndex` | Mount position. | int | — | `gimbalindex` enum. | yes | all |
| `wpml:gimbalHeadingYawBase` | Yaw coordinate system. | enum | — | `north` (relative geographic north). | yes | all |
| `wpml:gimbalRotateMode` | Rotation mode. | enum | — | `absoluteAngle` (relative to north). | yes | all |
| `wpml:gimbalPitchRotateEnable` | Enable pitch rotation. | bool | — | `0` / `1` | yes | all |
| `wpml:gimbalPitchRotateAngle` | Pitch angle. Gimbal-model-dependent range. | float | ° | model-specific | yes | all |
| `wpml:gimbalRollRotateEnable` | Enable roll rotation. | bool | — | `0` / `1` | yes | all |
| `wpml:gimbalRollRotateAngle` | Roll angle. Model-specific range. | float | ° | model-specific | yes | all |
| `wpml:gimbalYawRotateEnable` | Enable yaw rotation. | bool | — | `0` / `1` | yes | all |
| `wpml:gimbalYawRotateAngle` | Yaw angle. Model-specific range. | float | ° | model-specific | yes | all |
| `wpml:gimbalRotateTimeEnable` | Enable fixed rotation-time. | bool | — | `0` / `1` | yes | all |
| `wpml:gimbalRotateTime` | Time to complete rotation. | float | s | — | yes | all |

### 5.8 `gimbalEvenlyRotate`

Rotate the gimbal pitch angle evenly across a wayline segment. Must use the `betweenAdjacentPoints` trigger.

| Element | Description | Type | Unit | Value | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:gimbalPitchRotateAngle` | Pitch angle. Model-specific range. | float | — | model-specific | yes | all |
| `wpml:payloadPositionIndex` | Mount position. | int | — | `gimbalindex` enum. | yes | all |

### 5.9 `rotateYaw`

Rotate the drone itself (not the gimbal) around the yaw axis.

| Element | Description | Type | Unit | Value | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:aircraftHeading` | Drone target yaw (true north reference). 0° = north, 90° = east, -90° = west, ±180° = south. | float | ° | [-180, 180] | yes | all |
| `wpml:aircraftPathMode` | Rotation direction. | enum | — | `clockwise` / `counterClockwise` | yes | M300 RTK, M350 RTK |

### 5.10 `hover`

| Element | Description | Type | Unit | Value | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:hoverTime` | Hover duration. | float | s | > 0 | yes | all |

### 5.11 `accurateShoot` — deprecated

AI Spot-Check action. DJI's note: *"For M30/M30T models, the drone firmware version after V06.01.10.02 is no longer maintained and upgrades the accurateShoot. orientedShoot is recommended."* New integrations should use `orientedShoot` (§5.12) instead.

Elements (product support: M300 RTK, M350 RTK, M30/M30T): `wpml:gimbalPitchRotateAngle` (float, ° ∈ [-120, 45]), `wpml:gimbalYawRotateAngle` (float, ° ∈ [-180, 180]), `wpml:focusX` (int, px ∈ (0, 960)), `wpml:focusY` (int, px ∈ (0, 720)), `wpml:focusRegionWidth` (int, px ∈ (0, 960)), `wpml:focusRegionHeight` (int, px ∈ (0, 720)), `wpml:focalLength` (float, mm > 0), `wpml:aircraftHeading` (float, ° ∈ [-180, 180]), `wpml:accurateFrameValid` (bool — `1` auto-target, `0` repeat by attitude), `wpml:payloadPositionIndex`, `wpml:payloadLensIndex`, `wpml:useGlobalPayloadLensIndex`, `wpml:targetAngle` (float, ° ∈ [0, 360]), `wpml:imageWidth` (int, px = 960), `wpml:imageHeight` (int, px = 720), `wpml:AFPos`, `wpml:gimbalPort` (int — 0 for M30/M30T), `wpml:accurateCameraType` (enum: `52` M30, `53` M30T, `42` H20, `43` H20T, `82` H30, `83` H30T), `wpml:accurateFilePath`, `wpml:accurateFileMD5`, `wpml:accurateFileSize`, `wpml:accurateFileSuffix`, `wpml:accurateCameraApertue` (sic — DJI typo for "Aperture"; int = real aperture × 100, M30/M30T only), `wpml:accurateCameraLuminance` (int, M30/M30T only), `wpml:accurateCameraShutterTime` (float s, M30/M30T only), `wpml:accurateCameraISO` (int, M30/M30T only).

In-scope devices should ignore this function; use `orientedShoot`.

### 5.12 `orientedShoot`

Take Photo (Fixed Angle). Supersedes `accurateShoot`. The large set of metadata fields (`orientedFilePath`, `orientedFileMD5`, etc.) is intended to be populated by the drone at capture time and written back into the KMZ; generators may leave them empty.

| Element | Description | Type | Unit | Value | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:gimbalPitchRotateAngle` | Pitch angle. Range varies by cohort. | float | ° | M30/M30T: [-120, 45]; M3E/M3T: [-90, 35]; M3D/M3TD, M4E/M4T: [-90, 30] | yes | M30/M30T, M3E/M3T, M3D/M3TD, M4E/M4T |
| `wpml:gimbalYawRotateAngle` | Yaw angle. For M3E/M3T / M3D/M3TD / M4E/M4T, this must align with `aircraftHeading`. | float | ° | [-180, 180] | yes | same |
| `wpml:focusX` | Target region center, X (px from upper-left). | int | px | (0, 960) | yes | same |
| `wpml:focusY` | Target region center, Y (px from upper-left). | int | px | (0, 720) | yes | same |
| `wpml:focusRegionWidth` | Target region width. | int | px | (0, 960) | yes | same |
| `wpml:focusRegionHeight` | Target region height. | int | px | (0, 720) | yes | same |
| `wpml:focalLength` | Zoom focal length. | float | mm | > 0 | yes | same |
| `wpml:aircraftHeading` | Drone target yaw (true-north reference). | float | ° | [-180, 180] | yes | same |
| `wpml:accurateFrameValid` | `1` auto-find target / `0` repeat by attitude. | bool | — | `0` / `1` | yes | same |
| `wpml:payloadPositionIndex` | Mount position. | int | — | `gimbalindex` enum. | yes | same |
| `wpml:payloadLensIndex` | Storage lens list (`zoom` / `wide` / `ir`, or comma-separated combo). | enum-string | — | — | yes | same |
| `wpml:useGlobalPayloadLensIndex` | Use global storage flag. | bool | — | `0` / `1` | yes | same |
| `wpml:targetAngle` | Target-box rotation angle. | float | ° | [0, 360] | yes | same |
| `wpml:actionUUID` | Action UUID written to the captured image for association. | string | — | — | yes | same |
| `wpml:imageWidth` | Image width. | int | px | `960` | yes | same |
| `wpml:imageHeight` | Image height. | int | px | `720` | yes | same |
| `wpml:AFPos` | AF motor location. | int | — | — | yes | same |
| `wpml:gimbalPort` | Gimbal port number (`0` for in-scope cohorts). | int | — | `0` | yes | same |
| `wpml:orientedCameraType` | Camera type enum. | int | — | `52` M30 dual-light / `53` M30T triple-light. (M3D/M3TD / M4E/M4T-specific values are left blank by DJI — runtime-populated.) | yes | same |
| `wpml:orientedFilePath` | Image file path (post-capture). | string | — | — | yes | same |
| `wpml:orientedFileMD5` | Image file MD5 (post-capture). | string | — | — | yes | same |
| `wpml:orientedFileSize` | Image file size. | int | bytes | — | yes | same |
| `wpml:orientedFileSuffix` | Image file suffix. | string | — | — | yes | same |
| `wpml:orientedCameraApertue` | Aperture × 100. DJI typo (`Apertue` ≠ `Aperture`). | int | — | — | yes | same |
| `wpml:orientedCameraLuminance` | Environment luminance. | int | — | — | yes | same |
| `wpml:orientedCameraShutterTime` | Shutter time. | float | s | — | yes | same |
| `wpml:orientedCameraISO` | ISO. | int | — | — | yes | same |
| `wpml:orientedPhotoMode` | Capture mode. | enum-string | — | `normalPhoto` / `lowLightSmartShooting` | yes | same |

### 5.13 `panoShot`

Panorama capture.

| Element | Description | Type | Unit | Value / enum | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:payloadPositionIndex` | Mount position. | int | — | `gimbalindex` enum. | yes | M30/M30T |
| `wpml:payloadLensIndex` | Storage lens list. | enum-string list | — | `zoom` / `wide` / `ir` / `narrow_band` / `visible` | yes | M30/M30T |
| `wpml:useGlobalPayloadLensIndex` | Use global storage flag. | bool | — | `0` / `1` | yes | M30/M30T, M3E/M3T |
| `wpml:panoShotSubMode` | Panorama mode. | string | — | `panoShot_360` | yes | M30/M30T, M3D/M3TD, M4E/M4T |

*Source inconsistency:* the cohort list varies row by row. DJI lists `panoShotSubMode` as supported on `M30/M30T, M3D/M3TD, M4E/M4T` but lists `payloadPositionIndex` on only `M30/M30T`. Intended behavior is likely that all in-scope cohorts accept all fields; the M30-only labels on the position/lens fields appear to be extract defects rather than semantic restrictions. Implementers should test on hardware or consult DJI.

### 5.14 `recordPointCloud`

LiDAR point-cloud capture. M300 RTK / M350 RTK only.

| Element | Description | Type | Value | Required | Product support |
|---|---|---|---|---|---|
| `wpml:payloadPositionIndex` | Mount position. | int | `gimbalindex` enum. | yes | M300 RTK, M350 RTK |
| `wpml:recordPointCloudOperate` | Control. | string | `startRecord` / `pauseRecord` / `resumeRecord` / `stopRecord` | yes | M300 RTK, M350 RTK |

Not relevant to M3D/M3TD or M4D/M4TD.

### 5.15 `megaphone`

**M4D/M4TD only.** DJI's source uses the literal label `M4D/M4TD` on every row of this section — one of only two actuator functions that explicitly distinguish M4D/M4TD from the broader M4E/M4T cohort (the other is `searchlight`). Takes a pre-recorded audio file from `/wpmz/res/audio/` inside the KMZ archive.

| Element | Description | Type | Unit | Value | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:payloadPositionIndex` | Mount position. `0` = position 1, `1` = position 2, `2` = position 3. Interpretation varies by aircraft — see DJI source note below. | int | — | `0` / `1` / `2` | yes | M4D/M4TD |
| `wpml:actionUUID` | Action UUID. | string | — | — | yes | M4D/M4TD |
| `wpml:megaphoneOperateType` | Playback control. `0` start, `1` stop. | int | — | `0` / `1` | yes | M4D/M4TD |
| `wpml:megaphoneOperateVolume` | Volume. | int | — | [0, 100] | yes | M4D/M4TD |
| `wpml:megaphoneOperateLoop` | Single-track loop playback. | bool | — | `0` off / `1` on | yes | M4D/M4TD |
| `wpml:megaphoneOperateFilePath` | Audio file path inside KMZ. Example: `/wpmz/res/audio/71b4cf0504a7b899.opus`. | string | — | — | yes | M4D/M4TD |
| `wpml:megaphoneFileName` | Audio filename inside KMZ. Example: `71b4cf0504a7b899.opus`. | string | — | — | yes | M4D/M4TD |
| `wpml:megaphoneFileOriginalName` | Display name shown during playback. Example: `Megaphone Audio.mp3`. | string | — | — | yes | M4D/M4TD |
| `wpml:megaphoneFileMd5` | MD5 of the audio file. | string | — | — | yes | M4D/M4TD |
| `wpml:megaphoneFileBitrate` | Compression bitrate enum. `1` = 8000, `2` = 16000, `3` = 24000, `4` = 32000, `5` = 48000, `6` = 64000. **Currently only `4` (32000) is supported.** | int | — | `1..6` | yes | M4D/M4TD |

**Mount-position semantics** (from the DJI source, verbatim):

- `0` = Mount position of 1. M300 RTK / M350 RTK: front-left of the drone; other models: main gimbal.
- `1` = Mount position of 2. M300 RTK / M350 RTK: front-right of the drone.
- `2` = Mount position of 3. M300 RTK / M350 RTK: top of the drone.

The megaphone is a PSDK-style payload; it rides on the aircraft's accessory rail. Audio files are Opus (per the example path).

*Source typo*: `wpml:megaphoneOperateLoop` literal label in the v1.15 extract starts with a Chinese character (`是Single Track Loop Playback`). The intended English label is `Single Track Loop Playback` — the `是` (Chinese for "Is") is a translation artifact that DJI didn't strip.

### 5.16 `searchlight`

**M4D/M4TD only.** Attached searchlight control.

| Element | Description | Type | Unit | Value | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:payloadPositionIndex` | Mount position. Same 0 / 1 / 2 semantics as `megaphone` §5.15. | int | — | `0` / `1` / `2` | yes | M4D/M4TD |
| `wpml:actionUUID` | Action UUID. | string | — | — | **no** | M4D/M4TD |
| `wpml:searchlightOperateType` | Operation. `0` off, `1` illuminate, `2` flash. | int | — | `0` / `1` / `2` | yes | M4D/M4TD |
| `wpml:searchlightBrightness` | Brightness. | int | — | [0, 100] | yes | M4D/M4TD |

Note the `actionUUID` is the only actuator-parameter `actionUUID` across all 16 functions marked **not required** in the v1.15 source.

---

## 6. DJI-source inconsistencies noted

Carry into Phase 10 device annexes / Phase 9 wayline workflow authoring; none rise to OQ level:

- **`actionActuatorFunc` enum description is incomplete** — lists 13 values but three additional functions (`recordPointCloud`, `megaphone`, `searchlight`) have their own parameter sections. Authoritative list is the 16 actuator function sections.
- **`wpml:focusY` description is a copy-paste of `focusX`** — says "X-axis (width) coordinates" in both. `focusY` is the Y-axis coordinate.
- **`wpml:waypointHeadingPathMode` value `followBadArc`** — literal source text; likely a rough translation of "follow the shortest arc". Description reads "Rotation of the aircraft yaw angle along the shortest path."
- **`wpml:megaphoneOperateLoop` label starts with Chinese character `是`** — unstripped translation artifact. Intended label: `Single Track Loop Playback`.
- **`wpml:accurateCameraApertue` / `wpml:orientedCameraApertue`** — DJI typo. Element name is `Apertue` across both `accurateShoot` and `orientedShoot` — implementers must send exactly that misspelling.
- **`payloadLensIndex` value `visable`** — DJI typo in the source (should be `visible`). Consult the live site before committing an implementation — DJI may have fixed this in a refresh.
- **`panoShot` cohort lists are inconsistent** — `payloadPositionIndex` labeled M30/M30T only, `panoShotSubMode` labeled M30/M30T + M3D/M3TD + M4E/M4T. Likely the M30-only fields are extract defects; intended behavior is that in-scope cohorts accept all fields.
- **`accurateShoot` is listed with its own section but also marked deprecated**. The `actionActuatorFunc` enum still includes it without the deprecation note; generators authoring for current cohorts should emit `orientedShoot` instead.
- **WPML namespace version** — `xmlns:wpml="http://www.dji.com/wpmz/1.0.2"` across every v1.15 sample. The `1.0.2` version-in-namespace is stable across template-kml, waylines, and common-elements samples; no drift observed.

---

## 7. Source provenance

| Source | Role |
|---|---|
| [`DJI_Cloud/DJI_CloudAPI_WPML-Common-Elements.txt`](../../DJI_Cloud/DJI_CloudAPI_WPML-Common-Elements.txt) | v1.15 primary — 2,561 lines, full catalog of shared structs and 16 actuator functions. |
| [`DJI_Cloud/DJI_CloudAPI_WPML-Template-KML.txt`](../../DJI_Cloud/DJI_CloudAPI_WPML-Template-KML.txt) | v1.15 primary — template-file context; `<wpml:payloadParam>` on `<Folder>`. |
| [`DJI_Cloud/DJI_CloudAPI_WPML-Waylines.txt`](../../DJI_Cloud/DJI_CloudAPI_WPML-Waylines.txt) | v1.15 primary — execution-file context; action-group examples. |
