# `drone_close` — aircraft power-off progress

Event pushed by the dock while carrying out the [`drone_close`](../services/drone_close.md) service — powering off the aircraft inside the dock. Reports task state, percent complete, and the current safety-check step.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, events-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** (no v1.11 counterpart).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `drone_close` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `drone_close` *(Dock 2 only)* |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |
| `output.status` | enum string | Task state — `sent` / `in_progress` / `paused` / `ok` / `failed` / `canceled` / `rejected` / `timeout`. |
| `output.progress.percent` | int | Progress percentage, `0`–`100`. |
| `output.progress.step_key` | enum string | Current safety-check step. Values: `get_bid`, `check_ac_input_state`, `upgrading_prevent_reboot`, `check_work_mode`, `check_task_state`, `check_scram_state`, `close_drone` (power off the aircraft). |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "output": {
      "progress": {
        "percent": 20,
        "step_key": "check_work_mode"
      },
      "status": "in_progress"
    },
    "result": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp:": 1654070968655,
  "method": "drone_close"
}
```

## Source inconsistencies flagged by DJI's own example

- **`"timestamp:"` typo** in the v1.15 Dock 3 example.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Debugging.txt]` | v1.15 (Dock 2) — identical enum; adds explicit `events_reply`. |
