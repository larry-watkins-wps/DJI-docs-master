# POST /wayline/api/v1/workspaces/{workspace_id}/favorites

Mark one or more wayline files as favorites for the caller. Operates in batch.

Part of the Phase 3 HTTP endpoint catalog. Shared conventions (URI form, `X-Auth-Token`, response envelope, status codes) live in [`../README.md`](../README.md) and are not restated here.

Companion endpoint for removal: [`favorites-remove.md`](favorites-remove.md).

---

## Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `workspace_id` | path | string | yes | Workspace ID. |
| `id` | path | Array | yes | Wayline file IDs to favorite. See note below. |
| `x-auth-token` | header | string | yes | Access token — see [`../README.md` §4](../README.md#4-request-headers). |

> **Note on the `id` parameter.** DJI's v1.11 and v1.15 sources both list the `id` parameter with `In: path` and `Type: Array` — i.e. the ID collection is said to live in the path. The URL template shown by DJI does not contain an `{id}` segment, so the documentation here is internally inconsistent. Neighboring endpoints (e.g. [`favorites-remove.md`](favorites-remove.md), [`duplicate-name.md`](duplicate-name.md)) carry array collections as query parameters. The working assumption for implementations is that the ID array is in the query (matching the unfavorite path) or in a request body; verify against a concrete client before relying on the path interpretation.

## Request body

DJI documentation does not specify a request body schema. See the `id` parameter note above — the wire location of the ID collection is ambiguous.

## Response — 200 OK

`wayline_service.CreateFavoriteOutput`:

| Field | Type | Description |
|---|---|---|
| `code` | integer | Envelope code — `0` on success. |
| `message` | string | Envelope description. |
| `data.id` | array[string] | IDs of the files successfully favorited. |

### Example

```json
{
  "code": 0,
  "data": {},
  "message": "success"
}
```

(Note: DJI's example body shows empty `data`, while the schema definition shows `data.id` as an array. Either shape may be returned depending on server implementation; the schema is authoritative.)

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/10.https/20.waypoint-management/60.collect-waypointfile-in-batch.md]` | v1.11 canonical — URI, parameter list (with the documented inconsistency), response schema. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-Waypoint-Batch-Favorites-Wayline.txt]` | v1.15 corroboration — same ambiguity. |
