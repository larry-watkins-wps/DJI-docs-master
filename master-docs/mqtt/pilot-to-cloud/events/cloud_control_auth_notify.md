# `cloud_control_auth_notify` — cloud-control authorization result

RC-side notification of the user's response to a cloud-control authorization pop-up. The cloud sends [`cloud_control_auth_request`](../services/cloud_control_auth_request.md) to trigger a pop-up on the RC; the pilot accepts, rejects, or the request is superseded by another user. The RC emits `cloud_control_auth_notify` with the final outcome.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise + RC Pro Enterprise** — identical payload. v1.11 canonical covers RC Pro; v1.15 covers both.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `cloud_control_auth_notify` |

`need_reply: 0` — no reply expected.

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero = error. |
| `output` | struct | Container for `status`. |
| `output.status` | enum_string | `{"canceled": "Superseded by another user's authorization request", "failed": "Error or user denied", "ok": "User agreed"}`. |

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
  "method": "cloud_control_auth_notify",
  "need_reply": 0,
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1704038400000
}
```

## Relationship to other methods

- Paired with [`cloud_control_auth_request`](../services/cloud_control_auth_request.md) (cloud → device command that raised the pop-up) and [`cloud_control_release`](../services/cloud_control_release.md) (cloud → device command that relinquishes authority).
- The lifecycle is: cloud sends `cloud_control_auth_request` → RC pops up → user chooses → RC sends `cloud_control_auth_notify` with the chosen outcome → cloud either issues flight commands (if `ok`) or waits for another opportunity (if `failed` / `canceled`).

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/30.drc.md]` | v1.11 canonical (RC Pro) — filed under "drc.md" but actually an events-family method. |
| `[DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Live-Flight-Controls.txt]` | v1.15 (RC Pro). |
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Flight-Controls.txt]` | v1.15 (RC Plus 2) — wording "Authorization request popup was canceled due to another user's request" vs RC Pro's "Another user initiated an authorization request, this request was canceled"; semantics identical. |
