# `psdk_floating_window_text` — PSDK floating-window text push

Event pushed by the dock relaying the content of the PSDK payload's floating-window UI element. PSDK payload developers use the floating window to render short status strings (system uptime, internal counters, developer diagnostics); this event lets the cloud mirror that text to operator UIs.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — PSDK payload. Payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `psdk_floating_window_text` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `psdk_index` | integer | PSDK payload device index (`0`–`3`). |
| `value` | string | Floating-window content text, as provided by the PSDK payload. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "data": {
    "psdk_index": 2,
    "value": "System time : 1193683 ms"
  },
  "gateway": "4TADKAQ000002J",
  "method": "psdk_floating_window_text",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "timestamp": 1689911744380
}
```

## Relationship to other methods

- The DRC-session equivalent is [`drc_psdk_floating_window_text`](../drc/drc_psdk_floating_window_text.md) (Dock 3 only) — identical shape, different topic.
- Widget-value updates (as opposed to floating-window text) come from the DRC-side [`drc_psdk_state_info`](../drc/drc_psdk_state_info.md).

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/140.psdk.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-PSDK.txt]` | v1.15 (Dock 2) — identical. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-PSDK.txt]` | v1.15 (Dock 3) — identical. |
