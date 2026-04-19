# Dock-to-Cloud MQTT catalog

Per-method documentation of everything the **Dock 2** and **Dock 3** gateways emit on, and receive over, MQTT. Each entry uses the envelope and topic-taxonomy conventions from [`../README.md`](../README.md) (Phase 2) — don't restate those here.

Per-method files are named verbatim after the DJI `method` string (e.g., `airport_organization_bind.md`) so that searches for a method name hit the filename directly.

---

## Catalog status

Phase 4 is being landed in feature-area sub-drops. This index grows as drops land.

| Sub-phase | Feature area | Status |
|---|---|---|
| 4a | DeviceManagement + Organization + Configuration — binding, topology, config | **landed 2026-04-18** |
| 4b | WaylineManagement — flight-task lifecycle + Virtual Cockpit routes | **landed 2026-04-18** |
| 4c | Live-Flight-Controls — DRC, camera/gimbal/IR control, authority grab | **landed 2026-04-18** |
| 4d | LiveStream + Media-Management | pending |
| 4e | Firmware-Upgrade + Remote-Log + Remote-Debugging + Remote-Control | pending |
| 4f | FlySafe + Custom-Flight-Area + AirSense + HMS | pending |
| 4g | PSDK + PSDK-Interconnection + ESDK-Interconnection | pending |

## Current catalog

### `status/`

Topics under `sys/product/{gateway_sn}/status`.

| Method | Doc | Purpose |
|---|---|---|
| `update_topo` | [`status/update_topo.md`](status/update_topo.md) | Gateway reports its own state and sub-device list. |

### `events/`

Topics under `thing/product/{gateway_sn}/events`. Device → cloud pushes.

| Method | Doc | Purpose |
|---|---|---|
| `return_home_info` | [`events/return_home_info.md`](events/return_home_info.md) | Return-path trajectory + per-dock planning status. |
| `flighttask_ready` | [`events/flighttask_ready.md`](events/flighttask_ready.md) | Prepared conditional missions meet `ready_conditions`. |
| `flighttask_progress` | [`events/flighttask_progress.md`](events/flighttask_progress.md) | Periodic task-progress report with state, step, breakpoint. |
| `device_exit_homing_notify` | [`events/device_exit_homing_notify.md`](events/device_exit_homing_notify.md) | Aircraft enters / exits Return-to-Home Exit state. |
| `in_flight_wayline_progress` | [`events/in_flight_wayline_progress.md`](events/in_flight_wayline_progress.md) | Progress of a Virtual Cockpit in-flight route. |
| `fly_to_point_progress` | [`events/fly_to_point_progress.md`](events/fly_to_point_progress.md) | Flyto-to-point execution progress (state, distance, trajectory). |
| `takeoff_to_point_progress` | [`events/takeoff_to_point_progress.md`](events/takeoff_to_point_progress.md) | One-key takeoff mission progress. |
| `drc_status_notify` | [`events/drc_status_notify.md`](events/drc_status_notify.md) | *(Abandoned.)* DRC link state (connected / connecting / not connected). |
| `joystick_invalid_notify` | [`events/joystick_invalid_notify.md`](events/joystick_invalid_notify.md) | DRC flight control became invalid (RC-lost, low battery, takeover). |
| `camera_photo_take_progress` | [`events/camera_photo_take_progress.md`](events/camera_photo_take_progress.md) | Persistent photo-capture progress (currently panorama). |

### `services/`

Topics under `thing/product/{gateway_sn}/services`. Cloud → device commands.

| Method | Doc | Purpose |
|---|---|---|
| `flighttask_prepare` | [`services/flighttask_prepare.md`](services/flighttask_prepare.md) | Issue a mission (immediate / timed / conditional). |
| `flighttask_execute` | [`services/flighttask_execute.md`](services/flighttask_execute.md) | Execute a prepared mission. Multi-dock capable. |
| `flighttask_pause` | [`services/flighttask_pause.md`](services/flighttask_pause.md) | Pause an in-progress wayline. |
| `flighttask_recovery` | [`services/flighttask_recovery.md`](services/flighttask_recovery.md) | Resume a paused wayline. |
| `flighttask_stop` | [`services/flighttask_stop.md`](services/flighttask_stop.md) | Terminate a flight task. |
| `flighttask_undo` | [`services/flighttask_undo.md`](services/flighttask_undo.md) | Cancel prepared-but-not-executed missions (batch). |
| `flighttask_create` | [`services/flighttask_create.md`](services/flighttask_create.md) | *(Deprecated.)* Legacy mission-create method. |
| `return_home` | [`services/return_home.md`](services/return_home.md) | One-key return to home. |
| `return_home_cancel` | [`services/return_home_cancel.md`](services/return_home_cancel.md) | Cancel in-progress return. |
| `return_specific_home` | [`services/return_specific_home.md`](services/return_specific_home.md) | Designate landing dock in multi-dock tasks. |
| `in_flight_wayline_deliver` | [`services/in_flight_wayline_deliver.md`](services/in_flight_wayline_deliver.md) | Distribute a Virtual Cockpit flight route to an airborne aircraft. |
| `in_flight_wayline_stop` | [`services/in_flight_wayline_stop.md`](services/in_flight_wayline_stop.md) | Pause a Virtual Cockpit flight route. |
| `in_flight_wayline_recover` | [`services/in_flight_wayline_recover.md`](services/in_flight_wayline_recover.md) | Resume a paused Virtual Cockpit route. |
| `in_flight_wayline_cancel` | [`services/in_flight_wayline_cancel.md`](services/in_flight_wayline_cancel.md) | Cancel a Virtual Cockpit route. |
| `flight_authority_grab` | [`services/flight_authority_grab.md`](services/flight_authority_grab.md) | Grab flight-control authority from the bound RC. |
| `payload_authority_grab` | [`services/payload_authority_grab.md`](services/payload_authority_grab.md) | Grab gimbal / camera control authority. |
| `drc_mode_enter` | [`services/drc_mode_enter.md`](services/drc_mode_enter.md) | Open DRC session — MQTT relay info + OSD / HSI frequencies. |
| `drc_mode_exit` | [`services/drc_mode_exit.md`](services/drc_mode_exit.md) | Close DRC session. |
| `takeoff_to_point` | [`services/takeoff_to_point.md`](services/takeoff_to_point.md) | One-key takeoff + fly to target. |
| `fly_to_point` | [`services/fly_to_point.md`](services/fly_to_point.md) | Fly airborne aircraft to a target point. |
| `fly_to_point_stop` | [`services/fly_to_point_stop.md`](services/fly_to_point_stop.md) | End an in-progress flyto task (aircraft hovers). |
| `fly_to_point_update` | [`services/fly_to_point_update.md`](services/fly_to_point_update.md) | Update the target point of an in-flight flyto. |
| `camera_frame_zoom` | [`services/camera_frame_zoom.md`](services/camera_frame_zoom.md) | Subject-frame zoom (select rectangle; camera zooms + centers gimbal). |
| `camera_mode_switch` | [`services/camera_mode_switch.md`](services/camera_mode_switch.md) | Switch camera mode (capture / record / smart low-light / panorama). |
| `camera_photo_take` | [`services/camera_photo_take.md`](services/camera_photo_take.md) | Trigger still photo capture. |
| `camera_photo_stop` | [`services/camera_photo_stop.md`](services/camera_photo_stop.md) | Stop persistent capture (panorama). |
| `camera_recording_start` | [`services/camera_recording_start.md`](services/camera_recording_start.md) | Start video recording. |
| `camera_recording_stop` | [`services/camera_recording_stop.md`](services/camera_recording_stop.md) | Stop video recording. |
| `camera_screen_drag` | [`services/camera_screen_drag.md`](services/camera_screen_drag.md) | Gimbal pitch/yaw by angular speed (drag-equivalent). |
| `camera_aim` | [`services/camera_aim.md`](services/camera_aim.md) | Double-tap to aim — center a pixel in the field of view. |
| `camera_focal_length_set` | [`services/camera_focal_length_set.md`](services/camera_focal_length_set.md) | Set zoom factor. |
| `gimbal_reset` | [`services/gimbal_reset.md`](services/gimbal_reset.md) | Recenter / reset gimbal. |
| `camera_look_at` | [`services/camera_look_at.md`](services/camera_look_at.md) | Aim aircraft + gimbal at a geographic point. |
| `camera_screen_split` | [`services/camera_screen_split.md`](services/camera_screen_split.md) | Enable / disable split-screen view. |
| `photo_storage_set` | [`services/photo_storage_set.md`](services/photo_storage_set.md) | Select which lens outputs are stored per photo. |
| `video_storage_set` | [`services/video_storage_set.md`](services/video_storage_set.md) | Select which lens outputs are stored during recording. |
| `camera_exposure_mode_set` | [`services/camera_exposure_mode_set.md`](services/camera_exposure_mode_set.md) | Set exposure mode (auto / shutter / aperture / manual). |
| `camera_exposure_set` | [`services/camera_exposure_set.md`](services/camera_exposure_set.md) | Set EV compensation. |
| `camera_focus_mode_set` | [`services/camera_focus_mode_set.md`](services/camera_focus_mode_set.md) | Set focus mode (MF / AFS / AFC). |
| `camera_focus_value_set` | [`services/camera_focus_value_set.md`](services/camera_focus_value_set.md) | Set manual focus value. |
| `camera_point_focus_action` | [`services/camera_point_focus_action.md`](services/camera_point_focus_action.md) | Spot autofocus at a pixel coordinate. |
| `ir_metering_mode_set` | [`services/ir_metering_mode_set.md`](services/ir_metering_mode_set.md) | Set IR temperature-measurement mode (off / point / area). |
| `ir_metering_point_set` | [`services/ir_metering_point_set.md`](services/ir_metering_point_set.md) | Set IR point-measurement coordinate. |
| `ir_metering_area_set` | [`services/ir_metering_area_set.md`](services/ir_metering_area_set.md) | Set IR area-measurement region. |

### `requests/`

Topics under `thing/product/{gateway_sn}/requests`. Device → cloud requests, cloud → device replies.

| Method | Doc | Purpose |
|---|---|---|
| `config` | [`requests/config.md`](requests/config.md) | Gateway asks the cloud for License / NTP configuration. |
| `airport_bind_status` | [`requests/airport_bind_status.md`](requests/airport_bind_status.md) | Gateway asks whether given devices are bound. |
| `airport_organization_get` | [`requests/airport_organization_get.md`](requests/airport_organization_get.md) | Gateway resolves an organization ID to a display name. |
| `airport_organization_bind` | [`requests/airport_organization_bind.md`](requests/airport_organization_bind.md) | Gateway binds a device set to an organization. |
| `flighttask_progress_get` | [`requests/flighttask_progress_get.md`](requests/flighttask_progress_get.md) | In multi-dock tasks, query the other dock's latest progress. |
| `flighttask_resource_get` | [`requests/flighttask_resource_get.md`](requests/flighttask_resource_get.md) | Fetch a fresh pre-signed URL for the KMZ wayline file. |

### `drc/`

Topics under `thing/product/{gateway_sn}/drc/down` (cloud → device) and `/drc/up` (device → cloud). Lightweight DRC envelope per [`../README.md` §5.8](../README.md#58-drcup--drcdown--direct-remote-control).

| Method | Doc | Purpose |
|---|---|---|
| `stick_control` | [`drc/stick_control.md`](drc/stick_control.md) | Virtual-RC-stick control (5–10 Hz, no ack). |
| `drone_control` | [`drc/drone_control.md`](drc/drone_control.md) | *(Abandoned.)* Velocity-vector flight control (5–10 Hz, with reply). |
| `drone_emergency_stop` | [`drc/drone_emergency_stop.md`](drc/drone_emergency_stop.md) | Immediate hover; cancels DRC motion commands. |
| `heart_beat` | [`drc/heart_beat.md`](drc/heart_beat.md) | Bidirectional DRC keep-alive (>1 min silence auto-exits DRC). |
| `hsi_info_push` | [`drc/hsi_info_push.md`](drc/hsi_info_push.md) | Obstacle-sensing state + 360° distance ring. |
| `delay_info_push` | [`drc/delay_info_push.md`](drc/delay_info_push.md) | Image-transmission + per-stream latency. |
| `osd_info_push` | [`drc/osd_info_push.md`](drc/osd_info_push.md) | High-frequency OSD (attitude, position, velocity, gimbal). |

### `property/set`, `osd/`, `state/`

Pending in later sub-phases.

## Cohort coverage

Every method in this tree is documented with an explicit **Cohort** field at the top:

- **Dock 2 + Dock 3** — method exists in both cohorts with the same payload. This is the default for Phase 4a content.
- **Dock 3 only** — method is new in v1.15 with no Dock 2 counterpart (AirSense-aircraft events, AI-identify DRC modes, etc.). Marked explicitly.
- **Dock 2 only** — rare; indicates a legacy method that Dock 3 doesn't reimplement.

Per-cohort quirks that are larger than a one-line note live in Phase 10 (`device-annexes/`).

## Source reconciliation

v1.11 Cloud-API-Doc/ covers Dock 2 under `60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/`. v1.15 DJI_Cloud extracts cover both Dock 2 (`DJI_CloudAPI-Dock2-*.txt`) and Dock 3 (`DJI_CloudAPI-Dock3-*.txt`). Where v1.11 Dock 2 and v1.15 Dock 2 agree on a method, citations point to v1.11 first (formatting fidelity). Where a method exists only in v1.15, the DJI_Cloud file is primary.
