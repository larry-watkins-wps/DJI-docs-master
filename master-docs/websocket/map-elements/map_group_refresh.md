# `map_group_refresh` — refresh map-element list

Server push notifying Pilot 2 that a set of map elements should be re-fetched. Unlike per-element create/update/delete, this message is a batch-refresh signal: it carries a list of element IDs but no content, telling Pilot 2 to re-fetch those elements' full state from the HTTP `map/` surface.

Used when the server has made multiple changes to a group's elements and wants Pilot 2 to reconcile its in-memory state via a single HTTP fetch rather than a stream of per-element pushes.

Part of the Phase 5 WebSocket catalog. Shared conventions live in [`../README.md`](../README.md).

**Cohort**: **DJI Pilot 2**.

---

## Message identity

| Field | Value |
|---|---|
| `biz_code` | `map_group_refresh` |
| Family | Map Elements |
| Direction | Server → Pilot 2 |

## `data` fields

| Field | Type | Description |
|---|---|---|
| `ids` | array of string | List of map-element IDs to refresh. |

### Example

```json
{
  "biz_code": "map_group_refresh",
  "version": "1.0",
  "timestamp": 146052438362,
  "data": {
    "ids": [
      "string"
    ]
  }
}
```

## Relationship to other methods

- Follow-up fetch is the HTTP [`../../http/map/obtain.md`](../../http/map/obtain.md) scoped to the IDs in `data.ids`.
- This is the **WebSocket equivalent** of the push-and-fetch coordination pattern described in [`../README.md` §5](../README.md#5-push-and-fetch-coordination-pattern) — the WebSocket message is a trigger; the authoritative content comes from the follow-up HTTP call.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/20.websocket/10.map-elements/10.message-push.md]` | v1.11 canonical. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-WebSocket-Map-Elements-Push-Message.txt]` | v1.15 — identical shape. |
