# `drc_camera_mode_switch` — switch payload camera mode (Dock 2 legacy)

DRC command that switches the payload camera mode between capture, record, smart-low-light, panorama, and timed-shot. Dock 3 replaces this with [`camera_mode_switch`](../services/camera_mode_switch.md) on the standard `/services` topic (landed in 4c).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 only**.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `drc_camera_mode_switch` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `drc_camera_mode_switch` |

**Topic anomaly.** Despite the `drc_` method prefix, DJI documents this one as riding the standard `/services` + `/services_reply` topics (not `/drc/down` + `/drc/up`). This is inconsistent with sibling `drc_*` Dock 2 methods such as [`drc_force_landing`](drc_force_landing.md) which use `/drc/*`. Treat as a DJI source-level anomaly; a Dock-2 cloud implementation must subscribe on `services_reply` rather than `drc/up` for this one method.

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration. |
| `camera_mode` | enum int | `0` = Capturing, `1` = Recording, `2` = Smart Low-Light, `3` = Panorama, `4` = Timed Shot. |

### Example

```json
{
  "data": {
    "camera_mode": 2,
    "payload_index": "81-0-0"
  },
  "method": "drc_camera_mode_switch",
  "seq": 1
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

## Relationship to other methods

- **Dock 3 replacement**: [`camera_mode_switch`](../services/camera_mode_switch.md) — same enum, standard services envelope, no `drc_` prefix.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/180.remote-control.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Control.txt]` | v1.15 (Dock 2) — same anomaly. |
