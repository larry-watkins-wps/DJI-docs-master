"""
Error codes catalog generator.

Reads:
  - DJI_Cloud/DJI_CloudAPI-HMS-Codes.txt     (DJI primary v1.15 source; despite the "HMS"
                                              filename this file is the general API error-code
                                              reference — DJI's own preamble says HMS alarm
                                              descriptions are NOT in this file.)
  - Cloud-API-Doc/docs/en/71.error-code.md   (v1.11 drift cross-check only.)

Emits:
  - master-docs/error-codes/README.md        (single doc per TODO.md Phase 8 spec; grouped
                                              table by function-module BC digits.)
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
V15_SRC = ROOT / "DJI_Cloud" / "DJI_CloudAPI-HMS-Codes.txt"
V11_SRC = ROOT / "Cloud-API-Doc" / "docs" / "en" / "71.error-code.md"
OUT = ROOT / "master-docs" / "error-codes" / "README.md"

# Function-module labels — inferred from tip text and cross-referenced with DJI-Cloud-API-Demo
# cloud-sdk enum classes (FirmwareErrorCodeEnum 312xxx; WaylineErrorCodeEnum 314xxx;
# LogErrorCodeEnum 324xxx; CommonErrorEnum 325xxx; DebugErrorCodeEnum 326xxx+partial-514xxx;
# ControlErrorCodeEnum 327xxx; LiveErrorCodeEnum 513xxx; DrcStatusErrorEnum 514300+).
MODULE_LABELS = {
    "312": ("Firmware upgrade", "Dock / aircraft firmware update flow."),
    "314": ("Wayline task — distribution", "Wayline file transfer from cloud to dock to aircraft, and task-preparation handshake."),
    "315": ("Wayline task — dock communication", "Dock ↔ cloud and dock ↔ aircraft command-distribution faults during wayline execution."),
    "316": ("Wayline task — aircraft configuration", "Aircraft-side parameter-configuration and readiness faults before / during wayline execution."),
    "317": ("Media — aircraft storage", "Aircraft media-file enumeration and storage-format operations."),
    "319": ("Dock task lifecycle", "Dock-state gating (idle / busy / uploading / initializing) and task cancellation."),
    "321": ("Flight task execution", "In-flight task errors — route limits, obstacle detection, GEO zones, signal loss."),
    "322": ("Flight task — stop / abort", "Task termination reasons (manual stop, cloud-takeover, user RTH command)."),
    "324": ("Remote log upload", "Dock / aircraft log compression, listing, and upload to cloud."),
    "325": ("Common command", "Cloud-command parameter and dispatch errors shared across device interactions."),
    "326": ("Cellular / SIM / eSIM", "DJI Cellular Dongle state, SIM / eSIM activation, and 4G/LTE transmission."),
    "327": ("Live Flight Controls", "Cloud-initiated live flight operations — parameter-set, control-authority, livestream, speaker, panorama."),
    "328": ("CAAC real-name registration", "Registration-status gating introduced for Chinese-market aircraft."),
    "336": ("FlyTo command", "FlyTo-destination dispatch and command-response handling."),
    "337": ("Takeoff / FlyTo destination", "Takeoff-readiness and FlyTo-destination-validation errors."),
    "338": ("Aircraft communication", "Aircraft ↔ dock communication-layer faults."),
    "341": ("Dock location convergence", "Dock positioning / RTK-convergence gating."),
    "386": ("Miscellaneous task error", "Catch-all task fault with no dedicated module."),
    "513": ("Livestream", "Camera livestream start / stop, quality and lens / camera selection."),
    "514": ("Dock operations & DRC", "Dock commands (maintenance, cover, charging, remote debugging, rain sensor) and DRC-mode MQTT connection lifecycle."),
}


def parse_v15():
    rows = []
    with V15_SRC.open(encoding="utf-8") as f:
        for line in f:
            m = re.match(r"^(\d{6})\s+(.+)$", line.strip())
            if m:
                rows.append((m.group(1), m.group(2).strip()))
    return rows


def parse_v11():
    # v1.11 is an HTML-style markdown with <tr><td>CODE</td><td>DESC</td></tr>
    text = V11_SRC.read_text(encoding="utf-8")
    pattern = re.compile(r"<tr>\s*<td[^>]*>\s*(\d{6})\s*</td>\s*<td[^>]*>(.*?)</td>", re.DOTALL)
    return {m.group(1): m.group(2).strip() for m in pattern.finditer(text)}


def esc_md(s: str) -> str:
    return s.replace("|", "\\|").replace("\r\n", " ").replace("\n", " ").strip()


def main():
    v15 = parse_v15()
    v11 = parse_v11()
    v15_codes = {c for c, _ in v15}
    v11_codes = set(v11.keys())
    new_in_v15 = sorted(v15_codes - v11_codes)

    by_module = defaultdict(list)
    for c, d in v15:
        by_module[c[:3]].append((c, d))
    for rows in by_module.values():
        rows.sort(key=lambda r: r[0])

    unknown_modules = sorted(set(by_module.keys()) - set(MODULE_LABELS.keys()))
    if unknown_modules:
        # Paranoid — shouldn't happen with the dataset we've inspected.
        raise RuntimeError(f"Unknown BC modules: {unknown_modules}")

    lines = []
    lines.append("# Error codes")
    lines.append("")
    lines.append("DJI Cloud API general error-code reference. These are command-response and task-status codes "
                 "returned in HTTP bodies, MQTT `services_reply.result`, and event-payload `result` / `error` fields — "
                 "distinct from the HMS alarm codes in [`hms-codes/`](../hms-codes/README.md).")
    lines.append("")
    lines.append(f"**{len(v15_codes)} codes total** across {len(by_module)} function modules, drawn from "
                 f"[`DJI_Cloud/DJI_CloudAPI-HMS-Codes.txt`](../../DJI_Cloud/DJI_CloudAPI-HMS-Codes.txt). "
                 f"(The source file is mis-named; DJI's own preamble states that HMS alarm descriptions are "
                 "**not** in this file — they live in [`HMS.json`](../../DJI_Cloud/HMS.json), covered by "
                 "[`hms-codes/`](../hms-codes/README.md).)")
    lines.append("")
    lines.append("## 1. Format")
    lines.append("")
    lines.append("Every error code is a **six-digit decimal number** in the form `ABCDEF`:")
    lines.append("")
    lines.append("| Segment | Width | Meaning |")
    lines.append("|---|---|---|")
    lines.append("| `A` | 1 digit | Error source. `3` or `5` = device side (dock or aircraft); `4` or `6` = DJI Pilot 2. |")
    lines.append("| `BC` | 2 digits | Function module. See §3 for the full list. |")
    lines.append("| `DEF` | 3 digits | Module-specific code. No global meaning. |")
    lines.append("")
    lines.append("Source authority: [`DJI_Cloud/DJI_CloudAPI-HMS-Codes.txt`](../../DJI_Cloud/DJI_CloudAPI-HMS-Codes.txt) (v1.15) — the \"First Digit (A) Error Source\" table maps source codes `3`, `4`, `5`, `6` to either Device Side (`3` / `5`) or DJI Pilot 2 (`4` / `6`). v1.15 carries only `3` and `5` codes; Pilot-2 `4` / `6` codes are not present in this extract.")
    lines.append("")
    lines.append("## 2. How codes reach the cloud")
    lines.append("")
    lines.append("1. **HTTP** — response envelope `{code, message, data}` where `code != 0` carries the error value. See [`http/README.md §4`](../http/README.md).")
    lines.append("2. **MQTT services_reply** — the `data.result` field of `thing/product/{gateway_sn}/services_reply`. See [`mqtt/README.md §5`](../mqtt/README.md).")
    lines.append("3. **MQTT events with `need_reply: 1`** — the `data.result` field of the event payload itself. The cloud mirrors the value back in its `_reply`.")
    lines.append("4. **DRC / Low-latency channels** — `result` field on `drc/down` responses and `drc/up` heartbeats; see [`mqtt/dock-to-cloud/drc/`](../mqtt/dock-to-cloud/drc/).")
    lines.append("")
    lines.append("## 3. Catalog — grouped by function module")
    lines.append("")
    for mod in sorted(by_module):
        label, blurb = MODULE_LABELS[mod]
        rows = by_module[mod]
        lines.append(f"### {mod}xxx — {label}")
        lines.append("")
        lines.append(blurb)
        lines.append("")
        lines.append(f"{len(rows)} code{'s' if len(rows) != 1 else ''}.")
        lines.append("")
        lines.append("| Code | Description |")
        lines.append("|---|---|")
        for c, d in rows:
            lines.append(f"| `{c}` | {esc_md(d)} |")
        lines.append("")

    lines.append("## 4. v1.11 → v1.15 drift")
    lines.append("")
    lines.append("v1.15 is **fully additive** relative to v1.11: every v1.11 code is retained, and v1.15 introduces "
                 f"{len(new_in_v15)} new code{'s' if len(new_in_v15) != 1 else ''}:")
    lines.append("")
    if new_in_v15:
        lines.append("| Code | Module | Description (v1.15) |")
        lines.append("|---|---|---|")
        code_to_desc = {c: d for c, d in v15}
        for c in new_in_v15:
            mod = c[:3]
            label = MODULE_LABELS.get(mod, ("?", ""))[0]
            lines.append(f"| `{c}` | {mod}xxx ({label}) | {esc_md(code_to_desc[c])} |")
        lines.append("")
    lines.append("v1.11 source: [`Cloud-API-Doc/docs/en/71.error-code.md`](../../Cloud-API-Doc/docs/en/71.error-code.md). "
                 "Per [`OPEN-QUESTIONS.md` OQ-001](../OPEN-QUESTIONS.md#oq-001--source-version-mismatch-between-cloud-api-doc-v1113-and-dji_cloud-v115), "
                 "v1.15 is authoritative and v1.11 is retained for drift cross-check only.")
    lines.append("")
    lines.append("## 5. DJI-Cloud-API-Demo enum cross-reference")
    lines.append("")
    lines.append("The DJI-Cloud-API-Demo reference implementation (v1.10, deprecated 2025-04-10) groups error codes "
                 "into feature-module Java enum classes. These are not primary for the corpus (v1.15 `DJI_Cloud/` is primary "
                 "per OQ-001), but the enum names provide useful semantic labels for BC modules:")
    lines.append("")
    lines.append("| Enum class | BC modules covered | Path |")
    lines.append("|---|---|---|")
    lines.append("| `FirmwareErrorCodeEnum` | `312xxx` | [`cloud-sdk/.../firmware/FirmwareErrorCodeEnum.java`](../../DJI-Cloud-API-Demo/cloud-sdk/src/main/java/com/dji/sdk/cloudapi/firmware/FirmwareErrorCodeEnum.java) |")
    lines.append("| `WaylineErrorCodeEnum` | `314xxx`, `321xxx`, `322xxx` | [`cloud-sdk/.../wayline/WaylineErrorCodeEnum.java`](../../DJI-Cloud-API-Demo/cloud-sdk/src/main/java/com/dji/sdk/cloudapi/wayline/WaylineErrorCodeEnum.java) |")
    lines.append("| `LogErrorCodeEnum` | `324xxx` | [`cloud-sdk/.../log/LogErrorCodeEnum.java`](../../DJI-Cloud-API-Demo/cloud-sdk/src/main/java/com/dji/sdk/cloudapi/log/LogErrorCodeEnum.java) |")
    lines.append("| `CommonErrorEnum` | `314000`, `325001` | [`cloud-sdk/.../common/CommonErrorEnum.java`](../../DJI-Cloud-API-Demo/cloud-sdk/src/main/java/com/dji/sdk/common/CommonErrorEnum.java) |")
    lines.append("| `DebugErrorCodeEnum` | `326xxx` | [`cloud-sdk/.../debug/DebugErrorCodeEnum.java`](../../DJI-Cloud-API-Demo/cloud-sdk/src/main/java/com/dji/sdk/cloudapi/debug/DebugErrorCodeEnum.java) |")
    lines.append("| `ControlErrorCodeEnum` | `327xxx` | [`cloud-sdk/.../control/ControlErrorCodeEnum.java`](../../DJI-Cloud-API-Demo/cloud-sdk/src/main/java/com/dji/sdk/cloudapi/control/ControlErrorCodeEnum.java) |")
    lines.append("| `LiveErrorCodeEnum` | `513xxx` (and bare `13xxx` enum values that prepend source digit `5` on the wire) | [`cloud-sdk/.../livestream/LiveErrorCodeEnum.java`](../../DJI-Cloud-API-Demo/cloud-sdk/src/main/java/com/dji/sdk/cloudapi/livestream/LiveErrorCodeEnum.java) |")
    lines.append("| `DrcStatusErrorEnum` | `514300`–`514304` (DRC-mode MQTT errors) | [`cloud-sdk/.../control/DrcStatusErrorEnum.java`](../../DJI-Cloud-API-Demo/cloud-sdk/src/main/java/com/dji/sdk/cloudapi/control/DrcStatusErrorEnum.java) |")
    lines.append("")
    lines.append("## 6. Notes on source file naming")
    lines.append("")
    lines.append("The v1.15 source file is named `DJI_CloudAPI-HMS-Codes.txt` but its contents are the general API "
                 "error-code reference, **not** HMS alarm codes. DJI's own preamble (line 5 of the source) reads: "
                 "\"The error code description of HMS can not be directly obtained through the error code. Developer "
                 "needs to complete the concatenation of the 'Copy Key' according to the rules introduced in the HMS "
                 "Function. Search the error code description in the [hms.json](../../DJI_Cloud/HMS.json) based on the "
                 "'Copy Key'.\" HMS alarm codes have their own catalog at [`hms-codes/`](../hms-codes/README.md).")
    lines.append("")
    lines.append("## Sources")
    lines.append("")
    lines.append(f"- Primary — [`DJI_Cloud/DJI_CloudAPI-HMS-Codes.txt`](../../DJI_Cloud/DJI_CloudAPI-HMS-Codes.txt) (v1.15 authoritative, {len(v15_codes)} codes).")
    lines.append(f"- Drift cross-check — [`Cloud-API-Doc/docs/en/71.error-code.md`](../../Cloud-API-Doc/docs/en/71.error-code.md) (v1.11, {len(v11_codes)} codes).")
    lines.append("- Reference — the 7 `*ErrorCodeEnum.java` files in `DJI-Cloud-API-Demo/cloud-sdk/` (v1.10, deprecated).")
    lines.append("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT} — {len(v15_codes)} codes, {len(by_module)} modules, {len(new_in_v15)} new vs v1.11.")


if __name__ == "__main__":
    main()
