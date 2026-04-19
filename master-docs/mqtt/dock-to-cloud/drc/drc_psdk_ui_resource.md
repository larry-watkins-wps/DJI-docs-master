# `drc_psdk_ui_resource` — PSDK widget UI-resource tarball ready

Event pushed by a PSDK payload after it has uploaded the tarball containing its widget UI resources (HTML/JS/images that render the widget panel in pilot UI) to object storage. The cloud uses this to materialize the widget UI for the operator.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — absent from Dock 2 Remote-Control.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `drc_psdk_ui_resource` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `psdk_index` | int | PSDK payload device index. |
| `psdk_ready` | enum int | `0` = Not ready; `1` = Ready. |
| `object_key` | string | Key in the OSS / S3 bucket where the tarball was uploaded. |

### Example

```json
{
  "data": {
    "object_key": "b4cfaae6-bd9d-4cd0-8472-63b608c3c581/SN/psdk_config/0/2023_6_7_1103_XXXXXX.tar.gz",
    "psdk_index": 0,
    "psdk_ready": 1
  },
  "method": "drc_psdk_ui_resource",
  "seq": 1
}
```

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — only source. |
