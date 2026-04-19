# Source Directory Inventory

All source directories live at the repo root alongside `master-docs/`. They are **read-only** for this project — never modified.

## Authority ranking

The two DJI documentation sources in this repo are **different versions** of the Cloud API docs, not duplicates:

- `Cloud-API-Doc/` is **Cloud API v1.11.3** (per `docs/en/00.index.md` release-notes header). It predates Dock 3 / Matrice 4 and has zero mentions of `Dock 3`, `M4D`, or `M4TD` in `docs/{en,cn}/`.
- `DJI_Cloud/` is a **Cloud API v1.15** MHTML extraction (per every `DJI_CloudAPI-Dock3-*.txt`, `DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-*.txt`, and `DJI_CloudAPI_RC-Plus-2-Enterprise-*.txt` navigation header). It is the only written DJI source in this repo that covers the in-scope devices by name.

See [`OPEN-QUESTIONS.md`](OPEN-QUESTIONS.md) (OQ-001) for the full version-mismatch analysis.

### Ranking

1. **`Cloud-API-Doc/`** (v1.11.3) — authoritative for content that exists in v1.11. Formatting fidelity preferred over the `DJI_Cloud/` extract when both cover the same material.
2. **`DJI_Cloud/`** (v1.15 extraction) — authoritative written source for anything specific to **Dock 3, Matrice 4D, Matrice 4TD, RC paired with M4D**, and anything else introduced after v1.11. Derived from MHTML: tables and inline formatting may have been lost in extraction — verify table structure against the live site when a claim hinges on it.
3. **`DJI-Cloud-API-Demo/`** — authoritative for wire behavior; **deprecated 2025-04-10** by DJI. Use as evidence of what payloads DJI themselves send, not as a structural template. Last release: Cloud API 1.10.0 (2024-04-07).
4. **Live DJI developer site** (`developer.dji.com`, v1.15+) — Browser / Playwright fallback when the `DJI_Cloud/` extract appears to have lost structure, when checking for drift since the last scrape (2026-04-18), or when a page is not in the extraction set (e.g., release notes, tutorial-map content outside `/api-reference/`). Not stored in-repo outside of `DJI_Cloud/`; cite as `[developer.dji.com/...]` with the access date.
5. **`dji_cloud_dock3/`** — non-authoritative third-party; reference only. Any fact derived from here must be flagged and corroborated against sources #1–#4 before inclusion.

### Conflict resolution

- When #1 and #2 both cover the same topic and agree, cite #1.
- When #1 is silent and #2 covers the topic (typical for Dock 3 / M4D / M4TD content), cite #2.
- When #1 and #2 **disagree** on the same topic (version drift in the wire contract), log as a new entry in `OPEN-QUESTIONS.md` and ask before writing.
- When #2 appears to have dropped a table or structure, cross-check against #4 (live site) and cite both.
- #3 corroborates wire behavior; it never overrides #1 or #2 on what DJI documents.
- #5 never wins against #1–#4.

---

## 1. `Cloud-API-Doc/`

Layout: `docs/{cn,en}/` — bilingual Markdown docs tree.

**Origin**: Official DJI SDK Cloud API documentation repository.
**Version in repo**: **Cloud API v1.11.3** (per `docs/en/00.index.md` release-notes header).
**Use as**: Primary source of truth for API surface, topic definitions, device properties, and workflows **that exist in v1.11**. Does not cover Dock 3, Matrice 4D, Matrice 4TD, or anything introduced after v1.11 — see `DJI_Cloud/` for those.
**Preference**: Default to `docs/en/`. Use `docs/cn/` only when the EN version is missing or ambiguous.

---

## 2. `DJI-Cloud-API-Demo/`

Contents: `api/`, `cloud-sdk/`, `sample/`, `sql/`, `pom.xml`, `README.md`, `LICENSE`.

**Origin**: Official DJI Java/Spring Boot reference implementation.
**Status**: **DEPRECATED by DJI on 2025-04-10** (per its own README). DJI explicitly warns against using it in production. No further support or updates.
**Last release**: Cloud API 1.10.0 (2024-04-07).
**Use as**: Evidence of wire-level behavior — what payloads DJI themselves send, what endpoint shapes exist, what MQTT topics the SDK subscribes to.
**Do NOT use as**: A template for how a replacement server must be structured. Internal Java/Spring patterns are irrelevant to scope.

---

## 3. `DJI_Cloud/`

Contents: 87 `.txt` files plus `HMS.json` and two extraction scripts (`extract_mhtml.py`, `scrape_api_reference.py`).

**Origin**: Two ingestion pipelines, both targeting the official DJI Cloud API docs at `developer.dji.com/doc/cloud-api-tutorial/en/`:
  1. **MHTML capture → `extract_mhtml.py`** (original, hand-driven): the user saves pages as MHTML; the script converts to plain text and trims live-site page chrome using the `Github Edit open in new window` marker as a content boundary.
  2. **Live-site scrape → `scrape_api_reference.py`** (added 2026-04-18): Playwright headless Chromium renders each API Reference page and extracts the `.theme-default-content` container. Staged into `_scraped/`, deduped against existing filenames via normalized-slug matching, and then merged into `DJI_Cloud/`. Initial run pulled 43 pages covering sections not yet captured by the MHTML workflow (41 kept after manual dedupe; 2 were near-identical to pre-existing MHTML extracts under different names). A second run on 2026-04-18 with `--include-legacy` pulled 39 pages: 19 Dock 1, 19 Dock 2, 1 Dock 3 HMS (filled a Dock 3 coverage gap). Merged: 20 (all 19 Dock 2 + Dock 3 HMS), per the expanded scope (Dock 2 + M3D / M3TD + RC Pro Enterprise). **Dock 1 pages were scraped but discarded** — Dock 1 is out of scope and the staging directory was deleted after merge. Re-run `scrape_api_reference.py --include-legacy` to re-pull them if scope expands to include Dock 1 later.
**Version extracted**: **Cloud API v1.15** for both pipelines (the MHTML and live scrape both hit the same v1.15+ site; the live scrape was 2026-04-18).
**Use as**: The primary **written** DJI source for all in-scope devices — **Dock 2**, **Dock 3**, **M3D / M3TD**, **M4D / M4TD**, **RC Pro Enterprise**, **RC Plus 2 Enterprise** — plus out-of-scope device reference material (M30 / M30T, Matrice 400, Mavic 3 Enterprise, plain RC) captured alongside as a side-effect of the scrape. Covers the complete Pilot-to-Cloud surface (MQTT, HTTPS, WebSocket, JSBridge) and the full Dock-to-Cloud feature-set surface for Dock 2 and Dock 3. None of this material (for the in-scope devices) exists in `Cloud-API-Doc/` (v1.11).
**Caveat**: Both pipelines are lossy in different ways. MHTML extracts may have lost table/code-block structure; the live scrape preserves structure but can mid-line-break text around external-link icons ("open in new window"). When a claim hinges on table structure or inline formatting, verify against the live site. When content exists in both `Cloud-API-Doc/` and `DJI_Cloud/`, prefer `Cloud-API-Doc/` for formatting fidelity.
**Writability**: This directory is treated as writable for the extraction workflows (the user owns these workflows and the scripts write here). No corpus documentation is written into this directory — only extractions.

### File coverage

**Dock 3 feature set** — `DJI_CloudAPI-Dock3-*.txt` (19 files): AirSense, Configuration-Update, Custom-Flight-Area, DeviceManagement, DeviceProperties, ESDK-Interconnection, Firmware-Upgrade, FlySafe, HMS, Live-Flight-Controls, LiveStream, Media-Management, Organization-Management, PSDK, PSDK-Interconnection, Remote-Control, Remote-Debugging, Remote-Log, WaylineManagement.

**Dock 2 feature set** — `DJI_CloudAPI-Dock2-*.txt` (19 files): AirSense, Configuration-Update, Custom-Flight-Area, Device-Management, ESDK-Interconnection, Firmware-Upgrade, FlySafe, HMS, Live-Flight-Controls, Live-Stream, Media-Management, Organization-Management, PSDK, PSDK-Interconnection, Properties, Remote-Control, Remote-Debugging, Remote-Log, Wayline-Management.

**M4D / M4TD properties** — `DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt`. The M4D / M4TD dock-to-cloud MQTT property catalog. Supersedes the older generic `DJI_CloudAPI-Matrice4-DeviceProperties.txt` that existed during initial setup.

**Dock-to-Cloud other aircraft property catalogs** — `DJI_CloudAPI_M30_M30T-Properties.txt` (M30 / M30T), `DJI_CloudAPI_M3D_M3DT_Properties.txt` (Matrice 3D / 3TD), `DJI_CloudAPI_Matrice-400-Properties.txt` (Matrice 400). Included for enum-merging and cross-device reference.

**RC Plus 2 Enterprise feature set** (the RC paired with M4D, the in-scope controller) — `DJI_CloudAPI_RC-Plus-2-Enterprise-*.txt` (5 files): Device-Management, Live-Flight-Controls, Live-Stream, Properties, Remote-Control.

**RC Pro Enterprise feature set** (newer-generation controller, added by live-site scrape) — `DJI_CloudAPI_RC-Pro-Enterprise-*.txt` (5 files): Device-Management, Live-Flight-Controls, Live-Stream, Properties, Remote-Control.

**Pilot-to-Cloud MQTT (other / generic device classes)** — `DJI_CloudAPI_Aircraft-Properties.txt`, `DJI_CloudAPI_RC-Properties.txt`, `DJI_CloudAPI_RC-Device-Management.txt`, `DJI_CloudAPI_RC-Live-Stream.txt`, `DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`, `DJI_CloudAPI_Mavic3-Enterprise_Properties.txt`.

**Pilot-to-Cloud HTTPS endpoints** — `DJI_CloudAPI_Pilot-HTTPS-*.txt` (17 files):
- *Map Elements*: Create, Update, Obtain, Delete.
- *Waypoint Management*: Obtain-Wayline-List, Obtain-Temporary-Credential, Obtain-Wayline-File-Download-Address, Obtain-Duplicated-Wayline-Name, File-Upload-Result-Report, Batch-Favorites-Wayline, Batch-Unfavorite-Wayline.
- *Media Management*: Fast-Upload, Obtain-Exist-File-Tiny-Fingerprint, Obtain-Temporary-Credential, File-Upload-Result-Report, Group-Upload-Callback.
- *Situation Awareness*: Obtain-Device-Topology-List.

**Pilot-to-Cloud WebSocket push messages** — `DJI_CloudAPI_Pilot-WebSocket-Map-Elements-Push-Message.txt`, `DJI_CloudAPI_Pilot-WebSocket-Situation-Awareness-Push-Message.txt`.

**Pilot-to-Cloud JSBridge** — `DJI_CloudAPI_Pilot-JSBridge.txt`.

**HMS** — `DJI_CloudAPI-HMS.txt` (overview), `DJI_CloudAPI-HMS-Codes.txt` (full code list), `HMS.json` (structured data).

**MQTT topic reference** — `DJI_CloudAPI-TopicDefinitions.txt` (dock-to-cloud family), `DJI_CloudAPI-PilotToCloud-Topic-Definition.txt` (pilot-to-cloud family).

**DJI WPML (wayline file format)** — `DJI_CloudAPI_WPML-*.txt` (4 files): Overview, Template-KML, Waylines, Common-Elements. Renamed from the earlier `WMPL-*` filename segment to reflect DJI's actual format name (the `.wpml` file extension and the developer.dji.com URL path both use `WPML`).

**Generic references** — `DJI_CloudAPI_FAQ.txt`.

**Hand-authored canonical reference files** (not extracts — ASCII-headered files with cited `Source:` URLs, pre-trimmed before being added to the directory; the extraction scripts leave them untouched):
- `DJI_CloudAPI-Dock3-AirSense.txt`
- `DJI_CloudAPI-Dock3-FlySafe.txt`
- `DJI_CloudAPI_Aircraft-Properties.txt`

**Scope intentionally excluded from scraping**: Dock 1 and Dock 2 pages (37 pages on the live site). `scrape_api_reference.py` skips these by default per `CLAUDE.md` scope; pass `--include-legacy` to pull them.

**Tooling**:
- `extract_mhtml.py` — extracts new MHTMLs and trims live-site chrome from existing `.txt` files; run it after dropping new `.mhtml` captures into this directory.
- `scrape_api_reference.py` — headless Playwright scrape of the API Reference section of `developer.dji.com/doc/cloud-api-tutorial/en/`. Embedded URL inventory (captured from the live sidebar on 2026-04-18, 103 unique pages). Dedupes against existing filenames; stages new pages in `_scraped/` with a `_manifest.json` for review before merge. Requires `pip install playwright && playwright install chromium`. Re-run to refresh or pull newly-added pages.

---

## 4. `dji_cloud_dock3/`

Contents: `source/`, `docker-compose.yml`, `update_backend.sh`, `update_front.sh`, `README.md`, `README_SECURITY.md`, `配置说明.md`, `LICENSE`, `jt.png`, `wx.JPG`.

**Origin**: Third-party community project by hecongyuan ([GitHub](https://github.com/hecongyuan/dji_cloud_dock3), [Gitee](https://gitee.com/hecongyuan/dji_cloud_dock3)).
**Stack**: Java 11, Spring Boot 2.7.12, Vue 3.2.26, Cloud SDK 1.2.5.
**Status**: Non-official. Explicitly Dock-3-adapted.
**Use as**: A reality check for Dock-3-specific behaviors or workarounds — what a working Dock 3 integration actually had to implement that DJI's generic demo did not cover.
**Do NOT use as**: Authoritative source for any claim. Any fact derived from this must be flagged and ideally corroborated against `Cloud-API-Doc/` before inclusion in the corpus.

---

## Provenance convention

When citing a source in corpus docs, use a bracketed path relative to repo root, or a URL for live-web sources:
- `[Cloud-API-Doc/docs/en/<path>]` — v1.11.3
- `[DJI_Cloud/<file>]` — v1.15 extract
- `[DJI-Cloud-API-Demo/<path>]` — deprecated reference
- `[developer.dji.com/<path>]` (accessed YYYY-MM-DD) — live-site fallback
- `[dji_cloud_dock3/<path>]` — always flag as non-authoritative third-party
