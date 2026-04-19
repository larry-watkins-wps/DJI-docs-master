# `sdr_workmode_switch` — select SDR-only vs SDR+4G image transmission

Cloud command that switches the enhanced image-transmission link between SDR-only and SDR+4G (both channels active in parallel). The reply is a simple `result`-only ACK — unusually for Remote-Debugging, this service does **not** return `output.status`.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `sdr_workmode_switch` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `sdr_workmode_switch` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `link_workmode` | enum int | Video transmission mode. `0` = SDR Only; `1` = 4G Enhanced Mode (both SDR and 4G used simultaneously). |

DJI provides no example JSON for this service.

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | int | Return code. Non-zero represents an error. |

**No `output.status` struct** — the reply shape is minimal. Every other Remote-Debugging service in this file adds `output.status`; this one does not, across both Dock 2 and Dock 3 sources. Treat as intentional variance rather than a transcription error.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt]` | v1.15 (Dock 3). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Debugging.txt]` | v1.15 (Dock 2) — identical; also lacks `output.status` in reply. |
