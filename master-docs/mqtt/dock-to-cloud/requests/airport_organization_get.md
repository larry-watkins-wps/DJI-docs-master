# `airport_organization_get` — resolve organization info from a binding code

Given a device binding code and organization ID, fetch the display name of the organization. Used during the binding UX flow so the gateway can confirm to its operator which organization the code belongs to before committing to a bind.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, request-reply, `tid`/`bid` correlation) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload in both cohorts.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/requests` | `airport_organization_get` |
| Cloud → Device | `thing/product/{gateway_sn}/requests_reply` | `airport_organization_get` |

## Request (up) — `data` fields

| Field | Type | Description |
|---|---|---|
| `device_binding_code` | string | The binding code the gateway is about to redeem. |
| `organization_id` | string | Organization ID associated with the binding code. |

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "data": {
    "device_binding_code": "device_binding_code",
    "organization_id": "organization_id"
  }
}
```

## Reply (down) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero = error. |
| `output.organization_name` | string | Display name of the organization. |

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "data": {
    "result": 0,
    "output": {
      "organization_name": "organization_name"
    }
  }
}
```

## Relationship to other methods

- Companion methods in the binding flow: [`airport_bind_status`](airport_bind_status.md) (check if already bound), [`airport_organization_bind`](airport_organization_bind.md) (perform the bind).
- Full binding sequence documented in Phase 9 workflow `workflows/device-binding.md`.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/20.organization.md]` | v1.11 canonical (Dock 2) — method, parameters, examples. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Organization-Management.txt]` | v1.15 (Dock 2) — identical to v1.11. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Organization-Management.txt]` | v1.15 (Dock 3) — identical payload; confirms Dock 3 uses the same shape. |
