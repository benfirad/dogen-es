#!/usr/bin/env python3
"""index.template.html + logo.svg -> index.html (logo inline, currentColor ile renklenir)."""
import re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
logo = (root / "logo.svg").read_text()
logo = re.sub(r"<\?xml.*?\?>", "", logo).strip()
logo = re.sub(r"<svg\b", '<svg aria-hidden="true" focusable="false"', logo, count=1)
logo = logo.replace('role="img" ', "").replace(' aria-label="dogen"', "")
tpl = (root / "src" / "index.template.html").read_text()
(root / "index.html").write_text(tpl.replace("<!--LOGO-->", logo))
print("index.html built", len(tpl.replace("<!--LOGO-->", logo)))
