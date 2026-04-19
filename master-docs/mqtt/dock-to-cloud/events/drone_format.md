# `drone_format` — aircraft storage formatting progress

Event pushed by the dock (on behalf of the aircraft) while carrying out the [`drone_format`](../services/drone_format.md) service — formatting the aircraft-side storage. Reports task state + percent complete.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, events-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** (no v1.11 counterpart).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `drone_format` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `drone_format` *(Dock 2 only)* |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |
| `output.status` | enum string | Task state — `sent` / `in_progress` / `paused` / `ok` / `failed` / `canceled` / `rejected` / `timeout`. |
| `output.progress.percent` | int | Progress percentage, `0`–`100`. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "output": {
      "progress": {
        "percent": 80,
        "step_key": "xxx"
      },
      "status": "in_progress"
    },
    "result": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp:": 1654070968655,
  "method": "drone_format"
}
```

## Source inconsistencies flagged by DJI's own example

- **`step_key: "xxx"` placeholder in the example** — same issue as [`device_format`](device_format.md). The schema does not declare `step_key` for `drone_format`; the example carries a literal `"xxx"` placeholder. Treat as source noise.
- **`"timestamp:"` typo** in the v1.15 Dock 3 example.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Debugging.txt]` | v1.15 (Dock 2) — same shape; correct `"timestamp"` key. |
