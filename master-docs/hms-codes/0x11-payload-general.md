# HMS codes — 0x11** (Payload (general))

Prefix byte `0x11`. 45 alarm codes.

The prefix byte is the wire-level grouping DJI uses in the `data.list[].code` field emitted on [`thing/product/{gateway_sn}/events` method `hms`](../mqtt/dock-to-cloud/events/hms.md). The domain label above is inferred from the tip text — DJI does not publish an official prefix taxonomy.

Entries rendered with a trailing **+** have a curated CN→EN translation because the original `tipEn` value in [`HMS.json`](../../DJI_Cloud/HMS.json) contains Chinese-language developer-debug strings under the "English" field. The CN originals are preserved below each subsection in a `CN source` callout so the audit trail is intact.

| Alarm ID | Tip |
|---|---|
| `0x11000020` | Check whether payload is working normally (%alarmid). If yes, and the issue persists, contact your local dealer or DJI Support |
| `0x11000021` | Check whether payload is working normally (%alarmid). If yes, and the issue persists, contact your local dealer or DJI Support |
| `0x11000022` | Check whether payload is working normally (%alarmid). If yes, and the issue persists, contact your local dealer or DJI Support |
| `0x11000023` | Check whether payload is working normally (%alarmid). If yes, and the issue persists, contact your local dealer or DJI Support |
| `0x11000024` | Check whether payload is working normally (%alarmid). If yes, and the issue persists, contact your local dealer or DJI Support |
| `0x11000025` | Check whether payload is working normally (%alarmid). If yes, and the issue persists, contact your local dealer or DJI Support |
| `0x11000029` | Check whether PSDK is working normally (%alarmid). If yes, and the issue persists, contact your local dealer or DJI Support |
| `0x1100002A` | Check whether PSDK is working normally (%alarmid). If yes, and the issue persists, contact your local dealer or DJI Support |
| `0x1100002B` | Check whether PSDK is working normally (%alarmid). If yes, and the issue persists, contact your local dealer or DJI Support |
| `0x1100002C` | Check whether PSDK is working normally (%alarmid). If yes, and the issue persists, contact your local dealer or DJI Support |
| `0x1100002D` | Check whether PSDK is working normally (%alarmid). If yes, and the issue persists, contact your local dealer or DJI Support |
| `0x1100002E` | PSDK device rated power exceeded. Failed to restart (%alarmid) |
| `0x11000046` | Aircraft screw rod reaching maximum life span (%alarmid). To ensure flight safety, contact DJI Support and send aircraft back to DJI for maintenance |
| `0x11020030` | %battery_index Battery cover temperature error. Switched to single battery flight. Return to home or land promptly |
| `0x11020031` | %battery_index Battery connector temperature error. Switched to single battery flight. Return to home or land promptly |
| `0x110B0001` | %battery_index Battery overcurrent when discharging. Maintain smooth flight and check if aircraft is overloaded (%alarmid) |
| `0x110B0002` | %battery_index Battery overheated. Return to home promptly and wait until battery cools down (%alarmid) |
| `0x110B0003` | %battery_index Battery temperature too low. Warm up battery to 5°C or higher (%alarmid) |
| `0x110B0004` | %battery_index Battery short-circuited during discharge. Replace battery (%alarmid) |
| `0x110B0005` | Battery %index cell voltage low. Replace battery (%alarmid) |
| `0x110B0006` | %battery_index Battery cell damaged. Stop using battery and contact DJI Support (%alarmid) |
| `0x110B0006_ta101` | Large cycle count difference between batteries. Use batteries with similar cycle counts |
| `0x110B0007` | %battery_index Battery auto-check failed. Stop using battery and contact DJI Support (%alarmid) |
| `0x110B0008` | %battery_index Battery auto-check failed. Stop using battery and contact DJI Support (%alarmid) |
| `0x110B0009` | %battery_index Battery auto-check failed. Stop using battery and contact DJI Support (%alarmid) |
| `0x110B000A` | %battery_index Battery auto-check failed. Stop using battery and contact DJI Support (%alarmid) |
| `0x110B000B` | %battery_index Battery damaged. Stop using battery and contact DJI Support (%alarmid) |
| `0x110B000C` | %battery_index Battery maintenance required to ensure flight safety (%alarmid) |
| `0x110B000D` | %battery_index Battery damaged. Stop using battery and contact DJI Support (%alarmid) |
| `0x110B000F` | %battery_index Battery capacity significantly reduced. Continue using battery may cause safety risks (%alarmid) |
| `0x110B0010` | Safety requirements not met. Dispose of %battery_index Battery properly (%alarmid) |
| `0x110B0011` | %battery_index Battery data communication error. Reinstall battery. Replace battery if issue persists (%alarmid) |
| `0x110B0012` | %battery_index Battery maintenance required (%alarmid) |
| `0x110B0013` | Battery not detected in %battery_index Battery slot. Insert or replace battery (%alarmid) |
| `0x110B0015` | %battery_index Battery maintenance required to ensure flight safety (%alarmid) |
| `0x110B0016` | %battery_index Battery maintenance required to ensure flight safety (%alarmid) |
| `0x110B0017` | %battery_index Battery maintenance required to ensure flight safety (%alarmid) |
| `0x110B0018` | %battery_index Battery maintenance required to ensure flight safety (%alarmid) |
| `0x110B0019` | %battery_index Battery maintenance required to ensure flight safety (%alarmid) |
| `0x110B001A` | %battery_index Battery maintenance required to ensure flight safety (%alarmid) |
| `0x110B001B` | %battery_index Battery maintenance required to ensure flight safety (%alarmid) |
| `0x110B001C` | Large difference in batteries cycle counts or production dates. Use matching batteries to ensure flight safety (%alarmid) |
| `0x110B001D` | Battery discharge error. Land or return to home promptly (%alarmid) |
| `0x110B001E` | %battery_index Battery connection error (%alarmid). Return to home or land promptly |
| `0x110B0403` | Incompatible battery firmware versions. Update firmware |

## Contextual suffixes

Alarm IDs in this prefix include trailing suffixes that denote DJI-emitted variants of the same base code in different flight or airframe contexts:

- `_ta101` — 1 entry/entries.

---

**Source**: [`DJI_Cloud/HMS.json`](../../DJI_Cloud/HMS.json) (DJI v1.15 authoritative).

**See also**: 
- Event definition — [`mqtt/dock-to-cloud/events/hms.md`](../mqtt/dock-to-cloud/events/hms.md).
- Topic-level overview — [`mqtt/README.md`](../mqtt/README.md).
- General API error codes (distinct from HMS alarms) — [`error-codes/README.md`](../error-codes/README.md).
