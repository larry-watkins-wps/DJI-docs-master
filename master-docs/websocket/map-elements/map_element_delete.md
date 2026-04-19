# `map_element_delete` — map element deleted

Server push notifying Pilot 2 that a map element has been deleted. Unlike create/update, the delete message carries only the element identifiers (no `resource` body) — clients remove the element keyed by `id` within `group_id`.

Part of the Phase 5 WebSocket catalog. Shared conventions live in [`../README.md`](../README.md).

**Cohort**: **DJI Pilot 2**.

---

## Message identity

| Field | Value |
|---|---|
| `biz_code` | `map_element_delete` |
| Family | Map Elements |
| Direction | Server → Pilot 2 |

## `data` fields

| Field | Type | Description |
|---|---|---|
| `id` | string | Map-element ID to delete. |
| `group_id` | string | Containing map-group ID. |

### Example

```json
{
  "biz_code": "map_element_delete",
  "version": "1.0",
  "timestamp": 146052438362,
  "data": {
    "id": "string",
    "group_id": "string"
  }
}
```

## Relationship to other methods

- Triggered by the HTTP [`../../http/map/delete.md`](../../http/map/delete.md) — server persists the delete, then pushes this message.
- Clients should remove the in-memory element keyed by `id` + `group_id`.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/20.websocket/10.map-elements/10.message-push.md]` | v1.11 canonical. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-WebSocket-Map-Elements-Push-Message.txt]` | v1.15 — identical shape. |
