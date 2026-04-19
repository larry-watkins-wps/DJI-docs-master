# `drc_speaker_play_progress` — PSDK speaker playback progress

Event pushed by a PSDK speaker payload reporting playback state — download, encoding (for TTS conversion), upload to the aircraft, and actual playback. Matches the state-machine used by [`drc_speaker_tts_play_start`](drc_speaker_tts_play_start.md) and `drc_speaker_replay`.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — absent from Dock 2 Remote-Control.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_speaker_play_progress` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `psdk_index` | int | PSDK payload device index. |
| `result` | enum int | `0` = success. |
| `status` | enum string | `in_progress` / `failed` / `success`. |
| `progress` | struct | Progress detail. |
| `progress.step_key` | enum string | Current step. `change_work_mode` = working / switching mode, `download` = downloading audio, `encoding` = converting, `play` = playing, `tts_processing` = TTS playing, `upload` = upload. |
| `progress.percent` | int | `1`–`100`. |
| `md5` | string | MD5 checksum of the audio file (the correlation handle matching [`drc_speaker_tts_play_start.tts.md5`](drc_speaker_tts_play_start.md) or an equivalent audio identifier). |

DJI's source provides no example JSON for this event.

## Source inconsistencies flagged by DJI's own example

- **`md5` has a dual type declaration in the Dock 3 schema** — the column lists both `int` and `string` as the type (two separate type cells on the same row). Treat as string per conventional MD5 encoding.
- **No example JSON** provided in source.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — only source. |
