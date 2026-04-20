# HMS codes — 0x1F** (LTE / Cellular)

Prefix byte `0x1F`. 56 alarm codes.

The prefix byte is the wire-level grouping DJI uses in the `data.list[].code` field emitted on [`thing/product/{gateway_sn}/events` method `hms`](../mqtt/dock-to-cloud/events/hms.md). The domain label above is inferred from the tip text — DJI does not publish an official prefix taxonomy.

Entries rendered with a trailing **+** have a curated CN→EN translation because the original `tipEn` value in [`HMS.json`](../../DJI_Cloud/HMS.json) contains Chinese-language developer-debug strings under the "English" field. The CN originals are preserved below each subsection in a `CN source` callout so the audit trail is intact.

| Alarm ID | Tip |
|---|---|
| `0x1F010000` | 4G service: unable to obtain license. Contact DJI Support (%alarmid) |
| `0x1F010001` | 4G service: license expired. Import valid license (%alarmid) |
| `0x1F010002` | 4G service: license verification failed. Contact DJI Support (%alarmid) |
| `0x1F010003` | 4G service: device SN unauthorized. Authorize device SN (%alarmid) |
| `0x1F010004` | 4G service: device SN unauthorized. Purchase upgrade package (%alarmid) |
| `0x1F010005` | 4G service: the number of connected devices exceeds authorized number. Purchase upgrade package (%alarmid) |
| `0x1F010006` | 4G service: device firmware version too early. Upgrade firmware (%alarmid) |
| `0x1F010007` | 4G service: server version too early. Upgrade server (%alarmid) |
| `0x1F010008` | 4G service: requested parameter error. Contact DJI Support (%alarmid) |
| `0x1F010009` | 4G service: server internal error. Contact DJI Support (%alarmid) |
| `0x1F01000A` | 4G service: unable to obtain license. Contact DJI Support (%alarmid) |
| `0x1F01000B` | 4G service: license expired. Import valid license (%alarmid) |
| `0x1F01000C` | 4G service: license verification failed. Contact DJI Support (%alarmid) |
| `0x1F01000D` | System time error. Make sure device and server time are correct and try again |
| `0x1F01000E` | Current area does not match area unlocked by license. Check unlocked area |
| `0x1F010063` | 4G service: system unknown error. Contact DJI Support (%alarmid) |
| `0x1F0B0001` | Aircraft unable to use LTE Transmission. Network unstable or SIM card disconnected from network (%alarmid) |
| `0x1F0B0002` | No network on DJI Cellular Dongle of remote controller. Check SIM card service or connect to Wi-Fi network (%alarmid) |
| `0x1F0B0003` | LTE Transmission unavailable. Restart aircraft and remote controller (%alarmid) |
| `0x1F0B0004` | LTE Transmission unavailable. Restart aircraft and remote controller (%alarmid) |
| `0x1F0B0005` | LTE Transmission unavailable. Check and ensure remote controller and aircraft are linked properly (%alarmid) |
| `0x1F0B0006` | LTE Transmission unavailable. Restart remote controller (%alarmid) |
| `0x1F0B0007` | LTE Transmission unavailable. Check aircraft 4G Dongle network connectivity (%alarmid) |
| `0x1F0B0008` | LTE Transmission unavailable (%alarmid) |
| `0x1F0B0009` | LTE Transmission unavailable. Restart remote controller (%alarmid) |
| `0x1F0B0016` | LTE Transmission unavailable (%alarmid). Make sure you are connected to a valid Wi-Fi network or via a 4G dongle. If connection is still unavailable, restart RC |
| `0x1F0B0017` | LTE Transmission unavailable (%alarmid). Make sure you are connected to a valid Wi-Fi network or via a 4G dongle. If connection is still unavailable, restart RC |
| `0x1F0B0018` | LTE Transmission unavailable. Restart aircraft and remote controller (%alarmid) |
| `0x1F0B001A` | LTE Transmission unavailable. Check aircraft 4G Dongle network connectivity (%alarmid) |
| `0x1F0B001B` | LTE Transmission unavailable (%alarmid) |
| `0x1F0B001C` | LTE Transmission error. Aircraft authentication files missing (%alarmid). Immediately contact your local dealer or DJI Support |
| `0x1F0B001D` | LTE Transmission error. Aircraft authentication files missing (%alarmid). Immediately contact your local dealer or DJI Support |
| `0x1F0B0020` | Update DJI Cellular Dongle of aircraft required(%alarmid) |
| `0x1F0B0021` | Update DJI Cellular Dongle of remote controller required(%alarmid) |
| `0x1F0B0023` | LTE signal weak. Fly with caution.(%alarmid) |
| `0x1F0B0024` | LTE signal weak. Fly with caution.(%alarmid) |
| `0x1F0B0025` | LTE signal weak. Fly with caution.(%alarmid) |
| `0x1F0B0027` | Aircraft LTE certification update required. Contact your local dealer or DJI Support.(%alarmid) |
| `0x1F0B0028` | Remote controller LTE certification update required. Contact your local dealer or DJI Support.(%alarmid) |
| `0x1F0B002A` | Incompatible firmware versions. Return to home screen to update firmware.(%alarmid) |
| `0x1F0B002B` | Incompatible firmware versions. Return to home screen to update firmware.(%alarmid) |
| `0x1F0B002E` | Remote controller signal weak. Fly with caution (%alarmid) |
| `0x1F0B0030` | Failed to connect to LTE server. Try again later.(%alarmid) |
| `0x1F0B0036` | Enhanced Transmission unavailable in current region.(%alarmid) |
| `0x1F0B0037` | No internet access on DJI Cellular Dongle of aircraft. Move or change network.(%alarmid) |
| `0x1F0B0038` | No network on DJI Cellular Dongle of remote controller. Move to location with stronger signal or connect to Wi-Fi network (%alarmid) |
| `0x1F0B003A` | No internet access on DJI Cellular Dongle of aircraft. Change network provider.(%alarmid) |
| `0x1F0B003B` | No network on DJI Cellular Dongle of remote controller. Move to location with stronger signal or connect to Wi-Fi network (%alarmid) |
| `0x1F0B003D` | Move to a location with better network connection or try again later. If issue persists, check if SIM card service of DJI Cellular Dongle has sufficient balance and data allowance (%alarmid) |
| `0x1F0B003E` | No network on SIM card of DJI Cellular Dongle of remote controller. Check or replace SIM card (%alarmid) |
| `0x1F0B0040` | No network on remote controller. Install DJI Cellular Dongle or connect to Wi-Fi network (%alarmid) |
| `0x1F0B0045` | Enhanced link latency high. Fly with caution (%alarmid) |
| `0x1F0B0046` | Activate eSIM card or insert SIM card in DJI Cellular Dongle of aircraft |
| `0x1F0B0047` | Switch to SIM card in DJI Cellular Dongle of aircraft or activate eSIM card |
| `0x1F0B0048` | Activate eSIM card or insert SIM card in DJI Cellular Dongle of remote controller |
| `0x1F0B0049` | Switch to SIM card in DJI Cellular Dongle of remote controller or activate eSIM card |

---

**Source**: [`DJI_Cloud/HMS.json`](../../DJI_Cloud/HMS.json) (DJI v1.15 authoritative).

**See also**: 
- Event definition — [`mqtt/dock-to-cloud/events/hms.md`](../mqtt/dock-to-cloud/events/hms.md).
- Topic-level overview — [`mqtt/README.md`](../mqtt/README.md).
- General API error codes (distinct from HMS alarms) — [`error-codes/README.md`](../error-codes/README.md).
