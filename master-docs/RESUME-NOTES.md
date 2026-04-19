# Resume Notes

Mid-phase context that must survive a session break. If you're starting a fresh session and the user's first instruction is **"Continue at 4c"** (or similar), read this file first — it hands you everything you need to pick up without re-reading the whole corpus.

Latest entry is at the top. Older entries kept below for audit traceability.

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
