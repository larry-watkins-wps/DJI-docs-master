---
name: DJI source directory inventory
description: Which sibling directories in C:\repos\DJI-docs-master hold what DJI Cloud source material and their authority level
type: reference
---

Source directories under `C:\repos\DJI-docs-master\` (all read-only for this project):

- **`Cloud-API-Doc/docs/{cn,en}/`** — Official DJI SDK Cloud API documentation tree (bilingual). **Authoritative.** Primary source of truth. Verify claims against this.

- **`DJI-Cloud-API-Demo/`** — Official DJI Java/Spring Boot reference implementation. Contains `api/`, `cloud-sdk/`, `sample/`, `sql/`, `pom.xml`. **DEPRECATED by DJI on 2025-04-10** (per its own README) — still authoritative for how DJI themselves implemented the cloud-side, but no longer maintained and DJI explicitly warns against production use.

- **`DJI_Cloud/*.txt`** — ~30 plain-text files (36.5K lines total) extracted from MHTML dumps via `extract_mhtml.py`. Covers Dock 3 (AirSense, Config Update, Custom Flight Area, Device Management, Properties, FlySafe, Live Flight Controls, LiveStream, Remote Control, Wayline Management), HMS codes, M4 properties, MQTT topic definitions, RC Plus Enterprise, WMPL (Wayline Markup / KML). **Derived** — treat as convenience text of Cloud-API-Doc content; cross-check against Cloud-API-Doc when in doubt.

- **`dji_cloud_dock3/`** — Third-party community project by hecongyuan (GitHub/Gitee). Dock-3-specific adaptation of DJI's demo. Java 11 + Spring Boot 2.7.12 + Vue 3, Cloud SDK 1.2.5. **Non-authoritative.** Useful only as a reference for Dock-3-specific quirks/workarounds and what a working Dock 3 cloud integration looks like in practice.
