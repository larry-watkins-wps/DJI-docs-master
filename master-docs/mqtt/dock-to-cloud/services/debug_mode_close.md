# `debug_mode_close` — exit remote-debugging mode

Cloud command that takes the dock out of remote-debugging mode. `Data: null`. The reply ACKs task state.

The Remote-Debugging services (`charge_*`, `cover_*`, `drone_*`, `device_*`, `supplement_light_*`, etc.) rely on the dock being in debug mode; most of their progress events check `work_mode == remote_debugging` via the shared `step_key` enum value `check_work_mode`.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `debug_mode_close` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `debug_mode_close` |

## Down — `data`

`Data: null` — no parameters.

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |
| `output.status` | enum string | Task state — `sent` / `in_progress` / `paused` / `ok` / `failed` / `canceled` / `rejected` / `timeout`. |

## Relationship to other methods

- Entered via [`debug_mode_open`](debug_mode_open.md). Must be paired — entering debug mode without exiting leaves the dock unavailable for regular wayline / flight-task operations.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Debugging.txt]` | v1.15 (Dock 2) — identical. |
