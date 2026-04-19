# `cloud_control_release` — release cloud-control authority

Cloud command that relinquishes previously granted cloud-control authority. After `cloud_control_release` the RC's pilot regains sole control, and subsequent cloud-side flight commands will be rejected until a new [`cloud_control_auth_request`](cloud_control_auth_request.md) is accepted.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise + RC Pro Enterprise** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `cloud_control_release` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `cloud_control_release` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `control_keys` | array of text | Authorization scopes to release. `"flight"` = flight-control authority. Size = 1 per source. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "control_keys": ["flight"]
  },
  "method": "cloud_control_release",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1704038400000
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero = error. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "output": {
      "status": "ok"
    },
    "result": 0
  },
  "method": "cloud_control_release",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1704038400000
}
```

### Source inconsistencies flagged by DJI's own example

- **Reply `output` struct in example not declared in schema** — same pattern as [`cloud_control_auth_request`](cloud_control_auth_request.md). Treat `result` as authoritative.

## Relationship to other methods

- Companion to [`cloud_control_auth_request`](cloud_control_auth_request.md).
- Called on cloud-side session end, error recovery, or explicit hand-off back to the pilot.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/30.drc.md]` | v1.11 canonical (RC Pro). |
| `[DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Live-Flight-Controls.txt]` | v1.15 (RC Pro). |
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Flight-Controls.txt]` | v1.15 (RC Plus 2). |
