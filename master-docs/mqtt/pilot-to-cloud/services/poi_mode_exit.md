# `poi_mode_exit` — exit POI mode

Cloud command that ends POI (Point of Interest) circle mode and returns the aircraft to normal hover / manual flight. A terminal [`poi_status_notify`](../events/poi_status_notify.md) with `status: "ok"` and `reason: 160` (Normal exit) is expected after the aircraft stops circling.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.** Not present on RC Pro. No v1.11 counterpart.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `poi_mode_exit` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `poi_mode_exit` |

## Down — `data` fields

`null` — no payload fields required. Envelope `data` is an empty object.

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {},
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "poi_mode_exit"
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero = error. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "result": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "poi_mode_exit"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Flight-Controls.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |
