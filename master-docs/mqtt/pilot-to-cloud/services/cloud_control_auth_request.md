# `cloud_control_auth_request` — request cloud-control authorization

Cloud command that asks the RC's pilot to grant cloud-side flight-control authority. The RC displays a pop-up identifying the requesting cloud user; the pilot accepts or rejects. The final outcome is reported back via the [`cloud_control_auth_notify`](../events/cloud_control_auth_notify.md) event.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise + RC Pro Enterprise** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `cloud_control_auth_request` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `cloud_control_auth_request` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `user_id` | text | User ID of the cloud user requesting authorization. Shown on the pop-up. |
| `user_callsign` | text | Display nickname of the requesting user. Shown on the pop-up. |
| `control_keys` | array of text | Authorization scopes. `"flight"` = flight-control authority. Size = 1 per source; DJI does not document other values. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "control_keys": ["flight"],
    "user_callsign": "xxxxxxx",
    "user_id": "xxxxxxxxxxx"
  },
  "method": "cloud_control_auth_request",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1704038400000
}
```

## Up (reply) — `data` fields

The reply carries a transport-level ACK (`result`). The authorization **outcome** is reported asynchronously on [`cloud_control_auth_notify`](../events/cloud_control_auth_notify.md), not here — the pilot may take arbitrary time to respond to the pop-up.

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = pop-up successfully shown; non-zero = error (invalid `control_keys`, RC disconnected, etc.). |

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
  "method": "cloud_control_auth_request",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1704038400000
}
```

### Source inconsistencies flagged by DJI's own example

- **Reply `output` struct appears in the example** (`"output": { "status": "ok" }`) but is not declared in the `services_reply` schema table. Treat the example as advisory: DJI appears to return an extra `output.status` on successful pop-up display, though only `result` is schema-guaranteed.

## Relationship to other methods

- Companion to [`cloud_control_release`](cloud_control_release.md) (releases previously granted authority).
- Asynchronous outcome delivered via [`cloud_control_auth_notify`](../events/cloud_control_auth_notify.md).
- The cloud-control-authority concept is pilot-to-cloud-specific — on dock-to-cloud, the cloud holds implicit authority over the dock and asks the dock (not the pilot) to grant flight authority via [`../../dock-to-cloud/services/flight_authority_grab.md`](../../dock-to-cloud/services/flight_authority_grab.md).

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/30.drc.md]` | v1.11 canonical (RC Pro). |
| `[DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Live-Flight-Controls.txt]` | v1.15 (RC Pro). |
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Flight-Controls.txt]` | v1.15 (RC Plus 2). |
