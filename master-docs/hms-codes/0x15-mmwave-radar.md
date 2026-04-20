# HMS codes — 0x15** (mmWave Radar)

Prefix byte `0x15`. 39 alarm codes.

The prefix byte is the wire-level grouping DJI uses in the `data.list[].code` field emitted on [`thing/product/{gateway_sn}/events` method `hms`](../mqtt/dock-to-cloud/events/hms.md). The domain label above is inferred from the tip text — DJI does not publish an official prefix taxonomy.

Entries rendered with a trailing **+** have a curated CN→EN translation because the original `tipEn` value in [`HMS.json`](../../DJI_Cloud/HMS.json) contains Chinese-language developer-debug strings under the "English" field. The CN originals are preserved below each subsection in a `CN source` callout so the audit trail is intact.

| Alarm ID | Tip |
|---|---|
| `0x15000020` | Make sure ambient temperature is proper for millimeter-wave radar operation (%alarmid). Wait for radar temperature to return to normal before use |
| `0x15000021` | Make sure ambient temperature is proper for millimeter-wave radar operation (%alarmid). Wait for radar temperature to return to normal before use |
| `0x15010020` | Millimeter-wave radar power supply error. Restart radar (%alarmid) |
| `0x15010021` | Millimeter-wave radar power supply error. Restart radar (%alarmid) |
| `0x15010022` | Millimeter-wave radar power supply error. Restart radar (%alarmid) |
| `0x15010023` | Millimeter-wave radar power supply error. Restart radar (%alarmid) |
| `0x15020020` | Millimeter-wave radar motor error. Check whether radar is stalled (%alarmid). If not, restart radar and try again |
| `0x15020021` | Millimeter-wave radar motor error. Check whether radar is stalled (%alarmid). If not, restart radar and try again |
| `0x15020022` | Millimeter-wave radar motor error. Check whether radar is stalled (%alarmid). If not, restart radar and try again |
| `0x15020023` | Millimeter-wave radar sensing error (%alarmid). Check and update firmware to latest version to continue |
| `0x15030020` | Starting millimeter-wave radar timed out or radar link unstable (%alarmid). Check if there is strong interference in the surrounding area. If not, restart radar and try again |
| `0x15030021` | Starting millimeter-wave radar timed out or radar link unstable (%alarmid). Check if there is strong interference in the surrounding area. If not, restart radar and try again |
| `0x15030022` | Starting millimeter-wave radar timed out or radar link unstable (%alarmid). Check if there is strong interference in the surrounding area. If not, restart radar and try again |
| `0x15030023` | Starting millimeter-wave radar timed out or radar link unstable (%alarmid). Check if there is strong interference in the surrounding area. If not, restart radar and try again |
| `0x15030024` | Starting millimeter-wave radar timed out or radar link unstable (%alarmid). Check if there is strong interference in the surrounding area. If not, restart radar and try again |
| `0x15030025` | Starting millimeter-wave radar timed out or radar link unstable (%alarmid). Check if there is strong interference in the surrounding area. If not, restart radar and try again |
| `0x15030026` | Starting millimeter-wave radar timed out or radar link unstable (%alarmid). Check if there is strong interference in the surrounding area. If not, restart radar and try again |
| `0x15040020` | Millimeter-wave radar motor error. Check whether radar is stalled (%alarmid). If not, restart radar and try again |
| `0x15040021` | Millimeter-wave radar motor error. Check whether radar is stalled (%alarmid). If not, restart radar and try again |
| `0x15040022` | Millimeter-wave radar rotary table communication error. Restart aircraft (%alarmid) |
| `0x15040023` | Millimeter-wave radar rotary table communication error. Restart aircraft (%alarmid) |
| `0x15040024` | Millimeter-wave radar rotary table communication error. Restart aircraft (%alarmid) |
| `0x15060020` | Millimeter-wave radar motor error. Check whether radar is stalled (%alarmid). If not, restart radar and try again |
| `0x15070020` | Starting millimeter-wave radar timed out or radar link unstable (%alarmid). Check if there is strong interference in the surrounding area. If not, restart radar and try again |
| `0x15080020` | Make sure ambient temperature is proper for millimeter-wave radar operation (%alarmid). Wait for radar temperature to return to normal before use |
| `0x15090020` | Make sure ambient temperature is proper for millimeter-wave radar operation (%alarmid). Wait for radar temperature to return to normal before use |
| `0x15090021` | Millimeter-wave radar error. Obstacle sensing unavailable (%alarmid) |
| `0x15090022` | Millimeter-wave radar error. Restart aircraft (%alarmid) |
| `0x15090023` | Millimeter-wave radar error. Restart aircraft (%alarmid) |
| `0x15100020` | Starting millimeter-wave radar timed out or radar link unstable (%alarmid). Check if there is strong interference in the surrounding area. If not, restart radar and try again |
| `0x15100021` | Starting millimeter-wave radar timed out or radar link unstable (%alarmid). Check if there is strong interference in the surrounding area. If not, restart radar and try again |
| `0x15100022` | Starting millimeter-wave radar timed out or radar link unstable (%alarmid). Check if there is strong interference in the surrounding area. If not, restart radar and try again |
| `0x15110020` | Millimeter-wave radar motor error. Check whether radar is stalled (%alarmid). If not, restart radar and try again |
| `0x15130021` | Millimeter-wave radar sensing error (%alarmid). Check and update firmware to latest version to continue |
| `0x15140020` | Millimeter-wave radar RF clock error (%alarmid). Return to home promptly and check radar |
| `0x15220020` | Backward and downward radar disconnected (%alarmid). Restart aircraft or check and replace radar |
| `0x15300020` | Millimeter-wave radar sensing error (%alarmid). Check and update firmware to latest version to continue |
| `0x15300021` | Millimeter-wave radar sensing error (%alarmid). Check and update firmware to latest version to continue |
| `0x15300022` | Millimeter-wave radar sensing error (%alarmid). Check and update firmware to latest version to continue |

---

**Source**: [`DJI_Cloud/HMS.json`](../../DJI_Cloud/HMS.json) (DJI v1.15 authoritative).

**See also**: 
- Event definition — [`mqtt/dock-to-cloud/events/hms.md`](../mqtt/dock-to-cloud/events/hms.md).
- Topic-level overview — [`mqtt/README.md`](../mqtt/README.md).
- General API error codes (distinct from HMS alarms) — [`error-codes/README.md`](../error-codes/README.md).
