# `airport_bind_status` — query binding state for one or more devices

The gateway asks the cloud whether a set of devices (by serial number) are currently bound to any organization. Part of the License-backed binding flow — the gateway typically runs this at startup to decide whether to proceed with [`airport_organization_bind`](airport_organization_bind.md) or skip straight to operational traffic.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, request-reply, `tid`/`bid` correlation) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload in both cohorts.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/requests` | `airport_bind_status` |
| Cloud → Device | `thing/product/{gateway_sn}/requests_reply` | `airport_bind_status` |

## Request (up) — `data` fields

| Field | Type | Description |
|---|---|---|
| `devices` | array of struct | Collection of devices to query. Size: 2 (typical — gateway + sub-device). |
| `devices[].sn` | string | Device serial number. |

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "data": {
    "devices": [
      { "sn": "drone-sn" },
      { "sn": "dock-sn" }
    ]
  }
}
```

## Reply (down) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero = error. |
| `output.bind_status` | array of struct | Binding status per queried device. |
| `output.bind_status[].sn` | string | Device serial number (echoes the request). |
| `output.bind_status[].is_device_bind_organization` | boolean | `true` if bound to an organization. |
| `output.bind_status[].organization_id` | string | Organization ID if bound. |
| `output.bind_status[].organization_name` | string | Organization display name if bound. |
| `output.bind_status[].device_callsign` | string | Device name within the organization. |

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "data": {
    "result": 0,
    "output": {
      "bind_status": [
        {
          "sn": "12345",
          "is_device_bind_organization": true,
          "organization_id": "12345678",
          "organization_name": "12345",
          "device_callsign": "Device organization callsign"
        },
        {
          "sn": "12345",
          "is_device_bind_organization": true,
          "organization_id": "12345678",
          "organization_name": "12345",
          "device_callsign": "Device organization callsign"
        }
      ]
    }
  }
}
```

## Relationship to other methods

- Companion methods in the binding flow: [`airport_organization_get`](airport_organization_get.md) (resolve an organization_id to a name), [`airport_organization_bind`](airport_organization_bind.md) (perform the bind).
- Full binding sequence documented in Phase 9 workflow `workflows/device-binding.md`.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/20.organization.md]` | v1.11 canonical (Dock 2) — method, parameters, examples. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Organization-Management.txt]` | v1.15 (Dock 2) — identical to v1.11. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Organization-Management.txt]` | v1.15 (Dock 3) — identical payload; confirms Dock 3 uses the same shape. |
