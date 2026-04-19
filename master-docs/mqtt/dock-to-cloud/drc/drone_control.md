# `drone_control` — DRC flight control *(abandoned)*

Low-latency DRC command that drives the aircraft by 3-axis velocities + yaw rate. **Abandoned in v1.15** — DJI explicitly directs users to [`stick_control`](stick_control.md) instead for better response. Retained in the catalog for protocol archaeology and backwards-compatibility auditing. Sending frequency 5–10 Hz.

Unlike `stick_control`, `drone_control` **has a reply** on `/drc/up` carrying `result` + `output.seq`. Non-zero `result` typically indicates loss of flight-authority, loss of virtual-stick authority, or an out-of-order `seq`.

Part of the Phase 4 MQTT catalog. Shared conventions (DRC envelope) live in [`../../README.md` §5.8](../../README.md#58-drcup--drcdown--direct-remote-control).

**Cohort**: **Dock 2 + Dock 3** — identical payload. Marked abandoned in both cohorts' v1.15 docs.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drone_control` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drone_control` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `seq` | int | Command sequence. Increments across messages; resets to `0` when any of `x`/`y`/`h`/`w` changes. |
| `x` | double (m/s) | Left/right speed. Top-down view with aircraft heading forward: positive = left, negative = right. Range `[-17, 17]`. |
| `y` | double (m/s) | Forward/backward speed. Top-down view with aircraft heading forward: positive = forward, negative = backward. Range `[-17, 17]`. |
| `h` | double (m/s) | Vertical speed. Positive = up, negative = down. DJI's source lists the bounds as `{"min":5,"max":-4}` — the numbers are reversed (a DJI typo); the field is reciprocally a velocity, not a bound. Treat as velocity m/s; consult a packet capture if the exact magnitudes matter. |
| `w` | double (deg/s) | Yaw rate. Positive = clockwise, negative = counter-clockwise. Range `[-90, 90]`. |

### Example

```json
{
  "method": "drone_control",
  "data": {
    "seq": 1,
    "x": 2.34,
    "y": -2.45,
    "h": 2.76,
    "w": 2.86
  }
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. `0` = success; non-zero represents an error. Typical errors: no flight-control authority; no virtual-stick (joystick) authority; wrong `seq`. |
| `output` | struct | Output container. |
| `output.seq` | int | Echoed command sequence. |

### Example

```json
{
  "data": {
    "output": {
      "seq": -1
    },
    "result": 319033
  },
  "method": "drone_control"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2) — flags method abandoned. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — flags method abandoned, same payload as Dock 2 v1.15. |
