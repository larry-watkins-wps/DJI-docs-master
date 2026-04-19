# `drc_photo_storage_set` — choose which lens outputs to store per photo (Dock 2 legacy)

DRC command that selects which lens outputs (visible, IR, current) are written to storage when a photo is captured. Dock 3 replaces this with [`photo_storage_set`](../services/photo_storage_set.md) (landed in 4c).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 only**.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_photo_storage_set` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_photo_storage_set` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | string | Camera enumeration. |
| `photo_storage_settings` | array of string | Subset of `current`, `vision`, `ir`. Multi-select. |

### Example

```json
{
  "data": {
    "payload_index": "81-0-0",
    "photo_storage_settings": [
      "current",
      "ir",
      "vision"
    ]
  },
  "method": "drc_photo_storage_set",
  "seq": 1
}
```

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

## Relationship to other methods

- **Dock 3 replacement**: [`photo_storage_set`](../services/photo_storage_set.md) — same enum, standard services envelope.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/180.remote-control.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Control.txt]` | v1.15 (Dock 2) — identical. |
