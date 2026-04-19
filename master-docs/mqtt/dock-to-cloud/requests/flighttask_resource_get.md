# `flighttask_resource_get` — fetch the KMZ wayline file for a mission

Device-initiated request. The dock asks the cloud for a fresh pre-signed URL to the KMZ wayline file associated with a given `flight_id`. Used when the dock needs to re-download a mission (e.g., after a failure, or when resuming from breakpoint and the local copy is missing).

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/requests` | `flighttask_resource_get` |
| Cloud → Device | `thing/product/{gateway_sn}/requests_reply` | `flighttask_resource_get` |

## Up (request) — `data` fields

| Field | Type | Description |
|---|---|---|
| `flight_id` | string | Task ID for which to fetch resources. |

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "flighttask_resource_get",
  "timestamp": 1234567890123,
  "data": {
    "flight_id": "xxxxxxx"
  }
}
```

## Down (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success. |
| `output.file.url` | string | Pre-signed URL to the KMZ wayline file. |
| `output.file.fingerprint` | string | MD5 signature for integrity check. |

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "flighttask_resource_get",
  "timestamp": 1234567890123,
  "data": {
    "result": 0,
    "output": {
      "file": {
        "url": "https://xx.oss-cn-hangzhou.aliyuncs.com/xx.kmz?Expires=xx&OSSAccessKeyId=xxx&Signature=xxx",
        "fingerprint": "signxxxx"
      }
    }
  }
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/50.wayline.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Wayline-Management.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-WaylineManagement.txt]` | v1.15 (Dock 3). |
