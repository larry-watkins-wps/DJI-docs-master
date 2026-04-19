# `fileupload_list` — enumerate uploadable log files on the device

Cloud command that asks the dock (and sub-devices) for the list of log files currently available for upload, filtered by module. The reply returns per-module file indexes with start/end times and sizes, so the cloud can display a picker or decide which slices to request via [`fileupload_start`](fileupload_start.md).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3**. Shared payload shape. The unit label on the reply's `start_time` / `end_time` fields is inconsistent across sources — see [Source inconsistencies](#source-inconsistencies-flagged-by-djis-own-example).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `fileupload_list` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `fileupload_list` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `module_list` | array | Module filter list — returned log files are scoped to these modules. Declared as `array` of `enum_int`, but serialized as an array of **strings** in every source example (`["0", "3"]`). Values: `"0"` = Aircraft, `"3"` = Dock. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "module_list": [
      "0",
      "3"
    ]
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "fileupload_list"
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Top-level result for the request. Non-zero represents an error. |
| `files` | array of struct | One entry per requested module. Schema says `size: 2`; effectively "one per module in `module_list`". |
| `files[].device_sn` | string | Serial number of the device owning the logs. |
| `files[].module` | enum int | `0` = Aircraft, `3` = Dock. Serialized as string in examples. |
| `files[].result` | int | Per-module result (non-zero = that module failed to enumerate). |
| `files[].list` | array of struct | One entry per boot/session. |
| `files[].list[].boot_index` | int | Boot session index — the device's internal counter that identifies which boot produced the log slice. |
| `files[].list[].start_time` | int (ms epoch) | Start of the log window, epoch-milliseconds. DJI's v1.11 and Dock 2 v1.15 tables label this "Seconds / s" but every source's example uses millisecond-scale values (`1654070968655`, `1659427398806`); Dock 3 v1.15 is the only table that labels it correctly as "Milliseconds / ms". Treat the v1.11 / Dock 2 "seconds" label as a DJI source-table typo. Resolved as [OQ-004](../../../OPEN-QUESTIONS.md#oq-004--fileupload_list-log-window-timestamp-unit-is-inconsistent-across-dji-sources) 2026-04-19. |
| `files[].list[].end_time` | int (ms epoch) | End of the log window — epoch-milliseconds, same convention as `start_time`. |
| `files[].list[].size` | int (bytes) | Log file size. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "files": [
      {
        "device_sn": "xxxxxxxxx",
        "list": [
          {
            "boot_index": 1111,
            "end_time": 1659427398806,
            "size": 33789,
            "start_time": 1654070968655
          },
          {
            "boot_index": 22222,
            "end_ime": 1659427398806,
            "size": 33789,
            "start_time": 1659427398806
          }
        ],
        "module": "0",
        "result": 0
      },
      {
        "device_sn": "device_sn",
        "list": [
          {
            "boot_index": 11111,
            "end_time": 1659427398806,
            "size": 36772,
            "start_time": 1659427398806
          },
          {
            "boot_index": 22222,
            "end_ime": 1659427398806,
            "size": 33789,
            "start_time": 1659427398806
          }
        ],
        "module": "3",
        "result": 0
      }
    ],
    "result": 0
  },
  "gateway": "",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "fileupload_list"
}
```

## Relationship to other methods

- Typically called before [`fileupload_start`](fileupload_start.md) to discover which `boot_index` values and size ranges are available for a module.
- `fileupload_start`'s `params.files[].list[].boot_index` values are drawn from this reply.

## Source inconsistencies flagged by DJI's own example

- **`end_ime` typo** (missing `t`) in the second element of each `list` array in every source example. The schema is `end_time`; the typo reproduces verbatim across v1.11, v1.15 Dock 2, and v1.15 Dock 3. Treat as a copy-paste artifact in DJI's example — on the wire the field is `end_time`.
- **`module_list` declared `enum_int`, sent as `enum_string`.** All examples quote the enum values; treat them as strings.
- **Time-unit label disagreement** — v1.11 and Dock 2 v1.15 mislabel `start_time` / `end_time` as seconds; Dock 3 v1.15 and every source's example values confirm the fields are epoch-milliseconds. Resolved as [OQ-004](../../../OPEN-QUESTIONS.md#oq-004--fileupload_list-log-window-timestamp-unit-is-inconsistent-across-dji-sources).

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/90.log.md]` | v1.11 canonical (Dock 2) — says "Seconds / s"; example values are ms. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Log.txt]` | v1.15 (Dock 2) — still says "Seconds / s". |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Log.txt]` | v1.15 (Dock 3) — says "Milliseconds / ms"; example values match. |
