# `air_conditioner_mode_switch` — set dock AC working mode

Cloud command that overrides the dock air-conditioner working mode — idle, cooling, heating, or dehumidification. The dehumidification mode autonomously mixes cooling- and heating-based dehumidification without further operator input. The reply ACKs task state.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `air_conditioner_mode_switch` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `air_conditioner_mode_switch` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `action` | enum int | Target AC mode. `0` = idle (turn off cooling/heating/dehumidification); `1` = cooling; `2` = heating; `3` = dehumidification (device autonomously mixes cooling- and heating-based dehumidification). |

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
