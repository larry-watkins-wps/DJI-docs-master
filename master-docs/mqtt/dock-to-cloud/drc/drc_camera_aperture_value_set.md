# `drc_camera_aperture_value_set` — set camera aperture

DRC command that sets the aperture value on the selected lens (wide or zoom). Enum is an integer with key equal to the aperture × 100 (e.g. `200` = F2.0, `280` = F2.8, `560` = F5.6).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — payload shape identical; enum value-label syntax diverges (dots vs underscores) — see [Source differences](#source-differences).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_camera_aperture_value_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_camera_aperture_value_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration value. Format `{type-subtype-gimbalindex}`. |
| `camera_type` | enum string | `wide` = Wide-angle; `zoom` = Zoom. |
| `aperture_value` | enum int | Aperture value. `0` = F_AUTO. Non-zero keys are the F-stop × 100 (e.g. `200` = F2.0, `280` = F2.8). Full enum lists keys `50, 70, 80, 90, 95, 100, 110, 120, 140, 160, 170, 180, 200, 220, 240, 250, 280, 320, 330, 340, 350, 400, 440, 450, 480, 500, 560, 630, 670, 680, 710, 800, 900, 950, 960, 1000, 1100, 1300, 1400, 1600, 1800, 1900, 2000, 2200, 2500, 2700, 2900, 3200, 3600, 3800, 4000, 4500, 5100, 5400, 5700, 6400, 7200, 7600, 8000, 9000, 10700, 12800, 18000, 25600`. Depending on the aircraft model, the supported range varies. |

### Example

```json
{
  "data": {
    "aperture_value": 5,
    "camera_type": "zoom",
    "payload_index": "39-0-7"
  },
  "method": "drc_camera_aperture_value_set",
  "seq": 1
}
```

(DJI's example sends `aperture_value: 5`, which is not a value in the documented enum. Treat the documented enum as authoritative; the example's `5` appears to be a placeholder rather than a valid aperture key.)

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

### Example

```json
{
  "data": {
    "result": 0
  },
  "method": "drc_camera_aperture_value_set",
  "seq": 1
}
```

## Source differences

- **Enum label syntax**: Dock 2 + v1.11 use dots (`"200":"F2"`, `"220":"F2.2"`, `"280":"F2.8"`). Dock 3 uses underscores (`"200":"F2"`, `"220":"F2_2"`, `"280":"F2_8"`). The integer keys (`220`) are stable — only the label format differs.

## Source inconsistencies flagged by DJI's own example

- Example sends `aperture_value: 5` which is not a documented enum key on any cohort. Placeholder.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/180.remote-control.md]` | v1.11 canonical (Dock 2) — dot-label enum. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Control.txt]` | v1.15 (Dock 2) — dot-label enum. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — underscore-label enum. |
