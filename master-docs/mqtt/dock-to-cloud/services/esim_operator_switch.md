# `esim_operator_switch` — select eSIM carrier on a dongle

Cloud command that picks a carrier profile for a named dongle (dock-side or aircraft-side) on the eSIM. The reply is a plain ACK; the actual switch runs asynchronously and reports percent-complete via the [`esim_operator_switch`](../events/esim_operator_switch.md) event.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3**. Payloads are shape-identical; the `esim_operator` enum *description* wording differs between cohorts — see [Source differences](#source-differences).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `esim_operator_switch` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `esim_operator_switch` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `imei` | string | IMEI of the dongle whose eSIM the dock should update. |
| `device_type` | enum string | `dock` = set dock-side dongle; `drone` = set aircraft-side dongle. |
| `esim_operator` | enum int | Carrier to switch to. **Dock 3**: `{1: "China Mobile", 2: "China Unicom", 3: "China Telecom"}`. **Dock 2**: `{1: "Mobile", 2: "China Unicom", 3: "Telecommunications"}` — same wire values, shortened / alternative labels. |

DJI provides no example JSON for this service — just the schema tables.

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

## Relationship to other methods

- Asynchronous progress stream: [`esim_operator_switch`](../events/esim_operator_switch.md) event.
- [`sim_slot_switch`](sim_slot_switch.md) switches between physical-SIM and eSIM slots.
- [`esim_activate`](esim_activate.md) activates a newly-provisioned eSIM profile.

## Source differences

- **`esim_operator` description wording**: Dock 3 uses full names (`"China Mobile"`, `"China Unicom"`, `"China Telecom"`). Dock 2 uses shorter labels (`"Mobile"`, `"China Unicom"`, `"Telecommunications"`). The integer enum keys (`1 / 2 / 3`) are stable.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Debugging.txt]` | v1.15 (Dock 2) — different enum descriptions. |
