# `drc_speaker_tts_play_start` — send TTS text and begin playback

DRC command that sends a piece of TTS text to the PSDK speaker and starts playback. The `tts.md5` is the dock-side identifier for the audio — the speaker will use it to recognize / dedupe already-downloaded clips and to correlate with [`drc_speaker_play_progress`](drc_speaker_play_progress.md) events.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — PSDK speaker payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_speaker_tts_play_start` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_speaker_tts_play_start` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `psdk_index` | int | PSDK payload device index. |
| `tts` | struct | TTS payload. |
| `tts.name` | string | Filename (for dock-side caching). |
| `tts.text` | string | Text content to synthesize. |
| `tts.md5` | string | MD5 checksum of the file content — unique identifier that the dock uses to dedupe. |

### Example

```json
{
  "data": {
    "psdk_index": 2,
    "tts": {
      "md5": "ACDEFQD33D31C212",
      "name": "",
      "text": ""
    }
  },
  "method": "drc_speaker_tts_play_start",
  "seq": 1
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

## Relationship to other methods

- Progress stream: [`drc_speaker_play_progress`](drc_speaker_play_progress.md) (the `md5` field on the progress event is the correlation key).
- Configure TTS voice params first via [`drc_speaker_tts_set`](drc_speaker_tts_set.md).

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — only source. |
