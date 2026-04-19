# POST /wayline/api/v1/workspaces/{workspace_id}/upload-callback

Reports the result of a wayline file upload. Called by the client after it has uploaded a wayline file directly to object storage using credentials from [`../storage/sts-credential.md`](../storage/sts-credential.md). Ties the uploaded object key back to its wayline-file metadata.

Part of the Phase 3 HTTP endpoint catalog. Shared conventions (URI form, `X-Auth-Token`, response envelope, status codes) live in [`../README.md`](../README.md) and are not restated here.

---

## Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `workspace_id` | path | string | yes | Workspace ID. |
| `x-auth-token` | header | string | yes | Access token — see [`../README.md` §4](../README.md#4-request-headers). |
| body | body | `wayline.UploadCallbackInput` | yes | See **Request body** below. |

## Request body

`wayline.UploadCallbackInput`:

| Field | Type | Required | Description |
|---|---|---|---|
| `metadata` | `wayline.Metadata` | no | Wayline file metadata — see sub-schema. |
| `name` | string | no | Wayline file name. |
| `object_key` | string | yes | Object storage key returned by the STS upload. |

### `wayline.Metadata` sub-schema

| Field | Type | Required | Description |
|---|---|---|---|
| `drone_model_key` | string | no | Aircraft model enum. Full enum catalog in Phase 6. |
| `payload_model_keys` | array[string] | no | Payload model enums. |
| `template_types` | array[integer] | no | Wayline template collection. |

### Example request body

```json
{
  "metadata": {
    "drone_model_key": "string",
    "payload_model_keys": ["string"],
    "template_types": [0]
  },
  "name": "string",
  "object_key": "string"
}
```

## Response — 200 OK

`wayline.BaseResponse` — standard envelope with empty `data`.

### Example

```json
{
  "code": 0,
  "data": {},
  "message": "success"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/10.https/20.waypoint-management/50.waypointfile-upload-result-report.md]` | v1.11 canonical — URI, parameter list, request/response schemas, examples. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-Waypoint-File-Upload-Result-Report.txt]` | v1.15 corroboration — identical shape. |
