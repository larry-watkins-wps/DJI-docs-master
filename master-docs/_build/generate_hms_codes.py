"""
HMS codes catalog generator.

Reads:
  - DJI_Cloud/HMS.json                          (DJI primary v1.15 source, 1,769 alarms)
  - master-docs/_build/_translations.json       (curated CN->EN for 531 CN-content alarms)

Emits:
  - master-docs/hms-codes/0xNN-<slug>.md        (14 per-prefix files)
  - master-docs/hms-codes/README.md             (master index)

Policy:
  - All 1,769 alarmIds are preserved verbatim.
  - tipEn strings with CJK ideographs are rendered as the curated EN translation with a
    dagger (+) marker; the CN original is shown in a details/summary block beneath the row
    table section so the audit trail is preserved (no silent paraphrase).
  - Full-width Chinese parentheses (U+FF08, U+FF09) normalize to ASCII '(' and ')'.
  - Trailing _in_the_sky / _pm320 / _wm265 / _ta101 suffixes kept verbatim — these
    correspond to contextual variants DJI emits when the same alarm fires in different
    flight contexts or on different airframes.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict, Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent  # repo root
HMS_JSON = ROOT / "DJI_Cloud" / "HMS.json"
TRANSLATIONS = ROOT / "master-docs" / "_build" / "_translations.json"
OUT_DIR = ROOT / "master-docs" / "hms-codes"

CJK = re.compile(r"[\u4e00-\u9fff]")
FULLWIDTH_PAREN = str.maketrans({"\uff08": "(", "\uff09": ")"})

# First-byte prefix → (filename stem, domain label shown in headers / index)
PREFIX_META = {
    "11": ("0x11-payload-general", "Payload (general)"),
    "12": ("0x12-battery-station", "Battery Station"),
    "14": ("0x14-payload-imu", "Payload IMU"),
    "15": ("0x15-mmwave-radar", "mmWave Radar"),
    "16": ("0x16-flight-control", "Flight-control system"),
    "17": ("0x17-transmission", "Image transmission & RC link"),
    "19": ("0x19-system-overload", "System overload (CPU / memory / network)"),
    "1a": ("0x1A-vision-sensors", "Vision sensors"),
    "1b": ("0x1B-navigation-tracking", "Navigation & Target Acquisition"),
    "1c": ("0x1C-camera", "Camera"),
    "1d": ("0x1D-gimbal", "Gimbal"),
    "1e": ("0x1E-psdk-payload", "PSDK / third-party payload (searchlight, speaker, etc.)"),
    "1f": ("0x1F-cellular-lte", "LTE / Cellular"),
    "20": ("0x20-takeoff-tags", "Takeoff tags"),
}

# 0x16 second-byte → sub-section label (domain inferred from tip content)
SECTION_16 = {
    "00": "Flight controller",
    "01": "Sensor system",
    "02": "Tachometer",
    "03": "Accelerometer",
    "04": "Barometer",
    "05": "GNSS",
    "06": "Compass",
    "07": "RTK",
    "08": "Motors & ESC",
    "09": "Battery",
    "0a": "Real-name registration",
    "10": "Takeoff readiness",
    "11": "Thermal & accessory",
    "20": "USB / extension port",
    "30": "BDS satellite",
    "40": "Internal — abstract-data topics (CN+)",
    "41": "Internal — DSP interaction (CN+)",
    "42": "Internal — DBus topics (CN+)",
    "43": "Internal — Intelligent flight modes (CN+)",
    "45": "Internal — Landing & wayline",
    "46": "Internal — Fusion / hall / RTK",
    "47": "Internal — Positioning & compass calibration",
    "49": "Internal — Planner & global map (CN+)",
    "4a": "Internal — Flight control loops (CN+)",
    "67": "Power Line Follow",
}


def load():
    with HMS_JSON.open(encoding="utf-8") as f:
        data = json.load(f)
    with TRANSLATIONS.open(encoding="utf-8") as f:
        translations = json.load(f)
    return data, translations


def split_alarm_id(aid: str):
    """Return (normalized_hex_lower, trailing_suffix_or_None, raw_aid)."""
    m = re.match(r"0[xX]([0-9A-Fa-f]+)(_.+)?$", aid)
    if not m:
        return None, None, aid
    hex_part, tail = m.groups()
    return hex_part.lower(), tail, aid


def normalize_tip(tip: str) -> str:
    return tip.translate(FULLWIDTH_PAREN).strip()


def entry_rendering(row, translations):
    """Return (display_tip, is_translated, cn_original)."""
    raw = row["tipEn"]
    has_cjk = bool(CJK.search(raw))
    if has_cjk:
        en = translations.get(row["alarmId"])
        if not en:
            raise RuntimeError(f"Missing translation for {row['alarmId']}")
        return en, True, normalize_tip(raw)
    return normalize_tip(raw), False, None


def esc_md(s: str) -> str:
    # Minimal escaping for markdown table cells: collapse newlines, escape pipes.
    return s.replace("\r\n", " ").replace("\n", " ").replace("|", "\\|").strip()


def render_row(row, display_tip, is_translated):
    marker = "+" if is_translated else ""
    return f"| `{row['alarmId']}` | {esc_md(display_tip)}{marker} |"


def render_prefix_file(prefix, entries, translations, out_path, domain_label):
    lines = []
    stem = out_path.stem
    lines.append(f"# HMS codes — 0x{prefix.upper()}** ({domain_label})")
    lines.append("")
    lines.append(f"Prefix byte `0x{prefix.upper()}`. {len(entries)} alarm codes.")
    lines.append("")
    lines.append("The prefix byte is the wire-level grouping DJI uses in the `data.list[].code` field "
                 "emitted on [`thing/product/{gateway_sn}/events` method `hms`](../mqtt/dock-to-cloud/events/hms.md). "
                 "The domain label above is inferred from the tip text — DJI does not publish an official prefix taxonomy.")
    lines.append("")
    lines.append("Entries rendered with a trailing **+** have a curated CN→EN translation because the original "
                 "`tipEn` value in [`HMS.json`](../../DJI_Cloud/HMS.json) contains Chinese-language developer-debug "
                 "strings under the \"English\" field. The CN originals are preserved below each subsection in a "
                 "`CN source` callout so the audit trail is intact.")
    lines.append("")

    if prefix == "16":
        # Group by second byte
        by2 = defaultdict(list)
        for row in entries:
            hp, _, _ = split_alarm_id(row["alarmId"])
            sb = hp[2:4] if hp and len(hp) >= 4 else "xx"
            by2[sb].append(row)
        for sb in sorted(by2):
            label = SECTION_16.get(sb, "(unclassified)")
            rows = by2[sb]
            lines.append(f"## 0x16{sb.upper()}** — {label} ({len(rows)} codes)")
            lines.append("")
            lines.append("| Alarm ID | Tip |")
            lines.append("|---|---|")
            cn_backups = []
            for row in rows:
                disp, is_tr, cn = entry_rendering(row, translations)
                lines.append(render_row(row, disp, is_tr))
                if is_tr:
                    cn_backups.append((row["alarmId"], cn))
            lines.append("")
            if cn_backups:
                lines.append("<details><summary>CN source (verbatim from HMS.json)</summary>")
                lines.append("")
                lines.append("| Alarm ID | `tipEn` (original CN) |")
                lines.append("|---|---|")
                for aid, cn in cn_backups:
                    lines.append(f"| `{aid}` | {esc_md(cn)} |")
                lines.append("")
                lines.append("</details>")
                lines.append("")
    else:
        lines.append("| Alarm ID | Tip |")
        lines.append("|---|---|")
        cn_backups = []
        for row in entries:
            disp, is_tr, cn = entry_rendering(row, translations)
            lines.append(render_row(row, disp, is_tr))
            if is_tr:
                cn_backups.append((row["alarmId"], cn))
        lines.append("")
        if cn_backups:
            lines.append("<details><summary>CN source (verbatim from HMS.json)</summary>")
            lines.append("")
            lines.append("| Alarm ID | `tipEn` (original CN) |")
            lines.append("|---|---|")
            for aid, cn in cn_backups:
                lines.append(f"| `{aid}` | {esc_md(cn)} |")
            lines.append("")
            lines.append("</details>")
            lines.append("")

    # Trailing suffix callout — show unique suffixes observed in this prefix
    suffixes = Counter()
    for row in entries:
        _, tail, _ = split_alarm_id(row["alarmId"])
        if tail:
            suffixes[tail] += 1
    if suffixes:
        lines.append("## Contextual suffixes")
        lines.append("")
        lines.append("Alarm IDs in this prefix include trailing suffixes that denote DJI-emitted variants "
                     "of the same base code in different flight or airframe contexts:")
        lines.append("")
        for suf, n in sorted(suffixes.items()):
            lines.append(f"- `{suf}` — {n} entry/entries.")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("**Source**: [`DJI_Cloud/HMS.json`](../../DJI_Cloud/HMS.json) (DJI v1.15 authoritative).")
    lines.append("")
    lines.append("**See also**: ")
    lines.append("- Event definition — [`mqtt/dock-to-cloud/events/hms.md`](../mqtt/dock-to-cloud/events/hms.md).")
    lines.append("- Topic-level overview — [`mqtt/README.md`](../mqtt/README.md).")
    lines.append("- General API error codes (distinct from HMS alarms) — [`error-codes/README.md`](../error-codes/README.md).")
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")


def render_readme(by_prefix, others, translations, out_path):
    total = sum(len(v) for v in by_prefix.values()) + len(others)
    cjk_count = sum(1 for rows in by_prefix.values() for r in rows if CJK.search(r["tipEn"]))
    cjk_count += sum(1 for r in others if CJK.search(r["tipEn"]))

    lines = []
    lines.append("# HMS codes")
    lines.append("")
    lines.append(f"Catalog of DJI Health Management System (HMS) alarm codes, drawn verbatim from "
                 f"[`DJI_Cloud/HMS.json`](../../DJI_Cloud/HMS.json). **{total} codes total** across "
                 f"{len(by_prefix)} first-byte prefix buckets plus {len(others)} non-conforming outlier(s).")
    lines.append("")
    lines.append("## How HMS codes reach the cloud")
    lines.append("")
    lines.append("The dock (or RC, via pilot-to-cloud) publishes an `hms` event on "
                 "`thing/product/{gateway_sn}/events` whenever the aircraft raises a health warning. "
                 "Each event carries `data.list[].code` (an alarm ID string), `level` (0 = Notification, "
                 "1 = Reminder, 2 = Warning), `module` (the event-source module, **not** the alarm-ID "
                 "prefix), plus `component_index` / `sensor_index` that fill `%component_index` / `%index` "
                 "placeholders in the tip text.")
    lines.append("")
    lines.append("See [`mqtt/dock-to-cloud/events/hms.md`](../mqtt/dock-to-cloud/events/hms.md) for the "
                 "full event envelope and payload definition.")
    lines.append("")
    lines.append("## Cloud implementation workflow")
    lines.append("")
    lines.append("1. Subscribe to `thing/product/{gateway_sn}/events`.")
    lines.append("2. Filter messages where `method == \"hms\"`.")
    lines.append("3. For each entry in `data.list[]`, look up `code` in [`HMS.json`](../../DJI_Cloud/HMS.json) "
                 "to obtain the `tipEn` template.")
    lines.append("4. Substitute placeholders: `%alarmid` → the raw `code` value; `%component_index` and "
                 "`%index` → the `args.component_index` / `args.sensor_index` from the event payload.")
    lines.append("5. Correlate with `level`, `imminent`, and `in_the_sky` flags for UI severity handling.")
    lines.append("")
    lines.append("## Catalog — one file per first-byte prefix")
    lines.append("")
    lines.append("| Prefix | Domain (inferred) | Codes | File |")
    lines.append("|---|---|---|---|")
    for prefix in sorted(by_prefix):
        stem, domain = PREFIX_META[prefix]
        count = len(by_prefix[prefix])
        lines.append(f"| `0x{prefix.upper()}` | {domain} | {count} | [`{stem}.md`]({stem}.md) |")
    if others:
        lines.append(f"| — | Outliers (non-hex / uppercase-X) | {len(others)} | [`outliers.md`](outliers.md) |")
    lines.append(f"| **Total** | | **{total}** | |")
    lines.append("")
    lines.append(f"**{cjk_count}** entries have CJK-ideograph content in the source `tipEn` field — a DJI source defect "
                 "where Chinese-language developer-debug strings were leaked under the \"English\" copy key. These rows "
                 "display a curated EN translation marked with a trailing **+** and retain the CN original in a "
                 "collapsible `CN source` block under each subsection.")
    lines.append("")
    lines.append("## Source defects preserved")
    lines.append("")
    lines.append("- `unknown` — a single non-hex entry with tip `\"Contact your local dealer or DJI Support\"`. "
                 "Filed under [`outliers.md`](outliers.md).")
    lines.append("- `0X1B033001` — uppercase-`X` casing (all other IDs use lowercase `0x`). Included under prefix `0x1B`.")
    lines.append("- Full-width Chinese parentheses `（ ）` appear in 167 tips where the content is otherwise English — "
                 "normalized to ASCII `( )` in this catalog.")
    lines.append("- 0x16 takes **~52%** of all HMS codes (921/1,769) because DJI's flight-control system is the largest "
                 "source of health events. That file is sub-sectioned by second byte for navigability.")
    lines.append("")
    lines.append("## Sources")
    lines.append("")
    lines.append("- Primary — [`DJI_Cloud/HMS.json`](../../DJI_Cloud/HMS.json) (DJI v1.15 authoritative).")
    lines.append("- Event envelope — [`DJI_Cloud/DJI_CloudAPI-Dock3-HMS.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock3-HMS.txt), "
                 "[`DJI_Cloud/DJI_CloudAPI-Dock2-HMS.txt`](../../DJI_Cloud/DJI_CloudAPI-Dock2-HMS.txt).")
    lines.append("- Per-phase event doc — [`mqtt/dock-to-cloud/events/hms.md`](../mqtt/dock-to-cloud/events/hms.md).")
    lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def render_outliers(others, out_path):
    lines = []
    lines.append("# HMS codes — outliers (non-hex IDs)")
    lines.append("")
    lines.append("HMS.json entries whose `alarmId` does not match the `0x<hex>` pattern followed by the bulk of the catalog.")
    lines.append("")
    lines.append("| Alarm ID | Tip | Notes |")
    lines.append("|---|---|---|")
    for row in others:
        tip = esc_md(normalize_tip(row["tipEn"]))
        note = "Literal string `unknown` — not a hex code. Tip is a generic fallback." if row["alarmId"] == "unknown" else ""
        lines.append(f"| `{row['alarmId']}` | {tip} | {note} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("**Source**: [`DJI_Cloud/HMS.json`](../../DJI_Cloud/HMS.json).")
    lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    data, translations = load()
    by_prefix = defaultdict(list)
    others = []

    for row in data:
        hp, _, _ = split_alarm_id(row["alarmId"])
        if hp is None or len(hp) < 2 or hp[:2] not in PREFIX_META:
            others.append(row)
            continue
        by_prefix[hp[:2]].append(row)

    for rows in by_prefix.values():
        rows.sort(key=lambda r: r["alarmId"].lower())
    others.sort(key=lambda r: r["alarmId"])

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for prefix, rows in by_prefix.items():
        stem, domain = PREFIX_META[prefix]
        render_prefix_file(prefix, rows, translations, OUT_DIR / f"{stem}.md", domain)

    if others:
        render_outliers(others, OUT_DIR / "outliers.md")

    render_readme(by_prefix, others, translations, OUT_DIR / "README.md")

    total = sum(len(v) for v in by_prefix.values()) + len(others)
    print(f"Wrote {len(by_prefix) + (1 if others else 0) + 1} files covering {total} alarm entries.")
    for prefix in sorted(by_prefix):
        print(f"  0x{prefix.upper()}: {len(by_prefix[prefix])} -> {PREFIX_META[prefix][0]}.md")
    if others:
        print(f"  outliers: {len(others)} -> outliers.md")


if __name__ == "__main__":
    main()
