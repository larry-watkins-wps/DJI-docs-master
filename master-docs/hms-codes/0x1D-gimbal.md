# HMS codes — 0x1D** (Gimbal)

Prefix byte `0x1D`. 45 alarm codes.

The prefix byte is the wire-level grouping DJI uses in the `data.list[].code` field emitted on [`thing/product/{gateway_sn}/events` method `hms`](../mqtt/dock-to-cloud/events/hms.md). The domain label above is inferred from the tip text — DJI does not publish an official prefix taxonomy.

Entries rendered with a trailing **+** have a curated CN→EN translation because the original `tipEn` value in [`HMS.json`](../../DJI_Cloud/HMS.json) contains Chinese-language developer-debug strings under the "English" field. The CN originals are preserved below each subsection in a `CN source` callout so the audit trail is intact.

| Alarm ID | Tip |
|---|---|
| `0x1D001001` | Gimbal unresponsive after power on (%alarmid). Restart gimbal and retry auto check |
| `0x1D001101` | Gimbal unable to complete auto check (%alarmid). Restart gimbal and retry auto check |
| `0x1D010001` | Gimbal stuck. Check and ensure gimbal can rotate freely |
| `0x1D010002` | Gimbal stuck. Check whether gimbal lock is removed and ensure gimbal can rotate freely |
| `0x1D010003` | Gimbal motor overloaded. Check and ensure gimbal can rotate freely |
| `0x1D020001` | Gimbal calibration error. Try gimbal Auto Calibration. If the issue persists, contact DJI Support |
| `0x1D020002` | Gimbal IMU error (%alarmid). Restart aircraft |
| `0x1D030001` | Gimbal unable to retrieve aircraft data. Restart aircraft. If the issue persists, maintenance is required. Contact DJI Support |
| `0x1D030002` | Aircraft-to-payload communication link interrupted (%alarmid). Check the payload connection+ |
| `0x1D040001` | Excessive gimbal vibration. Check whether gimbal can rotate freely. |
| `0x1D040002` | Gimbal gyroscope malfunction. Maintenance required. Contact DJI Support |
| `0x1D040003` | Gimbal roll ESC malfunction. Maintenance required. Contact DJI Support |
| `0x1D040004` | Gimbal pitch ESC malfunction. Maintenance required. Contact DJI Support |
| `0x1D040005` | Gimbal yaw ESC malfunction. Maintenance required. Contact DJI Support |
| `0x1D050004` | Gimbal frozen due to low temperature. Return to dock and try unfreezing gimbal (%alarmid) |
| `0x1D050301` | Gimbal operation retry attempts exceeded limit. Exit Smart Oblique and restart camera. If the issue persists, contact DJI Support |
| `0x1D050302` | Camera exposure error. Exit Smart Oblique and restart camera |
| `0x1D05030F` | Gimbal rotation count approaching max limit. Contact DJI Support for maintenance |
| `0x1D050A01` | Gimbal voltage too low. Restart gimbal |
| `0x1D050A02` | Gimbal time synchronization error. Exit current mission, land, and restart aircraft |
| `0x1D0C0002` | Gimbal IMU error (%alarmid). Restart aircraft. Contact DJI Support if the issue persists |
| `0x1D0C0003` | Gimbal initialization error (%alarmid). Restart aircraft. Contact DJI Support if the issue persists |
| `0x1D0C0004` | Gimbal initialization error (%alarmid). Restart aircraft. Contact DJI Support if the issue persists |
| `0x1D0C000B` | Gimbal motor temperature too high (%alarmid). Check if gimbal can rotate freely. Power off aircraft. Try again after gimbal cools down. Contact DJI Support if the issue persists |
| `0x1D0E0001` | Gimbal initialization error (%alarmid). Restart aircraft. Contact DJI Support if the issue persists |
| `0x1D100002` | Gimbal unresponsive after power on (%alarmid). Restart gimbal and perform auto check |
| `0x1D100006` | Gimbal motors unresponsive after power on (%alarmid). Restart gimbal and perform auto check |
| `0x1D110002` | Gimbal unable to complete auto check (%alarmid). Restart gimbal and retry auto check |
| `0x1D110005` | Gimbal unable to complete auto check (%alarmid). Restart gimbal and retry auto check |
| `0x1D120001` | Gimbal unresponsive or experiencing irregular movement after completing auto check (%alarmid). Restart gimbal and retry auto check |
| `0x1D120002` | Gimbal unresponsive or experiencing irregular movement after completing auto check (%alarmid). Restart gimbal and retry auto check |
| `0x1D120004` | Gimbal unresponsive or experiencing irregular movement after completing auto check (%alarmid). Restart gimbal and retry auto check |
| `0x1D120006` | Gimbal unresponsive or experiencing irregular movement after completing auto check (%alarmid). Restart gimbal and retry auto check |
| `0x1D130003` | Excessive gimbal vibration (%alarmid). Check whether gimbal can rotate freely |
| `0x1D130005` | Excessive gimbal vibration (%alarmid). Check whether gimbal can rotate freely |
| `0x1D13000A` | Excessive gimbal vibration (%alarmid). Check whether gimbal can rotate freely |
| `0x1D140001` | Gimbal motor overloaded (%alarmid). Check whether gimbal can rotate freely |
| `0x1D150002` | Gimble drifting (%alarmid). Try Gimbal Auto Calibration. If the issue persists, contact DJI Support |
| `0x1D150003` | Gimbal drifting (%alarmid). Try Gimbal Auto Calibration. If the issue persists, contact DJI Support |
| `0x1D150004` | Gimbal drifting (%alarmid). Try Gimbal Auto Calibration. If the issue persists, contact DJI Support |
| `0x1D150005` | Gimbal drifting (%alarmid). Try Gimbal Auto Calibration. If the issue persists, contact DJI Support |
| `0x1D160004` | Camera tilted (%alarmid). Try Gimbal Auto Calibration or use Adjust Gimbal. If the issue persists, contact DJI Support |
| `0x1D170001` | Gimbal control error (%alarmid). Restart gimbal. If the issue persists, contact DJI Support |
| `0x1D180001` | Gimbal error (%alarmid). Try Gimbal Auto Calibration. If the issue persists, contact DJI Support |
| `0x1D190002` | Gimbal update failed (%alarmid). Update camera firmware to latest version |

<details><summary>CN source (verbatim from HMS.json)</summary>

| Alarm ID | `tipEn` (original CN) |
|---|---|
| `0x1D030002` | 飞行器与负载通讯链路中断(%alarmid)，请检查负载连接情况 |

</details>

---

**Source**: [`DJI_Cloud/HMS.json`](../../DJI_Cloud/HMS.json) (DJI v1.15 authoritative).

**See also**: 
- Event definition — [`mqtt/dock-to-cloud/events/hms.md`](../mqtt/dock-to-cloud/events/hms.md).
- Topic-level overview — [`mqtt/README.md`](../mqtt/README.md).
- General API error codes (distinct from HMS alarms) — [`error-codes/README.md`](../error-codes/README.md).
