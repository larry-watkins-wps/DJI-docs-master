# `heart_beat` — DRC heartbeat

Bidirectional DRC ping used to keep the DRC session alive and detect link health. **If the device does not receive a heartbeat for more than one minute, it considers the DRC link idle and exits DRC mode** (equivalent to an implicit [`drc_mode_exit`](../services/drc_mode_exit.md)).

Part of the Phase 4 MQTT catalog. Shared conventions (DRC envelope) live in [`../../README.md` §5.8](../../README.md#58-drcup--drcdown--direct-remote-control).

**Cohort**: **Dock 2 + Dock 3** — identical payload.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `heart_beat` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `heart_beat` |

## `data` fields (both directions — identical)

| Field | Type | Description |
|---|---|---|
| `seq` | int | **[Deprecated]** Command sequence. Increments to enforce ordering. Retained for compatibility; new integrations should rely on `timestamp`. |
| `timestamp` | int | Heartbeat send timestamp (13-digit ms Unix time). |

### Example

```json
{
  "method": "heart_beat",
  "data": {
    "timestamp": 1670415891013
  },
  "method": "heart_beat",
  "seq": 1
}
```

> DJI's own example has the `method` key written twice (one valid JSON key would be overwritten by the other during parse). This is a DJI source error, not an intentional wire convention. On the wire, expect a single `method` key plus a single `seq` field at the envelope level (not inside `data`), alongside the `data.timestamp`.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md]` | v1.11 canonical (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt]` | v1.15 (Dock 2). |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
