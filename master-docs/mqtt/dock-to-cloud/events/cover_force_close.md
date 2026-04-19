# `cover_force_close` — forced dock-cover close progress

Event pushed by the dock while carrying out the [`cover_force_close`](../services/cover_force_close.md) service — closing the dock cover while bypassing the usual safety interlocks. Unlike [`cover_close`](cover_close.md), this event carries **no** step_key decomposition — only percent-complete.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, events-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** (no v1.11 counterpart).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `cover_force_close` |

Dock 2 does not document an `events_reply` for this method (contrast sibling debugging events where Dock 2 does).

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
        "percent": 6
      },
      "status": "in_progress"
    },
    "result": 0
  },
  "method": "cover_force_close",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655
}
```

## Source inconsistencies flagged by DJI's own example

- **Consistent `"timestamp"` key across cohorts** for this one method — unusual for Dock 3's Remote-Debugging file, where most examples carry the `"timestamp:"` trailing-colon typo. The `cover_force_close` example is byte-identical between Dock 2 and Dock 3 sources.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Debugging.txt]` | v1.15 (Dock 2) — identical. |
