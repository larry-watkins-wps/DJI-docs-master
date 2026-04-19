# `drc_psdk_state_info` — PSDK payload state snapshot

Event pushed by a PSDK payload reporting its full configuration and runtime state — speaker settings, spotlight settings, developer-defined custom widget values. Emitted on connect, on meaningful state change, and in response to [`drc_initial_state_subscribe`](drc_initial_state_subscribe.md). Struct shape is large; client code typically cherry-picks fields.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — absent from Dock 2 Remote-Control.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `drc_psdk_state_info` |

Rides the standard `/events` topic — `seq` serves as the in-order sequence key per the DRC pattern.

## Up — `data` fields

Top-level fields plus two sub-structs (`speaker`, `light`) that are only populated when the payload has the matching capability.

### Top-level

| Field | Type | Description |
|---|---|---|
| `psdk_index` | int | PSDK payload device index. |
| `psdk_type` | enum int | `4` = Third party, `5` = DJI developed. |
| `psdk_name` | enum string | Known names: `Searchlight` = Spotlight, `Speaker` = Speaker. |
| `psdk_sn` | string | Payload serial number. |
| `psdk_version` | string | Firmware version. |
| `psdk_lib_version` | string | PSDK lib version the payload is running. |

### `speaker` sub-struct

| Field | Type | Description |
|---|---|---|
| `speaker.work_mode` | int | Speaker operating mode. |
| `speaker.play_mode` | enum int | `0` = Single play; `1` = Loop play (single track). |
| `speaker.system_state` | enum int | `0` = Idle, `1` = Transmitting (dock → aircraft), `2` = Playing, `3` = Abnormal, `4` = TTS text-conversion in progress, `99` = Downloading (dock → cloud). |
| `speaker.play_volume` | int | `1`–`100`. |
| `speaker.play_file_name` | string | Current audio filename. |
| `speaker.play_file_md5` | string | MD5 of current audio file. |
| `speaker.tts_volume` | int | TTS playback volume, `1`–`100`. |
| `speaker.tts_type` | enum int | `0` = Male voice; `1` = Female voice. |
| `speaker.tts_language` | enum int | `0` = Chinese; `1` = English. |
| `speaker.tts_speed` | int | TTS speech rate, `1`–`100`. |

### `light` sub-struct

| Field | Type | Description |
|---|---|---|
| `light.work_mode` | int | Spotlight operating mode. |
| `light.brightness` | int | Current brightness setting. |
| `light.calibration_status` | enum int | `0` = Complete, `1` = Calibrating, `2` = Failed. |
| `light.calibration_progress` | int | Calibration progress. |
| `light.left_value` | int | Left-light value, `1`–`100`. |
| `light.right_value` | int | Right-light value, `1`–`100`. |
| `light.wide_field_mode` | bool | Wide-field mode enabled. |
| `light.light_gimbal_control` | bool | Spotlight / gimbal linkage enabled. |

### `values` sub-struct (developer-defined widgets)

| Field | Type | Description |
|---|---|---|
| `values.index` | int | Widget index. |
| `values.value` | int | Widget value (semantics defined by the PSDK developer). |

DJI's source provides no example JSON for this event.

## Source inconsistencies flagged by DJI's own example

- **No example JSON** provided in source.
- `values` is documented as a `struct` but the DJI description implies it's keyed by `index` (suggesting it should be an array of structs or a map). Treat the declared shape as the authoritative schema.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — only source. |
