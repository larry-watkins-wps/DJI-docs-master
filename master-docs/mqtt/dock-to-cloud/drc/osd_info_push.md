# `osd_info_push` — DRC high-frequency OSD

Device → cloud push on the DRC uplink carrying a compact high-frequency OSD frame for live teleoperation UI — attitude heading, lat/lon/altitude, 3-axis velocities, and gimbal attitude.

Push cadence follows the `osd_frequency` passed to [`drc_mode_enter`](../services/drc_mode_enter.md) (range `1`–`30` Hz).

Part of the Phase 4 MQTT catalog. Shared conventions (DRC envelope) live in [`../../README.md` §5.8](../../README.md#58-drcup--drcdown--direct-remote-control).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `osd_info_push` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `attitude_head` | double (degrees) | Flight-attitude heading. |
| `latitude` | double (degrees) | Flight latitude. |
| `longitude` | double (degrees) | Flight longitude. |
| `height` | double (m) | Flight altitude. *(DJI source labels this field's unit as `degree` — this is a DJI typo; the field is an altitude in meters.)* |
| `speed_x` | double (m/s) | Aircraft velocity, X axis. |
| `speed_y` | double (m/s) | Aircraft velocity, Y axis. |
| `speed_z` | double (m/s) | Aircraft velocity, Z axis. |
| `gimbal_pitch` | double (degrees) | Gimbal pitch angle. |
| `gimbal_roll` | double (degrees) | Gimbal roll angle. |
| `gimbal_yaw` | double (degrees) | Gimbal yaw angle. |

### Example

```json
{
  "method": "osd_info_push",
  "timestamp": 1670415891013,
  "data": {
    "attitude_head": 60,
    "latitude": 10,
    "longitude": 10,
    "height": 10,
    "speed_x": 10,
    "speed_y": 10,
    "speed_z": 10,
    "gimbal_pitch": 60,
    "gimbal_roll": 60,
    "gimbal_yaw": 60
  }
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
