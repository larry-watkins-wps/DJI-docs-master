# `fileupload_update` — cancel an in-progress log upload

Cloud command that terminates a running log-upload batch by module. The current `status` enum has only one value (`cancel`) — the method is effectively "cancel uploads for these modules".

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `fileupload_update` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `fileupload_update` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `status` | enum string | Upload state to transition to. Only defined value: `cancel`. (Description wording drifts: v1.15 Dock 3 says `"Cancel"`, v1.15 Dock 2 + v1.11 say `"Cancelled"` — the enum key is stable.) |
| `module_list` | array | Modules to apply the update to. Serialized as an array of strings (`["0", "3"]` — Aircraft + Dock). Schema declares the array's `item_type` as blank in all three sources. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "module_list": [
      "0",
      "3"
    ],
    "status": "cancel"
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "fileupload_update"
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "result": 0
  },
  "gateway": "",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1655781392412,
  "method": "fileupload_update"
}
```

## Relationship to other methods

- Cancels a batch started by [`fileupload_start`](fileupload_start.md). The dock is expected to stop emitting further [`fileupload_progress`](../events/fileupload_progress.md) events for the cancelled modules.
- The correlation between the cancel and a specific prior `fileupload_start` is implicit — DJI does not specify whether `bid` must match the original start, whether `module_list` alone is sufficient, or both. See [`OPEN-QUESTIONS.md` OQ-005](../../../OPEN-QUESTIONS.md#oq-005--fileupload_start--fileupload_progress-correlation-key-is-undocumented).

## Source inconsistencies flagged by DJI's own example

- **Enum description wording drift**: `"cancel": "Cancel"` (Dock 3 v1.15) vs `"cancel": "Cancelled"` (Dock 2 v1.15, v1.11). Wire key `cancel` is stable.
- **`module_list.item_type` is blank** in the schema across all three sources — DJI left the array item type unspecified. Examples always send strings (`"0"`, `"3"`) matching the `module` encoding elsewhere.
- **Down example omits `timestamp`** while the reply example carries it — same envelope optionality as other `/services` commands.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/90.log.md]` | v1.11 canonical (Dock 2) — `cancel: Cancelled`. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Log.txt]` | v1.15 (Dock 2) — `cancel: Cancelled`. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Log.txt]` | v1.15 (Dock 3) — `cancel: Cancel`. |
