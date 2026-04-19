# `psdk_widget_value_set` — set PSDK generic widget value

Cloud command that sets the integer value of a generic PSDK widget (switch, slider, progress, etc.) outside of an active DRC session. The semantics of the integer `value` are defined by the PSDK developer (e.g., a switch might use `0`/`1`; a slider might use `0`–`100`). Sister method to the DRC-session variant [`drc_psdk_widget_value_set`](../drc/drc_psdk_widget_value_set.md).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — PSDK payload. Payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `psdk_widget_value_set` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `psdk_widget_value_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `psdk_index` | integer | PSDK payload device index. |
| `index` | integer | Widget number (assigned by the PSDK developer). |
| `value` | integer | Widget value — semantics defined by the PSDK developer (switch state, slider position, etc.). |

### Example (down)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "data": {
    "index": 1,
    "psdk_index": 2,
    "value": 60
  },
  "method": "psdk_widget_value_set",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "timestamp": 1689740550047
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
  "timestamp": 1654070968655,
  "method": "psdk_widget_value_set"
}
```

## Relationship to other methods

- DRC-session equivalent: [`drc_psdk_widget_value_set`](../drc/drc_psdk_widget_value_set.md).
- Text-box text (as opposed to widget value) is set with [`psdk_input_box_text_set`](psdk_input_box_text_set.md).
- Current widget values are reported back to the cloud via [`drc_psdk_state_info`](../drc/drc_psdk_state_info.md) (DRC-only; Dock 3).

## Source inconsistencies flagged by DJI's own example

- **Dock 3 reply example `"timestamp:"` trailing-colon typo.** Dock 2 + v1.11 spell the key correctly.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/140.psdk.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-PSDK.txt]` | v1.15 (Dock 2) — identical. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-PSDK.txt]` | v1.15 (Dock 3) — identical apart from reply `"timestamp:"` typo. |
