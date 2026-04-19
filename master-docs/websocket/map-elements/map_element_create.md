# `map_element_create` — map element created

Server push notifying Pilot 2 that a new map element has been created in the current workspace. `data.resource.content` carries a GeoJSON Feature — the authoritative map-element geometry.

Part of the Phase 5 WebSocket catalog. Shared conventions (session lifecycle, envelope, push-and-fetch pattern) live in [`../README.md`](../README.md).

**Cohort**: **DJI Pilot 2** (pilot-to-cloud WebSocket is pilot-only; no dock equivalent).

---

## Message identity

| Field | Value |
|---|---|
| `biz_code` | `map_element_create` |
| Family | Map Elements |
| Direction | Server → Pilot 2 |

## `data` fields

| Field | Type | Description |
|---|---|---|
| `id` | string | Map-element ID. |
| `group_id` | string | Containing map-group ID. Groups are managed via the HTTP `map/` endpoints (see [`../../http/map/`](../../http/map/)). |
| `name` | string | Element display name. |
| `resource` | object | Element payload container. |
| `resource.user_name` | string | Name of the user who created the element (display-only). |
| `resource.type` | integer | Element type. Canonical enum is maintained by the HTTP `map/` surface; WebSocket echoes the same integer. |
| `resource.content` | object | GeoJSON Feature — `type`, `properties`, `geometry` at the top level, following RFC 7946. Pilot 2 renders this directly on the map. |

### Example

```json
{
  "biz_code": "map_element_create",
  "version": "1.0",
  "timestamp": 146052438362,
  "data": {
    "group_id": "string",
    "id": "string",
    "name": "",
    "resource": {
      "user_name": "string",
      "content": {
        "type": "Feature",
        "properties": {
          "color": "#0091FF"
        },
        "geometry": {
          "type": "LineString",
          "coordinates": [
            [-114.59526255248164, 44.52039593722584],
            [-96.91234166804537, 47.39200791922252],
            [-101.53652432009943, 39.10142503321269]
          ]
        }
      },
      "type": 0
    }
  }
}
```

## Relationship to other methods

- Paired with [`map_element_update`](map_element_update.md) (same payload shape, updated content) and [`map_element_delete`](map_element_delete.md) (same `id` / `group_id` keys, no content body).
- The create operation itself is issued via the HTTP endpoint [`../../http/map/create.md`](../../http/map/create.md) (see Phase 3). Once the server persists the create, it pushes this WebSocket message to all Pilot 2 clients in the same workspace.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/20.websocket/10.map-elements/10.message-push.md]` | v1.11 canonical — payload table + example. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-WebSocket-Map-Elements-Push-Message.txt]` | v1.15 — identical shape. |
