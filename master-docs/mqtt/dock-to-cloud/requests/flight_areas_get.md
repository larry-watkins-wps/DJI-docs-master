# `flight_areas_get` — dock requests the custom-flight-area file list

Device-initiated request by which the dock asks the cloud for the current custom-flight-area (CFA) file inventory. The cloud replies with a list of files — each carrying a name, pre-signed download URL, SHA-256 checksum, and size — and the dock uses those URLs to download the files and sync them onto the aircraft. Triggered by a prior [`flight_areas_update`](../services/flight_areas_update.md) command or on the dock's own schedule (e.g., after reboot).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, requests-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/requests` | `flight_areas_get` |
| Cloud → Device | `thing/product/{gateway_sn}/requests_reply` | `flight_areas_get` |

## Request (up) — `data` fields

`data: null`. The request carries no parameters.

### Example (request)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": null,
  "method": "flight_areas_get",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655
}
```

## Reply (down) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero represents an error. |
| `output` | struct | Present when `result = 0`. |
| `output.files` | array&lt;struct&gt; | Custom flight area files. Empty array when no files are defined for this device. |
| `output.files[].name` | string | File name. Expected shape: `geofence_{fileMD5}.json` (MD5 is placeholder for the file's MD5 digest). |
| `output.files[].url` | string | Pre-signed download URL. Expires per the STS configuration — the dock must download promptly. |
| `output.files[].checksum` | string | SHA-256 digest of the file contents. Dock verifies before accepting. |
| `output.files[].size` | integer | File size in bytes. |

### Example (reply)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "output": {
      "files": [
        {
          "checksum": "sha256",
          "name": "geofence_xxx.json",
          "size": 500,
          "url": "https://xx.oss-cn-hangzhou.aliyuncs.com/xx.json?Expires=xx&OSSAccessKeyId=xxx&Signature=xxx"
        }
      ]
    },
    "result": 0
  },
  "method": "flight_areas_get",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655
}
```

## File naming constraint

Per DJI's Dock 2 v1.15 documentation, CFA files **must** be named `geofence_{fileMD5}.json` where `{fileMD5}` is the MD5 of the file contents. The `output.files[].name` field reflects this convention; clouds generating CFA files must honor it to remain compatible. A downloadable file template is linked from the Dock 2 source page.

## Relationship to other methods

- Usually triggered by [`flight_areas_update`](../services/flight_areas_update.md); the dock pulls file URLs, downloads, and reports via [`flight_areas_sync_progress`](../events/flight_areas_sync_progress.md).
- Once loaded, the aircraft reports per-area geometry via [`flight_areas_drone_location`](../events/flight_areas_drone_location.md).
- Full Custom-Flight-Area choreography will be documented in Phase 9 workflow `workflows/flysafe-custom-flight-area-sync.md`.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/130.custom-flight-area.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Custom-Flight-Area.txt]` | v1.15 (Dock 2) — identical; adds file-naming constraint note. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Custom-Flight-Area.txt]` | v1.15 (Dock 3) — identical. |
