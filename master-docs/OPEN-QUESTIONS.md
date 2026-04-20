# Open Questions

Standing gaps, ambiguities, and source conflicts encountered while building the corpus. Every entry must state the question, why it matters, what source(s) were consulted, and its current status (`open`, `deferred`, `resolved`).

Resolution notes stay in the entry after it is closed — do not delete resolved entries, so audits can trace how a decision was reached.

---

## OQ-001 — Source version mismatch between `Cloud-API-Doc/` (v1.11.3) and `DJI_Cloud/` (v1.15)

**Status**: **resolved 2026-04-19** — corpus is v1.15-only. v1.11 `Cloud-API-Doc/` material is retained in-repo solely for drift cross-check; it is no longer primary for any content, even where it agrees with v1.15.

**Raised**: 2026-04-18, during Phase 1 source survey.

**Question.** The two primary DJI sources in this repo ship different versions of the Cloud API documentation:

- `Cloud-API-Doc/docs/en/00.index.md` release-notes header: **Cloud API v1.11.3** (and older).
- `DJI_Cloud/DJI_CloudAPI-Dock3-*.txt` and `DJI_CloudAPI-DockToCloud_Matrice_4D_4DT-DeviceProperties.txt` navigation header: **Cloud API v1.15**.

The v1.11 markdown set has zero matches for `Dock 3`, `Dock3`, `Matrice 4`, `M4D`, or `M4TD` across `docs/en/` and `docs/cn/`. The v1.15 MHTML extracts cover those devices explicitly. For the in-scope devices (Dock 3, M4D, M4TD, RC paired with M4D), the v1.15 extracts are the only written DJI source in this repo.

**Why it matters.** The authority ranking in `SOURCES.md` originally listed `Cloud-API-Doc/` as authoritative #1 and `DJI_Cloud/` as derived #3. That ranking is correct for the v1.11 feature surface but inverted for anything that only exists in v1.15 (which is the entire in-scope device set).

**Resolution (2026-04-19)** — user directed: **the corpus documents v1.15 only**. `DJI_Cloud/` v1.15 extracts are the sole primary source. `Cloud-API-Doc/` v1.11 is retained only as a drift-cross-check corpus — useful to note what changed between versions, but never primary for any claim in the corpus. Simplified policy:

1. **All primary content cites `DJI_Cloud/`** (v1.15 extracts). When a v1.15 extract appears to have dropped table structure or inline formatting, verify against the live site at `developer.dji.com` and cite both — not against `Cloud-API-Doc/`.
2. **`Cloud-API-Doc/` is for drift tables only.** Per-device docs already follow this pattern (dock2.md §5, m3d.md §5, rc-pro.md §5) — v1.11 values appear in "v1.11 → v1.15 drift" columns, and v1.15 always wins on every conflict.
3. **No action on existing corpus.** Phases 0–6 already cite v1.15 as authoritative in practice; this resolution just formalizes the policy. Phase 7+ proceeds on the same basis.

Drift between v1.11 and v1.15 that is **not** captured in an existing drift table is treated as uninteresting (v1.15 wins without commentary). Drift that flips semantics (enum values removed/renamed, types changed) is still logged as a fresh OQ and flagged for user decision — but since all such drift encountered through 6c has been additive or cosmetic, there are no live cases.

`SOURCES.md` authority ranking updated 2026-04-19 to reflect this policy.

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

**Status**: **resolved 2026-04-19** — demo-code scan complete. DJI's own reference implementation uses QoS 1 for all cloud-side subscriptions, QoS 0 for the default outbound, QoS 2 specifically for `services_reply`, and never sets the `retain` flag. See findings below. Corpus policy locked: DJI documentation is silent on the wire, the demo provides the only DJI-authored evidence, and per-topic catalog entries cite the demo where applicable.

**Raised**: 2026-04-18, during Phase 2 MQTT-conventions drafting.

**Question.** The canonical MQTT concept page (`[Cloud-API-Doc/docs/en/10.overview/40.basic-concept/20.mqtt.md]`) describes the three MQTT 5.0 QoS levels generically (0, 1, 2) but does not state which QoS DJI uses per topic family. The topic-definition files (`[DJI_Cloud/DJI_CloudAPI-TopicDefinitions.txt]`, `[DJI_Cloud/DJI_CloudAPI-PilotToCloud-Topic-Definition.txt]`) also do not pin QoS or the `retain` flag for any topic. No per-feature page in `DJI_Cloud/*.txt` surveyed during Phase 2 design mentions QoS either.

**Why it matters.** A cloud implementation must choose QoS values for the subscriptions it establishes and for the messages it publishes. Wrong choices have real consequences:
- QoS 0 on a services/services_reply pair allows dropped commands silently.
- QoS 2 on the high-frequency `osd` topic is excessive and drives broker CPU up.
- `retain=true` on `status` preserves last-known topology across broker restarts — DJI's behavior on this flag affects cold-start correctness for third-party implementations.

**Demo-code scan findings (2026-04-19).** Scanned `[DJI-Cloud-API-Demo/cloud-sdk/]` for `MqttQoS`, `setQos`, `.qos(`, `setRetained`, and `retain`/`qos` in `.java` files. Complete evidence inventory:

| Setting | Value | Source | Notes |
|---|---|---|---|
| Inbound channel adapter QoS (all subscribed topics by default) | **1** | `[DJI-Cloud-API-Demo/cloud-sdk/src/main/java/com/dji/sdk/mqtt/MqttConfiguration.java:54]` → `adapter.setQos(1)` | The cloud subscribes to every inbound topic at QoS 1. This is `MqttPahoMessageDrivenChannelAdapter`'s default subscription QoS for topics added via the inbound `inboundTopic` config or via `IMqttTopicService.subscribe(String...)`. |
| Dynamic subscription QoS (multi-topic overload) | **1** | `[MqttTopicServiceImpl.java:34]` → `subscribe(topic, 1)` | When code calls `subscribe(String... topics)` with no explicit QoS, each topic is added at QoS 1. A QoS-specifying overload `subscribe(String topic, int qos)` exists at `:39` but no caller in the demo passes a value other than 1. |
| Outbound default QoS | **0** | `[MqttConfiguration.java:73]` → `messageHandler.setDefaultQos(0)` + `[MqttGatewayPublish.java:31]` → `DEFAULT_QOS = 0` | Every outbound publish that does not explicitly pass a QoS value goes out at QoS 0. This is the cloud → device direction — services commands, property-set writes, and any request-family call. |
| `services_reply` outbound QoS | **2** | `[MqttGatewayPublish.java:72]` → `this.publish(headers.get(MqttHeaders.RECEIVED_TOPIC) + TopicConst._REPLY_SUF, 2, response)` | Hardcoded override — `publishReply()` sends at QoS 2. This is the only non-default outbound QoS in the demo. Applied to any reply topic ending in `_reply` that the cloud sends in response to device-initiated requests. |
| `retain` flag | **never set** | — | No occurrences of `setRetained`, `retained(`, or any `retain` configuration in the demo. Paho default is `retain=false`. The demo relies entirely on live publish/subscribe with no broker-side retention. |
| Clean-session | **not inspected** | — | Scan did not cover `MqttPahoClientFactory` configuration; the Spring bean wiring was out of the pattern-match. Safe default for a Paho client is `cleanSession=true` unless overridden. Not blocking any Phase 4 catalog entry. |

**Interpretation.** The demo is the cloud-side server. It tells us:
- What the **cloud subscribes at** (QoS 1 for all inbound topics).
- What the **cloud publishes at** (QoS 0 default, QoS 2 for `_reply`).
- The **cloud never sets retain**.

MQTT delivery QoS is `min(pub_qos, sub_qos)`. If the cloud subscribes at QoS 1, the effective QoS of device-originated messages is capped at 1. If devices publish at QoS 0, messages can be dropped silently. If devices publish at QoS ≥1, delivery is reliable at QoS 1. **Device-side publish QoS remains unspecified by DJI** — the demo code covers only the cloud side — but the cloud's QoS-1 subscribe establishes what the cloud expects, and since the deployed DJI stack works against this demo, device publish QoS must be ≥1 for the reliability-sensitive families (services, services_reply, events with `need_reply: 1`). For best-effort families (`osd`, `state`), device publish at QoS 0 is plausible and would match the reply pattern.

**Policy locked.** Phase 4 per-topic catalog entries that need to state a QoS should cite the demo using the table above. For entries that do not cite a QoS, reading is: the demo evidence applies by default (QoS 1 subscribe, QoS 0 publish out, QoS 2 reply out, retain=false). Phase 9 workflows may surface any QoS-sensitive choreography; carry this evidence forward.

**Remaining open thread**: device-side publish QoS is not directly observed. Only a live packet capture or device-SDK code inspection would close that gap, and neither is in scope. The cloud-side evidence above is sufficient to implement a working server — which is the corpus's purpose.

**Caveat.** The demo is v1.10.0 (deprecated 2025-04-10). No v1.15-era DJI reference server-side code exists in this repo to corroborate whether these QoS choices have changed post-v1.10. In the absence of a newer source, the v1.10 demo remains DJI's only authored evidence.

---

## OQ-004 — `fileupload_list` log-window timestamp unit is inconsistent across DJI sources

**Status**: **resolved 2026-04-19** — user decision: treat as epoch-milliseconds. The v1.11 and Dock 2 v1.15 "Seconds / s" label is a DJI source-table error (the example values are epoch-ms in all three sources, confirming Dock 3's "Milliseconds / ms" label).

**Raised**: 2026-04-19, during Phase 4e drafting of [`mqtt/dock-to-cloud/services/fileupload_list.md`](mqtt/dock-to-cloud/services/fileupload_list.md).

**Question.** The `files[].list[].start_time` and `files[].list[].end_time` integer fields returned by `fileupload_list`'s reply carry different unit labels in each DJI source:

- `[Cloud-API-Doc/docs/en/60.api-reference/20.dock-to-cloud/00.mqtt/20.dock/10.dock2/90.log.md]` (v1.11 Dock 2) — `{"unit_name":"Seconds / s"}`.
- `[DJI_Cloud/DJI_CloudAPI-Dock2-Remote-Log.txt]` (v1.15 Dock 2) — `{"unit_name":"Seconds / s"}`.
- `[DJI_Cloud/DJI_CloudAPI-Dock3-Remote-Log.txt]` (v1.15 Dock 3) — `{"unit_name":"Milliseconds / ms"}`.

Examples in every source use values in the range `1654070968655` and `1659427398806`, which are epoch-milliseconds. If the fields were seconds, the same payload would reference dates in the year ~54400. The example values therefore contradict every v1.11/Dock-2 label *and* confirm the Dock-3 label.

**Resolution (2026-04-19).** User directed: use **milliseconds**. [`fileupload_list.md`](mqtt/dock-to-cloud/services/fileupload_list.md) now states epoch-milliseconds as authoritative and notes the v1.11/Dock-2 "seconds" label is a DJI source-table typo. Revisit if a live Dock 2 deployment reveals different behaviour.

---

## OQ-005 — `fileupload_start` → `fileupload_progress` correlation key is undocumented

**Status**: **resolved 2026-04-19** — user decision: correlate by `object_key` / `fingerprint` (present on both messages) rather than by `bid`. Documented in the affected docs.

**Raised**: 2026-04-19, during Phase 4e drafting of [`mqtt/dock-to-cloud/services/fileupload_start.md`](mqtt/dock-to-cloud/services/fileupload_start.md) and [`mqtt/dock-to-cloud/events/fileupload_progress.md`](mqtt/dock-to-cloud/events/fileupload_progress.md).

**Question.** For other multi-step flows in the corpus — `ota_create` → `ota_progress`, `flighttask_execute` → `flighttask_progress`, `charge_open` service → `charge_open` event, etc. — the cloud correlates the progress stream back to the originating command via the shared `bid` (the cloud picks a `bid` on the command and the device reuses it on each progress event). DJI states this convention for those flows either explicitly in prose or implicitly via example `bid` reuse.

For the log-upload flow, DJI never says whether `fileupload_progress` events echo the `bid` of the originating `fileupload_start` command. All three sources use `"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx"` placeholders in both messages, so the examples don't disambiguate. The `fileupload_progress` payload does carry per-file identifiers (`key`, `fingerprint`, `device_sn`, `module`) that would let the cloud match by file identity independent of `bid`.

**Resolution (2026-04-19).** User directed: treat **`object_key` / `fingerprint`** as the correlation key. The cloud should match `fileupload_progress.output.ext.files[].key` against the `fileupload_start.params.files[].object_key` it issued earlier (and use `fingerprint` as a secondary check). `bid` reuse across the two messages is not guaranteed by DJI and must not be the primary correlation mechanism. Documented in [`fileupload_start.md`](mqtt/dock-to-cloud/services/fileupload_start.md) and [`fileupload_progress.md`](mqtt/dock-to-cloud/events/fileupload_progress.md). Carry into Phase 9 workflow authoring.
