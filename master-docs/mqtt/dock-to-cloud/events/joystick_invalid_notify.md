# `joystick_invalid_notify` — DRC flight-control invalidity reason notification

Event pushed by the dock when DRC flight control becomes unavailable — i.e., when [`drone_control`](../drc/drone_control.md) / [`stick_control`](../drc/stick_control.md) commands can no longer drive the aircraft manually. Reports the reason (RC link loss, low-battery return/land, flight-restriction proximity, RC takeover). Requires reply (`need_reply: 1`).

> DJI's description: "The DRC - flight control is an integrated control feature for the aircraft. If it is unavailable, the drone_control capability cannot be used for manual operation."

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, request-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `joystick_invalid_notify` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `joystick_invalid_notify` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `reason` | enum int | Reason flight control became invalid. See **reason enum** below. |

### `reason` enum

| Value | Meaning |
|---|---|
| `0` | Remote controller lost connection. |
| `1` | Low battery return. |
| `2` | Low battery landing. |
| `3` | Close to the flight restriction zone. |
| `4` | Remote controller takeover control authority (for example, triggered return, B control takeover). |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "reason": 0
  },
  "need_reply": 1,
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "joystick_invalid_notify"
}
```

## Down (reply) — `data` fields

Standard events_reply envelope: `data.result` (integer; `0` = success).

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2) — titled "Notification of joystick control invalidity reasons"; v1.15 retitles to "Notification of DRC - flight control invalidity reasons". Fields identical. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
