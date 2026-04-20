# HMS codes — 0x14** (Payload IMU)

Prefix byte `0x14`. 52 alarm codes.

The prefix byte is the wire-level grouping DJI uses in the `data.list[].code` field emitted on [`thing/product/{gateway_sn}/events` method `hms`](../mqtt/dock-to-cloud/events/hms.md). The domain label above is inferred from the tip text — DJI does not publish an official prefix taxonomy.

Entries rendered with a trailing **+** have a curated CN→EN translation because the original `tipEn` value in [`HMS.json`](../../DJI_Cloud/HMS.json) contains Chinese-language developer-debug strings under the "English" field. The CN originals are preserved below each subsection in a `CN source` callout so the audit trail is intact.

| Alarm ID | Tip |
|---|---|
| `0x14010031` | Payload infusion data error (%alarmid). Restart payload |
| `0x14010032` | Unable to converge payload infusion data (%alarmid). Execute mapping task after the warning disappears. If the issue persists, restart the payload |
| `0x14010033` | Payload system time error (%alarmid). Restart aircraft |
| `0x14010034` | Payload tachometer data invalid (%alarmid). Restart payload |
| `0x14010035` | Payload tachometer data not updated (%alarmid). Restart payload |
| `0x14010036` | No payload tachometer data (%alarmid). Restart payload |
| `0x14010037` | Payload tachometer data exceeds limit (%alarmid). Restart payload |
| `0x14010038` | Payload tachometer data error (%alarmid). Execute mapping task after the warning disappears. If the warning persists, restart the payload |
| `0x14010039` | Payload accelerometer data invalid (%alarmid). Restart payload |
| `0x1401003A` | Payload accelerometer data not updated (%alarmid). Restart payload |
| `0x1401003B` | No payload accelerometer data (%alarmid). Restart payload |
| `0x1401003C` | Payload accelerometer data exceeds limit (%alarmid). Restart payload |
| `0x1401003D` | Payload accelerometer data error (%alarmid). Execute mapping task after the warning disappears. If the issue persists, restart the payload |
| `0x1401003E` | Payload RTK data calculation error (%alarmid). Restart aircraft |
| `0x1401003F` | Payload direction data error (%alarmid). Check satellite signal. Contact DJI Support if error occurs repeatedly |
| `0x14010040` | Payload RTK data error (%alarmid). Restart aircraft |
| `0x14010041` | Payload RTK time error (%alarmid). Restart aircraft |
| `0x14010042` | Payload RTK data invalid (%alarmid). Restart aircraft |
| `0x14010043` | Payload IMU warming up. Wait until IMU finished warming up to continue (%alarmid) |
| `0x14010044` | Payload IMU temperature control processor error (%alarmid). Restart payload |
| `0x14010045` | Payload IMU overheated (%alarmid). Restart payload |
| `0x14010046` | Payload IMU temperature too low (%alarmid). Restart payload |
| `0x14010047` | Payload processor overheated (%alarmid). Return to home or land promptly. Wait for payload to cool down and then restart payload before use |
| `0x14010048` | Payload fan error (%alarmid). Return to home or land. Check whether the fan is stalled |
| `0x14010049` | Payload PPS data error (%alarmid). Check GNSS or RTK signal and gimbal connection port |
| `0x1401004A` | Payload UTC time error (%alarmid). Check GNSS or RTK signal |
| `0x14020031` | Payload infusion data error (%alarmid). Restart payload |
| `0x14020032` | Unable to converge payload infusion data (%alarmid). Execute mapping task after the warning disappears. If the issue persists, restart the payload |
| `0x14020033` | Payload system time error (%alarmid). Restart aircraft |
| `0x14020034` | Payload tachometer data invalid (%alarmid). Restart payload |
| `0x14020035` | Payload tachometer data not updated (%alarmid). Restart payload |
| `0x14020036` | No payload tachometer data (%alarmid). Restart payload |
| `0x14020037` | Payload tachometer data exceeds limit (%alarmid). Restart payload |
| `0x14020038` | Payload tachometer data error (%alarmid). Execute mapping task after the warning disappears. If the warning persists, restart the payload |
| `0x14020039` | Payload accelerometer data invalid (%alarmid). Restart payload |
| `0x1402003A` | Payload accelerometer data not updated (%alarmid). Restart payload |
| `0x1402003B` | No payload accelerometer data (%alarmid). Restart payload |
| `0x1402003C` | Payload accelerometer data exceeds limit (%alarmid). Restart payload |
| `0x1402003D` | Payload accelerometer data error (%alarmid). Execute mapping task after the warning disappears. If the issue persists, restart the payload |
| `0x1402003E` | Payload RTK data calculation error (%alarmid). Restart aircraft |
| `0x14020040` | Payload RTK data error (%alarmid). Restart aircraft |
| `0x14020041` | Payload RTK time error (%alarmid). Restart aircraft |
| `0x14020042` | Payload RTK data invalid (%alarmid). Restart aircraft |
| `0x14030002` | Rotation speed error of LiDAR scanning module (%alarmid). Restart aircraft |
| `0x14030003` | Rotation speed error of LiDAR scanning module (%alarmid). Restart aircraft |
| `0x1403000B` | Calibrating LiDAR scanning module (%alarmid). Do not move aircraft. Wait until calibration is completed |
| `0x14060000` | NIR Illumination power error and disabled. Re-enable this function or contact DJI Support (%alarmid) |
| `0x14810040` | LiDAR temperature too high/low (%alarmid). Return to home or land promptly. Wait for LiDAR temperature to return to normal and then restart the payload |
| `0x14810080` | LiDAR voltage too high/low (%alarmid). Return to home or land promptly. Restart payload |
| `0x148100C0` | LiDAR motor error (%alarmid). Return to home or land promptly and restart payload |
| `0x14810100` | LiDAR lifecycle warning (%alarmid). Restart payload |
| `0x14810140` | LiDAR system error (%alarmid). Return to home or land promptly and restart payload |

---

**Source**: [`DJI_Cloud/HMS.json`](../../DJI_Cloud/HMS.json) (DJI v1.15 authoritative).

**See also**: 
- Event definition — [`mqtt/dock-to-cloud/events/hms.md`](../mqtt/dock-to-cloud/events/hms.md).
- Topic-level overview — [`mqtt/README.md`](../mqtt/README.md).
- General API error codes (distinct from HMS alarms) — [`error-codes/README.md`](../error-codes/README.md).
