# `drone_open` — aircraft power-on progress

Event pushed by the dock while carrying out the [`drone_open`](../services/drone_open.md) service — powering on the aircraft inside the dock. Unlike its paired [`drone_close`](drone_close.md), `drone_open` carries **no** `progress.percent` or `step_key` — the schema only defines `output.status`. The transition reports a single state change, not a multi-step progress stream.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, events-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** (no v1.11 counterpart).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `drone_open` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `drone_open` *(Dock 2 only)* |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |
| `output.status` | enum string | Task state — `sent` / `in_progress` / `paused` / `ok` / `failed` / `canceled` / `rejected` / `timeout`. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "output": {
      "status": "in_progress"
    },
    "result": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp:": 1654070968655,
  "method": "drone_open"
}
```

## Source inconsistencies flagged by DJI's own example

- **`"timestamp:"` typo** in the v1.15 Dock 3 example. Dock 2 example uses correct `"timestamp"`.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Debugging.txt]` | v1.15 (Dock 2) — same shape; adds explicit `events_reply`. |
