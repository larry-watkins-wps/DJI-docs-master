# `drc_camera_screen_split` — split screen enable (DRC channel)

RC-Plus-2-specific DRC variant of [`../../dock-to-cloud/services/camera_screen_split.md`](../../dock-to-cloud/services/camera_screen_split.md). Same semantics — enable or disable the multi-camera split-screen view — delivered on the lightweight DRC channel.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.**

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_camera_screen_split` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_screen_split` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | text | Camera enumeration `{type-subtype-gimbalindex}`. |
| `enable` | bool | `true` = enable split screen; `false` = disable. |

### Example

```json
{
  "data": {
    "enable": true,
    "payload_index": "89-0-0"
  },
  "method": "drc_camera_screen_split",
  "seq": 1
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success. |

### Example

```json
{
  "data": { "result": 0 },
  "method": "drc_camera_screen_split",
  "seq": 1
}
```

### Source inconsistencies flagged by DJI's own example

- **Reply example carries `enable` + `payload_index` instead of `result`.** DJI source's `drc/up` example literally reproduces the down-side fields, which is clearly a copy-paste error. Cloud implementations should emit/expect `{"result": 0}` on the reply as the schema table shows.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Remote-Control.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |
