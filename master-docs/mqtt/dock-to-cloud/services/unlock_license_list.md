# `unlock_license_list` — list the unlocking licenses loaded on the device

Cloud command that asks the dock (or the aircraft, via the dock) to enumerate every FlySafe unlocking license it currently holds. The reply carries a license array keyed by `type` — one of seven unlock flavors (authorization zone, custom circular area, country/region, altitude limit, custom polygon area, power, RID) — plus a `consistence` flag indicating whether the device-side licenses match the server-side approved set.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `unlock_license_list` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `unlock_license_list` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `device_model_domain` | enum int | Where to query. `0` = Aircraft (already-imported licenses on the aircraft); `3` = Dock (licenses approved for the dock on the FlySafe website). |

### Example (down)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "device_model_domain": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero represents an error. |
| `device_model_domain` | enum int | Echoes the domain from the command (`0` = Aircraft, `3` = Dock). |
| `consistence` | boolean | `true` = device-side licenses match the server-approved set; `false` = a sync is needed (either an online refresh or a [`unlock_license_update`](unlock_license_update.md)). |
| `licenses` | array&lt;struct&gt; | One entry per license. Each entry carries `common_fields` plus exactly one unlock-type sub-struct chosen by `common_fields.type`. |

### `licenses[].common_fields`

| Field | Type | Description |
|---|---|---|
| `license_id` | integer | Unique identifier of the license. Target of [`unlock_license_switch`](unlock_license_switch.md). |
| `name` | string | Display name. |
| `type` | enum int | `0` = Authorization zone, `1` = Custom circular area, `2` = Country/region, `3` = Altitude limit, `4` = Custom polygon area, `5` = Power, `6` = RID. Selects which unlock-type sub-struct is populated below. |
| `group_id` | integer | All licenses applied by one account for one device belong to the same group. |
| `user_id` | string | Account (DJI user ID or dock SN) to which the license belongs. |
| `device_sn` | string | Device serial number bound to the license. |
| `begin_time` | integer | Validity start — **second-level** UNIX timestamp. |
| `end_time` | integer | Validity end — **second-level** UNIX timestamp. |
| `user_only` | boolean | `true` = the license is valid only when the specified user account is logged in. |
| `enabled` | boolean | Mirrors the last `unlock_license_switch.enable` state. |

### Unlock-type sub-structs

Populated by `type`; exactly one sibling of `common_fields` per license.

| Sub-struct | Populated when | Fields |
|---|---|---|
| `area_unlock` | `type = 0` | `area_ids[]` — array of area IDs (integers). |
| `circle_unlock` | `type = 1` | `radius` (m), `latitude`, `longitude`, `height` (m, max `65535`). |
| `country_unlock` | `type = 2` | `country_number` (ISO-3166-1 numeric, e.g., `156` = China), `height` (m). |
| `height_unlock` | `type = 3` | `height` (m, max `65535`). |
| `polygon_unlock` | `type = 4` | `points[]` — each `{latitude, longitude}`. |
| `power_unlock` | `type = 5` | Empty object. |
| `rid_unlock` | `type = 6` | `level` — `1` = EU RID, `2` = China RID. |

### Example (reply — one of each type)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "consistence": false,
    "device_model_domain": 0,
    "licenses": [
      {
        "area_unlock": {
          "area_ids": [115001769, 8724]
        },
        "common_fields": {
          "begin_time": 1696948115,
          "device_sn": "xxxxxxxxx",
          "enabled": true,
          "end_time": 2145916800,
          "group_id": 2896,
          "license_id": 240330,
          "name": "Unlocking for XXX Area",
          "type": 0,
          "user_id": "xxxxxxxxx",
          "user_only": false
        }
      },
      {
        "circle_unlock": {
          "height": 500,
          "latitude": 22.60309,
          "longitude": 113.947815,
          "radius": 1581
        },
        "common_fields": {
          "begin_time": 1696948115,
          "device_sn": "xxxxxxxxx",
          "enabled": false,
          "end_time": 2145916800,
          "group_id": 2896,
          "license_id": 240331,
          "name": "Unlocking for XXX Circular Area",
          "type": 1,
          "user_id": "xxxxxxxxx",
          "user_only": false
        }
      },
      {
        "common_fields": {
          "begin_time": 1696948115,
          "device_sn": "xxxxxxxxx",
          "enabled": false,
          "end_time": 2145916800,
          "group_id": 2896,
          "license_id": 240332,
          "name": "Unlocking for China Country/Region",
          "type": 2,
          "user_id": "xxxxxxxxx",
          "user_only": false
        },
        "country_unlock": {
          "country_number": 156,
          "height": 500
        }
      },
      {
        "common_fields": {
          "begin_time": 1696948115,
          "device_sn": "xxxxxxxxx",
          "enabled": false,
          "end_time": 2145916800,
          "group_id": 2896,
          "license_id": 240333,
          "name": "Unlocking for XXX Altitude",
          "type": 3,
          "user_id": "xxxxxxxxx",
          "user_only": false
        },
        "height_unlock": {
          "height": 500
        }
      },
      {
        "common_fields": {
          "begin_time": 1696948115,
          "device_sn": "xxxxxxxxx",
          "enabled": false,
          "end_time": 2145916800,
          "group_id": 2896,
          "license_id": 240334,
          "name": "Unlocking for XXX Polygon Area",
          "type": 4,
          "user_id": "xxxxxxxxx",
          "user_only": false
        },
        "polygon_unlock": {
          "points": [
            {"latitude": 22.55403932, "longitude": 113.90488828},
            {"latitude": 22.55520018, "longitude": 113.92180215},
            {"latitude": 22.54656858, "longitude": 113.92051272}
          ]
        }
      },
      {
        "common_fields": {
          "begin_time": 1696948115,
          "device_sn": "xxxxxxxxx",
          "enabled": false,
          "end_time": 2145916800,
          "group_id": 2896,
          "license_id": 240335,
          "name": "Unlocking for XXX Power",
          "type": 5,
          "user_id": "xxxxxxxxx",
          "user_only": false
        },
        "power_unlock": {}
      },
      {
        "common_fields": {
          "begin_time": 1696948115,
          "device_sn": "xxxxxxxxx",
          "enabled": false,
          "end_time": 2145916800,
          "group_id": 2896,
          "license_id": 240336,
          "name": "Unlocking for XXX RID",
          "type": 6,
          "user_id": "xxxxxxxxx",
          "user_only": false
        },
        "rid_unlock": {
          "level": 1
        }
      }
    ],
    "result": 0
  },
  "gateway": "",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655
}
```

## Relationship to other methods

- Toggle an individual license with [`unlock_license_switch`](unlock_license_switch.md).
- Push a refreshed license file with [`unlock_license_update`](unlock_license_update.md).
- `consistence = false` is the cloud's signal that the device needs either an online resync (empty [`unlock_license_update`](unlock_license_update.md)) or an offline file push (populated [`unlock_license_update`](unlock_license_update.md)).
- Full FlySafe choreography will be documented in Phase 9 workflow `workflows/flysafe-custom-flight-area-sync.md`.

## Source differences

- **`type` enum label casing.** v1.11 Dock 2 and v1.15 Dock 2 label the unlock types in lowercase-running-text form (e.g., `"0":"Authorization zone unlocking"`); v1.15 Dock 3 (hand-authored) uses title-case with past-tense (e.g., `"0":"Authorization Zone Unlocked"`). Numeric values are stable across all three sources — only the human-readable labels differ.
- **`rid_unlock.level` label casing.** Same pattern: `"EU RID unlocking"` vs `"EU RID Unlocked"`. Numeric `{1, 2}` is stable.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/170.flysafe.md]` | v1.11 canonical (Dock 2) — fully typed table. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-FlySafe.txt]` | v1.15 (Dock 2) — structurally identical. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-FlySafe.txt]` | v1.15 (Dock 3, hand-authored) — structurally identical; enum labels re-phrased. |
