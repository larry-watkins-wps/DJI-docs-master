# `camera_focus_value_set` — set manual-focus value

Cloud command that sets the manual-focus value on a specific camera lens. Valid range is device-dependent — fetch `zoom_max_focus_value` and `zoom_min_focus_value` from the aircraft properties (Phase 6) to determine the range.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `camera_focus_value_set` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `camera_focus_value_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration (`{type}-{subtype}-{gimbalindex}`). |
| `camera_type` | enum string | Lens. `wide` = wide-angle, `zoom` = zoom. Note: on Matrice 30 series (out of scope here) this parameter is only settable on the zoom lens. |
| `focus_value` | integer | Focus value. Range bounded by the aircraft's `zoom_max_focus_value` and `zoom_min_focus_value` properties. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "camera_type": "zoom",
    "focus_value": 5,
    "payload_index": "39-0-7"
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "camera_focus_value_set"
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero represents an error. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": { "result": 0 },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "camera_focus_value_set"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
