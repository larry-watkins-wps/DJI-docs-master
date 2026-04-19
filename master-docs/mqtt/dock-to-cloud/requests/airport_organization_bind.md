# `airport_organization_bind` — bind one or more devices to an organization

Commit a binding between a set of devices and an organization, using the License-backed binding codes. Typically called by the gateway for itself plus its sub-device (e.g., Dock + aircraft) in a single request. Per-device error codes in the reply allow partial failure reporting.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, request-reply, `tid`/`bid` correlation) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload in both cohorts.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/requests` | `airport_organization_bind` |
| Cloud → Device | `thing/product/{gateway_sn}/requests_reply` | `airport_organization_bind` |

## Request (up) — `data` fields

| Field | Type | Description |
|---|---|---|
| `bind_devices` | array of struct | Collection of devices to bind. Typical size: 2 (gateway + sub-device). |
| `bind_devices[].device_binding_code` | string | Binding code to redeem. |
| `bind_devices[].organization_id` | string | Organization ID the device should join. |
| `bind_devices[].device_callsign` | string | Display name the device will carry inside the organization. |
| `bind_devices[].sn` | string | Device serial number. |
| `bind_devices[].device_model_key` | string | Product enumeration value (e.g., `3-1-0` for a dock, `0-67-0` for an M4D aircraft). Full enum in Phase 6 (`device-properties/`). |

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "data": {
    "bind_devices": [
      {
        "device_binding_code": "device_binding_code",
        "device_callsign": "dock-device-callsign",
        "device_model_key": "3-1-0",
        "organization_id": "organization_id",
        "sn": "dock-sn"
      },
      {
        "device_binding_code": "device_binding_code",
        "device_callsign": "drone-device-callsign",
        "device_model_key": "0-67-0",
        "organization_id": "organization_id",
        "sn": "drone-sn"
      }
    ]
  }
}
```

## Reply (down) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Overall return code. `0` = success; non-zero = error. |
| `output.err_infos` | array of struct | Per-device error details. Even when `result` is `0`, individual devices can fail — inspect this array. |
| `output.err_infos[].sn` | string | Serial number of the failing device. |
| `output.err_infos[].err_code` | integer | Error code for that device (e.g., `210231`). Full error code reference in Phase 8 (`error-codes/`). |

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "data": {
    "result": 0,
    "output": {
      "err_infos": [
        { "sn": "dock-sn",  "err_code": 210231 },
        { "sn": "drone-sn", "err_code": 210231 }
      ]
    }
  }
}
```

## Relationship to other methods

- Companion methods in the binding flow: [`airport_bind_status`](airport_bind_status.md) (pre-check current state), [`airport_organization_get`](airport_organization_get.md) (confirm org name before bind).
- Full binding sequence documented in Phase 9 workflow `workflows/device-binding.md`.
- Pre-condition: the device must have a valid DJI-issued License configured via [`config`](config.md).

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/20.organization.md]` | v1.11 canonical (Dock 2) — method, parameters, examples. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Organization-Management.txt]` | v1.15 (Dock 2) — identical to v1.11. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Organization-Management.txt]` | v1.15 (Dock 3) — identical payload; confirms Dock 3 uses the same shape. |
