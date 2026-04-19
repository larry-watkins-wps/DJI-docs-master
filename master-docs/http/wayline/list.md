# GET /wayline/api/v1/workspaces/{workspace_id}/waylines

List wayline files in a workspace, with optional filtering by favorited state, template type, aircraft model, and payload model. Supports pagination and ordering.

Part of the Phase 3 HTTP endpoint catalog. Shared conventions (URI form, `X-Auth-Token`, response envelope, status codes, pagination) live in [`../README.md`](../README.md) and are not restated here.

---

## Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `workspace_id` | path | string | yes | Workspace ID. |
| `favorited` | query | boolean | no | Filter to favorited waylines only. |
| `order_by` | query | string | no | Order clause — `xxx_column desc` or `xxx_column asc`. |
| `page` | query | integer | no | 1-indexed page number. |
| `page_size` | query | integer | no | Page size. |
| `template_type` | query | array[integer] | no | Filter by template type collection. |
| `action_type` | query | integer | no | `1` = filter to AI Spot-Check waylines only; omit to include all. |
| `drone_model_keys` | query | array[string] | no | Filter by aircraft model enum (e.g. `0-67-0`). |
| `payload_model_key` | query | array[string] | no | Filter by payload model enum (e.g. `1-53-0`). |
| `x-auth-token` | header | string | yes | Access token — see [`../README.md` §4](../README.md#4-request-headers). |

## Request body

None.

## Response — 200 OK

Envelope per [`../README.md` §5](../README.md#5-response-envelope). `data` shape:

### `data`

| Field | Type | Description |
|---|---|---|
| `list` | array of `AppFileItem` | Waylines matching the filters on the current page. |
| `pagination` | `api_render.PagyInfo` | See [`../README.md` §5.1](../README.md#51-pagination). |

### `AppFileItem`

| Field | Type | Description |
|---|---|---|
| `id` | string | Wayline file ID (UUID). |
| `name` | string | Wayline file name. |
| `drone_model_key` | string | Aircraft model enum. Full enum catalog in Phase 6 (`device-properties/`). |
| `payload_model_keys` | array[string] | Payload model enums. |
| `template_types` | array[integer] | Wayline template types. |
| `action_type` | integer | `1` = AI Spot-Check wayline. |
| `favorited` | boolean | Whether the caller has favorited this wayline. |
| `update_time` | integer | Last update time, ms epoch. |
| `user_name` | string | Uploader username. |
| `start_wayline_point` | object | `{start_latitude, start_lontitude}`. DJI's source spells longitude `lontitude` — preserved verbatim. |
| `start_wayline_point.start_latitude` | float | Latitude of the wayline's first point. |
| `start_wayline_point.start_lontitude` | float | Longitude of the wayline's first point. |

### Example

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "list": [
      {
        "id": "uuid",
        "drone_model_key": "0-67-0",
        "favorited": false,
        "name": "New wayline 1",
        "payload_model_keys": ["1-53-0"],
        "template_types": [0],
        "action_type": 0,
        "update_time": 1637158501230,
        "user_name": "string",
        "start_wayline_point": {
          "start_latitude": 22.5799601837589,
          "start_lontitude": 113.942744030171
        }
      }
    ],
    "pagination": {
      "page": 1,
      "page_size": 9,
      "total": 10
    }
  }
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/10.https/20.waypoint-management/10.obtain-waypointfile-list.md]` | v1.11 canonical — parameter list, `AppFileItem` schema, response body. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-Waypoint-Obtain-Wayline-List.txt]` | v1.15 corroboration — identical endpoint, identical shape. |
