---
name: Corpus content must use real payloads, real topics, real endpoints only
description: Never fabricate or paraphrase API examples; always cite verbatim from DJI source material so the corpus is trustworthy for both audit and implementation
type: feedback
---

All wire-level content in `master-docs/` — HTTP routes, MQTT topics, payload JSON, field names, enum values, examples — must be **sourced verbatim** (or near-verbatim with trivial cleanup like whitespace) from the DJI source directories. Do not invent, paraphrase, or "reconstruct" payload shapes.

**Why**: The corpus is used for two downstream purposes that both demand byte-level accuracy — auditing existing implementations against DJI's actual wire contract, and guiding future implementations of a DJI-Cloud-compatible server. Fabricated or paraphrased examples will silently mislead both.

**How to apply**:
- Pull payload examples verbatim from the **primary source for the content** per `master-docs/SOURCES.md` ranking: `Cloud-API-Doc/` (v1.11.3) for generic / older-v1.11 surfaces, `DJI_Cloud/` (v1.15 extraction) for anything specific to Dock 3 / M4D / M4TD / RC Plus 2 Enterprise or introduced after v1.11.
- Cite provenance for every non-trivial example using the path convention in `SOURCES.md` (e.g., `[Cloud-API-Doc/docs/en/<path>]` or `[DJI_Cloud/<file>]`).
- If an example doesn't exist in source material, say so explicitly in the doc (`**No example in sources**`) and add an entry to `OPEN-QUESTIONS.md` rather than making one up.
- If the source has a Chinese-only example and the EN doc is missing it, translate the EN narrative text only — leave JSON payloads and field names untouched.
- When multiple source docs show conflicting payloads for the same topic, document both with provenance and flag in `OPEN-QUESTIONS.md`.
