# HMS codes — 0x19** (System overload (CPU / memory / network))

Prefix byte `0x19`. 52 alarm codes.

The prefix byte is the wire-level grouping DJI uses in the `data.list[].code` field emitted on [`thing/product/{gateway_sn}/events` method `hms`](../mqtt/dock-to-cloud/events/hms.md). The domain label above is inferred from the tip text — DJI does not publish an official prefix taxonomy.

Entries rendered with a trailing **+** have a curated CN→EN translation because the original `tipEn` value in [`HMS.json`](../../DJI_Cloud/HMS.json) contains Chinese-language developer-debug strings under the "English" field. The CN originals are preserved below each subsection in a `CN source` callout so the audit trail is intact.

| Alarm ID | Tip |
|---|---|
| `0x19000001` | Avionics system overloaded (%alarmid). Fly with caution and check whether logs are being transmitted. Restart aircraft to restore |
| `0x19000002` | Avionics system overloaded (%alarmid). Fly with caution and check whether logs are being transmitted. Restart aircraft to restore |
| `0x19000004` | Speaker overheats (%alarmid). Lower broadcast volume or wait until speaker cools down |
| `0x19000011` | Avionics system memory insufficient (%alarmid). Restart aircraft or fly with caution |
| `0x19000012` | Avionics system memory insufficient (%alarmid). Restart aircraft or fly with caution |
| `0x19000021` | Avionics system error (%alarmid). Restart aircraft or fly with caution. |
| `0x19000022` | Avionics system error (%alarmid). Restart aircraft or fly with caution. |
| `0x19000031` | Restart aircraft after clearing data (%alarmid) |
| `0x19000041` | USB connection detected (%alarmid). Fly with caution or disconnect USB cable and restart aircraft |
| `0x19000042` | Restart aircraft after clearing data (%alarmid) |
| `0x19000051` | Firmware updating (%alarmid). Wait for update to complete before use |
| `0x19000060` | Selinux permission check error |
| `0x19000061` | Selinux permission check errors |
| `0x19000800` | Aircraft fan %index error (%alarmid). Check whether fan is stalled |
| `0x19000801` | Camera fan error (%alarmid). Check whether the fan is stalled |
| `0x19000802` | Camera processor overheated. Wait for camera processor to cool down before use |
| `0x19000803` | Camera overheated (%alarmid). Recording will stop soon. Wait for camera to cool down before use |
| `0x1901C080` | Current aircraft does not support working with both Zenmuse L2 and H30 series. Use one of the payloads separately (%alarmid) |
| `0x1901C081` | Current aircraft does not support working with more than one Zenmuse H30 series payload. Use one of the payloads separately (%alarmid) |
| `0x1901C082` | Current aircraft does not support working with more than one Zenmuse L2 payload. Use one of the payloads separately (%alarmid) |
| `0x19100041` | Livestream network connection unavailable (%alarmid). Check network connection status |
| `0x19100042` | Livestream registration password error. Check livestream parameters and password |
| `0x19100043` | Livestream registration timed out. Check network connection, port number, and server status |
| `0x19100044` | Livestream channel connection failed (%alarmid). Check network connection status |
| `0x19100045` | Livestream channel URL parameter format error (%alarmid). Check URL format |
| `0x19100051` | Selecting livestream channel timed out (%alarmid). Check server status |
| `0x19100052` | Selecting livestream channel. Parameters error (%alarmid). Check server compatibility |
| `0x19100053` | Selecting livestream channel received no response (%alarmid). Check server status |
| `0x19100054` | Deleted+ |
| `0x19100055` | No streaming data available after selecting livestream channel (%alarmid). Check whether the camera is in playback mode |
| `0x19100056` | Livestream channel bit rate error (%alarmid). Check network connection status and quality |
| `0x19100057` | Livestream channel frame rate error (%alarmid). Check network connection status and quality |
| `0x19100058` | Livestream channel data sending error (%alarmid). Check network connection status and quality |
| `0x19100071` | Livestream channel losing data packet (%alarmid). Check network connection status and quality |
| `0x19100072` | Livestream channel experiencing high latency (%alarmid). Check network connection status and quality |
| `0x19100073` | Livestream channel experiencing high network jitter (%alarmid). Check network connection status and quality |
| `0x19100074` | Livestream channel experiencing network congestion (%alarmid). Check network connection status and quality |
| `0x19100081` | Livestream metadata transfer frequency error (%alarmid). Check aircraft connection status |
| `0x19100082` | Livestream unable to get metadata (%alarmid). Check aircraft connection status and restart all devices |
| `0x19100083` | Unable to obtain aircraft location during livestream (%alarmid). Check aircraft GNSS positioning |
| `0x19117042` | Aircraft charging board did not enter charging state+ |
| `0x19117100` | Battery unable to heat and maintain temperature+ |
| `0x19117121` | Battery did not enter temperature-maintenance state+ |
| `0x19117200` | Aircraft power-on fault occurred+ |
| `0x19117300` | Aircraft power-off failed+ |
| `0x19117420` | Aircraft battery temperature too low — cannot operate+ |
| `0x19117440` | Aircraft battery temperature above 45 °C — cannot operate+ |
| `0x19200001` | Payload system CPU usage too high. Camera tasks may be affected. Restart aircraft to restore |
| `0x1920001` | Payload system CPU usage too high. Camera tasks may be affected. Restart aircraft to restore |
| `0x19200011` | Payload system low memory low. Camera tasks may be affected. Restart aircraft to restore |
| `0x19200021` | Payload system error. Camera tasks may be affected. Restart aircraft to restore |
| `0x1920011` | Payload system memory low. Camera tasks may be affected. Restart aircraft to restore |

<details><summary>CN source (verbatim from HMS.json)</summary>

| Alarm ID | `tipEn` (original CN) |
|---|---|
| `0x19100054` | 删除 |
| `0x19117042` | 飞机充电板未进入充电 |
| `0x19117100` | 电池无法加热保温 |
| `0x19117121` | 电池未进入保温状态 |
| `0x19117200` | 飞机开机发生故障 |
| `0x19117300` | 飞机关机失败 |
| `0x19117420` | 飞机电池温度过低，不能工作 |
| `0x19117440` | 飞机电池超45度，不能工作 |

</details>

---

**Source**: [`DJI_Cloud/HMS.json`](../../DJI_Cloud/HMS.json) (DJI v1.15 authoritative).

**See also**: 
- Event definition — [`mqtt/dock-to-cloud/events/hms.md`](../mqtt/dock-to-cloud/events/hms.md).
- Topic-level overview — [`mqtt/README.md`](../mqtt/README.md).
- General API error codes (distinct from HMS alarms) — [`error-codes/README.md`](../error-codes/README.md).
