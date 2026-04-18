# Source Directory Inventory

All source directories live at the repo root alongside `master-docs/`. They are **read-only** for this project — never modified.

## Authority ranking

1. **`Cloud-API-Doc/`** — authoritative
2. **`DJI-Cloud-API-Demo/`** — authoritative for wire behavior; **deprecated 2025-04-10** by DJI
3. **`DJI_Cloud/`** — derived (MHTML extractions); cross-check against #1
4. **`dji_cloud_dock3/`** — non-authoritative third-party; reference only

When sources disagree, #1 wins. When #1 is silent but #2 shows behavior, document behavior with provenance and flag in `OPEN-QUESTIONS.md`.

---

## 1. `Cloud-API-Doc/`

Layout: `docs/{cn,en}/` — bilingual Markdown docs tree.

**Origin**: Official DJI SDK Cloud API documentation repository.
**Use as**: Primary source of truth for API surface, topic definitions, device properties, workflows.
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

Contents: ~30 `.txt` files (36,552 lines total) plus `HMS.json` and `extract_mhtml.py`.

**Origin**: MHTML dumps of the official DJI docs, converted to plain text via the included extraction script.
**Use as**: Convenient searchable text corpus of the same material as `Cloud-API-Doc/`. Good for fast pattern search.
**Caveat**: Derived — formatting and embedded tables may have been lost in extraction. When a claim hinges on table structure or inline formatting, verify against `Cloud-API-Doc/`.

### File coverage (as of setup)
- `DJI_CloudAPI-Dock3-*.txt` (10 files) — Dock 3 specifics: AirSense, Config Update, Custom Flight Area, Device Management, Device Properties, FlySafe, Live Flight Controls, LiveStream, Remote Control, Wayline Management.
- `DJI_CloudAPI-HMS.txt`, `DJI_CloudAPI-HMS-Codes.txt`, `HMS.json` — HMS event taxonomy and code list.
- `DJI_CloudAPI-Matrice4-DeviceProperties.txt` — M4 family property catalog.
- `DJI_CloudAPI-TopicDefinitions.txt` — MQTT topic reference.
- `DJI_CloudAPI_Aircraft-Properties.txt` — general aircraft property reference.
- `DJI_CloudAPI_FAQ.txt`.
- `DJI_CloudAPI_RC-Plus-Enterprise*.txt` (6 files) — RC Plus Enterprise: overall, Device Management, Live Controls, Live Stream, Properties, Remote Control.
- `DJI_CloudAPI_WMPL-*.txt` (4 files) — Wayline Markup / KML: Common Elements, Overview, Template KML, Waylines.
- `extract_mhtml.py` — extraction script (not source content).

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

When citing a source in corpus docs, use a bracketed path relative to repo root:
- `[Cloud-API-Doc/docs/en/<path>]`
- `[DJI-Cloud-API-Demo/<path>]`
- `[DJI_Cloud/<file>]`
- `[dji_cloud_dock3/<path>]` — always flag as non-authoritative
