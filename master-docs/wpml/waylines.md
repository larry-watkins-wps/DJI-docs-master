# `waylines.wpml` — the execution file

The `waylines.wpml` file inside a WPML `.kmz` archive contains the **concrete drone commands** for a mission — waypoint coordinates, altitude, speed, heading, and action groups. DJI Pilot 2 / FlightHub 2 / third-party generators read [`template.kml`](template-kml.md) parameters and compute this executable file.

See [`overview.md`](overview.md) for the WPML format, archive layout, and device support.

---

## 1. File structure

Two top-level parts inside the root `<Document>`:

1. **Mission information** — `<wpml:missionConfig>`, carrying global parameters (fly-to-first-waypoint mode, finish action, RC-lost action, takeoff security height, global transitional speed, RTH height, drone info, payload info). Shared with `template.kml` — see [`common-elements.md`](common-elements.md).
2. **Waylines information** — one or more `<Folder>` elements. Each `<Folder>` represents one executable wayline. Template types that produce multiple waylines (e.g. `mapping3d` produces 5) emit one `<Folder>` per output wayline.

Inside each `<Folder>`:

- Wayline-scoped parameters (`wpml:waylineId`, `wpml:executeHeightMode`, `wpml:autoFlightSpeed`, optional `wpml:startActionGroup`).
- One or more `<Placemark>` elements, each a waypoint.

Inside each `<Placemark>`:

- `<Point>` with `<coordinates>longitude,latitude</coordinates>`.
- Waypoint-scoped parameters (`wpml:index`, `wpml:executeHeight`, `wpml:waypointSpeed`, heading params, turn params).
- Optional `<wpml:actionGroup>` children — what the drone does *at* or *after* this waypoint.

---

## 2. Complete example

Verbatim from the v1.15 source. Declares a two-waypoint mission with one action group on waypoint #1 (gimbal rotate + take photo):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:wpml="http://www.dji.com/wpmz/1.0.2">
<Document>
<!-- Step 1: Setup Mission Configuration -->
<wpml:missionConfig>
<wpml:flyToWaylineMode>safely</wpml:flyToWaylineMode>
<wpml:finishAction>goHome</wpml:finishAction>
<wpml:exitOnRCLost>goContinue</wpml:exitOnRCLost>
<wpml:executeRCLostAction>hover</wpml:executeRCLostAction>
<wpml:takeOffSecurityHeight>20</wpml:takeOffSecurityHeight>
<wpml:globalTransitionalSpeed>10</wpml:globalTransitionalSpeed>
<!-- Declare drone model with M30 -->
<wpml:droneInfo>
<wpml:droneEnumValue>67</wpml:droneEnumValue>
<wpml:droneSubEnumValue>0</wpml:droneSubEnumValue>
</wpml:droneInfo>
<!-- Declare drone model with M30 -->
<wpml:payloadInfo>
<wpml:payloadEnumValue>52</wpml:payloadEnumValue>
<wpml:payloadPositionIndex>0</wpml:payloadPositionIndex>
</wpml:payloadInfo>
</wpml:missionConfig>

<!-- Step 2: Setup A Folder for Waypoint Template -->
<Folder>
<wpml:templateId>0</wpml:templateId>
<wpml:executeHeightMode>WGS84</wpml:executeHeightMode>
<wpml:waylineId>0</wpml:waylineId>
<wpml:autoFlightSpeed>10</wpml:autoFlightSpeed>
<Placemark>
<Point>
<coordinates>
longitude,latitude
</coordinates>
</Point>
<wpml:index>0</wpml:index>
<wpml:executeHeight>116.57</wpml:executeHeight>
<wpml:waypointSpeed>10</wpml:waypointSpeed>
<wpml:waypointHeadingParam>
<wpml:waypointHeadingMode>followWayline</wpml:waypointHeadingMode>
</wpml:waypointHeadingParam>
<wpml:waypointTurnParam>
<wpml:waypointTurnMode>toPointAndStopWithDiscontinuityCurvature</wpml:waypointTurnMode>
<wpml:waypointTurnDampingDist>0</wpml:waypointTurnDampingDist>
</wpml:waypointTurnParam>
</Placemark>
<Placemark>
<Point>
<coordinates>
longitude,latitude
</coordinates>
</Point>
<wpml:index>1</wpml:index>
<wpml:executeHeight>116.57</wpml:executeHeight>
<wpml:waypointSpeed>7</wpml:waypointSpeed>
<wpml:waypointHeadingParam>
<wpml:waypointHeadingMode>followWayline</wpml:waypointHeadingMode>
</wpml:waypointHeadingParam>
<wpml:waypointTurnParam>
<wpml:waypointTurnMode>toPointAndStopWithDiscontinuityCurvature</wpml:waypointTurnMode>
<wpml:waypointTurnDampingDist>0</wpml:waypointTurnDampingDist>
</wpml:waypointTurnParam>
<!-- Declare action group for waypoint 1# -->
<wpml:actionGroup>
<wpml:actionGroupId>0</wpml:actionGroupId>
<wpml:actionGroupStartIndex>1</wpml:actionGroupStartIndex>
<wpml:actionGroupEndIndex>1</wpml:actionGroupEndIndex>
<wpml:actionGroupMode>sequence</wpml:actionGroupMode>
<wpml:actionTrigger>
<wpml:actionTriggerType>reachPoint</wpml:actionTriggerType>
</wpml:actionTrigger>
<!-- Declare the 1st action: rotate gimbal -->
<wpml:action>
<wpml:actionId>0</wpml:actionId>
<wpml:actionActuatorFunc>gimbalRotate</wpml:actionActuatorFunc>
<wpml:actionActuatorFuncParam>
<wpml:gimbalRotateMode>absoluteAngle</wpml:gimbalRotateMode>
<wpml:gimbalPitchRotateEnable>0</wpml:gimbalPitchRotateEnable>
<wpml:gimbalPitchRotateAngle>0</wpml:gimbalPitchRotateAngle>
<wpml:gimbalRollRotateEnable>0</wpml:gimbalRollRotateEnable>
<wpml:gimbalRollRotateAngle>0</wpml:gimbalRollRotateAngle>
<wpml:gimbalYawRotateEnable>1</wpml:gimbalYawRotateEnable>
<wpml:gimbalYawRotateAngle>30</wpml:gimbalYawRotateAngle>
<wpml:gimbalRotateTimeEnable>0</wpml:gimbalRotateTimeEnable>
<wpml:gimbalRotateTime>0</wpml:gimbalRotateTime>
<wpml:payloadPositionIndex>0</wpml:payloadPositionIndex>
</wpml:actionActuatorFuncParam>
</wpml:action>
<!-- Declare the 2nd action: take photo -->
<wpml:action>
<wpml:actionId>1</wpml:actionId>
<wpml:actionActuatorFunc>takePhoto</wpml:actionActuatorFunc>
<wpml:actionActuatorFuncParam>
<wpml:fileSuffix>point1</wpml:fileSuffix>
<wpml:payloadPositionIndex>0</wpml:payloadPositionIndex>
</wpml:actionActuatorFuncParam>
</wpml:action>
</wpml:actionGroup>
</Placemark>
</Folder>

</Document>
</kml>
```

---

## 3. Mission information — parent `<wpml:missionConfig>`

Shared with `template.kml`. Full catalog in [`common-elements.md` §2](common-elements.md#2-mission-configuration). Subset of elements specifically called out in `waylines.wpml`:

| Element | Type | Unit | Value / enum | Required | Product support |
|---|---|---|---|---|---|
| `wpml:flyToWaylineMode` | enum | — | `safely` / `pointToPoint` | yes | M300 RTK, M350 RTK, M30/M30T, M3E/M3T/M3M, M3D/M3TD, M4E/M4T |
| `wpml:finishAction` | enum | — | `goHome` / `noAction` / `autoLand` / `gotoFirstWaypoint` | yes | same |
| `wpml:exitOnRCLost` | enum | — | `goContinue` / `executeLostAction` | yes | same |
| `wpml:executeRCLostAction` | enum | — | `goBack` / `landing` / `hover` | iff `exitOnRCLost` = `executeLostAction` | same |
| `wpml:takeOffSecurityHeight` | float | m | RC: [1.2, 1500]; Dock: [8, 1500] (relative to take-off point) | yes | same |
| `wpml:globalTransitionalSpeed` | float | m/s | [0, 15] | yes | same |
| `wpml:globalRTHHeight` | float | m | [2, 1500] | yes | same |
| `wpml:droneInfo` | struct | — | see [`common-elements.md §3.1`](common-elements.md#31-wpmldroneinfo) | — | same |
| `wpml:payloadInfo` | struct | — | see [`common-elements.md §3.2`](common-elements.md#32-wpmlpayloadinfo) | — | same |
| `wpml:autoRerouteInfo` | struct | — | see [`common-elements.md §3.6`](common-elements.md#36-wpmlautorerouteinfo) | — | **M3D/M3TD, M4E/M4T only** |

**Enum details** (source-verbatim descriptions):

- `wpml:flyToWaylineMode`:
  - `safely` — (M300) aircraft takes off, rises to the first-waypoint altitude, then level-flies. If first waypoint is below the take-off point, level-flies over the first waypoint before descending. (M30) same, but if first waypoint is below the "safe take-off altitude", level-flies after reaching safe altitude. "Safe takeoff altitude" only applies when the aircraft has not taken off.
  - `pointToPoint` — (M300) after takeoff, tilts directly to the first waypoint. (M30) takes off to safe-takeoff altitude, then tilts to the first waypoint.
- `wpml:finishAction`:
  - `goHome` — after mission complete, exit wayline mode and return to home.
  - `noAction` — after mission complete, exit wayline mode.
  - `autoLand` — after mission complete, exit wayline mode and land in place.
  - `gotoFirstWaypoint` — after mission complete, fly to the first waypoint and exit wayline mode on arrival.
  - *Note:* If the aircraft exits wayline mode and enters RC-lost (runaway) state during the above, the runaway action fires first.
- `wpml:exitOnRCLost`:
  - `goContinue` — keep executing the wayline.
  - `executeLostAction` — exit wayline mode and run the runaway action.
- `wpml:executeRCLostAction`:
  - `goBack` — fly from the lost position to the take-off point.
  - `landing` — land in place at the lost position.
  - `hover` — hover at the lost position.

---

## 4. Wayline information — parent `<Folder>`

Each `<Folder>` declares one executable wayline.

| Element | Type | Unit | Value / enum | Required | Product support |
|---|---|---|---|---|---|
| `wpml:templateId` | int | — | [0, 65535] — unique per `.kmz`; monotonically increasing from 0 recommended. Used to associate this executable wayline back to its template.kml Folder. | yes | all |
| `wpml:waylineId` | int | — | [0, 65535] — unique per `.kmz`; monotonically increasing from 0 recommended. | yes | all |
| `wpml:autoFlightSpeed` | float | m/s | (0, max-flight-speed-of-drone]. Overridable per-waypoint. | yes | all |
| `wpml:executeHeightMode` | enum | — | `WGS84` (ellipsoid) / `relativeToStartPoint` / `realTimeFollowSurface` (M3E/M3T/M3M only) | yes — **execution-file only** (not in template.kml) | all (enum gating per row) |
| `Placemark(Point)` | struct | — | Waypoint detail. See §5. | yes (≥1 per Folder) | all |
| `wpml:startActionGroup` | struct | — | Initial actions run *before* the wayline starts. Also runs when a wayline is recovered from interruption, before waypoint actions. Structure per [`common-elements.md §4`](common-elements.md#4-wpmlactiongroup--wpmlactiontrigger--wpmlaction) (`actionGroup` / `actionTrigger` / `action` chain). | — | M30/M30T, M3E/M3T/M3M, M3D/M3TD, M4E/M4T |

`wpml:executeHeightMode` is **only valid inside `waylines.wpml`**. The template.kml uses `wpml:heightMode` (on `<wpml:waylineCoordinateSysParam>`) instead — see [`template-kml.md §9`](template-kml.md#9-coordinate-parameters--parent-wpmlwaylinecoordinatesysparam). The generator maps template `heightMode` values onto execution `executeHeightMode`.

---

## 5. Waypoint information — parent `<Placemark>`

Each `<Placemark>` is one waypoint in the wayline.

| Element | Type | Unit | Value / enum | Required | Product support |
|---|---|---|---|---|---|
| `Point/coordinates` | float,float | °, ° | `<Point><coordinates>longitude,latitude</coordinates></Point>`. Range: [-180, 180], [-90, 90]. | yes | all |
| `wpml:index` | int | — | [0, 65535]. Monotonically and continuously increasing from 0. | yes | all |
| `wpml:executeHeight` | float | m | Altitude per the wayline's `wpml:executeHeightMode`. **execution-file only**. | yes | all |
| `wpml:waypointSpeed` | float | m/s | (0, drone max speed]. Speed from this waypoint to the next. | yes (iff `useGlobalSpeed = 0`) | all |
| `wpml:waypointHeadingParam` | struct | — | See [`common-elements.md §3.4`](common-elements.md#34-wpmlwaypointheadingparam--wpmlglobalwaypointheadingparam). | yes (iff `useGlobalHeadingParam = 0`) | all |
| `wpml:waypointTurnParam` | struct | — | See [`common-elements.md §3.5`](common-elements.md#35-wpmlwaypointturnparam). | yes | all |
| `wpml:useStraightLine` | bool | — | `0` = curved trajectory; `1` = as close to straight-line as possible. | iff `waypointTurnMode` is `toPointAndStopWithContinuityCurvature` or `toPointAndPassWithContinuityCurvature`. Local overrides global. | M30/M30T, M3E/M3T/M3M, M3D/M3TD, M4E/M4T |
| `wpml:isRisky` | bool | — | `0` normal / `1` risky. Marks the point as risky for operator review. | — | M30/M30T, M3D/M3TD, M4E/M4T |
| `wpml:actionGroup` | struct | — | Actions triggered at / around this waypoint. Zero or more. See [`common-elements.md §4`](common-elements.md#4-wpmlactiongroup--wpmlactiontrigger--wpmlaction). | — | all |

Heading and turn parameters that are also shared with the template are documented in [`common-elements.md`](common-elements.md) rather than duplicated here.

---

## 6. Execution-vs-template shape rules

- The `<wpml:missionConfig>` block is the same in both files.
- The template's `<Folder>` describes **template parameters** (template type, survey area polygon, overlap rate, etc.); the execution's `<Folder>` describes **concrete waypoints** (coordinates, per-waypoint heading, per-waypoint turn).
- A single `<wpml:templateId>` in template.kml may emit multiple `<Folder>` elements in waylines.wpml (e.g. `mapping3d` produces 5).
- Height-mode vocabulary differs:
  - template.kml uses `wpml:heightMode` on `<wpml:waylineCoordinateSysParam>` — values `EGM96` / `relativeToStartPoint` / `aboveGroundLevel` / `realTimeFollowSurface`.
  - waylines.wpml uses `wpml:executeHeightMode` on `<Folder>` — values `WGS84` / `relativeToStartPoint` / `realTimeFollowSurface`.
- The template file declares the intent; the execution file declares what the drone actually flies.

---

## 7. Source provenance

| Source | Role |
|---|---|
| [`DJI_Cloud/DJI_CloudAPI_WPML-Waylines.txt`](../../DJI_Cloud/DJI_CloudAPI_WPML-Waylines.txt) | v1.15 primary — 533 lines, full execution-file catalog including the sample above. |
| [`DJI_Cloud/DJI_CloudAPI_WPML-Overview.txt`](../../DJI_Cloud/DJI_CloudAPI_WPML-Overview.txt) | v1.15 primary — cross-file concept notes (execution vs template). |
| [`DJI_Cloud/DJI_CloudAPI_WPML-Common-Elements.txt`](../../DJI_Cloud/DJI_CloudAPI_WPML-Common-Elements.txt) | v1.15 primary — detailed schemas for shared elements; linked inline. |
