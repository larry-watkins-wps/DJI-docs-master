# HMS codes — 0x12** (Battery Station)

Prefix byte `0x12`. 37 alarm codes.

The prefix byte is the wire-level grouping DJI uses in the `data.list[].code` field emitted on [`thing/product/{gateway_sn}/events` method `hms`](../mqtt/dock-to-cloud/events/hms.md). The domain label above is inferred from the tip text — DJI does not publish an official prefix taxonomy.

Entries rendered with a trailing **+** have a curated CN→EN translation because the original `tipEn` value in [`HMS.json`](../../DJI_Cloud/HMS.json) contains Chinese-language developer-debug strings under the "English" field. The CN originals are preserved below each subsection in a `CN source` callout so the audit trail is intact.

| Alarm ID | Tip |
|---|---|
| `0x12000000` | Activate the Battery Station as instructed by the user manual. Contact your local dealer or DJI Support for assistance |
| `0x12000001` | Restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12000002` | Restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12010000` | Restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12010001` | Try adjusting the power plug or changing the charging cable and restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12010002` | Try adjusting the power plug or changing the charging cable and restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12010003` | Restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12010004` | Restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12010005` | Restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12010006` | Restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12010007` | Restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12010008` | Power off the Battery Station. Wait for the temperature to return to normal before use. If the issue persists, contact your local dealer or DJI Support |
| `0x12020000` | Check the battery ports, reinsert the batteries, or restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12020001` | Wait for the battery temperature to return to normal before charging. If the issue persists, contact your local dealer or DJI Support |
| `0x12020002` | Remove the battery and wait for the temperature to return to normal before charging. If the issue persists, contact your local dealer or DJI Support |
| `0x12020003` | Reinsert the batteries, try other battery ports, or restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12020004` | Reinsert the batteries, try other battery ports, or restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12020005` | Reinsert the batteries, try other battery ports, or restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12020006` | Reinsert the batteries, try other battery ports, or restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12020007` | Reinsert the batteries, try other battery ports, or restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12020008` | Reinsert the batteries, try other battery ports, or restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12020009` | Reinsert the batteries, try other battery ports, or restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x1202000A` | Check the battery ports, reinsert the batteries, or restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x1202000B` | Reinsert the batteries, try other battery ports, or restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x1202000C` | Reinsert the batteries, try other battery ports, or restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x1202000D` | Reinsert the batteries, try other battery ports, or restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12030000` | Power off the Battery Station. Wait for the temperature to return to normal before use. If the issue persists, contact your local dealer or DJI Support |
| `0x12030001` | Restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12030002` | Restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12030003` | Check the battery ports, reinsert the batteries, or restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12030004` | 1. Do not connect two AC connectors to the same power strip or socket. Connect the AC wires separately\n2. Do not use connection cables longer than 30 m\n3. Use 6mm² 3-core cable for power supply (%alarmid) |
| `0x12030005` | 1. Change oil regularly based on the maintenance requirements in the generator user manual\n2. Press and hold the Maintenance Complete button on the generator display panel to cancel the alarm (%alarmid) |
| `0x12030006` | 1. Check whether the plug is properly connected with the battery module\n2. Check whether the charging cable is properly connected with charging device controller board (%alarmid) |
| `0x12030007` | 1. Check whether the plug is properly connected with the battery module\n2. Check whether the charging cable is properly connected with charging device controller board (%alarmid) |
| `0x12120000` | Reinsert the batteries, try other battery ports, or restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |
| `0x12120001` | Remove the battery and wait for the battery temperature to return to normal before charging. If the issue persists, contact your local dealer or DJI Support |
| `0x12120002` | Reinsert the batteries, try other battery ports, or restart the Battery Station. If the issue persists, contact your local dealer or DJI Support |

---

**Source**: [`DJI_Cloud/HMS.json`](../../DJI_Cloud/HMS.json) (DJI v1.15 authoritative).

**See also**: 
- Event definition — [`mqtt/dock-to-cloud/events/hms.md`](../mqtt/dock-to-cloud/events/hms.md).
- Topic-level overview — [`mqtt/README.md`](../mqtt/README.md).
- General API error codes (distinct from HMS alarms) — [`error-codes/README.md`](../error-codes/README.md).
