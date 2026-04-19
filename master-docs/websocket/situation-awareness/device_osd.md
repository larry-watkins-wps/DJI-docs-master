# `device_osd` — situation-awareness telemetry push

Fixed-frequency server push carrying the live position and motion state of every device in the workspace. Pilot 2 consumes this stream to update device icons on its map in real time. The server sources the underlying data from the device's MQTT OSD (see [`../../mqtt/dock-to-cloud/osd/README.md`](../../mqtt/dock-to-cloud/osd/README.md) and [`../../mqtt/pilot-to-cloud/osd/README.md`](../../mqtt/pilot-to-cloud/osd/README.md)) and re-projects it as a per-device WebSocket message.

Part of the Phase 5 WebSocket catalog. Shared conventions live in [`../README.md`](../README.md).

**Cohort**: **DJI Pilot 2**.

---

## Message identity

| Field | Value |
|---|---|
| `biz_code` | `device_osd` |
| Family | Situation Awareness |
| Direction | Server → Pilot 2 |

## `data` fields

| Field | Type | Description |
|---|---|---|
| `sn` | string | Device serial number. Identifies which workspace device this push is about. |
| `host` | object | Device state container (typically aircraft state). |
| `host.latitude` | number | Latitude in decimal degrees. |
| `host.longitude` | number | Longitude in decimal degrees. |
| `host.height` | integer | Height above takeoff / ground reference. |
| `host.attitude_head` | number | Heading (yaw) in degrees, 0–360. |
| `host.elevation` | number | Relative take-off altitude. |
| `host.horizontal_speed` | number | Horizontal speed. |
| `host.vertical_speed` | number | Vertical speed. |

> DJI's canonical source does not specify units for `height` / `elevation` / `horizontal_speed` / `vertical_speed`. The aircraft-OSD property catalog (Phase 6) is the authoritative unit reference; Pilot 2's rendering matches the MQTT OSD unit convention (meters, meters per second).

### Example

```json
{
  "biz_code": "device_osd",
  "version": "1.0",
  "timestamp": 146052438362,
  "data": {
    "host": {
      "latitude": 113.44444,
      "longitude": 23.45656,
      "height": 44.35,
      "attitude_head": 90,
      "elevation": 40,
      "horizontal_speed": 0,
      "vertical_speed": 2.3
    },
    "sn": "string"
  }
}
```

### Source inconsistencies flagged by DJI's own example

- **The example swaps `latitude` and `longitude`.** DJI's sample ships `"latitude": 113.44444, "longitude": 23.45656` — but 113.4° is a longitude (South China), not a latitude. Real wire traffic follows the field names, not the example values. This is cosmetic but worth flagging for Phase 9 workflows that may copy the example.

## Relationship to other methods

- Semantically the WebSocket projection of the MQTT `osd` family. A cloud implementation consumes MQTT OSD from docks + aircraft + RCs, reconciles them, and emits `device_osd` per aircraft at whatever frequency Pilot 2 expects.
- Unlike [`device_online`](device_online.md) / [`device_offline`](device_offline.md) / [`device_update_topo`](device_update_topo.md), this message carries its own payload — Pilot 2 does not need to follow up with an HTTP fetch.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/20.websocket/20.situation-awareness/10.message-push.md]` | v1.11 canonical — payload table + example. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-WebSocket-Situation-Awareness-Push-Message.txt]` | v1.15 — identical shape. |
