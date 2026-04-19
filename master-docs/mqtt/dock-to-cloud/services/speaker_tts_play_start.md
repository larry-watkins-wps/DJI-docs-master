# `speaker_tts_play_start` — play TTS audio on PSDK speaker

Cloud command that instructs the PSDK speaker payload to synthesize and play a short TTS (text-to-speech) message, outside of an active DRC session. The cloud supplies the text and the file identifier; the dock's internal workflow handles synthesis → transcode → PSDK upload → playback, and reports stage-by-stage progress via [`speaker_tts_play_start_progress`](../events/speaker_tts_play_start_progress.md). The `md5` is the correlation key.

Sister method to the DRC-session variant [`drc_speaker_tts_play_start`](../drc/drc_speaker_tts_play_start.md).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — PSDK payload. Payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `speaker_tts_play_start` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `speaker_tts_play_start` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `psdk_index` | integer | PSDK payload device index. |
| `tts` | struct | TTS payload. |
| `tts.name` | string | Logical file name of the TTS snippet. |
| `tts.text` | string | Text content to be synthesized. |
| `tts.md5` | string | MD5 of the file content — acts as the unique identifier the dock uses to cache synthesized audio, and as the correlation key in [`speaker_tts_play_start_progress`](../events/speaker_tts_play_start_progress.md). |

### Example (down)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "data": {
    "psdk_index": 2,
    "tts": {
      "md5": "0bfb9bceee974f41a6ddfd81521bd795",
      "name": "1111",
      "text": "1111"
    }
  },
  "method": "speaker_tts_play_start",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "timestamp": 1689860575397
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = accepted (playback will proceed; watch progress event for completion); non-zero represents an error. |

### Example (reply)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "result": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "speaker_tts_play_start"
}
```

## Relationship to other methods

- Triggers [`speaker_tts_play_start_progress`](../events/speaker_tts_play_start_progress.md) events, correlated by `md5`.
- DRC-session equivalent: [`drc_speaker_tts_play_start`](../drc/drc_speaker_tts_play_start.md).
- Playback mode (single / loop) and volume are set out-of-band with [`speaker_play_mode_set`](speaker_play_mode_set.md) and [`speaker_play_volume_set`](speaker_play_volume_set.md).

## Source inconsistencies flagged by DJI's own example

- **Dock 3 reply example `"timestamp:"` trailing-colon typo.** Dock 2 + v1.11 spell the key correctly.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/140.psdk.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-PSDK.txt]` | v1.15 (Dock 2) — identical. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-PSDK.txt]` | v1.15 (Dock 3) — identical apart from reply `"timestamp:"` typo. |
