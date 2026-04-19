# `drc_speaker_tts_set` — configure PSDK speaker TTS parameters

DRC command that configures text-to-speech parameters on the PSDK speaker — volume, voice gender, language, and speaking rate.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — PSDK speaker payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_speaker_tts_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_speaker_tts_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `psdk_index` | int | PSDK payload device index. |
| `volume` | int | TTS volume, `0`–`100` (per [`drc_psdk_state_info.speaker.tts_volume`](drc_psdk_state_info.md)). |
| `type` | enum int | `0` = Male voice; `1` = Female voice. |
| `language` | enum int | `0` = Chinese; `1` = English. |
| `speed` | int | Speaking rate, `0`–`100`. |

DJI's source provides no example JSON for this service.

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

### Example

```json
{
  "data": {
    "result": 0
  },
  "method": "drc_speaker_tts_set",
  "seq": 1
}
```

## Source inconsistencies flagged by DJI's own example

- **Malformed JSON in the Dock 3 constraint columns** — `volume` constraint literal is `{"max":"100","min"0:"","step":"","unit_name":null}` and `speed` constraint is `{"max"100:"","min":"0","step":"","unit_name":null}`. Numbers are embedded inside JSON keys, breaking the JSON. Treat the correct bounds as `max=100, min=0` for both fields (inferred from the surrounding `psdk_state_info` documentation).
- No example JSON for the down side in DJI's source.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — only source. |
