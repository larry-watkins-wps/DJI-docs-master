# `custom_data_transmission_to_esdk` — passthrough push from cloud to ESDK (onboard-SDK)

Cloud command delivering an opaque short payload to an ESDK application (aircraft-side onboard SDK) via the dock and aircraft link. The dock does not interpret the content — this is the **ESDK-Interconnection** passthrough channel: the cloud sends bytes, the dock relays them to the aircraft, the aircraft forwards them to the ESDK application, which decodes according to whatever protocol the ESDK developer established.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — ESDK-Interconnection. Payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `custom_data_transmission_to_esdk` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `custom_data_transmission_to_esdk` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `value` | string | Opaque text content pushed to the ESDK application. Length < 256 bytes. Format is defined by the ESDK developer. |

### Example (down)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "data": {
    "value": "hello world"
  },
  "method": "custom_data_transmission_to_esdk",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "timestamp": 1689740550047
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = relayed to the ESDK application. Non-zero represents an error (e.g., aircraft not reachable, ESDK not running). |

### Example (reply)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "data": {
    "result": 0
  },
  "method": "custom_data_transmission_to_esdk",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "timestamp": 1689740550047
}
```

## Relationship to other methods

- ESDK-to-cloud direction: [`custom_data_transmission_from_esdk`](../events/custom_data_transmission_from_esdk.md).
- PSDK (payload-side SDK) passthrough uses the sibling pair [`custom_data_transmission_from_psdk`](../events/custom_data_transmission_from_psdk.md) / [`custom_data_transmission_to_psdk`](custom_data_transmission_to_psdk.md).

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/160.esdk-transmit-custom-data.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-ESDK-Interconnection.txt]` | v1.15 (Dock 2) — identical. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-ESDK-Interconnection.txt]` | v1.15 (Dock 3) — identical. |
