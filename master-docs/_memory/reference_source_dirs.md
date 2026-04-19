---
name: DJI source directory inventory
description: Which sibling directories in C:\repos\DJI-docs-master hold what DJI Cloud source material and their authority level
type: reference
---

Source directories under `C:\repos\DJI-docs-master\` (all read-only for this project):

- **`Cloud-API-Doc/docs/{cn,en}/`** — Official DJI SDK Cloud API documentation tree (bilingual). **Authoritative.** Primary source of truth. Verify claims against this.

- **`DJI-Cloud-API-Demo/`** — Official DJI Java/Spring Boot reference implementation. Contains `api/`, `cloud-sdk/`, `sample/`, `sql/`, `pom.xml`. **DEPRECATED by DJI on 2025-04-10** (per its own README) — still authoritative for how DJI themselves implemented the cloud-side, but no longer maintained and DJI explicitly warns against production use.

- **`DJI_Cloud/*.txt`** — 67 plain-text files extracted from `developer.dji.com/doc/cloud-api-tutorial/en/` (Cloud API v1.15+) via two pipelines owned by the user: (1) MHTML dumps converted by `extract_mhtml.py` (original, hand-driven) and (2) headless-Playwright live-site scrape via `scrape_api_reference.py` (added 2026-04-18, pulled the 40+ pages missing from the MHTML set). **Primary written source for in-scope devices** per `master-docs/OPEN-QUESTIONS.md` OQ-001 — the only in-repo written source that names Dock 3 / M4D / M4TD / RC Plus 2 Enterprise. Coverage:
  - Dock 3 feature set — 18 files covering every API Reference subsection (AirSense, Configuration-Update, Custom-Flight-Area, DeviceManagement, DeviceProperties, ESDK-Interconnection, Firmware-Upgrade, FlySafe, Live-Flight-Controls, LiveStream, Media-Management, Organization-Management, PSDK, PSDK-Interconnection, Remote-Control, Remote-Debugging, Remote-Log, WaylineManagement).
  - Dock-to-Cloud aircraft property catalogs: `DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt` (M4D / M4TD), `DJI_CloudAPI_M30_M30T-Properties.txt`, `DJI_CloudAPI_M3D_M3DT_Properties.txt` (Matrice 3D / 3TD), `DJI_CloudAPI_Matrice-400-Properties.txt`.
  - RC Plus 2 Enterprise feature set (the in-scope controller, paired with M4D) — 5 files: Device-Management, Live-Flight-Controls, Live-Stream, Properties, Remote-Control.
  - RC Pro Enterprise feature set (newer controller family, added by live scrape) — 5 files.
  - Pilot-to-Cloud MQTT for generic / other device classes: `DJI_CloudAPI_Aircraft-Properties.txt`, `DJI_CloudAPI_RC-{Properties,Device-Management,Live-Stream}.txt`, `DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`, `DJI_CloudAPI_Mavic3-Enterprise_Properties.txt`.
  - Pilot-to-Cloud HTTPS — 17 files under `DJI_CloudAPI_Pilot-HTTPS-*` covering Map Elements (CRUD), Waypoint Management (7), Media Management (5), and Situation Awareness.
  - Pilot-to-Cloud WebSocket push messages (Map Elements, Situation Awareness) and JSBridge.
  - MQTT topic reference: `DJI_CloudAPI-TopicDefinitions.txt` (dock-to-cloud), `DJI_CloudAPI-PilotToCloud-Topic-Definition.txt`.
  - HMS event taxonomy + codes + `HMS.json`.
  - DJI WPML wayline format — `DJI_CloudAPI_WPML-*.txt` (4 files: Overview, Template-KML, Waylines, Common-Elements).
  - `DJI_CloudAPI_FAQ.txt`.
  - Three hand-authored canonical reference files with cited `Source:` URLs (ASCII-headered, not extracts): `DJI_CloudAPI-Dock3-AirSense.txt`, `DJI_CloudAPI-Dock3-FlySafe.txt`, `DJI_CloudAPI_Aircraft-Properties.txt`.

  Dock 1 and Dock 2 pages (37 on the live site) are deliberately **not** scraped — `scrape_api_reference.py` skips them per `CLAUDE.md` scope. Pass `--include-legacy` to pull them if ever needed.

  The directory is treated as writable for the extraction workflows (the user owns both `extract_mhtml.py` and `scrape_api_reference.py`); no corpus documentation is written here.

- **`dji_cloud_dock3/`** — Third-party community project by hecongyuan (GitHub/Gitee). Dock-3-specific adaptation of DJI's demo. Java 11 + Spring Boot 2.7.12 + Vue 3, Cloud SDK 1.2.5. **Non-authoritative.** Useful only as a reference for Dock-3-specific quirks/workarounds and what a working Dock 3 cloud integration looks like in practice.
