# `rtk_calibration` — trigger manual RTK calibration

Cloud command that triggers manual RTK calibration for a named device set (dock + optional relay), each supplied with a longitude / latitude / height fixpoint. The dock runs the calibration and pushes the terminal result via the [`rtk_calibration`](../events/rtk_calibration.md) event — the only `need_reply: 1` event in 4e.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — absent from Dock 2 Remote-Debugging. No v1.11 counterpart.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `rtk_calibration` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `rtk_calibration` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `devices` | array of struct | Calibration device list. |
| `devices[].sn` | string | Device serial number. Max length 10240. |
| `devices[].type` | enum int | Calibration type. Only defined value: `1` = Manual calibration. |
| `devices[].module` | enum string | `"3"` = Dock; `"6"` = Relay. (Declared `enum_string` with numeric-valued keys — the stored type is string, not int.) |
| `devices[].data` | struct | Fixpoint data for this device. |
| `devices[].data.longitude` | double | Longitude (decimal degrees). |
| `devices[].data.latitude` | double | Latitude (decimal degrees). |
| `devices[].data.height` | double | Height (meters). |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp:": 1654070968655,
  "method": "rtk_calibration",
  "data": {
    "devices": [
      {
        "sn": "string",
        "type": 1,
        "module": "3",
        "data": {
          "height": 60.285194396972656,
          "latitude": 22.755022128112614,
          "longitude": 114.89828051067889
        }
      }
    ]
  }
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |
| `output.status` | enum string | Task state — `canceled` / `failed` / `in_progress` / `ok` / `paused` / `rejected` / `sent` / `timeout`. |

## Relationship to other methods

- Terminal result pushed via the [`rtk_calibration`](../events/rtk_calibration.md) event (`need_reply: 1`, cloud ACKs with `data.result = 0`).
- Only meaningful for Dock 3 — no Dock 2 counterpart.

## Source inconsistencies flagged by DJI's own example

- **`"timestamp:"` typo** (trailing colon) in the services-down example at L1071.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3) — only source. |
