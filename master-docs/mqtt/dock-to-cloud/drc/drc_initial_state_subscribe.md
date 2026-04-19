# `drc_initial_state_subscribe` — subscribe to initial DRC state push

DRC command that tells the device to re-push all DRC-relevant state values — camera state, drone state, OSD info, PSDK state — so the cloud can prime its view after entering DRC mode (via [`drc_mode_enter`](../services/drc_mode_enter.md) in 4c). `Data: null`.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_initial_state_subscribe` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_initial_state_subscribe` |

## Down — `data`

`Data: null`. DJI's schema row is a placeholder (`null / null / double`) — the service takes no input.

### Example

```json
{
  "data": {},
  "method": "drc_initial_state_subscribe",
  "seq": 1
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

### Example (Dock 3 — correct)

```json
{
  "data": {
    "result": 0
  },
  "method": "drc_initial_state_subscribe",
  "seq": 1
}
```

## Relationship to other methods

- Typically issued after [`drc_mode_enter`](../services/drc_mode_enter.md) to retrieve an initial state snapshot.
- Triggers re-pushes of [`drc_camera_state_push`](drc_camera_state_push.md), [`drc_drone_state_push`](drc_drone_state_push.md), [`drc_camera_osd_info_push`](drc_camera_osd_info_push.md), [`drc_psdk_state_info`](drc_psdk_state_info.md), and [`drc_ai_info_push`](drc_ai_info_push.md) (where applicable).

## Source inconsistencies flagged by DJI's own example

- **Schema row is placeholder nonsense** (`null / null / double`) across all three sources. The service takes an empty-struct payload — confirmed by the example.
- **Dock 2 v1.11 reply example has the wrong `method` key** — shows `method: drone_emergency_stop` instead of `drc_initial_state_subscribe`. Dock 3 example is correct. Copy-paste error in DJI's source.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/180.remote-control.md]` | v1.11 canonical (Dock 2) — reply example has wrong method name. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Control.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — correct reply example. |
