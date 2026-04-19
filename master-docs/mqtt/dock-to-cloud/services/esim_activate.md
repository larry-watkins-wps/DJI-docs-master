# `esim_activate` — activate an eSIM profile

Cloud command that activates a newly-provisioned eSIM profile on the named dongle. The reply carries task state; actual progress reports stream via the [`esim_activate`](../events/esim_activate.md) event.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `esim_activate` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `esim_activate` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `imei` | string | IMEI of the dongle. |
| `device_type` | enum string | `dock` = set dock-side dongle; `drone` = set aircraft-side dongle. |

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
