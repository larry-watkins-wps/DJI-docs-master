# `ir_metering_area_set` — set infrared area-measurement region

Cloud command that sets a rectangular area-metering region on the IR camera. Only applies when the camera is in area-measurement mode (set via [`ir_metering_mode_set`](ir_metering_mode_set.md) with `mode=2`).

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `ir_metering_area_set` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `ir_metering_area_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration (`{type}-{subtype}-{gimbalindex}`). |
| `x` | double | Upper-left corner x, origin at lens upper-left, horizontal axis. Range `[0, 1]`. |
| `y` | double | Upper-left corner y, origin at lens upper-left, vertical axis. Range `[0, 1]`. |
| `width` | double | Region width, normalized `[0, 1]`. |
| `height` | double | Region height, normalized `[0, 1]`. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "height": 0.5,
    "payload_index": "39-0-7",
    "width": 0.5,
    "x": 0.5,
    "y": 0.5
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "ir_metering_area_set"
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero represents an error. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": { "result": 0 },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "ir_metering_area_set"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
