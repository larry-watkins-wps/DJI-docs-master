# `rtk_calibration` — RTK manual-calibration result

Event pushed by the dock after it finishes the [`rtk_calibration`](../services/rtk_calibration.md) service. Unlike other Remote-Debugging events this is not a per-step progress stream — it is a terminal result push that carries per-device status codes and an overall verdict. It is also the **only event in 4e that sets `need_reply: 1`** — the cloud is expected to ACK via `events_reply` with `{"result": 0}`, matching the 4d [`file_upload_callback`](file_upload_callback.md) pattern.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, events-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — absent from Dock 2 Remote-Debugging. No v1.11 counterpart.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `rtk_calibration` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `rtk_calibration` |

`need_reply: 1` is set in the event envelope — the cloud is obliged to publish an `events_reply` carrying `data.result = 0` (or a non-zero error). The specific reply schema is not documented in DJI source; treat as standard `data.result`.

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Top-level return code — fixed `0`. Actual per-device outcomes live in `output.ext.devices[].result`. |
| `output.status` | enum string | Overall verdict. `ok` = every device calibrated successfully; `failed` = any device failed. |
| `output.progress.percent` | int | Progress percentage — the dock only pushes terminal results, so values are `0` (overall failure) or `100` (overall success). |
| `output.progress.current_step` | int | Fixed `1`. |
| `output.ext.version` | int | Calibration format version. Example value: `1`. |
| `output.ext.devices` | array of struct | Per-device calibration result. |
| `output.ext.devices[].sn` | string | Device serial number. |
| `output.ext.devices[].type` | enum int | Calibration type. `1` = Manual calibration. |
| `output.ext.devices[].module` | enum string | Module. `"3"` = Dock, `"6"` = Relay. |
| `output.ext.devices[].result` | int | Per-device result code. `0` = success; non-zero = failure (check against error-code catalog in Phase 8). |
| `output.ext.devices[].status` | enum string | Per-device status — same enum as `output.status` (`canceled` / `failed` / `in_progress` / `ok` / `paused` / `rejected` / `sent` / `timeout`). On timeout the device returns `failed` with an error code. |

### Example

```json
{
  "method": "rtk_calibration",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1676948902792,
  "need_reply": 1,
  "data": {
    "output": {
      "ext": {
        "devices": [
          {
            "sn": "string",
            "type": 1,
            "module": "3",
            "result": 0,
            "status": "ok"
          },
          {
            "sn": "string",
            "type": 1,
            "module": "6",
            "result": 341010,
            "status": "failed"
          }
        ],
        "version": 1
      },
      "progress": {
        "percent": 0,
        "current_step": 1
      },
      "status": "failed"
    },
    "result": 0
  },
  "gateway": "sn"
}
```

## Down (reply) — `data` fields

Standard events-reply shape: `data.result` (integer; `0` = success). Not documented explicitly by DJI.

## Source inconsistencies flagged by DJI's own example

- **`"status": "ok"` has an empty description** in the Dock 3 schema (`"ok":""`). Treat as success (matches the status enum shared by every other Remote-Debugging event).
- **`type` enum only defines `1 = Manual calibration`.** Automatic or scheduled calibration types may exist but are not documented.
- **Example uses correct `"timestamp"`** — contrast with the other Dock 3 Remote-Debugging event examples where the `"timestamp:"` trailing-colon typo is pervasive.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3) — only source; method absent from Dock 2 v1.15. |
