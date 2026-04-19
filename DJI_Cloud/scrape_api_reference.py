"""Scrape the DJI Cloud API "API Reference" section into DJI_Cloud/*.txt files.

The live docs site at https://developer.dji.com/doc/cloud-api-tutorial/en/ is a
JavaScript-rendered VuePress SPA, so this uses Playwright to render each page
and extract the `.theme-default-content` container — that matches the clean
content shape of the existing hand-saved `DJI_CloudAPI-*.txt` files in this
directory (they came from MHTML exports that got trimmed the same way).

Scope filter mirrors CLAUDE.md: Dock 1 and Dock 2 pages are skipped by default
since they're out of scope; pass --include-legacy to pull them anyway.

Dedupe is done against existing *.txt filenames in this directory using a
normalized-slug comparison (lowercased, non-alphanumerics stripped), so minor
naming differences like `DeviceManagement` vs `Device-Management` count as the
same file. Anything that matches an existing file is reported and skipped;
everything else is written to `_scraped/` as a staging area for manual review
before moving into `DJI_Cloud/` proper.

Setup:
    pip install playwright
    playwright install chromium

Run:
    python scrape_api_reference.py              # stage new pages to _scraped/
    python scrape_api_reference.py --list       # print plan, don't scrape
    python scrape_api_reference.py --include-legacy   # also pull Dock 1/2
    python scrape_api_reference.py --force      # re-scrape even if dupe
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


# ---------------------------------------------------------------------------
# URL inventory — captured from the live sidebar on 2026-04-18.
# (label, url). Anchor-only links (with '#...') and update-note links were
# stripped; every entry here is a distinct content page.
# ---------------------------------------------------------------------------

URLS: list[tuple[str, str]] = [
    # DJI WPML
    ("Overview",                    "api-reference/dji-wpml/overview.html"),
    ("Template.kml",                "api-reference/dji-wpml/template-kml.html"),
    ("Waylines.wpml",               "api-reference/dji-wpml/waylines-wpml.html"),
    ("Common Elements",             "api-reference/dji-wpml/common-element.html"),

    # Pilot-to-cloud — MQTT
    ("Topic Definition",            "api-reference/pilot-to-cloud/mqtt/topic-definition.html"),
    ("Properties",                  "api-reference/pilot-to-cloud/mqtt/m3-series/properties.html"),
    ("Properties",                  "api-reference/pilot-to-cloud/mqtt/rc-pro/properties.html"),
    ("Device Management",           "api-reference/pilot-to-cloud/mqtt/rc-pro/device.html"),
    ("Live Stream",                 "api-reference/pilot-to-cloud/mqtt/rc-pro/live.html"),
    ("Live Flight Controls",        "api-reference/pilot-to-cloud/mqtt/rc-pro/drc.html"),
    ("Remote Control",              "api-reference/pilot-to-cloud/mqtt/rc-pro/remote-control.html"),
    ("Properties",                  "api-reference/pilot-to-cloud/mqtt/m4-series/properties.html"),
    ("Properties",                  "api-reference/pilot-to-cloud/mqtt/dji-rc-plus-2/properties.html"),
    ("Device Management",           "api-reference/pilot-to-cloud/mqtt/dji-rc-plus-2/device.html"),
    ("Live Stream",                 "api-reference/pilot-to-cloud/mqtt/dji-rc-plus-2/live.html"),
    ("Live Flight Controls",        "api-reference/pilot-to-cloud/mqtt/dji-rc-plus-2/drc.html"),
    ("Remote Control",              "api-reference/pilot-to-cloud/mqtt/dji-rc-plus-2/remote-control.html"),
    ("Properties",                  "api-reference/pilot-to-cloud/mqtt/matrice-400/properties.html"),
    ("Properties",                  "api-reference/pilot-to-cloud/mqtt/others/aircraft/properties.html"),
    ("Properties",                  "api-reference/pilot-to-cloud/mqtt/others/rc/properties.html"),
    ("Device Management",           "api-reference/pilot-to-cloud/mqtt/others/rc/device.html"),
    ("Live Stream",                 "api-reference/pilot-to-cloud/mqtt/others/rc/live.html"),

    # Pilot-to-cloud — HTTPS
    ("Create Map Elements",             "api-reference/pilot-to-cloud/https/map-elements/create.html"),
    ("Update Map Elements",             "api-reference/pilot-to-cloud/https/map-elements/update.html"),
    ("Obtain Map Elements",             "api-reference/pilot-to-cloud/https/map-elements/obtain.html"),
    ("Delete Map Elements",             "api-reference/pilot-to-cloud/https/map-elements/delete.html"),
    ("Obtain Wayline List",             "api-reference/pilot-to-cloud/https/waypoint-management/obtain-waypointfile-list.html"),
    ("Waypoint Obtain Temporary Credential", "api-reference/pilot-to-cloud/https/waypoint-management/obtain-temporary-credential.html"),
    ("Obtain Wayline File Download Address", "api-reference/pilot-to-cloud/https/waypoint-management/get-waypointfile-download-location.html"),
    ("Obtain Duplicated Wayline Name",  "api-reference/pilot-to-cloud/https/waypoint-management/get-duplicated-waypointfile-name.html"),
    ("Wayline File Upload Result Report", "api-reference/pilot-to-cloud/https/waypoint-management/waypointfile-upload-result-report.html"),
    ("Batch Favorites Wayline",         "api-reference/pilot-to-cloud/https/waypoint-management/collect-waypointfile-in-batch.html"),
    ("Batch Unfavorite Wayline",        "api-reference/pilot-to-cloud/https/waypoint-management/cancel-collect.html"),
    ("Media Fast Upload",               "api-reference/pilot-to-cloud/https/media-management/fast-upload.html"),
    ("Obtain Exist File Tiny Fingerprint", "api-reference/pilot-to-cloud/https/media-management/obtain-exited-tiny-fingerprint.html"),
    ("Media Obtain Temporary Credential", "api-reference/pilot-to-cloud/https/media-management/obtain-temporary-credential.html"),
    ("Media File Upload Result Report", "api-reference/pilot-to-cloud/https/media-management/mediafile-upload-result-report.html"),
    ("Group Upload Callback",           "api-reference/pilot-to-cloud/https/media-management/group-upload-callback.html"),
    ("Obtain Device Topology List",     "api-reference/pilot-to-cloud/https/situation-awareness/obtain-device-topology-list.html"),

    # Pilot-to-cloud — WebSocket
    ("Map Elements Push Message",       "api-reference/pilot-to-cloud/websocket/map-elements/message-push.html"),
    ("Situation Awareness Push Message", "api-reference/pilot-to-cloud/websocket/situation-awareness/message-push.html"),

    # Pilot-to-cloud — JSBridge
    ("JSBridge",                        "api-reference/pilot-to-cloud/jsbridge.html"),

    # Dock-to-cloud — MQTT top-level
    ("Topic Definition",                "api-reference/dock-to-cloud/mqtt/topic-definition.html"),

    # Dock-to-cloud — MQTT aircraft
    ("M30 M30T Properties",             "api-reference/dock-to-cloud/mqtt/aircraft/m30-properties.html"),
    ("M3D M3TD Properties",             "api-reference/dock-to-cloud/mqtt/aircraft/m3d-properties.html"),
    ("M4D M4TD Properties",             "api-reference/dock-to-cloud/mqtt/aircraft/m4d-properties.html"),

    # Dock-to-cloud — MQTT Dock 1  (legacy: skip unless --include-legacy)
    ("Properties",                      "api-reference/dock-to-cloud/mqtt/dock/dock1/properties.html"),
    ("Device Management",               "api-reference/dock-to-cloud/mqtt/dock/dock1/device.html"),
    ("Organization Management",         "api-reference/dock-to-cloud/mqtt/dock/dock1/organization.html"),
    ("Live Stream",                     "api-reference/dock-to-cloud/mqtt/dock/dock1/live.html"),
    ("Media Management",                "api-reference/dock-to-cloud/mqtt/dock/dock1/file.html"),
    ("Wayline Management",              "api-reference/dock-to-cloud/mqtt/dock/dock1/wayline.html"),
    ("HMS",                             "api-reference/dock-to-cloud/mqtt/dock/dock1/hms.html"),
    ("Remote Debugging",                "api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html"),
    ("Firmware Upgrade",                "api-reference/dock-to-cloud/mqtt/dock/dock1/firmware.html"),
    ("Remote Log",                      "api-reference/dock-to-cloud/mqtt/dock/dock1/log.html"),
    ("Configuration Update",            "api-reference/dock-to-cloud/mqtt/dock/dock1/config.html"),
    ("Live Flight Controls",            "api-reference/dock-to-cloud/mqtt/dock/dock1/drc.html"),
    ("AirSense",                        "api-reference/dock-to-cloud/mqtt/dock/dock1/airsense.html"),
    ("Custom Flight Area",              "api-reference/dock-to-cloud/mqtt/dock/dock1/custom-flight-area.html"),
    ("PSDK",                            "api-reference/dock-to-cloud/mqtt/dock/dock1/psdk.html"),
    ("PSDK Interconnection",            "api-reference/dock-to-cloud/mqtt/dock/dock1/psdk-transmit-custom-data.html"),
    ("ESDK Interconnection",            "api-reference/dock-to-cloud/mqtt/dock/dock1/esdk-transmit-custom-data.html"),
    ("FlySafe",                         "api-reference/dock-to-cloud/mqtt/dock/dock1/flysafe.html"),

    # Dock-to-cloud — MQTT Dock 2  (out of scope: skip unless --include-legacy)
    ("Properties",                      "api-reference/dock-to-cloud/mqtt/dock/dock2/properties.html"),
    ("Device Management",               "api-reference/dock-to-cloud/mqtt/dock/dock2/device.html"),
    ("Organization Management",         "api-reference/dock-to-cloud/mqtt/dock/dock2/organization.html"),
    ("Live Stream",                     "api-reference/dock-to-cloud/mqtt/dock/dock2/live.html"),
    ("Media Management",                "api-reference/dock-to-cloud/mqtt/dock/dock2/file.html"),
    ("Wayline Management",              "api-reference/dock-to-cloud/mqtt/dock/dock2/wayline.html"),
    ("HMS",                             "api-reference/dock-to-cloud/mqtt/dock/dock2/hms.html"),
    ("Remote Debugging",                "api-reference/dock-to-cloud/mqtt/dock/dock2/cmd.html"),
    ("Firmware Upgrade",                "api-reference/dock-to-cloud/mqtt/dock/dock2/firmware.html"),
    ("Remote Log",                      "api-reference/dock-to-cloud/mqtt/dock/dock2/log.html"),
    ("Configuration Update",            "api-reference/dock-to-cloud/mqtt/dock/dock2/config.html"),
    ("Live Flight Controls",            "api-reference/dock-to-cloud/mqtt/dock/dock2/drc.html"),
    ("AirSense",                        "api-reference/dock-to-cloud/mqtt/dock/dock2/airsense.html"),
    ("Custom Flight Area",              "api-reference/dock-to-cloud/mqtt/dock/dock2/custom-flight-area.html"),
    ("PSDK",                            "api-reference/dock-to-cloud/mqtt/dock/dock2/psdk.html"),
    ("PSDK Interconnection",            "api-reference/dock-to-cloud/mqtt/dock/dock2/psdk-transmit-custom-data.html"),
    ("ESDK Interconnection",            "api-reference/dock-to-cloud/mqtt/dock/dock2/esdk-transmit-custom-data.html"),
    ("FlySafe",                         "api-reference/dock-to-cloud/mqtt/dock/dock2/flysafe.html"),
    ("Remote Control",                  "api-reference/dock-to-cloud/mqtt/dock/dock2/remote-control.html"),

    # Dock-to-cloud — MQTT Dock 3  (in scope)
    ("Device Properties",               "api-reference/dock-to-cloud/mqtt/dock/dock3/properties.html"),
    ("Device Management",               "api-reference/dock-to-cloud/mqtt/dock/dock3/device.html"),
    ("Organization Management",         "api-reference/dock-to-cloud/mqtt/dock/dock3/organization.html"),
    ("Live Stream",                     "api-reference/dock-to-cloud/mqtt/dock/dock3/live.html"),
    ("Media Management",                "api-reference/dock-to-cloud/mqtt/dock/dock3/media.html"),
    ("Wayline Management",              "api-reference/dock-to-cloud/mqtt/dock/dock3/wayline.html"),
    ("HMS",                             "api-reference/dock-to-cloud/mqtt/dock/dock3/hms.html"),
    ("Remote Debugging",                "api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html"),
    ("Firmware Upgrade",                "api-reference/dock-to-cloud/mqtt/dock/dock3/firmware.html"),
    ("Remote Log",                      "api-reference/dock-to-cloud/mqtt/dock/dock3/log.html"),
    ("Configuration Update",            "api-reference/dock-to-cloud/mqtt/dock/dock3/config.html"),
    ("Live Flight Controls",            "api-reference/dock-to-cloud/mqtt/dock/dock3/drc.html"),
    ("Custom Flight Area",              "api-reference/dock-to-cloud/mqtt/dock/dock3/custom-fly-region.html"),
    ("PSDK",                            "api-reference/dock-to-cloud/mqtt/dock/dock3/psdk.html"),
    ("PSDK Interconnection",            "api-reference/dock-to-cloud/mqtt/dock/dock3/psdk-transmit-custom-data.html"),
    ("ESDK Interconnection",            "api-reference/dock-to-cloud/mqtt/dock/dock3/esdk-transmit-custom-data.html"),
    ("FlySafe",                         "api-reference/dock-to-cloud/mqtt/dock/dock3/flysafe.html"),
    ("AirSense",                        "api-reference/dock-to-cloud/mqtt/dock/dock3/airsense.html"),
    ("Remote Control",                  "api-reference/dock-to-cloud/mqtt/dock/dock3/remote-control.html"),

    # Error codes + FAQ (referenced from left nav; useful for HMS-Codes)
    ("Error Code",                      "error-code.html"),
    ("FAQ",                             "faq.html"),
]

BASE_URL = "https://developer.dji.com/doc/cloud-api-tutorial/en/"


# ---------------------------------------------------------------------------
# Naming — derive `DJI_CloudAPI-<family>-<page>.txt` from URL + label.
#
# The existing files don't follow one perfectly consistent rule (some use
# underscore separators, some hyphens), so this picks a reasonable default
# and trusts the dupe check below to catch variants we'd otherwise double-write.
# ---------------------------------------------------------------------------

# (path_substring, filename_prefix_including_separator, family_token)
FAMILY_MAP: list[tuple[str, str, str]] = [
    # Dock-to-cloud — aircraft properties (per-drone)
    ("/dock-to-cloud/mqtt/aircraft/m4d-properties",      "DJI_CloudAPI-", "DockToCloud_Matrice_4D_4DT"),
    ("/dock-to-cloud/mqtt/aircraft/m3d-properties",      "DJI_CloudAPI_", "M3D_M3DT"),
    ("/dock-to-cloud/mqtt/aircraft/m30-properties",      "DJI_CloudAPI_", "M30_M30T"),
    # Dock-to-cloud — dock families
    ("/dock-to-cloud/mqtt/dock/dock3/",                  "DJI_CloudAPI-", "Dock3"),
    ("/dock-to-cloud/mqtt/dock/dock2/",                  "DJI_CloudAPI-", "Dock2"),
    ("/dock-to-cloud/mqtt/dock/dock1/",                  "DJI_CloudAPI-", "Dock1"),
    # Dock-to-cloud top-level
    ("/dock-to-cloud/mqtt/topic-definition",             "DJI_CloudAPI-", "DockToCloud"),
    # Pilot-to-cloud — devices
    ("/pilot-to-cloud/mqtt/dji-rc-plus-2/",              "DJI_CloudAPI_", "RC-Plus-2-Enterprise"),
    ("/pilot-to-cloud/mqtt/rc-pro/",                     "DJI_CloudAPI_", "RC-Pro-Enterprise"),
    ("/pilot-to-cloud/mqtt/m3-series/",                  "DJI_CloudAPI_", "Mavic3-Enterprise"),
    ("/pilot-to-cloud/mqtt/m4-series/",                  "DJI_CloudAPI_", "Matrice4-Enterprise"),
    ("/pilot-to-cloud/mqtt/matrice-400/",                "DJI_CloudAPI_", "Matrice-400"),
    ("/pilot-to-cloud/mqtt/others/aircraft/",            "DJI_CloudAPI_", "Aircraft"),
    ("/pilot-to-cloud/mqtt/others/rc/",                  "DJI_CloudAPI_", "RC"),
    # Pilot-to-cloud — HTTPS / WebSocket / JSBridge
    ("/pilot-to-cloud/mqtt/topic-definition",            "DJI_CloudAPI-", "PilotToCloud"),
    ("/pilot-to-cloud/https/map-elements/",              "DJI_CloudAPI_", "Pilot-HTTPS-MapElements"),
    ("/pilot-to-cloud/https/waypoint-management/",       "DJI_CloudAPI_", "Pilot-HTTPS-Waypoint"),
    ("/pilot-to-cloud/https/media-management/",          "DJI_CloudAPI_", "Pilot-HTTPS-Media"),
    ("/pilot-to-cloud/https/situation-awareness/",       "DJI_CloudAPI_", "Pilot-HTTPS-SituationAwareness"),
    ("/pilot-to-cloud/websocket/",                       "DJI_CloudAPI_", "Pilot-WebSocket"),
    ("/pilot-to-cloud/jsbridge",                         "DJI_CloudAPI_", "Pilot"),
    # DJI WPML
    ("/dji-wpml/",                                       "DJI_CloudAPI_", "WPML"),
    # Fallback tail pages (error code / faq)
    ("error-code",                                       "DJI_CloudAPI-", "HMS-Codes"),
    ("faq",                                              "DJI_CloudAPI_", "FAQ"),
]

# Special-case: specific pages whose user-facing file already uses a different
# tail than the page label. Key is the URL suffix we match on.
TAIL_OVERRIDES: dict[str, str] = {
    "dock-to-cloud/mqtt/dock/dock3/device.html":    "DeviceManagement",
    "dock-to-cloud/mqtt/dock/dock3/properties.html": "DeviceProperties",
    "dock-to-cloud/mqtt/dock/dock3/live.html":      "LiveStream",
    "dock-to-cloud/mqtt/dock/dock3/wayline.html":   "WaylineManagement",
    "dock-to-cloud/mqtt/dock/dock3/hms.html":       "HMS",
    "dock-to-cloud/mqtt/dock/dock3/flysafe.html":   "FlySafe",
    "dock-to-cloud/mqtt/topic-definition.html":     "TopicDefinitions",
    "dock-to-cloud/mqtt/aircraft/m30-properties.html": "Properties",
    "dock-to-cloud/mqtt/aircraft/m3d-properties.html": "Properties",
    "dock-to-cloud/mqtt/aircraft/m4d-properties.html": "DeviceProperties",  # match existing
    "error-code.html":                              "",          # prefix carries the name
    "faq.html":                                     "",          # prefix carries the name
    "pilot-to-cloud/jsbridge.html":                 "JSBridge",
    # WPML: match existing file names that drop the ".wpml"/".kml" part.
    "dji-wpml/waylines-wpml.html":                  "Waylines",
    "dji-wpml/template-kml.html":                   "Template-KML",
    # Collapse redundant "Waypoint-Waypoint-" / "Media-Media-" labels (tail only).
    "pilot-to-cloud/https/waypoint-management/obtain-temporary-credential.html": "Obtain-Temporary-Credential",
    "pilot-to-cloud/https/waypoint-management/waypointfile-upload-result-report.html": "File-Upload-Result-Report",
    "pilot-to-cloud/https/media-management/fast-upload.html":  "Fast-Upload",
    "pilot-to-cloud/https/media-management/obtain-temporary-credential.html": "Obtain-Temporary-Credential",
    "pilot-to-cloud/https/media-management/mediafile-upload-result-report.html": "File-Upload-Result-Report",
}

# URL substrings we skip unless --include-legacy
LEGACY_SUBSTRS = ("/dock/dock1/", "/dock/dock2/")


@dataclass
class Page:
    label: str
    url: str               # absolute
    path: str              # relative
    filename: str          # proposed .txt filename
    status: str = ""       # "skipped-legacy" | "dupe" | "new" | "forced" | "error"
    dupe_of: str | None = None
    error: str | None = None
    chars: int = 0


def normalize_slug(s: str) -> str:
    """Lowercase + strip everything that isn't alphanumeric."""
    return re.sub(r"[^a-z0-9]", "", s.lower())


def propose_filename(label: str, path: str) -> str:
    prefix, family = "DJI_CloudAPI_", "Misc"
    for substr, pfx, fam in FAMILY_MAP:
        if substr in ("/" + path) or substr == path.split(".html", 1)[0]:
            prefix, family = pfx, fam
            break
    # Tail: prefer override (match on exact path or suffix), else sidebar label.
    tail: str | None = TAIL_OVERRIDES.get(path)
    if tail is None:
        for key, val in TAIL_OVERRIDES.items():
            if path.endswith(key):
                tail = val
                break
    if tail is None:
        tail = re.sub(r"[^A-Za-z0-9]+", "-", label).strip("-")
    # Join: <prefix><family>[-<tail>].txt, but drop separator if tail empty.
    if tail:
        return f"{prefix}{family}-{tail}.txt"
    return f"{prefix}{family}.txt"


def build_plan(include_legacy: bool, existing: set[str]) -> list[Page]:
    pages: list[Page] = []
    seen_fn: dict[str, str] = {}
    for label, path in URLS:
        p = Page(
            label=label,
            path=path,
            url=BASE_URL + path,
            filename=propose_filename(label, path),
        )
        if (not include_legacy) and any(s in path for s in LEGACY_SUBSTRS):
            p.status = "skipped-legacy"
            pages.append(p)
            continue
        # Dedupe against files already in DJI_Cloud/
        norm = normalize_slug(os.path.splitext(p.filename)[0])
        if norm in existing:
            p.status = "dupe"
            p.dupe_of = existing[norm]
            pages.append(p)
            continue
        # Dedupe within this plan (two URLs mapping to same filename).
        if p.filename in seen_fn:
            p.status = "dupe"
            p.dupe_of = seen_fn[p.filename]
            pages.append(p)
            continue
        seen_fn[p.filename] = p.url
        p.status = "new"
        pages.append(p)
    return pages


def load_existing_index(docs_dir: Path) -> dict[str, str]:
    """Map normalized-slug -> actual filename for all existing .txt files."""
    index: dict[str, str] = {}
    for p in docs_dir.glob("*.txt"):
        index[normalize_slug(p.stem)] = p.name
    return index


# ---------------------------------------------------------------------------
# Scraping
# ---------------------------------------------------------------------------

EXTRACT_JS = r"""
() => {
  const el = document.querySelector('.theme-default-content');
  if (!el) return { ok: false, reason: 'no-content-container' };
  // Drop the "open in new window" screen-reader text on external-link icons
  // so it doesn't appear mid-sentence after link text.
  el.querySelectorAll('.external-link-icon, .icon.outbound').forEach(n => n.remove());
  return { ok: true, text: el.innerText };
}
"""


def scrape(pages: list[Page], out_dir: Path, force: bool, *, wait_ms: int = 1500) -> None:
    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except ImportError:
        sys.exit(
            "error: playwright is not installed.\n"
            "  pip install playwright && playwright install chromium"
        )

    out_dir.mkdir(parents=True, exist_ok=True)
    targets = [p for p in pages if p.status == "new" or (force and p.status == "dupe")]
    if not targets:
        print("Nothing to scrape.")
        return

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        ctx = browser.new_context()
        page = ctx.new_page()
        try:
            for i, p in enumerate(targets, 1):
                print(f"[{i}/{len(targets)}] {p.url}")
                try:
                    page.goto(p.url, wait_until="domcontentloaded", timeout=30000)
                    # Give VuePress a beat to hydrate and render the markdown.
                    page.wait_for_selector(".theme-default-content", timeout=15000)
                    page.wait_for_timeout(wait_ms)
                    result = page.evaluate(EXTRACT_JS)
                    if not result or not result.get("ok"):
                        p.status = "error"
                        p.error = (result or {}).get("reason", "unknown")
                        print(f"  ! {p.error}")
                        continue
                    text = collapse_whitespace(result["text"])
                    p.chars = len(text)
                    (out_dir / p.filename).write_text(text, encoding="utf-8")
                    if p.status == "dupe":
                        p.status = "forced"
                    print(f"  -> {p.filename} ({p.chars} chars)")
                except Exception as e:
                    p.status = "error"
                    p.error = repr(e)
                    print(f"  ! {e}")
        finally:
            ctx.close()
            browser.close()


def collapse_whitespace(text: str) -> str:
    # Collapse runs of spaces/tabs (but not newlines); collapse 3+ newlines to 2.
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    lines = [line.rstrip() for line in text.splitlines()]
    return "\n".join(lines).strip() + "\n"


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def print_plan(pages: list[Page]) -> None:
    groups: dict[str, list[Page]] = {}
    for p in pages:
        groups.setdefault(p.status, []).append(p)
    for status in ("new", "dupe", "skipped-legacy", "error"):
        items = groups.get(status, [])
        if not items:
            continue
        print(f"\n=== {status} ({len(items)}) ===")
        for p in items:
            extra = ""
            if p.dupe_of:
                extra = f"  [existing: {p.dupe_of}]"
            if p.error:
                extra = f"  [error: {p.error}]"
            print(f"  {p.filename:<60} {p.path}{extra}")


def write_manifest(pages: list[Page], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    data = [
        {
            "label": p.label,
            "url": p.url,
            "path": p.path,
            "filename": p.filename,
            "status": p.status,
            "dupe_of": p.dupe_of,
            "error": p.error,
            "chars": p.chars,
        }
        for p in pages
    ]
    (out_dir / "_manifest.json").write_text(
        json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true", help="print the plan and exit without scraping")
    ap.add_argument("--include-legacy", action="store_true", help="include Dock 1 / Dock 2 pages")
    ap.add_argument("--force", action="store_true", help="re-scrape even pages that duplicate an existing .txt")
    ap.add_argument("--out", default="_scraped", help="staging subdir for new pages (default: _scraped)")
    args = ap.parse_args()

    docs_dir = Path(__file__).resolve().parent
    out_dir = docs_dir / args.out

    existing = load_existing_index(docs_dir)
    pages = build_plan(include_legacy=args.include_legacy, existing=existing)

    print_plan(pages)
    if args.list:
        return 0

    scrape(pages, out_dir, force=args.force)
    write_manifest(pages, out_dir)

    print(f"\nStaging dir: {out_dir}")
    print("Review files, then move the ones you want into DJI_Cloud/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
