#!/usr/bin/env python3
"""
Build script for the End2End Estate site.

Takes site.html (the editable source, with __TOKEN__ placeholders for images)
and produces dist/index.html with every image inlined as a data URI, so the
whole site is one self contained file that can be dropped on any host.

Run:  python3 build.py
"""
import base64
import os
import pathlib
import re

ROOT = pathlib.Path(__file__).parent

ASSETS = {
    "__LOGO_DARK__": ("logo_lockup.png", "image/png"),
    "__LOGO_LIGHT__": ("logo_lockup_light.png", "image/png"),
    "__FAVICON__": ("favicon.png", "image/png"),
}


def main():
    html = (ROOT / "site.html").read_text()

    for token, (filename, mime) in ASSETS.items():
        if token not in html:
            print("  warning: %s not found in site.html" % token)
            continue
        path = ROOT / filename
        if path.exists():
            encoded = base64.b64encode(path.read_bytes()).decode()
        else:
            # Binary assets are stored in the repo as base64 text (see assets/).
            fallback = ROOT / "assets" / (filename + ".b64")
            if not fallback.exists():
                raise SystemExit("missing asset: %s (and no %s)" % (filename, fallback))
            encoded = fallback.read_text().strip()
        html = html.replace(token, "data:%s;base64,%s" % (mime, encoded))

    leftover = re.findall(r"__[A-Z_]+__", html)
    if leftover:
        raise SystemExit("unsubstituted tokens remain: %s" % sorted(set(leftover)))

    if "—" in html:
        raise SystemExit("em dash found in output. The owner does not want em dashes anywhere.")

    if "REPLACE-WITH-YOUR-EMAIL" in html:
        print("  warning: contact form recipient is still the placeholder address")

    out = ROOT / "index.html"
    out.write_text(html)
    print("built %s (%d KB)" % (out, out.stat().st_size / 1024))


if __name__ == "__main__":
    main()
