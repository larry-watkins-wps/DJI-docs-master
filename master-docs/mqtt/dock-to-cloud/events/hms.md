# `hms` — Health Management System warning push

Event pushed by the dock carrying a batch of Health Management System (HMS) warnings. Each entry names a warning code, a module, a severity level, and a `{component_index, sensor_index}` pair that the cloud uses to look up human-readable copy in the bundled `hms.json` dictionary. The full warning-code catalog lives in [`hms-codes/`](../../../hms-codes/README.md); this doc covers only how HMS warnings are transported over MQTT.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `hms` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `list` | array&lt;struct&gt; | Up to 20 warnings per event (`size: 20`). |
| `list[].level` | enum int | `0` = Notification; `1` = Reminder; `2` = Warning. |
| `list[].module` | enum int | Event module. `0` = Flight mission; `1` = Device management; `2` = Media; `3` = HMS. |
| `list[].in_the_sky` | enum int | `0` = aircraft on the ground; `1` = aircraft in the sky. |
| `list[].code` | string | Warning code. Hex form like `0x16100083`. Full catalog in [`hms-codes/`](../../../hms-codes/README.md) (1,769 alarms across 14 first-byte prefixes). |
| `list[].device_type` | string | Device type emitting the warning. Format `{domain}-{type}-{subtype}`. See DJI Product Support reference. |
| `list[].imminent` | enum int | `0` = not imminent (persistent condition); `1` = imminent (transient — e.g., wind spike will clear when wind drops). |
| `list[].args` | struct | Parameters used to resolve the warning copy. |
| `list[].args.component_index` | integer | Copy variable. Key into the `hms.json` dictionary. |
| `list[].args.sensor_index` | integer | Copy variable. Key into the `hms.json` dictionary. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "list": [
      {
        "args": {
          "component_index": 0,
          "sensor_index": 0
        },
        "code": "0x16100083",
        "device_type": "0-67-0",
        "imminent": 1,
        "in_the_sky": 0,
        "level": 2,
        "module": 3
      }
    ]
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "hms"
}
```

## Relationship to other methods

- Warning-code catalog lives in [`DJI_Cloud/HMS.json`](../../../../DJI_Cloud/HMS.json) (structured) — curated in [`hms-codes/`](../../../hms-codes/README.md). Note: [`DJI_Cloud/DJI_CloudAPI-HMS-Codes.txt`](../../../../DJI_Cloud/DJI_CloudAPI-HMS-Codes.txt) is misnamed; despite the "HMS" label, its content is the general API error-code reference (not HMS alarms) — documented in [`error-codes/README.md`](../../../error-codes/README.md).
- This event is the sole MQTT vehicle for HMS fault transport — no request/service pairing exists.
- Full HMS event-handling choreography will be documented in Phase 9 workflow `workflows/hms-event-reporting.md`.

## Source differences

- **`module` enum label for HMS.** v1.11 Dock 2 and v1.15 Dock 2 label module `3` as `"hms"` (lowercase); v1.15 Dock 3 labels it as `"HMS"` (uppercase). Numeric value `3` is stable.
- **`level` / `code` label wording.** v1.11 Dock 2 + v1.15 Dock 2 use "Alarm level" / "Alarm code" / "Health alert list"; v1.15 Dock 3 uses "Warning level" / "Warning code" / "Health warning list". Semantics identical.
- **`need_reply` not set.** Every source's example omits `need_reply`; standard envelope default applies (no reply expected, fire-and-forget). Unlike [`airsense_warning`](airsense_warning.md) and [`flight_areas_sync_progress`](flight_areas_sync_progress.md), `hms` does not carry `need_reply: 1`.

## Source inconsistencies flagged by DJI's own example

- **Dock 3 `"timestamp:"` trailing-colon typo.** The Dock 3 v1.15 source example uses the key `"timestamp:"` with a trailing colon (`"timestamp:": 1654070968655`) — same class of source typo seen pervasively in 4e-1's Remote-Debugging source. Dock 2 v1.15 and v1.11 Dock 2 use the correct `"timestamp"` key. Cloud implementations must accept/emit the correct key on the wire.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/60.hms.md]` | v1.11 canonical (Dock 2) — "Alarm level" labels, `hms` module label lowercase. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-HMS.txt]` | v1.15 (Dock 2) — identical payload to v1.11. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-HMS.txt]` | v1.15 (Dock 3) — "Warning level" labels, `HMS` module label uppercase, carries the `"timestamp:"` trailing-colon source typo. |
