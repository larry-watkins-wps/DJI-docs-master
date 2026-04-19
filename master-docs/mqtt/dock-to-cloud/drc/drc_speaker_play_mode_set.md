# `drc_speaker_play_mode_set` — set PSDK speaker playback mode

DRC command that sets whether the PSDK speaker plays audio once (single play) or repeats (loop).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — PSDK speaker payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_speaker_play_mode_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_speaker_play_mode_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `psdk_index` | int | PSDK payload device index. |
| `play_mode` | enum int | `0` = Single play; `1` = Loop play (single track). |

### Example

```json
{
  "data": {
    "play_mode": 1,
    "psdk_index": 1
  },
  "method": "drc_speaker_play_mode_set",
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
