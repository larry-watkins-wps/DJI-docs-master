# `hsi_info_push` — DRC obstacle-avoidance information

Device → cloud push on the DRC uplink reporting the aircraft's obstacle-sensing state — upward / downward distances, sensor-enable flags, and a 360-point horizontal ring of distances.

Push cadence follows the `hsi_frequency` passed to [`drc_mode_enter`](../services/drc_mode_enter.md) (range `1`–`30` Hz).

Part of the Phase 4 MQTT catalog. Shared conventions (DRC envelope) live in [`../../README.md` §5.8](../../README.md#58-drcup--drcdown--direct-remote-control).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `hsi_info_push` |

## Up — `data` fields (schema table)

| Field | Type | Description |
|---|---|---|
| `up_distance` | int (mm) | Distance of the nearest upward obstacle. |
| `down_distance` | int (mm) | Distance of the nearest downward obstacle. |
| `up_enable` | bool | Upward obstacle-sensing switch state. |
| `up_work` | bool | Upward obstacle-sensing working state. |
| `down_enable` | bool | Downward obstacle-sensing switch state. |
| `down_work` | bool | Downward obstacle-sensing working state. |
| `around_distances` | array of int (mm, size 360) | Horizontal ring of distances, one entry per degree `[0, 360)`, clockwise. Index `0` = aircraft heading; index `90` = right side. |

### Example

```json
{
  "method": "hsi_info_push",
  "timestamp": 1670415891013,
  "data": {
    "up_distance": 10,
    "down_distance": 10,
    "around_distance": [
      10,
      8,
      9,
      16,
      2
    ],
    "up_enable": true,
    "up_work": true,
    "down_enable": true,
    "down_work": true,
    "left_enable": true,
    "left_work": true,
    "right_enable": true,
    "right_work": true,
    "front_enable": true,
    "front_work": true,
    "back_enable": true,
    "back_work": true,
    "vertical_enable": true,
    "vertical_work": true,
    "horizontal_enable": true,
    "horizontal_work": true
  }
}
```

> **Source inconsistencies flagged by DJI's own example.** The example diverges from the schema table in two ways, both preserved verbatim above:
>
> 1. The table names the surrounding-distance array `around_distances` (plural); the example uses `around_distance` (singular). Treat the plural (`around_distances`) as the schema name; the singular is a DJI typo in the example.
> 2. The example includes **eight additional boolean pairs** (`left_enable` / `left_work`, `right_*`, `front_*`, `back_*`, `vertical_*`, `horizontal_*`) that are not present in the schema table. These appear to be finer-grained per-direction sensing flags, but their formal status is undocumented. When a wire-level decision depends on these fields, flag the gap — don't guess their semantics.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
