---
name: DJI Cloud docs corpus project
description: Long-running multi-session project to build a curated DJI Dock 3 / Matrice 4D / Matrice 4TD Cloud API documentation corpus, with possible downstream implementation spec
type: project
---

**Project root**: `C:\repos\DJI-docs-master`
**Git remote** (`origin`): `https://github.com/larry-watkins-wps/DJI-docs-master.git` — clone from here on any new machine to resume work; push after each meaningful commit so the other machine can pull.
**Output directory**: `master-docs/` (only writable location for documentation output)
**Source directories** (read-only reference): `Cloud-API-Doc/`, `DJI-Cloud-API-Demo/`, `DJI_Cloud/`, `dji_cloud_dock3/`

**Hardware in scope**: two parallel cohorts.
- **Current gen**: DJI Dock 3, Matrice 4D (M4D), Matrice 4TD (M4TD), **RC Plus 2 Enterprise** (paired with M4D). RC Plus 2 Enterprise is distinct from the earlier RC Plus Enterprise.
- **Older gen**: DJI Dock 2, Matrice 3D (M3D), Matrice 3TD (M3TD), **RC Pro Enterprise** (paired with M3D / M3TD).
**Explicitly out of scope**: Dock 1, Matrice 30 / 30T, Matrice 300 / 350 RTK, Mavic 3 Enterprise, Matrice 400 — even though some of their source material is present in `DJI_Cloud/` as a side-effect of the scrape.

**Phase 1 goal**: Build a clean, concise, LLM-digestible documentation corpus in `master-docs/` covering the DJI Cloud API surface needed for the in-scope hardware.

**Scope — IN**:
- API surface (the wire contract: HTTP endpoints, MQTT topics/payloads, WebSocket push messages the devices emit or expect from the cloud).
- Device state and property model for Dock 3, M4D, M4TD, paired RC.
- Workflows / choreography: ordered sequences of API interactions that compose real device operations (e.g., Dock 3 pairing, device binding, wayline upload and execution, livestream start/stop, firmware update, HMS event reporting, remote control handoff).

**Scope — OUT**:
- Cloud server implementation details: databases, persistence choices, SQL schemas, message broker infrastructure picks, auth backends, business logic, framework-specific code patterns, deployment topology.
- The DJI demo code is source for **what DJI does on the wire** — do not document its internal Java/Spring structure as if it were required.

**Phase 2 (deferred decision)**: After corpus is complete, user will either (a) initiate an implementation spec for a self-hosted DJI Cloud replacement stack, or (b) use the corpus to audit existing systems. Do not start Phase 2 until user explicitly says so.

**Why**: The user wants a consolidated, trustworthy source of truth for DJI Cloud behavior — DJI's own demo project was deprecated 2025-04-10 and docs are scattered across multiple repos and MHTML extractions.

**How to apply**: Always check `master-docs/PLAN.md` and `master-docs/TODO.md` at session start to resume. Treat sibling source directories as read-only. Never start Phase 2 work without explicit user approval.
