# `speaker_audio_play_start_progress` — PSDK audio-playback progress

Event pushed by the dock reporting progress of a pre-recorded audio playback job started by [`speaker_audio_play_start`](../services/speaker_audio_play_start.md). Because the audio pipeline adds extra stages (download from cloud, PCM→Opus encoding) to the TTS pipeline, this event declares two additional `step_key` values compared with [`speaker_tts_play_start_progress`](speaker_tts_play_start_progress.md). The `md5` field correlates the progress event back to the request.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — PSDK payload. Payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3 apart from an `upload` step-key wording change.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `speaker_audio_play_start_progress` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero represents an error. |
| `output` | struct | Progress snapshot. |
| `output.psdk_index` | integer | PSDK payload device index (`0`–`3`). |
| `output.status` | enum string | `in_progress` = still running; `ok` = playback successful. |
| `output.md5` | string | MD5 of the audio file — acts as the correlation key back to [`speaker_audio_play_start`](../services/speaker_audio_play_start.md). |
| `output.progress` | struct | Progress details. |
| `output.progress.percent` | integer | Overall progress `0`–`100`. |
| `output.progress.step_key` | enum string | Current pipeline step. `change_work_mode` = switch speaker working mode; `download` = download audio from cloud to dock; `encoding` = encode PCM to Opus; `upload` = dock uploads audio to the PSDK payload; `play` = start playback. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "data": {
    "output": {
      "md5": "e0ecd29bb44d9e08107aaccecdc6cae2",
      "progress": {
        "percent": 89,
        "step_key": "upload"
      },
      "psdk_index": 2,
      "status": "in_progress"
    },
    "result": 0
  },
  "gateway": "4TADKAQ000002J",
  "method": "speaker_audio_play_start_progress",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "timestamp": 1689868551258
}
```

## Relationship to other methods

- Triggered by [`speaker_audio_play_start`](../services/speaker_audio_play_start.md). The two share the `md5` value.
- The DRC-session equivalent is [`drc_speaker_play_progress`](../drc/drc_speaker_play_progress.md) on `/drc/up` (Dock 3 only; covers both TTS and audio).
- Input audio must be PCM; the dock's encoding stage converts to Opus before uploading to the PSDK payload.

## Source inconsistencies flagged by DJI's own example

- **`step_key.upload` wording diverges.** Dock 3 reads "Dock uploads audio to payload"; Dock 2 + v1.11 read "Dock uploads audio to psdk". Enum key is stable.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/140.psdk.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-PSDK.txt]` | v1.15 (Dock 2) — identical payload. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-PSDK.txt]` | v1.15 (Dock 3) — identical payload, `upload` step-key wording differs. |
