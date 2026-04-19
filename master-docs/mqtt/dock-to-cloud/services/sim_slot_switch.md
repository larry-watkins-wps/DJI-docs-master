# `sim_slot_switch` — switch between physical-SIM and eSIM slots

Cloud command that tells a named dongle (dock-side or aircraft-side) to use either the physical SIM card slot or its eSIM. The reply is a plain ACK.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `sim_slot_switch` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `sim_slot_switch` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `imei` | string | IMEI of the dongle. |
| `device_type` | enum string | `dock` = set dock-side dongle; `drone` = set aircraft-side dongle. |
| `sim_slot` | enum int | `1` = Physical SIM card; `2` = eSIM. |

DJI provides no example JSON for this service.

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Debugging.txt]` | v1.15 (Dock 2) — identical. |
