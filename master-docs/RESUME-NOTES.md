# Resume Notes

Mid-phase context that must survive a session break. If you're starting a fresh session and the user's first instruction is **"Continue at 4c"** (or similar), read this file first — it hands you everything you need to pick up without re-reading the whole corpus.

Latest entry is at the top. Older entries kept below for audit traceability.

---

## 2026-04-19 — handoff at Phase 8 close, ready for review gate

### State of play

- Phases 0, 1, 2, 3, 4, 5, 6, 7 complete and committed. **Phase 8 (HMS codes + error codes) content-complete.**
- Phase 8 review gate is the only remaining Phase 8 item.
- **Phase 9 (Workflows) is next** after the review gate. Depends on Phases 3–5 transport catalogs (done) + Phase 7 WPML + Phase 8 codes (both done).

### What Phase 8 produced

Single-drop phase per PLAN.md — no sub-phase split. Total: **17 content files + 3 generator artifacts + 1 README table update**. Reproducible generator pipeline lives under [`_build/`](_build/).

**HMS codes** ([`hms-codes/`](hms-codes/README.md) — 16 files, 1,769 alarm entries):

- [`hms-codes/README.md`](hms-codes/README.md) — master index + first-byte-prefix catalog table + CN source-defect disclosure + `HMS.json` cross-reference to the [Phase 4f `events/hms.md`](mqtt/dock-to-cloud/events/hms.md) event definition.
- 14 per-prefix files — one per observed first byte of the `alarmId` hex value:
  - [`0x11-payload-general.md`](hms-codes/0x11-payload-general.md) (45 codes) — payload general faults, most reference `%component_index`.
  - [`0x12-battery-station.md`](hms-codes/0x12-battery-station.md) (37 codes) — battery-station activation and restart guidance.
  - [`0x14-payload-imu.md`](hms-codes/0x14-payload-imu.md) (52 codes) — payload IMU temperature / calibration.
  - [`0x15-mmwave-radar.md`](hms-codes/0x15-mmwave-radar.md) (39 codes) — mmWave-radar temperature and operation.
  - [`0x16-flight-control.md`](hms-codes/0x16-flight-control.md) (**921 codes** — 52% of catalog) — flight-control system. Sub-sectioned by second byte: `00` FC · `01` sensor · `02` tachometer · `03` accelerometer · `04` barometer · `05` GNSS · `06` compass · `07` RTK · `08` motors/ESC · `09` battery · `0A` registration · `10` takeoff readiness · `11` thermal/accessory · `20` USB/ext · `30` BDS · `40`–`4A` internal subsystems (abstract-data, DSP, DBus, intelligent-flight-modes, landing/wayline, fusion/hall/RTK, positioning, planner, control loops) · `67` Power Line Follow.
  - [`0x17-transmission.md`](hms-codes/0x17-transmission.md) (16 codes) — image transmission & RC link.
  - [`0x19-system-overload.md`](hms-codes/0x19-system-overload.md) (52 codes) — CPU / memory / network overload.
  - [`0x1A-vision-sensors.md`](hms-codes/0x1A-vision-sensors.md) (170 codes) — vision sensor faults across all positions.
  - [`0x1B-navigation-tracking.md`](hms-codes/0x1B-navigation-tracking.md) (138 codes) — navigation + Target Acquisition.
  - [`0x1C-camera.md`](hms-codes/0x1C-camera.md) (167 codes) — camera overheating, errors, SD-card full, EIS/H20-specific.
  - [`0x1D-gimbal.md`](hms-codes/0x1D-gimbal.md) (45 codes) — gimbal stuck, calibration, overload.
  - [`0x1E-psdk-payload.md`](hms-codes/0x1E-psdk-payload.md) (28 codes) — third-party PSDK payload + DJI searchlight + speaker.
  - [`0x1F-cellular-lte.md`](hms-codes/0x1F-cellular-lte.md) (56 codes) — LTE transmission + DJI Cellular Dongle.
  - [`0x20-takeoff-tags.md`](hms-codes/0x20-takeoff-tags.md) (2 codes) — "Remove before takeoff" + control-stick centered.
- [`hms-codes/outliers.md`](hms-codes/outliers.md) (1 entry) — the literal `unknown` alarmId with generic fallback tip.

**Curated CN→EN translations**: 531 entries — DJI leaked Chinese developer-debug strings under `tipEn`. Stored in [`_build/_translations.json`](_build/_translations.json); rendered inline with trailing **+** marker; CN originals preserved verbatim under collapsible `CN source` blocks within each affected second-byte subsection. Translation style: DJI's typical user-facing warning voice for user-level strings; literal technical translation for dev-debug strings (with internal symbols like `DBus topic gimbal_state`, `ap_fusion`, `circular_tracking` kept as code spans).

**Error codes** ([`error-codes/`](error-codes/README.md) — 1 file, 448 codes):

- [`error-codes/README.md`](error-codes/README.md) — single-doc per TODO.md. Preamble explains the `ABCDEF` format (source `A` = 3/5 device-side, 4/6 Pilot 2; module `BC`; local `DEF`). Grouped tables per BC module across 20 buckets (`312`–`514`). Module labels cross-referenced with DJI-Cloud-API-Demo enum classes (`FirmwareErrorCodeEnum` / `WaylineErrorCodeEnum` / `LogErrorCodeEnum` / `CommonErrorEnum` / `DebugErrorCodeEnum` / `ControlErrorCodeEnum` / `LiveErrorCodeEnum` / `DrcStatusErrorEnum`).

**v1.11 → v1.15 error-code drift**: Fully additive. 5 new codes in v1.15 (`321788`, `327022`, `341002`, `514155`, `514168`); 0 dropped. Documented in `error-codes/README.md` §4.

**Reproducibility artifacts** ([`_build/`](_build/)):

- [`_build/_translations.json`](_build/_translations.json) — 531 curated CN→EN translations keyed by alarmId.
- [`_build/generate_hms_codes.py`](_build/generate_hms_codes.py) — reads HMS.json + translations, emits 14 per-prefix files + README + outliers. Re-runnable after source refresh.
- [`_build/generate_error_codes.py`](_build/generate_error_codes.py) — reads HMS-Codes.txt + v1.11 drift source, emits the single error-codes README. Re-runnable.

PLAN.md mentions "Sanity-check script optional future polish" — these two generators are the materialization of that intent.

**Corpus updates**:

- [`README.md`](README.md) — TOC rows filled in for `hms-codes/` and `error-codes/`.
- [`TODO.md`](TODO.md) — Phase 8 checklist fully checked with drop-down details; "current phase" banner advanced to "Phase 8 content-complete, review gate pending; Phase 9 next".
- `OPEN-QUESTIONS.md` — **no new entries.** All Phase 8 source defects (CN-in-`tipEn`, filename mismatch, full-width-paren use, `unknown` fallback, uppercase-X outlier) are local DJI source defects that do not require clarification.

### Design decisions locked at Phase 8 drafting

Carried into Phase 9 / 10 where relevant:

1. **Single-drop phase** per PLAN.md framing. Reproducible pipeline makes sub-phasing unnecessary — any fix-up or source-refresh is a script re-run, not a re-draft.
2. **HMS layout = 14 files by first-byte prefix + sub-sectioned 0x16**. Keeps a 1:1 mapping with the DJI wire-level identifier while giving the 921-entry flight-control file a navigable internal structure. Alternatives (monolithic, per-second-byte physical split, cross-prefix functional grouping) were rejected.
3. **CN-in-`tipEn` policy — curate + mark + preserve**. DJI shipped ~30% of alarms with CN under the English field. We translate to English (flagged **+**), keep the CN verbatim in a collapsible callout under each subsection, and document the defect in the master README. This follows the "English-only corpus, flag translated passages" directive while preserving the audit trail per "real payloads only, no fabrication."
4. **Full-width parens normalize to ASCII**. 167 tips use U+FF08/FF09 `（ ）` (Chinese full-width) around otherwise-English content — pure copy defect. Generator normalizes to `(` `)` silently; not worth a per-entry callout.
5. **Error-codes = single file grouped by BC module**. TODO.md says "`error-codes/README.md` with grouped table" — single doc per that spec. BC module is DJI's own wire-level grouping (the second and third digits of `ABCDEF`), so partition aligns with DJI convention.
6. **Source-filename irony preserved as documentation**. The source file [`DJI_CloudAPI-HMS-Codes.txt`](../DJI_Cloud/DJI_CloudAPI-HMS-Codes.txt) is named "HMS-Codes" but contains general API error codes — DJI's own preamble explicitly says HMS alarm descriptions are **not** in this file. The corpus's `error-codes/README.md` §6 documents this mismatch so future readers aren't confused.
7. **`_build/` stays tracked in-repo, not gitignored**. The generator scripts + translations are first-class corpus artifacts — they let anyone regenerate the Phase 8 output from the two primary sources. PLAN.md's "Sanity-check script optional future polish" is satisfied.

### DJI-source inconsistencies noted during Phase 8

Carry into Phase 9 workflow authoring; none rise to OQ level:

**HMS**:

- **531 entries carry CJK-ideograph content in `tipEn`** — DJI leaked Chinese developer-debug strings under the English copy key. Concentrated in 0x16 second-byte ranges 0x40 (abstract-data topics), 0x41 (DSP interaction), 0x42 (DBus topics), 0x43 (intelligent flight modes — tracking, QuickShots, MasterShots, Hyperlapse, APAS, OA), 0x46 (fusion/hall/RTK), 0x47 (positioning + compass calibration — compass-cal entries are user-facing), 0x49 (planner + global map), 0x4A (control loops). Handled per policy above.
- **`unknown` alarmId** — a literal non-hex entry with generic fallback tip. Preserved as outlier.
- **`0X1B033001`** — uppercase-`X` casing (all other IDs use `0x`). Preserved verbatim, filed under `0x1B`.
- **167 entries use full-width Chinese parens** around otherwise-English content. Normalized to ASCII in the catalog.
- **Prefix-byte taxonomy is inferred, not DJI-documented**. Master README flags this explicitly — the per-file "inferred domain" label is a corpus convenience, not a DJI-authored claim.

**Error codes**:

- **Source filename mismatch** — [`DJI_CloudAPI-HMS-Codes.txt`](../DJI_Cloud/DJI_CloudAPI-HMS-Codes.txt) actually holds general API error codes; HMS alarms are in [`HMS.json`](../DJI_Cloud/HMS.json). DJI's own preamble line 5 clarifies this.
- **Source digits `4` and `6` (Pilot 2) are undocumented with codes** — the `ABCDEF` format allows A = 3/4/5/6 but v1.15 extracts only carry `3xxxxx` and `5xxxxx` codes. Pilot-2 `4xxxxx` / `6xxxxx` codes would come from Pilot-specific sources not in this repo.
- **Substitution placeholders persist** — `{dock_org_name}` and similar template variables appear in tip text (e.g., `312015`). Cloud implementations must substitute these from their own context; DJI does not document the substitution contract.
- **Modules `341` and `386` have 1 code each** — these are likely experimental or partially-deployed; preserved as-is.

No new OQ entries.

### Phase 8 completion summary

| File | Entries | Scope |
|---|---|---|
| [`hms-codes/README.md`](hms-codes/README.md) | — | master index + policy |
| [`hms-codes/0x16-flight-control.md`](hms-codes/0x16-flight-control.md) | 921 | flight-control subsystem |
| [`hms-codes/0x1A-vision-sensors.md`](hms-codes/0x1A-vision-sensors.md) | 170 | vision sensors |
| [`hms-codes/0x1C-camera.md`](hms-codes/0x1C-camera.md) | 167 | camera |
| [`hms-codes/0x1B-navigation-tracking.md`](hms-codes/0x1B-navigation-tracking.md) | 138 | navigation & target acquisition |
| [`hms-codes/0x1F-cellular-lte.md`](hms-codes/0x1F-cellular-lte.md) | 56 | cellular |
| [`hms-codes/0x14-payload-imu.md`](hms-codes/0x14-payload-imu.md) | 52 | payload IMU |
| [`hms-codes/0x19-system-overload.md`](hms-codes/0x19-system-overload.md) | 52 | system overload |
| [`hms-codes/0x11-payload-general.md`](hms-codes/0x11-payload-general.md) | 45 | payload general |
| [`hms-codes/0x1D-gimbal.md`](hms-codes/0x1D-gimbal.md) | 45 | gimbal |
| [`hms-codes/0x15-mmwave-radar.md`](hms-codes/0x15-mmwave-radar.md) | 39 | mmWave radar |
| [`hms-codes/0x12-battery-station.md`](hms-codes/0x12-battery-station.md) | 37 | battery station |
| [`hms-codes/0x1E-psdk-payload.md`](hms-codes/0x1E-psdk-payload.md) | 28 | PSDK payload |
| [`hms-codes/0x17-transmission.md`](hms-codes/0x17-transmission.md) | 16 | transmission |
| [`hms-codes/0x20-takeoff-tags.md`](hms-codes/0x20-takeoff-tags.md) | 2 | takeoff tags |
| [`hms-codes/outliers.md`](hms-codes/outliers.md) | 1 | non-hex outlier |
| [`error-codes/README.md`](error-codes/README.md) | 448 | general API error codes |
| [`_build/_translations.json`](_build/_translations.json) | 531 keys | CN→EN translations |
| [`_build/generate_hms_codes.py`](_build/generate_hms_codes.py) | — | HMS generator |
| [`_build/generate_error_codes.py`](_build/generate_error_codes.py) | — | error-codes generator |

Total Phase 8 output: **17 content files + 3 pipeline artifacts**, **1,769 HMS alarm entries + 448 error codes = 2,217 codes documented**.

### Remaining phases after Phase 8

- Phase 9 — Workflows. Dependencies now all satisfied: Phases 3 (HTTP), 4 (MQTT), 5 (WebSocket) transport catalogs done; Phase 7 WPML + livestream-protocols available to cite for wayline-upload / livestream-start workflows; Phase 8 codes available for error-path callouts in each workflow. Expected output ~11 workflow docs per PLAN.md §Phase 9.
- Phase 10 — Device annexes + final corpus review.

---

## 2026-04-19 — handoff at Phase 7 close, ready for review gate

### State of play

- Phases 0, 1, 2, 3, 4, 5, 6 complete and committed. **Phase 7 (WPML + livestream protocols) content-complete.**
- Phase 7 review gate is the only remaining Phase 7 item.
- **Phase 8 (HMS codes + error codes) is next** after the review gate.

### What Phase 7 produced

Phase 7 was a **single-drop phase** per PLAN.md's intent — no sub-phases. All 10 files delivered in one pass across two new top-level directories.

**WPML** (wayline file format, 5 files):

- [`wpml/overview.md`](wpml/overview.md) — WPML format intro. `.kmz` ZIP archive containing `template.kml` + `waylines.wpml` + `res/`. Namespace `xmlns:wpml="http://www.dji.com/wpmz/1.0.2"` (note: `wpmz` not `wpml` in the URL). Device-support conventions — WPML labels the M4 Enterprise cohort `M4E/M4T` with no separate M4D/M4TD row; the corpus treats that label as including in-scope M4D/M4TD (see §4.1). Existing-route change note (M300 RTK re-save in DJI Pilot 2 for format upgrade).
- [`wpml/template-kml.md`](wpml/template-kml.md) — `template.kml` full catalog. Create info + mission config + 4 template types:
  - `waypoint` — discrete waypoint flight; each `<Placemark>` is a concrete waypoint.
  - `mapping2d` — 2D area mapping (survey polygon + overlap + grid pattern).
  - `mapping3d` — 3D oblique photography. **Produces 5 executable waylines** (1 orthophoto + 4 oblique) → 5 `<Folder>` elements in `waylines.wpml`.
  - `mappingStrip` — strip/linear flight (LineString + lateral extension).
  Plus coordinate params + overlap rate + mapping heading param sections. 5 DJI-source inconsistencies flagged.
- [`wpml/waylines.md`](wpml/waylines.md) — `waylines.wpml` catalog. Mission config + `<Folder>`-per-wayline + `<Placemark>`-per-waypoint + `wpml:executeHeightMode` vs template's `wpml:heightMode` distinction + optional `wpml:startActionGroup` (M30/M30T/M3-series/M4E family only; runs before wayline starts + on recovery from interruption).
- [`wpml/common-elements.md`](wpml/common-elements.md) — the **largest Phase 7 doc**. Shared schemas (`droneInfo`, `payloadInfo`, `payloadParam`, `waypointHeadingParam` + `globalWaypointHeadingParam`, `waypointTurnParam`, `autoRerouteInfo` — the latter **M3D/M3TD + M4E/M4T only**, two-bool `missionAutoRerouteMode` + `transitionalAutoRerouteMode`), action chain (`actionGroup` → `actionTrigger` → `action`), and **16 actuator function parameter schemas**. Two actuator functions are explicitly **M4D/M4TD-labeled in DJI source** (not M4E/M4T): `megaphone` (plays Opus audio from `/wpmz/res/audio/`) and `searchlight` (off / illuminate / flash + brightness). 9 DJI-source inconsistencies flagged including: `actionActuatorFunc` enum lists 13 values but source documents 16 actuators; `focusY` description copy-pasted from `focusX`; `followBadArc` path-mode value reads as translation artifact; `megaphoneOperateLoop` label starts with Chinese character `是`; `accurateCameraApertue` / `orientedCameraApertue` DJI-typo (field must be sent with `Apertue` spelling); `payloadLensIndex` value `visable` DJI-typo; `accurateShoot` deprecated in favor of `orientedShoot`.
- [`wpml/README.md`](wpml/README.md) — path-level index with scope + doc jumplinks + related-doc pointers.

**Livestream protocols** (media-transport wire refs, 5 files):

- [`livestream-protocols/rtmp.md`](livestream-protocols/rtmp.md) — `url_type 1`. **All 4 in-scope cohorts.** URL shape `rtmp://host:port/app/stream`. Only protocol supported by every cohort; implement RTMP first for broadest coverage. Notes on RTMP variants (RTMPT / RTMPS / RTMPE) — DJI does not document support.
- [`livestream-protocols/gb28181.md`](livestream-protocols/gb28181.md) — `url_type 3`. **All 4 in-scope cohorts.** URL shape: `serverIP=…&serverPort=…&serverID=…&agentID=…&agentPassword=…&localPort=…&channel=…` (7 amp-joined kv pairs, not a URI). 20-digit GB28181 IDs. Describes SIP register → catalog → invite → PS-over-RTP media flow. Cloud must allocate valid 20-digit agent IDs.
- [`livestream-protocols/webrtc.md`](livestream-protocols/webrtc.md) — `url_type 4` / **WHIP only** per DJI explicit note. **Dock 2 + Dock 3 + RC Plus 2 — not RC Pro.** URL shape: `http://host:port/{whip-path}?app=…&stream=…`. DJI example path `/rtc/v1/whip/` matches SRS WHIP. Notes on STUN/TURN for NAT traversal. WHIP handshake flow described (POST SDP offer, 201 Created with SDP answer, ICE/DTLS/SRTP).
- [`livestream-protocols/agora.md`](livestream-protocols/agora.md) — `url_type 0`. **Dock 2 + RC Plus 2 + RC Pro — not Dock 3.** URL shape: `channel=…&sn=…&token=…&uid=…`. DJI's **URL-encode-exactly-once** rule for tokens containing `+` / `/` / `=` explicitly called out. Cloud must have Agora App ID + App Certificate and mint short-lived RTC tokens server-side. DJI's own DJI FlightHub historically used Agora — it's the default / historical option, not third-party.
- [`livestream-protocols/README.md`](livestream-protocols/README.md) — overall index with cohort×protocol matrix + JSBridge `type` enum cross-transport context note (JSBridge `{0: Unknown, 1: Agora, 2: RTMP, 3: RTSP, 4: GB28181}` ≠ MQTT `url_type {0: Agora, 1: RTMP, 3: GB28181, 4: WebRTC}`; a cloud operating a Pilot webview must translate and must not forward JSBridge RTSP to MQTT).

**Corpus updates**:

- [`README.md`](README.md) — TOC rows filled in for `wpml/` and `livestream-protocols/`.
- [`TODO.md`](TODO.md) — Phase 7 checklist fully checked with drop-down details; "current phase" banner advanced to "Phase 7 content-complete, review gate pending; Phase 8 next".
- `OPEN-QUESTIONS.md` — **no new entries.** All Phase 7 DJI-source inconsistencies are local source defects (typos, incomplete enums, translation artifacts) that don't require DJI clarification.

### Design decisions locked at Phase 7 drafting

Carried into Phase 8 / 9 / 10 where relevant:

1. **Single-drop phase** — no sub-phase split despite 10 files + ~2,500 lines of output. PLAN.md describes Phase 7 as "two self-contained spec references merged into one phase" and that framing held through drafting. No resume-mid-phase checkpoint was needed.
2. **`wpml/` = 1:1 doc mapping from 4 source files + README.** Exactly mirrors DJI's own page structure (Overview / Template-KML / Waylines / Common-Elements) so cross-refs back to DJI's developer site remain trivial. The large Common-Elements doc was the right call — 16 actuator functions in one place is more usable than 16 separate files.
3. **WPML "M4E/M4T" = in-scope M4D/M4TD** — carried throughout per [`overview.md §4.1`](wpml/overview.md#41-labeling-inconsistency--m4em4t-vs-m4dm4td). Exception: DJI explicitly labels `megaphone` and `searchlight` actuator functions as `M4D/M4TD` (not M4E/M4T), which [`common-elements.md §5.15 / §5.16`](wpml/common-elements.md#515-megaphone) preserves. This is DJI's distinction and the corpus mirrors it faithfully.
4. **Livestream protocols = per-protocol wire contract docs, not protocol compendium.** Each doc captures the DJI `url` shape + device support + what the cloud must host, and links out to external specs (Adobe RTMP PDF, GB/T 28181 overview, WHIP draft, Agora docs). We do **not** restate RTMP / GB28181 / WebRTC / Agora externally — those are stable, well-documented standards.
5. **RC Pro has no WebRTC; Dock 3 has no Agora.** These cohort asymmetries are the sharpest live-stream integration gotchas. Flagged in each affected doc's device-support table and cross-referenced back to the Phase 4d [`live_start_push.md`](mqtt/dock-to-cloud/services/live_start_push.md) doc (which already documented the Dock 3 enum drop and the v1.15 example's residual-Agora-URL copy-paste defect).
6. **JSBridge cross-transport note in livestream-protocols/README.md** — Phase 7 is the right home for the JSBridge `type` vs MQTT `url_type` enum mismatch. JSBridge is pilot-app-only and the corpus treats MQTT as primary; a separate docs branch for JSBridge was considered and rejected.

### DJI-source inconsistencies noted during Phase 7

Carry into Phase 9 workflow authoring; none rise to OQ level:

**WPML**:

- Overview file-structure illustration is missing from v1.15 extract.
- Template-KML: `wpml:imageFormat` intro row lacks explicit required-cell; `heightMode` value `WGS84` has verbose DJI prose; `gimbalPitchAngle` in mapping2d context has empty Type column; `stripUseTemplateAltitude` uses "opened"/"enabled" interchangeably in translated prose; `quickOrthoMappingEnable` labeled M4E only (unclear if M4D/M4TD inherits).
- Waylines file: none beyond source inconsistencies already in common-elements.
- Common-Elements: `actionActuatorFunc` enum description lists 13 of 16 actuators; `focusY` description is a copy-paste of `focusX`; `followBadArc` path-mode value reads as translation artifact; `megaphoneOperateLoop` label starts with Chinese `是`; `accurateCameraApertue` / `orientedCameraApertue` — DJI field-name typo, must send exactly as-is; `payloadLensIndex` value `visable` is a typo for `visible`; `panoShot` cohort lists inconsistent (M30-only fields + M30/M3D/M4 others); `accurateShoot` deprecated but still in enum; WPML namespace `1.0.2` stable across samples.

**Livestream protocols**:

- Dock 3 example payload in [`live_start_push.md`](mqtt/dock-to-cloud/services/live_start_push.md) uses `url_type: 0` despite Dock 3 dropping Agora — already flagged in the Phase 4d doc.
- v1.11 prose for pilot-feature-set mentioned RTSP; v1.15 MQTT `url_type` does not expose RTSP; JSBridge `type=3` does expose RTSP. Cross-transport enum mismatch documented in [`livestream-protocols/README.md §3`](livestream-protocols/README.md#3-pilot-side-jsbridge-layer-cross-transport-context).
- All v1.15 livestream sources (Dock 2, Dock 3, RC Plus 2, RC Pro, plain RC) diverge on `url_type` enum population per cohort but agree on what each value means.

No new OQ entries.

### Phase 7 completion summary

| Doc | Lines | Scope |
|---|---|---|
| [`wpml/overview.md`](wpml/overview.md) | ~110 | format intro + archive layout + device support |
| [`wpml/template-kml.md`](wpml/template-kml.md) | ~250 | template file catalog, 4 template types |
| [`wpml/waylines.md`](wpml/waylines.md) | ~200 | execution file catalog |
| [`wpml/common-elements.md`](wpml/common-elements.md) | ~460 | shared schemas + 16 actuator functions |
| [`wpml/README.md`](wpml/README.md) | ~40 | index |
| [`livestream-protocols/README.md`](livestream-protocols/README.md) | ~80 | protocol matrix + JSBridge note |
| [`livestream-protocols/rtmp.md`](livestream-protocols/rtmp.md) | ~130 | `url_type 1`, all devices |
| [`livestream-protocols/gb28181.md`](livestream-protocols/gb28181.md) | ~150 | `url_type 3`, all devices |
| [`livestream-protocols/webrtc.md`](livestream-protocols/webrtc.md) | ~140 | `url_type 4`, not RC Pro |
| [`livestream-protocols/agora.md`](livestream-protocols/agora.md) | ~160 | `url_type 0`, not Dock 3 |

Total Phase 7 output: **10 files**, roughly **1,720 lines** of markdown.

### Remaining phases after Phase 7

- Phase 8 — HMS codes + error codes. Sources: `DJI_Cloud/DJI_CloudAPI-HMS-Codes.txt` (full code list), `DJI_Cloud/HMS.json` (structured data), `DJI_Cloud/DJI_CloudAPI-HMS.txt` (overview), `DJI-Cloud-API-Demo/` error definitions, `Cloud-API-Doc/` error-code page. First step: inspect `HMS.json` structure to determine natural category partition and propose to user before drafting.
- Phase 9 — Workflows. Dependency: Phases 3–5 transport catalogs (done). Phase 7 wayline docs are now available to cite for `workflows/wayline-upload-and-execution.md`, and the livestream-protocols docs feed `workflows/livestream-start-stop.md`.
- Phase 10 — Device annexes + final corpus review.

---

## 2026-04-19 — Phase 6 wrap-up: v1.15-only policy locked + OQ-003 resolved + TODO.md reconciled

Brief housekeeping entry closing out the Phase 6 session. No new corpus content. Picked up after the `docs: close Phase 6 review gate` commit (`f4e9de4`).

### What changed

1. **OQ-001 resolved** — corpus documents **Cloud API v1.15 only**. [`Cloud-API-Doc/`](../Cloud-API-Doc/) (v1.11.3) is retained in-repo solely for `§5 drift` cross-check on the per-device docs — never primary. Policy in [`OPEN-QUESTIONS.md`](OPEN-QUESTIONS.md#oq-001--source-version-mismatch-between-cloud-api-doc-v1113-and-dji_cloud-v115) (resolution section) and [`SOURCES.md`](SOURCES.md) (authority ranking simplified, per-source entries updated). **No change to existing corpus content** — Phases 0–6 already followed this policy in practice; the resolution just formalizes it.

2. **OQ-003 resolved** — scanned [`DJI-Cloud-API-Demo/`](../DJI-Cloud-API-Demo/) for MQTT QoS / retain evidence. Findings documented in [`OPEN-QUESTIONS.md`](OPEN-QUESTIONS.md#oq-003--mqtt-qos-retain-and-clean-session-settings-are-not-specified-in-djis-published-documentation):
   - Cloud subscribes all inbound topics at **QoS 1** (`MqttConfiguration.java:54`).
   - Cloud publishes default at **QoS 0** (`MqttGatewayPublish.java:31`).
   - Cloud publishes `_reply` topics at **QoS 2** (`MqttGatewayPublish.java:72`).
   - Cloud **never sets `retain`** (Paho default `false`).
   - Device-side publish QoS not directly observed (demo is cloud-side only).
   - [`mqtt/README.md`](mqtt/README.md) §8 updated with the evidence table; Phase 4 per-topic entries can reference §8.

3. **TODO.md reconciled** — 6 stale unchecked boxes ticked:
   - Phase 0 `Review gate` + `Initial commit` — clearly closed since 24+ commits exist; reconciled with initial-commit pointer `f6a63eb`.
   - Phase 4 sub-gates 4b / 4d / 4e-1 / 4e — all implicit-closed by subsequent sub-phases ("Continue at 4c/4e/4e-2/4f" pattern); marked with landing-commit pointers (`7742419`, `debf5f8`, `b5c81e3`, `f196c0b`).

After this entry, every unchecked box in [`TODO.md`](TODO.md) belongs to Phase 7 / 8 / 9 / 10 or standing items — nothing pre-Phase-7 is in a partially-complete state.

### What this doesn't change

- Every doc already in the corpus was written with v1.15 as authoritative. No rewrites needed.
- OQ-002 (pilot-to-cloud OSD copy-paste bug) stays **open** — it is DJI's own documentation bug, not a corpus-side decision. The corpus already works around it by citing per-aircraft property files for pilot-path OSD content. No action available on our side until DJI fixes the source.

### Phase 7 kickoff

Phase 7 is **WPML + livestream protocols**. Self-contained spec references; no cross-dependency on transport catalogs (those are done). Expected output ~8 docs:

- `wpml/overview.md`, `template-kml.md`, `waylines.md`, `common-elements.md` — DJI WPML wayline file format.
- `livestream-protocols/rtmp.md`, `gb28181.md`, `webrtc.md`, `agora.md` — per-protocol specifics.

Sources (v1.15-only per OQ-001): `DJI_Cloud/DJI_CloudAPI_WPML-*.txt` (4 files) for WPML; livestream protocol details spread across dock and RC feature-set files ([`DJI_CloudAPI-Dock3-LiveStream.txt`](../DJI_Cloud/DJI_CloudAPI-Dock3-LiveStream.txt), [`DJI_CloudAPI-Dock2-Live-Stream.txt`](../DJI_Cloud/DJI_CloudAPI-Dock2-Live-Stream.txt), [`DJI_CloudAPI_RC-Pro-Enterprise-Live-Stream.txt`](../DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Live-Stream.txt), [`DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Stream.txt`](../DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Stream.txt), and any Agora/GB28181/WebRTC-specific overview pages in `DJI_Cloud/`).

---

## 2026-04-19 — handoff at Phase 6c close, ready for final Phase 6 review gate

### State of play

- Phases 0, 1, 2, 3, 4, 5 complete and committed. Phase 6 (Device properties) — **6a + 6b + 6c landed**.
- **Sub-phase 6c content-complete** — RC Plus 2 Enterprise + RC Pro Enterprise gateway-level catalogs. Final Phase 6 review gate is the only remaining Phase 6 item.
- **Phase 7 (WPML + livestream protocols) is next** after the gate.

### What 6c produced

- [`device-properties/rc-plus-2.md`](device-properties/rc-plus-2.md) — RC Plus 2 Enterprise full catalog. **11 top-level properties** (6 OSD + 5 state), **0 writable**. Source [`DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt`](../DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt) (625 lines; column-per-row layout). 5 DJI-source inconsistencies flagged (dock-text leakage in `wireless_link` descriptions + Dock-2-style telecom-operator labels + 2-value `esim_activate_state` + 4-value `video_quality` + no example payload). §5 drift vs RC Pro — 3 rows: adds `drc_state`, absent `country`, `video_quality` enum swap. No v1.11 counterpart.
- [`device-properties/rc-pro.md`](device-properties/rc-pro.md) — RC Pro Enterprise full catalog. **11 top-level properties** (6 OSD + 5 state), **0 writable**. Source [`DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt`](../DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt) (68 lines; tab-separated row-per-line layout) + v1.11 canonical [`Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/00.properties.md`](../Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/00.properties.md). 5 inconsistencies flagged (same cosmetic dock-text leakage as RC Plus 2 + near-equivalence with out-of-scope plain-RC file). §5 v1.11 → v1.15 drift — single row: adds `cloud_control_auth`. No other v1.11 drift.
- Extended [`device-properties/README.md`](device-properties/README.md) §4.3 — 12-row RC coverage table + unique-property summary + plain-RC sibling note. Added §6 6c provenance rows for both RCs + v1.11 canonical + out-of-scope plain-RC file.
- Updated 4i pilot-to-cloud shells:
  - [`mqtt/pilot-to-cloud/osd/README.md`](mqtt/pilot-to-cloud/osd/README.md) — removed "pending 6c" markers, added per-RC OSD property enumeration (RC Plus 2: 6 OSD including `drc_state`; RC Pro: 6 OSD including `country`).
  - [`mqtt/pilot-to-cloud/state/README.md`](mqtt/pilot-to-cloud/state/README.md) — removed "pending 6c" markers on RC pointers.
  - [`mqtt/pilot-to-cloud/property-set/README.md`](mqtt/pilot-to-cloud/property-set/README.md) — **corrected** the 4i speculative RC writable list. The shell had guessed RC Plus 2 owned "SIM-slot selection, DRC-mode preferences, livestream toggles" as writable, and RC Pro as a "subset of RC Plus 2". Both wrong — neither RC owns any writable gateway property. Corrected table + explicit correction note in a new subsection. Same flavor of correction as the 6a Dock 2/3 property-set correction (which fixed a 7-entry guess down to 3 actual writable properties).
- Updated corpus [`README.md`](README.md) TOC.
- Updated [`TODO.md`](TODO.md) 6c section.

### Design decisions locked at 6c drafting

Carried into Phase 10 device-annexes if relevant:

1. **Each RC gets a standalone catalog** — the two RCs are not delta-of-each-other (they swap `drc_state` ↔ `country`), so `rc-pro.md` → `rc-plus-2.md` delta treatment was rejected in favor of two full catalogs + drift tables. Matches the dock pattern: dock2.md full catalog, dock3.md full catalog + drift-vs-Dock-2 table.
2. **RC Plus 2 drift table references RC Pro** (cohort sibling) rather than v1.11 (nonexistent). RC Pro drift table references v1.11 (additive: adds `cloud_control_auth`) plus brief cross-ref to RC Plus 2 §5.
3. **Plain RC sibling file kept out of scope** — [`DJI_CloudAPI_RC-Properties.txt`](../DJI_Cloud/DJI_CloudAPI_RC-Properties.txt) is byte-equivalent to the RC Pro Enterprise file at the catalog level. Documented in `rc-pro.md` §4 (inconsistency note) + §7 (provenance) as a cross-check, not as a separate device doc. Same pattern as plain-RC callouts in 6a's out-of-scope policy.
4. **"Zero writable" as explicit finding** — each RC doc §3 states "None" rather than omitting the section, and explains that the `property/set` topic on the RC serial is still used (for aircraft-targeted writes). Avoids reader confusion since the wire topic exists even with zero RC-owned writable keys.
5. **4i property-set correction is inline** — put a dated "Correction — 4i speculative list (2026-04-19, 6c)" subsection in the shell rather than silently replacing the earlier wrong text. Keeps the audit trail of what changed and why, matching how 6a handled the speculative 7-entry Dock writable list.

### DJI-source inconsistencies noted during 6c

Carry into Phase 9 workflow authoring; none rise to OQ level:

- **`wireless_link` sub-field descriptions leak dock wording on both RCs** — `»dongle_number` = "Number of Dongles on the aircraft"; `»link_workmode` = "Dock's video transmission link mode". Cosmetic extract defect shared across dock / RC / aircraft property files; DJI's shared gateway-property template.
- **`dongle_infos.»esim_infos.»telecom_operator` + `dongle_infos.»sim_info.»telecom_operator` use Dock-2-style short labels** (`"Mobile"`, `"Telecommunications"`) on both RCs, versus Dock-3-style fully-qualified labels. Codes stable; same label drift as dock3.md §4.
- **`dongle_infos.»esim_activate_state` is 2-value on both RCs** (`{0: Not activated, 1: Activated}`) vs Dock 3's 3-value form (`{0: Unknown, 1: Not activated, 2: Activated}`). RC never emits code `2`; narrower-than-Dock-3 parsing is fine.
- **`live_status.»video_quality` 4-value vs 5-value enum incompatibility** between RC Plus 2 and RC Pro. Cloud implementations emitting / parsing this field must branch on RC cohort. Not a source defect; a genuine cohort delta.
- **No OSD example in either source file** — both extracts are property-list-only. Cloud implementations assume the shared pilot-to-cloud envelope from Phase 4i shells.
- **Plain-RC sibling file is byte-equivalent to RC Pro Enterprise** at the catalog level. Documented as a cross-check finding; plain RC is out-of-scope and does not get a per-device doc.

No new OQ entries.

### Phase 6 completion summary

After 6c, the full Phase 6 surface is:

| Doc | Top-level properties | Writable |
|---|---|---|
| [`dock2.md`](device-properties/dock2.md) | 48 (36 OSD + 12 state) | 3 |
| [`dock3.md`](device-properties/dock3.md) | 49 (37 OSD + 12 state) | 3 |
| [`_aircraft-pilot-base.md`](device-properties/_aircraft-pilot-base.md) | 42 (34 OSD + 8 state) | 3 |
| [`m3d.md`](device-properties/m3d.md) | 42 dock-path (24 OSD + 18 state) + baseline pilot-path | 6 dock-path (baseline 3 pilot-path) |
| [`m3td.md`](device-properties/m3td.md) | thermal-variant annex of M3D | — |
| [`m4d.md`](device-properties/m4d.md) | 42 dock-path + baseline + 7 M4D pilot extensions | 6 dock-path + 3 M4D pilot |
| [`m4td.md`](device-properties/m4td.md) | thermal-variant annex of M4D | — |
| [`rc-plus-2.md`](device-properties/rc-plus-2.md) | 11 (6 OSD + 5 state) | 0 |
| [`rc-pro.md`](device-properties/rc-pro.md) | 11 (6 OSD + 5 state) | 0 |

Plus the master matrix [`README.md`](device-properties/README.md) with §4.1 (dock gateway), §4.2 (aircraft), §4.3 (RC) coverage tables.

**Writable surface totals** (wire-level, gateway-grouped):

- Dock-path writable (landing on `thing/product/{dock_sn}/property/set`): 3 dock-gateway + 6 aircraft = 9 keys (M3D and M4D share 6 writable aircraft keys with cohort-specific enum / text drift).
- Pilot-path writable (landing on `thing/product/{rc_sn}/property/set`): 3 aircraft baseline (all cohorts) + 3 M4D-only extensions = 6 keys on M4D cohort; 3 keys on M3D cohort. **Zero RC-owned writable keys.**

### Remaining phases after Phase 6

- Phase 7 — WPML + livestream protocols. Sources: `DJI_Cloud/DJI_CloudAPI_WPML-*.txt` (multiple WPML extracts) + `Cloud-API-Doc/` canonical. Four WPML files (`wpml/overview.md`, `template-kml.md`, `waylines.md`, `common-elements.md`) + four livestream files (`rtmp.md`, `gb28181.md`, `webrtc.md`, `agora.md`). No cross-dependency on transport catalogs — can start immediately after Phase 6 review gate.
- Phase 8 — HMS codes + error codes.
- Phase 9 — Workflows (depends on Phases 3–5 transport catalogs; those are done).
- Phase 10 — Device annexes + final review. Per-device quirks that didn't fit the property catalogs (e.g., RC-level SIM-slot selection mechanics, DRC authorization semantics on RC Pro where the gateway doesn't publish `drc_state`).

---

## 2026-04-19 — handoff at Phase 6b close, ready for review gate

### State of play

- Phases 0, 1, 2, 3, 4, 5 complete and committed. Phase 6 (Device properties) — **6a + 6b landed**.
- **Sub-phase 6b content-complete** — aircraft catalog for M3D, M3TD, M4D, M4TD + shared pilot-path baseline. Phase 6b review gate is the only remaining 6b item.
- **Phase 6c (RCs) is next** — RC Plus 2 Enterprise + RC Pro Enterprise gateway-level catalogs.

### What 6b produced

- [`device-properties/_aircraft-pilot-base.md`](device-properties/_aircraft-pilot-base.md) — shared pilot-path aircraft baseline. 42 top-level (34 OSD + 8 state) + the `{type-subtype-gimbalindex}` per-payload struct with laser-ranging + thermal fields. Cites the full camera struct (wide / zoom exposure modes, 60-value shutter enum, ISO enum, etc.) inline to be self-contained. 3 writable properties (`height_limit`, `night_lights_state`, `camera_watermark_settings` struct) + the thermal cluster on the payload struct.
- [`device-properties/m3d.md`](device-properties/m3d.md) — M3D dock-path catalog (42 top-level: 24 OSD + 18 state) + pilot-path section citing the base. Dock-path source [`DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt`](../DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt) (2,373 lines — biggest Phase 6 source). 6 writable dock-path properties. Dock-path adds `"10":"RTK fixed"` to `position_state.»quality` and extends `mode_code_reason` to value 23 vs the pilot-path baseline. v1.11 cross-check confirms schema stable (v1.15 adds `distance_limit_status` + `rth_altitude` as new top-level aircraft properties).
- [`device-properties/m3td.md`](device-properties/m3td.md) — thermal-variant annex for M3D. Same property catalog; thermal variant distinguished at the `{domain-type-subtype}` device-model-key level, not at the property level.
- [`device-properties/m4d.md`](device-properties/m4d.md) — M4D dock-path catalog (42 top-level, same shape as M3D with two cohort deltas) + pilot-path section. Dock-path source [`DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt`](../DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt) (218 lines). Pilot-path source [`DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`](../DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt) (117 lines — **delta spec**, not full catalog). **7 M4D-only pilot-path extensions** beyond the baseline: `offline_map_enable`, `current_rth_mode`, `rth_mode`, `commander_flight_height` (rw), `commander_flight_mode` (rw), `current_commander_flight_mode` (read-back only on pilot-path), `commander_mode_lost_action` (rw). `mode_code` enum extended to value 19 `"Dock site evaluation in progress"`. No v1.11 counterpart for M4D on either path.
- [`device-properties/m4td.md`](device-properties/m4td.md) — thermal-variant annex for M4D. Property-level identical to M4D.
- Extended [`device-properties/README.md`](device-properties/README.md) §4.2 with a full 56-row aircraft coverage table (columns: Dock-path M3\* / Dock-path M4\* / Pilot-path M3\* / Pilot-path M4\*, rows grouped by semantic family). Added §4.3 pointer to pending 6c RC catalogs. Added §6 provenance table for 6b sources.
- Updated 4i shells (dock-to-cloud + pilot-to-cloud `osd/`, `state/`, `property-set/`) to link real 6b docs (removed the "pending 6b" markers; corrected property-source citations). Also added a **dock-vs-pilot path clarification** to [`mqtt/pilot-to-cloud/osd/README.md`](mqtt/pilot-to-cloud/osd/README.md) — the 4i language said aircraft OSD is "gateway-agnostic" but 6b discovered that while the topic is gateway-agnostic, the *set* of properties differs meaningfully (17 dock-path-exclusive properties, 1 pilot-path-exclusive, with occasional type drift on shared properties).
- Updated corpus [`README.md`](README.md) TOC and [`TODO.md`](TODO.md) 6b section.

### Design decisions locked at 6b drafting

Carried into 6c:

1. **Aircraft pilot-path baseline as a single source of truth** — [`_aircraft-pilot-base.md`](device-properties/_aircraft-pilot-base.md) carries the full catalog from [`Aircraft-Properties.txt`](../DJI_Cloud/DJI_CloudAPI_Aircraft-Properties.txt); per-aircraft pilot-path sections (m3d.md §B, m4d.md §B) cite the baseline and enumerate only deltas. Avoids duplicating ~250 rows across four aircraft files.
2. **Dock-path docs inline the full catalog** — readers doing an M3D dock-path lookup should not need to cross-reference three files. The m3d.md dock-path table (§A.1 / A.2) is self-contained. m4d.md §A refers to m3d.md §A.1/A.2 for the shared shape and enumerates only the M4D-specific cohort deltas (`mode_code` value 21, `remaining_power_*` text).
3. **Thermal variants as deltas** — m3td.md and m4td.md are small annex files. Property catalogs are identical; differences are at the payload enum level and are flagged for deeper treatment in Phase 10 device-annexes.
4. **Camera struct enum compression** — the 60-value shutter speed enum, 32-value EV enum, 13-value ISO enum are inlined once in [`_aircraft-pilot-base.md`](device-properties/_aircraft-pilot-base.md) §1 and cited ("same 60-value enum as `wide_shutter_speed`") in the per-device dock-path tables. Keeps tables readable while preserving full grep-ability.
5. **M4D pilot-path extract is a *delta spec***, not a full catalog — critical to flag (m4d.md §B.3). Cloud implementations that treat "absent from the Matrice4-Enterprise file" as "not published by M4D on pilot-path" will miss the baseline-inherited properties. This is DJI's own convention; we mirror it but call out the baseline-inheritance semantics clearly.
6. **Type drift between dock-path and pilot-path** — `latitude` / `longitude` / `height` are `double` on dock-path and `float` on pilot-path; `cameras.»zoom_factor` is `float` (dock) vs `int` (pilot-base) vs `float` (M3-series v1.11 pilot). Cloud parsers should be permissive.

### DJI-source inconsistencies noted during 6b

Carry into Phase 9 workflow authoring; none rise to OQ level:

- **`{_{type-subtype-gimbalindex}__aembLbhPpc}` garbled struct-name cell** in M4D dock-path and M4D pilot-path extracts. Source extraction artifact. Authoritative name: literal `{type-subtype-gimbalindex}`.
- **`mode_code` enum extensions divergent across paths**:
  - M3D dock-path: max 20 (`"POI"`).
  - M4D dock-path: max 21 (`"during the inbound and outbound flight procedures"`).
  - M3D pilot-path: max 18 (`"Airborne RTK fixing mode"`) — baseline.
  - M4D pilot-path: max 19 (`"Dock site evaluation in progress"`).
  - Cloud parsers should handle any of these; none are removed.
- **`mode_code_reason` enum** — pilot-path baseline max 22; dock-path extends to 23 (`"Triggered by strong winds in the dock scene (return)"`).
- **`position_state.»quality` enum** — pilot-path baseline stops at `"5":"Gear 5"`; dock-path adds `"10":"RTK fixed"`. An RTK-fixed aircraft reports `10` regardless of gateway.
- **Label drift between dock-path and pilot-path camera enums** — `"Shutter priority exposure"` vs `"Shutter Priority"`; `"Auto(high sense)"` vs `"Auto(High Sense)"`; `"-5.0ev"` vs `"-5.0EV"`; `"Fixed"` vs `"FIXED"`; `"Ir metering off"` vs `"Temperature measurement off"`. All enum codes stable.
- **Label drift `wind_direction` value 1**: `"True North"` (dock/pilot-baseline) vs `"North"` (M4D pilot extract).
- **`total_flight_time` type drift**: `float` (baseline) vs `int` (M4D pilot extract).
- **`obstacle_avoidance` accessMode drift**: `rw` (dock-path) vs `r` (pilot-path baseline).
- **`firmware_version` pushMode drift**: `1` / state (baseline) vs `0` / osd (M4D pilot extract).
- **`current_rth_mode` / `rth_mode` labels**: `"Intelligent altitude"` / `"Preset altitude"` (M3D dock-path) vs `"Optimal"` / `"Preset"` (M4D pilot extract). Same codes.
- **`remaining_power_for_return_home` recommendation text** differs between M3D ("Dock 2, 25–50%") and M4D ("Dock 3, 15–50%"). Wire range identical.
- **Pilot-path `{type-subtype-gimbalindex}` struct's nested `»payload_index` has `pushMode: 1`** while the parent struct is `pushMode: 0` OSD. Cosmetic source defect; the whole payload-indexed struct rides OSD.
- **`latitude` / `longitude` constraint cells use float-max/min dummy values** (`3.4028235E38` / `-1.4E-45`). Actual ranges `[-90, 90]` / `[-180, 180]` — source cosmetic.
- **`»»type` / `»»sub_type` in `battery.batteries`** have empty enum `{}` in source. Runtime-populated per battery model.

No new OQ entries.

### After 6b review gate — kickoff for 6c

**6c sources** (enumerated during 4i and re-verified 6b):

- [`DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt`](../DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt) (625 lines) — RC Plus 2 Enterprise primary. Much larger than RC Pro; likely includes RC-level gateway properties + relayed aircraft subset + DRC state.
- [`DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt`](../DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt) (68 lines) — RC Pro Enterprise primary. Thin extract — possibly a delta spec, possibly the full RC-level gateway catalog. Confirm at 6c enumeration.
- v1.11 canonical: [`Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/00.properties.md`](../Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/00.properties.md) — RC Pro Enterprise pilot-path properties.
- Out-of-scope sibling [`DJI_Cloud/DJI_CloudAPI_RC-Properties.txt`](../DJI_Cloud/DJI_CloudAPI_RC-Properties.txt) (67 lines) — plain RC, not enterprise; do not document. May have enum overlap worth cross-checking.

**Expected 6c output** (~500 lines total):
- [`device-properties/rc-plus-2.md`](device-properties/rc-plus-2.md) — RC Plus 2 Enterprise full catalog (~300 lines estimated based on source size).
- [`device-properties/rc-pro.md`](device-properties/rc-pro.md) — RC Pro Enterprise full catalog (~100 lines).
- Master matrix §4.3 extended with per-property RC coverage table.
- Updated 4i pilot-to-cloud shells with RC Phase 6c links (remove the remaining "pending 6c" markers on `rc-plus-2.md` / `rc-pro.md` citations).

**6c filing decisions to confirm at kickoff**:

- **RC Pro Enterprise 68-line file semantics** — is it a delta spec (vs RC Plus 2) or a standalone RC Pro catalog? If delta-spec, apply same pattern as M4D pilot-path (cite RC Plus 2 as base + enumerate deltas). If standalone, treat as full catalog.
- **RC Plus 2 vs RC Pro cohort split** — RC Plus 2 pairs with M4D (current gen), RC Pro with M3D/M3TD. At the RC property level, each RC reports its own serial's properties — they don't inherit from each other on the wire. But publication conventions may still share common structure.
- **RC-level `{gateway_sn}` ownership** — confirmed in Phase 4h that the RC is the `{gateway_sn}` on pilot-path; paired aircraft SN is the `{device_sn}`. RC property catalog is `{gateway_sn}`-scoped properties; paired aircraft property catalog is `{device_sn}`-scoped and belongs to the aircraft doc (6b).

### Known gotchas carried into 6c

- **6b-to-6c cross-link**: the pilot-path aircraft docs (m3d.md §B, m4d.md §B) describe what the **aircraft** publishes when relayed by an RC. The RC docs (6c) will describe what the **RC itself** publishes on its own `{gateway_sn}` topics. Keep these clearly separate.
- **`{gateway_sn}` in property-set** — pilot-path property-set always targets `{gateway_sn}` = RC serial, even when writing to an aircraft property. Phase 4h's pilot-to-cloud [`property-set/README.md`](mqtt/pilot-to-cloud/property-set/README.md) already captures this; 6c just confirms which RC-specific properties are writable.
- **Out-of-scope cohort references** — RC Plus 2's enums may reference M30 / M300 / M350 RTK aircraft (out-of-scope). Preserve those rows with out-of-scope notes for enum completeness, same pattern as 6a's Dock 2 / Dock 3 cross-references.
- **M30/M30T, M300/M350** — Per 6a decisions, keep out-of-scope devices' rows in enum tables (e.g., `compatible_device_type`) but do not document per-device.

### Open questions potentially affecting 6c

- [`OQ-001`](OPEN-QUESTIONS.md#oq-001--source-version-mismatch-between-cloud-api-doc-v1113-and-dji_cloud-v115) — v1.11 vs v1.15 drift. 6b had no semantic escalations; RC properties should also be mostly cosmetic given the RC feature surface is narrower than aircraft.
- [`OQ-002`](OPEN-QUESTIONS.md#oq-002--pilot-to-cloud-osd-struct-example-appears-to-be-a-copy-paste-of-the-dock-osd-example) — pilot OSD copy-paste bug. Resolved for 6b by citing per-aircraft property files; resolve similarly for 6c by citing per-RC files.
- [`OQ-003`](OPEN-QUESTIONS.md#oq-003--mqtt-qos-retain-and-clean-session-settings-are-not-specified-in-djis-published-documentation) — QoS / retain. Not affected by Phase 6.

### Remaining Phase 6 work

- **6c** — RC Plus 2 Enterprise + RC Pro Enterprise catalogs. Final Phase 6 review gate after 6c.

### Remaining phases after Phase 6

- Phase 7 — WPML + livestream protocols.
- Phase 8 — HMS codes + error codes.
- Phase 9 — Workflows.
- Phase 10 — Device annexes + final review.

---

## 2026-04-19 — handoff at Phase 6a close, ready for review gate

### State of play

- Phases 0, 1, 2, 3, 4, 5 complete and committed.
- Phase 6 (Device properties) started. **Sub-phase 6a landed** — master matrix README + Dock 2 + Dock 3 gateway properties. Phase 6a review gate is the only remaining 6a item.
- Phase 6b (aircraft: M3D, M3TD, M4D, M4TD) is next.

### What 6a produced

- [`device-properties/README.md`](device-properties/README.md) — master matrix + narrative. §4.1 (gateway-level dock properties table) is populated for Dock 2 + Dock 3; §4.2 (aircraft) and §4.3 (RC) are stubbed out with pending-6b / pending-6c markers.
- [`device-properties/dock2.md`](device-properties/dock2.md) — 48 top-level properties (36 OSD + 12 state), 3 writable. Full property table with nested struct fields preserved via DJI's `»` convention. 6 DJI-source inconsistencies flagged. v1.11 → v1.15 drift table.
- [`device-properties/dock3.md`](device-properties/dock3.md) — 49 top-level properties (37 OSD + 12 state), 3 writable. Dock 3 is a property superset of Dock 2 (+ `self_converge_coordinate`). 5 DJI-source inconsistencies flagged. Drift-vs-Dock-2 table (enum extension on `home_position_is_valid`, widespread label refinement).
- Updated 4i dock-to-cloud shells to link the real Phase 6 docs. Corrected the property-set shell's speculative writable-property list (was 7 entries including service methods and misidentified aircraft properties; actual Dock 2/3 writable surface is 3 properties).
- Updated corpus [`README.md`](README.md) and [`TODO.md`](TODO.md) with Phase 6 sub-phase structure.

### Design decisions locked at 6a kickoff

Carried into 6b/6c:

1. **Master matrix layout**: property-per-row with device-support columns (`✓`, `✓ rw`, blank), grouped by semantic family (Position / RTK, Comm, Livestream, Environment, Config, Battery, Maintenance, Mission, Metadata, Firmware, Storage, Media, Power, Dock physical, Topology, Safety, DRC). Built incrementally as sub-drops land.
2. **Per-device doc structure**: §1 OSD (pushMode=0) + §2 State (pushMode=1) + §3 Settable (accessMode=rw) + §4 DJI-source inconsistencies + §5 drift table + §6 property-set envelope + §7 source provenance. Nested struct fields preserved with `»` prefix. Enum values inline as JSON blobs.
3. **Aircraft docs in 6b**: single doc per aircraft with two sections — "Dock-path properties" and "Pilot-path properties". Same aircraft reports different subsets depending on which gateway is relaying.
4. **Shared aircraft properties**: extract to `_aircraft-pilot-base.md` (~250 rows from `DJI_CloudAPI_Aircraft-Properties.txt`). Per-aircraft pilot-path sections cite this file and enumerate only the deltas. Avoids 4× duplication across M3D / M3TD / M4D / M4TD.
5. **v1.11 vs v1.15 drift**: flag inline per-property. Policy is "prefer v1.15". Escalate to `OPEN-QUESTIONS.md` only if drift is **semantic** (enum values removed/renamed in a way that breaks existing cloud implementations, types changed, etc.). 6a drift is entirely cosmetic or additive — no escalations.
6. **Out-of-scope devices**: preserved in enum value tables (e.g., `rtcm_device_type: {1: Dock}` is fine; `compatible_device_type` enums that reference M30 / M300 keep the M30 / M300 rows with an "out-of-scope" note). No per-device doc.

### DJI-source inconsistencies noted during 6a

Carry into Phase 9 workflow authoring; none rise to OQ level:

- **`air_conditioner.air_conditioner_state` malformed enum** — both Dock 2 and Dock 3 v1.15 extracts have broken value-label encoding for values `10`–`15`. v1.11 Dock 2 has only `0`–`9`. Cloud should treat the `0`–`9` form as authoritative.
- **`wireless_link.4g_link_state` + `sdr_link_state` ship Chinese labels in Dock 2 extract** — known extract defect; Dock 3 has correct English.
- **`network_state.quality` label duplicate `"Poor" / "Poor"` in Dock 2 extract** — Dock 3 corrects to `"Very Poor" / "Poor"`.
- **`flighttask_step_code` value `255` ships Chinese `飞行器异常` in Dock 2** — Dock 3 has `"Aircraft Error"`.
- **`putter_state` in Dock 2 example but not in list** — undocumented field emitted by firmware.
- **`drone_battery_maintenance_info` missing `accessMode` on Dock 2** — default to `r`.
- **`sim_info.telecom_operator` vs `esim_infos.telecom_operator` enum labels disagree in Dock 3** — copy-paste lag; codes `{1, 2, 3}` map to China Mobile / China Unicom / China Telecom regardless of label.
- **Dock 3 example contains `electric_supply_voltage`, `flighttask_prepare_capacity`, `air_conditioner_mode` scalar** not in list — either list-omission or deprecated.

### After 6a review gate — kickoff for 6b

**6b sources**:

- `DJI_Cloud/DJI_CloudAPI_Aircraft-Properties.txt` (1,124 lines) — shared pilot-path aircraft baseline.
- `DJI_Cloud/DJI_CloudAPI_M3D_M3DT_Properties.txt` (2,373 lines — **biggest Phase 6 source**) — dock-path M3D + M3TD. The file contains both models co-documented; per-model cohort splits happen within the property table.
- `DJI_Cloud/DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt` (218 lines) — dock-path M4D + M4TD.
- `DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt` (117 lines) — pilot-path M4D.
- v1.11 canonical: `Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/10.aircraft/10.m3d-properties.md` (dock-path M3D) + `Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/10.m3-series/00.properties.md` (pilot-path M3-series) + `Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/30.others/10.aircraft/00.properties.md` (generic pilot-path aircraft).

**Expected surface**: ~500 property rows for M3D (largest), ~80 for M4D dock-path, ~40 for M4D pilot-path, ~250 shared. Total after dedupe ~600 unique property names on aircraft side, most heavily clustered in the M3D/M3TD dock-path source (camera subsystem with long enum tables for shutter speeds, ISO values, etc.).

**Expected output**: `_aircraft-pilot-base.md` (~400 lines extracted from shared source), `m3d.md` (~700 lines — both dock-path and pilot-path sections), `m3td.md` (~150 lines — deltas vs M3D), `m4d.md` (~400 lines), `m4td.md` (~150 lines — deltas vs M4D). Total 6b ~1,800 lines.

**6b filing decisions to confirm at kickoff**:

- Camera subsystem has very long enum tables (60+ values for shutter speeds, 30+ for exposure values). Inline as-is or truncate with "see expanded below"? Inline is simpler and preserves grep-ability, at the cost of wide tables. **Tentative: inline.**
- M3D vs M3TD: the DJI source co-documents both. Filing pattern: m3d.md = full catalog; m3td.md = deltas only pointing at m3d.md for shared. Same for M4D/M4TD.
- Dock-path vs pilot-path per aircraft: two sections in the same file, with clear subheaders.

### Known gotchas carried into 6b / 6c

- **Pilot-path aircraft OSD copy-paste bug ([`OQ-002`](OPEN-QUESTIONS.md))** — the pilot-to-cloud topic-definition file has an OSD struct example that shows dock content, not aircraft content. Don't cite that file for pilot-path OSD examples; use the per-aircraft property catalogs. 6b will need to resolve how to present pilot-path OSD content authoritatively.
- **Aircraft examples show payload-index-keyed sub-objects** — e.g., `"52-0-0": { "measure_target_altitude": 0, ... }`. The aircraft emits per-payload property groups keyed by `{type-subtype-gimbalindex}`. Per-aircraft docs will need a section explaining this keying pattern.
- **Shared aircraft properties (`Aircraft-Properties.txt`)** — 1,124 lines covers "generic" aircraft class, not any specific model. Extracting into `_aircraft-pilot-base.md` is the plan; may need to preserve the "aircraft class" framing in the file header.
- **v1.11 aircraft coverage**: v1.11 has M3 series and generic aircraft, but no M4 counterpart. M4D/M4TD docs will have no v1.11 drift section (same as Dock 3).

### Open questions potentially affecting 6b / 6c

- [`OQ-001`](OPEN-QUESTIONS.md#oq-001--source-version-mismatch-between-cloud-api-doc-v1113-and-dji_cloud-v115) — version drift. 6a had no semantic escalations; 6b aircraft camera enums are the most likely place for semantic drift (shutter speed value additions, exposure value refinements). Evaluate per-property.
- [`OQ-002`](OPEN-QUESTIONS.md#oq-002--pilot-to-cloud-osd-struct-example-appears-to-be-a-copy-paste-of-the-dock-osd-example) — pilot OSD copy-paste bug. 6b resolution: per-aircraft property files are the canonical source; the pilot topic-definition example is excluded.
- [`OQ-003`](OPEN-QUESTIONS.md#oq-003--mqtt-qos-retain-and-clean-session-settings-are-not-specified-in-djis-published-documentation) — QoS / retain. Not affected by Phase 6.

### Remaining Phase 6 work

- **6b** — aircraft (M3D, M3TD, M4D, M4TD) + shared pilot-path base. Review gate after.
- **6c** — RCs (RC Plus 2, RC Pro Enterprise). Final Phase 6 review gate after 6c.

### Remaining phases after Phase 6

- Phase 7 — WPML + livestream protocols.
- Phase 8 — HMS codes + error codes.
- Phase 9 — Workflows.
- Phase 10 — Device annexes + final review.

---

## 2026-04-19 — handoff at Phase 5 close, ready for review gate

### State of play

- Phases 0, 1, 2, 3, 4 complete and committed.
- Phase 5 (WebSocket message catalog) **content-complete**. 8 push messages across two families — map-elements (4) + situation-awareness (4).
- **Phase 5 review gate is the only remaining Phase 5 item.** Phase 6 (Device properties) is next.

### What Phase 5 produced

- `websocket/map-elements/` — 4 message docs: `map_element_create`, `map_element_update`, `map_element_delete`, `map_group_refresh`.
- `websocket/situation-awareness/` — 4 message docs: `device_osd`, `device_online`, `device_offline`, `device_update_topo`.
- `websocket/README.md` (Phase 2 doc) — extended §4 jump table with direct per-message doc links.
- Corpus `README.md` updated with Phase 5 landing.
- `TODO.md` Phase 5 section completed; only review gate remains.

### Scope was smaller than original plan

Phase 2's enumeration (which drafted the websocket/README.md) already surfaced the full 8-message inventory. Phase 5 did not discover additional `biz_code` values — the `sub_biz_code` possibility flagged in §3 of the README was checked during drafting and does not appear in any v1.15 sample. Per-message docs are straight instantiations of the Phase 2 inventory with payload tables + examples + cross-references to the MQTT / HTTP methods they coordinate with.

### Filing convention

- One file per message, filename verbatim after the `biz_code` (e.g., `map_element_create.md`) — consistent with Phase 4 method-doc naming.
- Family dirs (`map-elements/`, `situation-awareness/`) mirror DJI's v1.11 canonical subtree structure.

### DJI-source inconsistencies flagged during Phase 5 drafting

- **`device_osd` example swaps latitude and longitude.** DJI's sample ships `"latitude": 113.44444, "longitude": 23.45656` — but 113.4° is a longitude (South China), not a latitude. Real wire follows the field names, not the values. Flagged inline in [`websocket/situation-awareness/device_osd.md`](websocket/situation-awareness/device_osd.md).

Only one DJI bug in the whole phase — notably clean compared to the Phase 4 source inconsistency count. No new `OPEN-QUESTIONS.md` entries.

### After Phase 5 review gate

Phase 6 — Device properties — is the next major build. Sources were enumerated during 4i:

- Dock 2: `DJI_CloudAPI-Dock2-Properties.txt`
- Dock 3: `DJI_CloudAPI-Dock3-DeviceProperties.txt`
- M3D/M3TD: `DJI_CloudAPI_M3D_M3DT_Properties.txt` + shared aircraft
- M4D/M4TD: `DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt` + `DJI_CloudAPI_Matrice4-Enterprise-Properties.txt` + shared aircraft
- Shared aircraft: `DJI_CloudAPI_Aircraft-Properties.txt`
- RC Plus 2: `DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt` (625 lines)
- RC Pro: `DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt` (68 lines)
- v1.11 canonical: `Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/00.properties.md` (dock-side) + `Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/00.properties.md` + `.../10.m3-series/00.properties.md` (pilot-side)

Expected Phase 6 structure per PLAN.md:
- Master matrix (property × device support, including out-of-scope rows for enum completeness).
- Per-device doc: `device-properties/dock2.md`, `dock3.md`, `m3d.md`, `m3td.md`, `m4d.md`, `m4td.md`, `rc-plus-2.md`, `rc-pro.md`.
- Resolution of [`OQ-001`](OPEN-QUESTIONS.md) (v1.11 vs v1.15 drift) happens here — per-property.
- Phase 6 is substantial: the combined property sources likely total ~1500+ property entries across the 8 in-scope devices.

The 4i property shells already point at Phase 6 per-device docs; Phase 6 fills in the content those shells point to.

### Known gotchas for Phase 6

- **Master matrix first.** Before writing per-device docs, enumerate every distinct property name across all sources and build the master matrix. Per-device docs are then filtered views of that matrix.
- **Out-of-scope rows for enum completeness.** When a property has an enum that references devices outside scope (e.g., M30/M350 in a `compatible_device_type` enum), include the row but mark it out-of-scope rather than deleting it — complete enums matter for cloud implementations.
- **Shared aircraft properties.** `DJI_CloudAPI_Aircraft-Properties.txt` is common across all in-scope aircraft. Handle by having per-aircraft docs inherit from a shared aircraft section, rather than re-listing every shared property on each of M3D/M3TD/M4D/M4TD.
- **v1.11 vs v1.15 drift.** OQ-001 primarily affects Dock 2 enum values. Flag per-property drift inline and resolve by preferring v1.15 where the two versions disagree.

Phase 6 is likely a multi-sub-drop phase similar to Phase 4 — consider structuring as 6a (master matrix + dock devices), 6b (aircraft), 6c (RCs) if context pressure is high.

### Remaining phases

- Phase 6 — Device properties (next).
- Phase 7 — WPML + livestream protocols.
- Phase 8 — HMS codes + error codes.
- Phase 9 — Workflows.
- Phase 10 — Device annexes + final review.

---

## 2026-04-19 — handoff at Phase 4i close, ready for final Phase 4 review gate

### State of play

- Phases 0, 1, 2, 3 complete and committed.
- Phase 4 (MQTT topic catalog) — **sub-phases 4a, 4b, 4c, 4d, 4e-1, 4e-2, 4f, 4g, 4h, and 4i all landed**. Phase 4 is content-complete.
- Dock-to-cloud catalog: 197 methods. Pilot-to-cloud catalog: 94 methods. Property-family shells: 6 (dock + pilot × osd/state/property-set).
- **Final Phase 4 review gate is the only remaining Phase 4 item.** Phase 5 (WebSocket message catalog) is next.

### What 4i produced

- 6 thin shell READMEs, one per (path × property-family) combination:
  - `mqtt/dock-to-cloud/osd/README.md` — Dock 2 + Dock 3 + M3D + M3TD + M4D + M4TD OSD shell.
  - `mqtt/dock-to-cloud/state/README.md` — same device coverage, on-change push.
  - `mqtt/dock-to-cloud/property-set/README.md` — writable-property shell with envelope + per-property result-code enum.
  - `mqtt/pilot-to-cloud/osd/README.md` — RC Plus 2 + RC Pro + paired-aircraft OSD shell. Carries the OQ-002 pilot-OSD-copy-paste callout.
  - `mqtt/pilot-to-cloud/state/README.md` — parallel to dock-to-cloud state shell.
  - `mqtt/pilot-to-cloud/property-set/README.md` — parallel to dock-to-cloud property-set shell, plus a "services vs property-set" filing note.
- Each shell is ~30–70 lines: topic + push semantics + in-scope devices table + per-device source files + Phase 6 forward pointer + representative envelope example.
- `mqtt/dock-to-cloud/README.md` + `mqtt/pilot-to-cloud/README.md` updated with new `osd/`, `state/`, `property-set/` sections linking the shells.
- `mqtt/README.md` + corpus `README.md` updated with the 4i landing.
- `TODO.md` 4i checkboxes ticked; only the final Phase 4 review gate remains.

### Filing decision for 4i

**Per-family READMEs, not per-device shells.** The TODO language said "thin shells per device" but in practice the property wire-level surface (topic, push mode, envelope) is identical across devices on the same path — the per-device difference is the property *content*, which is Phase 6 scope. One README per (path × family) covers every in-scope device via a table and avoids writing 16+ near-identical per-device stubs. Consistent with the 4h cross-reference-table approach.

If the user wants per-device shell files at review, they're trivial to mass-generate from the READMEs.

### Why 4i is very small

- No new method content — property shells are wire-level pointers, not method docs.
- Property catalog is Phase 6. 4i only confirms "yes, this topic exists on this device for this push mode" and cites the source file the Phase 6 doc will consume.
- Total new content: 6 files × ~50 lines = ~300 lines. Plus 4 index updates and the TODO/RESUME-NOTES updates.

### DJI-source inconsistencies noted during 4i

Nothing new. 4i re-cites:

- [`OQ-001`](OPEN-QUESTIONS.md) — v1.11 vs v1.15 property enum drift. Cited on every shell; resolution is Phase 6.
- [`OQ-002`](OPEN-QUESTIONS.md) — pilot-to-cloud OSD example copy-paste bug. Prominently cited on [`mqtt/pilot-to-cloud/osd/README.md`](mqtt/pilot-to-cloud/osd/README.md) so Phase 6 authors don't rely on DJI's OSD example.
- [`OQ-003`](OPEN-QUESTIONS.md) — QoS / retain / clean-session unspecified. Cited on all 6 shells.

### After final Phase 4 review gate

Phase 5 — WebSocket message catalog — is next. Source: `DJI_Cloud/DJI_CloudAPI_Pilot-WebSocket-*.txt` (two files: Map-Elements-Push-Message and Situation-Awareness-Push-Message) + v1.11 Cloud-API-Doc `Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.websocket/` (the WebSocket is pilot-to-cloud only).

Phase 5 structure (from PLAN.md):
- One `.md` per push message type.
- Estimated surface: 8 biz_code values across two families (map-elements and situation-awareness) per Phase 2 enumeration. Phase 5 may uncover additional biz_codes during message-level drafting.
- Precedent from Phase 4: feature-area sub-drops with review gates. Phase 5 is small enough to likely land as a single drop.

### Known gotchas carried forward to Phase 5 and Phase 6

- Phase 6 (`device-properties/`) must be authored before these 4i shells are "complete" — right now every pointer to `device-properties/<device>.md` is a forward reference to a file that doesn't exist. This is intentional per the phased plan, but worth explicit flag at the review gate.
- Phase 9 workflows will reference both the method catalog (Phase 4) and the property shells (4i) plus the property catalog (Phase 6). 4i is designed to support that stitching.
- Phase 5 is entirely pilot-to-cloud; no dock-to-cloud WebSocket equivalent exists per Phase 2's enumeration.

### Open questions carried forward

- [`OQ-001`](OPEN-QUESTIONS.md) — resolve per-property during Phase 6.
- [`OQ-002`](OPEN-QUESTIONS.md) — called out in the pilot OSD shell; resolution is a Phase 6 decision (which source to treat as canonical for pilot-path aircraft OSD).
- [`OQ-003`](OPEN-QUESTIONS.md) — QoS / retain gap may finally get attention at Phase 5 if the WebSocket push families have different delivery guarantees. Otherwise defer to Phase 9 workflows.

---

## 2026-04-19 — handoff at Phase 4h close, ready for 4i

### State of play

- Phases 0, 1, 2, 3 complete and committed.
- Phase 4 (MQTT topic catalog) — **sub-phases 4a, 4b, 4c, 4d, 4e-1, 4e-2, 4f, 4g, and 4h all landed**. Dock-to-cloud catalog at 197 methods (sealed at 4g). Pilot-to-cloud catalog at 94 methods (landed in 4h).
- **4i is next** — property-family shells (`osd/`, `state/`, `property/set`) for both the dock-to-cloud and pilot-to-cloud paths. Thin pointer docs to Phase 6 `device-properties/`, not content-bearing. Est. ~16 shell docs (8 devices × 2 shell types on average).

### What 4h produced

- `mqtt/pilot-to-cloud/` — new subtree with `status/`, `events/`, `services/`, `drc/` family dirs. No `requests/` dir (pilot-to-cloud has no request-family methods per enumeration).
- `mqtt/pilot-to-cloud/README.md` — path-level index with a filing-convention explainer, five cross-reference tables (status, new events, parallel events, new services, parallel services, new DRC variants, parallel DRC methods), cohort roll-up, and a DJI-source inconsistencies section.
- 27 pilot-specific method docs:
  - `status/update_topo.md` — pilot gateway-sn semantics.
  - Events (2): `cloud_control_auth_notify`, `poi_status_notify`.
  - Services (5): `cloud_control_auth_request`, `cloud_control_release`, `poi_mode_enter`, `poi_mode_exit`, `poi_circle_speed_set`.
  - DRC variants (20): `drc_live_lens_change` + 19 drc-prefixed camera / gimbal / IR-metering methods pilot-to-cloud-specific.
- `mqtt/README.md` + corpus `README.md` updated with 4h landing + 94-method pilot-to-cloud total.
- `TODO.md` — 4h section re-scoped (94 methods vs ~70 estimate) with full method inventory; only the 4h review gate remains open.

### Filing-strategy decision for 4h

**27 new-method docs + cross-reference tables for ~67 parallels.** Rather than creating ~70 thin pointer files that repeat nothing but a cohort marker and a cross-link, the 4h [`pilot-to-cloud/README.md`](mqtt/pilot-to-cloud/README.md) carries rich tables that list every method with a direct link to its dock-to-cloud doc (same payload, RC is the `{gateway_sn}`). This preserves the grep-by-method-name ergonomic — the method name still appears verbatim in the README — while avoiding the file-bloat cost of near-duplicate pointer docs. Net: 29 new .md files under `pilot-to-cloud/` (1 README + 1 status + 7 new events/services + 20 DRC variants) covers a 94-method method surface.

This is a **deviation from the 4a–4g one-file-per-method convention.** Rationale: the dock-to-cloud catalog exercised that convention on a ~197-method set where every method was distinct. For pilot-to-cloud, ~70% of the methods are pure parallels with identical payloads — creating a thin doc for each adds no new information and dilutes the grep signal when searching for pilot-specific material. Flag during the 4h review gate if the user wants full pointer docs after all; trivial to mass-generate.

### Why the method count (94) is materially higher than the ~70 estimate

The 4g handoff projected "~70 methods" for 4h. Actual counts by source:

- **RC Plus 2 Enterprise Remote-Control (4420 lines)**: 40+ methods. The file is the largest pilot-to-cloud source and carries every drc-prefixed camera / IR / gimbal variant plus the shared DRC services that also appear on dock-to-cloud 4e-2. Most methods are parallels of 4e-2; 19 are genuinely new variants (pilot-side DRC versions of 4c non-prefixed camera methods).
- **RC Plus 2 Enterprise Live-Flight-Controls (1164 lines)**: 21 methods — 11 events + 13 services (includes POI mode + cloud-control trio).
- **RC Pro Enterprise Live-Flight-Controls (1670 lines)**: 27 methods — more camera services than RC Plus 2 because RC Pro ships the non-prefixed `camera_*` methods on `/services` (not the drc-prefixed versions).
- **Live-Stream × 2 (358 + 196 lines)**: 5 unique methods (4 shared + `drc_live_lens_change` RC Plus 2 only).
- **Device-Management × 2**: `update_topo` (status-family).

Net: 94 unique method names across the two RC cohorts.

### DJI-source inconsistencies flagged during 4h drafting

Carry into Phase 9 workflow authoring:

- **Pervasive `"timestamp:"` trailing-colon typo in RC Plus 2 Live-Stream examples.** Every method in `DJI_CloudAPI_RC-Plus-2-Enterprise-Live-Stream.txt` has the typo. RC Pro Live-Stream and all other pilot-to-cloud sources are clean. Matches the Dock 3 pattern first flagged in 4c.
- **`poi_status_notify` 14-digit timestamp example** (`16540709686556`). Same 14-digit pattern as 4f's CFA / AirSense examples.
- **`drc_gimbal_reset` garbled `payload_index` schema cell** — DJI source reads `{_{type-subtype-gimbalindex}__aembLbhPpc}` as the Name column. Clearly a copy-paste artifact. Flagged inline in the doc.
- **`drc_camera_screen_split` reply example duplicates down-side fields** (`enable: true, payload_index: "89-0-0"`) instead of carrying `{"result": 0}`. DJI copy-paste error. Flagged inline.
- **`cloud_control_auth_request` / `cloud_control_release` replies carry `output.status: "ok"`** in the examples, but the `services_reply` schema declares only `result`. Treat `result` as authoritative; `output` is an extra convenience field DJI returns but does not document.
- **`drc_live_lens_change` example omits `seq`** — the DRC envelope specification requires `seq` as the correlation key. DJI's example omits it. Cloud implementations should include `seq` per the envelope spec.
- **RC Plus 2 `live_start_push` still supports Agora** (`url_type: 0` in the enum), contrasting Dock 3 which dropped Agora in 4d. Cohort split: dock-to-cloud Dock 3 has `{1, 3, 4}` only; pilot-to-cloud both RC Plus 2 and RC Pro have `{0, 1, 3, 4}`.
- **v1.11 RC Pro `update_topo` uses `thing_version`** (not Dock-2-v1.11's `version`). Matches v1.15 convention; the Dock-2-v1.11 `version` is the outlier.

None of these rise to `OPEN-QUESTIONS.md` level — doc-level callouts are sufficient.

### After 4h review gate (= kick-off of 4i)

**4i scope — property-family shells for both paths.** Sources:

1. `DJI_Cloud/DJI_CloudAPI_Aircraft-Properties.txt` (shared aircraft properties).
2. `DJI_Cloud/DJI_CloudAPI_RC-Plus-2-Enterprise-Properties.txt` (625 lines — the larger of the two RC properties files).
3. `DJI_Cloud/DJI_CloudAPI_RC-Pro-Enterprise-Properties.txt` (68 lines).
4. `DJI_Cloud/DJI_CloudAPI_RC-Properties.txt` (67 lines — out-of-scope cohort; do not document).
5. Dock 2 + Dock 3 properties across `DJI_CloudAPI-Dock2-*.txt` / `DJI_CloudAPI-Dock3-*.txt` wherever per-feature property tables appear.
6. v1.11 Cloud-API-Doc: `Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/*.md` (dock-side) and `Cloud-API-Doc/docs/en/60.api-reference/10.pilot-to-cloud/00.mqtt/20.rc-pro/00.properties.md` + `10.m3-series/00.properties.md` (pilot-side).

Expected 4i deliverables:
- Thin `osd/`, `state/`, `property-set/` family shells per device **that link to Phase 6** `device-properties/` for content. Avoid duplicating property catalogs — 4i shells are pointers, not content-bearing.
- Per-device breakdown under both `mqtt/dock-to-cloud/osd/` and `mqtt/pilot-to-cloud/osd/` (similar for `state/` and `property-set/`).
- Estimated ~16 shell docs total (8 in-scope devices × 2 major shell types; `property-set/` may be subsumed into the `state/` shell per device if the writable property set is small).
- 4i closes Phase 4 — final Phase 4 review gate after 4i.

### Known gotchas carried forward

- Property family shells at 4i are deliberately thin — they say *"this device publishes these properties on this topic; see `device-properties/<device>.md` for the property catalog"* and nothing more. Do not inline property tables; they belong in Phase 6.
- 4h's cross-reference table approach in [`pilot-to-cloud/README.md`](mqtt/pilot-to-cloud/README.md) is an experiment — if it works well for 4h, 4i can use the same approach (cross-ref table per device, minimal per-device shell files). The filing convention decision is not final until the 4h review gate closes.
- Review gate: user checkpoint before 4i starts. Don't push through.

### Open questions potentially affecting 4i

- [`OQ-001`](OPEN-QUESTIONS.md) — v1.11 vs v1.15 property enum divergences. Phase 6 is the canonical place for these to be resolved; 4i only provides transport-shell pointers.
- [`OQ-002`](OPEN-QUESTIONS.md) — pilot-to-cloud OSD example copy-paste bug. The `mqtt/pilot-to-cloud/osd.md` shell (4i) will explicitly cite the per-aircraft property files and warn against relying on DJI's pilot-to-cloud OSD example.
- [`OQ-003`](OPEN-QUESTIONS.md) — QoS / retain / clean-session values still unspecified. Property-family shells do not resolve this; defer.

### Remaining Phase 4 work (4i only)

- **4i** — property-family shells (`osd/`, `state/`, `property-set/`) per device, linking to Phase 6. Final Phase 4 review gate after 4i.

---

## 2026-04-19 — handoff at Phase 4g close, ready for 4h

### State of play

- Phases 0, 1, 2, 3 complete and committed.
- Phase 4 (MQTT topic catalog) — **sub-phases 4a, 4b, 4c, 4d, 4e-1, 4e-2, 4f, and 4g all landed**. **197 methods total** across the dock-to-cloud MQTT catalog.
- **4h is next** — pilot-to-cloud (RC Plus 2 Enterprise + RC Pro Enterprise). Est. ~70 methods (to be re-verified at enumeration).

### What 4g produced

- `mqtt/dock-to-cloud/events/` — 6 new docs: `speaker_tts_play_start_progress`, `speaker_audio_play_start_progress`, `psdk_floating_window_text`, `psdk_ui_resource_upload_result`, `custom_data_transmission_from_psdk`, `custom_data_transmission_from_esdk`.
- `mqtt/dock-to-cloud/services/` — 10 new docs: `speaker_play_volume_set`, `speaker_play_mode_set`, `speaker_play_stop`, `speaker_replay`, `speaker_tts_play_start`, `speaker_audio_play_start`, `psdk_input_box_text_set`, `psdk_widget_value_set`, `custom_data_transmission_to_psdk`, `custom_data_transmission_to_esdk`.
- `mqtt/dock-to-cloud/requests/storage_config_get.md` — **updated, not duplicated.** Pre-4g version documented `module = 0 = Media` only; 4g PSDK source shows `module = 1 = PSDK UI resources`. Added the second enum value, expanded the intro + relationship section, added PSDK sources to the provenance table.
- No new family directory — all 16 new methods fit into existing `events/` + `services/`.
- `mqtt/dock-to-cloud/README.md` — added sub-phase 4g status row (landed), added events + services table rows, extended the `storage_config_get` row with the `module` split, added a new "Sub-phase 4g sub-areas" section grouping by PSDK speaker / PSDK widgets / PSDK-Interconnection / ESDK-Interconnection, and added a "Filing note for 4g PSDK speaker/widget methods" explaining the 4g-vs-4e-2 parallel.
- `mqtt/README.md` + corpus `README.md` updated to 197-method total.
- `TODO.md` — 4g section re-scoped (16 methods vs ~40 estimate) and checkboxes ticked; only the 4g review gate remains open.

### Why the method count (16) is much lower than the ~40 estimate

The 4e-2 handoff projected "~40 methods" for 4g. Actual counts by source:

- **PSDK** (`DJI_CloudAPI-Dock3-PSDK.txt`, 647 lines): 4 events + 8 services + 1 request-that-already-exists = 12 new methods + 1 update to `storage_config_get`. The file is mostly the "outside-DRC" speaker/widget surface — parallel to the 4e-2 `drc_*` family.
- **PSDK-Interconnection**: 1 event + 1 service = 2 methods. Plain `value: text<256B` passthrough, no complex payload.
- **ESDK-Interconnection**: 1 event + 1 service = 2 methods. Mirror of PSDK-Interconnection.

The estimate over-projected because the RESUME-NOTES anticipated "payload state/event methods" beyond the transmit passthrough. In reality, payload state methods (`drc_psdk_state_info`, `drc_psdk_ui_resource`, `drc_speaker_play_progress`, `drc_psdk_floating_window_text`) landed under 4e-2's `drc/`. 4g's new surface is the **non-DRC** counterparts of those methods plus the two interconnection passthrough families.

### Filing decision for 4g (vs. 4e-2 `drc_*` siblings)

**`speaker_*` / `psdk_*` methods live in `events/` + `services/`; their `drc_speaker_*` / `drc_psdk_*` siblings live in `drc/` (4e-2).** The two sets are not aliases — same payload shape, different topic envelopes (`/services` vs `/drc/down`), different flow semantics. A cloud operates the speaker/widget outside an active DRC session via 4g methods and inside a session via 4e-2 `drc_*` methods. The 4g docs cross-cite their DRC siblings in a "Relationship to other methods" section.

The `custom_data_transmission_*` passthrough methods are not DRC-related and have no `drc_*` siblings.

### DJI-source inconsistencies flagged during 4g drafting

Carry into Phase 9 workflow authoring:

- **Pervasive `"timestamp:"` trailing-colon typo in Dock 3 service-reply examples.** Every service in `DJI_CloudAPI-Dock3-PSDK.txt` has it; Dock 2 + v1.11 are correct. Same pattern first seen in 4c and re-flagged in every sub-phase since.
- **`speaker_tts_play_start_progress` example `output.status: "success"` is not in the declared enum** (`{"in_progress", "ok"}`). Bug is present in **all three sources** (v1.11 + Dock 2 v1.15 + Dock 3 v1.15). Cloud implementations should accept `"success"` as equivalent to `"ok"`, or rely on `progress.percent == 100 && progress.step_key == "play"` as the authoritative completion signal. The sibling `speaker_audio_play_start_progress` example uses `"in_progress"` (valid) so the bug is only in the TTS progress event.
- **`upload` step-key wording diverges.** Dock 3 reads "Dock uploads audio to payload"; Dock 2 + v1.11 read "Dock uploads audio to psdk". Enum key is stable.
- **`speaker_audio_play_start` example URL has `.webm.pcm` double extension.** The URL is opaque to the dock logic; `file.format: "pcm"` is authoritative for the wire format.
- **`storage_config_get.module` gap closed.** Pre-4g doc documented `module = 0` only (from the 4d Media-Management source). PSDK sources (Dock 2 + Dock 3, v1.11 + v1.15) add `module = 1 = PSDK UI resources`. Doc now carries both values with source citations. Classification: source-coverage gap rather than a DJI-source inconsistency.

None of these rise to `OPEN-QUESTIONS.md` level — doc-level callouts are sufficient.

### After 4g review gate (= kick-off of 4h)

**4h scope — pilot-to-cloud (RC Plus 2 Enterprise + RC Pro Enterprise).** Sources to enumerate (confirm filenames with `ls DJI_Cloud/ | grep -iE "(pilot|rc)"`):

1. Per-feature pilot-to-cloud files under `DJI_Cloud/` — FlightTask, Live-Flight-Controls, LiveStream, HMS, FlySafe, DeviceManagement (there's likely a `DJI_CloudAPI-Pilot*-*.txt` set).
2. Cloud-API-Doc v1.11 pilot-to-cloud: `Cloud-API-Doc/docs/en/60.api-reference/30.pilot-to-cloud/` subtree.
3. `DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt` (already cited in [`mqtt/README.md`](mqtt/README.md) §2).

Expected method count: ~70 (to be revised after enumeration). Expected families: mostly the same seven thing-model families as dock-to-cloud (`status/`, `events/`, `services/`, `requests/`, `drc/`, plus the property families in 4i). RC-specific divergences to watch: RC Plus 2 Enterprise pairs with M4D (current gen); RC Pro Enterprise pairs with M3D/M3TD (older gen). Any cohort split will mirror the Dock 2 / Dock 3 pattern.

**Filing convention from 4e-2 carries over** — all `drc_*` methods in `drc/`, all `_progress` events in `events/`.

### Known gotchas carried forward

- Pilot-to-cloud uses the same MQTT envelope + topic list as dock-to-cloud (verified at Phase 2). The `{device_sn}` parameterization differs: `{gateway_sn}` becomes the RC's serial number, and the sub-device aircraft SN is the inner `device_sn`. Phase 2 [`mqtt/README.md`](mqtt/README.md) has the canonical taxonomy.
- The pilot-to-cloud tree (`mqtt/pilot-to-cloud/`) does **not** yet exist — 4h creates it. Path-level index (`mqtt/pilot-to-cloud/README.md`) must mirror the dock-to-cloud one.
- Property-family shells (`osd/`, `state/`, `property-set/`) are 4i scope — Phase 6 catalogs properties per device, and the MQTT property shells are thin pointers to it. Do not duplicate property content in 4h.
- Review gate: user checkpoint before 4h starts. Don't push through.

### Open questions potentially affecting 4h

- [`OQ-003`](OPEN-QUESTIONS.md) — QoS / retain / clean-session values still unspecified. Pilot-to-cloud DRC topics are highly latency-sensitive; cite the gap, don't invent.
- [`OQ-002`](OPEN-QUESTIONS.md) — pilot OSD copy-paste issue. May resurface in 4h if pilot OSD lives as a `state/` property shell vs an `osd/` topic. Flag at enumeration.

### Remaining Phase 4 work (4i only, after 4h)

After 4h the remaining MQTT work is:
- **4i** — property-family shells (`osd/`, `state/`, `property-set/`) that link to Phase 6 `device-properties/`. Thin pointer docs, not content-bearing.

---

## 2026-04-19 — handoff at Phase 4f close, ready for 4g

### State of play

- Phases 0, 1, 2, 3 complete and committed.
- Phase 4 (MQTT topic catalog) — **sub-phases 4a, 4b, 4c, 4d, 4e-1, 4e-2, and 4f all landed**. **181 methods total** across the dock-to-cloud MQTT catalog.
- **4g is next** — PSDK + PSDK-Interconnection + ESDK-Interconnection (dock-to-cloud). Est. ~40 methods (to be re-verified at enumeration).

### What 4f produced

- `mqtt/dock-to-cloud/events/` — 4 new docs: `flight_areas_drone_location` (`need_reply: 0`), `flight_areas_sync_progress` (`need_reply: 1`; 13-reason failure enum), `airsense_warning` (`need_reply: 1`; `data` is an **array**, not a struct — unusual for the corpus), `hms` (no reply; up to 20 warnings per batch).
- `mqtt/dock-to-cloud/services/` — 4 new docs: `unlock_license_switch`, `unlock_license_update` (`file` struct optional — present = offline push, absent = online resync), `unlock_license_list` (7 license types — area / circle / country / height / polygon / power / RID — with `consistence` flag), `flight_areas_update` (`data: null`).
- `mqtt/dock-to-cloud/requests/` — 1 new doc: `flight_areas_get` (dock pulls CFA file inventory + pre-signed URLs).
- No new family directory — all 9 methods fit into existing `events/` + `services/` + `requests/`.
- `mqtt/dock-to-cloud/README.md` — added FlySafe / CFA / AirSense / HMS rows across all three family tables, plus a new "Sub-phase 4f sub-areas" section with per-family grouping (FlySafe, Custom-Flight-Area, AirSense, HMS). Status table shows 4f landed.
- `mqtt/README.md` + corpus `README.md` updated to 181-method total.
- `TODO.md` — 4f section re-scoped (9 methods vs ~35 estimate) and checkboxes ticked; only the 4f review gate remains open.

### Why the method count (9) is much lower than the ~35 estimate

The 4e-2 handoff projected "~35 methods" covering all four feature areas. Actual counts by source:

- **FlySafe**: 3 methods — all services (switch/update/list). No events, no requests. The ~10–15 estimate implied per-license-type methods; in reality all 7 unlock types are unified under a single `unlock_license_list` reply.
- **Custom-Flight-Area**: 4 methods (2 events + 1 service + 1 request). As expected.
- **AirSense**: 1 event. No services, no requests.
- **HMS**: 1 event. DJI transports HMS warnings as a batched list of up to 20 entries; the code catalog itself is Phase 8 scope (`hms-codes/`), not Phase 4. There is no per-code MQTT method.

Net effect: 4f was the smallest drop since 4a (5 methods). Context budget is wide open for 4g.

### DJI-source inconsistencies flagged during 4f drafting

Carry into Phase 9 workflow authoring:

- **Pervasive 14-digit timestamps in 4f examples.** Every CFA + AirSense source example ships `"timestamp": 16540709686556` (14 digits) instead of 13-digit epoch-ms. Pattern repeats across v1.11 Dock 2, v1.15 Dock 2, and v1.15 Dock 3. Flagged inline in all affected docs; cloud implementations should emit/accept 13-digit ms.
- **Dock 3 HMS `"timestamp:"` trailing-colon typo.** Matches the Remote-Debugging / Remote-Control pattern from 4e-1/4e-2. Dock 2 HMS uses the correct key.
- **`unlock_license_list` `type` enum labels diverge cosmetically.** v1.11 + Dock 2 v1.15 use running-text lowercase ("Authorization zone unlocking"); Dock 3 v1.15 hand-authored source uses title-case past-tense ("Authorization Zone Unlocked"). Numeric `{0..6}` is stable. `rid_unlock.level` shows the same pattern.
- **`airsense_warning` label rename.** v1.11 + Dock 2 v1.15 use "Alarm level"; Dock 3 v1.15 uses "Warning level". Semantics identical.
- **HMS `module` enum label.** v1.11 + Dock 2 label `module: 3` as `"hms"` (lowercase); Dock 3 uses `"HMS"` (uppercase). Numeric stable.
- **`flight_areas_drone_location` Dock 3 v1.15 schema omits `area_id`** but the example carries it. Dock 2 schema has the row. Treat as source-extraction bug; field is authoritative on the wire.
- **`flight_areas_sync_progress.reason` in success example.** DJI's example sends `"reason": 0` alongside `"status": "synchronized"`; documented enum starts at `1`. Treat `0` as "no error" and rely on `status` for the authoritative outcome.
- **`airsense_warning` has `data` as an array.** Unusual for this corpus — every other event in the dock-to-cloud tree nests content under a struct. The array shape is intentional (multi-intruder reporting).

None of these rise to `OPEN-QUESTIONS.md` level — doc-level callouts are sufficient.

### After 4f review gate (= kick-off of 4g)

**4g scope — PSDK + PSDK-Interconnection + ESDK-Interconnection (dock-to-cloud).** Sources to enumerate (confirm filenames with `ls DJI_Cloud/ | grep -iE "(psdk|esdk)"`):

1. `DJI_Cloud/DJI_CloudAPI-Dock3-PSDK.txt`
2. `DJI_Cloud/DJI_CloudAPI-Dock3-PSDK-Interconnection.txt`
3. `DJI_Cloud/DJI_CloudAPI-Dock3-ESDK-Interconnection.txt`
4. Dock 2 counterparts.
5. Cloud-API-Doc v1.11 Dock 2: `.../10.dock2/140.psdk.md`, `150.psdk-transmit-custom-data.md`, `160.esdk-transmit-custom-data.md`.

Expected method count: ~40 (to be revised after enumeration). Expected families: mostly `services/` (command PSDK/ESDK payloads; request/reply transmission) + `events/` (payload state pushes) + `requests/` (file download / widget resource fetch). Note: a large swath of PSDK-widget / PSDK-speaker / PSDK-spotlight methods already landed under `drc/` in **4e-2** — 4g will not re-document those. Expected new content is the "transmit-custom-data" plumbing (cloud ↔ PSDK/ESDK passthrough) plus the payload state/event methods.

### Known gotchas carried forward

- PSDK-Interconnection and ESDK-Interconnection are DJI's passthrough channels for third-party payload vendors — the MQTT method typically wraps opaque bytes. Document the envelope, not the opaque content.
- `bid` grouping applies to PSDK command → progress-event flows that mirror the Remote-Debugging pattern in 4e-1.
- Review gate: user checkpoint before 4g starts. Don't push through.
- 4f introduced no new open questions.

### Remaining pilot-to-cloud work (4h + 4i)

After 4g the remaining MQTT work is:
- **4h** — pilot-to-cloud (RC Plus 2 Enterprise + RC Pro Enterprise), est. ~70 methods.
- **4i** — property-family shells (`osd/`, `state/`, `property-set/`) that link to Phase 6 `device-properties/`.

---

## 2026-04-19 — handoff at Phase 4e close (4e-2 landed), ready for 4f

### State of play

- Phases 0, 1, 2, 3 complete and committed.
- Phase 4 (MQTT topic catalog) — **sub-phases 4a, 4b, 4c, 4d, 4e-1, and 4e-2 all landed**. Phase 4e is complete. **172 methods total** across the dock-to-cloud MQTT catalog.
- **4f is next** — FlySafe + Custom-Flight-Area + AirSense + HMS (dock-to-cloud). Est. ~35 methods.

### What 4e-2 produced

- `mqtt/dock-to-cloud/drc/` — 53 new docs. All `drc_*` methods filed under `drc/` per the filing-convention decision (explained in [`mqtt/dock-to-cloud/README.md` §Filing convention](mqtt/dock-to-cloud/README.md#filing-convention-for-drc-methods)).
  - 9 events (mix of `/events`, `/drc/up` topics; two of them are cross-cohort topic-divergent — `drc_drone_state_push`, `drc_camera_osd_info_push`).
  - 10 shared DRC services (Dock 2 + Dock 3 both).
  - 6 Dock-2-only legacy services (several superseded on Dock 3 by non-DRC equivalents already in 4c).
  - 28 Dock-3-only DRC services — 5 camera/lens, 4 PSDK spotlight, 6 PSDK speaker, 2 PSDK widgets, 11 AI identify / AI spotlight-zoom.
- `drone_emergency_stop` was already covered in 4c under `drc/`; **not re-documented**, just cross-cited from [`drc_force_landing`](mqtt/dock-to-cloud/drc/drc_force_landing.md) and [`drc_emergency_landing`](mqtt/dock-to-cloud/drc/drc_emergency_landing.md).
- `mqtt/dock-to-cloud/README.md` heavily expanded — sub-phase status table shows 4e-2 landed, new sub-sections under `drc/` for Remote-Control events + Dock 2+3 shared services + Dock-2-only legacy + Dock-3-only (grouped by camera / light / speaker / widgets / AI), plus the filing-convention explainer.
- `mqtt/README.md` + corpus `README.md` updated to 172-method total.
- `TODO.md` 4e-2 checkboxes ticked; only the 4e review gate remains open.

### Filing-convention decision (worth keeping in mind for 4h)

**All `drc_*` methods live in `drc/`** regardless of topic (`/drc/down|up`, `/events`, or `/services` + `/services_reply`). Per-doc topics table is the canonical source for the actual wire topic. Rationale: DRC methods cluster naturally by name prefix; splitting by topic would scatter related methods across three folders and break the grep-by-method-name ergonomic.

Two known cross-cohort topic divergences, flagged prominently in the affected docs:
- [`drc_drone_state_push`](mqtt/dock-to-cloud/drc/drc_drone_state_push.md) — Dock 3 uses `/events`; Dock 2 + v1.11 use `/drc/up`.
- [`drc_camera_osd_info_push`](mqtt/dock-to-cloud/drc/drc_camera_osd_info_push.md) — same split.

One Dock-2-specific anomaly: [`drc_camera_mode_switch`](mqtt/dock-to-cloud/drc/drc_camera_mode_switch.md) replies on `/services_reply` instead of `/drc/up` despite the `drc_` method name. Flagged in the doc. Dock 3 deprecates the method entirely (replaced by [`camera_mode_switch`](mqtt/dock-to-cloud/services/camera_mode_switch.md) in 4c).

### DJI-source inconsistencies flagged during 4e-2 drafting

Carry into Phase 9 workflow authoring:

- **Dock 3 topic downgrade for `drc_drone_state_push` / `drc_camera_osd_info_push`.** Same method name, different topic family per cohort. DJI doesn't explain the change. A cloud supporting both must subscribe on both topics.
- **`drc_camera_night_mode_set` enum typo.** Dock 3 schema says `{"0":"Enabled","1":"Enabled","2":"Auto"}` — two keys both labeled "Enabled". `0` should clearly read "Disabled". Flagged inline; treat as source typo.
- **`drc_camera_shutter_set` Auto-value enum key diverges.** Dock 2 + v1.11 use `65534` = Auto; Dock 3 uses `60` = Auto. Cohort-dependent.
- **`drc_camera_aperture_value_set` enum label syntax diverges.** Dock 2 + v1.11 use dot-labels (`"F2.2"`); Dock 3 uses underscore-labels (`"F2_2"`). Integer keys stable.
- **`drc_camera_denoise_level_set` can't write the full `denoise_level` range** — the setter accepts `{2, 3}`, but [`drc_camera_state_push`](mqtt/dock-to-cloud/drc/drc_camera_state_push.md) reports `{0, 1, 2, 3}`. Operators can only select the two higher-noise levels; the device sets `0` / `1` autonomously.
- **Multiple wrong-method-name reply examples in Dock 3 source.** `drc_light_brightness_set`'s reply example shows `method: drc_night_lights_state_set`; `drc_initial_state_subscribe` Dock 2 v1.11 reply example shows `method: drone_emergency_stop`; `drc_camera_shutter_set` Dock 2 down example shows `method: drc_camera_aperture_value_set`. All inline-flagged as copy-paste errors in DJI source.
- **`drc_ai_spotlight_zoom_select` example uses literal arithmetic expressions** (`center_x: 0.0*10000`) that are not valid JSON. DJI intends the wire value to be the integer product. Flagged inline as instructional notation.
- **`drc_ai_spotlight_zoom_select` field labels copy-pasted from IR metering.** The `center_x` schema description reads "Coordinate x of the left and upper corner of the temperature measurement area" — copied from the IR metering service and incorrect for AI box-select. Flagged inline.
- **`drc_speaker_tts_set` constraint JSONs are malformed.** Keys have numbers embedded in them (`"min"0:""` etc.). Correct bounds inferred as `max=100, min=0`.
- **`drc_ai_info_push` `ai_wayline_state` sub-struct in example but not in schema.** Fields `sequence_shot`, `wait_control`, `record`, `normal_shot`, `count_down_time`, `alert_uuid` present in example only. Semantics undocumented.
- **`drc_ai_info_push` `state_reason` enum** mixes in-tracking reasons (0–15) with exit reasons (160–168) in the same enum without splitting into separate fields.
- **`drc_light_brightness_set` `brightness` field missing from schema**, present in example. Schema incomplete.
- **`drc_camera_mechanical_shutter_set` v1.11 schema column named `dewarping_state`** (copy-paste from the neighbouring dewarp service). Example field name `mechanical_shutter_state` is authoritative.

### After 4e review gate (= kick-off of 4f)

**4f scope — FlySafe + Custom-Flight-Area + AirSense + HMS (dock-to-cloud).** Sources to enumerate (confirm filenames with `ls DJI_Cloud/ | grep -iE "(flysafe|custom|airsense|hms)"`):

1. `DJI_Cloud/DJI_CloudAPI-Dock3-FlySafe.txt` (or similar)
2. `DJI_Cloud/DJI_CloudAPI-Dock3-Custom-Flight-Area.txt`
3. `DJI_Cloud/DJI_CloudAPI-Dock3-AirSense.txt`
4. `DJI_Cloud/DJI_CloudAPI-Dock3-HMS.txt`
5. Dock 2 counterparts.
6. Cloud-API-Doc v1.11 Dock 2: `.../10.dock2/170.flysafe.md`, `130.custom-flight-area.md`, `120.airsense.md`, `60.hms.md`.

Estimated method count ~35 (to be revised after enumeration). Expected families: mostly events (FlySafe rule push, Custom-Flight-Area sync, AirSense aircraft-spotted events, HMS fault codes) + a few requests (list sync) + a few services (push updated area set).

### Known gotchas carried forward

- HMS codes are enumerated in `DJI_Cloud/HMS.json` (a separate artifact scheduled for Phase 8 — `hms-codes/` catalog). Phase 4f will document the HMS **event / push method** (how fault codes are transported over MQTT), not the code catalog itself. Avoid duplicating.
- AirSense material may include ADS-B-aircraft enumerations — these are transport events, the aircraft-state codes themselves are Phase 8 scope.
- Phase 4 has been running as sub-drop-per-feature-area. 4f is smaller than 4e and will likely land as a single drop.
- Review gate: user checkpoint before 4f starts. Don't push through.

### Open questions potentially affecting 4f

- [`OQ-003`](OPEN-QUESTIONS.md) — QoS / retain / clean-session values still unspecified. FlySafe / Custom-Flight-Area may warrant higher QoS (consistency matters for geofence enforcement). Cite the gap, don't invent.

### Remaining pilot-to-cloud work (4h + 4i)

After 4g (PSDK / interconnection) the remaining MQTT work is:
- **4h** — pilot-to-cloud (RC Plus 2 Enterprise + RC Pro Enterprise), est. ~70 methods.
- **4i** — property-family shells (`osd/`, `state/`, `property-set/`) that link to Phase 6 `device-properties/`.

Phase 4h can reuse the filing-convention decision from 4e-2 (all `drc_*` in `drc/`; all `*_progress` events in `events/`; etc.).

---

## 2026-04-19 — handoff at Phase 4e-1 close, ready for 4e-2

### State of play

- Phases 0, 1, 2, 3 complete and committed.
- Phase 4 (MQTT topic catalog) is in progress. Sub-drops landed to date: **4a** (commit `8059992`, 5 methods), **4b** (commit `7742419`, 21 methods), **4c** (commit `663ae85`, 42 methods), **4d** (commit `debf5f8`, 9 methods), **4e-1** (this commit, 42 methods). **119 methods total** across Phase 4 so far.
- **4e was re-scoped into 4e-1 + 4e-2.** Enumeration found ~90 methods across the four source files (vs. the ~30 estimated in the 4d handoff); Remote-Control alone is 53. Splitting keeps per-drop size aligned with the 4c drop (42 methods).
- **4e-2 is next** — Remote-Control (dock-to-cloud), ~53 methods.

### What 4e-1 produced

- `mqtt/dock-to-cloud/events/` — 15 new docs:
  - Firmware-Upgrade: `ota_progress`.
  - Remote-Log: `fileupload_progress` (`need_reply: 0`).
  - Remote-Debugging (13): `esim_operator_switch`, `esim_activate`, `device_format`, `drone_format`, `charge_close`, `charge_open`, `cover_open`, `cover_close`, `device_reboot`, `cover_force_close`, `drone_close`, `drone_open`, `rtk_calibration` (Dock 3 only, `need_reply: 1` — first `need_reply: 1` event since 4d's `file_upload_callback`).
- `mqtt/dock-to-cloud/services/` — 27 new docs:
  - Firmware-Upgrade (1): `ota_create`.
  - Remote-Log (3): `fileupload_list`, `fileupload_start`, `fileupload_update`.
  - Remote-Debugging (23): `esim_operator_switch`, `sim_slot_switch`, `esim_activate`, `sdr_workmode_switch`, `charge_close`, `charge_open`, `cover_close`, `cover_open`, `drone_format`, `device_format`, `drone_close`, `drone_open`, `device_reboot`, `battery_store_mode_switch`, `alarm_state_switch`, `air_conditioner_mode_switch`, `battery_maintenance_switch`, `supplement_light_close`, `supplement_light_open`, `debug_mode_close`, `debug_mode_open`, `cover_force_close`, `rtk_calibration` (Dock 3 only).
- **New OQ entries:** [OQ-004](OPEN-QUESTIONS.md#oq-004--fileupload_list-log-window-timestamp-unit-is-inconsistent-across-dji-sources) — `fileupload_list` timestamp unit (s vs ms disagreement); [OQ-005](OPEN-QUESTIONS.md#oq-005--fileupload_start--fileupload_progress-correlation-key-is-undocumented) — `fileupload_start`→`fileupload_progress` correlation key (bid vs object_key vs fingerprint) undocumented by DJI.
- No new family directory — Firmware + Log + Debugging fit entirely into existing `events/` + `services/` structure.
- `mqtt/dock-to-cloud/README.md`, `mqtt/README.md`, corpus `README.md`, `TODO.md` all updated to 119-method total and 4e-1 landed. TODO re-scoped 4e into 4e-1 (landed) and 4e-2 (pending).

### Why the method count differs from the 4d estimate

The 4d handoff projected "~30 methods" for 4e covering all four feature areas. Actual counts by source:

- Firmware-Upgrade: 2 methods (1 event + 1 service). Matches expectations.
- Remote-Log: 4 methods (1 event + 3 services). Slightly lower than expected (estimate implied distinct "firmware list fetch" / "log file slot fetch" methods; in reality `fileupload_list` covers both).
- Remote-Debugging: 36 methods (13 events + 23 services). Much higher than expected — DJI treats every dock operation (charge, cover, power cycle, format, reboot, AC mode, battery mode, alarm, fill-light, SIM slot, eSIM activate, SDR mode) as its own service + progress-event pair, yielding a long list.
- Remote-Control: 53 methods — reason for the split. Remote-Control is not just DRC flight commands; it's the PSDK-payload API for speaker, spotlight, widgets, photo-format, plus the full AI-identify / AI-spotlight-zoom family. The 4d handoff underestimated this substantially.

### DJI-source inconsistencies flagged during 4e-1 drafting

Carry into Phase 9 workflow authoring:

- **Pervasive `"timestamp:"` typo (trailing colon in key) on Dock 3 Remote-Debugging examples.** Every event in `DJI_CloudAPI-Dock3-Remote-Debugging.txt` except `cover_force_close` and `rtk_calibration` has the typo. Dock 2 examples are correct. Same pattern first seen in 4c.
- **`ota_progress`: step field renamed `step_key` → `current_step` between v1.11 and v1.15.** Wire-level change; cloud must accept the correct name per firmware version.
- **`ota_create` Dock 3 adds `firmware_upgrade_type: 4 = psdk update`.** Dock 2 enum is `{2, 3}`; Dock 3 is `{2, 3, 4}`.
- **`fileupload_progress` Dock 3 schema typo `prgress` (missing "o").** Only in the table; example correctly uses `progress`. Dock 2 spells it correctly.
- **`fileupload_list` `end_ime` typo** (missing `t`) in the second list element of every source example. Pervasive across v1.11 + Dock 2 v1.15 + Dock 3 v1.15.
- **`fileupload_list` timestamp unit disagreement** — v1.11 and Dock 2 v1.15 say "Seconds / s"; Dock 3 v1.15 says "Milliseconds / ms". Example values are epoch-ms across all three sources. Logged as [OQ-004](OPEN-QUESTIONS.md#oq-004--fileupload_list-log-window-timestamp-unit-is-inconsistent-across-dji-sources).
- **`fileupload_start` `credentials.expire` unit/value mismatch.** Schema says "Seconds / s" (TTL); example is an epoch-ms timestamp.
- **`device_format` / `drone_format` Dock 3 example placeholder `step_key: "xxx"`.** Schema has no `step_key` field for these methods; example carries the literal `"xxx"` placeholder. Treat as copy-paste leftover.
- **`device_format` Dock 3 source typo — services-side labelled `Method: drone_format`** (duplicating the prior `drone_format` section) while the `services_reply` below correctly says `Method: device_format`. Dock 2 has the method name correct on both sides. Treat Dock 2 as authoritative.
- **`esim_operator_switch` enum description drift** — Dock 3 says `{"China Mobile", "China Unicom", "China Telecom"}`; Dock 2 says `{"Mobile", "China Unicom", "Telecommunications"}`. Wire values (`1 / 2 / 3`) are stable.
- **`sdr_workmode_switch` reply omits `output.status`** — every other Remote-Debugging service reply carries `output.status`, but this one doesn't (consistent across Dock 2 and Dock 3 — intentional variance).
- **Dock 2 has explicit `events_reply` sections for Remote-Debugging events; Dock 3 v1.15 omits them.** Dock 3 examples do not carry `need_reply: 1`, so the absence is consistent (no reply expected). Treat Dock 2 `events_reply` as the authoritative reply pattern when one is needed: `data.result: 0`.
- **`rtk_calibration` event description typo** — Dock 3 schema says `"ok":""` (empty description) while siblings have descriptions. Minor.
- **`rtk_calibration` event `type` enum** only defines `{1: Manual Calibration}` — automatic/scheduled calibration types may exist but are unspecified in DJI source.

### After 4e-1 review gate (= kick-off of 4e-2)

**4e-2 scope — Remote-Control (dock-to-cloud).** Source: `DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt` (4611 lines — the largest 4e source) + `DJI_CloudAPI-Dock2-Remote-Control.txt` + v1.11 Dock 2 `180.remote-control.md`. See [`TODO.md` 4e-2 section](TODO.md#sub-phase-4e-2--remote-control-dock-to-cloud) for the full 53-method inventory and filing-convention questions.

**Key decisions to make at 4e-2 kickoff**:
1. **Filing convention for cross-topic methods.** Several Dock 3 `drc_*` events land on `/events` (standard envelope) while the matching Dock 2 events land on `/drc/up` (lightweight envelope). Proposal: file in `drc/` with a topic-divergence note per doc. Alternative: split cohorts across folders — messier.
2. **Which docs get Phase 10 annex callouts.** Dock-2-only methods like `drc_video_storage_set` (replaced by `video_storage_set` in 4c) and `drc_interval_photo_set` (moved to OSD property in Dock 3) should cross-reference their Dock 3 replacements when known.

Template unchanged from 4a–4e-1. Same cohort pattern and source-provenance table.

### Known gotchas carried forward

- DRC envelope is lighter (no `tid`/`bid`/`timestamp`, just `method` + `seq` + `data`). 4e-2 will add many `drc/` entries — `seq` is the correlation key, not `bid`.
- `bid` grouping still applies for 4e-1's Firmware + Debugging flows — `ota_create` → `ota_progress` events share `bid`, and every debugging service → matching event carries the same `bid`.
- `need_reply: 1` on the `rtk_calibration` event is the only one in 4e-1; cloud ACKs with `{"result": 0}` on `events_reply`.
- Review gate: user checkpoint before 4e-2 starts. Don't push through.

### Open questions potentially affecting 4e-2

- [`OQ-003`](OPEN-QUESTIONS.md) — QoS / retain / clean-session values still unspecified. DRC topics in 4e-2 are the most latency-sensitive of the corpus; cite the gap, don't invent.
- Filing-convention question (§"After 4e-1 review gate") is a project decision, not an OQ. Flag in the commit message and let the user confirm at 4e-2 kickoff.

---

## 2026-04-18 — handoff at Phase 4d close, ready for 4e

### State of play

- Phases 0, 1, 2, 3 complete and committed.
- Phase 4 (MQTT topic catalog) is in progress. Sub-drops landed to date: **4a** (commit `8059992`, 5 methods), **4b** (commit `7742419`, 21 methods), **4c** (commit `663ae85`, 42 methods), **4d** (this commit, 9 methods). **77 methods total** across Phase 4 so far.
- **4e is next** — Firmware-Upgrade + Remote-Log + Remote-Debugging + Remote-Control (dock-to-cloud).

### What 4d produced

- `mqtt/dock-to-cloud/events/` — 2 new docs: `highest_priority_upload_flighttask_media`, `file_upload_callback` (both `need_reply: 1`).
- `mqtt/dock-to-cloud/services/` — 6 new docs: the five LiveStream services (`live_start_push`, `live_stop_push`, `live_set_quality`, `live_camera_change`, `live_lens_change`) plus the Media-Management command `upload_flighttask_media_prioritize`.
- `mqtt/dock-to-cloud/requests/` — 1 new doc: `storage_config_get` (OSS / S3 / MinIO temporary credentials for dock-initiated media upload).
- No new family directory — LiveStream + Media-Management fit entirely into the existing `events/` + `services/` + `requests/` structure.
- `mqtt/dock-to-cloud/README.md`, `mqtt/README.md`, and corpus `README.md` all updated to cite 77-method count + 4d landed.

### Why the method count (9) is lower than the ~20 estimate

The 4c handoff projected ~20 methods for LiveStream + Media-Management. The actual count is 9:

- **LiveStream source** has only five services (switch FPV camera, switch lens, set quality, start, stop). No events and no requests in the v1.15 LiveStream files. The earlier estimate appears to have assumed event/request families existed.
- **Media-Management source** has two events, one service, and one request — four methods total. No additional service family for stream-state notifications.
- The RTMP / GB28181 / WebRTC / Agora protocol-specific wire details (handshake, transport packet format, etc.) live in `livestream-protocols/` (Phase 7), not here — so there are no per-protocol methods in 4d.

Net effect: 4d was a comparatively small drop and left room in the context budget. 4e can therefore be a larger drop if the estimate holds (~30 methods for Firmware + Remote-Log + Remote-Debugging + Remote-Control).

### DJI-source inconsistencies flagged during 4d drafting

Carry into Phase 9 workflow authoring:

- **`live_start_push` Dock 3 example**: uses `url_type: 0` while the Dock 3 enum is `{1, 3, 4}` — DJI left the example un-edited when Agora was removed from Dock 3 support. Dock 2 still supports Agora (`url_type: 0`). Flagged in the doc.
- **`live_start_push` quality bitrates diverge across three sources**: v1.11 Dock 2 says Smooth = 512 Kbps, v1.15 Dock 2 says 1 Mbps, v1.15 Dock 3 says 512 Kbps. UHD on Dock 2 v1.15 says 8 Mbps but the sibling `live_set_quality` doc on Dock 3 says 8 Mbps while `live_start_push` on Dock 3 says 3 Mbps. Treat bitrate as run-time-negotiated, not authoritative.
- **`live_lens_change` v1.11 parameter regression**: v1.11 Dock 2 documents both `video_id` and `video_type`; v1.15 (Dock 2 and Dock 3) drops `video_id`. Unexplained by DJI — potentially implies "switch the lens of the currently active stream", but DJI does not say so explicitly.
- **`live_lens_change` reply**: every source declares `Data: null` but the example still carries `data.result`. Standard reply shape; example is authoritative.
- **`file_upload_callback` v1.11-only `flight_task` counters**: v1.11 Dock 2 documents `uploaded_file_count / expected_file_count / flight_type` as a sibling struct of `file`; v1.15 tables drop it. Plausibly still sent by older dock firmware.
- **`file_upload_callback` cloud_to_cloud_id**: v1.11 documents it in the data table; v1.15 tables don't list it but both Dock 2 + Dock 3 v1.15 examples carry it. Treat as present in v1.15 on the wire.
- **Timestamp-key typo**: Dock 3 Live-Flight-Controls examples used `"timestamp:"` (trailing colon); the Media-Management Dock 3 file does not — so the typo is not uniform across Dock 3 sources.
- **`storage_config_get` `provider` enum capitalization**: v1.11 says `"MinIO"` (camel-caps), v1.15 Dock 2 says `"minio"` (lowercase). Minor; lowercase is current.

None of these rise to `OPEN-QUESTIONS.md` level — doc-level callouts are sufficient for any reader.

### After 4d review gate (= kick-off of 4e)

**4e scope — Firmware-Upgrade + Remote-Log + Remote-Debugging + Remote-Control (dock-to-cloud).** Sources (confirm filenames with `ls DJI_Cloud/ | grep -iE "(firmware|log|debug|remote)"` in a fresh session):

1. `DJI_Cloud/DJI_CloudAPI-Dock3-Firmware-Upgrade.txt` (or similar)
2. `DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Log.txt`
3. `DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Debugging.txt`
4. `DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Control.txt`
5. Dock 2 counterparts.
6. Cloud-API-Doc v1.11 Dock 2: `.../10.dock2/80.firmware.md`, `.../10.dock2/90.log.md`, `.../10.dock2/180.remote-control.md` (the v1.11 Dock 2 set does not appear to include a Remote-Debugging file — verify during enumeration, and if absent note that 4e's Remote-Debugging section is v1.15-only).

Expected method count: ~30. Expected families: services (deliver firmware to device, start/stop remote control, begin/end debugging session, request log bundle), events (upgrade progress, log-upload progress, debugging events), requests (firmware list fetch, log file slot fetch).

Template is unchanged from 4a–4d. Same cohort pattern and source-provenance table.

### Known gotchas carried forward from 4b + 4c + 4d

- DRC envelope is lighter (no `tid`/`bid`/`timestamp`, just `method` + `seq` + `data`). Only the `drc/` family uses this. 4e is unlikely to add a new family directory.
- Multi-step flows (prepare → execute → progress) use `bid` grouping — watch for that pattern in firmware-upgrade staging.
- `file_upload_callback` uses `need_reply: 1` with the cloud returning `{"result": 0}` on `events_reply`. Other events that need reliability (likely firmware-upgrade progress reports, log-upload results) will use the same pattern.
- Review gate: user checkpoint before 4e starts. Don't push through.

### Open questions potentially affecting 4e

- [`OQ-003`](OPEN-QUESTIONS.md) — QoS / retain / clean-session values unspecified. Firmware upgrade is an obvious place where a higher QoS might be warranted; cite the gap if it becomes relevant, don't invent.

---

## 2026-04-18 — handoff at Phase 4c close, ready for 4d

### State of play

- Phases 0, 1, 2, 3 complete and committed.
- Phase 4 (MQTT topic catalog) is in progress. Sub-drops landed to date: **4a** (commit `8059992`, 5 methods), **4b** (commit `7742419`, 21 methods), **4c** (this commit, 42 methods).
- **4c landed single-drop** (not split into 4c-1 / 4c-2). All 42 Live-Flight-Controls methods are identical across v1.15 Dock 2 + Dock 3 sources and covered by v1.11 Dock 2 canonical (`110.drc.md`). Cohort field on every doc is `Dock 2 + Dock 3`.
- **4d is next** — LiveStream + Media-Management (dock-to-cloud).

### What 4c produced

- `mqtt/dock-to-cloud/events/` — 5 new docs: `fly_to_point_progress`, `takeoff_to_point_progress`, `drc_status_notify` (flagged abandoned in v1.15), `joystick_invalid_notify`, `camera_photo_take_progress`.
- `mqtt/dock-to-cloud/services/` — 30 new docs covering authority grab (2), DRC mode enter/exit (2), flight commands (4: `takeoff_to_point`, `fly_to_point`, `fly_to_point_stop`, `fly_to_point_update`), payload capture/recording/mode (6), gimbal + aim + look + screen (6), storage + exposure + focus (7), IR metering (3).
- `mqtt/dock-to-cloud/drc/` — **new directory** with 7 docs on the `drc/up` + `drc/down` channel: `stick_control`, `drone_control` (flagged abandoned), `drone_emergency_stop`, `heart_beat`, `hsi_info_push`, `delay_info_push`, `osd_info_push`.
- `mqtt/dock-to-cloud/README.md` updated — status table marks 4c landed, new rows added in events/services tables, new `drc/` section added.
- `mqtt/README.md` updated — blurb now says "Phase 4a + 4b + 4c landed (68 methods total)".
- `README.md` (corpus TOC) updated — same.

### DJI-source inconsistencies flagged during 4c drafting

Worth knowing when you audit these docs, and worth carrying into Phase 9 workflow write-ups:

- `stick_control` — DJI's v1.15 example includes a `gimbal_pitch` key that is not in the schema table. Flagged in the doc; don't treat it as authoritative.
- `drone_control.h` — DJI documents the bounds as `{"min":5,"max":-4}`. Reversed numbers (typo); real semantic is ±m/s vertical velocity. Flagged in the doc.
- `drone_control` — DJI's own description marks it abandoned in favor of `stick_control`. `drc_status_notify` also marked abandoned in v1.15 (pointer to `drc_state` device property or `heart_beat`).
- `hsi_info_push` — DJI's example uses `around_distance` (singular) while the schema says `around_distances` (plural), and includes eight additional enable/work pairs (`left_*`, `right_*`, `front_*`, `back_*`, `vertical_*`, `horizontal_*`) not in the table. Flagged in the doc.
- `heart_beat` — DJI example has two `method` keys in the same JSON (one would overwrite the other on parse). Noted as a source error.
- `osd_info_push.height` — DJI lists the unit as "degree"; it's an altitude in meters. Noted.
- `camera_exposure_set.exposure_value` — declared `enum_string` in the table but sent as integer in the example. Treated as integer per the example.
- `camera_photo_take_progress.progress.current_step` — documented enum is `3000 / 3002 / 3005`; example shows `0` (not a valid enum value). Noted.
- `device_exit_homing_notify.reason` — Phase 4b precedent: `enum_int` declared, string `"0"` in example. (Same class of DJI typo.)

None of these rise to `OPEN-QUESTIONS.md` level — they're source-level inconsistencies that the per-doc "Source inconsistencies flagged by DJI's own example" callouts surface for any reader. Keep the pattern for 4d.

### After 4c review gate (= kick-off of 4d)

**4d scope — LiveStream + Media-Management (dock-to-cloud).** Sources:

1. `DJI_Cloud/DJI_CloudAPI-Dock3-LiveStream.txt` (or similar — confirm exact filename with `ls DJI_Cloud/ | grep -i live`)
2. `DJI_Cloud/DJI_CloudAPI-Dock3-Media-Management.txt` (likewise confirm filename)
3. Dock 2 counterparts
4. Cloud-API-Doc v1.11 Dock 2: `Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/30.live.md` + `40.file.md`

Expected method count: ~20. Expected families: mostly `services/` (livestream start/stop, quality set, media list request) + `events/` (media upload status, livestream state changes) + possibly `requests/` (media pull).

Template is unchanged from 4a–4c. Use the same cohort pattern and source-provenance table.

### Known gotchas carried forward from 4b + 4c

- DRC envelope is lighter (no `tid`/`bid`/`timestamp`, just `method` + `seq` + `data`). 4c added `drc/` as a family; 4d won't need new family dirs unless LiveStream/Media exposes one.
- `in_flight_wayline_*` docs in `services/` show that `bid` groups related transactions across a multi-step flow. Same pattern will apply to livestream start → quality set → stop.
- Review gate: user checkpoint before 4d starts. Don't push through.

---

## 2026-04-18 — handoff at Phase 4b close, ready for 4c

### State of play

- Phases 0, 1, 2, 3 complete and committed.
- Phase 4 (MQTT topic catalog) is in progress, being landed in sub-drops 4a–4i. See [`TODO.md`](TODO.md) for the full sub-phase scaffolding.
- **4a landed** (commit `8059992`) — 5 methods for DeviceManagement + Organization + Configuration.
- **4b landed** (commit is this handoff's commit — check `git log --oneline -3` in the fresh session) — 21 methods for WaylineManagement.
- **4c is next** — Live-Flight-Controls (DRC / camera / gimbal / IR).

### How to resume

1. Read [`CLAUDE.md`](../CLAUDE.md) (repo root) + [`README.md`](README.md) + [`PLAN.md`](PLAN.md) + [`TODO.md`](TODO.md) + [`_memory/MEMORY.md`](_memory/MEMORY.md) per the standard session-start checklist.
2. Read this file (you're doing it now).
3. Read [`mqtt/dock-to-cloud/README.md`](mqtt/dock-to-cloud/README.md) — the path-level index. It shows what's landed and what's next.
4. Pick two exemplar docs to match the template:
   - Short/simple: [`mqtt/dock-to-cloud/services/return_home_cancel.md`](mqtt/dock-to-cloud/services/return_home_cancel.md)
   - Complex schema: [`mqtt/dock-to-cloud/services/flighttask_prepare.md`](mqtt/dock-to-cloud/services/flighttask_prepare.md)
   - Event with reply + need_reply quirk: [`mqtt/dock-to-cloud/events/device_exit_homing_notify.md`](mqtt/dock-to-cloud/events/device_exit_homing_notify.md)
   - Event with big enum (avoid duplication pattern): [`mqtt/dock-to-cloud/events/flighttask_progress.md`](mqtt/dock-to-cloud/events/flighttask_progress.md)
5. Start drafting 4c per the plan below.

### 4c scope — Live-Flight-Controls (dock-to-cloud)

**Sources to read (in order):**

1. `DJI_Cloud/DJI_CloudAPI-Dock3-Live-Flight-Controls.txt` — 4277 lines, authoritative for Dock 3. Much larger than 4b sources; method examples are bigger.
2. `DJI_Cloud/DJI_CloudAPI-Dock2-Live-Flight-Controls.txt` — 2189 lines. Compare for Dock-2-only vs Dock-3-only divergence.
3. `Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/110.drc.md` — v1.11 Dock 2 canonical for DRC methods.

Plus cross-reference:
- `Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/70.cmd.md` — may contain overlapping Dock 2 command methods (verify during enumeration).

**Method inventory (from grep prep-work in the prior session, may need re-verification):**

Dock 3 Live-Flight-Controls has 42 unique method names spread across the events / services / drc families:

- **events/** — aircraft telemetry and progress events:
  `fly_to_point_progress`, `takeoff_to_point_progress`, `drc_status_notify`, `joystick_invalid_notify`, `camera_photo_take_progress` (5 events)
- **services/** — cloud commands with replies (authority grab, DRC mode, flight commands, camera/gimbal commands):
  `flight_authority_grab`, `payload_authority_grab`, `drc_mode_enter`, `drc_mode_exit`, `takeoff_to_point`, `fly_to_point`, `fly_to_point_stop`, `fly_to_point_update`, `camera_frame_zoom`, `camera_mode_switch`, `camera_photo_take`, `camera_photo_stop`, `camera_recording_start`, `camera_recording_stop`, `camera_screen_drag`, `camera_aim`, `camera_focal_length_set`, `gimbal_reset`, `camera_look_at`, `camera_screen_split`, `photo_storage_set`, `video_storage_set`, `camera_exposure_mode_set`, `camera_exposure_set`, `camera_focus_mode_set`, `camera_focus_value_set`, `camera_point_focus_action`, `ir_metering_mode_set`, `ir_metering_point_set`, `ir_metering_area_set` (~30 services)
- **drc/** — real-time control channel (`thing/product/{gateway_sn}/drc/up` + `/drc/down`, lighter envelope):
  `stick_control`, `drone_control`, `drone_emergency_stop`, `heart_beat`, `hsi_info_push`, `delay_info_push`, `osd_info_push` (7 drc-family methods)

**Total: 42 methods.** Approximately 80–100 lines per doc × 42 = 3500–4200 lines of output. That's at the edge of a single-drop budget — consider splitting 4c itself if context pressure is high. A reasonable split: `4c-1` = authority + DRC mode + flight commands + events (~15 methods); `4c-2` = camera/gimbal/IR control + DRC-family (~27 methods).

### Doc template (preserve this pattern)

Every method doc has:
1. H1 title: `` # `method_name` — short purpose ``
2. Intro paragraph — one or two sentences on what the method does.
3. `Part of the Phase 4 MQTT catalog. Shared conventions live in [../../README.md](../../README.md).` boilerplate.
4. **Cohort** line stating `Dock 2 + Dock 3` / `Dock 3 only` / `v1.15 addition`.
5. `## Topics` table — Direction / Topic / Method.
6. `## Up — data fields` or `## Down — data fields` table (whichever is the initiator side).
7. `### Example` fenced JSON (verbatim from DJI source, trimmed long examples with a note).
8. Reply-side `## Up (reply)` or `## Down (reply)` fields + example.
9. `## Source provenance` table citing v1.11 Cloud-API-Doc + v1.15 Dock 2 + v1.15 Dock 3.

For big enums (like `flighttask_progress.break_reason` with ~100 values): don't restate them; cite the source file and note "Full reference in Phase 8 (`error-codes/`) when that catalog lands."

For methods with no v1.11 counterpart (v1.15 additions): note "no v1.11 counterpart" in the Cohort line and omit the v1.11 provenance row.

### File naming

Verbatim DJI `method` string as filename (underscores preserved): e.g. `drone_emergency_stop.md`, not `drone-emergency-stop.md`. This is for grep-ability — searching for a method name hits the filename directly.

### After drafting 4c methods

1. Update [`mqtt/dock-to-cloud/README.md`](mqtt/dock-to-cloud/README.md):
   - Mark 4c as landed in the sub-phase status table.
   - Add `events/`, `services/`, `drc/` sections to the catalog (creating `drc/` dir if first time).
2. Update [`mqtt/README.md`](mqtt/README.md) to include 4c in the landed-count blurb.
3. Update [`README.md`](README.md) (corpus TOC) mqtt entry.
4. Update [`TODO.md`](TODO.md) — tick 4c checkboxes, close review gate line, advance **Current phase** pointer to 4d.
5. Append to this RESUME-NOTES.md with a new handoff entry at the top, summarizing what landed and what 4d scope is.
6. Commit with the same message style as prior Phase 4 commits (see `git log --oneline | grep Phase` for examples).

### Known gotchas / things I noticed during 4a/4b

- DRC topic envelope is lighter than other thing-model topics — no `tid`/`bid`/`timestamp`, just `method` + `seq` + `data`. See Phase 2 [`mqtt/README.md` §5.8](mqtt/README.md#58-drcup--drcdown--direct-remote-control) for the canonical envelope.
- Some DJI v1.15 examples omit the outer envelope wrapper and show just the `data` body; in the doc, note this and state the envelope still wraps it on the wire.
- Some DJI tables document types that contradict examples (e.g. `reason` shown as string in an `enum_int` column). When spotted, add a short note flagging the inconsistency; treat the declared type as authoritative.
- File names use underscores verbatim (match DJI method strings); heading format `` # `method_name` — purpose `` is standard.
- Never write without reading source — "real payloads only" directive in CLAUDE.md.
- Phase review gate is a user checkpoint — don't push through 4c into 4d automatically; stop and summarize.

### Open questions that may touch 4c

- [`OQ-003`](OPEN-QUESTIONS.md) — QoS / retain values unspecified. Phase 4 drafting does NOT fabricate QoS. DRC's `/drc/up` and `/drc/down` may have implementation-dependent QoS choices; cite the gap, don't invent.

---

(No older entries yet — this is the first RESUME-NOTES checkpoint.)
