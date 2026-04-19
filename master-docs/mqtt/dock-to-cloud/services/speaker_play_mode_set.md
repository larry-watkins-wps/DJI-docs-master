# `speaker_play_mode_set` — set PSDK speaker playback mode

Cloud command that sets the PSDK speaker's playback mode (single-shot or loop) outside of an active DRC session. Sister method to the DRC-session variant [`drc_speaker_play_mode_set`](../drc/drc_speaker_play_mode_set.md).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — PSDK payload. Payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `speaker_play_mode_set` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `speaker_play_mode_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `psdk_index` | integer | PSDK payload device index (`0`–`3`). |
| `play_mode` | enum int | `0` = Single play; `1` = Loop play (single track). |

### Example (down)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "data": {
    "play_mode": 1,
    "psdk_index": 2
  },
  "method": "speaker_play_mode_set",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "timestamp": 1689842974113
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero represents an error. |

### Example (reply)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "result": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "speaker_play_mode_set"
}
```

## Relationship to other methods

- DRC-session equivalent: [`drc_speaker_play_mode_set`](../drc/drc_speaker_play_mode_set.md).

## Source inconsistencies flagged by DJI's own example

- **Dock 3 reply example `"timestamp:"` trailing-colon typo.** Dock 2 + v1.11 spell the key correctly.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/140.psdk.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-PSDK.txt]` | v1.15 (Dock 2) — identical. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-PSDK.txt]` | v1.15 (Dock 3) — identical apart from reply `"timestamp:"` typo. |
