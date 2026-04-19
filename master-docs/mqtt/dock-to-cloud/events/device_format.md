# `device_format` — dock storage formatting progress

Event pushed by the dock while it carries out the [`device_format`](../services/device_format.md) service — formatting the onboard storage. Reports task state + percent complete.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, events-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** (no v1.11 counterpart).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `device_format` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `device_format` *(Dock 2 only)* |

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
  "method": "device_format"
}
```

## Source inconsistencies flagged by DJI's own example

- **`step_key: "xxx"` placeholder in the example** — the schema does not declare a `step_key` enum for `device_format`, but the example still carries a `step_key` field with the string literal `"xxx"`. DJI appears to have copy-pasted the example from a method that does use `step_key` and forgot to strip the field. Treat as source noise; the authoritative schema is `percent` only.
- **`"timestamp:"` typo** in the v1.15 Dock 3 example.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Debugging.txt]` | v1.15 (Dock 2) — same shape; example has the same `step_key: "xxx"` placeholder and the correct `"timestamp"` key. |
