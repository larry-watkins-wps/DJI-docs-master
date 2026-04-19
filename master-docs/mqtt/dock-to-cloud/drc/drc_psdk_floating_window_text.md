# `drc_psdk_floating_window_text` — PSDK floating-window text push

Event pushed by a PSDK payload with the content to display in the pilot's floating-window overlay. The `psdk_index` identifies which payload instance (index assigned by the device). Typically used by third-party payloads to surface status text (battery, signal, custom metrics) to the operator.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — absent from Dock 2 Remote-Control and v1.11.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `drc_psdk_floating_window_text` |

**Topic note.** Unlike other `drc_*` methods in this catalog, `drc_psdk_floating_window_text` lands on the **standard `/events` topic**, not the lightweight `/drc/up` DRC channel. The envelope shown in the DJI example is also lightweight (just `method`, `seq`, `data`) — DJI's own source is inconsistent about whether a full `tid`/`bid`/`timestamp` envelope is layered on top; treat the envelope as whatever the server's MQTT connection carries, with `seq` as the in-order sequence key per the DRC pattern.

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `psdk_index` | int | PSDK payload device index (pushed by the device). |
| `floating_window_text` | string | Text content for the floating-window overlay. |

### Example

```json
{
  "data": {
    "floating_window_text": "",
    "psdk_index": 0
  },
  "method": "drc_psdk_floating_window_text",
  "seq": 1
}
```

## Source inconsistencies flagged by DJI's own example

- **Example envelope is lightweight** (no `tid` / `bid` / `timestamp`) while the topic is `/events` — mixed-envelope shape. Either DJI's example is abbreviated or this method uses the DRC-style envelope despite riding the `/events` topic. Treat `seq` as the correlation primitive and accept whichever envelope the device actually publishes.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — only source. |
