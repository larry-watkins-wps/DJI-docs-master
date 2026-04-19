# `custom_data_transmission_from_psdk` — passthrough push from PSDK payload to cloud

Event carrying an opaque short payload emitted by a third-party PSDK payload. The dock does not interpret the content — this is the **PSDK-Interconnection** passthrough channel: the PSDK payload calls a vendor SDK function, and the dock relays the bytes to the cloud over MQTT. The cloud side is responsible for parsing the `value` according to whatever protocol the payload developer established.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — PSDK-Interconnection. Payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `custom_data_transmission_from_psdk` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `value` | string | Opaque text content pushed by the PSDK payload. Length < 256 bytes. Format is defined by the payload developer. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "data": {
    "value": "hello world"
  },
  "gateway": "4TADKAQ000002J",
  "method": "custom_data_transmission_from_psdk",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "timestamp": 1689911315621
}
```

## Relationship to other methods

- Cloud-to-PSDK direction: [`custom_data_transmission_to_psdk`](../services/custom_data_transmission_to_psdk.md).
- ESDK (aircraft-side onboard SDK) passthrough uses the sibling pair [`custom_data_transmission_from_esdk`](custom_data_transmission_from_esdk.md) / [`custom_data_transmission_to_esdk`](../services/custom_data_transmission_to_esdk.md).
- Higher-level PSDK widget / speaker state is carried by the dedicated methods in the PSDK family — this passthrough is for payload-specific protocols the dock doesn't natively understand.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/150.psdk-transmit-custom-data.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-PSDK-Interconnection.txt]` | v1.15 (Dock 2) — identical. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-PSDK-Interconnection.txt]` | v1.15 (Dock 3) — identical. |
