# `live_lens_change` — switch the aircraft lens used for an active stream

Cloud command that switches which lens of a multi-lens aircraft camera is pushed on an in-progress live stream (for example: zoom ↔ wide ↔ infrared on M3D / M3TD / M4D / M4TD). Aircraft-side counterpart to [`live_camera_change`](live_camera_change.md) (which toggles the dock's own FPV cameras).

Part of the Phase 4 MQTT catalog. Shared conventions (envelope, services-reply) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 2 + Dock 3**. v1.11 Dock 2 includes a `video_id` parameter that both v1.15 sources drop — see [Source differences](#source-differences).

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Cloud → Device | `thing/product/{gateway_sn}/services` | `live_lens_change` |
| Device → Cloud | `thing/product/{gateway_sn}/services_reply` | `live_lens_change` |

## Down — `data` fields

| Field | Type | Description |
|---|---|---|
| `video_id` | string | *v1.11 Dock 2 only.* Identifier of the stream whose lens is being switched. Format `{sn}/{camera_index}/{video_index}`. Dropped in v1.15 tables (both Dock 2 and Dock 3). |
| `video_type` | enum string | Target lens. `ir` = Infrared, `normal` = Default, `wide` = Wide-angle, `zoom` = Zoom. |

### Example (v1.11 Dock 2 — with `video_id`)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "video_id": "1581F5BMD228Q00A82XX/39-0-7/zoom-0",
    "video_type": "zoom"
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "live_lens_change"
}
```

### Example (v1.15 — `video_id` absent)

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "video_type": "zoom"
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "live_lens_change"
}
```

## Up (reply) — `data` fields

The reply table declares `Data: null` in every source, but the example carries a standard `result` field. Treat the reply as a standard services_reply envelope.

| Field | Type | Description |
|---|---|---|
| `result` | integer | Return code. `0` = success; non-zero represents an error. |

### Example

```json
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "data": {
    "result": 0
  },
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1654070968655,
  "method": "live_lens_change"
}
```

## Source differences

- **`video_id` parameter**: v1.11 Dock 2 requires both `video_id` and `video_type`; v1.15 Dock 2 and v1.15 Dock 3 list only `video_type`. A server driving a mixed fleet should be prepared to send `video_id` to older dock firmware and send only `video_type` to current firmware. The v1.15 behaviour presumably implies the dock switches the lens on the currently-active stream, but DJI does not explicitly state this — treat as a latent ambiguity if multiple streams are active at once.

## Source inconsistencies flagged by DJI's own example

- Every reply-side table declares `Data: null` while the reply example still includes `data.result`. Treat the example as authoritative; this is DJI's standard reply shape.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/30.live.md]` | v1.11 canonical (Dock 2) — documents `video_id` + `video_type`. |
| `[DJI_Cloud/DJI_CloudAPI-Dock2-Live-Stream.txt]` | v1.15 (Dock 2) — drops `video_id` from the request. |
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Live-Stream.txt]` | v1.15 (Dock 3) — identical to Dock 2 v1.15. |
