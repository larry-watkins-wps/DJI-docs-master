# `drc_camera_photo_info_push` — panorama-capture progress (Dock 2 legacy)

Event pushed by the Dock 2 aircraft during persistent capture (panorama). Reports current step + percent through the panorama state machine. Superseded on Dock 3 by [`camera_photo_take_progress`](../events/camera_photo_take_progress.md) (non-DRC, standard `/events` topic — landed in 4c).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 only** — absent from Dock 3 Remote-Control. Dock 3 uses the non-DRC `camera_photo_take_progress` instead.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_photo_info_push` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `countdown_time` | int | Countdown for Timed Shot. |
| `result` | int | Capturing result (non-zero represents an error). |
| `status` | enum string | `fail` / `in_progress` / `ok`. |
| `progress.current_step` | enum int | `3000` = Not started / finished, `3002` = Capturing panorama, `3005` = Generating panorama. |
| `progress.percent` | int | `0`–`100`. |
| `ext.camera_mode` | enum int | `3` = Panorama. |

### Example

```json
{
  "data": {
    "countdown_time": 4,
    "ext": {
      "camera_mode": 2
    },
    "progress": {
      "current_step": 0,
      "percent": 100
    },
    "result": 0,
    "status": "in_progress"
  },
  "method": "drc_camera_photo_info_push",
  "seq": 1
}
```

## Source inconsistencies flagged by DJI's own example

- **`progress.current_step` enum is `{3000, 3002, 3005}` but the example sends `0`** (not in the enum). Same class of DJI source typo seen in 4c's [`camera_photo_take_progress`](../events/camera_photo_take_progress.md).
- **`ext.camera_mode` enum only defines `3: Panorama` but the example sends `2`.** Either the schema is incomplete or the example is wrong.

## Relationship to other methods

- **Dock 3 replacement**: [`camera_photo_take_progress`](../events/camera_photo_take_progress.md) (landed in 4c). Dock 3 moves persistent-capture reporting out of the DRC channel onto the standard events topic.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/180.remote-control.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Control.txt]` | v1.15 (Dock 2) — same shape. |
