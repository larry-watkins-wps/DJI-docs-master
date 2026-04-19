# `esim_activate` — eSIM activation progress

Event pushed by the dock while it is carrying out the [`esim_activate`](../services/esim_activate.md) service — provisioning a newly-installed eSIM profile on the dock or aircraft dongle. Reports task state + percent complete.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, events-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** (no v1.11 counterpart).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `esim_activate` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `esim_activate` *(Dock 2 only)* |

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
        "percent": 0
      },
      "status": "in_progress"
    },
    "result": 0
  },
  "gateway": "dock_sn",
  "method": "esim_activate",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp:": 1654070968655
}
```

(Dock 3 example shown — `"timestamp:"` typo is Dock-3-specific. Dock 2 example uses the correct `"timestamp"` key.)

## Down (reply) — `data` fields *(Dock 2 only)*

Standard events-reply shape: `data.result` (integer; `0` = success).

## Source inconsistencies flagged by DJI's own example

- **`"timestamp:"` typo** in the v1.15 Dock 3 example.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Debugging.txt]` | v1.15 (Dock 2) — adds explicit `events_reply`. |
