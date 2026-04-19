# `device_exit_homing_notify` — return-to-home exit-state notification

Event pushed by the dock when the aircraft enters or exits the "Return-to-Home Exit" state — i.e., when the return-to-home sequence has been paused or resumed due to one of a documented set of conditions (throttle input, obstacles, flight restrictions, GPS loss, etc.). Requires reply (`need_reply: 1`).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, request-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `device_exit_homing_notify` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `device_exit_homing_notify` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `sn` | string | Dock serial number. |
| `action` | enum int | `0` = exit Return-to-Home Exit state (dock stops exiting the return-to-home process), `1` = enter Return-to-Home Exit state (dock exits the return-to-home process due to the condition in `reason`). |
| `reason` | enum int | See **reason enum** below. |

### `reason` enum

| Value | Meaning |
|---|---|
| `0` | Throttle added to the joystick. |
| `1` | Joystick interval added. |
| `2` | Behavior tree initialization failed. |
| `3` | Surrounded by obstacles. |
| `4` | Triggered flight restriction. |
| `5` | Obstacle too close. |
| `6` | No GPS signal. |
| `7` | GPS and VIO position output flags are false. |
| `8` | Large position error between GPS and VIO fusion. |
| `9` | Short-distance backtracking. |
| `10` | Return triggered at close range. |

> **Note on `reason` type.** DJI's sources list `reason` as `enum_int`, but the example shows the value as a string (`"reason": "0"`). Treat the documented type (integer) as authoritative; the example is a source-level inconsistency.

### Example

```json
{
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "method": "device_exit_homing_notify",
  "timestamp": 1654070968655,
  "need_reply": 1,
  "data": {
    "sn": "Dock SN",
    "action": 1,
    "reason": "0"
  }
}
```

## Down (reply) — `data` fields

Standard events_reply envelope: `data.result` (integer; `0` = success).

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/50.wayline.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Wayline-Management.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-WaylineManagement.txt]` | v1.15 (Dock 3). |
