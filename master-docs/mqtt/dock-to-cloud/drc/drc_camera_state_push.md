# `drc_camera_state_push` — camera state push

Event pushed by the aircraft reporting camera settings when they change — mode, resolution, photo size, recording state, remaining capacity, night-mode settings (Dock 3 M4TD), and storage routing. Larger struct than [`drc_drone_state_push`](drc_drone_state_push.md) because it tracks the full configuration of each camera.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3**. Payloads differ — Dock 3 adds `photo_format`, `night_mode_settings`, and extends some enums.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_state_push` |

Both cohorts use `/drc/up` (unlike [`drc_drone_state_push`](drc_drone_state_push.md)).

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration value. Format `{type-subtype-gimbalindex}` (e.g. `81-0-0`). |
| `camera_state` | struct | See below. |
| `media_storage` | struct | Storage routing. See below. |

### `camera_state`

| Field | Type | Description |
|---|---|---|
| `camera_mode` | enum int | `0` = Capturing, `1` = Recording, `2` = Smart Low-Light, `3` = Panorama, `4` = Timed Shot. |
| `interval_photo_interval` | int (seconds) | Interval of Timed Shot. |
| `video_resolution` | enum string | `0` = `1920_1080`, `1` = `3840_2160`. |
| `linkage_zoom_state` | bool | Link-Zoom state (`0` = Closed, `1` = Opened). |
| `photo_size` | enum int | `0`–`5` (Default / Extra small / Small / Medium / Large / Extra large). |
| `photo_format` | enum int | **Dock 3 only**. `7` = RJPEG, `16` = DLT664. |
| `record_time` | int (seconds) | Current video-recording duration. |
| `recording_state` | enum int | `0` = Idle, `1` = Recording. |
| `photo_state` | enum int | `0` = Idle, `1` = Capturing. |
| `remain_photo_num` | int | Remaining photo capacity. |
| `remain_record_duration` | int (seconds) | Remaining record time. |

### `camera_state.night_mode_settings` *(Dock 3 only — M4TD night mode)*

| Field | Type | Description |
|---|---|---|
| `night_mode` | enum int | `0` = Disabled, `1` = Enabled, `2` = Auto. |
| `denoise_level` | enum int | `0` = Disabled, `1` = Standard, `2` = Enhanced, `3` = Super. Enhanced affects frame rate. |
| `night_vision_enable` | bool | Only effective at zoom ≥ 7×. |
| `infrared_fill_light_enable` | bool | Only effective at zoom ≥ 7×. |
| `night_scene_mode_suggestion` | enum int | `0` = No suggestions, `1` = Recommend turning on night mode. |
| `is_working` | enum int | `0` = Not effective, `1` = Taking effect. |

### `media_storage`

| Field | Type | Description |
|---|---|---|
| `photo_storage_settings` | array of string | Photo storage routing. Values: `current`, `vision`, `ir`. |
| `video_storage_settings` | array of string | Video storage routing. Values: `current`, `vision`, `ir`. |

### Example (Dock 3 — includes `night_mode_settings`)

```json
{
  "data": {
    "camera_state": {
      "camera_mode": 0,
      "interval_photo_interval": 2.5,
      "linkage_zoom_state": 0,
      "photo_size": 1,
      "photo_state": 0,
      "record_time": 0,
      "recording_state": 0,
      "remain_photo_num": 6727,
      "remain_record_duration": 0,
      "video_resolution": 0,
      "night_mode_settings": {
        "night_mode": 0,
        "denoise_level": 1,
        "night_vision_enable": true,
        "infrared_fill_light_enable": true,
        "night_scene_mode_suggestion": 1,
        "is_working": 1
      }
    },
    "media_storage": {
      "photo_storage_settings": [
        "current",
        "ir"
      ],
      "video_storage_settings": [
        "current",
        "ir"
      ]
    },
    "payload_index": "81-0-0"
  },
  "method": "drc_camera_state_push",
  "seq": 1
}
```

### Example (Dock 2 — no `night_mode_settings`)

```json
{
  "data": {
    "camera_state": {
      "camera_mode": 0,
      "interval_photo_interval": 2.5,
      "linkage_zoom_state": 0,
      "photo_size": 1,
      "photo_state": 0,
      "record_time": 0,
      "recording_state": 0,
      "remain_photo_num": 6727,
      "remain_record_duration": 0,
      "video_resolution": 0
    },
    "media_storage": {
      "photo_storage_settings": [
        "current",
        "ir"
      ],
      "video_storage_settings": [
        "current",
        "ir"
      ]
    },
    "payload_index": "81-0-0"
  },
  "method": "drc_camera_state_push",
  "seq": 1
}
```

## Source differences

- Dock 3 adds `photo_format` (RJPEG / DLT664) and the full `night_mode_settings` sub-struct. Dock 2 + v1.11 do not carry these fields.
- Dock 2 `interval_photo_interval` is declared `int` but the example shows `2.5` (not an integer). Treat as numeric; the DJI-declared interval enum is at [`drc_interval_photo_set`](drc_interval_photo_set.md).

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/180.remote-control.md]` | v1.11 canonical (Dock 2) — no `night_mode_settings` / `photo_format`. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Control.txt]` | v1.15 (Dock 2) — same as v1.11. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — adds Dock-3-only fields. |
