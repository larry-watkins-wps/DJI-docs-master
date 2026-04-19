# `device_format` — format the dock storage

Cloud command that formats the dock-side storage. `Data: null`. The reply ACKs task state; progress streams via the [`device_format`](../events/device_format.md) event.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload shape. Dock 3's source has a copy-paste typo in the services `method` label — see [Source inconsistencies](#source-inconsistencies-flagged-by-djis-own-example).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `device_format` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `device_format` |

## Down — `data`

`Data: null` — no parameters.

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |
| `output.status` | enum string | Task state — `sent` / `in_progress` / `paused` / `ok` / `failed` / `canceled` / `rejected` / `timeout`. |

## Relationship to other methods

- Sibling: [`drone_format`](drone_format.md) formats the aircraft-side storage.
- Progress: [`device_format`](../events/device_format.md) event.

## Source inconsistencies flagged by DJI's own example

- **Dock 3 source typo — `Method: drone_format` on the services-side of `device_format`.** The "Dock Data Formatting" section (L733–L754) in `DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt` labels the down side as `Method: drone_format` (duplicating the prior `drone_format` section) while the `services_reply` side below correctly labels it `Method: device_format`. Reading Dock 3 in isolation you would see two consecutive `drone_format` service entries where the second one ACKs as `device_format` — a copy-paste error. The Dock 2 source has the method name correctly as `device_format` on both sides. The authoritative method name is `device_format`.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3) — services-side header shows copy-paste typo `drone_format`; reply-side correctly says `device_format`. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Debugging.txt]` | v1.15 (Dock 2) — both sides labelled `device_format`. Treat as authoritative on the method name. |
