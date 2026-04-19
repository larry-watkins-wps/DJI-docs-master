# GET /wayline/api/v1/workspaces/{workspace_id}/waylines/duplicate-names

Given a collection of wayline file names, return the subset that already exist in the workspace. Used by clients before an upload to warn about name collisions or to auto-suffix names.

Part of the Phase 3 HTTP endpoint catalog. Shared conventions (URI form, `X-Auth-Token`, response envelope, status codes) live in [`../README.md`](../README.md) and are not restated here.

---

> **Note on path notation.** DJI's v1.11 and v1.15 sources both show this endpoint's URL as `/wayline/api/v1/workspaces/:workspace_id/waylines/duplicate-names` with colon-style path parameter syntax — the only DJI-documented endpoint in the Pilot-HTTPS surface that doesn't use brace notation. The path parameter is `workspace_id` either way; this catalog normalizes to brace notation for consistency across the corpus.

## Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `workspace_id` | path | string | yes | Workspace ID. |
| `name` | query | array[string] | yes | Wayline file name collection to test for duplicates. |
| `x-auth-token` | header | string | yes | Access token — see [`../README.md` §4](../README.md#4-request-headers). |

## Request body

None.

## Response — 200 OK

Envelope per [`../README.md` §5](../README.md#5-response-envelope). `data` is an array of strings — the subset of submitted names that already exist in the workspace.

### `data`

| Field | Type | Description |
|---|---|---|
| (root) | array[string] | Duplicate file name collection. |

### Example

```json
{
  "code": 0,
  "message": "string",
  "data": ["name1", "name2"]
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/10.https/20.waypoint-management/40.get-duplicated-waypointfile-name.md]` | v1.11 canonical — parameter list, response schema, example body. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-Waypoint-Obtain-Duplicated-Wayline-Name.txt]` | v1.15 corroboration — identical shape. |
