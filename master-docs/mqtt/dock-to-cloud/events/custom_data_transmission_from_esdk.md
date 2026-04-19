# `custom_data_transmission_from_esdk` — passthrough push from ESDK (onboard-SDK) to cloud

Event carrying an opaque short payload emitted by an ESDK (aircraft-side onboard-SDK) application. The dock does not interpret the content — this is the **ESDK-Interconnection** passthrough channel: the ESDK application on the aircraft calls a vendor SDK function, the aircraft relays to the dock, and the dock forwards the bytes to the cloud over MQTT. The cloud side is responsible for parsing the `value` according to whatever protocol the ESDK developer established.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — ESDK-Interconnection. Payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/events` | `custom_data_transmission_from_esdk` |

## Up — `data` fields

| Field | Type | Description |
|---|---|---|
| `value` | string | Opaque text content pushed by the ESDK application. Length < 256 bytes. Format is defined by the ESDK developer. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "data": {
    "value": "hello world"
  },
  "gateway": "4TADKAQ000002J",
  "method": "custom_data_transmission_from_esdk",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "timestamp": 1689911315621
}
```

## Relationship to other methods

- Cloud-to-ESDK direction: [`custom_data_transmission_to_esdk`](../services/custom_data_transmission_to_esdk.md).
- PSDK (payload-side SDK) passthrough uses the sibling pair [`custom_data_transmission_from_psdk`](custom_data_transmission_from_psdk.md) / [`custom_data_transmission_to_psdk`](../services/custom_data_transmission_to_psdk.md). The distinction: ESDK runs on the aircraft body (e.g., a Manifold), while PSDK runs on a payload device attached to the gimbal port.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/160.esdk-transmit-custom-data.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-ESDK-Interconnection.txt]` | v1.15 (Dock 2) — identical. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-ESDK-Interconnection.txt]` | v1.15 (Dock 3) — identical. |
