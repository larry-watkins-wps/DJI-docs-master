# HMS codes — 0x1E** (PSDK / third-party payload (searchlight, speaker, etc.))

Prefix byte `0x1E`. 28 alarm codes.

The prefix byte is the wire-level grouping DJI uses in the `data.list[].code` field emitted on [`thing/product/{gateway_sn}/events` method `hms`](../mqtt/dock-to-cloud/events/hms.md). The domain label above is inferred from the tip text — DJI does not publish an official prefix taxonomy.

Entries rendered with a trailing **+** have a curated CN→EN translation because the original `tipEn` value in [`HMS.json`](../../DJI_Cloud/HMS.json) contains Chinese-language developer-debug strings under the "English" field. The CN originals are preserved below each subsection in a `CN source` callout so the audit trail is intact.

| Alarm ID | Tip |
|---|---|
| `0x1E000001` | Payload startup error. Restart aircraft. If the issue persists, contact the payload manufacturer for assistance |
| `0x1E000002` | Payload communication error. Restart aircraft. If the issue persists, contact the payload manufacturer for assistance |
| `0x1E000003` | Payload overheated. RTH or land promptly. When payload temperature returns to normal, restart payload |
| `0x1E000004` | Payload hardware error. Restart aircraft. If the issue persists, contact the payload manufacturer for assistance |
| `0x1E000006` | Speaker resonates with the aircraft. Power supply disconnected. Wait for power supply to recover |
| `0x1E000101` | Aircraft returning to home. Spotlight disabled automatically |
| `0x1E000102` | Aircraft has not taken off. Spotlight max brightness level limited to 40% |
| `0x1E000103` | Spotlight power restricted. Max brightness level reduced |
| `0x1E000104` | Spotlight temperature too high. Brightness will be continuously reduced |
| `0x1E000105` | Spotlight disabled. Battery level low and aircraft is auto landing |
| `0x1E010001` | Speaker overheats (%alarmid). Lower broadcast volume or wait until speaker cools down |
| `0x1E010002` | Speaker hardware error (%alarmid).Contact DJI Support |
| `0x1E010003` | Speaker overloaded (%alarmid). Restart aircraft |
| `0x1E010004` | Battery power limited. Speaker disabled |
| `0x1E040001` | Spotlight unable to obtain aircraft information |
| `0x1E040002` | Searchlight gimbal self-check failed+ |
| `0x1E040003` | Searchlight gimbal motor overloaded+ |
| `0x1E050001` | Searchlight gimbal calibration error+ |
| `0x1E050003` | Motor on left side of spotlight error. Try restarting spotlight. Contact your local dealer or DJI Support if issue persists |
| `0x1E060001` | Searchlight unable to retrieve aircraft information+ |
| `0x1E070002` | Searchlight gimbal sensor fault+ |
| `0x1E070003` | Searchlight left-side motor abnormal. Try restarting the searchlight. If the issue persists, contact your nearest dealer or DJI After-Sales Service+ |
| `0x1E070004` | Searchlight right-side motor abnormal. Try restarting the searchlight. If the issue persists, contact your nearest dealer or DJI After-Sales Service+ |
| `0x1E070005` | Searchlight gimbal motor fault+ |
| `0x1E0F0001` | Spotlight gimbal attitude initialization failed |
| `0x1E0F0002` | Searchlight has no IMU data+ |
| `0x1E0F0003` | Searchlight gimbal motor not initialized+ |
| `0x1E110001` | Searchlight gimbal attitude initialization failed+ |

<details><summary>CN source (verbatim from HMS.json)</summary>

| Alarm ID | `tipEn` (original CN) |
|---|---|
| `0x1E040002` | 探照灯云台自检失败 |
| `0x1E040003` | 探照灯云台电机过载 |
| `0x1E050001` | 探照灯云台标定错误 |
| `0x1E060001` | 探照灯无法获取飞行器信息 |
| `0x1E070002` | 探照灯云台传感器故障 |
| `0x1E070003` | 探照灯左侧电机异常，请尝试重启探照灯，若仍存在该问题，请联系就近代理商或大疆售后服务 |
| `0x1E070004` | 探照灯右侧电机异常，请尝试重启探照灯，若仍存在该问题，请联系就近代理商或大疆售后服务 |
| `0x1E070005` | 探照灯云台电机故障 |
| `0x1E0F0002` | 探照灯无IMU数据 |
| `0x1E0F0003` | 探照灯云台电机未初始化 |
| `0x1E110001` | 探照灯云台姿态初始化失败 |

</details>

---

**Source**: [`DJI_Cloud/HMS.json`](../../DJI_Cloud/HMS.json) (DJI v1.15 authoritative).

**See also**: 
- Event definition — [`mqtt/dock-to-cloud/events/hms.md`](../mqtt/dock-to-cloud/events/hms.md).
- Topic-level overview — [`mqtt/README.md`](../mqtt/README.md).
- General API error codes (distinct from HMS alarms) — [`error-codes/README.md`](../error-codes/README.md).
