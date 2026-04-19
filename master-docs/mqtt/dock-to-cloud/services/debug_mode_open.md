# `debug_mode_open` — enter remote-debugging mode

Cloud command that puts the dock into remote-debugging mode — a precondition for almost every other Remote-Debugging service in this family (`charge_open/close`, `cover_open/close`, `drone_open/close`, `device_reboot`, `drone_format`, `device_format`, etc., whose progress-event safety checks include `check_work_mode`). `Data: null`. The reply ACKs task state.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `debug_mode_open` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `debug_mode_open` |

## Down — `data`

`Data: null` — no parameters.

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |
| `output.status` | enum string | Task state — `sent` / `in_progress` / `paused` / `ok` / `failed` / `canceled` / `rejected` / `timeout`. |

## Relationship to other methods

- Exit the mode via [`debug_mode_close`](debug_mode_close.md).
- While in debug mode the dock rejects regular wayline execution. Operators need to exit debug mode to resume scheduled missions.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Debugging.txt]` | v1.15 (Dock 2) — identical. |
