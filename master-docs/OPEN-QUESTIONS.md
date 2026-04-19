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

**Remaining open thread.** As of 2026-04-18 the `DJI_Cloud/` extraction covers the entire `/api-reference/` section of the live site (67 files — see `SOURCES.md` §3). Pages outside `/api-reference/` — overview, product-support, release-notes, tutorials, quick-start, feature-set, debug — are **not** in the extraction set. If a later phase needs one of those, fetch from the live site (or extend `scrape_api_reference.py`'s URL inventory). No action required now.
