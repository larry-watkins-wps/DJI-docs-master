# Pilot-to-Cloud MQTT catalog

Per-method documentation of everything the **RC Plus 2 Enterprise** (pairs with M4D) and **RC Pro Enterprise** (pairs with M3D / M3TD) emit on, and receive over, MQTT. Each entry uses the envelope and topic-taxonomy conventions from [`../README.md`](../README.md) (Phase 2) — don't restate those here.

Pilot-to-cloud and dock-to-cloud share the same 13-topic taxonomy and envelope (verified envelope-identical during Phase 2). The key difference is the meaning of `{gateway_sn}` vs `{device_sn}`:

- On pilot-to-cloud: `{gateway_sn}` is the **RC's** serial number. The sub-device aircraft is identified in the topology's `sub_devices[0].sn` (M4D / M3D / M3TD). For device-scoped telemetry topics (`thing/product/{device_sn}/osd`, `thing/product/{device_sn}/state`) the `{device_sn}` is the aircraft's serial.
- On dock-to-cloud: `{gateway_sn}` is the **dock's** serial; sub-device is the M4D / M3D / M3TD.

This catalog is structured so that methods shared with the dock-to-cloud surface **link directly** to the [dock-to-cloud](../dock-to-cloud/README.md) docs for the schema, examples, and enum definitions — only pilot-specific additions and variants get their own doc files. This avoids ~70 near-duplicate pointer files while preserving grep-by-method-name via the tables below.

Per-method files are named verbatim after the DJI `method` string (e.g., `poi_mode_enter.md`) so that searches for a method name hit the filename directly.

---

## Catalog status

| Sub-phase | Feature area | Status |
|---|---|---|
| 4h | Pilot-to-cloud — RC Plus 2 Enterprise + RC Pro Enterprise | **landing 2026-04-19** |

## Cohort conventions

- **RC Plus 2 Enterprise** — current generation. v1.15 only (no v1.11 counterpart). Pairs with M4D / M4TD. Sources: `DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-*.txt`.
- **RC Pro Enterprise** — older generation. v1.11 + v1.15. Pairs with M3D / M3TD. Sources: `DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-*.txt` and `Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/*.md`.
- Out of scope: the older `DJI_CloudAPI_RC-*.txt` files (paired with M30/M30T/M300/M350/Mavic 3 Enterprise) — tracked in source inventory for completeness only.

## Filing conventions (4h)

1. **Full docs for methods new to pilot-to-cloud.** 8 NEW methods + 19 pilot-specific DRC variants = 27 new doc files.
2. **Parallel-method tables for dock-to-cloud overlaps.** ~64 methods that ride the same schema as a dock-to-cloud doc (just with the RC as `{gateway_sn}`) are cross-cited from the tables below rather than given their own files. Wire payloads are identical — re-documenting them would add churn with no new information. Cohort markers annotate which RC model sends each.
3. **DRC family in `drc/`.** Same convention as 4e-2 — any `drc_*` method or any method on `/drc/down` or `/drc/up` topics lives in `drc/`.

## Current catalog

### `status/`

Topics under `sys/product/{gateway_sn}/status`. `{gateway_sn}` = RC serial number.

| Method | Doc | Purpose |
|---|---|---|
| `update_topo` | [`status/update_topo.md`](status/update_topo.md) | RC reports its own state and the paired aircraft. |

### `events/` — new to pilot-to-cloud

Topics under `thing/product/{gateway_sn}/events`. Device → cloud pushes.

| Method | Doc | Purpose | Cohort |
|---|---|---|---|
| `cloud_control_auth_notify` | [`events/cloud_control_auth_notify.md`](events/cloud_control_auth_notify.md) | Pilot-side user response to a cloud-control authorization request (`canceled` / `failed` / `ok`). | RC Plus 2 + RC Pro |
| `poi_status_notify` | [`events/poi_status_notify.md`](events/poi_status_notify.md) | POI-circle status (radius, speed, max speed, entry/exit reason). | RC Plus 2 only |

### `events/` — parallels of dock-to-cloud events

Same payload as the cited dock-to-cloud doc; the only difference is that `{gateway_sn}` is the RC's serial. See each dock-to-cloud doc for schema, enum definitions, and examples.

| Method | Dock-to-cloud reference | Cohort |
|---|---|---|
| `fly_to_point_progress` | [`../dock-to-cloud/events/fly_to_point_progress.md`](../dock-to-cloud/events/fly_to_point_progress.md) | RC Plus 2 only |
| `takeoff_to_point_progress` | [`../dock-to-cloud/events/takeoff_to_point_progress.md`](../dock-to-cloud/events/takeoff_to_point_progress.md) | RC Plus 2 only |
| `drc_status_notify` | [`../dock-to-cloud/events/drc_status_notify.md`](../dock-to-cloud/events/drc_status_notify.md) | RC Plus 2 + RC Pro (abandoned in v1.15; use `drc_state` state property or `heart_beat`). |
| `joystick_invalid_notify` | [`../dock-to-cloud/events/joystick_invalid_notify.md`](../dock-to-cloud/events/joystick_invalid_notify.md) | RC Plus 2 only |
| `camera_photo_take_progress` | [`../dock-to-cloud/events/camera_photo_take_progress.md`](../dock-to-cloud/events/camera_photo_take_progress.md) | RC Plus 2 + RC Pro |
| `return_home_info` | [`../dock-to-cloud/events/return_home_info.md`](../dock-to-cloud/events/return_home_info.md) | RC Plus 2 only |

### `services/` — new to pilot-to-cloud

Topics under `thing/product/{gateway_sn}/services`. Cloud → device commands.

| Method | Doc | Purpose | Cohort |
|---|---|---|---|
| `cloud_control_auth_request` | [`services/cloud_control_auth_request.md`](services/cloud_control_auth_request.md) | Cloud requests flight-control authority; triggers pop-up on the RC. | RC Plus 2 + RC Pro |
| `cloud_control_release` | [`services/cloud_control_release.md`](services/cloud_control_release.md) | Cloud releases a previously acquired authority. | RC Plus 2 + RC Pro |
| `poi_mode_enter` | [`services/poi_mode_enter.md`](services/poi_mode_enter.md) | Enter Point-of-Interest circle mode about a latitude/longitude/height. | RC Plus 2 only |
| `poi_mode_exit` | [`services/poi_mode_exit.md`](services/poi_mode_exit.md) | Exit POI mode. | RC Plus 2 only |
| `poi_circle_speed_set` | [`services/poi_circle_speed_set.md`](services/poi_circle_speed_set.md) | Adjust circle speed (sign = direction). | RC Plus 2 only |

### `services/` — parallels of dock-to-cloud services

| Method | Dock-to-cloud reference | Cohort |
|---|---|---|
| `drc_mode_enter` | [`../dock-to-cloud/services/drc_mode_enter.md`](../dock-to-cloud/services/drc_mode_enter.md) | RC Plus 2 + RC Pro |
| `drc_mode_exit` | [`../dock-to-cloud/services/drc_mode_exit.md`](../dock-to-cloud/services/drc_mode_exit.md) | RC Plus 2 + RC Pro |
| `takeoff_to_point` | [`../dock-to-cloud/services/takeoff_to_point.md`](../dock-to-cloud/services/takeoff_to_point.md) | RC Plus 2 only |
| `fly_to_point` | [`../dock-to-cloud/services/fly_to_point.md`](../dock-to-cloud/services/fly_to_point.md) | RC Plus 2 only |
| `fly_to_point_stop` | [`../dock-to-cloud/services/fly_to_point_stop.md`](../dock-to-cloud/services/fly_to_point_stop.md) | RC Plus 2 only |
| `fly_to_point_update` | [`../dock-to-cloud/services/fly_to_point_update.md`](../dock-to-cloud/services/fly_to_point_update.md) | RC Plus 2 only |
| `return_home` | [`../dock-to-cloud/services/return_home.md`](../dock-to-cloud/services/return_home.md) | RC Plus 2 only |
| `return_home_cancel` | [`../dock-to-cloud/services/return_home_cancel.md`](../dock-to-cloud/services/return_home_cancel.md) | RC Plus 2 only |
| `camera_mode_switch` | [`../dock-to-cloud/services/camera_mode_switch.md`](../dock-to-cloud/services/camera_mode_switch.md) | RC Pro |
| `camera_recording_start` | [`../dock-to-cloud/services/camera_recording_start.md`](../dock-to-cloud/services/camera_recording_start.md) | RC Pro |
| `camera_recording_stop` | [`../dock-to-cloud/services/camera_recording_stop.md`](../dock-to-cloud/services/camera_recording_stop.md) | RC Pro |
| `camera_screen_drag` | [`../dock-to-cloud/services/camera_screen_drag.md`](../dock-to-cloud/services/camera_screen_drag.md) | RC Pro |
| `camera_aim` | [`../dock-to-cloud/services/camera_aim.md`](../dock-to-cloud/services/camera_aim.md) | RC Pro |
| `camera_focal_length_set` | [`../dock-to-cloud/services/camera_focal_length_set.md`](../dock-to-cloud/services/camera_focal_length_set.md) | RC Pro |
| `gimbal_reset` | [`../dock-to-cloud/services/gimbal_reset.md`](../dock-to-cloud/services/gimbal_reset.md) | RC Pro |
| `camera_look_at` | [`../dock-to-cloud/services/camera_look_at.md`](../dock-to-cloud/services/camera_look_at.md) | RC Pro |
| `camera_screen_split` | [`../dock-to-cloud/services/camera_screen_split.md`](../dock-to-cloud/services/camera_screen_split.md) | RC Pro |
| `photo_storage_set` | [`../dock-to-cloud/services/photo_storage_set.md`](../dock-to-cloud/services/photo_storage_set.md) | RC Pro |
| `video_storage_set` | [`../dock-to-cloud/services/video_storage_set.md`](../dock-to-cloud/services/video_storage_set.md) | RC Pro |
| `camera_frame_zoom` | [`../dock-to-cloud/services/camera_frame_zoom.md`](../dock-to-cloud/services/camera_frame_zoom.md) | RC Pro |
| `ir_metering_area_set` | [`../dock-to-cloud/services/ir_metering_area_set.md`](../dock-to-cloud/services/ir_metering_area_set.md) | RC Pro |
| `ir_metering_point_set` | [`../dock-to-cloud/services/ir_metering_point_set.md`](../dock-to-cloud/services/ir_metering_point_set.md) | RC Pro |
| `ir_metering_mode_set` | [`../dock-to-cloud/services/ir_metering_mode_set.md`](../dock-to-cloud/services/ir_metering_mode_set.md) | RC Pro |
| `camera_point_focus_action` | [`../dock-to-cloud/services/camera_point_focus_action.md`](../dock-to-cloud/services/camera_point_focus_action.md) | RC Pro |
| `camera_focus_value_set` | [`../dock-to-cloud/services/camera_focus_value_set.md`](../dock-to-cloud/services/camera_focus_value_set.md) | RC Pro |
| `camera_focus_mode_set` | [`../dock-to-cloud/services/camera_focus_mode_set.md`](../dock-to-cloud/services/camera_focus_mode_set.md) | RC Pro |
| `camera_exposure_set` | [`../dock-to-cloud/services/camera_exposure_set.md`](../dock-to-cloud/services/camera_exposure_set.md) | RC Pro |
| `camera_exposure_mode_set` | [`../dock-to-cloud/services/camera_exposure_mode_set.md`](../dock-to-cloud/services/camera_exposure_mode_set.md) | RC Pro |
| `camera_photo_stop` | [`../dock-to-cloud/services/camera_photo_stop.md`](../dock-to-cloud/services/camera_photo_stop.md) | RC Pro |
| `camera_photo_take` | [`../dock-to-cloud/services/camera_photo_take.md`](../dock-to-cloud/services/camera_photo_take.md) | RC Pro |
| `live_start_push` | [`../dock-to-cloud/services/live_start_push.md`](../dock-to-cloud/services/live_start_push.md) | RC Plus 2 + RC Pro. RC Plus 2 still supports Agora (`url_type: 0`); Dock 3 does not. |
| `live_stop_push` | [`../dock-to-cloud/services/live_stop_push.md`](../dock-to-cloud/services/live_stop_push.md) | RC Plus 2 + RC Pro |
| `live_set_quality` | [`../dock-to-cloud/services/live_set_quality.md`](../dock-to-cloud/services/live_set_quality.md) | RC Plus 2 + RC Pro |
| `live_lens_change` | [`../dock-to-cloud/services/live_lens_change.md`](../dock-to-cloud/services/live_lens_change.md) | RC Pro. RC Plus 2 uses [`drc/drc_live_lens_change.md`](drc/drc_live_lens_change.md) instead, on the `/drc/down` channel. |

### `drc/` — new to pilot-to-cloud

Same filing convention as dock-to-cloud 4e-2 — all `drc_*` prefixed methods and methods carried on `/drc/down` / `/drc/up` live here regardless of whether the reply lands on `/services_reply` or `/drc/up`. DRC envelope is lightweight (no `tid`/`bid`/`timestamp`, just `method` + `seq` + `data`).

**Pilot-side DRC camera variants** (RC Plus 2 only) — these are drc-prefixed variants of the dock-to-cloud 4c camera / IR / gimbal services. Same semantic intent as the non-prefixed method, delivered over the lightweight DRC channel instead of the standard services channel.

| Method | Doc | Dock-to-cloud parallel |
|---|---|---|
| `drc_live_lens_change` | [`drc/drc_live_lens_change.md`](drc/drc_live_lens_change.md) | [`../dock-to-cloud/services/live_lens_change.md`](../dock-to-cloud/services/live_lens_change.md) |
| `drc_camera_recording_start` | [`drc/drc_camera_recording_start.md`](drc/drc_camera_recording_start.md) | [`../dock-to-cloud/services/camera_recording_start.md`](../dock-to-cloud/services/camera_recording_start.md) |
| `drc_camera_recording_stop` | [`drc/drc_camera_recording_stop.md`](drc/drc_camera_recording_stop.md) | [`../dock-to-cloud/services/camera_recording_stop.md`](../dock-to-cloud/services/camera_recording_stop.md) |
| `drc_camera_screen_drag` | [`drc/drc_camera_screen_drag.md`](drc/drc_camera_screen_drag.md) | [`../dock-to-cloud/services/camera_screen_drag.md`](../dock-to-cloud/services/camera_screen_drag.md) |
| `drc_camera_aim` | [`drc/drc_camera_aim.md`](drc/drc_camera_aim.md) | [`../dock-to-cloud/services/camera_aim.md`](../dock-to-cloud/services/camera_aim.md) |
| `drc_camera_focal_length_set` | [`drc/drc_camera_focal_length_set.md`](drc/drc_camera_focal_length_set.md) | [`../dock-to-cloud/services/camera_focal_length_set.md`](../dock-to-cloud/services/camera_focal_length_set.md) |
| `drc_gimbal_reset` | [`drc/drc_gimbal_reset.md`](drc/drc_gimbal_reset.md) | [`../dock-to-cloud/services/gimbal_reset.md`](../dock-to-cloud/services/gimbal_reset.md) |
| `drc_camera_look_at` | [`drc/drc_camera_look_at.md`](drc/drc_camera_look_at.md) | [`../dock-to-cloud/services/camera_look_at.md`](../dock-to-cloud/services/camera_look_at.md) |
| `drc_camera_screen_split` | [`drc/drc_camera_screen_split.md`](drc/drc_camera_screen_split.md) | [`../dock-to-cloud/services/camera_screen_split.md`](../dock-to-cloud/services/camera_screen_split.md) |
| `drc_camera_frame_zoom` | [`drc/drc_camera_frame_zoom.md`](drc/drc_camera_frame_zoom.md) | [`../dock-to-cloud/services/camera_frame_zoom.md`](../dock-to-cloud/services/camera_frame_zoom.md) |
| `drc_ir_metering_area_set` | [`drc/drc_ir_metering_area_set.md`](drc/drc_ir_metering_area_set.md) | [`../dock-to-cloud/services/ir_metering_area_set.md`](../dock-to-cloud/services/ir_metering_area_set.md) |
| `drc_ir_metering_point_set` | [`drc/drc_ir_metering_point_set.md`](drc/drc_ir_metering_point_set.md) | [`../dock-to-cloud/services/ir_metering_point_set.md`](../dock-to-cloud/services/ir_metering_point_set.md) |
| `drc_ir_metering_mode_set` | [`drc/drc_ir_metering_mode_set.md`](drc/drc_ir_metering_mode_set.md) | [`../dock-to-cloud/services/ir_metering_mode_set.md`](../dock-to-cloud/services/ir_metering_mode_set.md) |
| `drc_camera_point_focus_action` | [`drc/drc_camera_point_focus_action.md`](drc/drc_camera_point_focus_action.md) | [`../dock-to-cloud/services/camera_point_focus_action.md`](../dock-to-cloud/services/camera_point_focus_action.md) |
| `drc_camera_focus_value_set` | [`drc/drc_camera_focus_value_set.md`](drc/drc_camera_focus_value_set.md) | [`../dock-to-cloud/services/camera_focus_value_set.md`](../dock-to-cloud/services/camera_focus_value_set.md) |
| `drc_camera_focus_mode_set` | [`drc/drc_camera_focus_mode_set.md`](drc/drc_camera_focus_mode_set.md) | [`../dock-to-cloud/services/camera_focus_mode_set.md`](../dock-to-cloud/services/camera_focus_mode_set.md) |
| `drc_camera_exposure_set` | [`drc/drc_camera_exposure_set.md`](drc/drc_camera_exposure_set.md) | [`../dock-to-cloud/services/camera_exposure_set.md`](../dock-to-cloud/services/camera_exposure_set.md) |
| `drc_camera_exposure_mode_set` | [`drc/drc_camera_exposure_mode_set.md`](drc/drc_camera_exposure_mode_set.md) | [`../dock-to-cloud/services/camera_exposure_mode_set.md`](../dock-to-cloud/services/camera_exposure_mode_set.md) |
| `drc_camera_photo_stop` | [`drc/drc_camera_photo_stop.md`](drc/drc_camera_photo_stop.md) | [`../dock-to-cloud/services/camera_photo_stop.md`](../dock-to-cloud/services/camera_photo_stop.md) |
| `drc_camera_photo_take` | [`drc/drc_camera_photo_take.md`](drc/drc_camera_photo_take.md) | [`../dock-to-cloud/services/camera_photo_take.md`](../dock-to-cloud/services/camera_photo_take.md) |

### `drc/` — parallels of dock-to-cloud `drc/`

Same DRC-envelope payload as the cited dock-to-cloud doc. RC Plus 2 and/or RC Pro send or receive them with the RC as `{gateway_sn}`.

| Method | Dock-to-cloud reference | Cohort |
|---|---|---|
| `heart_beat` | [`../dock-to-cloud/drc/heart_beat.md`](../dock-to-cloud/drc/heart_beat.md) | RC Plus 2 + RC Pro |
| `osd_info_push` | [`../dock-to-cloud/drc/osd_info_push.md`](../dock-to-cloud/drc/osd_info_push.md) | RC Plus 2 + RC Pro |
| `hsi_info_push` | [`../dock-to-cloud/drc/hsi_info_push.md`](../dock-to-cloud/drc/hsi_info_push.md) | RC Plus 2 + RC Pro |
| `delay_info_push` | [`../dock-to-cloud/drc/delay_info_push.md`](../dock-to-cloud/drc/delay_info_push.md) | RC Plus 2 + RC Pro |
| `stick_control` | [`../dock-to-cloud/drc/stick_control.md`](../dock-to-cloud/drc/stick_control.md) | RC Plus 2 |
| `drone_emergency_stop` | [`../dock-to-cloud/drc/drone_emergency_stop.md`](../dock-to-cloud/drc/drone_emergency_stop.md) | RC Plus 2 |
| `drc_initial_state_subscribe` | [`../dock-to-cloud/drc/drc_initial_state_subscribe.md`](../dock-to-cloud/drc/drc_initial_state_subscribe.md) | RC Plus 2 + RC Pro |
| `drc_drone_state_push` | [`../dock-to-cloud/drc/drc_drone_state_push.md`](../dock-to-cloud/drc/drc_drone_state_push.md) | RC Plus 2 + RC Pro. RC Plus 2 uses `/drc/up`; RC Pro also uses `/drc/up` (matches Dock 2 pattern, unlike Dock 3 which moved to `/events`). |
| `drc_camera_osd_info_push` | [`../dock-to-cloud/drc/drc_camera_osd_info_push.md`](../dock-to-cloud/drc/drc_camera_osd_info_push.md) | RC Plus 2 + RC Pro. Topic split mirrors `drc_drone_state_push` above. |
| `drc_camera_state_push` | [`../dock-to-cloud/drc/drc_camera_state_push.md`](../dock-to-cloud/drc/drc_camera_state_push.md) | RC Plus 2 |
| `drc_camera_photo_info_push` | [`../dock-to-cloud/drc/drc_camera_photo_info_push.md`](../dock-to-cloud/drc/drc_camera_photo_info_push.md) | RC Plus 2 |
| `drc_camera_dewarping_set` | [`../dock-to-cloud/drc/drc_camera_dewarping_set.md`](../dock-to-cloud/drc/drc_camera_dewarping_set.md) | RC Plus 2 |
| `drc_camera_mechanical_shutter_set` | [`../dock-to-cloud/drc/drc_camera_mechanical_shutter_set.md`](../dock-to-cloud/drc/drc_camera_mechanical_shutter_set.md) | RC Plus 2 |
| `drc_camera_iso_set` | [`../dock-to-cloud/drc/drc_camera_iso_set.md`](../dock-to-cloud/drc/drc_camera_iso_set.md) | RC Plus 2 |
| `drc_camera_shutter_set` | [`../dock-to-cloud/drc/drc_camera_shutter_set.md`](../dock-to-cloud/drc/drc_camera_shutter_set.md) | RC Plus 2 |
| `drc_camera_aperture_value_set` | [`../dock-to-cloud/drc/drc_camera_aperture_value_set.md`](../dock-to-cloud/drc/drc_camera_aperture_value_set.md) | RC Plus 2 |
| `drc_stealth_state_set` | [`../dock-to-cloud/drc/drc_stealth_state_set.md`](../dock-to-cloud/drc/drc_stealth_state_set.md) | RC Plus 2 |
| `drc_night_lights_state_set` | [`../dock-to-cloud/drc/drc_night_lights_state_set.md`](../dock-to-cloud/drc/drc_night_lights_state_set.md) | RC Plus 2 |
| `drc_camera_mode_switch` | [`../dock-to-cloud/drc/drc_camera_mode_switch.md`](../dock-to-cloud/drc/drc_camera_mode_switch.md) | RC Plus 2 |
| `drc_interval_photo_set` | [`../dock-to-cloud/drc/drc_interval_photo_set.md`](../dock-to-cloud/drc/drc_interval_photo_set.md) | RC Plus 2 |
| `drc_photo_storage_set` | [`../dock-to-cloud/drc/drc_photo_storage_set.md`](../dock-to-cloud/drc/drc_photo_storage_set.md) | RC Plus 2 |
| `drc_video_storage_set` | [`../dock-to-cloud/drc/drc_video_storage_set.md`](../dock-to-cloud/drc/drc_video_storage_set.md) | RC Plus 2 |
| `drc_video_resolution_set` | [`../dock-to-cloud/drc/drc_video_resolution_set.md`](../dock-to-cloud/drc/drc_video_resolution_set.md) | RC Plus 2 |
| `drc_linkage_zoom_set` | [`../dock-to-cloud/drc/drc_linkage_zoom_set.md`](../dock-to-cloud/drc/drc_linkage_zoom_set.md) | RC Plus 2 |
| `drc_emergency_landing` | [`../dock-to-cloud/drc/drc_emergency_landing.md`](../dock-to-cloud/drc/drc_emergency_landing.md) | RC Plus 2 |
| `drc_force_landing` | [`../dock-to-cloud/drc/drc_force_landing.md`](../dock-to-cloud/drc/drc_force_landing.md) | RC Plus 2 |

---

## Property families (`osd/`, `state/`, `property/set`)

Deferred to **Phase 4i** — property-family shells per device that link to the Phase 6 `device-properties/` catalog. RC Plus 2 + RC Pro property tables live at `DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt` + `DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt`.

## DJI-source inconsistencies flagged during 4h drafting

Carry into Phase 9 workflow authoring:

- **Pervasive `"timestamp:"` trailing-colon typo in RC Plus 2 Live-Stream examples.** Every method example in `DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Stream.txt` has the typo (`"timestamp:": 1654070968655` instead of `"timestamp": 1654070968655`). Matches the Dock 3 pattern first flagged in 4c. RC Pro Live-Stream is clean. Flagged inline in affected docs.
- **`poi_status_notify` 14-digit timestamp in example.** DJI ships `"timestamp": 16540709686556` (14 digits) instead of 13-digit epoch-ms. Matches the 4f pervasive 14-digit typo.
- **RC Plus 2 `live_start_push` still documents Agora** (`url_type: 0`) while Dock 3 dropped Agora from its enum in 4d. Cohort split: pilot-to-cloud (RC Plus 2 + RC Pro) supports all four protocols; dock-to-cloud Dock 3 only supports RTMP / GB28181 / WebRTC. The shared dock-to-cloud doc `live_start_push.md` already calls this out in its enum; re-cited here for pilot clarity.
- **v1.11 RC Pro `update_topo` uses `thing_version`** instead of the older `version` field the Dock 2 v1.11 uses. Dock 2 v1.15 and Dock 3 v1.15 also use `thing_version`. Effectively a Dock-2-v1.11 anomaly; the canonical field name is `thing_version`.
- **`drc_live_lens_change` is RC Plus 2 only, on the `/drc/down` channel.** RC Pro and the dock-to-cloud surface both use the non-prefixed `live_lens_change` on `/services`. Same semantic intent; different transport envelope.
- **Dock 3 has `live_camera_change`** (switch FPV-vs-payload camera source). Pilot-to-cloud does **not** have this method — the RC is the video source endpoint, not the aircraft, so there is no equivalent "switch camera source" control over the pilot-to-cloud path.

## Source provenance roll-up

| Cohort | v1.11 canonical | v1.15 extract |
|---|---|---|
| RC Plus 2 Enterprise | — (no v1.11 counterpart; current-gen only in v1.15) | `DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Device-Management.txt`, `…Live-Flight-Controls.txt`, `…Live-Stream.txt`, `…Remote-Control.txt` |
| RC Pro Enterprise | `Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/10.device.md`, `20.live.md`, `30.drc.md`, `40.remote-control.md` | `DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Device-Management.txt`, `…Live-Flight-Controls.txt`, `…Live-Stream.txt`, `…Remote-Control.txt` |
| Topic taxonomy | `Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/00.topic-definition.md` | `DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt` |
