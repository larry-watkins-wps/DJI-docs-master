# `cover_force_close` — force-close the dock cover

Cloud command that forces the dock cover to close without running the usual safety interlocks. `Data: null`.

DJI's own description warns: use only when the `drone_in_dock` OSD property is `0` **and** the operator has confirmed via the dock camera that the aircraft is not inside the dock. Otherwise the closing cover may pinch the propellers.

The reply ACKs task state; a short `cover_force_close` progress event streams percent-complete (without the `step_key` decomposition that [`cover_close`](cover_close.md) has).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `cover_force_close` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `cover_force_close` |

## Down — `data`

`Data: null` — no parameters.

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |
| `output.status` | enum string | Task state — `sent` / `in_progress` / `paused` / `ok` / `failed` / `canceled` / `rejected` / `timeout`. |

## Relationship to other methods

- Contrast [`cover_close`](cover_close.md) (with safety sequence, including the propeller-paddle check).
- Progress: [`cover_force_close`](../events/cover_force_close.md) event.
- The prerequisite OSD property `drone_in_dock` is covered in Phase 6 (`device-properties/`).

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Debugging.txt]` | v1.15 (Dock 2) — identical. |
