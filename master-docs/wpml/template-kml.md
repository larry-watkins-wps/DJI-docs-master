# `template.kml` — the template file

The `template.kml` file inside a WPML `.kmz` archive defines the **business parameters** of a mission — what kind of flight (waypoint / mapping / oblique / linear strip), the survey area polygon, overlap rate, payload, global flight speed, etc. DJI Pilot 2 / FlightHub 2 / third-party templating software reads this file and, combined with a path-generation algorithm, produces the executable [`waylines.wpml`](waylines.md).

See [`overview.md`](overview.md) for the WPML format, archive layout, and device support. Shared schemas (`<wpml:missionConfig>`, `<wpml:droneInfo>`, `<wpml:payloadInfo>`, action groups, etc.) are in [`common-elements.md`](common-elements.md).

---

## 1. File structure

Three top-level parts inside the root `<Document>`:

1. **Create information** — author, creation time, update time.
2. **Mission information** — `<wpml:missionConfig>`, the global mission parameters (same structure as in [`waylines.wpml`](waylines.md)).
3. **Template information** — one or more `<Folder>` elements, each declaring one template instance. Elements vary by `<wpml:templateType>`:
   - `waypoint` — discrete waypoint flight (each `<Placemark>` is a concrete waypoint).
   - `mapping2d` — 2D area-mapping aerial template (survey polygon + overlap + flight parameters).
   - `mapping3d` — 3D oblique-photography template (survey polygon + tilt angles; produces 5 executable waylines).
   - `mappingStrip` — strip/linear flight template (LineString with lateral extension).

---

## 2. Complete example (waypoint template)

Verbatim from the v1.15 source:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:wpml="http://www.dji.com/wpmz/1.0.2">
<Document>

<!-- Step 1: Implement File Creation Information -->
<wpml:author>Name</wpml:author>
<wpml:createTime>1637600807044</wpml:createTime>
<wpml:updateTime>1637600875837</wpml:updateTime>

<!-- Step 2: Setup Mission Configuration -->
<wpml:missionConfig>
<wpml:flyToWaylineMode>safely</wpml:flyToWaylineMode>
<wpml:finishAction>goHome</wpml:finishAction>
<wpml:exitOnRCLost>goContinue</wpml:exitOnRCLost>
<wpml:executeRCLostAction>hover</wpml:executeRCLostAction>
<wpml:takeOffSecurityHeight>20</wpml:takeOffSecurityHeight>
<wpml:takeOffRefPoint>23.98057,115.987663,100</wpml:takeOffRefPoint>
<wpml:takeOffRefPointAGLHeight>35</wpml:takeOffRefPointAGLHeight>
<wpml:globalTransitionalSpeed>8</wpml:globalTransitionalSpeed>
<wpml:droneInfo>
<wpml:droneEnumValue>67</wpml:droneEnumValue>
<wpml:droneSubEnumValue>0</wpml:droneSubEnumValue>
</wpml:droneInfo>
<wpml:payloadInfo>
<wpml:payloadEnumValue>52</wpml:payloadEnumValue>
<wpml:payloadPositionIndex>0</wpml:payloadPositionIndex>
</wpml:payloadInfo>
</wpml:missionConfig>

<!-- Step 3: Setup A Folder for Waypoint Template -->
<Folder>
<wpml:templateType>waypoint</wpml:templateType>
<wpml:templateId>0</wpml:templateId>
<wpml:waylineCoordinateSysParam>
<wpml:coordinateMode>WGS84</wpml:coordinateMode>
<wpml:heightMode>EGM96</wpml:heightMode>
<wpml:globalShootHeight>50</wpml:globalShootHeight>
<wpml:positioningType>GPS</wpml:positioningType>
<wpml:surfaceFollowModeEnable>1</wpml:surfaceFollowModeEnable>
<wpml:surfaceRelativeHeight>100</wpml:surfaceRelativeHeight>
</wpml:waylineCoordinateSysParam>
<wpml:autoFlightSpeed>7</wpml:autoFlightSpeed>
<wpml:gimbalPitchMode>usePointSetting</wpml:gimbalPitchMode>
<wpml:globalWaypointHeadingParam>
<wpml:waypointHeadingMode>followWayline</wpml:waypointHeadingMode>
<wpml:waypointHeadingAngle>45</wpml:waypointHeadingAngle>
<wpml:waypointPoiPoint>24.323345,116.324532,31.000000</wpml:waypointPoiPoint>
<wpml:waypointHeadingPathMode>clockwise</wpml:waypointHeadingPathMode>
</wpml:globalWaypointHeadingParam>
<wpml:globalWaypointTurnMode>toPointAndStopWithDiscontinuityCurvature</wpml:globalWaypointTurnMode>
<wpml:globalUseStraightLine>0</wpml:globalUseStraightLine>
<Placemark>
<Point>
<!-- Fill longitude and latitude here -->
<coordinates>
longitude,latitude
</coordinates>
</Point>
<wpml:index>0</wpml:index>
<wpml:ellipsoidHeight>90.2</wpml:ellipsoidHeight>
<wpml:height>100</wpml:height>
<wpml:useGlobalHeight>1</wpml:useGlobalHeight>
<wpml:useGlobalSpeed>1</wpml:useGlobalSpeed>
<wpml:useGlobalHeadingParam>1</wpml:useGlobalHeadingParam>
<wpml:useGlobalTurnParam>1</wpml:useGlobalTurnParam>
<wpml:gimbalPitchAngle>0</wpml:gimbalPitchAngle>
</Placemark>
<!-- ...additional Placemarks... -->
</Folder>
</Document>
</kml>
```

---

## 3. Create information — parent `<Document>`

| Element | Description | Type | Unit | Required | Product support |
|---|---|---|---|---|---|
| `wpml:author` | Author name. | string | — | — | all |
| `wpml:createTime` | File creation time (Unix timestamp, ms). | int | ms | — | all |
| `wpml:updateTime` | File update time (Unix timestamp, ms). | int | ms | — | all |

"All" here means **M300 RTK, M350 RTK, M30/M30T, M3E/M3T/M3M, M3D/M3TD, M4E/M4T** in the DJI source — the same product-support list on every WPML element.

---

## 4. Mission information — parent `<wpml:missionConfig>`

Shared with `waylines.wpml`. Schema catalog in [`common-elements.md` §2](common-elements.md#2-mission-configuration). Elements DJI called out specifically as part of template.kml:

| Element | Type | Unit | Value / enum | Required | Product support |
|---|---|---|---|---|---|
| `wpml:flyToWaylineMode` | enum | — | `safely` / `pointToPoint` | yes | all |
| `wpml:finishAction` | enum | — | `goHome` / `noAction` / `autoLand` / `gotoFirstWaypoint` | yes | all |
| `wpml:exitOnRCLost` | enum | — | `goContinue` / `executeLostAction` | yes | all |
| `wpml:executeRCLostAction` | enum | — | `goBack` / `landing` / `hover` | iff `exitOnRCLost` = `executeLostAction` | all |
| `wpml:takeOffSecurityHeight` | float | m | RC: [1.2, 1500]; Dock: [8, 1500]. Relative to take-off point. | yes | all |
| `wpml:globalTransitionalSpeed` | float | m/s | > 0 | yes | all |
| `wpml:takeOffRefPoint` | float,float,float | °, °, m | Reference take-off point `<latitude,longitude,altitude>`. Planning aid only — actual takeoff point wins at execution. Altitude is ellipsoid. | — | M30/M30T, M3E/M3T/M3M, M3D/M3TD, M4E/M4T |
| `wpml:takeOffRefPointAGLHeight` | float | m | AGL altitude of the reference take-off point, corresponding to the ellipsoid height above. | — | M30/M30T, M3E/M3T/M3M, M3D/M3TD, M4E/M4T |
| `wpml:droneInfo` | struct | — | See [`common-elements.md §3.1`](common-elements.md#31-wpmldroneinfo) | — | all |
| `wpml:payloadInfo` | struct | — | See [`common-elements.md §3.2`](common-elements.md#32-wpmlpayloadinfo) | — | all |
| `wpml:autoRerouteInfo` | struct | — | See [`common-elements.md §3.6`](common-elements.md#36-wpmlautorerouteinfo) | — | **M3D/M3TD, M4E/M4T only** |

Enum semantics for `flyToWaylineMode`, `finishAction`, `exitOnRCLost`, `executeRCLostAction` are identical across template.kml and waylines.wpml — full descriptions in [`waylines.md §3`](waylines.md#3-mission-information--parent-wpmlmissionconfig).

---

## 5. Template common elements — parent `<Folder>`

Elements that appear on every `<Folder>` regardless of `wpml:templateType`:

| Element | Description | Type | Unit | Value / enum | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:templateType` | Predefined template type. | enum | — | `waypoint` / `mapping2d` / `mapping3d` / `mappingStrip` | yes | all |
| `wpml:templateId` | Template ID — unique per `.kmz`; monotonic from 0 recommended. Associates this template `<Folder>` with generated `<Folder>`(s) in `waylines.wpml`. | int | — | [0, 65535] | yes | all |
| `wpml:autoFlightSpeed` | Global target flight speed for waylines generated from this template. | float | m/s | (0, drone max speed] | yes | all |
| `wpml:waylineCoordinateSysParam` | Coordinate system parameters. See §9. | struct | — | — | — | all |
| `wpml:payloadParam` | Payload parameters. See [`common-elements.md §3.3`](common-elements.md#33-wpmlpayloadparam). | struct | — | — | — | all |

Per-template-type elements are in §6–§8 below.

---

## 6. Waypoint Flight template — `wpml:templateType = waypoint`

Each `<Placemark>` is a concrete waypoint (latitude/longitude/altitude/heading/action).

### 6.1 Template-level elements

| Element | Description | Type | Unit | Value / enum | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:globalWaypointTurnMode` | Global turn type. Local `wpml:waypointTurnParam` overrides. | enum | — | `coordinateTurn` / `toPointAndStopWithDiscontinuityCurvature` / `toPointAndStopWithContinuityCurvature` / `toPointAndPassWithContinuityCurvature` | yes | all |
| `wpml:globalUseStraightLine` | Whether global flight segments fit straight lines. | bool | — | `0` curved / `1` as-close-to-straight-line-as-possible | iff `globalWaypointTurnMode` = `toPointAndStopWithContinuityCurvature` or `toPointAndPassWithContinuityCurvature`. Local override allowed. | M30/M30T, M3E/M3T/M3M, M3D/M3TD, M4E/M4T |
| `wpml:gimbalPitchMode` | Gimbal-pitch control model. `manual` keeps the pitch angle from the last waypoint; `usePointSetting` transitions evenly toward the next waypoint's pitch. | enum | — | `manual` / `usePointSetting` | yes | all |
| `wpml:globalHeight` | Global flight-route height, relative to the take-off point. | float | m | — | yes | all |
| `wpml:globalWaypointHeadingParam` | Global yaw mode. See [`common-elements.md §3.4`](common-elements.md#34-wpmlwaypointheadingparam--wpmlglobalwaypointheadingparam). | struct | — | — | — | all |
| `Placemark(Point)` | Waypoint — see §8. | struct | — | — | — | all |

### 6.2 Turn-mode semantics

Quoted verbatim from the v1.15 source:

- `coordinateTurn` — coordinated turn, no dips, early turns.
- `toPointAndStopWithDiscontinuityCurvature` — fly in a straight line, aircraft stops at the point.
- `toPointAndStopWithContinuityCurvature` — fly in a curve, aircraft stops at the point.
- `toPointAndPassWithContinuityCurvature` — fly in a curve, aircraft will not stop at the point.

*Note:* "Turns before waypoint. Flies through." mode in DJI Pilot 2 / FlightHub 2 is configured by setting `wpml:waypointTurnMode` to `toPointAndPassWithContinuityCurvature` **and** `wpml:useStraightLine` to `1`.

---

## 7. Area-mapping templates

Three template types — `mapping2d`, `mapping3d`, `mappingStrip` — share the general pattern: a survey-area polygon (or linestring), an overlap rate, and flight-mission metadata. Each has additional elements specific to its flight style.

### 7.1 `mapping2d` — Mapping Aerial template

2D aerial mapping. Single output wayline covering the survey polygon in a grid pattern.

| Element | Description | Type | Unit | Value / enum | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:caliFlightEnable` | Enable inertial-navigation calibration flight. At route end, performs 3 accel/decel flights; if route is long, accel/decel inserted at intervals (≤ 100 s between calibrations). | bool | — | `0` disable / `1` enable | — | M300 RTK, M350 RTK |
| `wpml:elevationOptimizeEnable` | Enable elevation optimization — after the main route, aircraft flies to the survey centre and takes tilted photos to improve elevation accuracy. | bool | — | `0` / `1` | yes | all |
| `wpml:smartObliqueEnable` | Enable Smart Posing — orthophoto and oblique photos captured in a single aerial task by swinging the gimbal. M300 RTK / M350 RTK support only P1 camera. | bool | — | `0` / `1` | — | all |
| `wpml:smartObliqueGimbalPitch` | Smart-Pose capture pitch angle. Must be within gimbal rotation range. M300 RTK / M350 RTK support only P1 camera. | int | ° | gimbal-dependent | — | all |
| `wpml:shootType` | Timed or fixed-distance shutter. Recommended: `time`. Template defines mode + overlap + speed; interval/distance is computed into `waylines.wpml`. | enum | — | `time` / `distance` | yes | all |
| `wpml:direction` | Route direction. | int | ° | [0, 360] | yes | all |
| `wpml:margin` | Expansion distance outside the survey area. | int | m | — | yes | all |
| `wpml:overlap` | Overlap-rate parameters. See §10. | struct | — | — | — | all |
| `wpml:ellipsoidHeight` | Global route ellipsoid height (used with `wpml:height`). | float | m | — | yes | all |
| `wpml:height` | Global route height (EGM96 / relative to takeoff / AGL). Paired with `ellipsoidHeight` as different reference-plane expressions of the same location. | float | m | — | yes | all |
| `wpml:facadeWaylineEnable` | Enable facade/slope mode. Used with `<LinearRing>`; when enabled, polygon heights use ellipsoid. | bool | — | `0` / `1` | — | M3E/M3T/M3M |
| `Polygon` | Survey polygon. KML form: `<Polygon><outerBoundaryIs><LinearRing><coordinates>lon,lat,height lon,lat,height …</coordinates></LinearRing></outerBoundaryIs></Polygon>`. When `facadeWaylineEnable` = 1, polygon supports aerial plane. | struct | — | — | — | all |
| `wpml:mappingHeadingParam` | Drone heading parameter in mapping. See §11. | struct | — | — | — | M3E/M3T/M3M |
| `wpml:gimbalPitchMode` | Gimbal-pitch mode (mapping-specific override). `manual` = manual control; `fixed` = fixed to user-set angle. | enum | — | `manual` / `fixed` | — | M3E/M3T/M3M |
| `wpml:gimbalPitchAngle` | Gimbal pitch angle (mapping-specific). | float | ° | [-90, -30] | iff `gimbalPitchMode` = `fixed` | M3E/M3T/M3M |

### 7.2 `mapping3d` — Oblique Photography template

3D oblique photography. Produces **5 executable waylines** per template: 1 orthophoto + 4 oblique-angle routes. The generator emits 5 `<Folder>` elements in `waylines.wpml`.

| Element | Description | Type | Unit | Value / enum | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:caliFlightEnable` | Enable calibration flight (M300 RTK / M350 RTK only). | bool | — | `0` / `1` | — | M300 RTK, M350 RTK |
| `wpml:inclinedGimbalPitch` | Gimbal pitch angle for tilt capture. Gimbal rotation range is model-dependent. Used for the 4 oblique routes. | int | ° | gimbal-dependent | yes | all |
| `wpml:inclinedFlightSpeed` | Flight speed for the 4 oblique routes. | float | m/s | (0, drone max speed] | yes | all |
| `wpml:shootType` | Timed or fixed-distance shutter. | enum | — | `time` / `distance` | yes | all |
| `wpml:direction` | Route direction. | int | ° | [0, 360] | yes | all |
| `wpml:margin` | Expansion distance outside survey area. | int | m | — | yes | all |
| `wpml:overlap` | Overlap-rate parameters. See §10. | struct | — | — | — | all |
| `wpml:ellipsoidHeight` | Global route ellipsoid height. | float | m | — | yes | all |
| `wpml:height` | Global route height (non-ellipsoid reference). | float | m | — | yes | all |
| `Polygon` | Survey polygon — `<Polygon><outerBoundaryIs><LinearRing><coordinates>lon,lat,0 lon,lat,0 …</coordinates></LinearRing></outerBoundaryIs></Polygon>`. | struct | — | — | — | all |

### 7.3 `mappingStrip` — Waypoint Segment Flight template

Linear/strip flight along a polyline, with lateral extension on either side. Used for pipeline inspections, road corridors, fence-line surveys.

| Element | Description | Type | Unit | Value / enum | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:caliFlightEnable` | Enable calibration flight. | bool | — | `0` / `1` | yes | all |
| `wpml:shootType` | Timed or fixed-distance shutter. | enum | — | `time` / `distance` | yes | all |
| `wpml:direction` | Route direction. | int | ° | [0, 360] | yes | all |
| `wpml:margin` | Expansion distance outside survey area. | float | m | — | yes | all |
| `wpml:singleLineEnable` | Enable single-route flight (rather than alternating back-and-forth). | bool | — | `0` / `1` | yes | all |
| `wpml:cuttingDistance` | Length of each sub-strip route. | float | m | — | yes | all |
| `wpml:boundaryOptimEnable` | Enable edge optimization. | bool | — | `0` / `1` | yes | all |
| `wpml:leftExtend` | Lateral extension on the left side of the line. | int | m | — | yes | all |
| `wpml:rightExtend` | Lateral extension on the right side of the line. | int | m | — | yes | all |
| `wpml:includeCenterEnable` | Whether to include the centreline in coverage. | bool | — | `0` / `1` | yes | all |
| `wpml:overlap` | Overlap-rate parameters. See §10. | struct | — | — | — | all |
| `wpml:ellipsoidHeight` | Global route ellipsoid height. | float | m | — | yes | all |
| `wpml:height` | Global route height (non-ellipsoid reference). | float | m | — | yes | all |
| `wpml:stripUseTemplateAltitude` | Whether linear flight reads `height` from the LineString coordinates. When enabled, `height` converts to ellipsoid. | bool | — | `0` / `1` | yes | all |
| `LineString` | Line geometry. `<LineString><coordinates>lon,lat,height lon,lat,height …</coordinates></LineString>`. `height` is only read when `stripUseTemplateAltitude` = 1. | struct | — | — | — | all |

---

## 8. Waypoint info — parent `<Placemark>`

Used by the `waypoint` template type to declare each concrete waypoint. Mapping templates use `Polygon` / `LineString` instead and do not carry per-waypoint `<Placemark>` elements.

| Element | Description | Type | Unit | Value / enum | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:isRisky` | Flag the waypoint as risky for operator review. | bool | — | `0` normal / `1` risky | — | M30/M30T, M3D/M3TD, M4E/M4T |
| `Point` | `<Point><coordinates>longitude,latitude</coordinates></Point>`. Range: [-180, 180], [-90, 90]. | float,float | °, ° | — | yes | all |
| `wpml:index` | Waypoint sequence number. Unique per route; monotonic from 0. | int | — | [0, 65535] | yes | all |
| `wpml:useGlobalHeight` | Use global height (`wpml:globalHeight`). | bool | — | `0` / `1` | yes | all |
| `wpml:ellipsoidHeight` | Waypoint ellipsoid height. Paired with `wpml:height`. | float | m | — | iff `useGlobalHeight` = 0 | all |
| `wpml:height` | Waypoint height (non-ellipsoid reference). Paired with `ellipsoidHeight`. | float | m | — | iff `useGlobalHeight` = 0 | all |
| `wpml:useGlobalSpeed` | Use global flight speed (`wpml:autoFlightSpeed`). | bool | — | `0` / `1` | yes | all |
| `wpml:waypointSpeed` | Per-waypoint speed. | float | m/s | (0, drone max speed] | iff `useGlobalSpeed` = 0 | all |
| `wpml:useGlobalHeadingParam` | Use global yaw parameter (`wpml:globalWaypointHeadingParam`). | bool | — | `0` / `1` | yes | all |
| `wpml:waypointHeadingParam` | Per-waypoint heading params. See [`common-elements.md §3.4`](common-elements.md#34-wpmlwaypointheadingparam--wpmlglobalwaypointheadingparam). | struct | — | — | iff `useGlobalHeadingParam` = 0 | all |
| `wpml:useGlobalTurnParam` | Use global turn mode (`wpml:globalWaypointTurnMode`). | bool | — | `0` / `1` | yes | all |
| `wpml:waypointTurnParam` | Per-waypoint turn params. See [`common-elements.md §3.5`](common-elements.md#35-wpmlwaypointturnparam). | struct | — | — | iff `useGlobalTurnParam` = 0 | all |
| `wpml:useStraightLine` | Override `globalUseStraightLine` locally. | bool | — | `0` / `1` | iff `waypointTurnMode` = `toPointAndStopWithContinuityCurvature` or `toPointAndPassWithContinuityCurvature` | M30/M30T, M3E/M3T/M3M, M3D/M3TD, M4E/M4T |
| `wpml:gimbalPitchAngle` | Per-waypoint gimbal pitch angle. | float | ° | model-gimbal range | iff `gimbalPitchMode` = `usePointSetting` | all |
| `wpml:quickOrthoMappingEnable` | Orthophoto smart-oblique shortcut — gimbal tilts through 3 different angles per photo stop; reduces route density. | bool | — | `0` / `1` | — | **M4E only** |
| `wpml:quickOrthoMappingPitch` | Smart-oblique pitch angle. | int | ° | [10, 30] | iff `quickOrthoMappingEnable` = 1 | **M4E only** |

---

## 9. Coordinate parameters — parent `<wpml:waylineCoordinateSysParam>`

| Element | Description | Type | Unit | Value / enum | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:coordinateMode` | Latitude/longitude coordinate system. | enum | — | `WGS84` (currently the only valid value) | yes | all |
| `wpml:heightMode` | Reference plane for waypoint elevation. | enum | — | `EGM96` / `relativeToStartPoint` / `aboveGroundLevel` (FlightHub 2 only) / `realTimeFollowSurface` (M3E/M3T/M3M only) | yes | all |
| `wpml:positioningType` | Source of location data. Marker only — does not affect execution. | enum | — | `GPS` / `RTKBaseStation` / `QianXun` / `Custom` | — | all |
| `wpml:globalShootHeight` | Aircraft height above the subject surface (AGL). Used for GSD and photo-spacing calculations. | float | m | — | yes *(for mapping2d / mapping3d / mappingStrip)* | all |
| `wpml:surfaceFollowModeEnable` | Enable surface-following flight. | bool | — | `0` / `1` | yes *(for mapping2d / mapping3d / mappingStrip)* | all |
| `wpml:surfaceRelativeHeight` | Surface-following flight height above ground. | float | m | — | iff `surfaceFollowModeEnable` = 1 | all |

---

## 10. Overlap rate — parent `<wpml:overlap>`

Separate forward / side overlaps for LiDAR vs visible cameras and orthophoto vs oblique routes.

| Element | Description | Type | Unit | Value | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:orthoLidarOverlapH` | Forward overlap (LiDAR / orthophoto). | int | % | [0, 100] | — | M300 RTK, M350 RTK |
| `wpml:orthoLidarOverlapW` | Side overlap (LiDAR / orthophoto). | int | % | [0, 100] | — | M300 RTK, M350 RTK |
| `wpml:orthoCameraOverlapH` | Forward overlap (visible / orthophoto). | int | % | [0, 100] | — | all |
| `wpml:orthoCameraOverlapW` | Side overlap (visible / orthophoto). | int | % | [0, 100] | — | all |
| `wpml:inclinedLidarOverlapH` | Forward overlap (LiDAR / oblique). | int | % | [0, 100] | — | M300 RTK, M350 RTK |
| `wpml:inclinedLidarOverlapW` | Side overlap (LiDAR / oblique). | int | % | [0, 100] | — | M300 RTK, M350 RTK |
| `wpml:inclinedCameraOverlapH` | Forward overlap (visible / oblique). | int | % | [0, 100] | — | all |
| `wpml:inclinedCameraOverlapW` | Side overlap (visible / oblique). | int | % | [0, 100] | — | all |

---

## 11. Mapping heading parameter — parent `<wpml:mappingHeadingParam>`

| Element | Description | Type | Unit | Value / enum | Required | Product support |
|---|---|---|---|---|---|---|
| `wpml:mappingHeadingMode` | Drone yaw-angle mode during mapping. | enum | — | `fixed` / `followWayline` | — | M3E/M3T/M3M, M3D/M3TD, M4E/M4T |
| `wpml:mappingHeadingAngle` | Drone yaw angle. | int | ° | [0, 360] | iff `mappingHeadingMode` = `fixed` | M3E/M3T/M3M, M3D/M3TD, M4E/M4T |

---

## 12. DJI-source inconsistencies noted

Carry into Phase 10 device annexes / Phase 9 wayline workflow authoring; none rise to OQ level:

- **`wpml:imageFormat` intro row** lacks explicit `unit` / `required` cells in the source — the flag text says "Yes" in `imageFormat` context but nothing in the Is-it-required cell. Treat as `required: yes`.
- **`wpml:heightMode` value `WGS84`** listed under `coordinateMode` — description literally says "WGS84: Current fixed use WGS84". DJI's phrasing is verbose; the point is `WGS84` is the only valid value.
- **`wpml:gimbalPitchAngle` in mapping2d context** has `unit: °` row but the Type column is empty — DJI extract defect. Actual type is `float`.
- **`wpml:stripUseTemplateAltitude` Note phrasing** — the v1.15 extract says "When it is opened, the value of height will be converted to ellipsoid." Treat `opened` as `enabled` (= 1). DJI's English translation is rough.
- **`wpml:quickOrthoMappingEnable` Product Support = `M4E`** only — the source explicitly excludes M4D/M4TD (and everything else). Whether M4D inherits this M4E feature when deployed in dock-pairing mode is not stated by DJI. Implementations should branch defensively or ask DJI.

---

## 13. Source provenance

| Source | Role |
|---|---|
| [`DJI_Cloud/DJI_CloudAPI_WPML-Template-KML.txt`](../../DJI_Cloud/DJI_CloudAPI_WPML-Template-KML.txt) | v1.15 primary — 1,923 lines, full template-file catalog including the sample above. |
| [`DJI_Cloud/DJI_CloudAPI_WPML-Overview.txt`](../../DJI_Cloud/DJI_CloudAPI_WPML-Overview.txt) | v1.15 primary — template vs execution concept. |
| [`DJI_Cloud/DJI_CloudAPI_WPML-Common-Elements.txt`](../../DJI_Cloud/DJI_CloudAPI_WPML-Common-Elements.txt) | v1.15 primary — shared schemas linked inline. |
