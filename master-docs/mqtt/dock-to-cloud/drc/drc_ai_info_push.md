# `drc_ai_info_push` — AI identify / tracking state push

Event pushed by the aircraft reporting the AI-identify subsystem's state: identification switch, tracking switch, list of loaded AI models, currently-selected model configuration, and the current tracking state + reason. Used by the pilot UI to render the AI toolbar and by cloud workflows to orchestrate search-and-rescue / counting modes.

Part of the Phase 4 MQTT catalog. Shared conventions (envelope) live in [`../../README.md`](../../README.md).

**Cohort**: **Dock 3 only** — absent from Dock 2 Remote-Control.

---

## Topics

| Direction | Topic | Method |
|---|---|---|
| Device → Cloud | `thing/product/{gateway_sn}/drc/up` | `drc_ai_info_push` |

## Up — `data` fields

### Top-level

| Field | Type | Description |
|---|---|---|
| `identify_on` | enum int | Global identification switch. `0` = Off, `1` = On. Paired with [`drc_ai_identify_set`](drc_ai_identify_set.md). |
| `spotlight_zoom_on` | enum int | Global AI-tracking switch. `0` = Off, `1` = On. Paired with [`drc_ai_spotlight_zoom_set`](drc_ai_spotlight_zoom_set.md). |
| `ai_spotlight_zoom` | struct | Current tracking state (see below). |
| `ai_model_list` | array of struct | Available AI models on the device. |
| `selected_ai_model` | struct | Currently-selected model's configuration. |

### `ai_spotlight_zoom`

| Field | Type | Description |
|---|---|---|
| `state` | enum int | `0` = Idle, `1` = Waiting for Selection, `2` = Waiting for Confirmation, `3` = Tracking. |
| `state_reason` | enum int | Reason for the current state. `0`–`15` are "during tracking" reasons (`0` = Normal, `14` = Tracking target lost, etc.); `160`–`168` are **exit reasons** (`160` = Normal Exit, `161` = Unsupported payload, `162` = Unsupported camera mode, `163` = Invalid command, `164` = Positioning failed, `165` = Aircraft not takeoff, `166` = Flight mode error, `167` = Mode unavailable (RTH / landing / attitude), `168` = Lost RC or video-link signal). Full enum in DJI source. |

### `ai_model_list[]`

| Field | Type | Description |
|---|---|---|
| `index` | int | Model index (≥ 0). |
| `signed_name` | string | Signed model name. |

### `selected_ai_model`

| Field | Type | Description |
|---|---|---|
| `index` | int | Index of the selected model. |
| `score` | int | Current recognition confidence, `0`–`100`. |
| `score_mode` | enum int | `0` = Invalid, `1` = Counting Mode, `2` = Search & Rescue Mode, `3` = User-Defined Mode. |
| `image_source` | enum list | Code streams supported by the model. `1` = Wide, `2` = Zoom, `3` = Infrared, `7` = Visible light. |
| `digital_effect` | enum list | Supported IR palettes. `0` = White Hot, `1` = Black Hot, `2` = Red Hot. |
| `filters` | array of int | Current target-filter list. **For third-party models, `filters` values are `label_index + 128`** (e.g. label 1 → filter 129). |
| `labels` | array of struct | Labels supported by the model. Each entry: `{index, name}`. |

### Example

```json
{
  "seq": 1,
  "method": "drc_ai_info_push",
  "data": {
    "identify_on": 1,
    "spotlight_zoom_on": 1,
    "ai_spotlight_zoom": {
      "state": 0,
      "state_reason": 0
    },
    "ai_model_list": [
      {
        "index": 0,
        "signed_name": "DJI"
      },
      {
        "index": 128,
        "signed_name": "Highway scene recognition"
      }
    ],
    "selected_ai_model": {
      "index": 0,
      "score": 100,
      "score_mode": 1,
      "image_source": [1, 2, 3],
      "digital_effect": [0, 1, 2],
      "filters": [1, 2, 3],
      "labels": [
        {
          "index": 0,
          "name": "Motorcycle"
        },
        {
          "index": 1,
          "name": "Bicycle"
        }
      ]
    },
    "ai_wayline_state": {
      "sequence_shot": true,
      "wait_control": true,
      "record": true,
      "normal_shot": true,
      "count_down_time": 23,
      "alert_uuid": "xxxxxxxxxxxxxxx"
    }
  }
}
```

## Source inconsistencies flagged by DJI's own example

- **`ai_wayline_state` sub-struct appears in the example but not in the schema table.** DJI's example shows fields `sequence_shot`, `wait_control`, `record`, `normal_shot`, `count_down_time`, `alert_uuid`. The schema documents `ai_spotlight_zoom` but not `ai_wayline_state`. Treat the example as authoritative evidence that `ai_wayline_state` can appear on the wire, but the field semantics are undocumented.
- **`state_reason` enum intermixes two regimes** — 0–15 are in-tracking reasons, 160–168 are exit reasons. DJI inserts a `Note:` between the two blocks rather than splitting them into separate fields; a cloud implementation must branch on value.

## Source provenance

| Source | Role |
|---|---|
| `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt]` | v1.15 (Dock 3) — only source. |
