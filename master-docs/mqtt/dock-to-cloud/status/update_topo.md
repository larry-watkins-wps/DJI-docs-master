# `update_topo` — device topology update

Topology push from the gateway device reporting its own online state, its device metadata, and the sub-devices currently attached. The cloud must treat every `update_topo` as the authoritative current topology (full snapshot, not a delta). An empty `sub_devices` array means no sub-device is attached.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, request-reply pattern, `{device_sn}` vs `{gateway_sn}`, QoS/retain gap per OQ-003) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — payload and semantics identical across cohorts. v1.11 Cloud-API-Doc only covers Dock 2; v1.15 DJI_Cloud extracts cover Dock 2 and Dock 3 with no observed divergence.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `sys/product/{gateway_sn}/status` | `update_topo` |
| Cloud → Device | `sys/product/{gateway_sn}/status_reply` | `update_topo` |

## Request (up) — `data` fields

| Field | Type | Description |
|---|---|---|
| `domain` | string | Gateway device namespace. See Phase 6 `device-properties/` for full enum. |
| `type` | integer | Gateway device product type. |
| `sub_type` | integer | Gateway device product subtype. |
| `device_secret` | string | Gateway device key. |
| `nonce` | string | Anti-replay nonce. |
| `thing_version` | string | Thing-model version of the gateway device (e.g., `"1.1.2"`). |
| `sub_devices` | array of struct | Sub-device list. Empty array = no sub-device attached. |
| `sub_devices[].sn` | string | Sub-device serial number. |
| `sub_devices[].domain` | string | Sub-device namespace. |
| `sub_devices[].type` | integer | Sub-device product type. |
| `sub_devices[].sub_type` | integer | Sub-device product subtype. |
| `sub_devices[].index` | string | Channel index connecting to the gateway device (e.g., `"A"`). |
| `sub_devices[].device_secret` | string | Sub-device key. |
| `sub_devices[].nonce` | string | Sub-device nonce. |
| `sub_devices[].thing_version` | string | Thing-model version of the sub-device. |

### Example — gateway and sub-device online

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

### Example — sub-device offline (gateway still online)

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
  "data": {
    "result": 0
  }
}
```

## Relationship to other surfaces

- This is the authoritative wire-level topology source. Every cloud implementation derives its gateway-to-sub-device mapping from these messages.
- The HTTP endpoint [`../../../http/device/topology.md`](../../../http/device/topology.md) is the read-back surface Pilot 2 uses to pull the current topology — its response is constructed from the cloud's reconciled view of these MQTT messages.
- The WebSocket messages `device_online` / `device_offline` / `device_update_topo` (see [`../../../websocket/README.md` §4.2](../../../websocket/README.md#42-situation-awareness)) are change signals that trigger Pilot 2 to call the HTTP topology endpoint.
- Domain / type / sub_type enum values are resolved via Phase 6 (`device-properties/`).

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/10.device.md]` | v1.11 canonical (Dock 2) — topic, parameters, examples. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Device-Management.txt]` | v1.15 (Dock 2) — identical to v1.11. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-DeviceManagement.txt]` | v1.15 (Dock 3) — identical payload; confirms Dock 3 uses the same shape. |
