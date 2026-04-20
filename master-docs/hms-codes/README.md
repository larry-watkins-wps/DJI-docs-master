# HMS codes

Catalog of DJI Health Management System (HMS) alarm codes, drawn verbatim from [`DJI_Cloud/HMS.json`](../../DJI_Cloud/HMS.json). **1769 codes total** across 14 first-byte prefix buckets plus 1 non-conforming outlier(s).

## How HMS codes reach the cloud

The dock (or RC, via pilot-to-cloud) publishes an `hms` event on `thing/product/{gateway_sn}/events` whenever the aircraft raises a health warning. Each event carries `data.list[].code` (an alarm ID string), `level` (0 = Notification, 1 = Reminder, 2 = Warning), `module` (the event-source module, **not** the alarm-ID prefix), plus `component_index` / `sensor_index` that fill `%component_index` / `%index` placeholders in the tip text.

See [`mqtt/dock-to-cloud/events/hms.md`](../mqtt/dock-to-cloud/events/hms.md) for the full event envelope and payload definition.

## Cloud implementation workflow

1. Subscribe to `thing/product/{gateway_sn}/events`.
2. Filter messages where `method == "hms"`.
3. For each entry in `data.list[]`, look up `code` in [`HMS.json`](../../DJI_Cloud/HMS.json) to obtain the `tipEn` template.
4. Substitute placeholders: `%alarmid` → the raw `code` value; `%component_index` and `%index` → the `args.component_index` / `args.sensor_index` from the event payload.
5. Correlate with `level`, `imminent`, and `in_the_sky` flags for UI severity handling.

## Catalog — one file per first-byte prefix

| Prefix | Domain (inferred) | Codes | File |
|---|---|---|---|
| `0x11` | Payload (general) | 45 | [`0x11-payload-general.md`](0x11-payload-general.md) |
| `0x12` | Battery Station | 37 | [`0x12-battery-station.md`](0x12-battery-station.md) |
| `0x14` | Payload IMU | 52 | [`0x14-payload-imu.md`](0x14-payload-imu.md) |
| `0x15` | mmWave Radar | 39 | [`0x15-mmwave-radar.md`](0x15-mmwave-radar.md) |
| `0x16` | Flight-control system | 921 | [`0x16-flight-control.md`](0x16-flight-control.md) |
| `0x17` | Image transmission & RC link | 16 | [`0x17-transmission.md`](0x17-transmission.md) |
| `0x19` | System overload (CPU / memory / network) | 52 | [`0x19-system-overload.md`](0x19-system-overload.md) |
| `0x1A` | Vision sensors | 170 | [`0x1A-vision-sensors.md`](0x1A-vision-sensors.md) |
| `0x1B` | Navigation & Target Acquisition | 138 | [`0x1B-navigation-tracking.md`](0x1B-navigation-tracking.md) |
| `0x1C` | Camera | 167 | [`0x1C-camera.md`](0x1C-camera.md) |
| `0x1D` | Gimbal | 45 | [`0x1D-gimbal.md`](0x1D-gimbal.md) |
| `0x1E` | PSDK / third-party payload (searchlight, speaker, etc.) | 28 | [`0x1E-psdk-payload.md`](0x1E-psdk-payload.md) |
| `0x1F` | LTE / Cellular | 56 | [`0x1F-cellular-lte.md`](0x1F-cellular-lte.md) |
| `0x20` | Takeoff tags | 2 | [`0x20-takeoff-tags.md`](0x20-takeoff-tags.md) |
| — | Outliers (non-hex / uppercase-X) | 1 | [`outliers.md`](outliers.md) |
| **Total** | | **1769** | |

**531** entries have CJK-ideograph content in the source `tipEn` field — a DJI source defect where Chinese-language developer-debug strings were leaked under the "English" copy key. These rows display a curated EN translation marked with a trailing **+** and retain the CN original in a collapsible `CN source` block under each subsection.

## Source defects preserved

- `unknown` — a single non-hex entry with tip `"Contact your local dealer or DJI Support"`. Filed under [`outliers.md`](outliers.md).
- `0X1B033001` — uppercase-`X` casing (all other IDs use lowercase `0x`). Included under prefix `0x1B`.
- Full-width Chinese parentheses `（ ）` appear in 167 tips where the content is otherwise English — normalized to ASCII `( )` in this catalog.
- 0x16 takes **~52%** of all HMS codes (921/1,769) because DJI's flight-control system is the largest source of health events. That file is sub-sectioned by second byte for navigability.

## Sources

- Primary — [`DJI_Cloud/HMS.json`](../../DJI_Cloud/HMS.json) (DJI v1.15 authoritative).
- Event envelope — [`DJI_Cloud/DJI_CloudAPI-Dock3-HMS.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock3-HMS.txt), [`DJI_Cloud/DJI_CloudAPI-Dock2-HMS.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock2-HMS.txt).
- Per-phase event doc — [`mqtt/dock-to-cloud/events/hms.md`](../mqtt/dock-to-cloud/events/hms.md).
