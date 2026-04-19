# `speaker_tts_play_start_progress` — PSDK TTS-playback progress

Event pushed by the dock reporting progress of a TTS (text-to-speech) playback job started by [`speaker_tts_play_start`](../services/speaker_tts_play_start.md). Every pipeline stage emits a progress update: the dock's internal workflow synthesizes the text, uploads the encoded audio to the PSDK payload, and then begins playback. The `md5` field correlates the progress event back to the request.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — PSDK payload. Payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3 apart from an `upload` step-key wording change.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `speaker_tts_play_start_progress` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero represents an error. |
| `output` | struct | Progress snapshot. |
| `output.psdk_index` | integer | PSDK payload device index (`0`–`3`). |
| `output.status` | enum string | `in_progress` = still running; `ok` = playback successful. See inconsistencies note below about `"success"`. |
| `output.md5` | string | MD5 of the TTS file content — acts as the correlation key back to [`speaker_tts_play_start`](../services/speaker_tts_play_start.md). |
| `output.progress` | struct | Progress details. |
| `output.progress.percent` | integer | Overall progress `0`–`100`. |
| `output.progress.step_key` | enum string | Current pipeline step. `change_work_mode` = switch speaker working mode; `upload` = dock uploads audio to the PSDK payload; `play` = start playback. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "data": {
    "output": {
      "md5": "bacee8ed225fa346f6da87f67c914728",
      "progress": {
        "percent": 100,
        "step_key": "play"
      },
      "psdk_index": 2,
      "status": "success"
    },
    "result": 0
  },
  "gateway": "4TADKAQ000002J",
  "method": "speaker_tts_play_start_progress",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "timestamp": 1689911352309
}
```

## Relationship to other methods

- Triggered by [`speaker_tts_play_start`](../services/speaker_tts_play_start.md). The two share the `md5` value.
- The DRC-session equivalent is [`drc_speaker_play_progress`](../drc/drc_speaker_play_progress.md) on `/drc/up` (Dock 3 only; covers both TTS and audio).
- Storage credentials for any PSDK-side uploads use [`storage_config_get`](../requests/storage_config_get.md) with `module = 1`.

## Source inconsistencies flagged by DJI's own example

- **`output.status` example value `"success"` is not in the enum.** Every source example (v1.11 Dock 2, v1.15 Dock 2, v1.15 Dock 3) ships `"status": "success"` alongside `"percent": 100`. The declared enum is `{"in_progress", "ok"}`. Treat `"success"` as a DJI source bug — cloud should accept it as equivalent to `"ok"` or rely on `progress.percent = 100 && progress.step_key = "play"` as the authoritative completion signal.
- **`step_key.upload` wording diverges.** Dock 3 reads "Dock uploads audio to payload"; Dock 2 + v1.11 read "Dock uploads audio to psdk". Enum key is stable.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/140.psdk.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-PSDK.txt]` | v1.15 (Dock 2) — identical payload. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-PSDK.txt]` | v1.15 (Dock 3) — identical payload, `upload` step-key wording differs. |
