# `fileupload_progress` — per-file log-upload progress

Event pushed by the dock during an in-flight log-upload batch started by [`fileupload_start`](../services/fileupload_start.md). Each event reports per-file status for every module whose logs the dock is uploading to object storage. Upload is file-oriented — one batch can cover multiple aircraft and dock logs concurrently.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3**. Payload shape is identical across v1.11, v1.15 Dock 2, and v1.15 Dock 3 except for one Dock 3 field-name typo — see [Source inconsistencies](#source-inconsistencies-flagged-by-djis-own-example).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `fileupload_progress` |

**Reply is not expected.** The event carries `"need_reply": 0` explicitly — the cloud does not publish an `events_reply` for this method (contrast [`file_upload_callback`](file_upload_callback.md) which sets `need_reply: 1`).

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code for the overall event. Non-zero represents an error. |
| `output.status` | enum string | Batch status (e.g. `ok`). |
| `output.ext.files` | array of struct | One entry per file in the batch. |
| `output.ext.files[].module` | enum int | Owning module. `0` = Aircraft, `3` = Dock. *Declared `enum_int` but serialized as a string (`"0"` / `"3"`) in every source example.* |
| `output.ext.files[].size` | int (bytes) | File size. |
| `output.ext.files[].device_sn` | string | Source device serial number. |
| `output.ext.files[].key` | string | Object-storage key that the file was uploaded under. |
| `output.ext.files[].fingerprint` | string | File fingerprint (content hash). |
| `output.ext.files[].progress` | struct | Per-file progress — see below. |

### Per-file `progress` sub-struct

The schema tables declare only three fields here (`progress`, `finish_time`, `upload_rate`), but every source example additionally carries `current_step`, `result`, `status`, and (on the second array element) `total_step`. Treat the fields below as the practical on-the-wire set.

| Field | Type | Description |
|---|---|---|
| `progress.progress` | int | Percent complete, `0`–`100`. *In the v1.15 Dock 3 **table** this innermost field is spelled `prgress` (missing "o") — the v1.15 Dock 3 example correctly uses `progress`. Treat the example as authoritative and use `progress`.* |
| `progress.current_step` | int | Current step index within the upload state machine (not declared in the schema; value `19` in DJI's example). |
| `progress.total_step` | int | Total steps in the upload state machine (value `30` in DJI's example; present on the second array element only). |
| `progress.status` | string | Per-file status (e.g. `ok`). |
| `progress.result` | int | Per-file result code (`0` = success). |
| `progress.finish_time` | int (ms epoch) | Upload completion time. |
| `progress.upload_rate` | int | Upload throughput (bytes/sec, or a DJI-internal rate — not specified). |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "output": {
      "ext": {
        "files": [
          {
            "device_sn": "drone_sn",
            "fingerprint": "4f65b891f3bc09bdb6d4c36a996b532d",
            "key": "4bf0039f-6434-44a8-b891-8d7b6b7ff138/drone_sn/video_20220621_110830.log",
            "module": "0",
            "progress": {
              "current_step": 19,
              "finish_time": 1655781395926,
              "progress": 100,
              "result": 0,
              "status": "ok",
              "upload_rate": 0
            },
            "size": 155232
          },
          {
            "device_sn": "dock_sn",
            "fingerprint": "4f65b891f3bc09bdb6d4c36a996b532d",
            "key": "4bf0039f-6434-44a8-b891-8d7b6b7ff138/dock_sn/video_20220621_110830.log",
            "module": "3",
            "progress": {
              "current_step": 19,
              "finish_time": 1655781395926,
              "progress": 100,
              "result": 0,
              "status": "ok",
              "total_step": 30,
              "upload_rate": 0
            },
            "size": 155232
          }
        ]
      },
      "status": "ok"
    }
  },
  "gateway": "dock_sn",
  "need_reply": 0,
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1655781395926,
  "method": "fileupload_progress"
}
```

(The v1.15 Dock 2 and v1.11 example envelopes omit the `method` key; the v1.15 Dock 3 example includes it.)

## Relationship to other methods

- Follows a [`fileupload_start`](../services/fileupload_start.md) service command that delivered the STS credentials and per-module file list to upload.
- A follow-up [`fileupload_update`](../services/fileupload_update.md) can cancel the batch mid-stream.
- **How the cloud correlates events back to the triggering batch is undocumented by DJI** — see [`OPEN-QUESTIONS.md` OQ-005](../../../OPEN-QUESTIONS.md#oq-005--fileupload_start--fileupload_progress-correlation-key-is-undocumented). The per-file `key` and `fingerprint` are the most reliable correlation handles; `bid` reuse is plausible but not confirmed by source.

## Source inconsistencies flagged by DJI's own example

- **`prgress` typo** in the v1.15 Dock 3 schema table — a missing "o". The v1.15 Dock 3 example correctly spells `progress`. The v1.15 Dock 2 and v1.11 schemas also spell it correctly. Use `progress`.
- **`module` declared `enum_int` but serialized as a string** in all source examples (`"0"` and `"3"`). Dock 2 and v1.11 behave the same way. Treat on-the-wire values as strings.
- **Schema tables don't list every field in the example.** `progress.current_step`, `progress.total_step`, `progress.status`, and `progress.result` appear in every source example but in none of the schema tables. The fields are present on the wire — use the example as authoritative.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/90.log.md]` | v1.11 canonical (Dock 2) — `progress` spelled correctly; schema omits extra example fields. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Log.txt]` | v1.15 (Dock 2) — identical to v1.11 shape. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Log.txt]` | v1.15 (Dock 3) — schema typo `prgress`; example identical to Dock 2. |
