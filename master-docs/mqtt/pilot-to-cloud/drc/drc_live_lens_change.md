# `drc_live_lens_change` — switch live-stream lens (DRC channel)

RC-Plus-2-specific DRC variant of [`../../dock-to-cloud/services/live_lens_change.md`](../../dock-to-cloud/services/live_lens_change.md). Same semantic intent — switch the video-source lens (wide / zoom / thermal) for an in-progress livestream — but delivered on the lightweight DRC channel (`/drc/down` + `/drc/up`) instead of the standard services channel.

Part of the Phase 4 MQTT catalog. Shared conventions live in [`../../README.md`](../../README.md).

**Cohort**: **RC Plus 2 Enterprise only.** RC Pro uses the non-prefixed [`live_lens_change`](../../dock-to-cloud/services/live_lens_change.md) on `/services`; RC Plus 2 ships this `drc_*` variant on `/drc/down`.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/drc/down` | `drc_live_lens_change` |
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_live_lens_change` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `payload_index` | text | Camera enumeration in `{type-subtype-gimbalindex}` form. |
| `video_type` | enum_string | `{"thermal": "Infrared", "wide": "Wide-angle", "zoom": "Zoom"}`. |

### Example

```json
{
  "data": {
    "payload_index": "80-0-0",
    "video_type": "zoom"
  },
  "timestamp:": 1654070968655,
  "method": "drc_live_lens_change"
}
```

### Source inconsistencies flagged by DJI's own example

- **`"timestamp:"` trailing-colon typo.** Pervasive across `DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Stream.txt` — matches the Dock 3 pattern first flagged in 4c. The field is `timestamp` on the wire (no colon in the key).
- **`timestamp` on a DRC-envelope message** — the pilot-to-cloud Topic-Definition file explicitly says DRC envelopes carry only `data` + `method` + `seq`. DJI's example here adds `timestamp`, which is harmless (cloud implementations should ignore unknown top-level fields) but inconsistent with the Topic-Definition.
- **No `seq` field in the example.** The DRC envelope schema requires `seq`; DJI's example omits it. Cloud implementations should include `seq` as per the envelope specification.

## Up (reply) — `data` fields

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero = error. |

### Example

```json
{
  "data": {
    "result": 0
  },
  "timestamp:": 1654070968655,
  "method": "drc_live_lens_change"
}
```

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Stream.txt]` | v1.15 (RC Plus 2) — authoritative; only source for this method. |

See also the dock/RC Pro equivalent: [`../../dock-to-cloud/services/live_lens_change.md`](../../dock-to-cloud/services/live_lens_change.md).
