# `storage_config_get` — dock requests temporary object-storage credentials

Request by which the dock fetches a short-lived credential bundle for uploading media (photos, videos, logs) to the server's object-storage bucket. The cloud replies with bucket name, endpoint, provider, and STS-style credentials that the dock uses directly against the storage provider's SDK. The dock then follows up with [`file_upload_callback`](../events/file_upload_callback.md) once each file has been uploaded.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, requests-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/requests` | `storage_config_get` |
| Cloud → Device | `thing/product/{gateway_sn}/requests_reply` | `storage_config_get` |

## Request (up) — `data` fields

| Field | Type | Description |
|---|---|---|
| `module` | enum int | Subsystem requesting credentials. `0` = Media. Reserved for future modules. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "module": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "storage_config_get"
}
```

## Reply (down) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero represents an error. |
| `output` | struct | Credential bundle (only meaningful when `result` = `0`). |
| `output.bucket` | string | Object-storage bucket name. |
| `output.endpoint` | string | Endpoint URL the dock connects to. |
| `output.provider` | enum string | Cloud provider. `ali` = Alibaba Cloud, `aws` = Amazon Cloud, `minio` = MinIO. |
| `output.region` | string | Data-center region (e.g., `hz`). |
| `output.object_key_prefix` | string | Prefix the dock must prepend to every uploaded object key. Typically a UUID identifying the device or deployment. |
| `output.credentials` | struct | Short-lived credential material. |
| `output.credentials.access_key_id` | string | Access key ID. |
| `output.credentials.access_key_secret` | string | Secret access key. |
| `output.credentials.security_token` | string | Session token. |
| `output.credentials.expire` | integer | TTL in seconds — after this the dock must re-request credentials before further uploads. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "output": {
      "bucket": "bucket_name",
      "credentials": {
        "access_key_id": "access_key_id",
        "access_key_secret": "access_key_secret",
        "expire": 3600,
        "security_token": "security_token"
      },
      "endpoint": "https://oss-cn-hangzhou.aliyuncs.com",
      "object_key_prefix": "b4cfaae6-bd9d-4cd0-8472-63b608c3c581",
      "provider": "ali",
      "region": "hz"
    },
    "result": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "storage_config_get"
}
```

## Relationship to other methods

- After receiving credentials, the dock uploads files directly to the storage provider (not over MQTT).
- Once a file has been uploaded, the dock reports it via [`file_upload_callback`](../events/file_upload_callback.md) so the cloud can index it.
- Upload ordering can be hinted by the cloud via [`upload_flighttask_media_prioritize`](../services/upload_flighttask_media_prioritize.md) or announced by the dock via [`highest_priority_upload_flighttask_media`](../events/highest_priority_upload_flighttask_media.md).
- Full media-upload flow documented in Phase 9 workflow `workflows/media-upload-from-dock.md`.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/40.file.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Media-Management.txt]` | v1.15 (Dock 2) — identical to v1.11 apart from case of `minio` enum label. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Media-Management.txt]` | v1.15 (Dock 3) — identical payload. |
