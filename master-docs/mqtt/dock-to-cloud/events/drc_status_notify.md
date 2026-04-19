# `drc_status_notify` — DRC link state notification *(abandoned)*

Event formerly pushed by the dock to report the state of the DRC (direct remote control) link. **Abandoned in v1.15** — DJI's v1.15 documentation explicitly states "This protocol is no longer maintained and may be inaccurate." For a current DRC link signal, use either the `drc_state` device property (reported by the dock) or the [`heart_beat`](../drc/heart_beat.md) DRC-channel ping. Retained in the catalog for protocol archaeology and backwards-compatibility auditing. Requires reply (`need_reply: 1`).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, request-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload. Flagged abandoned in v1.15 for both cohorts; v1.11 documents it as active.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `drc_status_notify` |
| Cloud → Device | `thing/product/{gateway_sn}/events_reply` | `drc_status_notify` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. Non-zero = error. |
| `drc_state` | enum int | Live flight controls state. `0` = Not connected. `1` = Connecting. `2` = Connected. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "drc_state": 2,
    "result": 0
  },
  "need_reply": 1,
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "drc_status_notify"
}
```

## Down (reply) — `data` fields

Standard events_reply envelope: `data.result` (integer; `0` = success).

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2) — documents the method as active. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2) — flags method as abandoned. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — flags method as abandoned, same payload as Dock 2 v1.15. |
