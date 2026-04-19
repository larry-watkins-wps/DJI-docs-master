# `device_offline` — workspace device went offline

Server broadcast telling Pilot 2 that a device in the current workspace has gone offline. Same shape as [`device_online`](device_online.md) — empty `data`, trigger for the Pilot 2 HTTP topology fetch.

Verbatim (v1.11 canonical):

> When the server receives a request to take any device offline in the same workspace, it also broadcasts a device offline push to DJI Pilot 2 via WebSocket, and when DJI Pilot 2 receives the push, it will trigger the "**Obtain Device Topology List**".

Part of the Phase 5 WebSocket catalog. Shared conventions live in [`../README.md`](../README.md).

**Cohort**: **DJI Pilot 2**.

---

## Message identity

| Field | Value |
|---|---|
| `biz_code` | `device_offline` |
| Family | Situation Awareness |
| Direction | Server → Pilot 2 |

## `data` fields

None. `data` is an empty object.

### Example

```json
{
  "biz_code": "device_offline",
  "version": "1.0",
  "timestamp": 146052438362,
  "data": {}
}
```

## Relationship to other methods

- Triggered by the server observing a sub-device leaving the MQTT topology — either via an explicit `update_topo` with an empty `sub_devices` array, or via inferred MQTT-level disconnect (PINGRESP timeout, LWT). See [`../../mqtt/README.md` §7](../../mqtt/README.md#7-status-lifecycle) for the three-state online/disconnected/offline model.
- Pilot 2's follow-up fetch: [`../../http/device/topology.md`](../../http/device/topology.md).
- Paired with [`device_online`](device_online.md) and [`device_update_topo`](device_update_topo.md).

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/20.websocket/20.situation-awareness/10.message-push.md]` | v1.11 canonical. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-WebSocket-Situation-Awareness-Push-Message.txt]` | v1.15 — identical shape. |
