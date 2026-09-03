#!/usr/bin/env python3
"""Generate the standalone index.html served by GitHub Pages.

    python3 build_page.py

`claude-code-vs-cowork.html` is authored in **Artifact page form**: it starts at
`<title>` and carries no `<!doctype>`, `<html>`, `<head>` or `<body>` of its own,
because the claude.ai Artifact publisher supplies that skeleton at publish time.

Served directly from a static host, that same file would render in *quirks mode*. It is
built to survive that (`*{box-sizing:border-box}`, no reliance on standards-mode
defaults), but shipping a real document is better than surviving a bad one. So this
script wraps the source once and writes `index.html`.

Keeping the wrap in a script rather than maintaining a second copy by hand is the whole
point: there is exactly one source of truth for the content, and the two outputs cannot
drift apart.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Every (source, output) pair this site publishes. Add a row to add a page; the loop
# below is the only thing that needs to know how many there are.
PAGES = [
    (Path("claude-code-vs-cowork.html"), Path("index.html")),
    (Path("copilot/copilot-vs-claude.html"), Path("copilot/index.html")),
]

# Pulled out of the source so the tab title and the page title can never disagree.
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)

DESCRIPTIONS = {
    "Code, Cowork, and Fabric":
        "A costed, first-party-sourced comparison of Claude Code and Claude Cowork on "
        "seats, security, retention and auditability, plus MCP-vs-CLI routes into "
        "Microsoft Fabric.",
    "Copilot or Claude Code":
        "Which agent sits in which chair, which budget each one spends, and whether "
        "GitHub Copilot reaches Microsoft Fabric from VS Code. Cited, dated, first-party.",
}


def build_one(SRC: Path, OUT: Path) -> int:
    if not SRC.exists():
        print(f"error: {SRC} not found", file=sys.stderr)
        return 2

    body = SRC.read_text(encoding="utf-8")

    m = TITLE_RE.search(body)
    if not m:
        print(f"error: no <title> found in {SRC}", file=sys.stderr)
        return 2
    title = m.group(1).strip()

    # The source's own <title> moves into the real <head>; leaving a duplicate in the
    # body is valid but untidy, so strip it from the copied content.
    content = TITLE_RE.sub("", body, count=1).lstrip("\n")

    html = (
        '<!doctype html>\n'
        '<html lang="en">\n'
        '<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<title>{title}</title>\n'
        f'<meta name="description" content="{DESCRIPTIONS.get(title, "")}">\n'
        # The palette defines both themes; tell the browser so form controls and
        # scrollbars match rather than staying stubbornly light.
        '<meta name="color-scheme" content="light dark">\n'
        '</head>\n'
        '<body>\n'
        f'{content}'
        '\n</body>\n'
        '</html>\n'
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT} ({len(html):,} bytes) — title {title!r}")
    return 0


def build() -> int:
    rc = 0
    for src, out in PAGES:
        rc |= build_one(src, out)
    print("  reminder: run check_page.py against each SOURCE, not the generated index files;")
    print("  the wrapper deliberately adds the tags the source-level check forbids.")
    return rc


if __name__ == "__main__":
    sys.exit(build())
