# `map_element_update` — map element updated

Server push notifying Pilot 2 that a map element has been updated. Payload shape is identical to [`map_element_create`](map_element_create.md) — the full updated element is pushed, not a delta.

Part of the Phase 5 WebSocket catalog. Shared conventions live in [`../README.md`](../README.md).

**Cohort**: **DJI Pilot 2**.

---

## Message identity

| Field | Value |
|---|---|
| `biz_code` | `map_element_update` |
| Family | Map Elements |
| Direction | Server → Pilot 2 |

## `data` fields

Same shape as [`map_element_create`](map_element_create.md#data-fields) — `id`, `group_id`, `name`, `resource.{user_name, type, content}`. `resource.content` is the full replacement GeoJSON Feature.

### Example

```json
{
  "biz_code": "map_element_update",
  "version": "1.0",
  "timestamp": 146052438362,
  "data": {
    "id": "string",
    "name": "string",
    "group_id": "string",
    "resource": {
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
      "type": 0,
      "user_name": "string"
    }
  }
}
```

## Relationship to other methods

- Triggered by the HTTP `map/update.md` (see Phase 3 [`../../http/map/update.md`](../../http/map/update.md)) — server persists the update, then pushes this message.
- Clients should replace the in-memory element keyed by `id` + `group_id` with the new `resource.content`; the push is a full replacement, not a merge.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/20.websocket/10.map-elements/10.message-push.md]` | v1.11 canonical. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-WebSocket-Map-Elements-Push-Message.txt]` | v1.15 — identical shape. |
