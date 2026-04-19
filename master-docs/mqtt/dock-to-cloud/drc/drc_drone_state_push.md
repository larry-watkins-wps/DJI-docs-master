# `drc_drone_state_push` — aircraft state push

Event pushed by the aircraft reporting current flight-mode code and beacon / stealth light state. Emitted on meaningful state change.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** with **topic and payload divergence** — see [Source differences](#source-differences). On Dock 2 the method also returns `landing_type` and `landing_protection_type`; on Dock 3 those fields are dropped. The topic changes between cohorts too.

---

## Topics

| Direction | Cohort | Topic | Method |
|---|---|---|---|
| Device → Cloud | **Dock 3 v1.15** | `thing/product/{gateway_sn}/events` | `drc_drone_state_push` |
| Device → Cloud | **Dock 2 v1.15 + v1.11** | `thing/product/{gateway_sn}/drc/up` | `drc_drone_state_push` |

**Same method name, different topic on different cohorts.** Dock 3 demotes the state push from the low-latency DRC channel to the standard events channel — DJI does not explain the change. A server that supports both cohorts needs to subscribe to both topics.

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `stealth_state` | bool (0/1) | Discreet / stealth mode state — `0` disabled, `1` enabled. |
| `night_lights_state` | bool (0/1) | Beacon (night-flight) lights — `0` disabled, `1` enabled. |
| `mode_code` | enum int | Aircraft state. `0` = Standby, `1` = Takeoff preparation, `2` = Takeoff preparation completed, `3` = Manual flight, `4` = Automatic takeoff, `5` = Wayline flight, `6` = Panorama, `7` = Intelligent tracking, `8` = ADS-B avoidance, `9` = Auto RTH, `10` = Auto landing, `11` = Forced landing, `12` = Three-blade landing, `13` = Upgrading, `14` = Not connected, `15` = APAS, `16` = Virtual stick, `17` = Live flight Controls. |
| `landing_type` | enum int | **Dock 2 only**. `0` = Not landed, `1` = Landing within dock, `2` = Landing at alternate site, `3` = Landing triggered by users, `4` = Landing triggered by aircraft. |
| `landing_protection_type` | enum int | **Dock 2 only**. `0` = Detection not opened, `1` = Detecting uneven ground or water — landing task exited, `2` = No ground-detecting result — landing task exited, `3` = Detection for landing within dock. Only emitted when obstacle sensing is enabled. |

### Example (Dock 3)

```json
{
  "data": {
    "mode_code": 0,
    "night_lights_state": 0,
    "stealth_state": 0
  },
  "method": "drc_drone_state_push",
  "seq": 1
}
```

### Example (Dock 2)

```json
{
  "data": {
    "landing_protection_type": 0,
    "landing_type": 1,
    "mode_code": 0,
    "night_lights_state": 0,
    "stealth_state": 0
  },
  "method": "drc_drone_state_push",
  "seq": 1
}
```

## Source differences

- **Topic family diverges.** Dock 2 + v1.11 use `/drc/up`; Dock 3 uses `/events`. A cloud supporting both must subscribe to both.
- **Dock 3 drops `landing_type` and `landing_protection_type`.** Those fields are likely exposed via OSD properties (Phase 6) or a different push method on Dock 3. The `mode_code` enum is unchanged.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/180.remote-control.md]` | v1.11 canonical (Dock 2) — `/drc/up`, includes landing fields. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Control.txt]` | v1.15 (Dock 2) — same shape as v1.11. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — topic is `/events`, landing fields removed. |
