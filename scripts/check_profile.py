"""Validate the README's local resources using only Python's standard library."""

from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
SVG = "{http://www.w3.org/2000/svg}svg"


class ProfileAssets(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "img" and not (attributes.get("alt") or "").strip():
            self.errors.append(f"Image missing alternative text: {attributes.get('src')}")
        for name in ("href", "src"):
            if attributes.get(name):
                self.links.append(attributes[name])
        if tag == "source" and attributes.get("srcset"):
            for candidate in attributes["srcset"].split(","):
                fields = candidate.split()
                if fields:
                    self.links.append(fields[0])


def main():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    profile = ProfileAssets()
    profile.feed(readme)
    # Capture inline Markdown links and images alongside the HTML components.
    for match in re.finditer(r"\[[^\]\n]*\]\(\s*(?:<([^>]+)>|([^\s)]+))", readme):
        profile.links.append(match[1] or match[2])

    for link in sorted(set(profile.links)):
        url = urlsplit(link)
        if url.scheme or url.netloc or not url.path:
            continue
        path = (ROOT / unquote(url.path)).resolve()
        if ROOT not in (path, *path.parents) or not path.exists():
            profile.errors.append(f"Invalid local reference: {link}")

    for path in sorted((ROOT / "assets").rglob("*.svg")):
        try:
            if ElementTree.parse(path).getroot().tag != SVG:
                profile.errors.append(f"Expected SVG root: {path.relative_to(ROOT)}")
        except ElementTree.ParseError as error:
            profile.errors.append(f"{path.relative_to(ROOT)}: {error}")

    if profile.errors:
        print("\n".join(profile.errors), file=sys.stderr)
        return 1
    print("Profile references and SVG assets are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
