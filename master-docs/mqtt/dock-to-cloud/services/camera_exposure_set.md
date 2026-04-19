# `camera_exposure_set` — set exposure value (EV)

Cloud command that adjusts the exposure compensation (EV) on a specific camera lens. Value is a discrete enumeration over the −5.0 EV to +5.0 EV range in 1/3-stop steps, plus a `FIXED` sentinel.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `camera_exposure_set` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `camera_exposure_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration (`{type}-{subtype}-{gimbalindex}`). |
| `camera_type` | enum string | Lens. `wide` = wide-angle, `zoom` = zoom. |
| `exposure_value` | enum (int key, in example sent as integer) | Discrete EV step. See **exposure_value enum** below. |

### `exposure_value` enum

DJI sources declare this as `enum_string` but the example sends it as an integer (`"exposure_value": 5`). Treat the declared key (integer 1–31, 255) as the wire value; the labels below are the 1/3-stop steps.

| Key | EV |
|---|---|
| `1` | −5.0 |
| `2` | −4.7 |
| `3` | −4.3 |
| `4` | −4.0 |
| `5` | −3.7 |
| `6` | −3.3 |
| `7` | −3.0 |
| `8` | −2.7 |
| `9` | −2.3 |
| `10` | −2.0 |
| `11` | −1.7 |
| `12` | −1.3 |
| `13` | −1.0 |
| `14` | −0.7 |
| `15` | −0.3 |
| `16` | 0 |
| `17` | 0.3 |
| `18` | 0.7 |
| `19` | 1.0 |
| `20` | 1.3 |
| `21` | 1.7 |
| `22` | 2.0 |
| `23` | 2.3 |
| `24` | 2.7 |
| `25` | 3.0 |
| `26` | 3.3 |
| `27` | 3.7 |
| `28` | 4.0 |
| `29` | 4.3 |
| `30` | 4.7 |
| `31` | 5.0 |
| `255` | `FIXED` |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "camera_type": "zoom",
    "exposure_value": 5,
    "payload_index": "39-0-7"
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "camera_exposure_set"
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero represents an error. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": { "result": 0 },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "camera_exposure_set"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
