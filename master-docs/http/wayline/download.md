# GET /wayline/api/v1/workspaces/{workspace_id}/waylines/{id}/url

Fetch the download URL for a specific wayline file. The returned URL is a pre-signed link against the object-storage backend (provider negotiated via the STS-credential endpoint — see [`../storage/sts-credential.md`](../storage/sts-credential.md)).

Part of the Phase 3 HTTP endpoint catalog. Shared conventions (URI form, `X-Auth-Token`, response envelope, status codes) live in [`../README.md`](../README.md) and are not restated here.

---

## Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `workspace_id` | path | string | yes | Workspace ID. |
| `id` | path | string | yes | Wayline file ID. |
| `x-auth-token` | header | string | yes | Access token — see [`../README.md` §4](../README.md#4-request-headers). |

## Request body

None.

## Response — 200 OK

DJI's v1.11 and v1.15 documentation both list the response schema as `/` — i.e. no schema is specified beyond the 200 status. The response body shape is therefore not fully pinned by official documentation.

Expected shape based on neighboring endpoints and endpoint purpose: the standard envelope with `data` containing the pre-signed URL. The exact field name is not documented here; Phase 9 workflow authoring will resolve the final shape when wayline upload/download choreography is written. Implementers should not assume a particular field name without cross-checking against a concrete client implementation or a live capture.

## Source provenance

| Source | Role |
|---|---|
| `[Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/10.https/20.waypoint-management/30.get-waypointfile-download-location.md]` | v1.11 canonical — URI, parameter list. Response schema not specified. |
| `[DJI_Cloud/DJI_CloudAPI_Pilot-HTTPS-Waypoint-Obtain-Wayline-File-Download-Address.txt]` | v1.15 corroboration — same URI, same parameters, response schema likewise unspecified. |
