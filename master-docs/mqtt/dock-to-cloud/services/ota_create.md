# `ota_create` — deliver firmware and start an upgrade task

Cloud command that hands the dock a list of firmware artifacts (each with SN, version, download URL, MD5, size, and upgrade type) and instructs the dock/aircraft to start an OTA upgrade. The `services_reply` ACKs with a task-state handshake; thereafter the dock pushes [`ota_progress`](../events/ota_progress.md) events under the same `bid` until the task terminates.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3**. Shared payload shape; the `firmware_upgrade_type` enum adds one Dock-3-only value — see [Source differences](#source-differences).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `ota_create` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `ota_create` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `devices` | array of struct | Firmware update targets. Array `size: 2` — typically one aircraft entry and one dock entry. Callers may supply a single-device array when only one target is being upgraded. |
| `devices[].sn` | string | Target device serial number. Max length 10240 per DJI's declared constraint. |
| `devices[].product_version` | string | Firmware version to install (e.g. `1.00.223`). |
| `devices[].file_url` | string | Download URL the dock fetches the firmware from. |
| `devices[].md5` | string | MD5 checksum of the firmware file. |
| `devices[].file_size` | int | Firmware file size in bytes. |
| `devices[].file_name` | string | Firmware filename. |
| `devices[].firmware_upgrade_type` | enum int | Upgrade mode. `2` = **Consistency upgrade** (bring the device in line with a target version, enforcing a compatible multi-device set); `3` = **Standard / regular upgrade** (Dock 2 v1.15 + v1.11 label it "Regular upgrade", Dock 3 v1.15 labels it "Standard update"); `4` = **psdk update** (Dock 3 only — used when upgrading an on-dock PSDK payload). |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "devices": [
      {
        "file_name": "wm245_1.00.223.zip",
        "file_size": 653467234,
        "file_url": "https://s3.com/xxx.zip",
        "firmware_upgrade_type": 2,
        "md5": "abcdefabcdefabcdef",
        "product_version": "1.00.223",
        "sn": "drone_sn"
      },
      {
        "firmware_upgrade_type": 3,
        "product_version": "1.00.223",
        "sn": "dock_sn"
      }
    ]
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "ota_create"
}
```

The second array element in DJI's own example omits `file_url` / `md5` / `file_size` / `file_name` — implying those fields are optional when the dock already has the artifact available locally (the dock's own firmware flow can reuse a staged image). Treat the fields as required for the target that owns the artifact and optional for secondary targets that inherit it.

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |
| `output.status` | enum string | Task state at ACK time. Typically `sent` (accepted, upgrade starting) or `in_progress`. Full enum is `sent / in_progress / paused / ok / failed / canceled / rejected / timeout` (shared with [`ota_progress`](../events/ota_progress.md)). |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "output": {
      "status": "in_progress"
    },
    "result": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "ota_create"
}
```

## Relationship to other methods

- After ACK, the dock pushes [`ota_progress`](../events/ota_progress.md) events carrying the same `bid` until it reaches a terminal state.
- The `bid` the cloud issues on `ota_create` is the correlation key for the entire upgrade transaction.

## Source differences

- **`firmware_upgrade_type` enum widens on Dock 3.** Dock 2 (v1.11 + v1.15) accepts only `{2, 3}` (Consistency + Regular upgrade). Dock 3 adds `4 = psdk update` for upgrading an on-dock PSDK payload.
- **Wording drift on `firmware_upgrade_type` labels.** v1.11 Dock 2 and v1.15 Dock 2 say "upgrade" ("Consistency upgrade", "Regular upgrade"). v1.15 Dock 3 says "update" ("Consistency update", "Standard update"). The field name itself is stable as `firmware_upgrade_type` across all three sources.
- **Section headings:** v1.11 Dock 2 and v1.15 Dock 2 title the section "Firmware upgrade"; v1.15 Dock 3 titles it "Firmware Update".

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/80.firmware.md]` | v1.11 canonical (Dock 2) — `firmware_upgrade_type` enum has `{2, 3}` only. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Firmware-Upgrade.txt]` | v1.15 (Dock 2) — enum unchanged from v1.11. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Firmware-Upgrade.txt]` | v1.15 (Dock 3) — enum adds `4 = psdk update`; labels switch to "update" wording. |
