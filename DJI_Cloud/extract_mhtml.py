"""Extract primary text content from MHTML files into .txt files for Claude Code ingestion."""

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


def main():
    docs_dir = os.path.dirname(os.path.abspath(__file__))
    mhtml_files = sorted(glob.glob(os.path.join(docs_dir, "*.mhtml")))

    if not mhtml_files:
        print("No .mhtml files found in", docs_dir)
        return

    for mhtml_path in mhtml_files:
        basename = os.path.splitext(os.path.basename(mhtml_path))[0]
        txt_path = os.path.join(docs_dir, f"{basename}.txt")

        print(f"Processing: {os.path.basename(mhtml_path)}")
        html = extract_html_from_mhtml(mhtml_path)
        text = html_to_text(html)
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"  -> {os.path.basename(txt_path)} ({len(text)} chars)")

    print("Done.")


if __name__ == "__main__":
    main()
