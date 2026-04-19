# `flighttask_execute` — execute a prepared mission

Cloud command that tells the device to execute a flight mission that was previously sent via [`flighttask_prepare`](flighttask_prepare.md). For single-dock tasks, only `flight_id` is required. For multi-dock tasks, the `multi_dock_task` block provides the wireless-link topology (frequency pairing info) and per-dock geometry / calibration parameters so both docks can coordinate.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `flighttask_execute` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `flighttask_execute` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `flight_id` | string | Task ID to execute. |
| `multi_dock_task` | struct | Multi-dock parameters. Required for multi-dock tasks; omit for single-dock. |

### `multi_dock_task`

| Field | Type | Description |
|---|---|---|
| `wireless_link_topo` | struct | Wireless link topology — see below. |
| `dock_infos` | array of struct (size 2) | Per-dock geometry + RTK info + alternate landing point. |

### `multi_dock_task.wireless_link_topo`

| Field | Type | Description |
|---|---|---|
| `secret_code` | array of 28 ints | Encryption code, obtained from aircraft device properties. |
| `center_node` | struct | Aircraft frequency info — `{sdr_id, sn}`. |
| `leaf_nodes` | array of struct | Dock / RC frequency info — `{sdr_id, sn, control_source_index}` (range 1–2). |

### `multi_dock_task.dock_infos[*]`

| Field | Type | Description |
|---|---|---|
| `dock_type` | enum string | `takeoff` or `landing`. |
| `sn` | string | Dock SN. |
| `latitude`, `longitude` | double | Dock position (from device properties). |
| `height` | double | Ellipsoid height, meters. |
| `heading` | double | Dock heading angle, degrees (±180). |
| `home_position_is_valid` | enum int | `0` invalid, `1` valid. |
| `index` | integer | Dock task unique identifier (1–31). |
| `rtcm_info` | struct | `{host, port, mount_point, rtcm_device_type, source_type}`. RTK calibration source. |
| `alternate_land_point` | struct | `{latitude, longitude, safe_land_height, is_configured}`. Alternate landing target. |

### Example (multi-dock)

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "flighttask_execute",
  "timestamp": 1720095314016,
  "data": {
    "flight_id": "aee739dc-f1cc-47d5-beaa-64d327f2d797",
    "multi_dock_task": {
      "wireless_link_topo": {
        "center_node": { "sdr_id": 933765657, "sn": "1581F6Q8D245P00EKS87" },
        "leaf_nodes": [
          { "control_source_index": 1, "sdr_id": 920128532, "sn": "7CTDM5900B3X1B" },
          { "control_source_index": 2, "sdr_id": 911741468, "sn": "7CTDM5900BK07M" }
        ],
        "secret_code": [0,0,0,0,1,0,0,0,123,114,19,203,192,100,244,160,146,228,196,213,105,220,176,147,87,182,90,210]
      },
      "dock_infos": [
        {
          "dock_type": "takeoff",
          "sn": "7CTDM5900B3X1B",
          "latitude": 37.3487657248638,
          "longitude": 116.52893686422743,
          "height": 30.81130027770996,
          "heading": -78.7066650390625,
          "home_position_is_valid": 1,
          "index": 1,
          "rtcm_info": {
            "host": "120.253.226.97",
            "port": "8002",
            "mount_point": "RTCM33_GRCEJ",
            "rtcm_device_type": 1,
            "source_type": 3
          },
          "alternate_land_point": {
            "latitude": 37.348792490321514,
            "longitude": 116.52867090782102,
            "height": 0,
            "safe_land_height": 30,
            "is_configured": 1
          }
        },
        {
          "dock_type": "landing",
          "sn": "7CTDM5900BK07M",
          "latitude": 37.33605462094235,
          "longitude": 116.55416413516038,
          "height": 32.31420135498047,
          "heading": -69.79183197021484,
          "home_position_is_valid": 1,
          "index": 2,
          "rtcm_info": {
            "host": "120.253.226.97",
            "port": "8002",
            "mount_point": "RTCM33_GRCEJ",
            "rtcm_device_type": 1,
            "source_type": 3
          },
          "alternate_land_point": {
            "latitude": 37.336024417709915,
            "longitude": 116.554075635852,
            "height": 0,
            "safe_land_height": 30,
            "is_configured": 1
          }
        }
      ]
    }
  }
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success. |

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "flighttask_execute",
  "timestamp": 1234567890123,
  "data": { "result": 0 }
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/50.wayline.md]` | v1.11 canonical (Dock 2) — minor table formatting glitch on the `alternate_land_point.height` row; the v1.15 extract is cleaner. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Wayline-Management.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-WaylineManagement.txt]` | v1.15 (Dock 3). |
