# HMS codes — 0x1B** (Navigation & Target Acquisition)

Prefix byte `0x1B`. 138 alarm codes.

The prefix byte is the wire-level grouping DJI uses in the `data.list[].code` field emitted on [`thing/product/{gateway_sn}/events` method `hms`](../mqtt/dock-to-cloud/events/hms.md). The domain label above is inferred from the tip text — DJI does not publish an official prefix taxonomy.

Entries rendered with a trailing **+** have a curated CN→EN translation because the original `tipEn` value in [`HMS.json`](../../DJI_Cloud/HMS.json) contains Chinese-language developer-debug strings under the "English" field. The CN originals are preserved below each subsection in a `CN source` callout so the audit trail is intact.

| Alarm ID | Tip |
|---|---|
| `0x1B010001` | Navigation system error . Restart aircraft(%alarmid) |
| `0x1B010002` | Target Acquisition unavailable with current payload(%alarmid) |
| `0x1B010003` | Target Acquisition unavailable in current Photo mode (%alarmid). Switch to Single Shot or Video mode |
| `0x1B010004` | Target too close(%alarmid) |
| `0x1B010005` | Target lost. Target Acquisition paused(%alarmid) |
| `0x1B010006` | Gimbal not facing flight direction. Fly with caution(%alarmid) |
| `0x1B010007` | Target Acquisition paused . Switch to P mode(%alarmid) |
| `0x1B010008` | Enabling Target Acquisition failed(%alarmid) |
| `0x1B010009` | Obstacle detected. Circling stopped. Manually control aircraft to avoid obstacle(%alarmid) |
| `0x1B01000A` | GEO Zone nearby. Circling stopped. Manually control aircraft to avoid GEO Zone(%alarmid) |
| `0x1B01000B` | Smart Track paused(%alarmid) |
| `0x1B01000C` | Target moving too fast. Circling stopped(%alarmid) |
| `0x1B01000D` | Unusual target movement. Drag-select target again(%alarmid) |
| `0x1B01000E` | GNSS signal weak and vision positioning unavailable. Aircraft switched to A mode. Control aircraft manually (%alarmid) |
| `0x1B01000F` | Target lost. Searching...(%alarmid) |
| `0x1B010010` | During Smart Track, you can control gimbals within a certain limit(%alarmid) |
| `0x1B010011` | During Smart Track, you can control lens zoom within a certain limit(%alarmid) |
| `0x1B010401` | Camera data sending error. Target Acquisition paused. Restart camera(%alarmid) |
| `0x1B010402` | Camera data sending error. Smart Track paused. Restart camera(%alarmid) |
| `0x1B010403` | Camera data sending error. Smart Track paused. Restart camera(%alarmid) |
| `0x1B010404` | Camera data sending error. Smart Track paused. Restart camera(%alarmid) |
| `0x1B010405` | Camera data sending error. Smart Track paused. Restart camera(%alarmid) |
| `0x1B010406` | Camera data sending error. Smart Track paused. Restart camera(%alarmid) |
| `0x1B010407` | Camera data sending error. Smart Track paused. Restart camera(%alarmid) |
| `0x1B010408` | Camera data sending error. Smart Track paused. Restart camera(%alarmid) |
| `0x1B010801` | DJI Pilot error. Target Acquisition paused. Restart DJI Pilot(%alarmid) |
| `0x1B010802` | DJI Pilot error. Smart Track paused. Restart DJI Pilot(%alarmid) |
| `0x1B010803` | DJI Pilot error. Smart Track paused. Restart DJI Pilot(%alarmid) |
| `0x1B010C01` | Flight Controller data sending error. Target Acquisition paused. Restart aircraft(%alarmid) |
| `0x1B010C02` | Flight Controller data sending error. Smart Track paused. Restart aircraft(%alarmid) |
| `0x1B010C03` | Flight Controller data sending error. Smart Track paused. Restart aircraft(%alarmid) |
| `0x1B011001` | Gimbal data sending error. Target Acquisition paused. Reinstall payload(%alarmid) |
| `0x1B011002` | Gimbal data sending error. Smart Track paused. Reinstall payload(%alarmid) |
| `0x1B011003` | Gimbal data sending error. Smart Track paused. Reinstall payload(%alarmid) |
| `0x1B011801` | Remote controller data sending error. Target Acquisition stopped. Restart RC(%alarmid) |
| `0x1B011802` | Remote controller data sending error. Target Acquisition paused. Check connection between RC and aircraft(%alarmid) |
| `0x1B030001` | Obstacle detected. RTH stopped. Manually control aircraft to avoid obstacle(%alarmid) |
| `0x1B030002` | GEO Zone nearby. RTH stopped. Manually control aircraft to avoid GEO Zone(%alarmid) |
| `0x1B030003` | RTH error. Fly aircraft manually(%alarmid) |
| `0x1B030004` | Aircraft signal lost. RTH started (%alarmid) |
| `0x1B030005` | Enabling RTH Obstacle Check failed. Control aircraft to return to home manually(%alarmid) |
| `0x1B030006` | Obstacle avoidance or backlight detected. Press the Pause button on the remote controller to exit RTH and manually control aircraft to return to home(%alarmid) |
| `0x1B030007` | Control stick pushed down. Aircraft descending. Aircraft RTH canceled(%alarmid) |
| `0x1B030008` | Control stick pushed down. Aircraft flying backward. Aircraft RTH canceled(%alarmid) |
| `0x1B030010` | Approaching evening (%alarmid). Setting RTH altitude recommended |
| `0x1B030011` | Ambient light too low (%alarmid). Aircraft flying to Home Point in straight line |
| `0x1B030012` | Aircraft accelerating (%alarmid). Battery draining faster |
| `0x1B030013` | Moving control stick reversely detected. RTH stopped (%alarmid) |
| `0x1B030014` | Aircraft accelerating. Battery draining faster (%alarmid). Fly with caution |
| `0x1B030016` | Complex environment. Obstacle avoidance triggered and RTH stopped (%alarmid). Manually control aircraft to return to home and pay attention to flight safety |
| `0x1B030017` | Unable to return to home due to low battery level. Aircraft may land earlier. Selecting alternate landing site recommended (%alarmid) |
| `0x1B03002B` | Obstacle avoidance triggered during return-to-home. Monitor remaining battery and take over promptly (%alarmid)+ |
| `0x1B030033` | Aircraft power draw elevated. Monitor remaining battery and fly safely (%alarmid)+ |
| `0x1B030C02` | GNSS signal weak. RTH accuracy affected. It is recommended to manually control aircraft to return to home (%alarmid) |
| `0X1B033001` | RTH Obstacle Check error. Control aircraft to return to home manually(%alarmid) |
| `0x1B040001` | Focused shooting unavailable with current payload(%alarmid) |
| `0x1B040002` | Focused shooting failed . Switched to normal shooting mode(%alarmid) |
| `0x1B040003` | AI Spot-Check failed. Switched to normal shooting mode(%alarmid) |
| `0x1B040004` | Camera not mounted. Focused shooting failed(%alarmid) |
| `0x1B040401` | Camera error. Focused shooting failed. Restart camera(%alarmid) |
| `0x1B040402` | Switching shooting modes failed. AI Spot-Check failed. Restart camera(%alarmid) |
| `0x1B040403` | Camera zoom timed out. AI Spot-Check failed. Restart camera(%alarmid) |
| `0x1B040801` | Unable to locate focused shooting sample. Reupload flight route(%alarmid) |
| `0x1B040802` | Target box parameter error. Readjust target box(%alarmid) |
| `0x1B041001` | Gimbal error. Focused shooting failed. Reinstall payload(%alarmid) |
| `0x1B060001` | Flight speed limited (%alarmid). Firmware update required |
| `0x1B090001` | Target tracking stopped(%alarmid) |
| `0x1B090002` | Target tracking stopped(%alarmid) |
| `0x1B090003` | Target tracking stopped(%alarmid) |
| `0x1B092C01` | Target identification error(%alarmid) |
| `0x1B092C02` | Target identification error(%alarmid) |
| `0x1B092C03` | Target identification error(%alarmid) |
| `0x1B092C04` | Target identification error(%alarmid) |
| `0x1B092C05` | Target identification error(%alarmid) |
| `0x1B092C06` | Target identification error(%alarmid) |
| `0x1B092C07` | Target identification error(%alarmid) |
| `0x1B092C08` | Target identification error(%alarmid) |
| `0x1B092C09` | Target identification error(%alarmid) |
| `0x1B092C0A` | Target identification error(%alarmid) |
| `0x1B092C0B` | Target identification error(%alarmid) |
| `0x1B092C0C` | Target identification error(%alarmid) |
| `0x1B092C0D` | Target identification error(%alarmid) |
| `0x1B092C0E` | Target identification error(%alarmid) |
| `0x1B092C0F` | Target identification error(%alarmid) |
| `0x1B092C10` | Target identification error(%alarmid) |
| `0x1B092C11` | Target identification error(%alarmid) |
| `0x1B092C12` | Target identification error(%alarmid) |
| `0x1B092C13` | Target identification error(%alarmid) |
| `0x1B092C14` | Target identification error(%alarmid) |
| `0x1B092C15` | Target identification error(%alarmid) |
| `0x1B092C16` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B092C17` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B092C18` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B092C19` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B092C1A` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B092C1B` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B092C1C` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B092C1D` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B092C1E` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B092C1F` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B092C20` | Enabling Smart Track failed. Ensure selected target is valid(%alarmid) |
| `0x1B092C21` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B092C22` | Enabling Smart Track failed. Reduce selected area(%alarmid) |
| `0x1B092C23` | Enabling Smart Track failed. Increase selected area(%alarmid) |
| `0x1B092C24` | Enabling Smart Track failed. Ensure selected target is valid(%alarmid) |
| `0x1B092C25` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B093001` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B093002` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B093003` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B093004` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B093005` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B093006` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B093007` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B093008` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B093009` | Enabling Smart Track failed. Increase selected area(%alarmid) |
| `0x1B09300A` | Enabling Smart Track failed. Ensure selected target is valid(%alarmid) |
| `0x1B09300B` | Target lost. Exited Target Acquisition(%alarmid) |
| `0x1B09300C` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B09300D` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B09300E` | Camera parameters changed. Exited Target Acquisition(%alarmid) |
| `0x1B09300F` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B093010` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B093011` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B093012` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B093013` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B093014` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B093015` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B093016` | Target lost. Exited Smart Track(%alarmid) |
| `0x1B093017` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B093018` | Target too far away. Exited Target Acquisition(%alarmid) |
| `0x1B093019` | Camera parameters changed. Exited Smart Track(%alarmid) |
| `0x1B09301A` | Enabling Smart Track failed. Check and try again(%alarmid) |
| `0x1B0A0001` | GNSS signal weak. Geo-awareness function degraded. Fly with caution |
| `0x1B0A0002` | Failed to load dynamic safety data. Geo-awareness function degraded. It is recommended to update FlySafe database on GEO Zone map |
| `0x1B0A0003` | Failed to query dynamic safety data. Geo-awareness function degraded. It is recommended to update FlySafe database on GEO Zone map |
| `0x1B0A0004` | FlySafe data density high in current region. Aircraft may not be able to fully process data. It is recommended to update FlySafe database |
| `0x1B310001` | Battery level too low to complete flight mission. Adjust flight plan |
| `0x1B310002` | Battery level too low to fly to alternate landing site. Land promptly |

<details><summary>CN source (verbatim from HMS.json)</summary>

| Alarm ID | `tipEn` (original CN) |
|---|---|
| `0x1B03002B` | 返航中触发避障,请注意剩余电量,及时接管(%alarmid) |
| `0x1B030033` | 飞行器功率偏大，请注意剩余电量，安全飞行(%alarmid) |

</details>

---

**Source**: [`DJI_Cloud/HMS.json`](../../DJI_Cloud/HMS.json) (DJI v1.15 authoritative).

**See also**: 
- Event definition — [`mqtt/dock-to-cloud/events/hms.md`](../mqtt/dock-to-cloud/events/hms.md).
- Topic-level overview — [`mqtt/README.md`](../mqtt/README.md).
- General API error codes (distinct from HMS alarms) — [`error-codes/README.md`](../error-codes/README.md).
