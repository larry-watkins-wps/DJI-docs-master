# `cover_close` — close the dock cover

Cloud command that closes the dock cover. `Data: null`. The reply ACKs task state; progress streams via the [`cover_close`](../events/cover_close.md) event, which tracks a propeller-paddle safety sequence (forward spin → close cover → reverse spin → stop) before the cover finishes locking.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `cover_close` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `cover_close` |

## Down — `data`

`Data: null` — no parameters.

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |
| `output.status` | enum string | Task state — `sent` / `in_progress` / `paused` / `ok` / `failed` / `canceled` / `rejected` / `timeout`. |

## Relationship to other methods

- Compare [`cover_force_close`](cover_force_close.md) — skips the safety sequence when the aircraft is known to be out of the dock.
- Progress: [`cover_close`](../events/cover_close.md) event.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Debugging.txt]` | v1.15 (Dock 2) — identical. |
