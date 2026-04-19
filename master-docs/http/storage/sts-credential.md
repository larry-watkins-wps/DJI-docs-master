# POST /storage/api/v1/workspaces/{workspace_id}/sts

Issue short-lived credentials for direct upload to the backing object-storage provider (Alibaba Cloud OSS, AWS S3, or MinIO). Clients use these credentials to upload wayline files and media directly to the storage backend, then call the appropriate `upload-callback` endpoint ([`../wayline/upload-callback.md`](../wayline/upload-callback.md), [`../media/upload-callback.md`](../media/upload-callback.md)) to register the uploaded object with the cloud.

Part of the Phase 3 HTTP endpoint catalog. Shared conventions (URI form, `X-Auth-Token`, response envelope, status codes) live in [`../README.md`](../README.md) and are not restated here.

---

> **Note: single endpoint, two documentation stubs.** DJI's source docs place this endpoint under both the Waypoint Management and Media Management sections of the Pilot-HTTPS catalog — the URL and behavior are identical, but the schema names differ (`storage.GetStsOutput` / `storage.Credentials` under Waypoint; `media.GetStsOutput` / `media.Credentials` under Media). This corpus treats them as one endpoint. The media-section schema adds `minio` to the `provider` enum; the waypoint-section schema only lists `ali` / `aws`. This catalog uses the superset.

## Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `workspace_id` | path | string | yes | Workspace ID. |
| `x-auth-token` | header | string | yes | Access token — see [`../README.md` §4](../README.md#4-request-headers). |

## Request body

None.

## Response — 200 OK

Envelope per [`../README.md` §5](../README.md#5-response-envelope). `data` shape:

### `data`

| Field | Type | Description |
|---|---|---|
| `bucket` | string | Bucket name in the object store. |
| `credentials` | object | Short-lived STS credentials — see sub-schema. |
| `endpoint` | string | Access domain for the object-storage provider (e.g. `https://oss-cn-hangzhou.aliyuncs.com`). |
| `object_key_prefix` | string | Prefix the client must prepend to any object key it uploads (scopes to the workspace). |
| `provider` | string | Object-storage provider enum: `ali`, `aws`, or `minio`. |
| `region` | string | Region of the data center (e.g. `cn-hangzhou`). |

### `credentials` sub-schema

| Field | Type | Description |
|---|---|---|
| `access_key_id` | string | STS access key ID. |
| `access_key_secret` | string | STS access key secret. |
| `expire` | integer | Time-to-live in seconds. |
| `security_token` | string | STS session token. |

### Example

```json
{
  "code": 0,
  "data": {
    "bucket": "string",
    "credentials": {
      "access_key_id": "STS.NUBdKtVadL1U8aBJ2TH6PWoYo",
      "access_key_secret": "9NG2P2yJaUrck576CkdRoRbchKssJiZygi5D93CBsduY",
      "expire": 3600,
      "security_token": "CAIS8AN1q6Ft5B2yfSjIr5b3L/HAu75F+/O+OkfzrjIBRLl8uKryjTz2IHhOenBhB..."
    },
    "endpoint": "https://oss-cn-hangzhou.aliyuncs.com",
    "object_key_prefix": "5a6f9d4b-2a38-4b4b-86f9-3a678da0bf4a",
    "provider": "ali",
    "region": "cn-hangzhou"
  },
  "message": "success"
}
```

(The `security_token` in DJI's sample is truncated here for readability; the full token in the source is ~800 characters. Tokens returned in practice are similarly long opaque strings.)

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/10.https/20.waypoint-management/20.obtain-temporary-credential.md]` | v1.11 canonical (Waypoint section) — URI, parameter list, `storage.GetStsOutput` schema, example. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-Waypoint-Obtain-Temporary-Credential.txt]` | v1.15 corroboration (Waypoint section) — identical shape. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-Media-Obtain-Temporary-Credential.txt]` | v1.15 corroboration (Media section) — same URI; schema adds `minio` to the `provider` enum and shows `region: cn-hangzhou` in the example. |
