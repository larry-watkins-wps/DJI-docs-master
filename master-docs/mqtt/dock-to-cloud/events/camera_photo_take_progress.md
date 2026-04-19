# `camera_photo_take_progress` — photo-capture progress (panorama)

Event pushed by the dock during long-running photo-capture operations — specifically panorama capture, which runs as "capturing" → "synthesizing" → "finished" — triggered by [`camera_photo_take`](../services/camera_photo_take.md) in the relevant camera mode. Requires reply (`need_reply: 1`).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, request-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `camera_photo_take_progress` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `camera_photo_take_progress` |

## Up — `data` fields

The payload is wrapped by the events envelope in `data.output`, with `data.result` carrying the event-level result code.

### `output` fields

| Field | Type | Description |
|---|---|---|
| `status` | enum string | Capturing state. `in_progress` = executing, `ok` = completed (DJI source spells this `Cpmpleted` — a typo in DJI's table), `fail` = failed. |
| `progress` | struct | Step / percent progress. |
| `progress.current_step` | enum int | Execution step. `3000` = panorama photo capturing is not started or is finished; `3002` = panorama photo is capturing; `3005` = panorama photo is synthesizing. |
| `progress.percent` | integer | Progress, `0`–`100`, step `1`. |
| `ext` | struct | Extended context. |
| `ext.camera_mode` | enum int | Current camera mode. Documented value: `3` = Panorama. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "output": {
      "ext": {
        "camera_mode": 3
      },
      "progress": {
        "current_step": 0,
        "percent": 100
      },
      "status": "ok"
    },
    "result": 0
  },
  "need_reply": 1,
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "camera_photo_take_progress"
}
```

> DJI's own example shows `progress.current_step: 0`, which is not one of the three documented values (`3000 / 3002 / 3005`). The source example is inconsistent with the declared enum; treat the declared enum as authoritative and the example's `0` as a placeholder.

## Down (reply) — `data` fields

Standard events_reply envelope: `data.result` (integer; `0` = success).

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
