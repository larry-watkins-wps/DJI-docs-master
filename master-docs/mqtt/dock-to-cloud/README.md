# Dock-to-Cloud MQTT catalog

Per-method documentation of everything the **Dock 2** and **Dock 3** gateways emit on, and receive over, MQTT. Each entry uses the envelope and topic-taxonomy conventions from [`../README.md`](../README.md) (Phase 2) — don't restate those here.

Per-method files are named verbatim after the DJI `method` string (e.g., `airport_organization_bind.md`) so that searches for a method name hit the filename directly.

---

## Catalog status

Phase 4 is being landed in feature-area sub-drops. This index grows as drops land.

| Sub-phase | Feature area | Status |
|---|---|---|
| 4a | DeviceManagement + Organization + Configuration — binding, topology, config | **landed 2026-04-18** |
| 4b | WaylineManagement + Live-Flight-Controls (flight-task lifecycle, DRC) | pending |
| 4c | LiveStream + Media-Management | pending |
| 4d | Firmware-Upgrade + Remote-Log + Remote-Debugging + Remote-Control | pending |
| 4e | FlySafe + Custom-Flight-Area + AirSense + HMS | pending |
| 4f | PSDK + PSDK-Interconnection + ESDK-Interconnection | pending |

## Current catalog

### `status/`

Topics under `sys/product/{gateway_sn}/status`.

| Method | Doc | Purpose |
|---|---|---|
| `update_topo` | [`status/update_topo.md`](status/update_topo.md) | Gateway reports its own state and sub-device list. |

### `requests/`

Topics under `thing/product/{gateway_sn}/requests`.

| Method | Doc | Purpose |
|---|---|---|
| `config` | [`requests/config.md`](requests/config.md) | Gateway asks the cloud for License / NTP configuration. |
| `airport_bind_status` | [`requests/airport_bind_status.md`](requests/airport_bind_status.md) | Gateway asks whether given devices are bound. |
| `airport_organization_get` | [`requests/airport_organization_get.md`](requests/airport_organization_get.md) | Gateway resolves an organization ID to a display name. |
| `airport_organization_bind` | [`requests/airport_organization_bind.md`](requests/airport_organization_bind.md) | Gateway binds a device set to an organization. |

### `services/`, `events/`, `property/set`, `drc/`, `osd/`, `state/`

Pending in later sub-phases.

## Cohort coverage

Every method in this tree is documented with an explicit **Cohort** field at the top:

- **Dock 2 + Dock 3** — method exists in both cohorts with the same payload. This is the default for Phase 4a content.
- **Dock 3 only** — method is new in v1.15 with no Dock 2 counterpart (AirSense-aircraft events, AI-identify DRC modes, etc.). Marked explicitly.
- **Dock 2 only** — rare; indicates a legacy method that Dock 3 doesn't reimplement.

Per-cohort quirks that are larger than a one-line note live in Phase 10 (`device-annexes/`).

## Source reconciliation

v1.11 Cloud-API-Doc/ covers Dock 2 under `60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/`. v1.15 DJI_Cloud extracts cover both Dock 2 (`DJI_CloudAPI-Dock2-*.txt`) and Dock 3 (`DJI_CloudAPI-Dock3-*.txt`). Where v1.11 Dock 2 and v1.15 Dock 2 agree on a method, citations point to v1.11 first (formatting fidelity). Where a method exists only in v1.15, the DJI_Cloud file is primary.
