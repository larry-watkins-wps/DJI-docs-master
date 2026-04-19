# `drc_interval_photo_set` — set timed-shot interval (Dock 2 legacy)

DRC command that sets the capture interval for timed-shot mode on Dock 2 aircraft. Allowed values depend on photo size — at 8K photo size, 0.7s and 1s intervals are unsupported. On Dock 3 this appears to be handled via an OSD property setter rather than a dedicated method.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 only**.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_interval_photo_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_interval_photo_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration. |
| `interval` | enum string | Interval keys: `"0.7"` (0.7 s), `"1"`, `"2"`, `"3"`, `"5"`, `"7"`, `"10"`, `"15"`, `"20"`, `"30"`, `"60"` — all declared as strings because `"0.7"` is not integer-expressible. |

### Example

```json
{
  "data": {
    "interval": 1,
    "payload_index": "80-0-0"
  },
  "method": "drc_interval_photo_set",
  "seq": 1
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

## Source inconsistencies flagged by DJI's own example

- **`interval` declared `enum_string` (string keys) but example sends integer `1`.** Mixed-type declaration. For the `"0.7"` value the wire type must be string; for integer-expressible values DJI's own example accepts integer. A conservative server-side implementation should accept either type.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/180.remote-control.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Control.txt]` | v1.15 (Dock 2) — identical. |
