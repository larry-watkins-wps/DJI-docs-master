# `delay_info_push` — DRC image-transmission link delay

Device → cloud push on the DRC uplink reporting the current latency of the image-transmission command link and the latency of each liveview code stream. Used to let the cloud (and any operator UI layered above it) detect when DRC teleoperation is stalling because the video path has degraded.

Part of the Phase 4 MQTT catalog. Shared conventions (DRC envelope) live in [`../../README.md` §5.8](../../README.md#58-drcup--drcdown--direct-remote-control).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `delay_info_push` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `sdr_cmd_delay` | int (ms) | Image-transmission command-link delay. |
| `liveview_delay_list` | array of struct | Per-code-stream delay list (multi-channel). |
| `liveview_delay_list[].video_id` | string | Code-stream identifier (e.g. `1581BN210004555439234/52-0-0/normal-0`). |
| `liveview_delay_list[].liveview_delay_time` | int (ms) | Delay for that code stream. |

### Example

```json
{
  "method": "delay_info_push",
  "timestamp": 1670415891013,
  "data": {
    "sdr_cmd_delay": 10,
    "liveview_delay_list": [
      {
        "video_id": "1581BN210004555439234/52-0-0/normal-0",
        "liveview_delay_time": 60
      },
      {
        "video_id": "1581BN210004555439234/53-0-0/normal-0",
        "liveview_delay_time": 80
      }
    ]
  }
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
