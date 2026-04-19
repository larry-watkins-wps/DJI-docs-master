# `drc_camera_denoise_level_set` — set noise-reduction level (night mode)

DRC command that sets the camera's noise-reduction level while night mode is manually enabled. Takes effect only when `night_mode == 1` (manually enabled) — it is ignored when night mode is Auto or Disabled.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — M4D / M4TD cameras.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_camera_denoise_level_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_denoise_level_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration. |
| `level` | enum int | `2` = Enhanced Noise Reduction (15 fps); `3` = Ultra Noise Reduction (5 fps). |

### Example

```json
{
  "seq": 1,
  "method": "drc_camera_denoise_level_set",
  "data": {
    "payload_index": "99-0-0",
    "level": 2
  }
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

## Source inconsistencies flagged by DJI's own example

- **Enum mismatch with the paired event.** The `drc_camera_denoise_level_set` service enum only defines 2 values (`{2, 3}`), while the [`drc_camera_state_push`](drc_camera_state_push.md) `denoise_level` field declares 4 values (`{0: Disabled, 1: Standard, 2: Enhanced, 3: Super}`). The state push can report values the set command cannot produce — presumably because the low-noise levels (`0` / `1`) are automatically driven rather than operator-selected.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — only source. |
