# `stick_control` — DRC stick control

Low-latency DRC command that drives the aircraft and gimbal attitude with virtual-RC-stick values. Issued on the DRC downlink after the DRC link is open (see [`drc_mode_enter`](../services/drc_mode_enter.md)).

**Protocol rules (verbatim from DJI):** "The sending frequency must be maintained at 5–10 Hz to ensure precise control of aircraft movements. **This protocol has no acknowledgment mechanism.**" — i.e. there is no `stick_control` on `drc/up`.

Part of the Phase 4 MQTT catalog. Shared conventions (DRC envelope shape — lighter than thing-model topics, no `tid` / `bid` / `timestamp`, `seq` + `method` + `data`) live in [`../../README.md` §5.8](../../README.md#58-drcup--drcdown--direct-remote-control).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `stick_control` |

## Down — `data` fields

All four stick channels are integers in the range `[364, 1684]` (RC raw ticks, span ±660 around neutral `1024`).

| Field | Type | Description |
|---|---|---|
| `roll` | int | A-channel (Aileron). Range `364`–`1684`, `1024` = neutral. Higher = right tilt, lower = left tilt. |
| `pitch` | int | E-channel (Elevator). Range `364`–`1684`, `1024` = neutral. Higher = forward dive, lower = backward tilt. |
| `throttle` | int | T-channel (Throttle). Range `364`–`1684`, `1024` = hover. Higher = ascend, lower = descend. |
| `yaw` | int | R-channel (Rudder). Range `364`–`1684`, `1024` = neutral. Higher = clockwise rotation, lower = counter-clockwise. |

### Example

```json
{
  "seq": 1,
  "method": "stick_control",
  "data": {
    "roll": 1024,
    "pitch": 1024,
    "throttle": 1024,
    "yaw": 1024,
    "gimbal_pitch": 1024
  }
}
```

> DJI's v1.15 example includes a `gimbal_pitch` key that is **not listed in the schema table**. Treat this as a DJI documentation inconsistency: the four channels above are authoritatively typed; `gimbal_pitch` appears to be a gimbal-axis additive on the same message, but its range/behavior is undocumented. When a wire-level decision hangs on this field, do not guess — flag it and cross-reference a packet capture.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
