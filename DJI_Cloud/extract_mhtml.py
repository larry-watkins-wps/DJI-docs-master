"""Extract primary text content from MHTML files into .txt files for Claude Code ingestion.

Running this script does two passes:

1. For every *.mhtml in this directory, extract text and write a trimmed .txt
   (overwriting an existing .txt of the same base name).
2. For every remaining *.txt in this directory (existing extractions with no
   paired .mhtml), trim the same top/bottom page-chrome in place.

"Trimming" means keeping only the lines strictly between the first and last
line ending with `Github Edit open in new window`. Those markers bracket the
actual doc content in the live DJI docs site UI and are emitted on every page.
Dropping them removes ~380 lines of repeated left-nav header and ~5-15 lines
of footer per file while leaving every byte of documentation content intact.

Files with zero or one marker are reported as warnings and left untouched so
the human can triage them.
"""

import email
import email.policy
import glob
import os
import quopri
import re
from html.parser import HTMLParser


class TextExtractor(HTMLParser):
    """Extract visible text from HTML, skipping scripts/styles."""

    SKIP_TAGS = {"script", "style", "noscript", "svg", "head"}
    BLOCK_TAGS = {
        "p", "div", "h1", "h2", "h3", "h4", "h5", "h6",
        "li", "tr", "th", "td", "br", "hr", "section", "article",
        "header", "footer", "nav", "blockquote", "pre", "table",
        "thead", "tbody", "tfoot", "dt", "dd", "figcaption",
    }

    def __init__(self):
        super().__init__()
        self.result = []
        self._skip_depth = 0
        self._tag_stack = []

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        self._tag_stack.append(tag)
        if tag in self.SKIP_TAGS:
            self._skip_depth += 1
        if tag in self.BLOCK_TAGS and self._skip_depth == 0:
            self.result.append("\n")

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in self.SKIP_TAGS:
            self._skip_depth = max(0, self._skip_depth - 1)
        if tag in self.BLOCK_TAGS and self._skip_depth == 0:
            self.result.append("\n")
        if self._tag_stack and self._tag_stack[-1] == tag:
            self._tag_stack.pop()

    def handle_data(self, data):
        if self._skip_depth == 0:
            self.result.append(data)

    def handle_entityref(self, name):
        if self._skip_depth == 0:
            from html import unescape
            self.result.append(unescape(f"&{name};"))

    def handle_charref(self, name):
        if self._skip_depth == 0:
            from html import unescape
            self.result.append(unescape(f"&#{name};"))

    def get_text(self):
        text = "".join(self.result)
        # Collapse runs of whitespace on the same line
        text = re.sub(r"[^\S\n]+", " ", text)
        # Collapse 3+ newlines to 2
        text = re.sub(r"\n{3,}", "\n\n", text)
        # Strip leading/trailing whitespace per line
        lines = [line.strip() for line in text.splitlines()]
        return "\n".join(lines).strip() + "\n"


def extract_html_from_mhtml(mhtml_path: str) -> str:
    """Parse an MHTML file and return the decoded HTML content."""
    with open(mhtml_path, "rb") as f:
        msg = email.message_from_binary_file(f, policy=email.policy.default)

    # Walk MIME parts, find the text/html one
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/html":
                payload = part.get_payload(decode=True)
                charset = part.get_content_charset() or "utf-8"
                return payload.decode(charset, errors="replace")

    # Non-multipart fallback
    payload = msg.get_payload(decode=True)
    charset = msg.get_content_charset() or "utf-8"
    return payload.decode(charset, errors="replace")


def html_to_text(html: str) -> str:
    """Convert HTML string to clean plain text."""
    extractor = TextExtractor()
    extractor.feed(html)
    return extractor.get_text()


MARKER_RE = re.compile(r"Github Edit open in new window\s*$")


def trim_boilerplate(text: str):
    """Trim top page-chrome and bottom footer using the 'Github Edit open in new window' marker.

    Returns (new_text, marker_count). Caller checks marker_count:
      - >= 2 : trimmed, new_text is the content between first and last marker
      - <  2 : untrimmed, new_text == text. Caller should warn and skip writing.
    """
    lines = text.splitlines()
    marker_indices = [i for i, line in enumerate(lines) if MARKER_RE.search(line)]
    if len(marker_indices) < 2:
        return text, len(marker_indices)
    first = marker_indices[0]
    last = marker_indices[-1]
    kept = lines[first + 1 : last]
    while kept and not kept[0].strip():
        kept.pop(0)
    while kept and not kept[-1].strip():
        kept.pop()
    return "\n".join(kept) + "\n", len(marker_indices)


def main():
    docs_dir = os.path.dirname(os.path.abspath(__file__))
    warnings = []

    # Pass 1: extract every .mhtml -> trimmed .txt (overwriting if present).
    mhtml_files = sorted(glob.glob(os.path.join(docs_dir, "*.mhtml")))
    extracted_basenames = set()
    for mhtml_path in mhtml_files:
        basename = os.path.splitext(os.path.basename(mhtml_path))[0]
        extracted_basenames.add(basename)
        txt_path = os.path.join(docs_dir, f"{basename}.txt")

        print(f"Extracting: {os.path.basename(mhtml_path)}")
        html = extract_html_from_mhtml(mhtml_path)
        raw_text = html_to_text(html)
        trimmed, marker_count = trim_boilerplate(raw_text)
        if marker_count < 2:
            warnings.append(
                f"{os.path.basename(mhtml_path)}: found {marker_count} 'Github Edit...' marker(s); "
                f"writing untrimmed .txt ({len(raw_text)} chars)"
            )
            payload = raw_text
        else:
            payload = trimmed
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(payload)
        print(f"  -> {os.path.basename(txt_path)} ({len(payload)} chars)")

    # Pass 2: trim every other .txt in place (existing extractions without a paired .mhtml).
    all_txts = sorted(glob.glob(os.path.join(docs_dir, "*.txt")))
    for txt_path in all_txts:
        basename = os.path.splitext(os.path.basename(txt_path))[0]
        if basename in extracted_basenames:
            continue  # already written in pass 1
        with open(txt_path, "r", encoding="utf-8") as f:
            original = f.read()
        trimmed, marker_count = trim_boilerplate(original)
        if marker_count < 2:
            warnings.append(
                f"{os.path.basename(txt_path)}: found {marker_count} 'Github Edit...' marker(s); left untouched"
            )
            continue
        if trimmed != original:
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(trimmed)
            print(f"Trimmed: {os.path.basename(txt_path)} ({len(original)} -> {len(trimmed)} chars)")
        else:
            print(f"No change: {os.path.basename(txt_path)}")

    if warnings:
        print("\n=== Warnings ===")
        for w in warnings:
            print(f"  {w}")
    else:
        print("\nNo warnings.")
    print("Done.")


if __name__ == "__main__":
    main()
