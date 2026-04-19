# `ota_progress` — firmware-update task progress

Event pushed by the device after [`ota_create`](../services/ota_create.md) to report percent-complete and current step of the firmware-update task. The `bid` on each event matches the `bid` the cloud issued on the originating `ota_create` — correlate progress back to a specific upgrade by `bid`.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, events-reply pattern) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3**. Payload shape is identical in v1.15 across both docks. The `current_step` field was named `step_key` in v1.11 — see [Source differences](#source-differences).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `ota_progress` |

The device does not set `need_reply` on this event; the cloud is not required to publish an `events_reply`.

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |
| `output.status` | enum string | Task state. One of `sent`, `in_progress`, `paused`, `ok`, `failed`, `canceled`, `rejected`, `timeout`. |
| `output.progress.percent` | int | Progress percentage. `0`–`100`, step `1`. |
| `output.progress.current_step` | enum string | Current step. `download_firmware` = firmware download in progress; `upgrade_firmware` = update is being applied. *Named `step_key` in v1.11.* |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "output": {
      "progress": {
        "percent": 10,
        "current_step": "download_firmware"
      },
      "status": "in_progress"
    },
    "result": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "ota_progress"
}
```

## Relationship to other methods

- Triggered by a preceding [`ota_create`](../services/ota_create.md) command. The `bid` is reused across all progress events for the same upgrade so the cloud can correlate the stream of events back to the originating task.
- Terminal `output.status` values are `ok`, `failed`, `canceled`, `rejected`, and `timeout`. A dock that reports `paused` can still transition back to `in_progress`.

## Source differences

- **`current_step` / `step_key` field-name drift.** v1.11 Dock 2 names the nested step field `step_key` (both table and example). v1.15 Dock 2 and v1.15 Dock 3 name it `current_step` (both table and example). Wire-level change, not a cosmetic table edit — a cloud implementation must accept the correct name per firmware version.
- **Example envelope differs by source on the `method` key.** The v1.15 Dock 3 example includes `"method": "ota_progress"` inside the envelope; v1.15 Dock 2 and v1.11 Dock 2 examples omit the `method` key (but keep `tid` / `bid` / `timestamp`). The `method` key is otherwise standard on MQTT topics — treat its presence in Dock 3's example as the reliable form.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/80.firmware.md]` | v1.11 canonical (Dock 2) — uses `step_key` name. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Firmware-Upgrade.txt]` | v1.15 (Dock 2) — renames to `current_step`. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Firmware-Upgrade.txt]` | v1.15 (Dock 3) — same payload as v1.15 Dock 2. |
