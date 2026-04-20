# DJI Cloud Docs Corpus

Curated, LLM-digestible documentation of the **DJI Cloud API wire contract and workflows** needed by two parallel device cohorts:

**Current generation** (Dock 3 cohort):
- **DJI Dock 3**
- **Matrice 4D** (M4D)
- **Matrice 4TD** (M4TD)
- **RC Plus 2 Enterprise** running DJI Pilot 2 (the RC paired with the M4D)

**Older generation** (Dock 2 cohort):
- **DJI Dock 2**
- **Matrice 3D** (M3D)
- **Matrice 3TD** (M3TD)
- **RC Pro Enterprise** running DJI Pilot 2 (the RC paired with the M3D / M3TD)

Dock 1, M30 / M30T, M300 / M350 RTK, and Mavic 3 Enterprise families are out of scope.

For repo-level scope, directives, and session-start instructions, see [`/CLAUDE.md`](../CLAUDE.md).

## Orientation

| File | Purpose |
|---|---|
| [`PLAN.md`](PLAN.md) | Phased plan with review gates |
| [`TODO.md`](TODO.md) | Cross-session fine-grained checklist |
| [`SOURCES.md`](SOURCES.md) | Source directory authority ranking |
| [`OPEN-QUESTIONS.md`](OPEN-QUESTIONS.md) | Standing gaps tracker |
| [`_memory/MEMORY.md`](_memory/MEMORY.md) | In-repo Claude memory index |

## Corpus table of contents

New docs are added to the table below as they land.

| Area | Docs |
|---|---|
| `architecture/` | [`README.md`](architecture/README.md) — transports, device-edge-cloud model, thing model, topic taxonomy, in-scope topologies |
| `http/` | [`README.md`](http/README.md) — URI form, `X-Auth-Token`, response envelope, status-code behavior + Phase 3 catalog of 16 endpoints across wayline / media / map / storage / device |
| `mqtt/` | [`README.md`](mqtt/README.md) — topic taxonomy, 13-topic list, envelope, per-family payloads + Phase 4a–4g [`dock-to-cloud/`](mqtt/dock-to-cloud/README.md) catalog (197 methods) + Phase 4h [`pilot-to-cloud/`](mqtt/pilot-to-cloud/README.md) catalog (94 methods across RC Plus 2 Enterprise + RC Pro Enterprise) + Phase 4i property-family shells (`osd/`, `state/`, `property-set/` per path — thin pointers to Phase 6) |
| `websocket/` | [`README.md`](websocket/README.md) — session lifecycle, envelope, push-and-fetch pattern + Phase 5 per-message catalog: [`map-elements/`](websocket/map-elements/) (4 push messages) + [`situation-awareness/`](websocket/situation-awareness/) (4 push messages) |
| `device-properties/` | [`README.md`](device-properties/README.md) — master matrix + narrative + Phase 6a dock-gateway entries: [`dock2.md`](device-properties/dock2.md) (48 properties, 3 writable) + [`dock3.md`](device-properties/dock3.md) (49 properties, 3 writable) + Phase 6b aircraft entries: [`_aircraft-pilot-base.md`](device-properties/_aircraft-pilot-base.md) (shared pilot-path baseline, 42 properties) + [`m3d.md`](device-properties/m3d.md) (dock-path 42 + pilot-path baseline) + [`m3td.md`](device-properties/m3td.md) (thermal-variant annex) + [`m4d.md`](device-properties/m4d.md) (dock-path 42 + pilot-path baseline + 7 M4 extensions) + [`m4td.md`](device-properties/m4td.md) (thermal-variant annex) + Phase 6c RC entries: [`rc-plus-2.md`](device-properties/rc-plus-2.md) (11 properties, 0 writable) + [`rc-pro.md`](device-properties/rc-pro.md) (11 properties, 0 writable) |
| `wpml/` | [`README.md`](wpml/README.md) — WPML wayline file format. Phase 7 entries: [`overview.md`](wpml/overview.md) (format, archive layout, device support) + [`template-kml.md`](wpml/template-kml.md) (`template.kml` — 4 template types: `waypoint` / `mapping2d` / `mapping3d` / `mappingStrip`) + [`waylines.md`](wpml/waylines.md) (`waylines.wpml` — executable commands) + [`common-elements.md`](wpml/common-elements.md) (shared schemas + 16 actuator functions including `takePhoto`, `gimbalRotate`, `orientedShoot`, `panoShot`, M4D-only `megaphone` / `searchlight`) |
| `livestream-protocols/` | [`README.md`](livestream-protocols/README.md) — protocol-selector matrix. Phase 7 per-protocol docs: [`rtmp.md`](livestream-protocols/rtmp.md) (`url_type 1`, all devices) + [`gb28181.md`](livestream-protocols/gb28181.md) (`url_type 3`, all devices) + [`webrtc.md`](livestream-protocols/webrtc.md) (`url_type 4` / WHIP; not RC Pro) + [`agora.md`](livestream-protocols/agora.md) (`url_type 0`; not Dock 3) |
| `hms-codes/` | [`README.md`](hms-codes/README.md) — master index for 1,769 HMS alarm codes. Phase 8 entries: one file per first-byte prefix — [`0x11`](hms-codes/0x11-payload-general.md) payload (45) · [`0x12`](hms-codes/0x12-battery-station.md) battery station (37) · [`0x14`](hms-codes/0x14-payload-imu.md) payload IMU (52) · [`0x15`](hms-codes/0x15-mmwave-radar.md) mmWave radar (39) · [`0x16`](hms-codes/0x16-flight-control.md) flight-control (921) · [`0x17`](hms-codes/0x17-transmission.md) transmission (16) · [`0x19`](hms-codes/0x19-system-overload.md) system overload (52) · [`0x1A`](hms-codes/0x1A-vision-sensors.md) vision (170) · [`0x1B`](hms-codes/0x1B-navigation-tracking.md) navigation (138) · [`0x1C`](hms-codes/0x1C-camera.md) camera (167) · [`0x1D`](hms-codes/0x1D-gimbal.md) gimbal (45) · [`0x1E`](hms-codes/0x1E-psdk-payload.md) PSDK payload (28) · [`0x1F`](hms-codes/0x1F-cellular-lte.md) cellular (56) · [`0x20`](hms-codes/0x20-takeoff-tags.md) takeoff tags (2) · [`outliers.md`](hms-codes/outliers.md) (1). 531 CJK-in-`tipEn` entries carry curated CN→EN translations flagged with `+` |
| `error-codes/` | [`README.md`](error-codes/README.md) — 448 codes across 20 function modules (`ABCDEF` format: source `A` + module `BC` + local `DEF`). Grouped tables per BC module (`312`–`514`), plus v1.11 → v1.15 drift (5 new, 0 dropped) and DJI-Cloud-API-Demo enum cross-reference |
| `workflows/` | [`README.md`](workflows/README.md) — phase index + sub-phase roadmap. Phase 9a entries: [`dock-bootstrap-and-pairing.md`](workflows/dock-bootstrap-and-pairing.md) (MQTT connect → License → org bind → first topology), [`device-binding.md`](workflows/device-binding.md) (topology lifecycle + OSD + state + `property/set` + Pilot-2 change fan-out; all cohorts), [`firmware-and-config-update.md`](workflows/firmware-and-config-update.md) (`ota_create` → `ota_progress` loop + post-bootstrap `config` refresh). Phase 9b entries: [`wayline-upload-and-execution.md`](workflows/wayline-upload-and-execution.md) (Pilot-HTTPS upload + `flighttask_prepare` → `_execute` → `_progress` + immediate / timed / conditional variants + breakpoint resume + in-flight delivery + RTH controls), [`live-flight-controls-drc.md`](workflows/live-flight-controls-drc.md) (authority grab + `drc_mode_enter` → stick / drone-control DRC stream + HSI/OSD/delay push; dock + pilot paths; DRC 2.0), [`livestream-start-stop.md`](workflows/livestream-start-stop.md) (`live_capacity` → `live_start_push` per-protocol + mid-stream quality / lens / camera changes + pilot JSBridge coordination). Phase 9c entries: [`hms-event-reporting.md`](workflows/hms-event-reporting.md) (full-snapshot `hms` event push + Copy Key splicing + placeholder substitution + `hms.json` lookup), [`flysafe-custom-flight-area-sync.md`](workflows/flysafe-custom-flight-area-sync.md) (FlySafe license list / update / switch + CFA `flight_areas_update` → `_get` → `_sync_progress` → `_drone_location`), [`airsense-events.md`](workflows/airsense-events.md) (ADS-B 5-level warning push + snapshot diff + onboard avoidance at level ≥3), [`media-upload-from-dock.md`](workflows/media-upload-from-dock.md) (dock-path MQTT STS + `file_upload_callback` + prioritize; pilot-path HTTPS tiny-fingerprint → fast-upload → STS → `upload-callback` → `group-upload-callback`), [`remote-control-handoff.md`](workflows/remote-control-handoff.md) (RC consent pop-up via `cloud_control_auth_request` → `cloud_control_auth_notify` → `cloud_control_auth` state → `cloud_control_release` / pilot grab-back). |
| `device-annexes/` | [`README.md`](device-annexes/README.md) — phase overview + annex layout. Phase 10 entries: [`dock2.md`](device-annexes/dock2.md), [`dock3.md`](device-annexes/dock3.md), [`m3d.md`](device-annexes/m3d.md), [`m3td.md`](device-annexes/m3td.md), [`m4d.md`](device-annexes/m4d.md), [`m4td.md`](device-annexes/m4td.md), [`rc-plus-2.md`](device-annexes/rc-plus-2.md), [`rc-pro.md`](device-annexes/rc-pro.md) — per-device triangulation of Phase 4 / 6 / 7 / 8 / 9 content, quirks, gotchas, and "features this device lacks". |
| `_build/` | Internal tooling — Phase 8 catalog generators: `generate_hms_codes.py` + `generate_error_codes.py` + `_translations.json` (531 curated CN→EN translations). Not user-facing content; regenerate `hms-codes/` + `error-codes/` from source extracts on demand. |

## Authoring rules (quick reference)

- **Real payloads only** — verbatim from DJI source, never fabricated. Cite provenance.
- **English corpus** — translate from CN only when EN is missing/inadequate; flag translated passages.
- **Transport catalog owns schemas** — workflows link; they don't duplicate schema bodies.
- **Flag ambiguity** — add to `OPEN-QUESTIONS.md`; don't guess.
- **Update this README** every time a new doc lands.
