# `config` — gateway asks the cloud for configuration

The gateway requests its configuration from the cloud — License parameters (app_id / app_key / app_license), NTP server host and port. Sent at startup, before the gateway can bind or run operational traffic. The License parameters in the reply gate subsequent MQTT traffic: a gateway without a valid License cannot proceed to [`airport_organization_bind`](airport_organization_bind.md).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, request-reply, `tid`/`bid` correlation) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload in both cohorts.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/requests` | `config` |
| Cloud → Device | `thing/product/{gateway_sn}/requests_reply` | `config` |

## Request (up) — `data` fields

| Field | Type | Description |
|---|---|---|
| `config_type` | enum string | Configuration format. Documented value: `"json"`. |
| `config_scope` | enum string | Configuration dimension. Documented value: `"product"`. |

### Example

```json
{
  "tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
  "bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
  "gateway": "sn",
  "timestamp": 1667803298000,
  "method": "config",
  "data": {
    "config_scope": "product",
    "config_type": "json"
  }
}
```

## Reply (down) — `data` fields

| Field | Type | Description |
|---|---|---|
| `app_id` | string | App ID created at the DJI Developer Website. |
| `app_key` | string | App Key created at the DJI Developer Website. |
| `app_license` | string | App License created at the DJI Developer Website. |
| `ntp_server_host` | string | NTP service hostname. |
| `ntp_server_port` | integer | NTP server port. If omitted, default is `123`. |

### Example

```json
{
  "tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
  "bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
  "gateway": "sn",
  "timestamp": 1667803298000,
  "method": "config",
  "data": {
    "app_id": "123456",
    "app_key": "app_key",
    "app_license": "app_license",
    "ntp_server_host": "host_url",
    "ntp_server_port": 456
  }
}
```

> **Note on `app_id` type.** v1.11 Cloud-API-Doc/ shows `"app_id": 123456` (integer) in the example; v1.15 `DJI_Cloud/` shows `"app_id": "123456"` (string). The v1.15 string form matches the documented type (`text`) and is the current canonical; v1.11's integer form is a documentation example inconsistency.

## Relationship to other methods

- This request bootstraps the gateway's ability to bind. See [`airport_organization_bind`](airport_organization_bind.md) for the follow-on step.
- Full startup-and-pairing sequence documented in Phase 9 workflow `workflows/dock-bootstrap-and-pairing.md`.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/100.config.md]` | v1.11 canonical (Dock 2) — method, parameters, examples. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Configuration-Update.txt]` | v1.15 (Dock 2) — identical payload; `app_id` shown as string. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Configuration-Update.txt]` | v1.15 (Dock 3) — identical payload; confirms Dock 3 uses the same shape. |
