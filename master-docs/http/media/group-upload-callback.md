# POST /media/api/v1/workspaces/{workspace_id}/group-upload-callback

Callback issued after all media files in a file group have finished uploading. Used primarily at the end of a wayline task to signal that the complete media set for that task is persisted — useful for triggering downstream processing (AI inference, dataset assembly, notification to end users).

Part of the Phase 3 HTTP endpoint catalog. Shared conventions (URI form, `X-Auth-Token`, response envelope, status codes) live in [`../README.md`](../README.md) and are not restated here.

---

## Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `workspace_id` | path | string | yes | Workspace ID. |
| `x-auth-token` | header | string | yes | Access token — see [`../README.md` §4](../README.md#4-request-headers). |
| body | body | `storage.FolderUploadCallbackInput` | yes | See **Request body** below. |

## Request body

`storage.FolderUploadCallbackInput`:

| Field | Type | Required | Description |
|---|---|---|---|
| `file_group_id` | string | no | File group ID — shared across all media files from one wayline task. Matches the `file_group_id` in each file's prior [`upload-callback.md`](upload-callback.md) body. |
| `file_count` | integer | yes | Total number of media files in the group. |
| `file_uploaded_count` | integer | yes | Number of files successfully uploaded. |

### Example request body

```json
{
  "file_group_id": "xxx",
  "file_count": 0,
  "file_uploaded_count": 0
}
```

## Response — 200 OK

`storage.FolderUploadCallbackOutput` — standard envelope with empty `data`.

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
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/10.https/30.media-management/50.group-upload-callback.md]` | v1.11 canonical — URI, parameter list, request/response schemas. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-Media-Group-Upload-Callback.txt]` | v1.15 corroboration — identical. |
