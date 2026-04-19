# `drc_speaker_play_stop` — stop PSDK speaker playback

DRC command that stops whatever the PSDK speaker is currently playing.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — PSDK speaker payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_speaker_play_stop` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_speaker_play_stop` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `psdk_index` | int | PSDK payload device index. |

### Example

```json
{
  "data": {
    "psdk_index": 2
  },
  "method": "drc_speaker_play_stop",
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
