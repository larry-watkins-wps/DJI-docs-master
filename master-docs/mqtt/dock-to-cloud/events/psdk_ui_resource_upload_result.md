# `psdk_ui_resource_upload_result` — PSDK UI-resource package upload result

Event pushed by the dock after it has uploaded a PSDK widget UI-resource tarball (iconset, layout definitions) to the cloud's object storage. The cloud uses the reported `object_key` to fetch the resources and render the PSDK widget UI in the operator console. The underlying upload is HTTP directly against the object-storage provider; this MQTT event only announces the outcome.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — PSDK payload. Payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `psdk_ui_resource_upload_result` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `psdk_index` | integer | PSDK payload device index (`0`–`3`). |
| `object_key` | string | Key of the uploaded resource tarball in the cloud's object-storage bucket (use with the `object_key_prefix` / `bucket` returned by [`storage_config_get`](../requests/storage_config_get.md)). |
| `size` | integer | Uploaded file size in bytes. |
| `result` | integer | Return code. `0` = success; non-zero represents an error. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "data": {
    "object_key": "f4a4a171-bb33-45d6-bd3d-b10034f66734/1581F5BLD22BE00A090U_2023_07_21_11_48_33_widget",
    "psdk_index": 2,
    "result": 0,
    "size": 43488
  },
  "gateway": "4TADKAQ000002J",
  "method": "psdk_ui_resource_upload_result",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "timestamp": 1689911315621
}
```

## Relationship to other methods

- The dock requests short-lived credentials for the resource-tarball upload via [`storage_config_get`](../requests/storage_config_get.md) with `module = 1` (PSDK UI resources).
- The DRC-session equivalent is [`drc_psdk_ui_resource`](../drc/drc_psdk_ui_resource.md) on `/drc/up` (Dock 3 only).
- Once the cloud has the tarball it uses widget definitions in the resource package alongside the live [`drc_psdk_state_info`](../drc/drc_psdk_state_info.md) stream to render widget state.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/140.psdk.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-PSDK.txt]` | v1.15 (Dock 2) — identical. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-PSDK.txt]` | v1.15 (Dock 3) — identical. |
