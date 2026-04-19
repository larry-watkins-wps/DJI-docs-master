# GET /manage/api/v1/workspaces/{workspace_id}/devices/topologies

Fetch the list of all devices and their gateway-to-sub-device topology in a workspace. Pilot 2 calls this endpoint on first connection, and again any time it receives a `device_online` / `device_offline` / `device_update_topo` WebSocket push — see [`../../websocket/README.md` §5](../../websocket/README.md#5-push-and-fetch-coordination-pattern) for the push-and-fetch pattern.

Part of the Phase 3 HTTP endpoint catalog. Shared conventions (URI form, `X-Auth-Token`, response envelope, status codes) live in [`../README.md`](../README.md) and are not restated here.

---

## Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `workspace_id` | path | string | yes | Workspace ID. |
| `x-auth-token` | header | string | yes | Access token — see [`../README.md` §4](../README.md#4-request-headers). |

## Request body

None.

## Response — 200 OK

`tsa.GetWebPrjDeviceForOpenPlatformRsp`. `data.list` is an array of topology clusters; each cluster has a `hosts` collection (sub-devices, typically aircraft) and a `parents` collection (gateway devices — Docks, RCs).

### `data`

| Field | Type | Description |
|---|---|---|
| `list` | array of `tsa.DeviceTopoRsp` | One entry per topology cluster. |

### `tsa.DeviceTopoRsp`

| Field | Type | Description |
|---|---|---|
| `hosts` | array of `tsa.TopoHostDeviceRsp` | Drone / sub-device topology collection. |
| `parents` | array of `tsa.TopoGatewayDeviceRsp` | Gateway device topology collection. |

### `tsa.TopoHostDeviceRsp` / `tsa.TopoGatewayDeviceRsp`

Same shape for both host (sub-device) and parent (gateway):

| Field | Type | Description |
|---|---|---|
| `sn` | string | Device serial number. |
| `device_model` | `tsa.DeviceModelEnum` | Device model enum — `{key, domain, type, sub_type}`. Full enum catalog in Phase 6 (`device-properties/`). |
| `device_callsign` | string | Device callsign. |
| `user_id` | string | Owner user ID. |
| `user_callsign` | string | Owner callsign. |
| `online_status` | boolean | Current online state. |
| `icon_urls` | object | Optional custom icon for display — `{normal_icon_url, selected_icon_url}`. If omitted, Pilot uses the default icon mapped from `device_model.type`. |

### Example

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "list": [
      {
        "hosts": [
          {
            "sn": "drone01",
            "device_model": {
              "key": "0-60-0",
              "domain": "0",
              "type": "60",
              "sub_type": "0"
            },
            "online_status": true,
            "device_callsign": "Rescue aircraft",
            "user_id": "string",
            "user_callsign": "string",
            "icon_urls": {
              "normal_icon_url": "resource://pilot/drawable/tsa_aircraft_others_normal",
              "selected_icon_url": "resource://pilot/drawable/tsa_aircraft_others_pressed"
            }
          }
        ],
        "parents": [
          {
            "sn": "rc02",
            "online_status": true,
            "device_model": {
              "key": "2-56-0",
              "domain": "2",
              "type": "56",
              "sub_type": "0"
            },
            "device_callsign": "Remote controller",
            "user_id": "string",
            "user_callsign": "string",
            "icon_urls": {
              "normal_icon_url": "resource://pilot/drawable/tsa_aircraft_others_normal",
              "selected_icon_url": "resource://pilot/drawable/tsa_aircraft_others_pressed"
            }
          }
        ]
      }
    ]
  }
}
```

## Relationship to MQTT topology

This HTTP endpoint is the **authoritative read** of topology state. The source of truth is maintained by the cloud from `sys/product/{gateway_sn}/status` with `method: update_topo` messages (see [`../../mqtt/README.md` §5.7](../../mqtt/README.md#57-status--status_reply--topology)). The WebSocket pushes (`device_online` / `device_offline` / `device_update_topo`) are change signals only — they do not carry topology content.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/10.https/40.situation-awareness/10.obtain-device-topology-list.md]` | v1.11 canonical — URI, parameter list, `tsa.*` schemas, full example with aircraft + RC topology. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-SituationAwareness-Obtain-Device-Topology-List.txt]` | v1.15 corroboration — identical. |
