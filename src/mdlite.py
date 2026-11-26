"""Bağımlılıksız küçük Markdown → HTML dönüştürücü (dogen.es blog için).

Desteklenen: #/##/### başlık (id'li), paragraf, - / 1. liste, > alıntı (> **Not:** ile kutu),
| tablo |, **kalın**, *italik*, `kod`, [bağlantı](url), --- ayırıcı.
"""
import html
import re
import unicodedata

TR_MAP = str.maketrans("çğıöşüÇĞİÖŞÜâîûÂÎÛ", "cgiosuCGIOSUaiuAIU")


def slugify(text):
    t = re.sub(r"<[^>]+>", "", text).translate(TR_MAP)
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t or "bolum"


def inline(text):
    codes = []

    def keep(m):
        codes.append("<code>" + html.escape(m.group(1)) + "</code>")
        return "\x00%d\x00" % (len(codes) - 1)

    text = re.sub(r"`([^`]+)`", keep, text)
    text = html.escape(text, quote=False)

    def link(m):
        label, url = m.group(1), m.group(2).strip()
        ext = url.startswith("http") and "dogen.es" not in url
        attrs = ' target="_blank" rel="noopener"' if ext else ""
        return '<a href="%s"%s>%s</a>' % (html.escape(url, quote=True), attrs, label)

    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], text)
    return text


def convert(md):
    """Markdown → (html, başlıklar[(seviye, id, metin)])"""
    lines = md.replace("\r\n", "\n").split("\n")
    out, heads, used = [], [], set()
    i = 0

    def para(buf):
        if buf:
            out.append("<p>" + inline(" ".join(s.strip() for s in buf)) + "</p>")

    buf = []
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if not s:
            para(buf); buf = []; i += 1; continue
        m = re.match(r"^(#{2,4})\s+(.*)$", s)
        if m:
            para(buf); buf = []
            lvl, txt = len(m.group(1)), m.group(2).strip()
            hid = slugify(txt)
            base, n = hid, 2
            while hid in used:
                hid = "%s-%d" % (base, n); n += 1
            used.add(hid)
            heads.append((lvl, hid, re.sub(r"[*`]", "", txt)))
            out.append('<h%d id="%s">%s</h%d>' % (lvl, hid, inline(txt), lvl))
            i += 1; continue
        if s == "---":
            para(buf); buf = []; out.append("<hr>"); i += 1; continue
        if s.startswith(">"):
            para(buf); buf = []
            q = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                q.append(lines[i].strip()[1:].strip()); i += 1
            body = " ".join(x for x in q if x)
            cls = ' class="note"' if re.match(r"^\*\*[^*]+:\*\*", body) else ""
            out.append("<blockquote%s><p>%s</p></blockquote>" % (cls, inline(body)))
            continue
        if s.startswith("|"):
            para(buf); buf = []
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            head = rows[0]
            body = [r for r in rows[1:] if not all(re.match(r"^:?-{2,}:?$", c) for c in r)]
            t = ['<div class="table"><table><thead><tr>']
            t += ["<th>%s</th>" % inline(c) for c in head]
            t.append("</tr></thead><tbody>")
            for r in body:
                t.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in r) + "</tr>")
            t.append("</tbody></table></div>")
            out.append("".join(t))
            continue
        lm = re.match(r"^(-|\d+\.)\s+(.*)$", s)
        if lm:
            para(buf); buf = []
            tag = "ol" if lm.group(1)[0].isdigit() else "ul"
            items = []
            while i < len(lines):
                cur = lines[i].strip()
                mm = re.match(r"^(-|\d+\.)\s+(.*)$", cur)
                if mm:
                    items.append(mm.group(2)); i += 1
                elif cur and lines[i].startswith(("  ", "\t")) and items:
                    items[-1] += " " + cur; i += 1
                else:
                    break
            out.append("<%s>%s</%s>" % (tag, "".join("<li>%s</li>" % inline(x) for x in items), tag))
            continue
        buf.append(ln); i += 1
    para(buf)
    return "\n".join(out), heads


def plain(md):
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)
    t = re.sub(r"[#>*`|_-]", " ", t)
    return re.sub(r"\s+", " ", t).strip()
