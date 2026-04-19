# `drc_speaker_play_volume_set` — set PSDK speaker playback volume

DRC command that sets the speaker's playback volume (independent of the TTS volume set by [`drc_speaker_tts_set`](drc_speaker_tts_set.md)).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — PSDK speaker payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_speaker_play_volume_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_speaker_play_volume_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `psdk_index` | int | PSDK payload device index. |
| `play_volume` | int | Volume, `1`–`100`. |

### Example

```json
{
  "data": {
    "play_volume": 60,
    "psdk_index": 1
  },
  "method": "drc_speaker_play_volume_set",
  "seq": 1
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — only source. |
