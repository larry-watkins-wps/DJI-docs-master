# POST /map/api/v1/workspaces/{workspace_id}/element-groups/{group_id}/elements

Create a map element (pin point, line, or polygon) inside an element group. Used by Pilot 2 and web clients to persist map annotations.

Part of the Phase 3 HTTP endpoint catalog. Shared conventions (URI form, `X-Auth-Token`, response envelope, status codes) live in [`../README.md`](../README.md) and are not restated here.

Related: [`update.md`](update.md), [`obtain.md`](obtain.md), [`delete.md`](delete.md). WebSocket push companion on successful persistence: `biz_code: map_element_create` — see [`../../websocket/README.md` §4.1](../../websocket/README.md#41-map-elements).

---

## Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `workspace_id` | path | string | yes | Workspace ID. |
| `group_id` | path | string | yes | Element group ID the new element belongs to. |
| `x-auth-token` | header | string | yes | Access token — see [`../README.md` §4](../README.md#4-request-headers). |
| body | body | `map.ElementCreateInput` | yes | See **Request body** below. |

## Request body

`map.ElementCreateInput`:

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Element ID (UUID, caller-assigned). |
| `name` | string | yes | Element name. |
| `resource` | `map.ResourceItem` | yes | Element geometry and styling — see sub-schema. |

### `map.ResourceItem` sub-schema

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | integer | no | Resource type: `0` = pin point, `1` = line, `2` = polygon. |
| `content` | `map.Content` | no | GeoJSON-shaped geometry and properties — see sub-schema. |

### `map.Content` sub-schema

Mirrors a GeoJSON Feature.

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string | no | GeoJSON feature type (typically `"Feature"`). |
| `geometry.type` | string | no | GeoJSON geometry type: `"Point"`, `"LineString"`, or `"Polygon"`. |
| `geometry.coordinates` | array | no | Coordinates — see GeoJSON spec. |
| `properties.color` | string | no | Supported colors: `#2D8CF0` (blue), `#19BE6B` (green), `#FFBB00` (yellow), `#B620E0` (orange — DJI documents this as the "ORANGE" slot with purple-ish hex), `#E23C39` (red), `#212121` (purple). |
| `properties.clampToGround` | boolean | no | Whether the element is clamped to ground. |
| `properties.is3d` | boolean | no | Whether the element is a spatial (3-D) line or surface. **v1.15 only** — not present in v1.11. |

### Example request body

```json
{
  "id": "string",
  "name": "string",
  "resource": {
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
    "type": 0
  }
}
```

## Response — 200 OK

`map.SwagUUIDResp`. `data` shape:

### `data`

| Field | Type | Description |
|---|---|---|
| `id` | string | ID of the created element. |

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
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/10.https/10.map-elements/10.create.md]` | v1.11 canonical — URI, parameter list, schemas, example. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-MapElements-Create-Map-Elements.txt]` | v1.15 corroboration — adds `is3d` to `map.Content.properties`. |
