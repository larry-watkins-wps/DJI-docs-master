# Dock-to-Cloud MQTT catalog

Per-method documentation of everything the **Dock 2** and **Dock 3** gateways emit on, and receive over, MQTT. Each entry uses the envelope and topic-taxonomy conventions from [`../README.md`](../README.md) (Phase 2) — don't restate those here.

Per-method files are named verbatim after the DJI `method` string (e.g., `airport_organization_bind.md`) so that searches for a method name hit the filename directly.

---

## Catalog status

Phase 4 is being landed in feature-area sub-drops. This index grows as drops land.

| Sub-phase | Feature area | Status |
|---|---|---|
| 4a | DeviceManagement + Organization + Configuration — binding, topology, config | **landed 2026-04-18** |
| 4b | WaylineManagement — flight-task lifecycle + Virtual Cockpit routes | **landed 2026-04-18** |
| 4c | Live-Flight-Controls — DRC, camera/gimbal/IR control, authority grab | pending |
| 4d | LiveStream + Media-Management | pending |
| 4e | Firmware-Upgrade + Remote-Log + Remote-Debugging + Remote-Control | pending |
| 4f | FlySafe + Custom-Flight-Area + AirSense + HMS | pending |
| 4g | PSDK + PSDK-Interconnection + ESDK-Interconnection | pending |

## Current catalog

### `status/`

Topics under `sys/product/{gateway_sn}/status`.

| Method | Doc | Purpose |
|---|---|---|
| `update_topo` | [`status/update_topo.md`](status/update_topo.md) | Gateway reports its own state and sub-device list. |

### `events/`

Topics under `thing/product/{gateway_sn}/events`. Device → cloud pushes.

| Method | Doc | Purpose |
|---|---|---|
| `return_home_info` | [`events/return_home_info.md`](events/return_home_info.md) | Return-path trajectory + per-dock planning status. |
| `flighttask_ready` | [`events/flighttask_ready.md`](events/flighttask_ready.md) | Prepared conditional missions meet `ready_conditions`. |
| `flighttask_progress` | [`events/flighttask_progress.md`](events/flighttask_progress.md) | Periodic task-progress report with state, step, breakpoint. |
| `device_exit_homing_notify` | [`events/device_exit_homing_notify.md`](events/device_exit_homing_notify.md) | Aircraft enters / exits Return-to-Home Exit state. |
| `in_flight_wayline_progress` | [`events/in_flight_wayline_progress.md`](events/in_flight_wayline_progress.md) | Progress of a Virtual Cockpit in-flight route. |

### `services/`

Topics under `thing/product/{gateway_sn}/services`. Cloud → device commands.

| Method | Doc | Purpose |
|---|---|---|
| `flighttask_prepare` | [`services/flighttask_prepare.md`](services/flighttask_prepare.md) | Issue a mission (immediate / timed / conditional). |
| `flighttask_execute` | [`services/flighttask_execute.md`](services/flighttask_execute.md) | Execute a prepared mission. Multi-dock capable. |
| `flighttask_pause` | [`services/flighttask_pause.md`](services/flighttask_pause.md) | Pause an in-progress wayline. |
| `flighttask_recovery` | [`services/flighttask_recovery.md`](services/flighttask_recovery.md) | Resume a paused wayline. |
| `flighttask_stop` | [`services/flighttask_stop.md`](services/flighttask_stop.md) | Terminate a flight task. |
| `flighttask_undo` | [`services/flighttask_undo.md`](services/flighttask_undo.md) | Cancel prepared-but-not-executed missions (batch). |
| `flighttask_create` | [`services/flighttask_create.md`](services/flighttask_create.md) | *(Deprecated.)* Legacy mission-create method. |
| `return_home` | [`services/return_home.md`](services/return_home.md) | One-key return to home. |
| `return_home_cancel` | [`services/return_home_cancel.md`](services/return_home_cancel.md) | Cancel in-progress return. |
| `return_specific_home` | [`services/return_specific_home.md`](services/return_specific_home.md) | Designate landing dock in multi-dock tasks. |
| `in_flight_wayline_deliver` | [`services/in_flight_wayline_deliver.md`](services/in_flight_wayline_deliver.md) | Distribute a Virtual Cockpit flight route to an airborne aircraft. |
| `in_flight_wayline_stop` | [`services/in_flight_wayline_stop.md`](services/in_flight_wayline_stop.md) | Pause a Virtual Cockpit flight route. |
| `in_flight_wayline_recover` | [`services/in_flight_wayline_recover.md`](services/in_flight_wayline_recover.md) | Resume a paused Virtual Cockpit route. |
| `in_flight_wayline_cancel` | [`services/in_flight_wayline_cancel.md`](services/in_flight_wayline_cancel.md) | Cancel a Virtual Cockpit route. |

### `requests/`

Topics under `thing/product/{gateway_sn}/requests`. Device → cloud requests, cloud → device replies.

| Method | Doc | Purpose |
|---|---|---|
| `config` | [`requests/config.md`](requests/config.md) | Gateway asks the cloud for License / NTP configuration. |
| `airport_bind_status` | [`requests/airport_bind_status.md`](requests/airport_bind_status.md) | Gateway asks whether given devices are bound. |
| `airport_organization_get` | [`requests/airport_organization_get.md`](requests/airport_organization_get.md) | Gateway resolves an organization ID to a display name. |
| `airport_organization_bind` | [`requests/airport_organization_bind.md`](requests/airport_organization_bind.md) | Gateway binds a device set to an organization. |
| `flighttask_progress_get` | [`requests/flighttask_progress_get.md`](requests/flighttask_progress_get.md) | In multi-dock tasks, query the other dock's latest progress. |
| `flighttask_resource_get` | [`requests/flighttask_resource_get.md`](requests/flighttask_resource_get.md) | Fetch a fresh pre-signed URL for the KMZ wayline file. |

### `property/set`, `drc/`, `osd/`, `state/`

Pending in later sub-phases.

## Cohort coverage

Every method in this tree is documented with an explicit **Cohort** field at the top:

- **Dock 2 + Dock 3** — method exists in both cohorts with the same payload. This is the default for Phase 4a content.
- **Dock 3 only** — method is new in v1.15 with no Dock 2 counterpart (AirSense-aircraft events, AI-identify DRC modes, etc.). Marked explicitly.
- **Dock 2 only** — rare; indicates a legacy method that Dock 3 doesn't reimplement.

Per-cohort quirks that are larger than a one-line note live in Phase 10 (`device-annexes/`).

## Source reconciliation

v1.11 Cloud-API-Doc/ covers Dock 2 under `60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/`. v1.15 DJI_Cloud extracts cover both Dock 2 (`DJI_CloudAPI-Dock2-*.txt`) and Dock 3 (`DJI_CloudAPI-Dock3-*.txt`). Where v1.11 Dock 2 and v1.15 Dock 2 agree on a method, citations point to v1.11 first (formatting fidelity). Where a method exists only in v1.15, the DJI_Cloud file is primary.
