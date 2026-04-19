# `drc_mode_enter` — enter live flight controls mode

Cloud command that opens the DRC (direct remote control) session. The payload provides the dock with the MQTT relay broker connection info it must use for the low-latency DRC topic pair (`thing/product/{gateway_sn}/drc/up` + `/drc/down`). Also sets the reporting frequencies for the [`osd_info_push`](../drc/osd_info_push.md) and [`hsi_info_push`](../drc/hsi_info_push.md) DRC events.

Must be called after [`flight_authority_grab`](flight_authority_grab.md) / [`payload_authority_grab`](payload_authority_grab.md) and before any DRC-channel command.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `drc_mode_enter` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `drc_mode_enter` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `mqtt_broker` | struct | MQTT relay-broker connection info for the DRC channel. |
| `mqtt_broker.address` | string | Broker address + port, e.g. `192.0.2.1:8883`, `mqtt.dji.com:8883`. |
| `mqtt_broker.client_id` | string | MQTT client ID. Recommended: the device SN, optionally prefixed (e.g. `drc-4J4R101`). |
| `mqtt_broker.username` | string | Broker username. |
| `mqtt_broker.password` | string | Broker password (JWT or equivalent). |
| `mqtt_broker.expire_time` | integer (s) | Unix timestamp when credentials expire. Credentials are reusable within the validity window; expiry does not terminate already-established connections. |
| `mqtt_broker.enable_tls` | boolean | Whether to TLS-wrap the MQTT link. |
| `osd_frequency` | integer (Hz) | OSD reporting frequency. Range `1`–`30`. |
| `hsi_frequency` | integer (Hz) | HSI reporting frequency. Range `1`–`30`. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "hsi_frequency": 1,
    "mqtt_broker": {
      "address": "mqtt.dji.com:8883",
      "client_id": "sn_a",
      "enable_tls": true,
      "expire_time": 1672744922,
      "password": "jwt_token",
      "username": "sn_a_username"
    },
    "osd_frequency": 10
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "drc_mode_enter"
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
  "method": "drc_mode_enter"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
