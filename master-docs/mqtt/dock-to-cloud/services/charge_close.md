# `charge_close` — stop charging the aircraft

Cloud command to stop the dock's charging cycle on the aircraft. `Data: null` — no input parameters. The reply ACKs task state; progress thereafter streams via the [`charge_close`](../events/charge_close.md) event with the same `bid`.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `charge_close` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `charge_close` |

## Down — `data`

`Data: null` — no parameters.

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |
| `output.status` | enum string | Task state — `sent` / `in_progress` / `paused` / `ok` / `failed` / `canceled` / `rejected` / `timeout`. |

## Relationship to other methods

- Typically requires [`debug_mode_open`](debug_mode_open.md) to have been issued first (the progress event's `step_key` enum includes `check_work_mode` = verify the dock is in remote-debugging mode).
- Progress: [`charge_close`](../events/charge_close.md) event.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Debugging.txt]` | v1.15 (Dock 2) — identical. |
