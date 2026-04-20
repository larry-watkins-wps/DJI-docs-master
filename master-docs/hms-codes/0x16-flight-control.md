# HMS codes — 0x16** (Flight-control system)

Prefix byte `0x16`. 921 alarm codes.

The prefix byte is the wire-level grouping DJI uses in the `data.list[].code` field emitted on [`thing/product/{gateway_sn}/events` method `hms`](../mqtt/dock-to-cloud/events/hms.md). The domain label above is inferred from the tip text — DJI does not publish an official prefix taxonomy.

Entries rendered with a trailing **+** have a curated CN→EN translation because the original `tipEn` value in [`HMS.json`](../../DJI_Cloud/HMS.json) contains Chinese-language developer-debug strings under the "English" field. The CN originals are preserved below each subsection in a `CN source` callout so the audit trail is intact.

## 0x1600** — Flight controller (2 codes)

| Alarm ID | Tip |
|---|---|
| `0x16000001` | Flight controller overloaded. Land and restart aircraft promptly (%alarmid) |
| `0x16000002` | Flight data recording error (%alarmid). Contact your local dealer or DJI Support |

## 0x1601** — Sensor system (27 codes)

| Alarm ID | Tip |
|---|---|
| `0x16010001` | Sensor system error (%alarmid). Restart aircraft |
| `0x16010005` | Sensor system error (%alarmid). Land promptly |
| `0x16010007` | Sensor system error (%alarmid). Land promptly |
| `0x1601000A` | Sensor system error (%alarmid). Restart aircraft |
| `0x1601000D` | Sensor system error (%alarmid). Restart aircraft |
| `0x16010010` | Sensor system error (%alarmid). Restart aircraft |
| `0x16010013` | Sensor system error (%alarmid). Restart aircraft |
| `0x16010016` | Sensor system error (%alarmid). Restart aircraft |
| `0x16010019` | Sensor system error (%alarmid). Restart aircraft |
| `0x1601001C` | Sensor system error (%alarmid). Restart aircraft |
| `0x1601001F` | Sensor system error (%alarmid). Restart aircraft |
| `0x16010022` | Sensor system error (%alarmid). Restart aircraft |
| `0x16010025` | Sensor system error (%alarmid). Restart aircraft |
| `0x16010026` | Unable to take off. Non-DJI RTK module detected (%alarmid). Use official module |
| `0x16010028` | Sensor system error (%alarmid). Restart aircraft |
| `0x1601002B` | Sensor system error (%alarmid). Restart aircraft |
| `0x1601002F` | Sensor system error (%alarmid). Restart aircraft |
| `0x16010032` | Sensor system error (%alarmid). Restart aircraft |
| `0x16010033` | Vision positioning detection poor. Fly with caution (%alarmid) |
| `0x16010034` | GNSS detection poor. Fly with caution (%alarmid) |
| `0x16010035` | Positioning quality poor. Fly with caution (%alarmid) |
| `0x16010036` | Vision positioning detection poor. Fly with caution (%alarmid) |
| `0x16010037` | GNSS detection poor. Fly with caution (%alarmid) |
| `0x16010038` | Positioning quality poor. Fly with caution (%alarmid) |
| `0x16010041` | Sensor system error (%alarmid). Restart aircraft |
| `0x16010042` | Severe error in aircraft positioning system (%alarmid). Aircraft will automatically land soon. Fly aircraft to open area promptly |
| `0x16010050` | Currently using LiDAR positioning only. Do not fly in narrow corridors, tunnels, or similar environments (%alarmid)+ |

<details><summary>CN source (verbatim from HMS.json)</summary>

| Alarm ID | `tipEn` (original CN) |
|---|---|
| `0x16010050` | 当前仅使用激光雷达定位，请勿在狭窄走廊、隧道等环境飞行(%alarmid) |

</details>

## 0x1602** — Tachometer (12 codes)

| Alarm ID | Tip |
|---|---|
| `0x16020001` | Tachometer error (%alarmid). Restart aircraft |
| `0x16020004` | Tachometer error (%alarmid). Restart aircraft |
| `0x16020007` | Tachometer error (%alarmid). Restart aircraft |
| `0x1602000A` | Tachometer error (%alarmid). Restart aircraft |
| `0x1602000D` | Tachometer error (%alarmid). Restart aircraft |
| `0x16020016` | IMU error (%alarmid). Calibrate IMU |
| `0x16020027` | Tachometer error (%alarmid). Restart aircraft |
| `0x1602002A` | Tachometer error (%alarmid). Restart aircraft |
| `0x1602002B` | Gyroscope thermal control abnormal. Constant temperature cannot be guaranteed+ |
| `0x16020620` | RTH canceled. Obstacle detected (%alarmid) |
| `0x16020621` | RTH canceled. Strong wind or aircraft approaching GEO Zone (%alarmid) |
| `0x16020622` | GNSS error (%alarmid). RTH canceled. Fly aircraft to open area |

<details><summary>CN source (verbatim from HMS.json)</summary>

| Alarm ID | `tipEn` (original CN) |
|---|---|
| `0x1602002B` | 陀螺温度控制异常，无法保证恒温 |

</details>

## 0x1603** — Accelerometer (10 codes)

| Alarm ID | Tip |
|---|---|
| `0x16030001` | Accelerometer error (%alarmid). Restart aircraft |
| `0x16030004` | Accelerometer error (%alarmid). Restart aircraft |
| `0x16030007` | Accelerometer error (%alarmid). Restart aircraft |
| `0x1603000A` | Accelerometer error (%alarmid). Restart aircraft |
| `0x1603000D` | Accelerometer error (%alarmid). Restart aircraft |
| `0x16030010` | Accelerometer error (%alarmid). Restart aircraft |
| `0x16030013` | Accelerometer error (%alarmid). Restart aircraft |
| `0x16030016` | IMU error (%alarmid). Calibrate IMU |
| `0x1603001C` | Accelerometer error (%alarmid). Restart aircraft |
| `0x1603001D` | Abnormal aircraft vibration. Return to home or land promptly. Check propellers and PSDK status |

## 0x1604** — Barometer (8 codes)

| Alarm ID | Tip |
|---|---|
| `0x16040001` | Barometer error (%alarmid). Restart aircraft |
| `0x16040004` | Barometer error (%alarmid). Restart aircraft |
| `0x16040007` | Barometer error (%alarmid). Restart aircraft |
| `0x1604000A` | Barometer error (%alarmid). Restart aircraft |
| `0x16040010` | Barometer error (%alarmid). Restart aircraft |
| `0x16040013` | Barometer error (%alarmid). Restart aircraft |
| `0x16040016` | Barometer error (%alarmid). Restart aircraft |
| `0x16040019` | Barometer error (%alarmid). Restart aircraft |

## 0x1605** — GNSS (8 codes)

| Alarm ID | Tip |
|---|---|
| `0x16050001` | GNSS error (%alarmid). Restart aircraft |
| `0x16050004` | GNSS error (%alarmid). Restart aircraft |
| `0x16050019` | GNSS error (%alarmid). Restart aircraft |
| `0x1605001C` | GNSS error (%alarmid). Restart aircraft |
| `0x1605001F` | Strong GNSS signal interference (%alarmid). Fly with caution. Move away from source of interference. Return to home or land promptly if issue persists |
| `0x16050020` | Strong GNSS interference. Return to home promptly |
| `0x16050021` | RTK not converged. Place aircraft in an open area and start task after RTK converged |
| `0x1605002B` | Flight controller overheats (%alarmid). Returning to home automatically. Fly with caution. Check aircraft fan after landing |

## 0x1606** — Compass (5 codes)

| Alarm ID | Tip |
|---|---|
| `0x16060001` | Compass error (%alarmid). Restart aircraft |
| `0x16060007` | Compass error (%alarmid). Restart aircraft |
| `0x1606000A` | Compass error (%alarmid). Restart aircraft |
| `0x1606000D` | Compass interference (%alarmid). Move away from interference source or calibrate compass |
| `0x16060010` | Compass interference (%alarmid). Move away from interference source or calibrate compass |

## 0x1607** — RTK (27 codes)

| Alarm ID | Tip |
|---|---|
| `0x16070001` | Flight controller overheats (%alarmid). Returning to home. Fly with caution. Check aircraft fan after landing |
| `0x16070002` | Flight controller overheats (%alarmid). Landing automatically. Fly with caution. Check aircraft fan after landing |
| `0x16070003` | RTH canceled. Control stick pushed down (%alarmid) |
| `0x16070020` | Check RTK base station status and restart aircraft (%alarmid). If the issue persists, contact your local dealer or DJI Support |
| `0x16070021` | Check RTK base station status and restart aircraft (%alarmid). If the issue persists, contact your local dealer or DJI Support |
| `0x16070022` | RTK dual-antenna installation error+ |
| `0x16070023` | RTK device error (%alarmid). Fly with caution |
| `0x16070024` | RTK device error (%alarmid). Fly with caution |
| `0x16070025` | Check RTK base station status and restart aircraft (%alarmid). If the issue persists, contact your local dealer or DJI Support |
| `0x16070026` | Check RTK base station status and restart aircraft (%alarmid). If the issue persists, contact your local dealer or DJI Support |
| `0x16070027` | Check RTK base station status and restart aircraft (%alarmid). If the issue persists, contact your local dealer or DJI Support |
| `0x16070028` | Check RTK base station status and restart aircraft (%alarmid). If the issue persists, contact your local dealer or DJI Support |
| `0x16070029` | Check RTK base station status and restart aircraft (%alarmid). If the issue persists, contact your local dealer or DJI Support |
| `0x16070030` | Update D-RTK 2 mobile station and aircraft to latest firmware versions. If the issue persists, contact your local dealer or DJI Support |
| `0x16070031` | Restart aircraft (%alarmid) or disable RTK function in RTK Settings and enable RTK again |
| `0x16070032` | Check RTK base station status and restart aircraft (%alarmid). If the issue persists, contact your local dealer or DJI Support |
| `0x16070033` | Check RTK base station status and restart aircraft. If the issue persists, contact your local dealer or DJI Support |
| `0x16070034` | RTK device error (%alarmid). Fly with caution |
| `0x16070035` | RTK device error. Fly with caution |
| `0x16070036` | RTK antennas disconnected. Return to home or land promptly (%alarmid). Contact DJI Support for repairs |
| `0x16070037` | RTK dongle certification error (%alarmid). Use official DJI RTK dongle |
| `0x16070038` | RTK primary-antenna signal abnormal+ |
| `0x16070039` | RTK secondary-antenna signal abnormal+ |
| `0x16070040` | RTK not converged. Place aircraft in an open area and start task after RTK converged |
| `0x16070042` | RTK base station data error (%alarmid). Check if network RTK or D-RTK is connected |
| `0x16070043` | GNSS is interfered with error signal. Fly with caution or return to home |
| `0x16070044` | GNSS is receiving false signal. Return to home or land promptly |

<details><summary>CN source (verbatim from HMS.json)</summary>

| Alarm ID | `tipEn` (original CN) |
|---|---|
| `0x16070022` | RTK双天线安装错误 |
| `0x16070038` | RTK主天线信号异常 |
| `0x16070039` | RTK副天线信号异常 |

</details>

## 0x1608** — Motors & ESC (64 codes)

| Alarm ID | Tip |
|---|---|
| `0x16080020` | Motor stalled (%alarmid). Land immediately and check whether motor is blocked |
| `0x16080021` | ESC short-circuited (%alarmid). Land immediately and restart aircraft |
| `0x16080022` | Motor overloaded (%alarmid). Land immediately and check whether motor and propellers are blocked, or aircraft is overloaded |
| `0x16080023` | Motor communication error (%alarmid). Land aircraft immediately |
| `0x16080024` | Motor over-accelerating (%alarmid). Stop pressing control stick |
| `0x16080025` | Motor communication error (%alarmid). Land aircraft promptly |
| `0x16080026` | Motor communication error (%alarmid). Land aircraft promptly |
| `0x16080027` | Motor communication error (%alarmid). Land aircraft promptly |
| `0x16080028` | Motor communication error (%alarmid). Land aircraft promptly |
| `0x16080029` | Motor propeller detached, propeller not installed, or motor underloaded (%alarmid). Land aircraft immediately |
| `0x1608002A` | ESC overheated (%alarmid). Wait for aircraft to cool down before flying |
| `0x1608002B` | ESC overheated (%alarmid). Wait for aircraft to cool down before flying |
| `0x1608002C` | ESC voltage too high (%alarmid). Land aircraft immediately |
| `0x1608002D` | ESC voltage too low (%alarmid). Return to home promptly and replace battery |
| `0x1608002E` | ESC flash memory error (%alarmid). Unable to turn on propellers |
| `0x1608002F` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x16080030` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x16080031` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x16080032` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x16080033` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x16080034` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x16080035` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x16080036` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x16080037` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x16080038` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x16080039` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x1608003a` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x1608003b` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x1608003c` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x1608003d` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x1608003e` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x1608003f` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x16080040` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x16080041` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x16080042` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x16080043` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x16080044` | ESC voltage too high (%alarmid). Unable to turn on propellers. Check and ensure current battery level is sufficient |
| `0x16080045` | ESC voltage too high (%alarmid). Unable to turn on propellers. Check and ensure battery is installed correctly |
| `0x16080046` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x16080047` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x16080048` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x16080049` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x1608004a` | ESC overheated (%alarmid). Check and ensure temperature of current environment is within normal range |
| `0x1608004b` | ESC temperature too low (%alarmid). Check and ensure temperature of current environment is within normal range |
| `0x1608004c` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x1608004d` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x1608004e` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x1608004f` | ESC auto-check error (%alarmid). Unable to turn on propellers. Restart aircraft |
| `0x16080050` | ESC error (%alarmid). Unable to take off. Restart aircraft and try again. Contact DJI Support if the issue persists |
| `0x16080051` | ESC error (%alarmid). Unable to take off. Restart aircraft and try again. Contact DJI Support if the issue persists |
| `0x16080052` | Propulsion system error and propellers folded (%alarmid). Check propellers and restart aircraft. Contact DJI Support if the issue persists |
| `0x16080053` | ESC error (%alarmid). Restart aircraft. Contact DJI Support if the issue persists |
| `0x16080054` | ESC error (%alarmid). Unable to take off. Restart aircraft and try again. Contact DJI Support if the issue persists |
| `0x16080055` | Motor %index overheated (%alarmid). Reduce flight speed and land aircraft immediately. Restart aircraft after motor cools down. Contact DJI Support if issue persists |
| `0x16080056` | Motor %index overheated (%alarmid). Aircraft may be auto landing. Fly with caution and land aircraft immediately. Restart aircraft after motor cools down. Contact DJI Support if issue persists |
| `0x16080057` | ESC error (%alarmid). Unable to take off. Restart aircraft and try again. Contact DJI Support if the issue persists |
| `0x16080058` | ESC error (%alarmid). Unable to take off. Restart aircraft and try again. Contact DJI Support if the issue persists |
| `0x16080059` | ESC error (%alarmid). Unable to take off. Restart aircraft and try again. Contact DJI Support if the issue persists |
| `0x1608005A` | ESC error. Unable to take off. Contact DJI Support |
| `0x1608005B` | ESC error (%alarmid). Unable to take off. Restart aircraft and try again. Contact DJI Support if the issue persists |
| `0x1608005C` | ESC error (%alarmid). Unable to take off. Restart aircraft and try again. Contact DJI Support if the issue persists |
| `0x1608005D` | ESC error (%alarmid). Unable to take off. Restart aircraft and try again. Contact DJI Support if the issue persists |
| `0x1608005E` | ESC %index auto-check error (%alarmid) |
| `0x1608005F` | Motor %index overheated (%alarmid). Attitude error. Aircraft auto landing. Restart aircraft after motor cools down. Contact DJI Support if issue persists |

## 0x1609** — Battery (97 codes)

| Alarm ID | Tip |
|---|---|
| `0x16090020` | 1. Re-insert the battery and confirm there is no foreign matter in the battery connector. 2. Swap in a different battery to test whether the battery is damaged. 3. Check whether the power-distribution board gold-finger contacts are deformed or fouled. 4. With the aircraft powered off, verify that the connections between the power-distribution board, the distribution module, and the avionics module are normal. 5. If the issue persists, contact your nearest dealer or DJI After-Sales Service.+ |
| `0x16090021` | 1. Confirm the battery is an official DJI battery. 2. Check whether the power-distribution board gold-finger contacts are deformed or fouled. 3. Re-insert the battery and confirm there is no foreign matter in the battery connector. 4. Swap in a different battery to test whether the battery is damaged. 5. If the issue persists, contact your nearest dealer or DJI After-Sales Service.+ |
| `0x16090022` | 1. Check whether any battery cell voltage is abnormal. 2. If the issue persists, contact your nearest dealer or DJI After-Sales Service.+ |
| `0x16090023` | Return to home or land promptly |
| `0x16090024` | Return to home or land promptly |
| `0x16090025` | Return to home or land promptly |
| `0x16090026` | Return to home or land promptly |
| `0x16090027` | 1. Return to home or land as soon as possible. 2. Check whether any battery cell voltage is abnormal. 3. If the issue persists, contact your nearest dealer or DJI After-Sales Service.+ |
| `0x16090028` | 1. Return to home or land as soon as possible. 2. Check whether any battery cell voltage is abnormal. 3. If the issue persists, contact your nearest dealer or DJI After-Sales Service.+ |
| `0x16090029` | 1. Return to home or land as soon as possible. 2. Check whether a battery cell is damaged and whether the voltage is normal. 3. If the issue persists, contact your nearest dealer or DJI After-Sales Service.+ |
| `0x1609002A` | 1. Check whether the aircraft is carrying additional payload. 2. If the issue persists, contact your nearest dealer or DJI After-Sales Service.+ |
| `0x1609002B` | 1. Return to home or land as soon as possible. 2. Wait for the battery temperature to drop before resuming use.+ |
| `0x1609002C` | Battery temperature too low. Warm up battery and take off after battery is fully charged |
| `0x1609002D` | 1. Return to home or land as soon as possible. 2. Re-insert the battery and confirm there is no foreign matter in the battery connector. 3. Confirm the flight-environment temperature is normal. 4. Swap in a different battery to test whether the battery is at fault. 5. If the issue persists, contact your nearest dealer or DJI After-Sales Service.+ |
| `0x1609002E` | 1. Return to home or land as soon as possible. 2. Re-insert the battery and confirm there is no foreign matter in the battery connector. 3. Confirm the flight-environment temperature is normal. 4. Swap in a different battery to test whether the battery is at fault. 5. If the issue persists, contact your nearest dealer or DJI After-Sales Service.+ |
| `0x1609002F` | 1. Confirm the battery is an official DJI battery. 2. Re-insert the battery and confirm there is no foreign matter in the battery connector. 3. Swap in a different battery to test whether the battery is at fault. 4. If the issue persists, contact your nearest dealer or DJI After-Sales Service.+ |
| `0x16090030` | 1. Confirm the battery is an official DJI battery. 2. Re-insert the battery and confirm there is no foreign matter in the battery connector. 3. Swap in a different battery to test whether the battery is at fault. 4. If the issue persists, contact your nearest dealer or DJI After-Sales Service.+ |
| `0x16090031` | 1. Return to home or land as soon as possible. 2. Update to the latest firmware. 3. Check whether a battery cell is damaged and whether the voltage is normal. 4. If the issue persists, contact your nearest dealer or DJI After-Sales Service.+ |
| `0x16090032` | 1. Battery has aged. 2. Charge to full and reduce the payload before flying, and lower the flight speed. 3. To ensure flight safety, replacement with a new battery is recommended.+ |
| `0x16090033` | 1. Return to home as soon as possible. 2. Charge the battery to full before flying again. 3. Check whether any cell is damaged. 4. If the issue persists, contact your nearest dealer or DJI After-Sales Service.+ |
| `0x16090034` | 1. Battery current too high — aircraft auto-landing triggered. 2. Reduce spray load or replace the battery. 3. If the issue persists, contact your nearest dealer or DJI After-Sales Service.+ |
| `0x16090035` | 1. Battery current too high — aircraft performance limited. Move the control sticks gently and fly with caution. 2. Reduce spray load or replace the battery. 3. If the issue persists, contact your nearest dealer or DJI After-Sales Service.+ |
| `0x16090036` | 1. Battery current too high — aircraft auto-landing. 2. Reduce spray load or replace the battery. 3. If the issue persists, contact your nearest dealer or DJI After-Sales Service.+ |
| `0x16090038` | 1. Battery power too high — aircraft performance limited. Move the control sticks gently and fly with caution. 2. Reduce spray load or replace the battery. 3. If the issue persists, contact your nearest dealer or DJI After-Sales Service.+ |
| `0x16090039` | 1. Battery power too high — aircraft auto-landing triggered. 2. Reduce spray load or replace the battery. 3. If the issue persists, contact your nearest dealer or DJI After-Sales Service.+ |
| `0x16090050` | %battery_index Battery power supply error (%alarmid). Return to home or land promptly |
| `0x16090051` | %battery_index Battery power supply error (%alarmid). Return to home or land promptly |
| `0x16090052` | %battery_index Battery temperature sensor error (%alarmid). Return to home or land promptly |
| `0x16090060` | 1. Return to home or land as soon as possible — battery temperature sensor abnormal. 2. Battery temperature sensor fault. This battery cannot continue to be used. Stop using it and contact your nearest dealer or DJI After-Sales Service.+ |
| `0x16090061` | %battery_index Battery overheated (%alarmid). Return to home or land promptly |
| `0x16090062` | %battery_index Battery MOS temperature too high (%alarmid). Return to home or land promptly |
| `0x16090063` | %battery_index Battery voltage too high (%alarmid). Return to home or land promptly |
| `0x16090064` | %battery_index Battery voltage too low (%alarmid). Return to home or land promptly |
| `0x16090065` | %battery_index Battery single cell voltage too high (%alarmid). Return to home or land promptly |
| `0x16090066` | %battery_index Battery single cell voltage too low (%alarmid). Return to home or land promptly |
| `0x16090067` | Large static voltage difference between %battery_index Battery cells (%alarmid). Stop using battery |
| `0x16090068` | Large charge voltage difference between %battery_index Battery cells (%alarmid). Return to home or land promptly. Stop using battery |
| `0x16090069` | Large discharge voltage difference between %battery_index Battery cells (%alarmid). Return to home or land promptly. Stop using battery |
| `0x1609006A` | %battery_index Battery MOS connection error (%alarmid). Return to home or land promptly |
| `0x1609006B` | %battery_index Battery MOS impedance error (%alarmid). Return to home or land promptly |
| `0x1609006C` | %battery_index Battery aging (%alarmid). Flight safety may be affected |
| `0x1609006D` | %battery_index Battery experienced micro short circuit (%alarmid). Flight safety may be affected |
| `0x1609006F` | %battery_index Battery connector temperature too high (%alarmid). Return to home or land promptly |
| `0x16090070` | %battery_index Battery voltage too low (%alarmid). Return to home or land promptly |
| `0x16090072` | %battery_index Battery overcurrent when charging (%alarmid). Check charging device |
| `0x16090073` | %battery_index Battery overcurrent when discharging (%alarmid). Check if aircraft is overloaded |
| `0x16090074` | %battery_index Battery over discharged (%alarmid). Check if aircraft is overloaded |
| `0x16090075` | %battery_index Battery system error (%alarmid). Restart %battery_index Battery and try again |
| `0x16090076` | %battery_index Battery internal module error (%alarmid). Return to home or land promptly |
| `0x16090077` | %battery_index Battery charging temperature too high (%alarmid). Stop charging |
| `0x16090078` | %battery_index Battery discharging temperature too high (%alarmid). Return to home or land promptly |
| `0x16090079` | %battery_index Battery charging temperature too low (%alarmid). Stop charging |
| `0x1609007A` | %battery_index Battery discharging temperature too low (%alarmid). Return to home or land promptly |
| `0x1609007B` | %battery_index Battery voltage too high (%alarmid). Reinstall %battery_index Battery before takeoff |
| `0x1609007C` | %battery_index Battery voltage too low (%alarmid). Reinstall %battery_index Battery before takeoff |
| `0x1609007D` | Charging device voltage too high (%alarmid). Check device |
| `0x1609007E` | Charging device voltage too low (%alarmid). Check device |
| `0x1609007F` | %battery_index Battery overheated (%alarmid). Unable to take off |
| `0x16090080` | %battery_index Battery overheated (%alarmid). Return to home or land promptly |
| `0x16090081` | %battery_index Battery overheated (%alarmid). Return to home or land promptly |
| `0x16090082` | %battery_index Battery internal communication error (%alarmid). Return to home or land promptly |
| `0x16090083` | %battery_index Battery internal communication error (%alarmid). Return to home or land promptly |
| `0x16090084` | %battery_index Battery internal communication error (%alarmid). Return to home or land promptly |
| `0x16090085` | %battery_index Battery external communication error (%alarmid). Return to home or land promptly |
| `0x16090086` | %battery_index Battery connector overheated. Flight safety affected |
| `0x16090093` | %battery_index Battery voltage unstable (%alarmid). Return to home or land promptly. Restart aircraft after landing |
| `0x16090094` | %battery_index Battery voltage sensor error (%alarmid). Return to home or land promptly. Check if battery is water-damaged, connector corroded, or other damage occurred |
| `0x16090095` | %battery_index Battery voltage too high (%alarmid). Return to home or land promptly. Restart aircraft after landing |
| `0x16090096` | %battery_index Battery maintenance required (%alarmid). Fly with caution. It is recommended to replace with new battery and maintain %battery_index Battery |
| `0x16090097` | %battery_index battery maintenance required (%alarmid). Fly with caution. It is recommended to replace %battery_index battery and perform maintenance |
| `0x16090099` | %battery_index Battery overcurrent (%alarmid). Fly with caution. Check if payloads are working normally after landing |
| `0x1609009B` | %battery_index Battery temperature high (%alarmid). Return to home or land promptly |
| `0x1609009C` | %battery_index Battery temperature high (%alarmid). Return to home or land promptly |
| `0x1609009D` | %battery_index Battery connector overheated |
| `0x1609009E` | %battery_index Battery voltage high (%alarmid). Return to home or land promptly |
| `0x1609009F` | %battery_index Battery voltage low (%alarmid). Return to home or land promptly |
| `0x160900A6` | %battery_index Battery connection error (%alarmid). Return to home or land promptly |
| `0x160900B0` | %battery_index Battery level incorrect (%alarmid). Return to home or land promptly |
| `0x160900B1` | %battery_index Battery level unstable (%alarmid). Return to home or land promptly |
| `0x160900B3` | %battery_index Battery capacity error (%alarmid). Fly with caution. It is recommended to replace with new battery and maintain %battery_index Battery |
| `0x160900B4` | %battery_index Battery capacity too low (%alarmid). Fly with caution. It is recommended to replace with new battery and maintain %battery_index Battery |
| `0x160900B5` | %battery_index Battery capacity error (%alarmid). Fly with caution. It is recommended to replace with new battery and maintain %battery_index Battery |
| `0x160900B6` | %battery_index Battery capacity too low (%alarmid). Fly with caution. It is recommended to replace with new battery and maintain %battery_index Battery |
| `0x160900B7` | %battery_index Battery capacity error (%alarmid). Fly with caution. It is recommended to replace with new battery and maintain %battery_index Battery |
| `0x160900B8` | %battery_index Battery capacity error (%alarmid). Fly with caution. It is recommended to replace with new battery and maintain %battery_index Battery |
| `0x160900B9` | %battery_index Battery capacity not updated for extended period (%alarmid). Maintenance required. Fly with caution |
| `0x160900BA` | %battery_index Battery capacity not updated for extended period (%alarmid). Maintenance required. Fly with caution |
| `0x160900BB` | %battery_index Battery degraded (%alarmid). Fly with caution. It is recommended to replace with new battery and maintain %battery_index Battery |
| `0x160900BD` | %battery_index Battery aging (%alarmid). Flight safety may be affected |
| `0x160900BE` | %battery_index Battery aging (%alarmid). Flight safety may be affected |
| `0x160900BF` | %battery_index Battery approaching cycle count limit (%alarmid). It is recommended to replace with new battery and maintain %battery_index Battery |
| `0x160900C0` | %battery_index Battery rated power exceeded (%alarmid). Performance limited |
| `0x160900C3` | Battery approaching cycle count limit (%alarmid). Continuing use will pose safety risks. Replace battery recommended |
| `0x160900C4` | %battery_index battery level calibration required (%alarmid). Let battery sit for 2 hours to restore |
| `0x160900D2` | %battery_index battery level not calibrated for a long time (%alarmid). Let battery sit for 1 hour before calibration |
| `0x160900D5` | Unable to take off: Battery reached end of lifespan. Replace battery |
| `0x160900D6` | Battery SOHc low. Battery will reach end of lifespan after 20 cycles or days. Replace battery promptly |

<details><summary>CN source (verbatim from HMS.json)</summary>

| Alarm ID | `tipEn` (original CN) |
|---|---|
| `0x16090020` | 1.请重新插拔电池并确认电池接口无异物；\n2.请更换电池测试确认是否电池损坏；\n3.请检查分电板的金手指是否有变形、污损；\n4.请在关机状态下检查分电板-分线模块-航电模块之间的连接是否正常；\n5.若仍存在该问题，请联系就近代理商或DJI         大疆创新售后服务。\n |
| `0x16090021` | 1.请确认是否为官方电池；\n2.请检查分电板的金手指是否有变形、污损；\n3.请重新插拔电池并确认电池接口无异物；\n4.请更换电池测试确认是否电池损坏；\n5.若仍存在该问题，请联系就近代理商或DJI         大疆创新售后\n |
| `0x16090022` | 1.请确认电池各电芯电压是否有异常；\n2.若仍存在该问题，请联系就近代理商或DJI 大疆创新售后\n |
| `0x16090027` | 1.请尽快返航或降落；\n2.请确认电池各电芯电压是否有异常；\n3.若仍存在该问题，请联系就近代理商或DJI         大疆创新售后服务。\n |
| `0x16090028` | 1.请尽快返航或降落；\n2.请确认电池各电芯电压是否有异常；\n3.若仍存在该问题，请联系就近代理商或DJI         大疆创新售后服务。\n |
| `0x16090029` | 1.请尽快返航或降落；         \n2.请确认电池电芯是否有损坏，电压是否正常；\n3.若仍存在该问题，请联系就近代理商或DJI 大疆创新售后服务。\n |
| `0x1609002A` | 1.请检查飞机是否有额外负载；\n2.若仍存在该问题，请联系就近代理商或DJI 大疆创新售后服务。\n |
| `0x1609002B` | 1.请尽快返航或降落；\n2.请等待电池温度降低后再使用。\n |
| `0x1609002D` | 1.请尽快返航或降落；\n2.请重新插拔电池并确认电池接口无异物；\n3.请确认飞行环境温度是否正常；\n4.请更换电池测试确认是否电池问题；\n5.若仍存在该问题，请联系就近代理商或DJI         大疆创新售后服务。\n |
| `0x1609002E` | 1.请尽快返航或降落；\n2.请重新插拔电池并确认电池接口无异物；\n3.请确认飞行环境温度是否正常；\n4.请更换电池测试确认是否电池问题；\n5.若仍存在该问题，请联系就近代理商或DJI         大疆创新售后服务。\n |
| `0x1609002F` | 1.请确认电池是否为官方电池；\n2.请重新插拔电池并确认电池接口无异物；\n3.请更换电池测试确认是否电池问题；\n4.若仍存在该问题，请联系就近代理商或DJI         大疆创新售后服务。\n |
| `0x16090030` | 1.请确认电池是否为官方电池；\n2.请重新插拔电池并确认电池接口无异物；\n3.请更换电池测试确认是否电池问题；\n4.若仍存在该问题，请联系就近代理商或DJI         大疆创新售后服务。\n |
| `0x16090031` | 1.请尽快返航或降落；\n2.请升级最新固件版本；\n3.请确认电池电芯是否有损坏，电压是否正常；\n4.若仍存在该问题，请联系就近代理商或DJI 大疆创新售后服务。\n |
| `0x16090032` | 1.电池已老化；\n2.请充满电减少载重后再飞行，并调低飞行速度；\n3.为了保证飞行安全，建议您更换新的电池。\n |
| `0x16090033` | 1.请尽快返航\n2.请充满电后再飞行；\n3.请检查电芯是否有损坏；\n4.若仍存在该问题，请联系就近代理商或DJI 大疆创新售后服务。\n |
| `0x16090034` | 1.电池电流过大，导致自动降落；\n2.请减少载药量或更换电池；\n3.若仍存在该问题，请联系就近代理商或DJI         大疆创新售后服务。\n |
| `0x16090035` | 1.电池电流过大，已限制飞行器性能，请轻柔打杆，注意飞行安全；\n2.请减少载药量或更换电池； \n3.若仍存在该问题，请联系就近代理商或DJI 大疆创新售后服务。\n |
| `0x16090036` | 1.电池电流过大，自动降落；\n2.请减少载药量或更换电池；\n3.若仍存在该问题，请联系就近代理商或DJI         大疆创新售后服务。\n |
| `0x16090038` | 1.电池功率过大，已限制飞行器性能，请轻柔打杆，注意飞行安全；\n2.请减少载药量或更换电池；\n3.若仍存在该问题，请联系就近代理商或DJI 大疆创新售后服务。\n |
| `0x16090039` | 1.电池功率过大，导致自动降落；\n2.请减少载药量或更换电池；\n3.若仍存在该问题，请联系就近代理商或DJI         大疆创新售后服务。\n |
| `0x16090060` | 1.请尽快返航或降落，电池温度传感器异常\n2.电池温度传感器故障，无法继续使用，请停止使用该电池，并联系就近代理商或DJI售后服务\n |

</details>

## 0x160A** — Real-name registration (1 codes)

| Alarm ID | Tip |
|---|---|
| `0x160A0011` | Real-name registration is canceled, which may result in flight safety risks. View Help Documentation and complete real-name registration based on instructions before flight |

## 0x1610** — Takeoff readiness (142 codes)

| Alarm ID | Tip |
|---|---|
| `0x16100001` | Compass error (%alarmid). Restart aircraft |
| `0x16100002` | DJI Assistant connected. Unable to take off. Disconnect before taking off(%alarmid) |
| `0x16100003` | Unable to take off. Check whether aircraft is activated or update to latest firmware version (%alarmid) |
| `0x16100005` | IMU error(%alarmid). Restart aircraft |
| `0x16100006` | Invalid IMU serial number (%alarmid). Maintenance required |
| `0x16100008` | Compass calibrating. Unable to take off. Wait for calibration to complete before taking off(%alarmid)(%alarmid) |
| `0x16100009` | Sensor system initializing (%alarmid)... |
| `0x1610000A` | Aircraft in Beginner mode. Unable to take off. Take off in an open outdoor area when in Beginner mode(%alarmid) |
| `0x1610000B` | Battery cell error (%alarmid). Contact DJI Support |
| `0x1610000C` | Battery error (%alarmid). Contact DJI Support |
| `0x1610000D` | Critical low battery voltage. Unable to take off. Charge promptly(%alarmid) |
| `0x1610000E` | Critical low battery. Unable to take off. Charge promptly(%alarmid) |
| `0x1610000F` | Critical low battery voltage. Unable to take off. Charge promptly(%alarmid) |
| `0x16100010` | Battery output power insufficient. Charge promptly (%alarmid) |
| `0x16100011` | Critical low battery. Unable to take off. Charge promptly(%alarmid) |
| `0x16100012` | Battery initializing. Unable to take off. Wait for initialization to complete before taking off |
| `0x16100013` | Running Flight Simulator. Unable to take off. Restart aircraft before taking off(%alarmid) |
| `0x16100015` | Aircraft pitch angle too large. Ensure aircraft is level before taking off (%alarmid) |
| `0x16100016` | Aircraft not activated. Restart DJI Pilot and activate (%alarmid) |
| `0x16100017` | Aircraft in GEO Zone. Unable to take off. Check map to find Recommended Zones(%alarmid) |
| `0x16100018` | IMU error (%alarmid). Calibrate IMU |
| `0x16100019` | ESC error. Land promptly and contact DJI Support (%alarmid) |
| `0x1610001A` | Sensor system initializing (%alarmid) .Unable to take off. Wait for initialization to complete before taking off |
| `0x1610001B` | System updating. Unable to take off. Wait for update to complete(%alarmid) |
| `0x1610001C` | Running Flight Simulator. Unable to take off. Restart aircraft before taking off(%alarmid) |
| `0x1610001D` | IMU calibrating. Unable to take off. Wait for calibration to complete before takeoff(%alarmid) |
| `0x1610001E` | Aircraft pitch angle too large. Ensure aircraft is level before taking off (%alarmid) |
| `0x1610001F` | Flight controller overheats (%alarmid). Returning to home. Fly with caution. Check aircraft fan after landing |
| `0x16100020` | Flight controller overheats (%alarmid). Landing automatically. Fly with caution. Check aircraft fan after landing |
| `0x16100021` | RTH canceled. Control stick pushed down (%alarmid) |
| `0x16100022` | Unable to take off. Aircraft unable to remain stable for several times. To ensure flight safety, contact DJI Support |
| `0x16100024` | Compass interference. Unable to take off. Move away from source of interference or calibrate compass (%alarmid) |
| `0x16100025` | Hot swapping not supported for RTK module (%alarmid). Install RTK module and restart aircraft |
| `0x16100026` | Unable to take off. Non-DJI RTK module detected (%alarmid). Use official module |
| `0x16100027` | Flight control system error. Unable to take off (%alarmid). Restart aircraft and try again. Contact DJI Support if the issue persists |
| `0x16100029` | Invalid aircraft serial number. Contact your local dealer or DJI Support (%alarmid) |
| `0x1610002D` | GNSS error (%alarmid). Restart aircraft |
| `0x1610002F` | Data recorder error (%alarmid). Restart aircraft |
| `0x16100030` | Aircraft model and firmware version do not match (%alarmid). Contact your local dealer or DJI Support |
| `0x16100033` | Real-name registration not performed. View Help Documentation and complete real-name registration based on instructions before flight |
| `0x16100034` | Real-name registration is canceled. View Help Documentation and complete real-name registration based on instructions before flight |
| `0x1610003A` | Unable to take off. RTK module overheated. Aircraft will power off immediately (%alarmid) |
| `0x1610003D` | Sensor system error (%alarmid). Restart aircraft |
| `0x1610003E` | Unable to take off. Calibrating remote controller. Wait for calibration to complete |
| `0x1610003F` | Remote controller calibration data error (%alarmid). Recalibrate remote controller |
| `0x16100040` | Remote controller calibration incomplete. Continue calibration |
| `0x16100041` | Unable to take off. Control sticks off-centered. Calibrate remote controller |
| `0x16100042` | Unable to take off. Control stick hardware error. Contact DJI Support |
| `0x1610004A` | Sensor system error (%alarmid). Restart aircraft |
| `0x1610004B` | Sensor system error (%alarmid). Restart aircraft |
| `0x1610004C` | Unable to take off. Remote Controller Calibration Required (%alarmid) |
| `0x1610004D` | Flight controller data error. Restart aircraft (%alarmid) |
| `0x1610004E` | Not enough batteries installed. Install two batteries before taking off (%alarmid) |
| `0x1610004F` | Battery authentication failed. Replace with standard DJI battery (%alarmid) |
| `0x16100051` | Large voltage difference between batteries. Replace batteries with new ones of a similar capacity (%alarmid) |
| `0x16100053` | Aircraft module firmware versions do not match (%alarmid). Contact your local dealer or DJI Support |
| `0x16100054` | Gimbal error (%alarmid). Contact DJI Support |
| `0x16100055` | Gimbal error (%alarmid). Contact DJI Support |
| `0x16100055_pm320` | Gimbal error (%alarmid). Make sure tilt axis is unlocked |
| `0x16100056` | Gimbal error (%alarmid). Contact DJI Support |
| `0x16100057` | Gimbal error (%alarmid). Contact DJI Support |
| `0x16100058` | Gimbal updating (%alarmid)... |
| `0x1610005D` | IMU calibration successful. Unable to take off. Restarting aircraft required(%alarmid) |
| `0x1610005E` | Aircraft rolled during takeoff. Check whether propellers were installed correctly (%alarmid) |
| `0x1610005F` | Motor stalled. Check for objects blocking motor or contact DJI Support (%alarmid) |
| `0x16100060` | Motor rotation speed error. Restart aircraft (%alarmid) |
| `0x16100061` | Motor idle. Unable to take off. Check whether propellers are detached or installed incorrectly (%alarmid) |
| `0x16100062` | Unable to turn on motor. Check aircraft status and restart (%alarmid) |
| `0x16100063` | Auto Takeoff failed. Unable to take off(%alarmid) |
| `0x16100064` | Aircraft rolled over. Restart aircraft and ensure it is level before taking off (%alarmid) |
| `0x16100065` | Battery firmware version error. Replace battery or update to the latest firmware (%alarmid) |
| `0x16100066` | RTK signal weak. Move to an open area for takeoff or turn off RTK (%alarmid) |
| `0x16100067` | Compass interference (%alarmid). Move away from interference source or calibrate compass |
| `0x16100068` | ESC short-circuited. Restart aircraft (%alarmid) |
| `0x16100069` | Propulsion system hardware error. Restart aircraft (%alarmid) |
| `0x1610006A` | Incompatible battery (%alarmid). Replace battery |
| `0x1610006B` | Unable to take off. Battery firmware update required (%alarmid) |
| `0x1610006C` | Severe battery error (%alarmid). Auto landing... |
| `0x1610006D` | Power and flight attitude restricted (%alarmid). Return to home promptly. Check battery warning for issue reason |
| `0x16100071` | GNSS error (%alarmid). Restart aircraft |
| `0x16100072` | Gimbal calibrating (%alarmid)... |
| `0x16100073` | Aircraft firmware or Fly Safe database out of date, or flight route uploading to aircraft (%alarmid) |
| `0x16100074` | Takeoff altitude error. Land and restart aircraft (%alarmid) |
| `0x16100075` | ESC firmware versions do not match. Update to latest firmware version (%alarmid) |
| `0x16100076` | IMU position data does not match (%alarmid). Maintenance required |
| `0x16100078` | Compass error (%alarmid). Contact DJI Support |
| `0x1610007A` | ESC beeping. Unable to take off. Turn off ESC beeping before takeoff(%alarmid) |
| `0x1610007B` | ESC overheated (%alarmid). Wait for ESC temperature to return to normal before use |
| `0x1610007D` | Impact detected. Aircraft landed. Restart aircraft (%alarmid) |
| `0x1610007F` | Impact detected. Restart aircraft (%alarmid) |
| `0x16100080` | Aircraft altitude control error. Restart aircraft (%alarmid) |
| `0x16100081` | Battery firmware out-of-date. Update to latest firmware version (%alarmid) |
| `0x16100082` | Large voltage difference between battery cells (%alarmid). Maintain battery according to Help Documentation |
| `0x16100083` | Turn battery locker to its limit and ensure both batteries are installed correctly (%alarmid) |
| `0x16100083_wm265` | Make sure battery is properly installed (%alarmid) |
| `0x16100084` | Check whether aircraft fan is stalled (%alarmid) |
| `0x16100084_pm320` | Check whether aircraft fan is stalled (%alarmid) |
| `0x16100085` | Aircraft overheated. Power off aircraft and wait for processor temperature to return to normal (%alarmid) |
| `0x16100087` | Emergency propeller stop triggered (%alarmid) |
| `0x16100088` | Unable to take off. Calibrating remote controller. Exit calibration first |
| `0x16100089` | Unable to take off (%alarmid). Remote controller still confirming binding status/not bound. Max number of temporary flights reached. Use bound remote controller or bind aircraft to current remote controller |
| `0x1610008A` | Flight control system error (%alarmid). Restart aircraft |
| `0x1610008F` | Aircraft antenna satellite signal searching error. Move to open area for takeoff (%alarmid) |
| `0x16100090` | Sensor system error (%alarmid). Restart aircraft |
| `0x16100091` | Unable to fly in this area (%alarmid) |
| `0x16100092` | Battery maintenance required for flight safety (%alarmid) |
| `0x16100095` | Unable to take off. Set Hover mode before flying (%alarmid) |
| `0x16100096` | %battery_index Battery power supply error. Aircraft auto landing. Move control stick to control landing location (%alarmid) |
| `0x16100099` | Gimbal startup error. Check whether gimbal can rotate freely and restart the aircraft (%alarmid) |
| `0x1610009A` | Excessive gimbal vibration. Check whether gimbal can rotate freely or is damaged. Restart aircraft (%alarmid) |
| `0x1610009F` | Flight controller unit error (%alarmid). Restart aircraft |
| `0x161000A0` | GEO module error. Unable to take off. Contact DJI Support (%alarmid) |
| `0x161000A1` | Land promptly and check whether frame arm sleeves are tightened securely (%alarmid) |
| `0x161000A2` | Check whether lower fan is stalled  (%alarmid) |
| `0x161000A4` | Aircraft on moving platform such as vehicle (%alarmid). Take off on flat and stable surface |
| `0x161000A5` | Unable to take off. Propellers folded (%alarmid). Unfold propellers before takeoff |
| `0x161000A6` | Remote controller battery low (%alarmid). Return to home or land promptly and recharge battery |
| `0x161000A7` | Unable to take off (%alarmid). Failed to verify remote controller. Max number of temporary flights reached. Use bound remote controller or bind to another remote controller |
| `0x161000A9` | Propellers in slow motion mode (%alarmid). Take off after propellers stopped |
| `0x161000AA` | GEO module error (%alarmid). Restart aircraft. Contact DJI Support if warning persists |
| `0x161000AB` | Fly Safe database error (%alarmid). Update database |
| `0x161000AC` | Flight control system error. Unable to take off (%alarmid). Restart aircraft and try again. Contact DJI Support if the issue persists |
| `0x161000AF` | Initializing flight control system (%alarmid). Wait for initialization to complete |
| `0x161000c0` | Unable to take off: left battery and right battery models do not match. Replace battery for model consistency |
| `0x161000c0_in_the_sky` | Left battery and right battery models do not match. Land aircraft immediately and replace battery |
| `0x161000C4` | Unable to take off. Auto checking ESC... |
| `0x161000C7` | Battery temperature lower than 10°C. Unable to take off (%alarmid). Warm up battery to higher than 10° or replace with warmed-up battery |
| `0x161000C8` | Unable to take off. Check whether aircraft is connected to DJI Assistant or system is updating(%alarmid) |
| `0x161000C9` | Unable to take off. Check whether aircraft is connected to DJI Assistant or system is updating(%alarmid) |
| `0x161000F1` | Make sure front right frame arm is fully unfolded before takeoff (%alarmid) |
| `0x161000F2` | Make sure front left frame arm is fully unfolded before takeoff (%alarmid) |
| `0x161000F3` | Make sure back left frame arm is fully unfolded before takeoff (%alarmid) |
| `0x161000F4` | Make sure back right frame arm is fully unfolded before takeoff (%alarmid) |
| `0x161000F5` | Unable to take off. Initializing system (%alarmid). Try again later |
| `0x161000F6` | Flight control system error (%alarmid). Restart aircraft |
| `0x161000F7` | Sensor system initialization in progress (%alarmid) |
| `0x161000F8` | Sensor system initialization in progress (%alarmid) |
| `0x161000F9` | Unable to take off. Remote controller signal weak (%alarmid). Take off near remote controller |
| `0x161000FA` | Unable to take off. Remote controller signal weak (%alarmid). Take off near remote controller |
| `0x161000FB` | Unable to take off. Propeller damaged (%alarmid). Contact DJI Support to replace propeller |
| `0x161000FC` | Unable to take off. DJI Dock in site selection process (%alarmid). Complete site selection before taking off |
| `0x161000FD` | Make sure aircraft is in custom task area or take off 10 m away from the boundary of the task area |

## 0x1611** — Thermal & accessory (7 codes)

| Alarm ID | Tip |
|---|---|
| `0x16110023` | Aircraft output power insufficient. Land immediately with caution (%alarmid) |
| `0x16110029` | Accessory installed — flight performance and wind resistance reduced (%alarmid)+ |
| `0x1611002A` | Searchlight disconnected+ |
| `0x1611002B` | Megaphone disconnected+ |
| `0x16110065` | Aircraft overheated. AI recognition failed. Wait for temperature to return to normal before use (%alarmid) |
| `0x16110066` | RTK module overheated. Wait for temperature to return to normal before use (%alarmid) |
| `0x16110067` | RTK module overheated and disabled. Wait for temperature to return to normal before use (%alarmid) |

<details><summary>CN source (verbatim from HMS.json)</summary>

| Alarm ID | `tipEn` (original CN) |
|---|---|
| `0x16110029` | 配件已安装，飞行性能和抗风性能降低(%alarmid) |
| `0x1611002A` | 探照灯断开连接 |
| `0x1611002B` | 喊话器断开连接 |

</details>

## 0x1620** — USB / extension port (16 codes)

| Alarm ID | Tip |
|---|---|
| `0x16200101` | USB connected (%alarmid). Unable to take off. Disconnect USB, restart aircraft, and try again |
| `0x16200102` | Unable to take off. Clearing logs (%alarmid). Take off after logs are cleared |
| `0x16200103` | Unable to take off. Updating firmware (%alarmid). Take off after firmware is updated |
| `0x16200104` | Unable to take off. Firmware update required or update in progress (%alarmid). Take off after firmware is updated |
| `0x16200201` | Unable to take off. Updating Fly Safe database (%alarmid). Take off after database is updated |
| `0x16200202` | Vision sensor calibration error (%alarmid). Calibrate again. Contact DJI Support if the issue persists |
| `0x16200203` | ToF sensor calibration error (%alarmid). Contact DJI Support |
| `0x16200204` | Vision sensor status error (%alarmid). Restart aircraft. Contact DJI Support if the issue persists |
| `0x16200207` | Unable to take off. Bottom infrared sensor connection error (%alarmid). Restart aircraft |
| `0x16200208` | Propeller error. Unable to take off. Make sure propellers are not damaged. Restart aircraft and try again |
| `0x16200301` | Extension port device error. Unable to take off (%alarmid) |
| `0x16200302` | PSDK extension port error (%alarmid). Stop propellers |
| `0x16200401` | Mandatory Fly Safe database update in progress (%alarmid). Take off after database is updated |
| `0x16200402` | Mandatory firmware update in progress (%alarmid). Take off after firmware is updated |
| `0x16200501` | Incompatible battery versions (%alarmid). Replace with battery of same version |
| `0x16200601` | Initializing flight system... |

## 0x1630** — BDS satellite (1 codes)

| Alarm ID | Tip |
|---|---|
| `0x16300001` | Only BDS data used (%alarmid). Number of searched satellites may be affected. Fly with caution |

## 0x1640** — Internal — abstract-data topics (CN+) (10 codes)

| Alarm ID | Tip |
|---|---|
| `0x16400110` | Abstract data `gimbal_state` has no content+ |
| `0x16400111` | Abstract data `camera_state` has no content+ |
| `0x16400112` | Abstract data `camera_cap_status` has no content+ |
| `0x16400113` | Abstract data `camera_video_param` has no content+ |
| `0x16400114` | Abstract data `camera_lens_param` has no content+ |
| `0x16400115` | Abstract data `camera_lens_param_ir` has no content+ |
| `0x16400116` | Abstract data `camera_data_hd` has no content+ |
| `0x16400117` | Abstract data `camera_data_vga` has no content+ |
| `0x16400118` | Stick-passthrough `rc` abnormal+ |
| `0x16400119` | Stick-passthrough `motion_rc` abnormal+ |

<details><summary>CN source (verbatim from HMS.json)</summary>

| Alarm ID | `tipEn` (original CN) |
|---|---|
| `0x16400110` | 抽象数据gimbal_state无内容 |
| `0x16400111` | 抽象数据camera_state无内容 |
| `0x16400112` | 抽象数据camera_cap_status无内容 |
| `0x16400113` | 抽象数据camera_video_param无内容 |
| `0x16400114` | 抽象数据camera_lens_param无内容 |
| `0x16400115` | 抽象数据camera_lens_param_ir无内容 |
| `0x16400116` | 抽象数据camera_data_hd无内容 |
| `0x16400117` | 抽象数据camera_data_vga无内容 |
| `0x16400118` | 杆量直通rc异常 |
| `0x16400119` | 杆量直通motion_rc异常 |

</details>

## 0x1641** — Internal — DSP interaction (CN+) (7 codes)

| Alarm ID | Tip |
|---|---|
| `0x16416001` | DSP-to-ARM interrupt dispatch failed+ |
| `0x16416002` | DSP-side interaction timeout+ |
| `0x16418000` | Caller invoked DSP interface incorrectly+ |
| `0x16418001` | DSP input parameter error+ |
| `0x16418500` | Developer-side DSP interface design error+ |
| `0x16418501` | DSP operator call timeout+ |
| `0x16418502` | DSP operator call busy+ |

<details><summary>CN source (verbatim from HMS.json)</summary>

| Alarm ID | `tipEn` (original CN) |
|---|---|
| `0x16416001` | DSP向ARM发出中断失败 |
| `0x16416002` | DSP侧交互部分超时 |
| `0x16418000` | 使用者调用dsp接口出错 |
| `0x16418001` | DSP输入参数错误 |
| `0x16418500` | 开发者设计dsp接口出错 |
| `0x16418501` | DSP算子调用超时 |
| `0x16418502` | DSP算子调用忙 |

</details>

## 0x1642** — Internal — DBus topics (CN+) (39 codes)

| Alarm ID | Tip |
|---|---|
| `0x16420000` | Flight system module initialization failed+ |
| `0x16420001` | Flight system `AP_Linux` module init failed+ |
| `0x16420002` | Flight system `AP_Linux` module start failed+ |
| `0x16420003` | Flight system `AP_RTOS` module init failed+ |
| `0x16420004` | Flight system `AP_RTOS` module start failed+ |
| `0x16420010` | Flight system power management abnormal+ |
| `0x16420011` | `sysmode` did not respond to event+ |
| `0x16420012` | Flight system event notification failed+ |
| `0x16420013` | Flight system power scenario switch timeout+ |
| `0x16420014` | Power-management message-queue send timeout+ |
| `0x16420015` | Power-management node state sync failed+ |
| `0x16420016` | Power-management child-node V1 messages not routed+ |
| `0x16420020` | Capability item parameter sync failed+ |
| `0x16420021` | `csdk` disconnected+ |
| `0x16420022` | Capability-set parameter table read failed+ |
| `0x16420100` | DBus topic `app_state` has no data+ |
| `0x16420101` | DBus topic `battery_state` has no data+ |
| `0x16420102` | DBus topic `flight_state` has no data+ |
| `0x16420103` | DBus topic `fly_limit` has no data+ |
| `0x16420104` | DBus topic `home_state` has no data+ |
| `0x16420105` | DBus topic `mission_config` has no data+ |
| `0x16420106` | DBus topic `rc_state` has no data+ |
| `0x16420107` | DBus topic `sensor_data` has no data+ |
| `0x16420108` | DBus topic `flight_record` has no data+ |
| `0x16420109` | DBus topic `motion_rc_info` has no data+ |
| `0x1642010A` | DBus topic `vio_result` has no data+ |
| `0x1642010B` | DBus topic `image_status` has no data+ |
| `0x1642010C` | DBus topic `fmu_gps` has no data+ |
| `0x1642010D` | DBus topic `fmu_rtk` has no data+ |
| `0x1642010E` | DBus topic `fusion_out` has no data+ |
| `0x1642010F` | DBus topic `radar_detect_info` has no data+ |
| `0x16420110` | DBus topic `gimbal_state` has no data+ |
| `0x16420111` | DBus topic `camera_state` has no data+ |
| `0x16420112` | DBus topic `camera_cap_status` has no data+ |
| `0x16420113` | DBus topic `camera_video_param` has no data+ |
| `0x16420114` | DBus topic `camera_lens_param` has no data+ |
| `0x16420115` | DBus topic `camera_lens_param_ir` has no data+ |
| `0x16420116` | DBus topic `camera_data_hd` has no data+ |
| `0x16420117` | DBus topic `camera_data_vga` has no data+ |

<details><summary>CN source (verbatim from HMS.json)</summary>

| Alarm ID | `tipEn` (original CN) |
|---|---|
| `0x16420000` | 飞行系统模块初始化失败 |
| `0x16420001` | 飞行系统AP_Linux模块init失败 |
| `0x16420002` | 飞行系统AP_Linux模块start失败 |
| `0x16420003` | 飞行系统AP_RTOS模块init失败 |
| `0x16420004` | 飞行系统AP_RTOS模块start失败 |
| `0x16420010` | 飞行系统功耗管理异常 |
| `0x16420011` | sysmode未响应event事件 |
| `0x16420012` | 飞行系统event事件通知失败 |
| `0x16420013` | 飞行系统功耗场景切换超时 |
| `0x16420014` | 功耗管理消息队列发送超时 |
| `0x16420015` | 功耗管理节点状态同步失败 |
| `0x16420016` | 功耗管理子节点间V1消息不通 |
| `0x16420020` | 能力项参数同步失败 |
| `0x16420021` | csdk断连 |
| `0x16420022` | 能力集参数表数据读取失败 |
| `0x16420100` | dbus话题app_state无数据 |
| `0x16420101` | dbus话题battery_state无数据 |
| `0x16420102` | dbus话题flight_state无数据 |
| `0x16420103` | dbus话题fly_limit无数据 |
| `0x16420104` | dbus话题home_state无数据 |
| `0x16420105` | dbus话题mission_config无数据 |
| `0x16420106` | dbus话题rc_state无数据 |
| `0x16420107` | dbus话题sensor_data无数据 |
| `0x16420108` | dbus话题flight_record无数据 |
| `0x16420109` | dbus话题motion_rc_info无数据 |
| `0x1642010A` | dbus话题vio_result无数据 |
| `0x1642010B` | dbus话题image_status无数据 |
| `0x1642010C` | dbus话题fmu_gps无数据 |
| `0x1642010D` | dbus话题fmu_rtk无数据 |
| `0x1642010E` | dbus话题fusion_out无数据 |
| `0x1642010F` | dbus话题radar_detect_info无数据 |
| `0x16420110` | dbus话题gimbal_state无数据 |
| `0x16420111` | dbus话题camera_state无数据 |
| `0x16420112` | dbus话题camera_cap_status无数据 |
| `0x16420113` | dbus话题camera_video_param无数据 |
| `0x16420114` | dbus话题camera_lens_param无数据 |
| `0x16420115` | dbus话题camera_lens_param_ir无数据 |
| `0x16420116` | dbus话题camera_data_hd无数据 |
| `0x16420117` | dbus话题camera_data_vga无数据 |

</details>

## 0x1643** — Internal — Intelligent flight modes (CN+) (171 codes)

| Alarm ID | Tip |
|---|---|
| `0x16430001` | Focus Track exited abnormally+ |
| `0x16430002` | Spotlight exited abnormally+ |
| `0x16430003` | Multi-target scan exited abnormally+ |
| `0x16430004` | Focus Track warning+ |
| `0x16430005` | Fusion data invalid+ |
| `0x16430006` | Sensor data update failed+ |
| `0x16430007` | Aircraft has not taken off+ |
| `0x16430008` | Camera mode not supported+ |
| `0x16430009` | Fusion timestamp abnormal+ |
| `0x1643000A` | Abstract-data pointer is null+ |
| `0x1643000B` | DBus data-retrieval pointer is null+ |
| `0x1643000C` | TM abnormal+ |
| `0x1643000D` | Aircraft attitude too large+ |
| `0x1643000E` | Ambient light too dark+ |
| `0x1643000F` | Remote controller disconnected+ |
| `0x16430010` | TKPlanner abnormal+ |
| `0x16430011` | TE abnormal+ |
| `0x16430012` | POI abnormal+ |
| `0x16430013` | ML abnormal+ |
| `0x16430014` | Data link abnormal+ |
| `0x16430015` | IMU data abnormal+ |
| `0x16430016` | Gimbal data abnormal+ |
| `0x16430017` | FOV data abnormal+ |
| `0x16430018` | ML state abnormal+ |
| `0x16430019` | SOE data abnormal+ |
| `0x1643001A` | IMU data invalid+ |
| `0x1643001B` | Gimbal data invalid+ |
| `0x1643001C` | FOV data invalid+ |
| `0x1643001D` | ML state data invalid+ |
| `0x1643001E` | SOE data invalid+ |
| `0x1643001F` | Circle-ranging duration too long+ |
| `0x16430020` | Circling altitude too close to ground+ |
| `0x16430021` | Distance limit reached+ |
| `0x16430022` | Altitude limit reached+ |
| `0x16430023` | Target type not supported+ |
| `0x16430024` | Target lost as aircraft was about to enter Tracking / Circling+ |
| `0x16430025` | Mind zoom range during target tracking+ |
| `0x16430026` | Target occupies too much of the frame+ |
| `0x16430101` | Exited QuickShots abnormally+ |
| `0x16430102` | QuickShots recording terminated abnormally+ |
| `0x16430103` | Sensor data verification error+ |
| `0x16430104` | Null pointer+ |
| `0x16430105` | Abstract-data pointer is null+ |
| `0x16430106` | DBus data-retrieval pointer is null+ |
| `0x16430107` | QuickShots cannot be executed on the ground+ |
| `0x16430108` | User moved the control stick+ |
| `0x16430109` | User paused+ |
| `0x1643010A` | Altitude limit reached+ |
| `0x1643010B` | Distance limit reached+ |
| `0x1643010C` | Recording stop error+ |
| `0x1643010D` | Recording start error+ |
| `0x1643010E` | Obstacle avoidance+ |
| `0x1643010F` | Remote controller signal lost+ |
| `0x16430110` | Initialization failed+ |
| `0x16430111` | Authority acquisition failed+ |
| `0x16430112` | Insufficient storage+ |
| `0x16430113` | Target lost+ |
| `0x16430114` | Photo capture failed+ |
| `0x16430115` | Compositing failed+ |
| `0x16430116` | Failed to load camera parameters+ |
| `0x16430117` | Failed to adjust camera parameters+ |
| `0x16430118` | Camera angle error+ |
| `0x16430119` | Camera unknown error+ |
| `0x1643011A` | Camera parameter error+ |
| `0x1643011B` | Camera state error+ |
| `0x1643011C` | Setting TOPMODE timed out+ |
| `0x1643011D` | Camera TOPMODE error+ |
| `0x1643011E` | QuickShots warning+ |
| `0x16430201` | MasterShots exited abnormally+ |
| `0x16430202` | MasterShots paused abnormally+ |
| `0x16430203` | MasterShots detected null pointer+ |
| `0x16430204` | MasterShots abstract-data pointer is null+ |
| `0x16430205` | MasterShots DBus data-retrieval pointer is null+ |
| `0x16430206` | MasterShots sensor data verification error+ |
| `0x16430207` | MasterShots — user moved the control stick+ |
| `0x16430208` | MasterShots — user paused+ |
| `0x16430209` | MasterShots — altitude limit reached+ |
| `0x1643020A` | MasterShots — distance limit reached+ |
| `0x1643020B` | MasterShots recording stop failed+ |
| `0x1643020C` | MasterShots recording start failed+ |
| `0x1643020D` | MasterShots encountered obstacle+ |
| `0x1643020E` | MasterShots — remote controller signal lost+ |
| `0x1643020F` | MasterShots initialization failed+ |
| `0x16430210` | MasterShots authority acquisition failed+ |
| `0x16430211` | MasterShots insufficient storage+ |
| `0x16430212` | MasterShots target lost+ |
| `0x16430213` | MasterShots camera parameter error+ |
| `0x16430214` | MasterShots set TOPMODE timed out+ |
| `0x16430215` | MasterShots set TOPMODE abnormal+ |
| `0x16430216` | MasterShots warning+ |
| `0x16430217` | MasterShots failed to adjust camera parameters+ |
| `0x16430218` | MasterShots gimbal control error+ |
| `0x16430219` | MasterShots yaw control error+ |
| `0x1643021A` | MasterShots VA control error+ |
| `0x1643021B` | MasterShots speed control error+ |
| `0x1643021C` | MasterShots camera control error+ |
| `0x1643021D` | MasterShots task mismatch+ |
| `0x16430301` | Exited Hyperlapse abnormally+ |
| `0x16430302` | Hyperlapse exited current task abnormally+ |
| `0x16430303` | Hyperlapse entered pause state abnormally+ |
| `0x16430304` | Hyperlapse warning+ |
| `0x16430305` | Ground-level motors already started+ |
| `0x16430306` | Camera mode abnormal+ |
| `0x16430307` | Current task does not match+ |
| `0x16430308` | Abstract data is empty+ |
| `0x16430309` | Camera mode timed out+ |
| `0x1643030a` | Camera mode mismatch+ |
| `0x1643030b` | Waypoint Hyperlapse — target frame lost+ |
| `0x1643030c` | Return-to-first-waypoint route-platform abnormal+ |
| `0x1643030d` | Circle-ranging timeout+ |
| `0x1643030e` | Flight restricted+ |
| `0x1643030f` | Ground Hyperlapse battery low+ |
| `0x16430310` | GNSS signal weak |
| `0x16430311` | Obstacle avoidance+ |
| `0x16430312` | Circle-ranging triggered flight restriction+ |
| `0x16430313` | Track Hyperlapse triggered altitude limit+ |
| `0x16430314` | Return-to-first-waypoint triggered flight restriction+ |
| `0x16430315` | Obstacle avoidance disabled+ |
| `0x16430316` | Return-to-first-waypoint triggered obstacle avoidance+ |
| `0x16430317` | Obstacle avoidance triggered during execution+ |
| `0x16430318` | Flight restriction triggered during shooting+ |
| `0x16430319` | Route platform aborted abnormally+ |
| `0x1643031a` | Camera storage slow+ |
| `0x1643031b` | Satellite positioning signal weak — waypoint record failed+ |
| `0x1643031c` | Maximum photo limit reached+ |
| `0x1643031d` | Insufficient storage+ |
| `0x1643031e` | Waypoint Hyperlapse route not locked+ |
| `0x1643031f` | Gimbal attitude change too small+ |
| `0x16430320` | Gimbal attitude change out of range+ |
| `0x16430321` | Trajectory load failed+ |
| `0x16430322` | Failed to increment by 1 second+ |
| `0x16430323` | Too few photos captured — unable to composite video+ |
| `0x16430324` | Return-to-first-waypoint trajectory generation failed+ |
| `0x16432400` | ApasMission exited abnormally+ |
| `0x16432401` | Fusion-data subscription abnormal+ |
| `0x16432402` | JSON file read failed+ |
| `0x16432403` | FlyCore data subscription abnormal+ |
| `0x16432404` | Fusion data timeout+ |
| `0x16432405` | Fusion positioning data invalid+ |
| `0x16432410` | ApasMission exited abnormally to closed state+ |
| `0x16432411` | ImageStatus subscription abnormal+ |
| `0x16432412` | Night scene mode+ |
| `0x16432413` | Ambient light too dark, but flight environment is safe+ |
| `0x16432414` | Ambient light too dark — hovering with no horizontal stick input+ |
| `0x16432415` | APAS Planner malfunction, but flight environment is safe+ |
| `0x16432416` | APAS Planner malfunction — hovering with no horizontal stick input+ |
| `0x16432417` | OA Planner malfunction, but flight environment is safe+ |
| `0x16432418` | OA Planner malfunction — hovering with no horizontal stick input+ |
| `0x16432419` | In cloud or fog+ |
| `0x16432420` | ApasMission detour exited abnormally to brake-stop+ |
| `0x16432421` | At flight-restriction-zone edge+ |
| `0x16432422` | Less than 0.5 m above ground+ |
| `0x16432423` | Partial ambient-light too dark+ |
| `0x16432424` | APAS Planner malfunction+ |
| `0x16432425` | High-frame-rate recording+ |
| `0x16432430` | ApasMission triggered brake abnormally+ |
| `0x16432431` | Ambient light too dark — normal brake+ |
| `0x16432432` | Ambient light too dark — emergency brake+ |
| `0x16432433` | APAS Planner malfunction — normal brake+ |
| `0x16432434` | APAS Planner malfunction — emergency brake+ |
| `0x16432435` | OA Planner malfunction — normal brake+ |
| `0x16432436` | OA Planner malfunction — emergency brake+ |
| `0x16432500` | OA module unable to function normally+ |
| `0x16432501` | OA module unable to function normally due to map abnormality+ |
| `0x16432502` | OA module unable to function normally due to map abnormality+ |
| `0x16432503` | Camera is in night-scene mode — OA cannot function normally+ |
| `0x16432504` | OA module unable to function normally — in cloud or fog+ |
| `0x16432505` | OA module unable to function normally — ambient light too dark+ |
| `0x16432506` | OA module ToF obstacle avoidance unable to function normally+ |
| `0x16432550` | OA module triggered abnormal protection+ |
| `0x16432551` | OA module triggered emergency brake+ |

<details><summary>CN source (verbatim from HMS.json)</summary>

| Alarm ID | `tipEn` (original CN) |
|---|---|
| `0x16430001` | 异常退出焦点跟随 |
| `0x16430002` | 异常退出到聚焦 |
| `0x16430003` | 异常退出到多目标扫描 |
| `0x16430004` | 焦点跟随异常提示 |
| `0x16430005` | 融合数据无效 |
| `0x16430006` | 传感器数据更新失败 |
| `0x16430007` | 未起飞 |
| `0x16430008` | 相机模式不支持 |
| `0x16430009` | 融合时间戳异常 |
| `0x1643000A` | 抽象数据指针为空 |
| `0x1643000B` | DBUS获取数据指针为空 |
| `0x1643000C` | TM异常 |
| `0x1643000D` | 飞机姿态过大 |
| `0x1643000E` | 环境光过暗 |
| `0x1643000F` | 遥控器断连 |
| `0x16430010` | TKPlanner异常 |
| `0x16430011` | TE异常 |
| `0x16430012` | POI异常 |
| `0x16430013` | ML异常 |
| `0x16430014` | 数据链路异常 |
| `0x16430015` | IMU数据异常 |
| `0x16430016` | 云台数据异常 |
| `0x16430017` | fov数据异常 |
| `0x16430018` | ml状态异常 |
| `0x16430019` | soe数据异常 |
| `0x1643001A` | IMU数据无效 |
| `0x1643001B` | 云台数据无效 |
| `0x1643001C` | fov数据无效 |
| `0x1643001D` | ml状态数据无效 |
| `0x1643001E` | soe数据无效 |
| `0x1643001F` | 环绕测距时间过长 |
| `0x16430020` | 环绕时距地面过近 |
| `0x16430021` | 限远 |
| `0x16430022` | 限高 |
| `0x16430023` | 目标类型不支持 |
| `0x16430024` | 将要进入Tracking/环绕时目标丢失 |
| `0x16430025` | 目标跟随中注意变焦范围 |
| `0x16430026` | 目标在画面中占比过大 |
| `0x16430101` | 异常退出一键短片 |
| `0x16430102` | 异常终止一键短片拍摄 |
| `0x16430103` | 传感器数据验证错误 |
| `0x16430104` | 空指针 |
| `0x16430105` | 抽象数据指针为空 |
| `0x16430106` | DBUS获取数据指针为空 |
| `0x16430107` | 在地面不能执行一键短片 |
| `0x16430108` | 用户打杆 |
| `0x16430109` | 用户暂停 |
| `0x1643010A` | 限高 |
| `0x1643010B` | 限远 |
| `0x1643010C` | 录像停止错误 |
| `0x1643010D` | 录像开始错误 |
| `0x1643010E` | 避障 |
| `0x1643010F` | 遥控器信号丢失 |
| `0x16430110` | 初始化失败 |
| `0x16430111` | 夺权失败 |
| `0x16430112` | 储存空间不足 |
| `0x16430113` | 目标丢失 |
| `0x16430114` | 拍照失败 |
| `0x16430115` | 合成失败 |
| `0x16430116` | 加载相机参数失败 |
| `0x16430117` | 调整相机参数失败 |
| `0x16430118` | 相机角度错误 |
| `0x16430119` | 相机未知错误 |
| `0x1643011A` | 相机参数错误 |
| `0x1643011B` | 相机状态错误 |
| `0x1643011C` | 设置TOPMODE超时 |
| `0x1643011D` | 相机TOPMODE错误 |
| `0x1643011E` | 异常提示一键短片 |
| `0x16430201` | 大师镜头异常退出 |
| `0x16430202` | 大师镜头异常暂停 |
| `0x16430203` | 大师镜头发现空指针 |
| `0x16430204` | 大师镜头抽象数据指针为空 |
| `0x16430205` | 大师镜头DBUS获取数据指针为空 |
| `0x16430206` | 大师镜头传感器数据验证错误 |
| `0x16430207` | 大师镜头用户打杆 |
| `0x16430208` | 大师镜头用户暂停 |
| `0x16430209` | 大师镜头遇限高 |
| `0x1643020A` | 大师镜头遇限远 |
| `0x1643020B` | 大师镜头录像停止失败 |
| `0x1643020C` | 大师镜头录像开始失败 |
| `0x1643020D` | 大师镜头遇障碍物 |
| `0x1643020E` | 大师镜头遥控器信号丢失 |
| `0x1643020F` | 大师镜头初始化失败 |
| `0x16430210` | 大师镜头夺权失败 |
| `0x16430211` | 大师镜头储存空间不足 |
| `0x16430212` | 大师镜头目标丢失 |
| `0x16430213` | 大师镜头相机参数错误 |
| `0x16430214` | 大师镜头设置TOPMODE超时 |
| `0x16430215` | 大师镜头设置TOPMODE异常 |
| `0x16430216` | 大师镜头警告 |
| `0x16430217` | 大师镜头调整相机参数失败 |
| `0x16430218` | 大师镜头云台控制错误 |
| `0x16430219` | 大师镜头Yaw控制错误 |
| `0x1643021A` | 大师镜头VA控制错误 |
| `0x1643021B` | 大师镜头速度控制错误 |
| `0x1643021C` | 大师镜头相机控制错误 |
| `0x1643021D` | 大师镜头任务不匹配 |
| `0x16430301` | 异常退出延时摄影 |
| `0x16430302` | 延时摄影异常退出当前任务 |
| `0x16430303` | 延时摄影异常进入暂停状态 |
| `0x16430304` | 延时摄影异常提示 |
| `0x16430305` | 地面电机已启动 |
| `0x16430306` | 相机模式异常 |
| `0x16430307` | 当前任务不匹配 |
| `0x16430308` | 抽象数据为空 |
| `0x16430309` | 相机模式超时 |
| `0x1643030a` | 相机模式不匹配 |
| `0x1643030b` | 定向延时中框丢失 |
| `0x1643030c` | 返回首航点航线平台异常 |
| `0x1643030d` | 环绕测距超时 |
| `0x1643030e` | 限飞 |
| `0x1643030f` | 地面延时电量低 |
| `0x16430311` | 避障 |
| `0x16430312` | 环绕测距触发限飞 |
| `0x16430313` | 轨迹延时触发限高 |
| `0x16430314` | 返回首航点触发限飞 |
| `0x16430315` | 避障失效 |
| `0x16430316` | 返回首航点触发避障 |
| `0x16430317` | 运行过程中触发避障 |
| `0x16430318` | 拍摄过程中触发限飞 |
| `0x16430319` | 航线平台异常终止 |
| `0x1643031a` | 相机存储慢 |
| `0x1643031b` | 卫星定位信号弱轨迹点记录失败 |
| `0x1643031c` | 已达到最大照片限制 |
| `0x1643031d` | 存储空间不足 |
| `0x1643031e` | 定向延时航线未锁定 |
| `0x1643031f` | 云台姿态变化太小 |
| `0x16430320` | 云台姿态变化超限 |
| `0x16430321` | 轨迹载入失败 |
| `0x16430322` | 增加1s失败 |
| `0x16430323` | 完成照片太少无法合成视频 |
| `0x16430324` | 返回首航点轨迹生成失败 |
| `0x16432400` | 异常退出 ApasMission |
| `0x16432401` | 融合数据订阅异常 |
| `0x16432402` | Json文件读取失败 |
| `0x16432403` | FlyCore数据订阅异常 |
| `0x16432404` | 融合数据超时 |
| `0x16432405` | 融合定位数据无效 |
| `0x16432410` | ApasMission 异常退出到关闭 |
| `0x16432411` | ImageStatus 订阅异常 |
| `0x16432412` | 夜景模式 |
| `0x16432413` | 环境光过暗且飞行环境安全 |
| `0x16432414` | 环境光过暗且悬停无水平杆 |
| `0x16432415` | APAS Planner 功能异常且飞行环境安全 |
| `0x16432416` | APAS Planner 功能异常且悬停无水平杆 |
| `0x16432417` | OA Planner 功能异常且飞行环境安全 |
| `0x16432418` | OA Planner 功能异常且悬停无水平杆 |
| `0x16432419` | 在云雾中 |
| `0x16432420` | ApasMission 绕行异常退出到刹停 |
| `0x16432421` | 限飞区边缘 |
| `0x16432422` | 距离地面过近小于0.5m |
| `0x16432423` | 部分环境光过暗 |
| `0x16432424` | APAS Planner功能异常 |
| `0x16432425` | 高帧率录像 |
| `0x16432430` | ApasMission 异常触发刹车 |
| `0x16432431` | 环境光过暗普通刹车 |
| `0x16432432` | 环境光过暗紧急刹车 |
| `0x16432433` | APAS Planner 功能异常普通刹车 |
| `0x16432434` | APAS Planner 功能异常紧急刹车 |
| `0x16432435` | OA Planner 功能异常普通刹车 |
| `0x16432436` | OA Planner 功能异常紧急刹车 |
| `0x16432500` | OA模块无法正常工作 |
| `0x16432501` | OA模块因地图异常无法正常工作 |
| `0x16432502` | OA模块因地图异常无法正常工作 |
| `0x16432503` | 相机处于夜景模式OA无法正常工作 |
| `0x16432504` | OA模块因处于云雾中无法正常工作 |
| `0x16432505` | OA模块因环境光过暗无法正常工作 |
| `0x16432506` | OA模块tof避障无法正常工作 |
| `0x16432550` | OA模块触发异常保护 |
| `0x16432551` | OA模块触发紧急刹车 |

</details>

## 0x1645** — Internal — Landing & wayline (62 codes)

| Alarm ID | Tip |
|---|---|
| `0x16450001` | Aircraft failed to return to the dock+ |
| `0x16450002` | Aircraft triggered non-cancellable landing outside the dock+ |
| `0x16450011` | Aircraft hover timeout+ |
| `0x16450012` | Aircraft cannot receive dock status+ |
| `0x16450013` | Dock temporarily does not allow landing+ |
| `0x16450014` | Marker horizontal-position source invalid+ |
| `0x16450015` | Marker horizontal-position source deviation large+ |
| `0x16450016` | Marker horizontal-position source subscription failed+ |
| `0x16450017` | RTK horizontal-position source invalid+ |
| `0x16450018` | RTK horizontal-position source ionospheric check failed+ |
| `0x16450019` | Aircraft horizontal control capability weak+ |
| `0x16450021` | Dock landing function operating abnormally+ |
| `0x16450022` | Aircraft switched to normal landing due to attitude change+ |
| `0x16450023` | Dock has no alternate landing point configured — cannot trigger alternate landing+ |
| `0x16450024` | Aircraft did not trigger early propeller stop+ |
| `0x16450025` | Abstract data update failed+ |
| `0x16450031` | Aircraft triggered alternate landing+ |
| `0x16450032` | Aircraft MCU took over control+ |
| `0x16450033` | Dock state abnormal — landing permanently disallowed+ |
| `0x16450034` | Aircraft hovered to low battery — triggered alternate landing+ |
| `0x16450035` | Aircraft failed to reach alternate landing point — mid-route landing+ |
| `0x16450101` | Wayline paused abnormally+ |
| `0x16450102` | Wayline aborted abnormally+ |
| `0x16450103` | Wayline function abnormal+ |
| `0x16450104` | Wayline altitude limit reached+ |
| `0x16450105` | Wayline low-altitude limit reached+ |
| `0x16450106` | Wayline distance limit reached+ |
| `0x16450107` | Wayline hit no-fly zone+ |
| `0x16450108` | Obstacle detected during wayline execution+ |
| `0x16450109` | GNSS signal weak during task |
| `0x1645010A` | Low battery+ |
| `0x1645010B` | Wayline generation timed out+ |
| `0x1645010C` | Unable to obtain abstract data+ |
| `0x1645010D` | Parameter table read failed+ |
| `0x1645010E` | Trajectory-library computation failed+ |
| `0x1645010F` | Takeoff request failed+ |
| `0x16450110` | Wayline-task request failed+ |
| `0x16450111` | Return-to-home request failed+ |
| `0x16450112` | Landing request failed+ |
| `0x16450113` | Aircraft lost signal+ |
| `0x16450114` | During real-time terrain-follow, camera state has issues (too bright, too dark, or bilateral brightness mismatch)+ |
| `0x16450115` | Global-map computation error during real-time terrain-follow+ |
| `0x16450116` | Wayline action-group parsing failed+ |
| `0x16450117` | Flight task conflict — unable to acquire aircraft control authority+ |
| `0x16450118` | File to be executed has parse error+ |
| `0x16450119` | WPMZ file read wait time too long+ |
| `0x1645011A` | Wayline has already started — cannot start again+ |
| `0x1645011B` | Camera abstract-device abnormal+ |
| `0x1645011C` | Gimbal abstract-device abnormal+ |
| `0x1645011D` | App link abnormal+ |
| `0x1645011E` | Factory file not deleted+ |
| `0x1645011F` | RTK state jumped — wayline exited+ |
| `0x16450120` | Quick-takeoff request failed+ |
| `0x16450121` | Auto-takeoff execution failed+ |
| `0x16450122` | Wayline hit custom flight area+ |
| `0x16450123` | Wayline panorama-photo action error+ |
| `0x16450124` | Panorama-photo execution timeout+ |
| `0x16450125` | Panorama-photo — camera TOPMODE set failed+ |
| `0x16450126` | Panorama-photo — camera SUBMODE set failed+ |
| `0x16450127` | Aircraft yaw-rotation timeout before panorama photo+ |
| `0x16450128` | Aircraft yaw-recovery timeout after panorama photo+ |
| `0x16450129` | Panorama-photo null-pointer error+ |

<details><summary>CN source (verbatim from HMS.json)</summary>

| Alarm ID | `tipEn` (original CN) |
|---|---|
| `0x16450001` | 飞机未能返回机场 |
| `0x16450002` | 飞机机场外触发不可取消降落 |
| `0x16450011` | 飞机悬停超时 |
| `0x16450012` | 飞机无法接收到机场状态 |
| `0x16450013` | 机场暂时不允许降落 |
| `0x16450014` | Marker水平位置源无效 |
| `0x16450015` | Marker水平位置源偏差大 |
| `0x16450016` | Marker水平位置源订阅失败 |
| `0x16450017` | RTK水平位置源无效 |
| `0x16450018` | RTK水平位置源电离层校验不通过 |
| `0x16450019` | 飞机水平控制能力弱 |
| `0x16450021` | 机场降落功能运行异常 |
| `0x16450022` | 飞机因为切姿态变为普通降落 |
| `0x16450023` | 机场没有设置备降点无法触发备降 |
| `0x16450024` | 飞机没有触发提前停桨 |
| `0x16450025` | 抽象数据更新失败 |
| `0x16450031` | 飞机触发备降 |
| `0x16450032` | 飞机MCU接管控制 |
| `0x16450033` | 机场状态异常永久不允许降落 |
| `0x16450034` | 飞机悬停到低电量触发备降 |
| `0x16450035` | 飞机未能到达备降点中途降落 |
| `0x16450101` | 航线异常暂停 |
| `0x16450102` | 航线异常中止 |
| `0x16450103` | 航线功能异常 |
| `0x16450104` | 航线限高 |
| `0x16450105` | 航线限低 |
| `0x16450106` | 航线限远 |
| `0x16450107` | 航线触碰到禁飞区 |
| `0x16450108` | 航线执行中检测到障碍物 |
| `0x1645010A` | 低电量 |
| `0x1645010B` | 航线生成超时 |
| `0x1645010C` | 拿不到抽象数据 |
| `0x1645010D` | 参数表读取失败 |
| `0x1645010E` | 轨迹库计算失败 |
| `0x1645010F` | 请求起飞失败 |
| `0x16450110` | 请求航线任务失败 |
| `0x16450111` | 请求返航失败 |
| `0x16450112` | 请求降落失败 |
| `0x16450113` | 飞行器失联 |
| `0x16450114` | 实时仿地过程中，相机状态有问题(过亮，过暗，两侧亮度不一致) |
| `0x16450115` | 实时仿地过程中全局地图计算出错 |
| `0x16450116` | 航线动作组解析失败 |
| `0x16450117` | 飞行任务冲突，无法获取飞机控制权 |
| `0x16450118` | 要执行的文件解析错误 |
| `0x16450119` | 等待wpmz文件读取时间过长 |
| `0x1645011A` | 航线已经开始，不能再次开始 |
| `0x1645011B` | 相机抽象设备异常 |
| `0x1645011C` | 云台抽象设备异常 |
| `0x1645011D` | app链路异常 |
| `0x1645011E` | 工厂文件未删除 |
| `0x1645011F` | RTK状态跳变，航线已退出 |
| `0x16450120` | 请求快速起飞失败 |
| `0x16450121` | 自动起飞运行失败 |
| `0x16450122` | 航线触碰到自定义飞行区 |
| `0x16450123` | 航线全景拍照动作出错 |
| `0x16450124` | 执行全景拍照过程超时 |
| `0x16450125` | 全景拍照设置相机topmode失败 |
| `0x16450126` | 全景拍照设置相机submode失败 |
| `0x16450127` | 全景拍照前飞机转yaw超时 |
| `0x16450128` | 全景拍照后飞机恢复yaw超时 |
| `0x16450129` | 全景拍照空指针错误 |

</details>

## 0x1646** — Internal — Fusion / hall / RTK (29 codes)

| Alarm ID | Tip |
|---|---|
| `0x16461000` | Fusion-positioning system abnormal switch+ |
| `0x16461001` | `ap_fusion` disconnected+ |
| `0x16461002` | `ap_fusion` has critical fault+ |
| `0x16461003` | Default fusion-positioning system was modified+ |
| `0x16462001` | Hall-effect device disconnected+ |
| `0x16462004` | Hall-effect calibration data abnormal+ |
| `0x16462007` | Hall-effect sensor missing magnet ring — operating abnormally+ |
| `0x1646200A` | Hall-effect sensor mutual check failed+ |
| `0x16463001` | RTK No NLFix |
| `0x16463004` | Primary-antenna observation quality poor+ |
| `0x16463005` | Signal frequently loses lock+ |
| `0x16463006` | Ionosphere active+ |
| `0x16463007` | Primary-antenna SNR sharp drop+ |
| `0x16463008` | Secondary-antenna SNR sharp drop+ |
| `0x16463009` | Primary-antenna open-circuit or short-circuit+ |
| `0x1646300A` | Secondary-antenna open-circuit or short-circuit+ |
| `0x1646300B` | RTK Heading No NLFix |
| `0x16463011` | RTK base-station RTCM data abnormal+ |
| `0x16463012` | 2607 did not receive RTCM+ |
| `0x16463013` | 2607 RTCM V1 packet assembly abnormal+ |
| `0x16463014` | 2607 RTCM transmission bit error+ |
| `0x16463021` | 2906 did not receive RTCM+ |
| `0x16463022` | 2906 RTK data source inconsistent+ |
| `0x16463023` | 2906 RTK data source invalid+ |
| `0x16463024` | 2906 RTK data source initialization failed+ |
| `0x16463031` | 2606 did not receive RTCM+ |
| `0x16463032` | 2606 RTK data source inconsistent+ |
| `0x16463033` | 2606 RTK data source invalid+ |
| `0x16463034` | 2606 did not receive data from RTK information source+ |

<details><summary>CN source (verbatim from HMS.json)</summary>

| Alarm ID | `tipEn` (original CN) |
|---|---|
| `0x16461000` | 融合定位系统异常切换 |
| `0x16461001` | ap_fusion 断联 |
| `0x16461002` | ap_fusion 存在严重故障 |
| `0x16461003` | 默认融合定位系统被修改 |
| `0x16462001` | 霍尔设备断开 |
| `0x16462004` | 霍尔校准数据异常 |
| `0x16462007` | 霍尔传感器缺少磁环，工作异常 |
| `0x1646200A` | 霍尔传感器间互检失败 |
| `0x16463004` | 主天线观测质量差 |
| `0x16463005` | 信号频繁失锁 |
| `0x16463006` | 电离层活跃 |
| `0x16463007` | 主天线SNR陡降 |
| `0x16463008` | 副天线SNR陡降 |
| `0x16463009` | 主天线开路或短路 |
| `0x1646300A` | 副天线开路或短路 |
| `0x16463011` | RTK基站RTCM数据异常 |
| `0x16463012` | 2607未收到RTCM |
| `0x16463013` | 2607 RTCM V1组包异常 |
| `0x16463014` | 2607RTCM传输误码 |
| `0x16463021` | 2906未收到RTCM |
| `0x16463022` | 2906RTK数据源不一致 |
| `0x16463023` | 2906RTK数据源无效 |
| `0x16463024` | 2906RTK数据源初始化失败 |
| `0x16463031` | 2606未收到RTCM |
| `0x16463032` | 2606RTK数据源不一致 |
| `0x16463033` | 2606RTK数据源无效 |
| `0x16463034` | 2606未收到RTK信息源的信息 |

</details>

## 0x1647** — Internal — Positioning & compass calibration (86 codes)

| Alarm ID | Tip |
|---|---|
| `0x16471000` | Positioning has no output — FC sensors may not be ready+ |
| `0x16471001` | Positioning abnormal — system abnormality or loading abnormality+ |
| `0x16471002` | Positioning output velocity-position consistency poor+ |
| `0x16471003` | Flight-control sensors not ready+ |
| `0x16471004` | State real-time delay too large+ |
| `0x16471005` | Loop execution time abnormal+ |
| `0x16471006` | State timestamp abnormal+ |
| `0x16471007` | IMU BIAS random-walk abnormal+ |
| `0x16471010` | Visual positioning multi-direction sync abnormal+ |
| `0x16471012` | Hardware-accelerator call abnormal+ |
| `0x16471100` | IMU timestamp abnormal+ |
| `0x16471101` | Visual timestamp abnormal+ |
| `0x16471102` | UBLOX GPS timestamp abnormal+ |
| `0x16471103` | DJI GPS timestamp abnormal+ |
| `0x16471201` | IMU stationary-detection update abnormal+ |
| `0x16471204` | Barometer update abnormal+ |
| `0x16471205` | ToF update abnormal+ |
| `0x16471207` | Visual update abnormal+ |
| `0x16471209` | GPS update abnormal+ |
| `0x16476000` | VIO front-end abnormal+ |
| `0x16476001` | Initialization abnormal+ |
| `0x16476002` | Front-end startup error+ |
| `0x16476004` | TF tree abnormal+ |
| `0x16476005` | `circular_tracking` error+ |
| `0x16476006` | DSP translation KLT abnormal+ |
| `0x16476007` | DSP EIS KLT abnormal+ |
| `0x16476008` | Input Harris point count exceeds maximum setting+ |
| `0x16476009` | Camera parameters not updated+ |
| `0x16476100` | VIO dynamic image-slicing abnormal+ |
| `0x16476101` | Dynamic image-slicing initialization abnormal+ |
| `0x16476102` | Dynamic image-slicing parameter abnormal+ |
| `0x16476103` | `acc_rectify_channel_update` abnormal+ |
| `0x16476104` | `insert_rectify_one_channel` abnormal+ |
| `0x16476105` | `ss_dbus_shm_acquire` abnormal+ |
| `0x16476106` | `ss_dbus_shm_publish` abnormal+ |
| `0x16476107` | Camera-parameter retrieval timed out+ |
| `0x16479000` | V1-RTK function abnormal+ |
| `0x16479001` | RTK initialization abnormal+ |
| `0x16479002` | RTK DSP execution abnormal+ |
| `0x16479003` | RTK process scheduling abnormal+ |
| `0x16479004` | RTK output frequency abnormal+ |
| `0x16479005` | RTK MIPI data abnormal+ |
| `0x16479006` | RTK device driver abnormal+ |
| `0x16479011` | RTK device configuration abnormal+ |
| `0x16479012` | RTK initialization resource allocation abnormal+ |
| `0x16479013` | MIPI initialization abnormal+ |
| `0x16479014` | RTK initialization parameter configuration abnormal+ |
| `0x16479015` | RTK firmware version mismatch+ |
| `0x16479021` | RTK operator abnormally hung+ |
| `0x16479022` | RTK operator execution timeout+ |
| `0x16479031` | RTK system interrupt abnormal+ |
| `0x16479032` | RTK system real-time abnormal+ |
| `0x16479041` | RTK timing error+ |
| `0x16479051` | RTK MIPI data sync error+ |
| `0x16479052` | RTK MIPI data frame drop+ |
| `0x1647C010` | Compass requires calibration+ |
| `0x1647C011` | Compass magnitude too large — calibration required+ |
| `0x1647C012` | Compass yaw error large — calibration required+ |
| `0x1647C013` | Compass yaw inconsistent — calibration required+ |
| `0x1647C014` | Compass magnitude inconsistent — calibration required+ |
| `0x1647C015` | Compass heading inconsistent — calibration required+ |
| `0x1647C016` | Compass not calibrated over long distance — calibration required+ |
| `0x1647C017` | Compass not calibrated for a long time — calibration required+ |
| `0x1647C018` | Compass abnormal for a long time — calibration required+ |
| `0x1647C019` | Compass heading inconsistent with fusion heading — calibration required+ |
| `0x1647C020` | Move the aircraft+ |
| `0x1647C021` | After compass calibration, magnitude too large — move the aircraft+ |
| `0x1647C022` | After compass calibration, yaw error large — move the aircraft+ |
| `0x1647C023` | After compass calibration, yaw inconsistent — move the aircraft+ |
| `0x1647C024` | After compass calibration, magnitude inconsistent — move the aircraft+ |
| `0x1647C025` | After compass calibration, heading inconsistent — move the aircraft+ |
| `0x1647C030` | Move the aircraft or wait for RTK-FIX+ |
| `0x1647C031` | After compass calibration, magnitude too large — move the aircraft or wait for RTK-FIX+ |
| `0x1647C032` | After compass calibration, yaw error large — move the aircraft or wait for RTK-FIX+ |
| `0x1647C033` | After compass calibration, yaw inconsistent — move the aircraft or wait for RTK-FIX+ |
| `0x1647C034` | After compass calibration, magnitude inconsistent — move the aircraft or wait for RTK-FIX+ |
| `0x1647C035` | After compass calibration, heading inconsistent — move the aircraft or wait for RTK-FIX+ |
| `0x1647C040` | Compass requires calibration or wait for RTK-FIX+ |
| `0x1647C041` | Compass magnitude too large — calibration required or wait for RTK-FIX+ |
| `0x1647C042` | Compass yaw error large — calibration required or wait for RTK-FIX+ |
| `0x1647C043` | Compass yaw inconsistent — calibration required or wait for RTK-FIX+ |
| `0x1647C044` | Compass magnitude inconsistent — calibration required or wait for RTK-FIX+ |
| `0x1647C045` | Compass heading inconsistent — calibration required or wait for RTK-FIX+ |
| `0x1647C046` | Compass not calibrated over long distance — calibration required or wait for RTK-FIX+ |
| `0x1647C047` | Compass not calibrated for a long time — calibration required or wait for RTK-FIX+ |
| `0x1647C048` | Compass abnormal for a long time — calibration required or wait for RTK-FIX+ |

<details><summary>CN source (verbatim from HMS.json)</summary>

| Alarm ID | `tipEn` (original CN) |
|---|---|
| `0x16471000` | 定位无输出，可能是FC传感器未就绪 |
| `0x16471001` | 定位异常，系统异常或loading异常 |
| `0x16471002` | 定位输出速度位置一致性差 |
| `0x16471003` | 飞控传感器未就绪 |
| `0x16471004` | 状态实时性delay太大 |
| `0x16471005` | loop耗时异常 |
| `0x16471006` | 状态时间戳异常 |
| `0x16471007` | IMU BIAS随机游走异常 |
| `0x16471010` | 视觉定位多方向同步异常 |
| `0x16471012` | 硬件加速器调用异常 |
| `0x16471100` | IMU 时间戳异常 |
| `0x16471101` | 视觉时间戳异常 |
| `0x16471102` | UBLOX GPS时间戳异常 |
| `0x16471103` | DJI GPS时间戳异常 |
| `0x16471201` | IMU静止检测更新异常 |
| `0x16471204` | 气压计更新异常 |
| `0x16471205` | TOF更新异常 |
| `0x16471207` | 视觉更新异常 |
| `0x16471209` | GPS更新异常 |
| `0x16476000` | VIO 前端异常 |
| `0x16476001` | 初始化异常 |
| `0x16476002` | 前端启动错误 |
| `0x16476004` | TF树异常 |
| `0x16476005` | circular_tracking错误 |
| `0x16476006` | DSP translation KLT异常 |
| `0x16476007` | DSP eis KLT异常 |
| `0x16476008` | 输入harris点数大于最大设置点数 |
| `0x16476009` | 相机参数未更新 |
| `0x16476100` | VIO 动态切图异常 |
| `0x16476101` | 动态切图初始化异常 |
| `0x16476102` | 动态切图参数异常 |
| `0x16476103` | acc_rectify_channel_update异常 |
| `0x16476104` | insert_rectify_one_channel异常 |
| `0x16476105` | ss_dbus_shm_acquire异常 |
| `0x16476106` | ss_dbus_shm_publish异常 |
| `0x16476107` | 获取相机参数超时 |
| `0x16479000` | V1-RTK功能异常 |
| `0x16479001` | RTK初始化异常 |
| `0x16479002` | RTK DSP运行异常 |
| `0x16479003` | RTK进程调度异常 |
| `0x16479004` | RTK输出频率异常 |
| `0x16479005` | RTK MIPI数据异常 |
| `0x16479006` | RTK 设备驱动异常 |
| `0x16479011` | RTK 设备配置异常 |
| `0x16479012` | RTK初始化资源申请异常 |
| `0x16479013` | MIPI初始化异常 |
| `0x16479014` | RTK初始化参数配置异常 |
| `0x16479015` | RTK固件版本不匹配 |
| `0x16479021` | RTK算子异常挂死 |
| `0x16479022` | RTK算子运行超时 |
| `0x16479031` | RTK系统中断异常 |
| `0x16479032` | RTK系统实时性异常 |
| `0x16479041` | RTK时序错误 |
| `0x16479051` | RTK MIPI数据同步错误 |
| `0x16479052` | RTK MIPI数据丢帧 |
| `0x1647C010` | 指南针需要校准 |
| `0x1647C011` | 指南针模长过大，需要校准 |
| `0x1647C012` | 指南针Yaw误差大，需要校准 |
| `0x1647C013` | 指南针yaw不一致，需要校准 |
| `0x1647C014` | 指南针模长不一致，需要校准 |
| `0x1647C015` | 指南针航向不一致，需要校准 |
| `0x1647C016` | 指南针长距离未校准，需要校准 |
| `0x1647C017` | 指南针长时间未校准，需要校准 |
| `0x1647C018` | 指南针长时间异常，需要校准 |
| `0x1647C019` | 指南针航向与融合航向不一致，需要校准 |
| `0x1647C020` | 需要移动飞机 |
| `0x1647C021` | 指南针校准完后模长过大，需要移动飞机 |
| `0x1647C022` | 指南针校准完后Yaw误差大，需要移动飞机 |
| `0x1647C023` | 指南针校准完后yaw不一致，需要移动飞机 |
| `0x1647C024` | 指南针校准完后模长不一致，需要移动飞机 |
| `0x1647C025` | 指南针校准完后航向不一致，需要移动飞机 |
| `0x1647C030` | 需要移动飞机或等待RTK-FIX |
| `0x1647C031` | 指南针校准完后模长过大，需要移动飞机或等待RTK-FIX |
| `0x1647C032` | 指南针校准完后Yaw误差大，需要移动飞机或等待RTK-FIX |
| `0x1647C033` | 指南针校准完后yaw不一致，需要移动飞机或等待RTK-FIX |
| `0x1647C034` | 指南针校准完后模长不一致，需要移动飞机或等待RTK-FIX |
| `0x1647C035` | 指南针校准完后航向不一致，需要移动飞机或等待RTK-FIX |
| `0x1647C040` | 指南针需要校准或等待RTK-FIX |
| `0x1647C041` | 指南针模长过大，需要校准或等待RTK-FIX |
| `0x1647C042` | 指南针Yaw误差大，需要校准或等待RTK-FIX |
| `0x1647C043` | 指南针yaw不一致，需要校准或等待RTK-FIX |
| `0x1647C044` | 指南针模长不一致，需要校准或等待RTK-FIX |
| `0x1647C045` | 指南针航向不一致，需要校准或等待RTK-FIX |
| `0x1647C046` | 指南针长距离未校准，需要校准或等待RTK-FIX |
| `0x1647C047` | 指南针长时间未校准，需要校准或等待RTK-FIX |
| `0x1647C048` | 指南针长时间异常，需要校准或等待RTK-FIX |

</details>

## 0x1649** — Internal — Planner & global map (CN+) (47 codes)

| Alarm ID | Tip |
|---|---|
| `0x16490001` | Tracking planner exited abnormally+ |
| `0x16490002` | Tracking planner parameters invalid+ |
| `0x16490004` | Tracking planner follow failed+ |
| `0x16490005` | Tracking planner map timeout+ |
| `0x16490006` | Tracking planner map null pointer+ |
| `0x16490007` | Tracking planner obstacle-avoidance exited abnormally+ |
| `0x16490008` | Tracking planner target-safety abnormal+ |
| `0x16490009` | Tracking planner trajectory-follow abnormal+ |
| `0x1649000A` | Tracking planner target-estimation error+ |
| `0x1649000B` | Tracking planner failed+ |
| `0x1649000C` | Tracking planner emergency brake+ |
| `0x1649000D` | Tracking planner smoothness abnormal+ |
| `0x1649000E` | Tracking planner trajectory detection abnormal+ |
| `0x1649000F` | Tracking planner brake-planning abnormal+ |
| `0x16490010` | Tracking planner path-planning abnormal+ |
| `0x16490011` | Tracking planner trajectory-planning abnormal+ |
| `0x16493000` | Global map: cannot receive high-frequency MCU push `fly_core`+ |
| `0x16493100` | Global map: cannot receive low-frequency MCU push `fly_extend`+ |
| `0x16493200` | Global map: cannot obtain valid positioning data `fusion_output`+ |
| `0x16493300` | Global map: cannot obtain valid calibration data+ |
| `0x16493400` | Global map: cannot obtain valid sky semantics+ |
| `0x16493500` | Global map: cannot obtain valid local map+ |
| `0x16493600` | Global map: local-map processing failed or timed out+ |
| `0x16494000` | APAS Planner malfunction+ |
| `0x16494001` | Local-map subscription abnormal+ |
| `0x16494002` | Environment speed-limit subscription abnormal+ |
| `0x16494003` | APAS Planner blocked+ |
| `0x16494004` | APAS Follower blocked+ |
| `0x16494100` | APAS Planner performance abnormal+ |
| `0x16494101` | APAS Planner local-map shared-memory timeout+ |
| `0x16494102` | APAS Planner initial trajectory solve failed+ |
| `0x16494103` | APAS Planner detour trajectory solve failed+ |
| `0x16494104` | APAS Planner triggered emergency brake+ |
| `0x16494105` | APAS Follower tracking error too large+ |
| `0x16494106` | APAS Follower control-sequence collision check failed+ |
| `0x16497100` | Terrain-follow detour abnormal+ |
| `0x16497110` | Terrain-follow detour task setting abnormal+ |
| `0x16497111` | Terrain-follow detour task altitude abnormal+ |
| `0x16497112` | Terrain-follow detour task speed abnormal+ |
| `0x16497113` | Terrain-follow detour task wayline setting abnormal+ |
| `0x16497120` | Terrain-follow detour perception input abnormal+ |
| `0x16497121` | Terrain-follow detour mapping abnormal+ |
| `0x16497122` | Terrain-follow detour map timeout+ |
| `0x16497130` | Terrain-follow detour planning failed+ |
| `0x16497131` | Terrain-follow detour search path invalid+ |
| `0x16497132` | Terrain-follow detour search failed+ |
| `0x16497133` | Terrain-follow detour trajectory optimization failed+ |

<details><summary>CN source (verbatim from HMS.json)</summary>

| Alarm ID | `tipEn` (original CN) |
|---|---|
| `0x16490001` | tracking planner异常退出 |
| `0x16490002` | tracking planner参数无效 |
| `0x16490004` | tracking planner跟随失败 |
| `0x16490005` | tracking planner地图超时 |
| `0x16490006` | tracking planner地图空指针 |
| `0x16490007` | tracking planner避障异常退出 |
| `0x16490008` | tracking planner目标安全性异常 |
| `0x16490009` | tracking planner轨迹跟随异常 |
| `0x1649000A` | tracking planner目标估计错误 |
| `0x1649000B` | tracking planner失效 |
| `0x1649000C` | tracking planner紧急刹车 |
| `0x1649000D` | tracking planner平滑性异常 |
| `0x1649000E` | tracking planner轨迹检测异常 |
| `0x1649000F` | tracking planner刹车规划异常 |
| `0x16490010` | tracking planner路径规划异常 |
| `0x16490011` | tracking planner轨迹规划异常 |
| `0x16493000` | 全局地图：拿不到MCU的高频推送 fly_core |
| `0x16493100` | 全局地图：拿不到MCU的低频推送 fly_extend |
| `0x16493200` | 全局地图：拿不到有效的定位数据 fusion_output |
| `0x16493300` | 全局地图：拿不到有效的标定数据 |
| `0x16493400` | 全局地图：拿不到有效的天空语义 |
| `0x16493500` | 全局地图：拿不到有效的局部地图 |
| `0x16493600` | 全局地图：局部地图处理失败/超时 |
| `0x16494000` | APAS Planner 功能异常 |
| `0x16494001` | 局部地图订阅异常 |
| `0x16494002` | 环境限速订阅异常 |
| `0x16494003` | APAS Planner 阻塞 |
| `0x16494004` | APAS Follower 阻塞 |
| `0x16494100` | APAS Planner 性能异常 |
| `0x16494101` | APAS Planner 局部地图共享内存超时 |
| `0x16494102` | APAS Planner 初始轨迹求解失败 |
| `0x16494103` | APAS Planner 绕行轨迹求解失败 |
| `0x16494104` | APAS Planner 触发紧急刹车 |
| `0x16494105` | APAS Follower 跟踪误差过大 |
| `0x16494106` | APAS Follower 控制序列碰撞检查失败 |
| `0x16497100` | 仿地绕行异常 |
| `0x16497110` | 仿地绕行任务设置异常 |
| `0x16497111` | 仿地绕行任务高度异常 |
| `0x16497112` | 仿地绕行任务速度异常 |
| `0x16497113` | 仿地绕行任务航线设置异常 |
| `0x16497120` | 仿地绕行感知输入异常 |
| `0x16497121` | 仿地绕行建图异常 |
| `0x16497122` | 仿地绕行地图超时 |
| `0x16497130` | 仿地绕行规划失败 |
| `0x16497131` | 仿地绕行搜索路径无效 |
| `0x16497132` | 仿地绕行搜索失败 |
| `0x16497133` | 仿地绕行轨迹优化失败 |

</details>

## 0x164A** — Internal — Flight control loops (CN+) (10 codes)

| Alarm ID | Tip |
|---|---|
| `0x164a0001` | Vertical altitude control abnormal+ |
| `0x164a0002` | Vertical velocity control abnormal+ |
| `0x164a0003` | Vertical altitude feedback abnormal+ |
| `0x164a0004` | Vertical velocity feedback abnormal+ |
| `0x164a0005` | Vertical power saturation abnormal+ |
| `0x164a1001` | Horizontal control abnormal+ |
| `0x164a1002` | Horizontal velocity control abnormal+ |
| `0x164a1003` | Horizontal velocity feedback abnormal+ |
| `0x164a1004` | Attitude control abnormal+ |
| `0x164A1005` | In No Position Hold mode, aircraft is unable to hover stably. It is recommended to switch to Normal mode |

<details><summary>CN source (verbatim from HMS.json)</summary>

| Alarm ID | `tipEn` (original CN) |
|---|---|
| `0x164a0001` | 垂直高度控制异常 |
| `0x164a0002` | 垂直速度控制异常 |
| `0x164a0003` | 垂直高度反馈异常 |
| `0x164a0004` | 垂直速度反馈异常 |
| `0x164a0005` | 垂直动力饱和异常 |
| `0x164a1001` | 水平控制异常 |
| `0x164a1002` | 水平速度控制异常 |
| `0x164a1003` | 水平速度反馈异常 |
| `0x164a1004` | 姿态控制异常 |

</details>

## 0x1667** — Power Line Follow (33 codes)

| Alarm ID | Tip |
|---|---|
| `0x16670000` | No power lines identified ahead. Power Line Follow task ended (%alarmid) |
| `0x16670001` | Home Point not set. Check and update Home Point (%alarmid) |
| `0x16670002` | GNSS signal weak. Power Line Follow task stopped (%alarmid) |
| `0x16670003` | Power Line Follow in progress. Stop task and try again (%alarmid) |
| `0x16670004` | Power Line Follow not supported by current payload type (%alarmid) |
| `0x16670005` | GNSS signal weak. Power Line Follow task stopped (%alarmid) |
| `0x16670006` | Remote controller signal lost. Power Line Follow task stopped (%alarmid) |
| `0x16670101` | Too close to obstacle. Power Line Follow task stopped (%alarmid) |
| `0x16670102` | Approaching ground. Power Line Follow task stopped (%alarmid) |
| `0x16670103` | Approaching Altitude Zone. Power Line Follow task stopped (%alarmid) |
| `0x16670104` | Reaching max flight distance. Power Line Follow task stopped (%alarmid) |
| `0x16670105` | Approaching GEO Zone. Power Line Follow task stopped (%alarmid) |
| `0x16670106` | Approaching Altitude Zone. Power Line Follow task stopped (%alarmid) |
| `0x16670107` | Identifying power lines (%alarmid) |
| `0x16670108` | Identifying power lines (%alarmid) |
| `0x16670201` | Payload communication link error. Power Line Follow task stopped (%alarmid) |
| `0x16670202` | LiDAR communication link error. Power Line Follow task stopped (%alarmid) |
| `0x16670203` | Error in receiving point cloud data. Power Line Follow task stopped (%alarmid) |
| `0x16670204` | Point cloud recording stopped. Power Line Follow task stopped (%alarmid) |
| `0x16670301` | Flight speed in Power Line Follow exceeds limit. Change settings (%alarmid) |
| `0x16670302` | Flight altitude in Power Line Follow exceeds limit. Change settings (%alarmid) |
| `0x16670303` | Gimbal tilt angle exceeds limit. Change settings (%alarmid) |
| `0x16670304` | Failed to identify power lines. Try again (%alarmid) |
| `0x16670305` | Failed to identify power lines. Try again (%alarmid) |
| `0x16670401` | Failed to recenter gimbal. Try again (%alarmid) |
| `0x16670402` | Failed to set gimbal tilt angle. Try again (%alarmid) |
| `0x16670403` | Failed to start recording point cloud. Try again (%alarmid) |
| `0x16670501` | Power Line Follow task ended (%alarmid) |
| `0x16670502` | Aircraft returning to home or landing. Power Line Follow task stopped (%alarmid) |
| `0x16670503` | Too close to crewed aircraft. Power Line Follow task stopped (%alarmid) |
| `0x16670504` | Power Line Follow task stopped (%alarmid) |
| `0x16670505` | Failed to obtain camera view. Power Line Follow task stopped (%alarmid) |
| `0x16670506` | Failed to calibrate IMU. Try again (%alarmid) |

## Contextual suffixes

Alarm IDs in this prefix include trailing suffixes that denote DJI-emitted variants of the same base code in different flight or airframe contexts:

- `_in_the_sky` — 1 entry/entries.
- `_pm320` — 2 entry/entries.
- `_wm265` — 1 entry/entries.

---

**Source**: [`DJI_Cloud/HMS.json`](../../DJI_Cloud/HMS.json) (DJI v1.15 authoritative).

**See also**: 
- Event definition — [`mqtt/dock-to-cloud/events/hms.md`](../mqtt/dock-to-cloud/events/hms.md).
- Topic-level overview — [`mqtt/README.md`](../mqtt/README.md).
- General API error codes (distinct from HMS alarms) — [`error-codes/README.md`](../error-codes/README.md).
