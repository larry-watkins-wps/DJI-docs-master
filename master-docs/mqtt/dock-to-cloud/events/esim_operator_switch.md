# `esim_operator_switch` — eSIM operator-switch progress

Event pushed by the dock while it is carrying out the [`esim_operator_switch`](../services/esim_operator_switch.md) service — changing the carrier profile on the dock or aircraft eSIM dongle. Reports task state + percent complete.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, events-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** (no v1.11 counterpart — Remote-Debugging is a v1.15 addition).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `esim_operator_switch` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `esim_operator_switch` *(Dock 2 only — Dock 3 v1.15 does not document `events_reply`)* |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |
| `output.status` | enum string | Task state. One of `sent`, `in_progress`, `paused`, `ok`, `failed`, `canceled`, `rejected`, `timeout`. |
| `output.progress.percent` | int | Progress percentage, `0`–`100`. |

### Example (Dock 3 v1.15)

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
  "method": "esim_operator_switch",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp:": 1654070968655
}
```

### Example (Dock 2 v1.15 — correct timestamp key)

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
  "method": "esim_operator_switch",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655
}
```

## Down (reply) — `data` fields *(Dock 2 only)*

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code (`0` = success). |

Dock 2 explicitly documents an `events_reply` topic and example. Dock 3 v1.15 omits the `events_reply` section — behavior follows the usual MQTT events pattern (no explicit reply when `need_reply` is absent; cloud may or may not ACK).

## Source inconsistencies flagged by DJI's own example

- **`"timestamp:"` typo** (trailing colon inside the key) in the v1.15 Dock 3 example. The v1.15 Dock 2 example uses the correct `"timestamp"` key. The typo is pervasive across Dock 3's Remote-Debugging event examples — see [Source inconsistencies across 4e-1](../../README.md#source-inconsistencies-across-4e-1) *(pending)*.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3) — no `events_reply` section. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Debugging.txt]` | v1.15 (Dock 2) — includes explicit `events_reply` (`data.result` only). |
