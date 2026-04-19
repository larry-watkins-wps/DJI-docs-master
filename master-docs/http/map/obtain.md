# GET /map/api/v1/workspaces/{workspace_id}/element-groups

List element groups and their elements in a workspace. DJI Pilot 2 calls this to fetch the initial map state and to refresh after a `map_group_refresh` WebSocket push.

Part of the Phase 3 HTTP endpoint catalog. Shared conventions (URI form, `X-Auth-Token`, response envelope, status codes) live in [`../README.md`](../README.md) and are not restated here.

Related: [`create.md`](create.md), [`update.md`](update.md), [`delete.md`](delete.md). WebSocket trigger: `biz_code: map_group_refresh` — see [`../../websocket/README.md` §4.1](../../websocket/README.md#41-map-elements).

---

## Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `workspace_id` | path | string | yes | Workspace ID. |
| `group_id` | query | string | no | Filter to a single element group. |
| `is_distributed` | query | boolean | no | Filter by element-group distributed status. Defaults to `true`. |
| `x-auth-token` | header | string | yes | Access token — see [`../README.md` §4](../README.md#4-request-headers). |

## Request body

None.

## Response — 200 OK

`map.SwagTree`. `data` is a list of element groups, each containing a list of elements.

### `data` (array of `map.ElementGroupOutput`)

| Field | Type | Description |
|---|---|---|
| `id` | string | Element group ID. |
| `name` | string | Element group name. |
| `type` | integer | Element group type: `0` = custom, `1` = default, `2` = App Shared (Pilot adds maps to this group by default). |
| `is_lock` | boolean | If `true`, elements in this group cannot be deleted or modified. |
| `create_time` | integer | Creation time, ms epoch. |
| `elements` | array of `map.ElementItem` | Elements in the group. |

### `map.ElementItem`

| Field | Type | Description |
|---|---|---|
| `id` | string | Element ID. |
| `name` | string | Element name. |
| `create_time` | integer | Creation time, ms epoch. |
| `update_time` | integer | Last update time, ms epoch. |
| `resource` | `map.ResourceItem` | Geometry + styling (see [`create.md`](create.md#mapresourceitem-sub-schema)). |

### Example

```json
{
  "code": 0,
  "message": "success",
  "data": [
    {
      "id": "d275c4e1-d864-4736-8b5d-5f5882ee9bdd",
      "type": 1,
      "name": "string",
      "is_lock": false,
      "create_time": 1637158501230,
      "elements": [
        {
          "id": "6d5da7b4-ac39-42bf-9580-4c8a94c11989",
          "name": "string",
          "create_time": 1637158501230,
          "update_time": 1637158501230,
          "resource": {
            "type": 0,
            "user_name": "name",
            "content": {
              "type": "Feature",
              "properties": {
                "color": "#0091FF",
                "clampToGround": false
              },
              "geometry": {
                "type": "Point",
                "coordinates": [
                  -112.49344909640939,
                  48.18734850103778,
                  40.2
                ]
              }
            }
          }
        }
      ]
    }
  ]
}
```

The live v1.11 example (from the source file) includes three elements — a Point, LineString, and Polygon — demonstrating the three GeoJSON geometry types supported. See the source file for the full example body.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/10.https/10.map-elements/30.obtain.md]` | v1.11 canonical — URI, parameter list, `map.SwagTree` / `map.ElementGroupOutput` / `map.ElementItem` schemas, full three-geometry-type example. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-MapElements-Obtain-Map-Elements.txt]` | v1.15 corroboration — adds `is3d` to `map.Content.properties`. |
