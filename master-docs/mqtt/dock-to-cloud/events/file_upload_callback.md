# `file_upload_callback` — dock reports a single media file upload

Event pushed by the dock after a media file has been uploaded to the object-storage bucket (for which the dock fetched temporary credentials via [`storage_config_get`](../requests/storage_config_get.md)). The cloud uses this to register the file, index its metadata, and associate it with the originating flight task. Requires reply (`need_reply: 1`).

One event per file. For a wayline task producing 14 photos, expect 14 `file_upload_callback` events.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, events-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3**. Payload shape is identical across v1.11, v1.15 Dock 2, and v1.15 Dock 3 for the `file` struct. A v1.11-only `flight_task` struct (per-task progress counters) is absent from v1.15 tables — see [Source differences](#source-differences).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `file_upload_callback` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `file_upload_callback` |

## Up — `data` fields

### `file` — uploaded file descriptor

| Field | Type | Description |
|---|---|---|
| `file.object_key` | string | Key of the file inside the object-storage bucket (S3 / OSS / MinIO path). |
| `file.path` | string | Business path — logical folder hierarchy the cloud should display the file under. |
| `file.name` | string | Filename (including extension). |
| `file.cloud_to_cloud_id` | string | ID of the destination cloud-to-cloud bucket. `"DEFAULT"` when the file is not routed to an alternate (customer-supplied) bucket. *v1.11 table documents this; v1.15 tables omit the row but the examples carry it.* |
| `file.ext` | struct | File extension/extra context. |
| `file.ext.flight_id` | string | Flight-task ID this file belongs to. |
| `file.ext.drone_model_key` | string | Aircraft product enumeration value (e.g., `0-67-0`). Full enum in Phase 6 (`device-properties/`). |
| `file.ext.payload_model_key` | string | Payload product enumeration value. |
| `file.ext.is_original` | boolean | `true` = original image; `false` = thumbnail/derived. |
| `file.metadata` | struct | Capture-time sensor metadata. |
| `file.metadata.gimbal_yaw_degree` | float | Gimbal yaw (pan) angle at capture. |
| `file.metadata.absolute_altitude` | float | Absolute altitude (meters) at capture. |
| `file.metadata.relative_altitude` | float | Relative altitude (meters) at capture. |
| `file.metadata.create_time` | ISO 8601 date | Capture time. |
| `file.metadata.shoot_position` | struct | Capture position. |
| `file.metadata.shoot_position.lat` | float | Latitude. |
| `file.metadata.shoot_position.lng` | float | Longitude. |

### `flight_task` — per-task progress counters (v1.11 only)

v1.11 Dock 2 documents an additional sibling struct that tracks per-task upload progress. The v1.15 tables (both Dock 2 and Dock 3) no longer list these fields; see [Source differences](#source-differences).

| Field | Type | Description |
|---|---|---|
| `flight_task.uploaded_file_count` | integer | Files uploaded so far for this flight. |
| `flight_task.expected_file_count` | integer | Total files expected for this flight. |
| `flight_task.flight_type` | enum int | `0` = Wayline mission, `1` = One-key takeoff mission. |

### Example (v1.11 Dock 2 — fullest form)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "file": {
      "cloud_to_cloud_id": "DEFAULT",
      "ext": {
        "drone_model_key": "0-67-0",
        "flight_id": "xxx",
        "is_original": true,
        "payload_model_key": "0-67-0"
      },
      "metadata": {
        "absolute_altitude": 56.311,
        "create_time": "2021-05-10 16:04:20",
        "gimbal_yaw_degree": "-91.40",
        "relative_altitude": 41.124,
        "shoot_position": {
          "lat": 22.1,
          "lng": 122.5
        }
      },
      "name": "dog.jpeg",
      "object_key": "object_key",
      "path": "xxx"
    },
    "flight_task": {
      "expected_file_count": 14,
      "flight_type": 0,
      "uploaded_file_count": 12
    }
  },
  "gateway": "xxx",
  "method": "file_upload_callback",
  "need_reply": 1,
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655
}
```

### Example (v1.15 — `flight_task` absent)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "file": {
      "cloud_to_cloud_id": "DEFAULT",
      "ext": {
        "drone_model_key": "0-67-0",
        "flight_id": "xxx",
        "is_original": true,
        "payload_model_key": "0-67-0"
      },
      "metadata": {
        "absolute_altitude": 56.311,
        "create_time": "2021-05-10 16:04:20",
        "gimbal_yaw_degree": "-91.40",
        "relative_altitude": 41.124,
        "shoot_position": {
          "lat": 22.1,
          "lng": 122.5
        }
      },
      "name": "dog.jpeg",
      "object_key": "object_key",
      "path": "xxx"
    }
  },
  "gateway": "xxx",
  "method": "file_upload_callback",
  "need_reply": 1,
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655
}
```

## Down (reply) — `data` fields

Standard events_reply envelope: `data.result` (integer; `0` = success).

## Source differences

- **`flight_task` struct** is documented only in v1.11 Dock 2; the v1.15 Dock 2 and v1.15 Dock 3 tables drop it. A server implementation should treat it as present-but-optional and handle absence (v1.15 clients will not send it).
- **`file.cloud_to_cloud_id`**: v1.11 Dock 2 documents this field in the data table. v1.15 tables don't list it, but both v1.15 Dock 2 and Dock 3 examples include it in the `file` struct — so the field is present on the wire in v1.15 as well.
- **Typo in Dock 3 source**: the timestamp key in the Dock 3 example is `"timestamp"` (correct here — some sibling Dock 3 files use `"timestamp:"` with a trailing colon).

## Source inconsistencies flagged by DJI's own example

None within this method beyond the `flight_task` / `cloud_to_cloud_id` table-vs-example divergence noted above.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/40.file.md]` | v1.11 canonical (Dock 2) — fullest shape, documents the optional `flight_task` counters. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Media-Management.txt]` | v1.15 (Dock 2) — drops `flight_task` from the table. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Media-Management.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
