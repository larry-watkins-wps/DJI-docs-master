# HMS codes — 0x17** (Image transmission & RC link)

Prefix byte `0x17`. 16 alarm codes.

The prefix byte is the wire-level grouping DJI uses in the `data.list[].code` field emitted on [`thing/product/{gateway_sn}/events` method `hms`](../mqtt/dock-to-cloud/events/hms.md). The domain label above is inferred from the tip text — DJI does not publish an official prefix taxonomy.

Entries rendered with a trailing **+** have a curated CN→EN translation because the original `tipEn` value in [`HMS.json`](../../DJI_Cloud/HMS.json) contains Chinese-language developer-debug strings under the "English" field. The CN originals are preserved below each subsection in a `CN source` callout so the audit trail is intact.

| Alarm ID | Tip |
|---|---|
| `0x17000001` | Primary image transmission disconnected (%alarmid). Adjust antennas |
| `0x17000002` | Remote controller signal weak. Adjust antennas (%alarmid) |
| `0x17000003` | Strong signal interference in aircraft location (%alarmid). Fly with caution |
| `0x17000004` | Image transmission signal weak (%alarmid). Adjust antennas |
| `0x17000005` | Strong signal interference in remote controller location (%alarmid). Fly with caution |
| `0x17000006` | Country code error (%alarmid). Move aircraft and remote controller to open area |
| `0x17000011` | Avionics system memory insufficient (%alarmid). Restart aircraft or fly with caution |
| `0x17000013` | Strong remote controller signal interference (%alarmid). Move away from other remote controllers or source of interference |
| `0x17000014` | Strong remote controller signal interference (%alarmid). Move away from other remote controllers or source of interference |
| `0x17000015` | Strong aircraft signal interference (%alarmid). Return to home promptly or move away from source of interference |
| `0x17000016` | Remote controller signal weak (%alarmid). Adjust antenna |
| `0x17000071` | Avionics system overloaded (%alarmid). Fly with caution and check whether logs are being transmitted. Restart aircraft to restore |
| `0x17000081` | Avionics system memory insufficient (%alarmid). Restart aircraft or fly with caution |
| `0x17010021` | Flight controller error (%alarmid). Return to home promptly |
| `0x17110041` | Control stick input error (%alarmid). Fly with caution, land promptly, restart remote controller, and try again |
| `0x1720020A` | Winch limit switch error. Check if the switch is stuck or damaged in case payload is dropped during flight or cable length is incorrect |

---

**Source**: [`DJI_Cloud/HMS.json`](../../DJI_Cloud/HMS.json) (DJI v1.15 authoritative).

**See also**: 
- Event definition — [`mqtt/dock-to-cloud/events/hms.md`](../mqtt/dock-to-cloud/events/hms.md).
- Topic-level overview — [`mqtt/README.md`](../mqtt/README.md).
- General API error codes (distinct from HMS alarms) — [`error-codes/README.md`](../error-codes/README.md).
