# `cover_close` — dock-cover close progress

Event pushed by the dock while carrying out the [`cover_close`](../services/cover_close.md) service — closing the dock cover. The step machine runs a propeller-paddle sequence that spins the aircraft's propellers forward and reverse to clear the cover path before locking; every step is reported as `step_key`.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, events-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** (no v1.11 counterpart).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `cover_close` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `cover_close` *(Dock 2 only)* |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |
| `output.status` | enum string | Task state — `sent` / `in_progress` / `paused` / `ok` / `failed` / `canceled` / `rejected` / `timeout`. |
| `output.progress.percent` | int | Progress percentage, `0`–`100`. |
| `output.progress.step_key` | enum string | Current safety-check step. Values: `get_bid`, `check_work_mode`, `check_task_state`, `check_scram_state`, `turn_on_drone` (power on the aircraft), `drone_paddle_forward` (aircraft slowly rotates propellers), `close_cover`, `drone_paddle_reverse` (aircraft slowly rotates propellers in reverse), `drone_paddle_stop`. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "output": {
      "progress": {
        "percent": 58,
        "step_key": "drone_paddle_reverse"
      },
      "status": "in_progress"
    },
    "result": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp:": 1654070968655,
  "method": "cover_close"
}
```

## Source inconsistencies flagged by DJI's own example

- **`"timestamp:"` typo** in the v1.15 Dock 3 example.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Debugging.txt]` | v1.15 (Dock 2) — identical enum; adds explicit `events_reply`. |
