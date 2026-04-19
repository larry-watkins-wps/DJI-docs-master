# `return_home` — one-key return

Cloud command that triggers one-key return-to-home. The aircraft exits the current wayline and returns to the landing dock (single-dock) or the dock designated by [`return_specific_home`](return_specific_home.md) (multi-dock).

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `return_home` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `return_home` |

## Down — `data` fields

`null` — no payload fields required.

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success. |
| `output.status` | enum string | Task state: `sent`, `in_progress`, `paused`, `ok`, `canceled`, `rejected`, `failed`, `timeout`. |

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/50.wayline.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Wayline-Management.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-WaylineManagement.txt]` | v1.15 (Dock 3) — DJI sources show no example for this method; only the schema tables. |
