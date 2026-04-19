# `alarm_state_switch` — enable / disable dock sound-and-light alarm

Cloud command that enables or disables the dock's audible and visual alarm signals. The reply ACKs task state; no progress event is associated with this method.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `alarm_state_switch` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `alarm_state_switch` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `action` | enum int | `0` = Disable; `1` = Enable. |

DJI provides no example JSON for this service.

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |
| `output.status` | enum string | Task state — `sent` / `in_progress` / `paused` / `ok` / `failed` / `canceled` / `rejected` / `timeout`. |

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Debugging.txt]` | v1.15 (Dock 2) — identical. |
