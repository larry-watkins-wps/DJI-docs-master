# `fileupload_start` — deliver credentials and start uploading log files

Cloud command that hands the dock a short-lived object-storage credential bundle plus the per-module list of `boot_index` log slices to upload. The dock acknowledges immediately with a single-field reply; per-file progress thereafter flows on the [`fileupload_progress`](../events/fileupload_progress.md) event topic.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3. Shares the credential bundle shape with [`storage_config_get`](../requests/storage_config_get.md) but adds the per-module `params.files[]` list.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `fileupload_start` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `fileupload_start` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `bucket` | string | Object-storage bucket name. |
| `region` | string | Region where the data center is located (e.g. `hz`). |
| `endpoint` | string | Access domain for the storage provider (e.g. `https://oss-cn-hangzhou.aliyuncs.com`). |
| `provider` | enum string | Storage provider. `ali` = Alibaba Cloud, `aws` = Amazon Cloud, `minio` = MinIO. All three sources agree on lowercase `minio`. |
| `credentials` | struct | Short-lived credential material. |
| `credentials.access_key_id` | string | Access key ID. |
| `credentials.access_key_secret` | string | Secret access key. |
| `credentials.security_token` | string | Session token. |
| `credentials.expire` | int | Access key expiration time. Schema says `{"step":"1","unit_name":"Seconds / s"}`, but the DJI example uses `1659432522000` — an epoch-ms timestamp, not a TTL in seconds. Treat as epoch-ms. |
| `params.files` | array of struct | One entry per module being uploaded. |
| `params.files[].object_key` | string | Key (path) in the bucket the device should upload under. |
| `params.files[].module` | string | Module these logs belong to. `"0"` = Aircraft, `"3"` = Dock. Schema declares `text`. |
| `params.files[].list` | array of struct | Which boot-sessions to upload. |
| `params.files[].list[].boot_index` | int | `boot_index` value taken from a prior [`fileupload_list`](fileupload_list.md) reply. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "bucket": "stg-dji-service-hz-ksd7",
    "credentials": {
      "access_key_id": "STS.access_key_id",
      "access_key_secret": "access_key_secret",
      "expire": 1659432522000,
      "security_token": "security_token"
    },
    "endpoint": "https://oss-cn-hangzhou.aliyuncs.com",
    "params": {
      "files": [
        {
          "list": [
            {
              "boot_index": 321
            },
            {
              "boot_index": 322
            }
          ],
          "module": "3",
          "object_key": "object_key"
        }
      ]
    },
    "provider": "ali",
    "region": "hz"
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1659429523120,
  "method": "fileupload_start"
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "result": 0
  },
  "gateway": "",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1655781392412,
  "method": "fileupload_start"
}
```

The reply is a plain ACK — it does **not** carry per-file upload status. The actual progress stream is the [`fileupload_progress`](../events/fileupload_progress.md) event.

## Relationship to other methods

- Typically preceded by [`fileupload_list`](fileupload_list.md) (to choose `boot_index` values).
- Followed by [`fileupload_progress`](../events/fileupload_progress.md) events until the batch finishes — but the correlation key is not documented by DJI; see [`OPEN-QUESTIONS.md` OQ-005](../../../OPEN-QUESTIONS.md#oq-005--fileupload_start--fileupload_progress-correlation-key-is-undocumented).
- Cancelled via [`fileupload_update`](fileupload_update.md) with `status: cancel`.
- The credential bundle shape overlaps with [`storage_config_get`](../requests/storage_config_get.md) (which the dock uses for media, not logs). `fileupload_start` is cloud-initiated with a pre-chosen file list; `storage_config_get` is dock-initiated and returns only credentials.

## Source inconsistencies flagged by DJI's own example

- **`expire` unit mismatch.** Schema claims "Seconds / s"; example value is `1659432522000`, which is an epoch-ms timestamp. Treat as epoch-ms. (Compare to [`storage_config_get`](../requests/storage_config_get.md), where `credentials.expire` is documented as a TTL in seconds.)
- **`provider.minio` capitalization.** All three sources (v1.11 Dock 2, v1.15 Dock 2, v1.15 Dock 3) agree on lowercase `"minio"` — contrast the 4d finding where `storage_config_get` v1.11 spelled it `"MinIO"` (camel-caps) while v1.15 is lowercase. `fileupload_start` converged on lowercase earlier.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/90.log.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Log.txt]` | v1.15 (Dock 2) — identical payload. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Log.txt]` | v1.15 (Dock 3) — identical payload. |
