# `unlock_license_update` — push a new unlocking-license file to the device

Cloud command that hands the dock (or aircraft via the dock) a signed FlySafe unlocking-license file to import. The `file` struct is **optional**: when provided, the dock downloads from `file.url`, verifies the MD5 signature in `file.fingerprint`, and imports the licenses contained in the file; when omitted, the dock instead pulls the latest licenses directly from the FlySafe server (online-unlock flow).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `unlock_license_update` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `unlock_license_update` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `file` | struct | **Optional.** Offline license file to import. When the field is present, the dock downloads from `file.url` and verifies against `file.fingerprint` before importing. When absent, the dock falls back to pulling from the online FlySafe server. |
| `file.url` | string | Pre-signed URL of the license file (KMZ / JSON as supplied by the Flysafe server). |
| `file.fingerprint` | string | MD5 signature of the file contents; the dock must verify before importing. |

### Example (down — offline file provided)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "file": {
      "fingerprint": "xxxx",
      "url": "https://xx.oss-cn-hangzhou.aliyuncs.com/xx.kmz?Expires=xx&OSSAccessKeyId=xxx&Signature=xxx"
    }
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero represents an error. |

### Example (reply)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "result": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1234567890123
}
```

## Relationship to other methods

- After an update, call [`unlock_license_list`](unlock_license_list.md) to observe the resulting license inventory.
- Individual licenses can then be toggled with [`unlock_license_switch`](unlock_license_switch.md).
- Full FlySafe choreography will be documented in Phase 9 workflow `workflows/flysafe-custom-flight-area-sync.md`.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/170.flysafe.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-FlySafe.txt]` | v1.15 (Dock 2) — identical payload. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-FlySafe.txt]` | v1.15 (Dock 3, hand-authored) — identical payload. |
