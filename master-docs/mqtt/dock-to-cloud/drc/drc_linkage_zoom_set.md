# `drc_linkage_zoom_set` — enable / disable Link Zoom (Dock 2 M3TD only)

DRC command that toggles Link Zoom — a zoom-follows-lens coupling that ties visible and infrared zoom ratios together. DJI documents this as **Matrice 3TD only** among the Dock 2 aircraft cohort. No Dock 3 counterpart.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 only**.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_linkage_zoom_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_linkage_zoom_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration. |
| `state` | bool (0/1) | Link Zoom status. `0` = Closed; `1` = Opened. |

### Example

```json
{
  "data": {
    "payload_index": "81-0-0",
    "state": 0
  },
  "method": "drc_linkage_zoom_set",
  "seq": 1
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/180.remote-control.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Control.txt]` | v1.15 (Dock 2) — identical. |
