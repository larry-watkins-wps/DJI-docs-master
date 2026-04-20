# HMS codes — 0x1A** (Vision sensors)

Prefix byte `0x1A`. 170 alarm codes.

The prefix byte is the wire-level grouping DJI uses in the `data.list[].code` field emitted on [`thing/product/{gateway_sn}/events` method `hms`](../mqtt/dock-to-cloud/events/hms.md). The domain label above is inferred from the tip text — DJI does not publish an official prefix taxonomy.

Entries rendered with a trailing **+** have a curated CN→EN translation because the original `tipEn` value in [`HMS.json`](../../DJI_Cloud/HMS.json) contains Chinese-language developer-debug strings under the "English" field. The CN originals are preserved below each subsection in a `CN source` callout so the audit trail is intact.

| Alarm ID | Tip |
|---|---|
| `0x1A010006` | Restart the aircraft (%alarmid). If the issue persists, contact your nearest dealer or DJI After-Sales Service.+ |
| `0x1A010007` | System in factory mode. Contact DJI Support (%alarmid) |
| `0x1A010040` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A010041` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A010042` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A010043` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A010044` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A010045` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A010046` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A010047` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A010048` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A010049` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A01004A` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A01004B` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A010080` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A010081` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A010082` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A010083` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A010084` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A010085` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A010086` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A010087` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A010088` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A010089` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A01008A` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A01008B` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A0100C0` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A0100C1` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A0100C2` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A0100C3` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A0100C4` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A0100C5` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A0100C6` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A0100C7` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A0100C8` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A0100C9` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A0100CA` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A0100CB` | Vision sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A0100F0` | Perception sensor initialized normally (factory line-test use only) (%alarmid)+ |
| `0x1A011340` | Vision system calibration error (%alarmid). Contact DJI Support |
| `0x1A011341` | Vision system calibration error (%alarmid). Contact DJI Support |
| `0x1A011342` | Vision system calibration error (%alarmid). Contact DJI Support |
| `0x1A011343` | Vision system calibration error (%alarmid). Contact DJI Support |
| `0x1A011344` | Vision system calibration error (%alarmid). Contact DJI Support |
| `0x1A011345` | Vision system calibration error (%alarmid). Contact DJI Support |
| `0x1A011346` | Vision system calibration error (%alarmid). Contact DJI Support |
| `0x1A011347` | Vision system calibration error (%alarmid). Contact DJI Support |
| `0x1A011348` | Vision system calibration error (%alarmid). Contact DJI Support |
| `0x1A011349` | Vision system calibration error (%alarmid). Contact DJI Support |
| `0x1A01134A` | Vision system calibration error (%alarmid). Contact DJI Support |
| `0x1A01134B` | Vision system calibration error (%alarmid). Contact DJI Support |
| `0x1A020040` | Infrared sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A020041` | Infrared sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A020042` | Infrared sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A020043` | Infrared sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A020044` | Infrared sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A020045` | Infrared sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A020080` | Infrared sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A020081` | Infrared sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A020082` | Infrared sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A020083` | Infrared sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A020084` | Infrared sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A020085` | Infrared sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A0200C0` | Infrared sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A0200C1` | Infrared sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A0200C2` | Infrared sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A0200C3` | Infrared sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A0200C4` | Infrared sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A0200C5` | Infrared sensor connection error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A020100` | Infrared sensor calibration error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A020101` | Infrared sensor calibration error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A020102` | Infrared sensor calibration error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A020103` | Infrared sensor calibration error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A020104` | Infrared sensor calibration error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A020105` | Infrared sensor calibration error (%alarmid). Restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x1A020140` | Infrared sensors blocked (%alarmid). Check and remove any objects blocking sensors |
| `0x1A020180` | Infrared sensors overheated (%alarmid). Return to home or land promptly. Move away from high-temperature environment. If the issue persists, contact DJI Support. |
| `0x1A020400` | Low visibility. Sensor system may not work (%alarmid). Fly with caution |
| `0x1A030040` | Bottom infrared sensor connection error. Restart aircraft (%alarmid) |
| `0x1A030041` | Front infrared sensor connection error. Restart aircraft (%alarmid) |
| `0x1A030042` | Back infrared sensor connection error. Restart aircraft (%alarmid) |
| `0x1A030043` | Top infrared sensor connection error. Restart aircraft (%alarmid) |
| `0x1A030044` | Left infrared sensor connection error. Restart aircraft (%alarmid) |
| `0x1A030045` | Right infrared sensor connection error. Restart aircraft (%alarmid) |
| `0x1A030080` | Bottom infrared sensor connection error. Restart aircraft (%alarmid) |
| `0x1A030081` | Front infrared sensor connection error. Restart aircraft (%alarmid) |
| `0x1A030082` | Back infrared sensor connection error. Restart aircraft (%alarmid) |
| `0x1A030083` | Top infrared sensor connection error. Restart aircraft (%alarmid) |
| `0x1A030084` | Left infrared sensor connection error. Restart aircraft (%alarmid) |
| `0x1A030085` | Right infrared sensor connection error. Restart aircraft (%alarmid) |
| `0x1A030180` | Bottom infrared sensor connection error. Restart aircraft (%alarmid) |
| `0x1A030181` | Front infrared sensor connection error. Restart aircraft (%alarmid) |
| `0x1A030182` | Back infrared sensor connection error. Restart aircraft (%alarmid) |
| `0x1A040001` | Power mode error. Restart aircraft |
| `0x1A210180` | Sensor system error (%alarmid). Downward vision sensor error. Restart aircraft |
| `0x1A210181` | Sensor system error (%alarmid). Front vision sensor error. Restart aircraft |
| `0x1A210182` | Sensor system error (%alarmid). Backward vision sensor error. Restart aircraft |
| `0x1A210183` | Sensor system error (%alarmid). Upward vision sensor error. Restart aircraft |
| `0x1A210184` | Sensor system error (%alarmid). Left vision sensor error. Restart aircraft |
| `0x1A210185` | Sensor system error (%alarmid). Right vision sensor error. Restart aircraft |
| `0x1A2101C0` | Sensor system error (%alarmid). Downward vision sensor initialization error. Restart aircraft |
| `0x1A2101C1` | Sensor system error (%alarmid). Front vision sensor initialization error. Restart aircraft |
| `0x1A2101C2` | Sensor system error (%alarmid). Backward vision sensor initialization error. Restart aircraft |
| `0x1A2101C3` | Sensor system error (%alarmid). Upward vision sensor initialization error. Restart aircraft |
| `0x1A2101C4` | Sensor system error (%alarmid). Left vision sensor initialization error. Restart aircraft |
| `0x1A2101C5` | Sensor system error (%alarmid). Right vision sensor initialization error. Restart aircraft |
| `0x1A310980` | Vision positioning system error (%alarmid). Fly with caution. Restart aircraft and try again |
| `0x1A310981` | Vision positioning system error (%alarmid). Fly with caution. Restart aircraft and try again |
| `0x1A420040` | Obstacle sensing system error (%alarmid). Fly with caution. Restart aircraft and try again |
| `0x1A420041` | Obstacle sensing system error (%alarmid). Fly with caution. Restart aircraft and try again |
| `0x1A420042` | Obstacle sensing system error (%alarmid). Fly with caution. Restart aircraft and try again |
| `0x1A420043` | Obstacle sensing system error (%alarmid). Fly with caution. Restart aircraft and try again |
| `0x1A420044` | Obstacle sensing system error (%alarmid). Fly with caution. Restart aircraft and try again |
| `0x1A420045` | Obstacle sensing system error (%alarmid). Fly with caution. Restart aircraft and try again |
| `0x1A420440` | Obstacle sensing system error (%alarmid). Fly with caution. Restart aircraft and try again |
| `0x1A4205C0` | Obstacle sensing system error (%alarmid). Fly with caution. Restart aircraft and try again |
| `0x1A420680` | Obstacle sensing system error (%alarmid). Fly with caution. Restart aircraft and try again |
| `0x1A420BC0` | Downward ambient light too low (%alarmid). Downward obstacle sensing unavailable. Fly with caution |
| `0x1A420BC1` | Forward ambient light too low (%alarmid). Forward obstacle sensing unavailable. Fly with caution |
| `0x1A420BC2` | Backward ambient light too low (%alarmid). Backward obstacle sensing unavailable. Fly with caution |
| `0x1A420BC3` | Right ambient light too low (%alarmid). Right obstacle sensing unavailable. Fly with caution |
| `0x1A420BC4` | Left ambient light too low (%alarmid). Left obstacle sensing unavailable. Fly with caution |
| `0x1A420BC5` | Upward ambient light too low (%alarmid). Upward obstacle sensing unavailable. Fly with caution |
| `0x1A420BC6` | Horizontal ambient light too low (%alarmid). Horizontal obstacle sensing unavailable. Fly with caution |
| `0x1A420C00` | Downward ambient light too bright (%alarmid). Downward Obstacle Avoidance unavailable. Return to home promptly and check downward vision sensors. Fly with caution |
| `0x1A420C01` | Forward ambient light too bright (%alarmid). Forward Obstacle Avoidance unavailable. Return to home promptly and check forward vision sensors. Fly with caution |
| `0x1A420C02` | Backward ambient light too bright (%alarmid). Backward Obstacle Avoidance unavailable. Return to home promptly and check backward vision sensors. Fly with caution |
| `0x1A420C03` | Right ambient light too bright (%alarmid). Right Obstacle Avoidance unavailable. Return to home promptly and check right vision sensors. Fly with caution |
| `0x1A420C04` | Left ambient light too bright (%alarmid). Left Obstacle Avoidance unavailable. Return to home promptly and check left vision sensors. Fly with caution |
| `0x1A420C05` | Upward ambient light too bright (%alarmid). Upward Obstacle Avoidance unavailable. Return to home promptly and check upward vision sensors. Fly with caution |
| `0x1A420C06` | Horizontal ambient light too bright (%alarmid). Horizontal Obstacle Avoidance unavailable. Return to home promptly and check horizontal vision sensors. Fly with caution |
| `0x1A420C40` | Downward vision sensors blocked (%alarmid). Downward Obstacle Avoidance unavailable. Return to home promptly and check downward vision sensors. Fly with caution |
| `0x1A420C41` | Forward vision sensors blocked (%alarmid). Forward Obstacle Avoidance unavailable. Return to home promptly and check forward vision sensors. Fly with caution |
| `0x1A420C42` | Backward vision sensors blocked (%alarmid). Backward Obstacle Avoidance unavailable. Return to home promptly and check backward vision sensors. Fly with caution |
| `0x1A420C43` | Right vision sensors blocked (%alarmid). Right Obstacle Avoidance unavailable. Return to home promptly and check right vision sensors. Fly with caution |
| `0x1A420C44` | Left vision sensors blocked (%alarmid). Left Obstacle Avoidance unavailable. Return to home promptly and check left vision sensors. Fly with caution |
| `0x1A420C45` | Upward vision sensors blocked (%alarmid). Upward Obstacle Avoidance unavailable. Return to home promptly and check upward vision sensors. Fly with caution |
| `0x1A420C46` | Payload installation detected (%alarmid). Aircraft obstacle-avoidance capability reduced — watch the radar chart and fly with caution+ |
| `0x1A420C80` | Downward vision sensors blurry (%alarmid). Downward Obstacle Avoidance unavailable. Return to home promptly and check downward vision sensors. Fly with caution |
| `0x1A420C81` | Forward vision sensors blurry (%alarmid). Forward Obstacle Avoidance unavailable. Return to home promptly and check forward vision sensors. Fly with caution |
| `0x1A420C82` | Backward vision sensor blurry (%alarmid). Backward Obstacle Avoidance unavailable. Return to home promptly and check backward vision sensors. Fly with caution |
| `0x1A420C83` | Right vision sensors blurry (%alarmid). Right Obstacle Avoidance unavailable. Return to home promptly and check right vision sensors. Fly with caution |
| `0x1A420C84` | Left vision sensors blurry (%alarmid). Left Obstacle Avoidance unavailable. Return to home promptly and check left vision sensors. Fly with caution |
| `0x1A420C85` | Upward vision sensors blurry (%alarmid). Upward Obstacle Avoidance unavailable. Return to home promptly and check upward vision sensors. Fly with caution |
| `0x1A420CC0` | Aircraft attitude angle too large. Obstacle sensing system unavailable (%alarmid). Fly with caution. Check for high wind velocity or other causes |
| `0x1A420D00` | Aircraft attitude angle too large. Obstacle sensing system unavailable and landing protection unavailable (%alarmid). Land aircraft manually. Check for high wind velocity or other causes |
| `0x1A420D40` | Aircraft approaching obstacle sensing blind spot and may not be able to detect obstacles (%alarmid). Fly with caution |
| `0x1A421B00` | Vision system disabled. Switched to lidar obstacle avoidance. The obstacle avoidance available range will change (%alarmid) |
| `0x1A421B40` | LiDAR connected (%alarmid) |
| `0x1A421B80` | LiDAR disconnected (%alarmid) |
| `0x1A430680` | Vision system calibration error (%alarmid). Contact DJI Support |
| `0x1A510380` | Sensor calibration error (%alarmid). Fly with caution |
| `0x1A510381` | Sensor calibration error (%alarmid). Fly with caution |
| `0x1A510382` | Sensor calibration error (%alarmid). Fly with caution |
| `0x1A510383` | Sensor calibration error (%alarmid). Fly with caution |
| `0x1A510384` | Sensor calibration error (%alarmid). Fly with caution |
| `0x1A510385` | Sensor calibration error (%alarmid). Fly with caution |
| `0x1A5103C0` | Sensor calibration error (%alarmid). Recalibrate with DJI Assistant 2 |
| `0x1A5103C1` | Sensor calibration error (%alarmid). Recalibrate with DJI Assistant 2 |
| `0x1A5103C2` | Sensor calibration error (%alarmid). Recalibrate with DJI Assistant 2 |
| `0x1A5103C3` | Sensor calibration error (%alarmid). Recalibrate with DJI Assistant 2 |
| `0x1A5103C4` | Sensor calibration error (%alarmid). Recalibrate with DJI Assistant 2 |
| `0x1A5103C5` | Sensor calibration error (%alarmid). Recalibrate with DJI Assistant 2 |
| `0x1A680040` | Propeller guards mounted. Obstacle Avoidance unavailable. Flight performance and wind resistance performance reduced |
| `0x1A680080` | Propeller guards removed |
| `0x1AFC0080` | Storage module frame loss (%alarmid)+ |
| `0x1AFC0100` | Perception key logs approaching upper limit — land and retrieve logs as soon as possible+ |
| `0x1AFC0140` | Crash logs present — retrieve and clear crash logs before performing flight tests+ |
| `0x1AFD0040` | Sensor system error (%alarmid). Unable to take off. Restart aircraft |
| `0x1AFE0040` | Vision system overloaded. Fly to open area (%alarmid). If the issue persists, contact your local dealer or DJI Support |

<details><summary>CN source (verbatim from HMS.json)</summary>

| Alarm ID | `tipEn` (original CN) |
|---|---|
| `0x1A010006` | 请重启飞行器(%alarmid)，若仍存在该问题，请联系就近代理商或大疆售后服务。 |
| `0x1A0100F0` | 感知传感器初始化正常(仅用于工厂链路测试)(%alarmid) |
| `0x1A420C46` | 检测到安装负载(%alarmid)，飞行器避障能力下降，请观察雷达图谨慎飞行 |
| `0x1AFC0080` | 存储模块丢图(%alarmid) |
| `0x1AFC0100` | 感知关键日志即将到达上限，请尽快降落拉取日志 |
| `0x1AFC0140` | 存在炸机日志，拉取并清理炸机日志后在进行飞测 |

</details>

---

**Source**: [`DJI_Cloud/HMS.json`](../../DJI_Cloud/HMS.json) (DJI v1.15 authoritative).

**See also**: 
- Event definition — [`mqtt/dock-to-cloud/events/hms.md`](../mqtt/dock-to-cloud/events/hms.md).
- Topic-level overview — [`mqtt/README.md`](../mqtt/README.md).
- General API error codes (distinct from HMS alarms) — [`error-codes/README.md`](../error-codes/README.md).
