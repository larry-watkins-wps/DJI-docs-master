# DELETE /wayline/api/v1/workspaces/{workspace_id}/favorites

Remove one or more wayline files from the caller's favorites. Operates in batch.

Part of the Phase 3 HTTP endpoint catalog. Shared conventions (URI form, `X-Auth-Token`, response envelope, status codes) live in [`../README.md`](../README.md) and are not restated here.

Companion endpoint for adding favorites: [`favorites-add.md`](favorites-add.md).

---

## Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `workspace_id` | path | string | yes | Workspace ID. |
| `id` | query | array[string] | no | Wayline file ID collection to unfavorite. |
| `x-auth-token` | header | string | yes | Access token — see [`../README.md` §4](../README.md#4-request-headers). |

## Request body

None.

## Response — 200 OK

`wayline.BaseResponse` — standard envelope with `data` typed as `any` (effectively empty in success examples).

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
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/10.https/20.waypoint-management/70.cancel-collect.md]` | v1.11 canonical — parameter list, response schema, example. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-Waypoint-Batch-Unfavorite-Wayline.txt]` | v1.15 corroboration — identical. |
