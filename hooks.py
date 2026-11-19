"""MkDocs hook: publish the Player Form as a downloadable raw .md file.

MkDocs turns every .md under docs/ into an HTML page and never copies the
source, so this copies docs/players/form.md to <site>/players/player-form.md
after each build. The download button block on the page (between the
download-start/end markers) is stripped from the copy.
"""

import re
from pathlib import Path

SOURCE = "players/form.md"
TARGET = "players/player-form.md"
MARKERS = re.compile(r"<!-- download-start -->.*?<!-- download-end -->\n*", re.DOTALL)


def on_post_build(config, **kwargs):
    text = (Path(config["docs_dir"]) / SOURCE).read_text(encoding="utf-8")
    text = MARKERS.sub("", text)
    out = Path(config["site_dir"]) / TARGET
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
