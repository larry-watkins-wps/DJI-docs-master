# Resume Notes

Mid-phase context that must survive a session break. If you're starting a fresh session and the user's first instruction is **"Continue at 4c"** (or similar), read this file first — it hands you everything you need to pick up without re-reading the whole corpus.

Latest entry is at the top. Older entries kept below for audit traceability.

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
