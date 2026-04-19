# `speaker_audio_play_start` — play pre-recorded audio on PSDK speaker

Cloud command that instructs the PSDK speaker payload to download and play a pre-recorded audio file, outside of an active DRC session. The cloud supplies a URL + MD5; the dock downloads, transcodes PCM → Opus, uploads to the PSDK payload, then plays. Each pipeline stage is reported via [`speaker_audio_play_start_progress`](../events/speaker_audio_play_start_progress.md).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — PSDK payload. Payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `speaker_audio_play_start` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `speaker_audio_play_start` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `psdk_index` | integer | PSDK payload device index. |
| `file` | struct | Audio file descriptor. |
| `file.name` | string | Logical file name. |
| `file.url` | string | Download URL (cloud-issued, dock uses HTTP GET to fetch). |
| `file.md5` | string | MD5 of the audio content — unique identifier + correlation key for [`speaker_audio_play_start_progress`](../events/speaker_audio_play_start_progress.md). |
| `file.format` | enum string | Input file format. Only `pcm` is documented. |

### Example (down)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "data": {
    "file": {
      "format": "pcm",
      "md5": "b38257017001f45ec064b5157b2e4416",
      "name": "20230720162718",
      "url": "https://example.com/5a6f9d4b-2a38-4b4b-86f9-3a678da0bf4a/3dd27366-bf21-41a7-9f07-62b74f2e93a7/fe2f2474-720a-4122-a552-010e1ed08920/20230720162718.webm.pcm"
    },
    "psdk_index": 2
  },
  "method": "speaker_audio_play_start",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "timestamp": 1689912303287
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = accepted; non-zero represents an error. |

### Example (reply)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "result": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "speaker_audio_play_start"
}
```

## Relationship to other methods

- Triggers [`speaker_audio_play_start_progress`](../events/speaker_audio_play_start_progress.md), correlated by `file.md5`.
- Playback mode (single / loop) and volume are set out-of-band with [`speaker_play_mode_set`](speaker_play_mode_set.md) and [`speaker_play_volume_set`](speaker_play_volume_set.md).
- No `drc_speaker_audio_play_start` exists — the DRC-session equivalent only covers TTS (see [`drc_speaker_tts_play_start`](../drc/drc_speaker_tts_play_start.md)).

## Source inconsistencies flagged by DJI's own example

- **Dock 3 reply example `"timestamp:"` trailing-colon typo.** Dock 2 + v1.11 spell the key correctly.
- **Example URL has `.webm.pcm` double extension.** Treat the URL as opaque; the `file.format` field is authoritative for the wire format.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/140.psdk.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-PSDK.txt]` | v1.15 (Dock 2) — identical. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-PSDK.txt]` | v1.15 (Dock 3) — identical apart from reply `"timestamp:"` typo. |
