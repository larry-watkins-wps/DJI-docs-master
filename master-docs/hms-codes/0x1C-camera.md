# HMS codes — 0x1C** (Camera)

Prefix byte `0x1C`. 167 alarm codes.

The prefix byte is the wire-level grouping DJI uses in the `data.list[].code` field emitted on [`thing/product/{gateway_sn}/events` method `hms`](../mqtt/dock-to-cloud/events/hms.md). The domain label above is inferred from the tip text — DJI does not publish an official prefix taxonomy.

Entries rendered with a trailing **+** have a curated CN→EN translation because the original `tipEn` value in [`HMS.json`](../../DJI_Cloud/HMS.json) contains Chinese-language developer-debug strings under the "English" field. The CN originals are preserved below each subsection in a `CN source` callout so the audit trail is intact.

| Alarm ID | Tip |
|---|---|
| `0x1C000103` | Camera processor temperature high (%alarmid). Power off aircraft and wait for temperature to return to normal before use |
| `0x1C000104` | Camera processor temperature too high (%alarmid). Power off aircraft and wait for temperature to return to normal before use |
| `0x1C000201` | Camera hardware error (%alarmid). Restart and try again |
| `0x1C000202` | Camera hardware error (%alarmid). Restart and try again |
| `0x1C000203` | Camera hardware error (%alarmid). Restart and try again |
| `0x1C000204` | Camera image sensor overheated (%alarmid). Check whether the vents at the back of the camera are blocked. Wait for temperature to return to normal before use. |
| `0x1C00020A` | Image sensor calibration data error (%alarmid). Restart aircraft. Contact DJI Support if issue persists |
| `0x1C000303` | Camera connection error (%alarmid). Check whether camera is installed properly. Do not press the lens release button when installing the lens. If the warning persists, contact your local dealer or DJI Support |
| `0x1C000305` | Shutter trigger count reached 100K design limit. Contact DJI Support for maintenance |
| `0x1C000306` | Currently using non-DJI Enterprise lens. Surveying accuracy is not guaranteed (%alarmid). Replace with a DJI Enterprise lens |
| `0x1C000317` | Lens calibration data error (%alarmid). Re-install lens or restart aircraft. Contact DJI Support if issue persists |
| `0x1C000401` | Invalid memory card. Replace card (%alarmid) |
| `0x1C000402` | Memory card speed low (%alarmid). Shots may be missed. Replace with faster card |
| `0x1C000403` | Replace memory card (%alarmid) |
| `0x1C000404` | Insert memory card or restart camera (%alarmid) |
| `0x1C000405` | Confirm memory card read and write permissions (%alarmid) |
| `0x1C00040E` | Memory card write speed low. Format card or restart camera |
| `0x1C00040F` | Memory card write speed low. Format card or restart camera |
| `0x1C000411` | SD card write error (%alarmid). Replace SD card |
| `0x1C000412` | Verification required before using memory card. Enter password to verify. Contact your local dealer or DJI Support if issue persists |
| `0x1C000414` | SD card storage severely fragmented. Back up files and format SD card (%alarmid) |
| `0x1C000602` | Ambient light too low (%alarmid). Check ambient light conditions and whether the lens cap is still on |
| `0x1C000603` | Photos may be underexposed (%alarmid). Make sure camera parameters such as EV, ISO, and aperture are properly configured |
| `0x1C000604` | Photos may be overexposed (%alarmid). Make sure camera parameters such as EV, ISO, and aperture are properly configured |
| `0x1C000901` | PPS signal sending error. Restart camera |
| `0x1C000902` | Camera time synchronization error. Restart camera |
| `0x1C000903` | Camera hardware error (%alarmid). Restart and try again |
| `0x1C000904` | Camera hardware error (%alarmid). Restart and try again |
| `0x1C000905` | Camera hardware error (%alarmid). Restart and try again |
| `0x1C000906` | Camera hardware error (%alarmid). Restart and try again |
| `0x1C000907` | Camera hardware error (%alarmid). Restart and try again |
| `0x1C000908` | Camera hardware error (%alarmid). Restart and try again |
| `0x1C000909` | Camera hardware error (%alarmid). Restart and try again |
| `0x1C00090A` | Camera hardware error (%alarmid). Restart and try again |
| `0x1C000B01` | Camera hardware error (%alarmid). Restart and try again |
| `0x1C000D01` | Focusing failed. Check and retry |
| `0x1C000D02` | Lens infinity focus not calibrated (%alarmid). Go to Camera Settings > Calibrate for infinity focus calibration |
| `0x1C000D03` | Infinity focus calibration data expired (%alarmid). Go to Camera Settings > Calibrate and recalibrate |
| `0x1C000D04` | Infinity focus calibration data expired. Recalibrate |
| `0x1C000E01` | Camera and lens intrinsic parameters calibration data do not match (%alarmid). Check whether devices are compatible. If not, calibration data is not applicable |
| `0x1C000E02` | Intrinsic parameters calibration data expired (%alarmid). Calibrate camera intrinsic parameters with DJI Terra |
| `0x1C001306` | System busy. Recording not allowed |
| `0x1C001307` | System not busy. Recording available |
| `0x1C001501` | Light sensor error (%alarmid). Contact DJI Support |
| `0x1C001502` | Light sensor error (%alarmid). Contact DJI Support |
| `0x1C001503` | Light sensor calibration data error (%alarmid). Contact DJI Support |
| `0x1C001E04` | System busy. Photo is not allowed |
| `0x1C001E05` | System not busy.Photo available |
| `0x1C001F01` | System busy. Zoom is not available |
| `0x1C001F02` | System not busy. Zoom available |
| `0x1C002001` | System busy. Do not switch cameras |
| `0x1C002002` | System not busy. Switching cameras allowed |
| `0x1C002004` | H20 camera image-sensor chip abnormal. Power-cycle the camera. If the issue persists, contact DJI After-Sales Service.+ |
| `0x1C002101` | Camera receiving LiDAR data timed out (%alarmid). Restart aircraft and try again |
| `0x1C002102` | Point cloud data frames dropped (%alarmid). The ultimate point cloud model may not be complete. Restart aircraft |
| `0x1C002103` | LiDAR may be blocked or object out of measuring range (%alarmid) |
| `0x1C002104` | RNG sampling failed. Try again later or restart aircraft (%alarmid). Contact DJI Support if issue persists |
| `0x1C002301` | EIS image-frame `vsync` is 0.+ |
| `0x1C002302` | EIS image-frame `vsync` order error.+ |
| `0x1C002303` | EIS unable to retrieve IMU data.+ |
| `0x1C002304` | EIS retrieved insufficient IMU data.+ |
| `0x1C002305` | EIS retrieved excessive IMU data.+ |
| `0x1C002306` | EIS failed to retrieve IMU data.+ |
| `0x1C002307` | EIS retrieved IMU-data `vsync` order error.+ |
| `0x1C002308` | EIS IMU target out of constraint range.+ |
| `0x1C002309` | EIS iterative solve result exceeds input image bounds.+ |
| `0x1C00230A` | EIS IMU alignment range exceeds position of retrieved IMU data.+ |
| `0x1C00230B` | EIS inter-frame interval problem — `vsync` unstable.+ |
| `0x1C00230C` | Current frame matched `vsync` information via step mode.+ |
| `0x1C00230D` | Current frame matched invalid `vsync` information.+ |
| `0x1C00230E` | Current frame cannot match `vsync` information.+ |
| `0x1C003001` | H20 lens abnormal. Power-cycle the camera. If the issue persists, contact DJI After-Sales Service.+ |
| `0x1C100001` | Camera %component_index overheated (%alarmid). Wait for temperature to return to normal before use |
| `0x1C100101` | Camera %component_index error (%alarmid). Restart camera. If the issue persists, contact your local dealer or DJI Support |
| `0x1C100102` | Camera %component_index error (%alarmid). Restart camera. If the issue persists, contact your local dealer or DJI Support |
| `0x1C100103` | Camera processor temperature high (%alarmid). Power off aircraft and wait for temperature to return to normal before use |
| `0x1C100104` | Camera processor temperature too high (%alarmid). Power off aircraft and wait for temperature to return to normal before use |
| `0x1C100105` | Camera %component_index error (%alarmid). Restart camera. If the issue persists, contact your local dealer or DJI Support |
| `0x1C100201` | H20 camera image transmission sensor processor error (%alarmid). Restart camera. If the issue persists, contact DJI Support |
| `0x1C100202` | H20 camera image transmission sensor processor error (%alarmid). Restart camera. If the issue persists, contact DJI Support |
| `0x1C100203` | Camera processor overheated (%alarmid). Power off aircraft and wait for temperature to return to normal before use |
| `0x1C100204` | H20 camera image transmission sensor processor error (%alarmid). Restart camera. If the issue persists, contact DJI Support |
| `0x1C100301` | H20 camera lens error (%alarmid). Restart camera. If the issue persists, contact DJI Support |
| `0x1C100302` | H20 camera lens error (%alarmid). Restart camera. If the issue persists, contact DJI Support |
| `0x1C100303` | H20 camera lens error (%alarmid). Restart camera. If the issue persists, contact DJI Support |
| `0x1C100304` | H20 camera lens error (%alarmid). Restart camera. If the issue persists, contact DJI Support |
| `0x1C100401` | Invalid memory card. Replace card (%alarmid) |
| `0x1C100402` | Memory card speed low (%alarmid). Shots may be missed. Replace with faster card |
| `0x1C100403` | Memory card error. Replace card (%alarmid) |
| `0x1C100404` | No memory card (%alarmid) |
| `0x1C100405` | Confirm memory card read and write permissions (%alarmid) |
| `0x1C100406` | Memory card not formatted. Format card before use (%alarmid) |
| `0x1C100407` | Formatting memory card (%alarmid)... |
| `0x1C100408` | Memory card file system not supported. Format card before use (%alarmid) |
| `0x1C100409` | Refreshing memory card (%alarmid)... |
| `0x1C10040A` | SD card full — clear storage+ |
| `0x1C10040B` | File naming index full. Format card and restart camera (%alarmid) |
| `0x1C10040C` | Initializing memory card (%alarmid)... |
| `0x1C10040D` | Memory card error. Format card before use (%alarmid) |
| `0x1C10040E` | Fixing memory card (%alarmid)... |
| `0x1C10040F` | Memory card read and write speed low (%alarmid). Wait until process completes |
| `0x1C200001` | Camera %component_index overheated (%alarmid). Wait for temperature to return to normal before use |
| `0x1C200101` | Camera %component_index error (%alarmid). Restart camera. If the issue persists, contact your local dealer or DJI Support |
| `0x1C200102` | Camera %component_index error (%alarmid). Restart camera. If the issue persists, contact your local dealer or DJI Support |
| `0x1C200103` | Camera processor temperature high (%alarmid). Power off aircraft and wait for temperature to return to normal before use |
| `0x1C200104` | Camera processor temperature too high (%alarmid). Power off aircraft and wait for temperature to return to normal before use |
| `0x1C200105` | Camera %component_index error (%alarmid). Restart camera. If the issue persists, contact your local dealer or DJI Support |
| `0x1C200201` | Camera %component_index error (%alarmid). Restart camera. If the issue persists, contact your local dealer or DJI Support |
| `0x1C200202` | Camera %component_index error (%alarmid). Restart camera. If the issue persists, contact your local dealer or DJI Support |
| `0x1C200203` | Camera processor overheated (%alarmid). Power off aircraft and wait for temperature to return to normal before use |
| `0x1C200204` | H20 camera image transmission sensor processor error (%alarmid). Restart camera. If the issue persists, contact DJI Support |
| `0x1C200301` | H20 camera lens error (%alarmid). Restart camera. If the issue persists, contact DJI Support |
| `0x1C200302` | H20 camera lens error (%alarmid). Restart camera. If the issue persists, contact DJI Support |
| `0x1C200303` | H20 camera lens error (%alarmid). Restart camera. If the issue persists, contact DJI Support |
| `0x1C200304` | H20 camera lens error (%alarmid). Restart camera. If the issue persists, contact DJI Support |
| `0x1C200401` | Invalid memory card. Replace card (%alarmid) |
| `0x1C200402` | Memory card speed low (%alarmid). Shots may be missed. Replace with faster card |
| `0x1C200403` | Memory card error. Replace card (%alarmid) |
| `0x1C200404` | No memory card (%alarmid) |
| `0x1C200405` | Confirm memory card read and write permissions (%alarmid) |
| `0x1C200406` | Memory card not formatted. Format card before use (%alarmid) |
| `0x1C200407` | Formatting memory card (%alarmid)... |
| `0x1C200408` | Memory card file system not supported. Format card before use (%alarmid) |
| `0x1C200409` | Refreshing memory card (%alarmid)... |
| `0x1C20040A` | SD card full — clear storage+ |
| `0x1C20040B` | File naming index full. Format card and restart camera (%alarmid) |
| `0x1C20040C` | Initializing memory card (%alarmid)... |
| `0x1C20040D` | Memory card error. Format card before use (%alarmid) |
| `0x1C20040E` | Fixing memory card (%alarmid)... |
| `0x1C20040F` | Memory card read and write speed low (%alarmid). Wait until process completes |
| `0x1C200410` | Verification required before using memory card (%alarmid). Enter password to verify |
| `0x1C300001` | Camera %component_index overheated (%alarmid). Wait for temperature to return to normal before use |
| `0x1C300101` | Camera %component_index error (%alarmid). Restart camera. If the issue persists, contact your local dealer or DJI Support |
| `0x1C300102` | Camera %component_index error (%alarmid). Restart camera. If the issue persists, contact your local dealer or DJI Support |
| `0x1C300103` | Camera processor temperature high (%alarmid). Power off aircraft and wait for temperature to return to normal before use |
| `0x1C300104` | Camera processor temperature too high (%alarmid). Power off aircraft and wait for temperature to return to normal before use |
| `0x1C300105` | Camera %component_index error (%alarmid). Restart camera. If the issue persists, contact your local dealer or DJI Support |
| `0x1C300301` | H20 camera lens error (%alarmid). Restart camera. If the issue persists, contact DJI Support |
| `0x1C300302` | H20 camera lens error (%alarmid). Restart camera. If the issue persists, contact DJI Support |
| `0x1C300303` | H20 camera lens error (%alarmid). Restart camera. If the issue persists, contact DJI Support |
| `0x1C300304` | H20 camera lens error (%alarmid). Restart camera. If the issue persists, contact DJI Support |
| `0x1C300401` | Invalid memory card. Replace card (%alarmid) |
| `0x1C300402` | Memory card speed low (%alarmid). Shots may be missed. Replace with faster card |
| `0x1C300403` | Memory card error. Replace card (%alarmid) |
| `0x1C300404` | No memory card (%alarmid) |
| `0x1C300405` | Confirm memory card read and write permissions (%alarmid) |
| `0x1C300406` | Memory card not formatted. Format card before use (%alarmid) |
| `0x1C300407` | Formatting memory card (%alarmid)... |
| `0x1C300408` | Memory card file system not supported. Format card before use (%alarmid) |
| `0x1C300409` | Refreshing memory card (%alarmid)... |
| `0x1C30040A` | Memory card full. Clear space |
| `0x1C30040B` | File naming index full. Format card and restart camera (%alarmid) |
| `0x1C30040C` | Initializing memory card (%alarmid)... |
| `0x1C30040D` | Memory card error. Format card before use (%alarmid) |
| `0x1C30040E` | Fixing memory card (%alarmid)... |
| `0x1C30040F` | Memory card read and write speed low (%alarmid). Wait until process completes |
| `0x1C300601` | Temperature of current environment too low (%alarmid). Only enable temperature measurement when temperature is between -20° C to 50° C. If the issue persists, contact DJI Support |
| `0x1C300602` | Temperature of current environment too high (%alarmid). Only enable temperature measurement when temperature is between -20° C to 50° C. If the issue persists, contact DJI Support |
| `0x1C300603` | Infrared thermal camera processor switching between high and low gain modes (%alarmid). Wait or restart camera after it cools down. If the issue persists, contact DJI Support |
| `0x1C300604` | Zenmuse H20T infrared thermal camera calibration data missing (%alarmid). Restart camera. If the issue persists, contact DJI Support |
| `0x1C300605` | Zenmuse H20T initialization error (%alarmid). Restart camera. If the issue persists, contact DJI Support |
| `0x1C300606` | Temperature measurement failed (%alarmid). Adjust camera parameters and try again or restart camera. If the issue persists, contact DJI Support |
| `0x1C300607` | Exceeded measuring range limit. Switch to Low Gain mode |
| `0x1C300608` | Exceeded measuring range limit. It is recommended to attach an infrared density filter |
| `0x1C300609` | Exceeded temperature measuring range limit (%alarmid) |
| `0x1C300701` | Sun detected. Infrared shutter closed to prevent damage to sensor (%alarmid). Rotate gimbal and shutter will be automatically open when sun is not detected in camera view |
| `0x1C300702` | Sun detected. Rotate gimbal to avoid direct sunlight and prevent damage to sensor (%alarmid) |

<details><summary>CN source (verbatim from HMS.json)</summary>

| Alarm ID | `tipEn` (original CN) |
|---|---|
| `0x1C002004` | H20 相机图像传感器芯片异常，请断电重启相机。若仍无法解决问题，请联系大疆售后服务。 |
| `0x1C002301` | EIS的图像帧的vsync为0. |
| `0x1C002302` | EIS图像帧的vsync顺序错误. |
| `0x1C002303` | EIS获取不到IMU数据. |
| `0x1C002304` | EIS获取IMU数据不足. |
| `0x1C002305` | EIS获取IMU数据过多. |
| `0x1C002306` | EIS获取IMU数据失败. |
| `0x1C002307` | EIS获取到的IMU数据vsync顺序错误. |
| `0x1C002308` | EIS的IMU target超出约束范围. |
| `0x1C002309` | EIS迭代求解结果超出输入图像的边界. |
| `0x1C00230A` | EIS的IMU对齐范围超出拿到的IMU数据的位置 . |
| `0x1C00230B` | EIS帧间时间间隔有问题，vsync不稳定. |
| `0x1C00230C` | 当前帧通过step模式匹配到了vsync信息. |
| `0x1C00230D` | 当前帧匹配到无效的vsync信息. |
| `0x1C00230E` | 当前帧匹配不到vsync信息. |
| `0x1C003001` | H20 镜头异常，请断电重启相机。若仍无法解决问题，请联系大疆售后服务。 |
| `0x1C10040A` | SD卡已满，请清除内存 |
| `0x1C20040A` | SD卡已满，请清除内存 |

</details>

---

**Source**: [`DJI_Cloud/HMS.json`](../../DJI_Cloud/HMS.json) (DJI v1.15 authoritative).

**See also**: 
- Event definition — [`mqtt/dock-to-cloud/events/hms.md`](../mqtt/dock-to-cloud/events/hms.md).
- Topic-level overview — [`mqtt/README.md`](../mqtt/README.md).
- General API error codes (distinct from HMS alarms) — [`error-codes/README.md`](../error-codes/README.md).
