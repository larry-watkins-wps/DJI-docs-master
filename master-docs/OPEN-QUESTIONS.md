# Open Questions

Standing gaps, ambiguities, and source conflicts encountered while building the corpus. Every entry must state the question, why it matters, what source(s) were consulted, and its current status (`open`, `deferred`, `resolved`).

Resolution notes stay in the entry after it is closed — do not delete resolved entries, so audits can trace how a decision was reached.

---

## OQ-001 — Source version mismatch between `Cloud-API-Doc/` (v1.11.3) and `DJI_Cloud/` (v1.15)

**Status**: open — policy captured in `SOURCES.md`; individual content choices resolved inline as encountered.

**Raised**: 2026-04-18, during Phase 1 source survey.

**Question.** The two primary DJI sources in this repo ship different versions of the Cloud API documentation:

- `Cloud-API-Doc/docs/en/00.index.md` release-notes header: **Cloud API v1.11.3** (and older).
- `DJI_Cloud/DJI_CloudAPI-Dock3-*.txt` and `DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt` navigation header: **Cloud API v1.15**.

The v1.11 markdown set has zero matches for `Dock 3`, `Dock3`, `Matrice 4`, `M4D`, or `M4TD` across `docs/en/` and `docs/cn/`. The v1.15 MHTML extracts cover those devices explicitly. For the in-scope devices (Dock 3, M4D, M4TD, RC paired with M4D), the v1.15 extracts are the only written DJI source in this repo.

**Why it matters.** The authority ranking in `SOURCES.md` originally listed `Cloud-API-Doc/` as authoritative #1 and `DJI_Cloud/` as derived #3. That ranking is correct for the v1.11 feature surface but inverted for anything that only exists in v1.15 (which is the entire in-scope device set).

**Resolution policy** (see `SOURCES.md`):

1. For content present in both sets, `Cloud-API-Doc/` wins on formatting fidelity (the v1.15 extract is plain text and may have lost tables, code blocks, or inline structure).
2. For content specific to Dock 3 / M4D / M4TD / RC-Plus-2-Enterprise-with-M4D, the v1.15 extracts in `DJI_Cloud/*.txt` are the primary written source. Where the extract appears to have dropped structure, the live site at `developer.dji.com` (v1.15+) is the fallback cross-check via browser automation or Playwright (see `DJI_Cloud/scrape_api_reference.py`).
3. When a statement is drawn from the v1.15 extract and has no counterpart in `Cloud-API-Doc/`, cite the `DJI_Cloud/*.txt` file explicitly. When the two sets agree on generic architecture, citing `Cloud-API-Doc/` is sufficient.
4. If a conflict is found between v1.11 and v1.15 (not just silence), log it as a new `OQ-###` entry and ask.

**Remaining open thread.** As of 2026-04-18 the `DJI_Cloud/` extraction covers the entire `/api-reference/` section of the live site (87 files after the Dock 2 cohort scope expansion — see `SOURCES.md` §3). Pages outside `/api-reference/` — overview, product-support, release-notes, tutorials, quick-start, feature-set, debug — are **not** in the extraction set. If a later phase needs one of those, fetch from the live site (or extend `scrape_api_reference.py`'s URL inventory). No action required now.

---

## OQ-002 — Pilot-to-Cloud OSD struct example appears to be a copy-paste of the Dock OSD example

**Status**: open — DJI-side documentation bug; affects how we can cite the pilot-to-cloud topic definition for OSD content.

**Raised**: 2026-04-18, during Phase 2 design work (direct comparison of the two topic-definition files).

**Question.** `DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt` has an OSD struct example that is byte-identical (after whitespace normalization) to the OSD struct example in `DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt` (the dock-to-cloud page). Both show a payload with `"gateway": "dock_sn"`, a `sub_device` block, `drone_in_dock`, `cover_state`, `emergency_stop_state`, dock environmental sensors, `alternate_land_point`, etc. — that is **Dock OSD content**, not Pilot OSD content. DJI appears to have copy-pasted the example between the two topic-definition pages.

**Why it matters.** Phase 4 `mqtt/pilot-to-cloud/osd.md` cannot cite the pilot-to-cloud topic definition file for the canonical Pilot-path OSD payload — the example there does not represent what a Pilot-attached aircraft actually publishes. If we cited it uncritically we'd mislead anyone auditing or implementing the Pilot path.

**Where to get the real Pilot OSD payload.** The per-aircraft property catalogs — e.g. `DJI_Cloud/DJI_CloudAPI_Matrice4-Enterprise-Properties.txt`, `DJI_CloudAPI_Mavic3-Enterprise_Properties.txt`, `DJI_CloudAPI_M3D_M3DT_Properties.txt` — list the actual property set a Pilot-attached aircraft reports. These are primary for OSD content. The pilot-to-cloud topic definition file can only be cited for the envelope shape (tid / bid / timestamp / gateway / data), not for the OSD payload content.

**How to handle**:
1. Phase 2 `mqtt/README.md` — cite the pilot-to-cloud topic definition file only for the envelope and the topic list. Add a footnote flagging the OSD copy-paste bug.
2. Phase 4 `mqtt/pilot-to-cloud/osd.md` — use per-aircraft property catalogs as the canonical content source. Cite this `OQ-002` entry for traceability.
3. Re-verify against the live site periodically — if DJI fixes the copy-paste, re-scrape the topic definition file and close this entry with a resolved note.

---

## OQ-003 — MQTT QoS, retain, and clean-session settings are not specified in DJI's published documentation

**Status**: open — gap to close before Phase 4 per-topic catalog entries claim specific QoS values.

**Raised**: 2026-04-18, during Phase 2 MQTT-conventions drafting.

**Question.** The canonical MQTT concept page (`[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/20.mqtt.md]`) describes the three MQTT 5.0 QoS levels generically (0, 1, 2) but does not state which QoS DJI uses per topic family. The topic-definition files (`[DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt]`, `[DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt]`) also do not pin QoS or the `retain` flag for any topic. No per-feature page in `DJI_Cloud/*.txt` surveyed during Phase 2 design mentions QoS either.

**Why it matters.** A cloud implementation must choose QoS values for the subscriptions it establishes and for the messages it publishes. Wrong choices have real consequences:
- QoS 0 on a services/services_reply pair allows dropped commands silently.
- QoS 2 on the high-frequency `osd` topic is excessive and drives broker CPU up.
- `retain=true` on `status` preserves last-known topology across broker restarts — DJI's behavior on this flag affects cold-start correctness for third-party implementations.

**Where the evidence likely lives.**
1. `[DJI-Cloud-API-Demo/]` (deprecated, v1.10) — the Java/Spring client code explicitly passes QoS to the MQTT library when subscribing and publishing. Scanning `cloud-sdk/` and `sample/` for `MqttQoS`, `.qos(`, `setQos(`, `setRetained(` will expose DJI's own defaults.
2. Live packet capture against a real Dock or RC — out of scope for the corpus phase.

**Proposed resolution.**
- Phase 4 per-topic catalog entries must not cite QoS or `retain` values unless they can cite a specific source. When captured from the demo, cite as e.g. `[DJI-Cloud-API-Demo/cloud-sdk/.../FooHandler.java:42]`.
- If no demo evidence supports a topic's QoS, the Phase 4 entry states "not specified by DJI" and links back to this OQ.
- Do not attempt to reverse-engineer values; either cite or omit.

**Remaining open thread.** When Phase 4 starts, scan `DJI-Cloud-API-Demo/` for `MqttQoS` / `.qos(` / `setQos(` / `setRetained(` and compile a table of observed QoS per topic. Update this entry with findings and close if the coverage is complete for the in-scope topics.

---

## OQ-004 — `fileupload_list` log-window timestamp unit is inconsistent across DJI sources

**Status**: open — a cloud implementer handling Remote-Log has to pick a unit to interpret `start_time` / `end_time`, and the three DJI sources disagree.

**Raised**: 2026-04-19, during Phase 4e drafting of [`mqtt/dock-to-cloud/services/fileupload_list.md`](mqtt/dock-to-cloud/services/fileupload_list.md).

**Question.** The `files[].list[].start_time` and `files[].list[].end_time` integer fields returned by `fileupload_list`'s reply carry different unit labels in each DJI source:

- `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/90.log.md]` (v1.11 Dock 2) — `{"unit_name":"Seconds / s"}`.
- `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Log.txt]` (v1.15 Dock 2) — `{"unit_name":"Seconds / s"}`.
- `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Log.txt]` (v1.15 Dock 3) — `{"unit_name":"Milliseconds / ms"}`.

Examples in every source use values in the range `1654070968655` and `1659427398806`, which are epoch-milliseconds. If the fields were seconds, the same payload would reference dates in the year ~54400. The example values therefore contradict every v1.11/Dock-2 label *and* confirm the Dock-3 label.

**Why it matters.** A cloud implementation building a "list logs and let the operator choose a time window" UI must decide which unit to display. Picking seconds per v1.11 misreads every timestamp as a wall-clock date thousands of years in the future. Picking ms per Dock 3 matches the examples but contradicts two of three sources' declared labels.

**Proposed resolution.**
- Treat the fields as **epoch-milliseconds** in the `fileupload_list` doc — backed by the actual example values in all three sources.
- Flag the v1.11 / Dock 2 "seconds" label as a DJI source-table error.
- Revisit if DJI publishes corrected labels or a live firmware differs.

**Remaining open thread.** Verify against a real Dock 2 deployment if one becomes available (or the v1.10 Java demo's `FileuploadListResponse` handling) before closing.

---

## OQ-005 — `fileupload_start` → `fileupload_progress` correlation key is undocumented

**Status**: open — affects how a cloud matches per-file progress events back to the upload batch that triggered them.

**Raised**: 2026-04-19, during Phase 4e drafting of [`mqtt/dock-to-cloud/services/fileupload_start.md`](mqtt/dock-to-cloud/services/fileupload_start.md) and [`mqtt/dock-to-cloud/events/fileupload_progress.md`](mqtt/dock-to-cloud/events/fileupload_progress.md).

**Question.** For other multi-step flows in the corpus — `ota_create` → `ota_progress`, `flighttask_execute` → `flighttask_progress`, `charge_open` service → `charge_open` event, etc. — the cloud correlates the progress stream back to the originating command via the shared `bid` (the cloud picks a `bid` on the command and the device reuses it on each progress event). DJI states this convention for those flows either explicitly in prose or implicitly via example `bid` reuse.

For the log-upload flow, DJI never says whether `fileupload_progress` events echo the `bid` of the originating `fileupload_start` command. All three sources use `"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx"` placeholders in both messages, so the examples don't disambiguate. The `fileupload_progress` payload does carry per-file identifiers (`key`, `fingerprint`, `device_sn`, `module`) that would let the cloud match by file identity independent of `bid`.

**Why it matters.** A server implementation needs to decide:
- Subscribe to `fileupload_progress` and correlate events back to the triggering `fileupload_start` by `bid`, or
- Subscribe and correlate by `object_key` / `fingerprint`.

Picking the wrong approach silently misattributes progress in scenarios where multiple uploads are in flight concurrently (possible for multi-module batches, or after operator-retriggered uploads).

**Proposed resolution.**
- Phase 4e `fileupload_start.md` and `fileupload_progress.md` note the ambiguity: a cloud should expect to correlate by `object_key` / `fingerprint` (available in both `fileupload_start.params.files[].object_key` and `fileupload_progress.output.ext.files[].key`), and treat `bid` reuse as unconfirmed.
- Flag this for Phase 9 workflow `media-upload-from-dock.md` (or a dedicated `log-upload-from-dock.md`).
- Verify against `DJI-Cloud-API-Demo/` log-upload handler if one is present when Phase 9 arrives.
