# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this repository.

## What this repo is

A long-running, multi-session project to build a curated **DJI Cloud API documentation corpus** for two parallel device cohorts:

- **Current generation** — **DJI Dock 3**, **Matrice 4D (M4D)**, **Matrice 4TD (M4TD)**, and the RC paired with the M4D (**RC Plus 2 Enterprise**).
- **Older generation** — **DJI Dock 2**, **Matrice 3D (M3D)**, **Matrice 3TD (M3TD)**, and the RC paired with the M3D / M3TD (**RC Pro Enterprise**).

**Dock 1** (the original DJI Dock) and the Matrice 30 / 30T / 300 RTK / 350 RTK / Mavic 3 Enterprise families are **out of scope**, even though their material is present in `DJI_Cloud/` and `Cloud-API-Doc/` as a side-effect of how the docs are organized.

Output lives in [`master-docs/`](master-docs/). All other top-level directories are **read-only source material** (see [`master-docs/SOURCES.md`](master-docs/SOURCES.md)).

## At session start — read these first

1. [`master-docs/README.md`](master-docs/README.md) — corpus table of contents
2. [`master-docs/PLAN.md`](master-docs/PLAN.md) — phased plan + current phase
3. [`master-docs/TODO.md`](master-docs/TODO.md) — fine-grained cross-session TODO
4. [`master-docs/_memory/MEMORY.md`](master-docs/_memory/MEMORY.md) — project memory index
5. [`master-docs/SOURCES.md`](master-docs/SOURCES.md) — source authority & inventory

## Scope — IN

The wire contract and workflows only:
- HTTP endpoints, MQTT topics/payloads, WebSocket push messages the in-scope devices emit or expect from a DJI-Cloud-compatible server.
- Device state and property model.
- Workflows / choreography (pairing, wayline execution, livestream, HMS, firmware, etc.).
- Media-transport protocol specifics (RTMP / GB28181 / WebRTC / Agora).
- WMPL (wayline file format), HMS codes, error codes.

## Scope — OUT

Server-side implementation details:
- Databases, persistence choices, SQL schemas.
- Message broker infrastructure picks, auth backends.
- Business logic, framework-specific code patterns.
- Deployment topology.

The official DJI demo (`DJI-Cloud-API-Demo/`) and the third-party `dji_cloud_dock3/` are evidence of **what DJI does on the wire** — not templates for how to structure a server.

## Core directives

- **Only `master-docs/` is writable.** Never modify source directories.
- **Real payloads only.** Every wire example must be verbatim from DJI source (`Cloud-API-Doc/` preferred, `DJI_Cloud/*.txt` as backup, cross-checked). Never fabricate or paraphrase payloads, topics, routes, or field names. Cite provenance.
- **English-only corpus.** Translate from CN only when EN is missing/inadequate; flag translated passages.
- **Ask, don't guess.** When sources are ambiguous or conflict, ask the user and log in `master-docs/OPEN-QUESTIONS.md`.
- **Transport catalog owns schemas.** Workflows link to canonical schema docs rather than duplicating them.
- **Update `TODO.md` as work completes** — it's the cross-session source of truth. Session `TodoWrite` is secondary.
- **Update `master-docs/README.md`** whenever a new doc lands — it's the corpus table of contents.
- **Phase review gates.** Stop at phase boundaries for user review. Don't push through.
- **Small commits.** Ship finished units; don't leave large half-done chunks.
- **Phase 2 (project-level)** — implementation spec or audit — is **not** started without explicit user instruction.

## Git

Repo is initialized on `main`. Source directories are tracked (for cross-machine resumability); only build outputs, IDE dirs, OS noise, and vendored build-tool tarballs are ignored. Line endings normalize to LF in repo via `.gitattributes`.
