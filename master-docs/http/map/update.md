# PUT /map/api/v1/workspaces/{workspace_id}/elements/{id}

Update an existing map element — rename, change geometry, or restyle.

Part of the Phase 3 HTTP endpoint catalog. Shared conventions (URI form, `X-Auth-Token`, response envelope, status codes) live in [`../README.md`](../README.md) and are not restated here.

Related: [`create.md`](create.md), [`obtain.md`](obtain.md), [`delete.md`](delete.md). WebSocket push companion on successful persistence: `biz_code: map_element_update` — see [`../../websocket/README.md` §4.1](../../websocket/README.md#41-map-elements).

---

## Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `workspace_id` | path | string | yes | Workspace ID. |
| `id` | path | string | yes | Element ID to update. |
| `x-auth-token` | header | string | yes | Access token — see [`../README.md` §4](../README.md#4-request-headers). |
| body | body | `map.ElementUpdateInput` | yes | See **Request body** below. |

## Request body

`map.ElementUpdateInput`:

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | no | New element name. |
| `content` | `map.Content` | no | New geometry + styling. See [`create.md`](create.md) for the full `map.Content` sub-schema (identical, plus the v1.15 `is3d` field). |

### Example request body

```json
{
  "content": {
    "geometry": {
      "coordinates": [null],
      "type": "text"
    },
    "properties": {
      "clampToGround": true,
      "color": "string"
    },
    "type": "text"
  },
  "name": "string"
}
```

## Response — 200 OK

`map.SwagUUIDResp` — same shape as [`create.md`](create.md#response--200-ok). `data.id` echoes the updated element ID.

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
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/10.https/10.map-elements/20.update.md]` | v1.11 canonical — URI, parameter list, schemas, example. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-MapElements-Update-Map-Elements.txt]` | v1.15 corroboration — adds `is3d` to `map.Content.properties`. |
