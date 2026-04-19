# `device_update_topo` — workspace device topology changed

Server broadcast telling Pilot 2 that the device topology in the current workspace has changed (device added, removed, or its sub-device membership changed). Same shape as [`device_online`](device_online.md) and [`device_offline`](device_offline.md) — empty `data`, trigger for the Pilot 2 HTTP topology fetch.

Verbatim (v1.11 canonical):

> When the Server receives a request for updating the device topology of any device in the same workspace, a push of updating the device topology is also broadcast by WebSocket to the Pilot. After the Pilot receives the push, **Obtain Device Topology List** API will be triggered.

Part of the Phase 5 WebSocket catalog. Shared conventions live in [`../README.md`](../README.md).

**Cohort**: **DJI Pilot 2**.

---

## Message identity

| Field | Value |
|---|---|
| `biz_code` | `device_update_topo` |
| Family | Situation Awareness |
| Direction | Server → Pilot 2 |

## `data` fields

None. `data` is an empty object.

### Example

```json
{
  "biz_code": "device_update_topo",
  "version": "1.0",
  "timestamp": 146052438362,
  "data": {}
}
```

## Relationship to other methods

- Triggered by the server observing a topology-level change on an already-online gateway — e.g., an aircraft pairing or unpairing with a dock / RC without the gateway itself going offline. Sourced from the MQTT `update_topo` method (see [`../../mqtt/dock-to-cloud/status/update_topo.md`](../../mqtt/dock-to-cloud/status/update_topo.md) and [`../../mqtt/pilot-to-cloud/status/update_topo.md`](../../mqtt/pilot-to-cloud/status/update_topo.md)).
- Pilot 2's follow-up fetch: [`../../http/device/topology.md`](../../http/device/topology.md).
- Paired with [`device_online`](device_online.md) and [`device_offline`](device_offline.md). The three messages differ semantically (new device, departed device, re-paired) but all drive the same HTTP fetch — Pilot 2 does not branch on the `biz_code`, only on the fact that topology has changed.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/20.websocket/20.situation-awareness/10.message-push.md]` | v1.11 canonical. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-WebSocket-Situation-Awareness-Push-Message.txt]` | v1.15 — identical shape. |
