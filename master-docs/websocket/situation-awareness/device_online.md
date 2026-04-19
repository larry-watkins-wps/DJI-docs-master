# `device_online` — workspace device came online

Server broadcast telling Pilot 2 that a device in the current workspace has come online. The message carries no content — it is a **trigger** that causes Pilot 2 to re-fetch the authoritative topology via HTTP.

Verbatim (v1.11 canonical):

> When the server receives a request for any device in the same workspace to come online, it also broadcasts a push to DJI Pilot 2 via WebSocket, and when DJI Pilot 2 receives the push, it will trigger the "**Obtain Device Topology List**".

Part of the Phase 5 WebSocket catalog. Shared conventions (including the push-and-fetch coordination pattern) live in [`../README.md`](../README.md).

**Cohort**: **DJI Pilot 2**.

---

## Message identity

| Field | Value |
|---|---|
| `biz_code` | `device_online` |
| Family | Situation Awareness |
| Direction | Server → Pilot 2 |

## `data` fields

None. `data` is an empty object.

### Example

```json
{
  "biz_code": "device_online",
  "version": "1.0",
  "timestamp": 146052438362,
  "data": {}
}
```

## Relationship to other methods

- Triggered by the server observing an MQTT `update_topo` that added a sub-device (see [`../../mqtt/dock-to-cloud/status/update_topo.md`](../../mqtt/dock-to-cloud/status/update_topo.md) and [`../../mqtt/pilot-to-cloud/status/update_topo.md`](../../mqtt/pilot-to-cloud/status/update_topo.md)).
- Pilot 2's follow-up fetch: [`../../http/device/topology.md`](../../http/device/topology.md).
- Paired with [`device_offline`](device_offline.md) and [`device_update_topo`](device_update_topo.md) — the three messages collectively trigger the same HTTP fetch and differ only in which event they announce.

## Push-and-fetch ordering

[`../README.md` §5](../README.md#5-push-and-fetch-coordination-pattern) documents the ordering constraint: the server must reconcile its workspace state (based on incoming MQTT topology) **before** emitting this WebSocket push, so Pilot 2's follow-up HTTP fetch returns consistent topology.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/20.websocket/20.situation-awareness/10.message-push.md]` | v1.11 canonical. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-WebSocket-Situation-Awareness-Push-Message.txt]` | v1.15 — identical shape. |
