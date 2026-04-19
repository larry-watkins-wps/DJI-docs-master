# DELETE /map/api/v1/workspaces/{workspace_id}/elements/{id}

Delete a map element.

Part of the Phase 3 HTTP endpoint catalog. Shared conventions (URI form, `X-Auth-Token`, response envelope, status codes) live in [`../README.md`](../README.md) and are not restated here.

Related: [`create.md`](create.md), [`update.md`](update.md), [`obtain.md`](obtain.md). WebSocket push companion on successful deletion: `biz_code: map_element_delete` — see [`../../websocket/README.md` §4.1](../../websocket/README.md#41-map-elements).

---

## Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `workspace_id` | path | string | yes | Workspace ID. |
| `id` | path | string | yes | Element ID to delete. See note below. |
| `x-auth-token` | header | string | yes | Access token — see [`../README.md` §4](../README.md#4-request-headers). |

> **Note on `id` type.** DJI's v1.11 and v1.15 sources list `id` with `Type: integer`. The values seen in actual responses (e.g. `"94c51c50-f111-45e8-ac8c-4f96c93ced44"` in [`create.md`](create.md#example) and [`obtain.md`](obtain.md#example)) are UUID strings, not integers. This catalog lists `id` as `string` to match the wire behavior; the DJI source annotation is a documentation error.

## Request body

None.

## Response — 200 OK

`map.SwagUUIDResp` — echoes back the deleted element ID in `data.id`.

### Example

```json
{
  "code": 0,
  "data": {
    "id": "94c51c50-f111-45e8-ac8c-4f96c93ced44"
  },
  "message": "success"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/10.https/10.map-elements/40.delete.md]` | v1.11 canonical — URI, parameter list, response schema, example. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-MapElements-Delete-Map-Elements.txt]` | v1.15 corroboration — identical. |
