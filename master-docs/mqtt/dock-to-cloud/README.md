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
| 4d | LiveStream + Media-Management | **landed 2026-04-18** |
| 4e-1 | Firmware-Upgrade + Remote-Log + Remote-Debugging | **landed 2026-04-19** |
| 4e-2 | Remote-Control (DRC PSDK + AI identify + camera/speaker/light) | **landed 2026-04-19** |
| 4f | FlySafe + Custom-Flight-Area + AirSense + HMS | **landed 2026-04-19** |
| 4g | PSDK + PSDK-Interconnection + ESDK-Interconnection | **landed 2026-04-19** |

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
| `highest_priority_upload_flighttask_media` | [`events/highest_priority_upload_flighttask_media.md`](events/highest_priority_upload_flighttask_media.md) | Dock announces the flight task whose media will be uploaded first. |
| `file_upload_callback` | [`events/file_upload_callback.md`](events/file_upload_callback.md) | Single media file has been uploaded; carries file descriptor + metadata. |
| `ota_progress` | [`events/ota_progress.md`](events/ota_progress.md) | Firmware-update task progress (percent + current step). |
| `fileupload_progress` | [`events/fileupload_progress.md`](events/fileupload_progress.md) | Per-file progress for a log-upload batch (`need_reply: 0`). |
| `esim_operator_switch` | [`events/esim_operator_switch.md`](events/esim_operator_switch.md) | eSIM operator-switch progress (dock / aircraft dongle). |
| `esim_activate` | [`events/esim_activate.md`](events/esim_activate.md) | eSIM activation progress. |
| `device_format` | [`events/device_format.md`](events/device_format.md) | Dock-storage formatting progress. |
| `drone_format` | [`events/drone_format.md`](events/drone_format.md) | Aircraft-storage formatting progress. |
| `charge_close` | [`events/charge_close.md`](events/charge_close.md) | Stop-charging progress (4 safety-check steps). |
| `charge_open` | [`events/charge_open.md`](events/charge_open.md) | Start-charging progress (6 safety-check steps). |
| `cover_open` | [`events/cover_open.md`](events/cover_open.md) | Dock-cover open progress (5 safety-check steps). |
| `cover_close` | [`events/cover_close.md`](events/cover_close.md) | Dock-cover close progress (9-step propeller-paddle sequence). |
| `device_reboot` | [`events/device_reboot.md`](events/device_reboot.md) | Dock-reboot progress (6 safety-check steps). |
| `cover_force_close` | [`events/cover_force_close.md`](events/cover_force_close.md) | Forced dock-cover close progress (no step_key decomposition). |
| `drone_close` | [`events/drone_close.md`](events/drone_close.md) | Aircraft power-off progress (7 safety-check steps). |
| `drone_open` | [`events/drone_open.md`](events/drone_open.md) | Aircraft power-on state change (no progress percent / step_key). |
| `rtk_calibration` | [`events/rtk_calibration.md`](events/rtk_calibration.md) | RTK manual-calibration result (Dock 3 only; `need_reply: 1`). |
| `flight_areas_drone_location` | [`events/flight_areas_drone_location.md`](events/flight_areas_drone_location.md) | Aircraft distance/inside-state for every loaded custom flight area (`need_reply: 0`). |
| `flight_areas_sync_progress` | [`events/flight_areas_sync_progress.md`](events/flight_areas_sync_progress.md) | Custom-flight-area file sync state + failure reason (`need_reply: 1`). |
| `airsense_warning` | [`events/airsense_warning.md`](events/airsense_warning.md) | ADS-B proximity warning (five levels; `need_reply: 1`). |
| `hms` | [`events/hms.md`](events/hms.md) | Health Management System warning push (batch up to 20 entries). |
| `speaker_tts_play_start_progress` | [`events/speaker_tts_play_start_progress.md`](events/speaker_tts_play_start_progress.md) | PSDK TTS-playback progress (`md5` correlates back to the service request). |
| `speaker_audio_play_start_progress` | [`events/speaker_audio_play_start_progress.md`](events/speaker_audio_play_start_progress.md) | PSDK audio-playback progress (adds `download` + `encoding` pipeline steps). |
| `psdk_floating_window_text` | [`events/psdk_floating_window_text.md`](events/psdk_floating_window_text.md) | PSDK floating-window text push (outside DRC; mirror of [`drc_psdk_floating_window_text`](drc/drc_psdk_floating_window_text.md)). |
| `psdk_ui_resource_upload_result` | [`events/psdk_ui_resource_upload_result.md`](events/psdk_ui_resource_upload_result.md) | PSDK widget UI-resource tarball uploaded to object storage (`object_key` + `size`). |
| `custom_data_transmission_from_psdk` | [`events/custom_data_transmission_from_psdk.md`](events/custom_data_transmission_from_psdk.md) | **PSDK-Interconnection** passthrough — opaque bytes pushed by PSDK payload. |
| `custom_data_transmission_from_esdk` | [`events/custom_data_transmission_from_esdk.md`](events/custom_data_transmission_from_esdk.md) | **ESDK-Interconnection** passthrough — opaque bytes pushed by aircraft onboard-SDK. |

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
| `live_start_push` | [`services/live_start_push.md`](services/live_start_push.md) | Start a live stream on one of RTMP / GB28181 / WebRTC / Agora (Dock 2). |
| `live_stop_push` | [`services/live_stop_push.md`](services/live_stop_push.md) | Stop an in-progress live stream. |
| `live_set_quality` | [`services/live_set_quality.md`](services/live_set_quality.md) | Change quality (resolution/bitrate) of an in-progress stream. |
| `live_camera_change` | [`services/live_camera_change.md`](services/live_camera_change.md) | Switch FPV camera between inside-the-dock and outside-the-dock. |
| `live_lens_change` | [`services/live_lens_change.md`](services/live_lens_change.md) | Switch aircraft lens (IR / Normal / Wide / Zoom) on an active stream. |
| `upload_flighttask_media_prioritize` | [`services/upload_flighttask_media_prioritize.md`](services/upload_flighttask_media_prioritize.md) | Cloud bumps a flight task to the top of the media-upload queue. |
| `ota_create` | [`services/ota_create.md`](services/ota_create.md) | Deliver firmware artifacts and start an OTA upgrade task. |
| `fileupload_list` | [`services/fileupload_list.md`](services/fileupload_list.md) | Enumerate uploadable log files by module. |
| `fileupload_start` | [`services/fileupload_start.md`](services/fileupload_start.md) | Deliver STS credentials + per-module file list; start log upload. |
| `fileupload_update` | [`services/fileupload_update.md`](services/fileupload_update.md) | Cancel an in-progress log-upload batch. |
| `esim_operator_switch` | [`services/esim_operator_switch.md`](services/esim_operator_switch.md) | Select eSIM carrier on a dongle. |
| `sim_slot_switch` | [`services/sim_slot_switch.md`](services/sim_slot_switch.md) | Switch dongle between physical-SIM and eSIM slots. |
| `esim_activate` | [`services/esim_activate.md`](services/esim_activate.md) | Activate an eSIM profile. |
| `sdr_workmode_switch` | [`services/sdr_workmode_switch.md`](services/sdr_workmode_switch.md) | Select SDR-only vs SDR+4G image transmission. |
| `charge_close` | [`services/charge_close.md`](services/charge_close.md) | Stop aircraft charging. |
| `charge_open` | [`services/charge_open.md`](services/charge_open.md) | Start aircraft charging. |
| `cover_close` | [`services/cover_close.md`](services/cover_close.md) | Close the dock cover. |
| `cover_open` | [`services/cover_open.md`](services/cover_open.md) | Open the dock cover. |
| `drone_format` | [`services/drone_format.md`](services/drone_format.md) | Format the aircraft-side storage. |
| `device_format` | [`services/device_format.md`](services/device_format.md) | Format the dock-side storage. |
| `drone_close` | [`services/drone_close.md`](services/drone_close.md) | Power off the aircraft inside the dock. |
| `drone_open` | [`services/drone_open.md`](services/drone_open.md) | Power on the aircraft inside the dock. |
| `device_reboot` | [`services/device_reboot.md`](services/device_reboot.md) | Reboot the dock. |
| `battery_store_mode_switch` | [`services/battery_store_mode_switch.md`](services/battery_store_mode_switch.md) | Switch aircraft battery between Schedule and Standby modes. |
| `alarm_state_switch` | [`services/alarm_state_switch.md`](services/alarm_state_switch.md) | Enable / disable dock sound-and-light alarm. |
| `air_conditioner_mode_switch` | [`services/air_conditioner_mode_switch.md`](services/air_conditioner_mode_switch.md) | Force dock AC to idle / cooling / heating / dehumidification. |
| `battery_maintenance_switch` | [`services/battery_maintenance_switch.md`](services/battery_maintenance_switch.md) | Enable / disable aircraft-battery maintenance mode. |
| `supplement_light_close` | [`services/supplement_light_close.md`](services/supplement_light_close.md) | Turn off dock auxiliary fill-light. |
| `supplement_light_open` | [`services/supplement_light_open.md`](services/supplement_light_open.md) | Turn on dock auxiliary fill-light. |
| `debug_mode_close` | [`services/debug_mode_close.md`](services/debug_mode_close.md) | Exit remote-debugging mode. |
| `debug_mode_open` | [`services/debug_mode_open.md`](services/debug_mode_open.md) | Enter remote-debugging mode. |
| `cover_force_close` | [`services/cover_force_close.md`](services/cover_force_close.md) | Force the dock cover closed (bypasses safety interlocks). |
| `rtk_calibration` | [`services/rtk_calibration.md`](services/rtk_calibration.md) | Trigger manual RTK calibration (Dock 3 only). |
| `unlock_license_switch` | [`services/unlock_license_switch.md`](services/unlock_license_switch.md) | Enable / disable a single FlySafe unlocking license. |
| `unlock_license_update` | [`services/unlock_license_update.md`](services/unlock_license_update.md) | Push a refreshed FlySafe license file (or trigger online resync). |
| `unlock_license_list` | [`services/unlock_license_list.md`](services/unlock_license_list.md) | Enumerate the unlocking licenses loaded on aircraft or dock. |
| `flight_areas_update` | [`services/flight_areas_update.md`](services/flight_areas_update.md) | Tell the device to refresh its custom-flight-area set (no params). |
| `speaker_play_volume_set` | [`services/speaker_play_volume_set.md`](services/speaker_play_volume_set.md) | Set PSDK speaker volume outside DRC (mirror of [`drc_speaker_play_volume_set`](drc/drc_speaker_play_volume_set.md)). |
| `speaker_play_mode_set` | [`services/speaker_play_mode_set.md`](services/speaker_play_mode_set.md) | Set PSDK speaker single / loop playback mode outside DRC. |
| `speaker_play_stop` | [`services/speaker_play_stop.md`](services/speaker_play_stop.md) | Stop PSDK speaker playback outside DRC. |
| `speaker_replay` | [`services/speaker_replay.md`](services/speaker_replay.md) | Replay last PSDK speaker audio outside DRC. |
| `speaker_tts_play_start` | [`services/speaker_tts_play_start.md`](services/speaker_tts_play_start.md) | Play TTS text on PSDK speaker outside DRC. |
| `speaker_audio_play_start` | [`services/speaker_audio_play_start.md`](services/speaker_audio_play_start.md) | Play pre-recorded audio file on PSDK speaker outside DRC. |
| `psdk_input_box_text_set` | [`services/psdk_input_box_text_set.md`](services/psdk_input_box_text_set.md) | Set PSDK text-box widget content outside DRC. |
| `psdk_widget_value_set` | [`services/psdk_widget_value_set.md`](services/psdk_widget_value_set.md) | Set PSDK generic widget value outside DRC (mirror of [`drc_psdk_widget_value_set`](drc/drc_psdk_widget_value_set.md)). |
| `custom_data_transmission_to_psdk` | [`services/custom_data_transmission_to_psdk.md`](services/custom_data_transmission_to_psdk.md) | **PSDK-Interconnection** passthrough — cloud sends opaque bytes to PSDK payload. |
| `custom_data_transmission_to_esdk` | [`services/custom_data_transmission_to_esdk.md`](services/custom_data_transmission_to_esdk.md) | **ESDK-Interconnection** passthrough — cloud sends opaque bytes to aircraft onboard-SDK. |

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
| `storage_config_get` | [`requests/storage_config_get.md`](requests/storage_config_get.md) | Dock requests short-lived object-storage credentials. `module = 0` = Media (4d); `module = 1` = PSDK UI resources (4g). |
| `flight_areas_get` | [`requests/flight_areas_get.md`](requests/flight_areas_get.md) | Dock pulls the cloud's current custom-flight-area file inventory. |

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

#### Remote-Control events (4e-2)

All `drc_*` methods are filed under `drc/` per the filing-convention decision of 4e-2 (see section [Filing convention](#filing-convention-for-drc-methods) below). Several of these events ride `/events` or `/drc/up` depending on cohort — the doc's topics table captures the per-cohort topic.

| Method | Doc | Purpose |
|---|---|---|
| `drc_psdk_floating_window_text` | [`drc/drc_psdk_floating_window_text.md`](drc/drc_psdk_floating_window_text.md) | PSDK floating-window text push (Dock 3 only, `/events`). |
| `drc_speaker_play_progress` | [`drc/drc_speaker_play_progress.md`](drc/drc_speaker_play_progress.md) | PSDK speaker playback progress (Dock 3 only, `/drc/up`). |
| `drc_psdk_state_info` | [`drc/drc_psdk_state_info.md`](drc/drc_psdk_state_info.md) | PSDK payload state snapshot (speaker + spotlight + widgets; Dock 3 only). |
| `drc_psdk_ui_resource` | [`drc/drc_psdk_ui_resource.md`](drc/drc_psdk_ui_resource.md) | PSDK widget UI-resource tarball ready (Dock 3 only). |
| `drc_drone_state_push` | [`drc/drc_drone_state_push.md`](drc/drc_drone_state_push.md) | Aircraft state push (mode code + lights). **Topic diverges by cohort.** |
| `drc_camera_state_push` | [`drc/drc_camera_state_push.md`](drc/drc_camera_state_push.md) | Camera state push. Dock 3 adds night-mode sub-struct. |
| `drc_camera_osd_info_push` | [`drc/drc_camera_osd_info_push.md`](drc/drc_camera_osd_info_push.md) | Camera OSD (exposure / zoom / IR / liveview FOV). **Topic diverges by cohort.** |
| `drc_ai_info_push` | [`drc/drc_ai_info_push.md`](drc/drc_ai_info_push.md) | AI identify / tracking state (Dock 3 only). |
| `drc_camera_photo_info_push` | [`drc/drc_camera_photo_info_push.md`](drc/drc_camera_photo_info_push.md) | Panorama-capture progress (Dock 2 only; Dock 3 uses [`camera_photo_take_progress`](events/camera_photo_take_progress.md)). |

#### Remote-Control DRC services — Dock 2 + Dock 3 (4e-2)

| Method | Doc | Purpose |
|---|---|---|
| `drc_force_landing` | [`drc/drc_force_landing.md`](drc/drc_force_landing.md) | Land ignoring obstacles (cancellable via `drone_emergency_stop`). |
| `drc_emergency_landing` | [`drc/drc_emergency_landing.md`](drc/drc_emergency_landing.md) | Land, pausing on obstacles. |
| `drc_initial_state_subscribe` | [`drc/drc_initial_state_subscribe.md`](drc/drc_initial_state_subscribe.md) | Re-push all DRC-relevant state values (prime cloud after entering DRC mode). |
| `drc_night_lights_state_set` | [`drc/drc_night_lights_state_set.md`](drc/drc_night_lights_state_set.md) | Enable / disable beacon (night-flight) lights. |
| `drc_stealth_state_set` | [`drc/drc_stealth_state_set.md`](drc/drc_stealth_state_set.md) | Enable / disable stealth mode (all lights off). |
| `drc_camera_aperture_value_set` | [`drc/drc_camera_aperture_value_set.md`](drc/drc_camera_aperture_value_set.md) | Set camera aperture. |
| `drc_camera_shutter_set` | [`drc/drc_camera_shutter_set.md`](drc/drc_camera_shutter_set.md) | Set camera shutter speed. |
| `drc_camera_iso_set` | [`drc/drc_camera_iso_set.md`](drc/drc_camera_iso_set.md) | Set camera ISO. |
| `drc_camera_mechanical_shutter_set` | [`drc/drc_camera_mechanical_shutter_set.md`](drc/drc_camera_mechanical_shutter_set.md) | Enable / disable mechanical shutter (wide-angle). |
| `drc_camera_dewarping_set` | [`drc/drc_camera_dewarping_set.md`](drc/drc_camera_dewarping_set.md) | Enable / disable lens dewarp. |

#### Remote-Control DRC services — Dock 2 legacy (4e-2)

Superseded on Dock 3 by non-DRC equivalents (in `services/`); kept here for Dock 2 support.

| Method | Doc | Purpose |
|---|---|---|
| `drc_camera_mode_switch` | [`drc/drc_camera_mode_switch.md`](drc/drc_camera_mode_switch.md) | Switch camera mode (Dock 2; Dock 3 uses [`camera_mode_switch`](services/camera_mode_switch.md)). |
| `drc_linkage_zoom_set` | [`drc/drc_linkage_zoom_set.md`](drc/drc_linkage_zoom_set.md) | Enable / disable Link Zoom (Dock 2 M3TD only). |
| `drc_video_resolution_set` | [`drc/drc_video_resolution_set.md`](drc/drc_video_resolution_set.md) | Set video resolution (Dock 2 only). |
| `drc_video_storage_set` | [`drc/drc_video_storage_set.md`](drc/drc_video_storage_set.md) | Video storage routing (Dock 2; Dock 3 uses [`video_storage_set`](services/video_storage_set.md)). |
| `drc_photo_storage_set` | [`drc/drc_photo_storage_set.md`](drc/drc_photo_storage_set.md) | Photo storage routing (Dock 2; Dock 3 uses [`photo_storage_set`](services/photo_storage_set.md)). |
| `drc_interval_photo_set` | [`drc/drc_interval_photo_set.md`](drc/drc_interval_photo_set.md) | Set timed-shot interval (Dock 2 only). |

#### Remote-Control DRC services — Dock 3 only (4e-2)

Camera / lens:

| Method | Doc | Purpose |
|---|---|---|
| `drc_camera_night_mode_set` | [`drc/drc_camera_night_mode_set.md`](drc/drc_camera_night_mode_set.md) | Set M4D / M4TD night mode. |
| `drc_camera_denoise_level_set` | [`drc/drc_camera_denoise_level_set.md`](drc/drc_camera_denoise_level_set.md) | Set noise-reduction level (manual night mode only). |
| `drc_camera_night_vision_enable` | [`drc/drc_camera_night_vision_enable.md`](drc/drc_camera_night_vision_enable.md) | Enable / disable night vision (M4TD, zoom ≥ 7×). |
| `drc_infrared_fill_light_enable` | [`drc/drc_infrared_fill_light_enable.md`](drc/drc_infrared_fill_light_enable.md) | Enable / disable near-infrared fill light (M4TD, zoom ≥ 7×). |
| `drc_camera_photo_format_set` | [`drc/drc_camera_photo_format_set.md`](drc/drc_camera_photo_format_set.md) | Set infrared photo format (RJPEG / DLT664). |

PSDK spotlight:

| Method | Doc | Purpose |
|---|---|---|
| `drc_light_brightness_set` | [`drc/drc_light_brightness_set.md`](drc/drc_light_brightness_set.md) | Set PSDK spotlight brightness. |
| `drc_light_mode_set` | [`drc/drc_light_mode_set.md`](drc/drc_light_mode_set.md) | Set PSDK spotlight operating mode. |
| `drc_light_fine_tuning_set` | [`drc/drc_light_fine_tuning_set.md`](drc/drc_light_fine_tuning_set.md) | Fine-tune per-side brightness (with `saved` persistence flag). |
| `drc_light_calibration` | [`drc/drc_light_calibration.md`](drc/drc_light_calibration.md) | Trigger PSDK spotlight gimbal calibration. |

PSDK speaker:

| Method | Doc | Purpose |
|---|---|---|
| `drc_speaker_play_mode_set` | [`drc/drc_speaker_play_mode_set.md`](drc/drc_speaker_play_mode_set.md) | Set speaker playback mode (single / loop). |
| `drc_speaker_tts_set` | [`drc/drc_speaker_tts_set.md`](drc/drc_speaker_tts_set.md) | Configure TTS voice params (volume / gender / language / rate). |
| `drc_speaker_play_volume_set` | [`drc/drc_speaker_play_volume_set.md`](drc/drc_speaker_play_volume_set.md) | Set playback volume. |
| `drc_speaker_play_stop` | [`drc/drc_speaker_play_stop.md`](drc/drc_speaker_play_stop.md) | Stop speaker playback. |
| `drc_speaker_replay` | [`drc/drc_speaker_replay.md`](drc/drc_speaker_replay.md) | Replay most recent audio. |
| `drc_speaker_tts_play_start` | [`drc/drc_speaker_tts_play_start.md`](drc/drc_speaker_tts_play_start.md) | Send TTS text + begin playback (MD5 correlation). |

PSDK widgets:

| Method | Doc | Purpose |
|---|---|---|
| `drc_psdk_input_box_text_set` | [`drc/drc_psdk_input_box_text_set.md`](drc/drc_psdk_input_box_text_set.md) | Set widget input-box text. |
| `drc_psdk_widget_value_set` | [`drc/drc_psdk_widget_value_set.md`](drc/drc_psdk_widget_value_set.md) | Set generic widget value (switch / slider / etc.). |

AI identify:

| Method | Doc | Purpose |
|---|---|---|
| `drc_ai_model_select` | [`drc/drc_ai_model_select.md`](drc/drc_ai_model_select.md) | Select which AI model to use. |
| `drc_ai_identify_set` | [`drc/drc_ai_identify_set.md`](drc/drc_ai_identify_set.md) | Enable / disable AI recognition globally. |
| `drc_ai_spotlight_zoom_set` | [`drc/drc_ai_spotlight_zoom_set.md`](drc/drc_ai_spotlight_zoom_set.md) | Enable / disable AI tracking. |
| `drc_ai_spotlight_zoom_track` | [`drc/drc_ai_spotlight_zoom_track.md`](drc/drc_ai_spotlight_zoom_track.md) | Track a specific recognized target by `target_index`. |
| `drc_ai_spotlight_zoom_select` | [`drc/drc_ai_spotlight_zoom_select.md`](drc/drc_ai_spotlight_zoom_select.md) | Box-select a target region on the liveview. |
| `drc_ai_spotlight_zoom_confirm` | [`drc/drc_ai_spotlight_zoom_confirm.md`](drc/drc_ai_spotlight_zoom_confirm.md) | Confirm the box-selected target. |
| `drc_ai_spotlight_zoom_stop` | [`drc/drc_ai_spotlight_zoom_stop.md`](drc/drc_ai_spotlight_zoom_stop.md) | Stop AI tracking. |
| `drc_ai_identify_score_mode_set` | [`drc/drc_ai_identify_score_mode_set.md`](drc/drc_ai_identify_score_mode_set.md) | Set AI recognition confidence mode. |
| `drc_ai_identify_score_set` | [`drc/drc_ai_identify_score_set.md`](drc/drc_ai_identify_score_set.md) | Set custom AI confidence threshold (`0`–`100`). |
| `drc_ai_identify_score_reset` | [`drc/drc_ai_identify_score_reset.md`](drc/drc_ai_identify_score_reset.md) | Reset AI confidence to default. |
| `drc_ai_identify_filter_set` | [`drc/drc_ai_identify_filter_set.md`](drc/drc_ai_identify_filter_set.md) | Set AI label-filter list (third-party offset `+128`). |

### Filing convention for `drc_*` methods

All methods whose name begins with `drc_` are filed in the `drc/` directory regardless of whether they ride `/drc/down` + `/drc/up`, `/events`, or (rarely, on Dock 2) `/services` + `/services_reply`. The per-doc topics table is the canonical source for the actual topic. This convention keeps the DRC family co-located so a reader can grep `drc/` and find every DRC method in one place — the alternative (splitting by topic) scattered related methods across three folders and broke the "grep for the method name" ergonomic.

Cross-cohort topic divergence (Dock 3 `/events` vs Dock 2 `/drc/up`) is flagged prominently in each affected doc — [`drc_drone_state_push`](drc/drc_drone_state_push.md) and [`drc_camera_osd_info_push`](drc/drc_camera_osd_info_push.md) are the known cases.

### Sub-phase 4f sub-areas

9 methods covering FlySafe unlocking, custom flight areas (CFA), AirSense ADS-B warnings, and HMS. All identical across Dock 2 + Dock 3.

**FlySafe unlocking (3 services, all in `services/`):**

| Method | Doc | Purpose |
|---|---|---|
| `unlock_license_switch` | [`services/unlock_license_switch.md`](services/unlock_license_switch.md) | Toggle a single unlocking license on or off by ID. |
| `unlock_license_update` | [`services/unlock_license_update.md`](services/unlock_license_update.md) | Push a refreshed FlySafe license file (optional `file` → offline; absent → online resync). |
| `unlock_license_list` | [`services/unlock_license_list.md`](services/unlock_license_list.md) | Enumerate the 7 license types loaded on aircraft or dock with `consistence` flag. |

**Custom-Flight-Area (2 events + 1 service + 1 request):**

| Method | Doc | Family | Purpose |
|---|---|---|---|
| `flight_areas_drone_location` | [`events/flight_areas_drone_location.md`](events/flight_areas_drone_location.md) | event | Aircraft per-area distance + inside-state (`need_reply: 0`). |
| `flight_areas_sync_progress` | [`events/flight_areas_sync_progress.md`](events/flight_areas_sync_progress.md) | event | Sync state + 13-code failure-reason enum (`need_reply: 1`). |
| `flight_areas_update` | [`services/flight_areas_update.md`](services/flight_areas_update.md) | service | Cloud asks device to resync (no params). |
| `flight_areas_get` | [`requests/flight_areas_get.md`](requests/flight_areas_get.md) | request | Dock asks cloud for the file list with pre-signed URLs. |

**AirSense (1 event):**

| Method | Doc | Purpose |
|---|---|---|
| `airsense_warning` | [`events/airsense_warning.md`](events/airsense_warning.md) | ADS-B crewed-airplane proximity warning array (5-level severity; `need_reply: 1`). |

**HMS (1 event):**

| Method | Doc | Purpose |
|---|---|---|
| `hms` | [`events/hms.md`](events/hms.md) | Health warning batch (up to 20 entries). Code catalog belongs to Phase 8 (`hms-codes/`). |

### Sub-phase 4g sub-areas

16 methods covering the non-DRC PSDK speaker/widget surface and the PSDK / ESDK interconnection passthrough channels. All identical across Dock 2 + Dock 3. See the [4g filing note](#filing-note-for-4g-psdk-speakerwidget-methods) below for why `speaker_*` and `psdk_*` methods live in `events/` + `services/` while their `drc_*` siblings live in `drc/`.

**PSDK — speaker (2 events + 6 services):**

| Method | Doc | Family | Purpose |
|---|---|---|---|
| `speaker_tts_play_start_progress` | [`events/speaker_tts_play_start_progress.md`](events/speaker_tts_play_start_progress.md) | event | TTS playback progress (`md5` correlation). |
| `speaker_audio_play_start_progress` | [`events/speaker_audio_play_start_progress.md`](events/speaker_audio_play_start_progress.md) | event | Audio playback progress (adds `download` + `encoding` steps). |
| `speaker_play_volume_set` | [`services/speaker_play_volume_set.md`](services/speaker_play_volume_set.md) | service | Set volume `0`–`100`. |
| `speaker_play_mode_set` | [`services/speaker_play_mode_set.md`](services/speaker_play_mode_set.md) | service | Single vs loop playback. |
| `speaker_play_stop` | [`services/speaker_play_stop.md`](services/speaker_play_stop.md) | service | Stop playback. |
| `speaker_replay` | [`services/speaker_replay.md`](services/speaker_replay.md) | service | Replay last audio. |
| `speaker_tts_play_start` | [`services/speaker_tts_play_start.md`](services/speaker_tts_play_start.md) | service | Play TTS text (`tts.md5` correlation). |
| `speaker_audio_play_start` | [`services/speaker_audio_play_start.md`](services/speaker_audio_play_start.md) | service | Play pre-recorded PCM audio (`file.md5` correlation). |

**PSDK — widgets (2 events + 2 services):**

| Method | Doc | Family | Purpose |
|---|---|---|---|
| `psdk_floating_window_text` | [`events/psdk_floating_window_text.md`](events/psdk_floating_window_text.md) | event | Floating-window text push. |
| `psdk_ui_resource_upload_result` | [`events/psdk_ui_resource_upload_result.md`](events/psdk_ui_resource_upload_result.md) | event | Widget UI-resource tarball uploaded (`object_key`). |
| `psdk_input_box_text_set` | [`services/psdk_input_box_text_set.md`](services/psdk_input_box_text_set.md) | service | Set text-box widget content. |
| `psdk_widget_value_set` | [`services/psdk_widget_value_set.md`](services/psdk_widget_value_set.md) | service | Set generic widget value (switch / slider / etc.). |

**PSDK-Interconnection (1 event + 1 service):**

| Method | Doc | Family | Purpose |
|---|---|---|---|
| `custom_data_transmission_from_psdk` | [`events/custom_data_transmission_from_psdk.md`](events/custom_data_transmission_from_psdk.md) | event | Opaque bytes (<256 B) pushed by PSDK payload. |
| `custom_data_transmission_to_psdk` | [`services/custom_data_transmission_to_psdk.md`](services/custom_data_transmission_to_psdk.md) | service | Cloud sends opaque bytes to PSDK payload. |

**ESDK-Interconnection (1 event + 1 service):**

| Method | Doc | Family | Purpose |
|---|---|---|---|
| `custom_data_transmission_from_esdk` | [`events/custom_data_transmission_from_esdk.md`](events/custom_data_transmission_from_esdk.md) | event | Opaque bytes (<256 B) pushed by aircraft ESDK application. |
| `custom_data_transmission_to_esdk` | [`services/custom_data_transmission_to_esdk.md`](services/custom_data_transmission_to_esdk.md) | service | Cloud sends opaque bytes to aircraft ESDK application. |

#### Filing note for 4g PSDK speaker/widget methods

The 4g PSDK speaker + widget methods (`speaker_*` / `psdk_*`) live in `events/` + `services/` because their topic is the standard `/events` + `/services` pair — not `/drc/down` + `/drc/up`. Their DRC-session siblings (with the `drc_` prefix, filed under `drc/` in 4e-2) exist as parallel methods for in-session use. The two sets are **not** aliases: same payload shape, different topic envelopes, different MQTT flow semantics. A cloud that operates the speaker / widget outside of a DRC session must use the 4g methods; inside a session, the 4e-2 `drc_*` counterparts.

The PSDK-Interconnection + ESDK-Interconnection `custom_data_transmission_*` passthrough methods are not DRC-related and have no `drc_*` siblings.

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
