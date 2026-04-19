# `update_topo` — pilot device topology update

Topology push from the **RC** (as gateway device) reporting its own online state and the currently paired sub-device aircraft. The cloud must treat every `update_topo` as the authoritative current topology (full snapshot, not a delta). An empty `sub_devices` array means no aircraft is paired.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, request-reply pattern, QoS/retain gap per OQ-003) live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise + RC Pro Enterprise** — payload schema identical to the dock-to-cloud variant. The only difference is the meaning of `{gateway_sn}` and the identity carried in `sub_devices[0]`. See [`../../dock-to-cloud/status/update_topo.md`](../../dock-to-cloud/status/update_topo.md) for a side-by-side field reference.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `sys/product/{gateway_sn}/status` | `update_topo` |
| Cloud → Device | `sys/product/{gateway_sn}/status_reply` | `update_topo` |

`{gateway_sn}` = RC's serial number. `sub_devices[0].sn` = paired aircraft serial (M4D / M4TD for RC Plus 2; M3D / M3TD for RC Pro).

## Request (up) — `data` fields

Same shape as the [dock-to-cloud doc](../../dock-to-cloud/status/update_topo.md#request-up--data-fields):

- `domain`, `type`, `sub_type` identify the RC as the gateway. See Phase 6 `device-properties/` for the full enum.
- `sub_devices` carries the paired aircraft; its `domain` / `type` / `sub_type` identify the aircraft model.

### Example — RC Pro Enterprise with M3D paired (v1.11 canonical)

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "update_topo",
  "timestamp": 1234567890123,
  "data": {
    "domain": "3",
    "type": 119,
    "sub_type": 0,
    "device_secret": "secret",
    "nonce": "nonce",
    "thing_version": "1.1.2",
    "sub_devices": [
      {
        "sn": "drone001",
        "domain": "0",
        "type": 60,
        "sub_type": 0,
        "index": "A",
        "device_secret": "secret",
        "nonce": "nonce",
        "thing_version": "1.1.2"
      }
    ]
  }
}
```

### Example — aircraft unpaired

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "update_topo",
  "timestamp": 1234567890123,
  "data": {
    "domain": "3",
    "type": 119,
    "sub_type": 0,
    "device_secret": "secret",
    "nonce": "nonce",
    "thing_version": "1.1.2",
    "sub_devices": []
  }
}
```

## Reply (down) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero = error. |

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "update_topo",
  "timestamp": 1654070968655,
  "data": { "result": 0 }
}
```

## Relationship to other surfaces

- This is the authoritative wire-level topology source for the pilot-to-cloud surface, symmetric with the dock-to-cloud surface.
- The HTTP endpoint [`../../../http/device/topology.md`](../../../http/device/topology.md) is the read-back surface Pilot 2 uses to pull the current topology.
- The WebSocket messages `device_online` / `device_offline` / `device_update_topo` (see [`../../../websocket/README.md` §4.2](../../../websocket/README.md#42-situation-awareness)) are change signals that trigger Pilot 2 to call the HTTP topology endpoint.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/10.device.md]` | v1.11 canonical (RC Pro) — topic, parameters, examples. |
| `[DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Device-Management.txt]` | v1.15 (RC Pro). |
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Device-Management.txt]` | v1.15 (RC Plus 2) — same schema, no v1.11 counterpart. |
