# `custom_data_transmission_to_psdk` — passthrough push from cloud to PSDK payload

Cloud command delivering an opaque short payload to a third-party PSDK payload via the dock. The dock does not interpret the content — this is the **PSDK-Interconnection** passthrough channel: the cloud sends bytes, the dock relays them to the attached PSDK payload, which decodes them according to whatever protocol the payload developer established.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — PSDK-Interconnection. Payload identical across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `custom_data_transmission_to_psdk` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `custom_data_transmission_to_psdk` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `value` | string | Opaque text content pushed to the PSDK payload. Length < 256 bytes. Format is defined by the payload developer. |

### Example (down)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "data": {
    "value": "hello world"
  },
  "method": "custom_data_transmission_to_psdk",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "timestamp": 1689740550047
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = relayed to the PSDK payload. Non-zero represents an error (e.g., no PSDK payload attached, relay failure). |

### Example (reply)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "data": {
    "result": 0
  },
  "method": "custom_data_transmission_to_psdk",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "timestamp": 1689740550047
}
```

## Relationship to other methods

- PSDK-to-cloud direction: [`custom_data_transmission_from_psdk`](../events/custom_data_transmission_from_psdk.md).
- ESDK (aircraft-side onboard SDK) passthrough uses the sibling pair [`custom_data_transmission_from_esdk`](../events/custom_data_transmission_from_esdk.md) / [`custom_data_transmission_to_esdk`](custom_data_transmission_to_esdk.md).

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/150.psdk-transmit-custom-data.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-PSDK-Interconnection.txt]` | v1.15 (Dock 2) — identical. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-PSDK-Interconnection.txt]` | v1.15 (Dock 3) — identical. |
