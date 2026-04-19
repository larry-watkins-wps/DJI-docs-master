# `device_reboot` — dock reboot progress

Event pushed by the dock while carrying out the [`device_reboot`](../services/device_reboot.md) service — rebooting the dock itself. Reports task state, percent complete, and the current safety-check step. The dock checks AC power, verifies it isn't in the middle of a firmware upgrade, and writes a reboot flag before cycling.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, events-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** (no v1.11 counterpart).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `device_reboot` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `device_reboot` *(Dock 2 only)* |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |
| `output.status` | enum string | Task state — `sent` / `in_progress` / `paused` / `ok` / `failed` / `canceled` / `rejected` / `timeout`. |
| `output.progress.percent` | int | Progress percentage, `0`–`100`. |
| `output.progress.step_key` | enum string | Current safety-check step. Values: `get_bid`, `check_ac_input_state` (check AC power), `upgrading_prevent_reboot` (refuse reboot during firmware upgrade), `check_work_mode`, `check_task_state`, `write_reboot_param_file` (write reboot flag). |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "output": {
      "progress": {
        "percent": 20,
        "step_key": "write_reboot_param_file"
      },
      "status": "in_progress"
    },
    "result": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp:": 1654070968655,
  "method": "device_reboot"
}
```

## Source inconsistencies flagged by DJI's own example

- **`"timestamp:"` typo** in the v1.15 Dock 3 example.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Debugging.txt]` | v1.15 (Dock 2) — identical enum; adds explicit `events_reply`. |
