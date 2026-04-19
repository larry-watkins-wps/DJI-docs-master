# POST /media/api/v1/workspaces/{workspace_id}/upload-callback

Reports the result of a media file upload. Called by the client after it has uploaded a media file (photo, video) directly to object storage using credentials from [`../storage/sts-credential.md`](../storage/sts-credential.md). Ties the uploaded object key back to its capture metadata (position, altitude, gimbal angle, creation time) and file-association context (drone SN, payload model, file group, etc.).

Part of the Phase 3 HTTP endpoint catalog. Shared conventions (URI form, `X-Auth-Token`, response envelope, status codes) live in [`../README.md`](../README.md) and are not restated here.

---

## Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `workspace_id` | path | string | yes | Workspace ID. |
| `x-auth-token` | header | string | yes | Access token — see [`../README.md` §4](../README.md#4-request-headers). |
| body | body | `media.UploadCallbackInput` | yes | See **Request body** below. |

## Request body

`media.UploadCallbackInput`:

| Field | Type | Required | Description |
|---|---|---|---|
| `result` | integer | yes | Upload outcome. `0` = success; non-zero = failure. |
| `name` | string | yes | File name. |
| `object_key` | string | yes | Object storage key of the uploaded file. |
| `fingerprint` | string | no | File fingerprint. |
| `path` | string | no | Business path of the file. |
| `sub_file_type` | integer | no | Photo sub-type: `0` = normal, `1` = panorama. Only meaningful for images. |
| `ext` | `media.MediaFile` | no | File-association attributes — see sub-schema. |
| `metadata` | `media.MetaData` | no | Capture metadata — see sub-schema. |

### `media.MediaFile` sub-schema

Same as in [`fast-upload.md`](fast-upload.md) plus `file_group_id`:

| Field | Type | Required | Description |
|---|---|---|---|
| `file_group_id` | string | no | File group ID — shared across all media files produced by a single wayline task. |
| `drone_model_key` | string | no | Aircraft model enum. |
| `payload_model_key` | string | no | Payload model enum. |
| `tinny_fingerprint` | string | no | Tiny fingerprint (`tinny` verbatim per DJI source). |
| `is_original` | boolean | no | Whether this is the original image. |
| `sn` | string | no | Device serial number. |

### `media.MetaData` sub-schema

| Field | Type | Required | Description |
|---|---|---|---|
| `absolute_altitude` | number | no | Absolute altitude (above mean sea level). |
| `relative_altitude` | integer | no | Relative altitude (above takeoff point). |
| `gimbal_yaw_degree` | number | no | Gimbal yaw at capture, degrees. |
| `created_time` | string | no | Media creation time. |
| `shoot_position` | object | no | `{lat, lng}` capture location. |
| `shoot_position.lat` | integer | no | Latitude of capture. |
| `shoot_position.lng` | integer | no | Longitude of capture. |

### Example request body

```json
{
  "result": 0,
  "ext": {
    "file_group_id": "string",
    "drone_model_key": "string",
    "is_original": true,
    "payload_model_key": "string",
    "tinny_fingerprint": "string",
    "sn": "string"
  },
  "fingerprint": "string",
  "metadata": {
    "absolute_altitude": 0,
    "created_time": "string",
    "gimbal_yaw_degree": 0,
    "relative_altitude": 0,
    "shoot_position": {
      "lat": 0,
      "lng": 0
    }
  },
  "name": "string",
  "object_key": "string",
  "path": "string",
  "sub_file_type": 0
}
```

## Response — 200 OK

`media.UploadCallbackOutput`. `data` shape:

### `data`

| Field | Type | Description |
|---|---|---|
| `object_key` | string | Echoed-back object key of the persisted file. |

### Example

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "object_key": "5asjwu24-2a18-4b4b-86f9-3a678da0bf4d/example.jpg"
  }
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/10.https/30.media-management/40.mediafile-upload-result-report.md]` | v1.11 canonical — URI, parameter list, full request/response schemas, example. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-Media-File-Upload-Result-Report.txt]` | v1.15 corroboration — identical. |
