# HTTP Protocol Reference

Conventions for every HTTPS interaction between the in-scope devices (Dock 2, Dock 3, Matrice 3D / 3TD / 4D / 4TD, RC Plus 2 Enterprise, RC Pro Enterprise) and a DJI-Cloud-compatible server. This document is the canonical home for the HTTP envelope, header set, request-method rules, and the error-code-to-app-behavior mapping.

Per-endpoint catalog is Phase 3 under [`http/`](.) (one `.md` per endpoint, grouped by resource).

---

## 1. Scope

- All third-party-cloud HTTPS endpoints exposed to DJI Pilot 2 and DJI Dock.
- Both the Pilot Webview login / token-exchange step and the subsequent business traffic.
- The 17 Pilot-to-Cloud endpoints captured in `DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-*.txt` (v1.15) are within scope; they share the conventions defined here. Per-endpoint detail lives in Phase 3.

Out of scope: the MQTT plane (see [`mqtt/README.md`](../mqtt/README.md)), WebSocket push (see [`websocket/README.md`](../websocket/README.md)), server implementation (databases, auth backends, framework choices).

## 2. URI form

Verbatim (`[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/40.https.md]`):

```
{URI-scheme}://{Endpoint}/{module}/api/{api_version}/{resource_path}?{query_string}
```

| Segment | Description |
|---|---|
| `URI-scheme` | Enforces the use of secure `https` |
| `Endpoint` | Service domain or IP |
| `module` | Function module |
| `api_version` | API version number, used to manage API versions |
| `resource_path` | Resource path |
| `query_string` | Query parameter, not required |

Evidence in the wild — every v1.15 Pilot-to-Cloud endpoint conforms:

- `GET /wayline/api/v1/workspaces/{workspace_id}/waylines` — `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-Waypoint-Obtain-Wayline-List.txt]`

The full module inventory (`wayline`, `media`, `map`, `manage`, ...) is enumerated in the Phase 3 catalog, not here.

## 3. Request methods

Verbatim (`[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/40.https.md]`):

> The following request methods are supported: `GET`, `PUT`, `POST`, `DELETE`. The `Content-Type` of the request should be `application/json`.
>
> Parameter specification:
> - `GET` / `DELETE`: Parameter in query.
> - `POST` / `PUT`: The parameter is in the header, in json format.

**Note on the last line.** DJI's source says "the parameter is in the header" for `POST` / `PUT`. In actual v1.15 Pilot-HTTPS endpoints the JSON parameters travel in the request **body** (with `Content-Type: application/json`), not in a header. This is a wording bug in DJI's documentation; cited verbatim above for fidelity, and every Phase 3 endpoint entry will show the body-carried JSON pattern.

## 4. Request headers

DJI's canonical header table (`[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/40.https.md]`):

| Parameter | Type | Position | Required | Description |
|---|---|---|---|---|
| `X-Auth-Token` | String | header | Yes | Token (access token) |
| `X-Device-ID` | String | header | No | Device ID number — used when the server needs to determine the model to do corresponding processing. Not currently required. |
| `X-Firmware-Version` | String | header | No | Firmware version of the aircraft |
| `X-Request-ID` | String | header | No | UUID identifying an HTTP request |

Authentication is per-request via `X-Auth-Token`, issued during the Pilot Webview login exchange and handed to the Pilot application layer (and through it to the device layer) via JSBridge. See architecture §8 for the relationship to the license-backed MQTT binding.

The v1.15 Pilot-HTTPS extracts spell the header lowercase as `x-auth-token` in the parameter column. HTTP headers are case-insensitive per RFC 7230; both forms are equivalent on the wire.

## 5. Response envelope

Verbatim (`[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/40.https.md]`):

```json
{
  "code": 0,
  "message": "string",
  "data": {}
}
```

| Field | Description |
|---|---|
| `code` | `0` on success; non-zero is a business error code. Distinct from the HTTP status code. The error-code catalog lives in Phase 8 (`error-codes/`). |
| `message` | Human-readable description. `"success"` when `code == 0` in the v1.15 sample traffic. |
| `data` | Response payload. Shape is per-endpoint; see Phase 3 catalog entries. |

Live v1.15 example (`[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-Waypoint-Obtain-Wayline-List.txt]`):

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "list": [
      {
        "id": "uuid",
        "drone_model_key": "0-67-0",
        "favorited": false,
        "name": "New wayline 1",
        "payload_model_keys": ["1-53-0"],
        "template_types": [0],
        "action_type": 0,
        "update_time": 1637158501230,
        "user_name": "string",
        "start_wayline_point": {
          "start_latitude": 22.5799601837589,
          "start_lontitude": 113.942744030171
        }
      }
    ],
    "pagination": {
      "page": 1,
      "page_size": 9,
      "total": 10
    }
  }
}
```

### 5.1 Pagination

List endpoints return a `pagination` object alongside `list` in `data`:

```json
"pagination": {
  "page": 1,
  "page_size": 9,
  "total": 10
}
```

Request parameters `page` and `page_size` are carried as query arguments (e.g., `GET /wayline/api/v1/workspaces/{workspace_id}/waylines?page=1&page_size=9`). This is the `api_render.PagyInfo` schema — canonical sample is in `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-Waypoint-Obtain-Wayline-List.txt]`.

Individual endpoints may add additional query parameters for filtering or ordering (e.g., `favorited`, `order_by`, `template_type`). Those live in the per-endpoint Phase 3 docs.

## 6. HTTP status codes and DJI Pilot 2 behavior

DJI's canonical status-code taxonomy (`[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/40.https.md]`):

- **2xx** — success. `200` OK, `201` Created.
- **3xx** — redirect. `301` Moved Permanently, `304` Not Modified.
- **4xx** — client error. `400` syntax error; `401` authentication required; `403` permission denied; `404` resource not found; `410` permanently deleted.
- **5xx** — server error. `500` internal server error.

DJI Pilot 2's response to each class — verbatim table from the canonical:

| Status code | App behavior (image transmission page) | App behavior (not on image transmission page) |
|---|---|---|
| 2xx | Normal flow | Normal flow |
| 3xx | Normal flow | Normal flow |
| 400 | Toast: "parameter error, please try again, or contact the administrator" | Toast: "parameter error, please try again, or contact the administrator" |
| 401 | 1. Toast: "The login to the cloud platform is invalid, please log in again". 2. Cloud platform does the cloud withdrawal processing. | 1. Cloud platform does the cloud withdrawal processing. 2. Pop-up box prompts, go to login. |
| 403 | Toast: "You do not have permission to operate, please try again, or contact the administrator" | (same) |
| 404 | Toast: "the resource does not exist, please try again, or contact the administrator" | (same) |
| 5xx | Toast: "server exception, please try again later (`resp.code`)" | (same) |
| Unknown | Toast: "The network request is abnormal, please try again later (`resp.code`)" | (same) |

This is **Pilot 2 client-side behavior**. The server is expected to return the appropriate HTTP status code per normal HTTP semantics; the toast text is useful for server-side error-response design so the end-user experience is coherent.

## 7. TLS

The same certificate trust applies to HTTPS and MQTT. DJI Pilot 2 and DJI Dock trust certificates issued by Godaddy; see architecture §8 for the verbatim quote and broader auth context.

## 8. What this document is not

- Not an endpoint catalog. Per-endpoint request/response schemas live in Phase 3 under `http/<resource>/<endpoint>.md`.
- Not an error-code reference. Business error codes (values of the envelope `code` field) are in Phase 8 (`error-codes/`).
- Not a workflow reference. Login, token exchange, and endpoint sequencing are in Phase 9 (`workflows/`).

## 9. Source provenance

| Source | Role in this doc |
|---|---|
| `[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/40.https.md]` | Canonical URI form, request-method quote, header table, response envelope, status-code → Pilot behavior mapping (§2, §3, §4, §5, §6). |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-Waypoint-Obtain-Wayline-List.txt]` | Live v1.15 example of envelope shape, pagination block, URI conformance (§2, §5, §5.1). |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-*.txt]` (16 more files) | Corroborating v1.15 endpoint structure — cataloged in Phase 3, not quoted here. |

Verbatim quotations are fenced and cited inline; nothing is paraphrased where a direct quote carries the same load.
