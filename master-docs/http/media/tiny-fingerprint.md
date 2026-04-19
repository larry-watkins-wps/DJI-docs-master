# POST /media/api/v1/workspaces/{workspace_id}/files/tiny-fingerprints

Given a collection of tiny fingerprints, return the subset that already exist in the workspace. The tiny fingerprint is a lightweight pre-check — smaller and faster to compute than the full file fingerprint — used by clients to decide which files to subject to the fast-upload / full-upload flow.

Part of the Phase 3 HTTP endpoint catalog. Shared conventions (URI form, `X-Auth-Token`, response envelope, status codes) live in [`../README.md`](../README.md) and are not restated here.

---

## Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `workspace_id` | path | string | yes | Workspace ID. |
| `x-auth-token` | header | string | yes | Access token — see [`../README.md` §4](../README.md#4-request-headers). |
| `tiny_fingerprints` | body | array[string] | yes | Tiny fingerprint collection to test. |

> **Note on body shape.** DJI's source lists `tiny_fingerprints` with `In: body` and `Type: array[string]`. This is DJI's way of saying the request body is a JSON object with a single field `tiny_fingerprints` whose value is an array of strings — i.e. `{"tiny_fingerprints": [...]}` — consistent with how neighboring endpoints structure their bodies. The literal `array[string]` body shape (a bare JSON array at the root) is not indicated elsewhere in the surface, and `Content-Type: application/json` with a field-wrapped object is the safe interpretation.

## Response — 200 OK

Envelope per [`../README.md` §5](../README.md#5-response-envelope). `data` shape:

### `data`

| Field | Type | Description |
|---|---|---|
| `tiny_fingerprints` | array[string] | Subset of submitted tiny fingerprints that already exist in workspace storage. |

### Example

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "tiny_fingerprints": [
      "5aec4c6e78052bf38fab901bcd1a2319_2021_12_8_22_13_10"
    ]
  }
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/10.https/30.media-management/20.obtain-exited-tiny-fingerprint.md]` | v1.11 canonical — URI, parameter list, `media.GetTinyFingerprintsOutput` schema, example. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-Media-Obtain-Exist-File-Tiny-Fingerprint.txt]` | v1.15 corroboration — identical. |
