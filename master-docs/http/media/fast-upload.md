# POST /media/api/v1/workspaces/{workspace_id}/fast-upload

File-skip / "instant upload" entry point. If a media file with the same fingerprint already exists in workspace storage, the server acknowledges the file without requiring the client to upload its bytes — useful when a file was previously uploaded from another device in the same workspace. If the file does not exist, the client falls back to the STS-credential upload flow ([`../storage/sts-credential.md`](../storage/sts-credential.md) → direct PUT → [`upload-callback.md`](upload-callback.md)).

Part of the Phase 3 HTTP endpoint catalog. Shared conventions (URI form, `X-Auth-Token`, response envelope, status codes) live in [`../README.md`](../README.md) and are not restated here.

---

## Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `workspace_id` | path | string | yes | Workspace ID. |
| `x-auth-token` | header | string | yes | Access token — see [`../README.md` §4](../README.md#4-request-headers). |
| body | body | `media.FastUploadInput` | yes | See **Request body** below. |

## Request body

`media.FastUploadInput`:

| Field | Type | Required | Description |
|---|---|---|---|
| `fingerprint` | string | yes | File fingerprint — the primary lookup key for "does this file already exist?". |
| `name` | string | no | File name. |
| `path` | string | no | Business path of the file. |
| `ext` | `media.MediaFile` | no | Extended file-association attributes — see sub-schema. |

### `media.MediaFile` sub-schema

| Field | Type | Required | Description |
|---|---|---|---|
| `drone_model_key` | string | no | Aircraft model enum. Full enum catalog in Phase 6. |
| `payload_model_key` | string | no | Payload model enum. |
| `tinny_fingerprint` | string | no | Tiny fingerprint — DJI's source spells it `tinny` verbatim. |
| `is_original` | boolean | no | Whether this is the original (non-transcoded) image. |
| `sn` | string | no | Device serial number. |

### Example request body

```json
{
  "ext": {
    "drone_model_key": "string",
    "is_original": true,
    "payload_model_key": "string",
    "tinny_fingerprint": "string",
    "sn": "string"
  },
  "fingerprint": "string",
  "name": "string",
  "path": "string"
}
```

## Response — 200 OK

`media.FastUploadOutput` — standard envelope with empty `data` on success.

### Example

```json
{
  "code": 0,
  "message": "success",
  "data": {}
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/10.https/30.media-management/10.fast-upload.md]` | v1.11 canonical — URI, parameter list, `media.FastUploadInput` schema, example. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-Media-Fast-Upload.txt]` | v1.15 corroboration — identical. |
