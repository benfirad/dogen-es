#!/usr/bin/env python3
"""dogen.es site üreticisi.

src/index.template.html + logo.svg + app.js(ES sözlüğü) + content/blog/*.md →
  index.html (TR), es/index.html (ES), blog/, blog/<slug>/, blog/feed.xml,
  sitemap.xml, robots.txt, 404.html

Kullanım:  python3 src/build.py
"""
import datetime as dt
import html
import json
import math
import pathlib
import re
import subprocess
import sys
from urllib.parse import quote

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import mdlite  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://dogen.es"
WA = "https://wa.me/34666104496"
PHONE = "+34666104496"
AUTHOR = "Fırat Daşdöğen"
FONT = '<link rel="preconnect" href="https://fonts.googleapis.com" />\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n  <link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400..700;1,400..600&display=swap" rel="stylesheet" />'
AYLAR = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]

e = lambda s: html.escape(str(s), quote=True)


def tr_date(d):
    return "%d %s %d" % (d.day, AYLAR[d.month - 1], d.year)


def logo_svg():
    logo = (ROOT / "logo.svg").read_text()
    logo = re.sub(r"<\?xml.*?\?>", "", logo).strip()
    logo = re.sub(r"<svg\b", '<svg aria-hidden="true" focusable="false"', logo, count=1)
    return logo.replace('role="img" ', "").replace(' aria-label="dogen"', "")


def es_dict():
    js = (ROOT / "app.js").read_text()
    block = js[js.index("var ES = {"): js.index("\n  };", js.index("var ES = {"))]
    d = {}
    for k, v in re.findall(r'(\w+):\s*"((?:[^"\\]|\\.)*)"', block):
        d[k] = json.loads('"' + v + '"')
    return d


def git_date(*paths):
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", *paths], cwd=ROOT,
                             capture_output=True, text=True, timeout=10).stdout.strip()
        dirty = subprocess.run(["git", "status", "--porcelain", "--", *paths], cwd=ROOT,
                               capture_output=True, text=True, timeout=10).stdout.strip()
        if out and not dirty:
            return out
    except Exception:
        pass
    return dt.date.today().isoformat()


def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + "</script>"


# ---------------------------------------------------------------- blog
def load_posts(folder="content/blog"):
    posts = []
    for p in sorted((ROOT / folder).glob("*.md")):
        raw = p.read_text()
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
        if not m:
            raise SystemExit("frontmatter yok: %s" % p)
        meta = {}
        for ln in m.group(1).splitlines():
            if ":" in ln:
                k, v = ln.split(":", 1)
                meta[k.strip()] = v.strip()
        body = m.group(2).strip()
        for req in ("title", "description", "date"):
            if not meta.get(req):
                raise SystemExit("%s: '%s' alanı eksik" % (p.name, req))
        if meta.get("draft", "").lower() in ("true", "yes", "1"):
            continue
        slug = meta.get("slug") or p.stem
        date = dt.date.fromisoformat(meta["date"])
        updated = dt.date.fromisoformat(meta.get("updated") or meta["date"])
        body_html, heads = mdlite.convert(body)
        words = len(mdlite.plain(body).split())
        posts.append(dict(slug=slug, title=meta["title"], description=meta["description"], date=date,
                          updated=max(updated, date), tags=[t.strip() for t in meta.get("tags", "").split(",") if t.strip()],
                          html=body_html, heads=heads, minutes=max(2, math.ceil(words / 200)), words=words,
                          url="%s/blog/%s/" % (SITE, slug), path="/blog/%s/" % slug))
    posts.sort(key=lambda x: (x["date"], x["title"]), reverse=True)
    return posts


def site_header(logo, current):
    def a(href, label, key):
        cur = ' aria-current="page"' if key == current else ""
        return '<a href="%s"%s>%s</a>' % (href, cur, label)
    return f'''<header class="b-header">
    <div class="b-wrap b-header-row">
      <a href="/" class="b-logo" aria-label="dogen.es ana sayfa">{logo}<span class="tld">.es</span></a>
      <nav class="b-nav" aria-label="Ana menü">
        {a("/#hizmetler", "Hizmetler", "svc")}
        {a("/blog/", "Blog", "blog")}
        {a("/#iletisim", "İletişim", "ct")}
      </nav>
      <a class="b-btn" href="{WA}" target="_blank" rel="noopener">WhatsApp’tan yazın</a>
    </div>
  </header>'''


def site_footer(logo):
    year = dt.date.today().year
    return f'''<footer class="b-footer">
    <div class="b-wrap b-footer-row">
      <a href="/" class="b-logo" aria-label="dogen.es ana sayfa">{logo}<span class="tld">.es</span></a>
      <nav class="b-foot-links" aria-label="Alt menü">
        <a href="/">Ana sayfa</a><a href="/blog/">Blog</a><a href="/blog/feed.xml">RSS</a><a href="/es/" hreflang="es">Español</a><a href="mailto:info@dogen.es">info@dogen.es</a>
      </nav>
      <p class="b-legal">dogen.es bağımsız bir eğitim ve yerleşim danışmanlığıdır. Yazılar genel bilgilendirme amaçlıdır, hukuki görüş değildir; vize ve oturum kararları yetkili İspanyol makamlarına aittir. © {year} {AUTHOR}, Sevilla.</p>
    </div>
  </footer>'''


def page_head(title, desc, canonical, og_type="website", extra="", alts=None, lang="tr"):
    alt = ""
    for hl, href in (alts or []):
        alt += f'\n  <link rel="alternate" hreflang="{hl}" href="{href}" />'
    locale = "tr_TR" if lang == "tr" else "es_ES"
    return f'''<title>{e(title)}</title>
  <meta name="description" content="{e(desc)}" />
  <link rel="canonical" href="{canonical}" />{alt}
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1" />
  <meta name="author" content="{AUTHOR}" />
  <meta name="theme-color" content="#f6f4ef" />
  <meta property="og:site_name" content="dogen.es" />
  <meta property="og:locale" content="{locale}" />
  <meta property="og:type" content="{og_type}" />
  <meta property="og:title" content="{e(title)}" />
  <meta property="og:description" content="{e(desc)}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:image" content="{SITE}/og.png" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="dogen.es — İspanya’da eğitim, Sevilla’dan birebir" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{e(title)}" />
  <meta name="twitter:description" content="{e(desc)}" />
  <meta name="twitter:image" content="{SITE}/og.png" />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <link rel="icon" type="image/png" sizes="192x192" href="/icon-192.png" />
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" />
  <link rel="alternate" type="application/rss+xml" title="dogen.es Blog" href="{SITE}/blog/feed.xml" />{extra}'''


ORG = {
    "@type": ["ProfessionalService", "EducationalOrganization"],
    "@id": SITE + "/#org",
    "name": "dogen.es",
    "url": SITE + "/",
    "logo": SITE + "/icon-512.png",
    "image": SITE + "/og.png",
    "email": "info@dogen.es",
    "telephone": PHONE,
    "address": {"@type": "PostalAddress", "addressLocality": "Sevilla", "addressRegion": "Andalucía", "addressCountry": "ES"},
    "areaServed": [{"@type": "Country", "name": "Türkiye"}, {"@type": "Country", "name": "España"}],
    "knowsLanguage": ["tr", "es", "en"],
    "founder": {"@type": "Person", "name": AUTHOR},
    "contactPoint": [{"@type": "ContactPoint", "contactType": "customer service", "telephone": PHONE,
                      "email": "info@dogen.es", "availableLanguage": ["Turkish", "Spanish"]}],
}

HOME_META = {
    "tr": dict(
        title="İspanya’da Eğitim ve Öğrenci Vizesi Danışmanlığı · Sevilla | dogen.es",
        desc="Sevilla’dan birebir danışmanlık: İspanyolca dil okulu, ücretsiz devlet meslek eğitimi (FP), üniversite, öğrenci vizesi dosyası ve İspanya’daki ilk 30 gün. Türkçe destek.",
        url=SITE + "/", alt_path="es/", alt_lang="es", alt_label="Español",
        knows=["İspanya öğrenci vizesi", "İspanyolca dil okulu", "Formación Profesional (FP)", "Lise diploması denkliği (homologación)", "Sevilla’da yerleşim"],
    ),
    "es": dict(
        title="Estudiar en España desde Turquía · Consultoría en Sevilla | dogen.es",
        desc="Acompañamiento personal desde Sevilla para estudiantes de Turquía: escuela de español, FP pública, universidad, visado de estudios y primeros 30 días en España.",
        url=SITE + "/es/", alt_path="", alt_lang="tr", alt_label="Türkçe",
        knows=["Visado de estudios", "Escuelas de español", "Formación Profesional", "Homologación de títulos", "Relocalización en Sevilla"],
    ),
}


def faq_ld(tpl_html, lang, es):
    qs = []
    for n in range(1, 10):
        m = re.search(r'data-i18n="q%d">([^<]*)<.*?data-i18n="a%d">([^<]*)<' % (n, n), tpl_html, re.S)
        if not m:
            break
        q, a = html.unescape(m.group(1)), html.unescape(m.group(2))
        if lang == "es":
            q, a = es.get("q%d" % n, q), es.get("a%d" % n, a)
        qs.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}})
    return {"@type": "FAQPage", "@id": HOME_META[lang]["url"] + "#sss", "inLanguage": lang, "mainEntity": qs}


def latest_block(posts, lang):
    if not posts:
        return ""
    items = []
    for p in posts[:3]:
        tag = e(p["tags"][0]) if p["tags"] else "Rehber"
        items.append(f'''            <li><a href="{p["path"]}"{' hreflang="tr" lang="tr"' if lang == "es" else ""}><span class="bl-tag">{tag}</span><strong>{e(p["title"])}</strong><span class="bl-meta">{tr_date(p["date"])} · {p["minutes"]} dk</span><i aria-hidden="true">→</i></a></li>''')
    return f'''        <div class="blog-latest reveal" id="rehber">
          <div class="bl-head">
            <span class="partners-h" data-i18n="bl_tag">Rehber yazıları</span>
            <h2 data-i18n="bl_h">İspanya’da okumak için rehber yazıları</h2>
            <a class="text-link" href="/blog/" data-i18n="bl_all">Tüm yazılar →</a>
          </div>
          <ul class="bl-list">
{chr(10).join(items)}
          </ul>
        </div>
'''


def build_home(posts, logo):
    tpl = (ROOT / "src" / "index.template.html").read_text()
    es = es_dict()
    for lang in ("tr", "es"):
        M = HOME_META[lang]
        alts = [("tr", SITE + "/"), ("es", SITE + "/es/"), ("x-default", SITE + "/")]
        graph = {"@context": "https://schema.org", "@graph": [
            dict(ORG, knowsAbout=M["knows"]),
            {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "dogen.es",
             "inLanguage": ["tr", "es"], "publisher": {"@id": SITE + "/#org"}},
            {"@type": "WebPage", "@id": M["url"] + "#webpage", "url": M["url"], "name": M["title"],
             "description": M["desc"], "inLanguage": lang, "isPartOf": {"@id": SITE + "/#website"},
             "about": {"@id": SITE + "/#org"}},
            faq_ld(tpl, lang, es),
        ]}
        head = "  " + page_head(M["title"], M["desc"], M["url"], alts=alts, lang=lang) + "\n  " + jsonld(graph) + "\n"
        out = tpl.replace("<!--HEAD-->\n", head).replace("<!--LOGO-->", logo)
        out = out.replace("<!--BLOG_LATEST-->\n", latest_block(posts, lang))
        out = out.replace("<!--ALT_PATH-->", M["alt_path"]).replace("<!--ALT_LANG-->", M["alt_lang"]).replace("<!--ALT_LABEL-->", M["alt_label"])
        if lang == "es":
            out = out.replace('<html lang="tr">', '<html lang="es">', 1)
            missing = []

            def sub(m):
                key = m.group(3)
                if key in es:
                    return m.group(1) + html.escape(es[key], quote=False)
                missing.append(key)
                return m.group(0)
            # 1=açılış etiketi, 2=etiket adı, 3=anahtar, 4=metin (kapanış etiketi lookahead ile korunur)
            out = re.sub(r'(<(\w+)\b[^>]*\sdata-i18n="([\w-]+)"[^>]*>)([^<]*)(?=</\2>)', sub, out)
            out = out.replace('aria-label="Ana menü"', 'aria-label="Menú principal"').replace('aria-label="Alt menü"', 'aria-label="Menú inferior"')
            out = out.replace('aria-label="Dil / Idioma"', 'aria-label="Idioma / Dil"')
            if missing:
                print("  ES karşılığı olmayan anahtarlar (TR kaldı):", ", ".join(sorted(set(missing))))
            (ROOT / "es").mkdir(exist_ok=True)
            (ROOT / "es" / "index.html").write_text(out)
        else:
            (ROOT / "index.html").write_text(out)
    print("  index.html + es/index.html")


def related(posts, cur, n=3):
    others = [p for p in posts if p["slug"] != cur["slug"]]
    others.sort(key=lambda p: (-len(set(p["tags"]) & set(cur["tags"])), -p["date"].toordinal()))
    return others[:n]


def build_post(p, posts, logo):
    crumbs = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "dogen.es", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog/"},
        {"@type": "ListItem", "position": 3, "name": p["title"], "item": p["url"]}]}
    art = {"@type": "BlogPosting", "@id": p["url"] + "#article", "headline": p["title"][:110],
           "description": p["description"], "inLanguage": "tr", "url": p["url"], "mainEntityOfPage": p["url"],
           "datePublished": p["date"].isoformat(), "dateModified": p["updated"].isoformat(),
           "wordCount": p["words"], "keywords": ", ".join(p["tags"]), "image": SITE + "/og.png",
           "author": {"@type": "Person", "name": AUTHOR, "url": SITE + "/#hakkimizda"},
           "publisher": {"@id": SITE + "/#org"}}
    ld = jsonld({"@context": "https://schema.org", "@graph": [art, crumbs, ORG]})
    extra = (f'\n  <meta property="article:published_time" content="{p["date"].isoformat()}" />'
             f'\n  <meta property="article:modified_time" content="{p["updated"].isoformat()}" />'
             + "".join(f'\n  <meta property="article:tag" content="{e(t)}" />' for t in p["tags"])
             + "\n  " + ld)
    head = page_head(p["title"] + " | dogen.es", p["description"], p["url"], og_type="article", extra=extra)
    toc = ""
    h2 = [h for h in p["heads"] if h[0] == 2 and h[2].lower() != "kaynaklar"]
    if len(h2) >= 3:
        toc = '<details class="toc" open><summary>Bu yazıda</summary><ol>' + "".join(
            f'<li><a href="#{hid}">{e(t)}</a></li>' for _, hid, t in h2) + "</ol></details>"
    upd = ""
    if p["updated"] > p["date"]:
        upd = f' · <span>Güncellendi: <time datetime="{p["updated"].isoformat()}">{tr_date(p["updated"])}</time></span>'
    tags = "".join(f'<span class="b-tag">{e(t)}</span>' for t in p["tags"])
    rel = "".join(f'<li><a href="{r["path"]}"><strong>{e(r["title"])}</strong><span>{r["minutes"]} dk okuma</span></a></li>' for r in related(posts, p))
    page = f'''<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  {head}
  {FONT}
  <link rel="stylesheet" href="/blog.css" />
</head>
<body>
  <a class="skip" href="#icerik">İçeriğe geç</a>
  {site_header(logo, "blog")}
  <main id="icerik" class="b-wrap b-article-wrap">
    <nav class="b-crumbs" aria-label="Konum"><a href="/">dogen.es</a><span aria-hidden="true">/</span><a href="/blog/">Blog</a></nav>
    <article class="b-article">
      <header class="b-art-head">
        <div class="b-tags">{tags}</div>
        <h1>{e(p["title"])}</h1>
        <p class="b-lead">{e(p["description"])}</p>
        <p class="b-meta"><span>{AUTHOR}</span> · <time datetime="{p["date"].isoformat()}">{tr_date(p["date"])}</time>{upd} · <span>{p["minutes"]} dk okuma</span></p>
      </header>
      {toc}
      <div class="b-prose">
{p["html"]}
      </div>
      <aside class="b-cta" aria-label="İletişim">
        <h2>Kendi dosyanız için yol haritası mı lazım?</h2>
        <p>Hedefinizi ve takviminizi kısaca yazın; Sevilla’dan, Türkçe olarak size uygun rotayı birlikte çıkaralım.</p>
        <a class="b-btn b-btn-light" href="{WA}?text={quote("Merhaba, blogdaki “" + p["title"] + "” yazısını okudum. Kendi durumum için bilgi almak istiyorum.")}" target="_blank" rel="noopener">WhatsApp’tan yazın →</a>
      </aside>
    </article>
    <section class="b-related" aria-labelledby="ilgili">
      <h2 id="ilgili">İlgili yazılar</h2>
      <ul>{rel}</ul>
    </section>
  </main>
  {site_footer(logo)}
</body>
</html>
'''
    d = ROOT / "blog" / p["slug"]
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(page)


def build_blog_index(posts, logo):
    url = SITE + "/blog/"
    title = "Blog · İspanya’da eğitim ve yerleşim rehberleri | dogen.es"
    desc = "İspanya öğrenci vizesi, ücretsiz devlet meslek eğitimi (FP), lise denkliği, Sevilla’da yerleşim ve öğrenciyken çalışma üzerine güncel, kaynaklı rehber yazılar."
    ld = jsonld({"@context": "https://schema.org", "@graph": [
        {"@type": "Blog", "@id": url + "#blog", "url": url, "name": "dogen.es Blog", "description": desc, "inLanguage": "tr",
         "publisher": {"@id": SITE + "/#org"},
         "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": p["url"], "datePublished": p["date"].isoformat(),
                       "dateModified": p["updated"].isoformat()} for p in posts]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "dogen.es", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": url}]},
        ORG]})
    head = page_head(title, desc, url, extra="\n  " + ld)
    cards = []
    for i, p in enumerate(posts):
        tag = e(p["tags"][0]) if p["tags"] else "Rehber"
        cards.append(f'''      <li class="b-card{' b-card-lead' if i == 0 else ''}"><a href="{p["path"]}">
        <span class="b-tag">{tag}</span>
        <h2>{e(p["title"])}</h2>
        <p>{e(p["description"])}</p>
        <span class="b-meta"><time datetime="{p["date"].isoformat()}">{tr_date(p["date"])}</time> · {p["minutes"]} dk okuma</span>
      </a></li>''')
    page = f'''<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  {head}
  {FONT}
  <link rel="stylesheet" href="/blog.css" />
</head>
<body>
  <a class="skip" href="#icerik">İçeriğe geç</a>
  {site_header(logo, "blog")}
  <main id="icerik" class="b-wrap">
    <header class="b-hero">
      <span class="b-kicker">Blog · Rehber yazıları</span>
      <h1>İspanya’da okumak için bilmeniz gerekenler.</h1>
      <p>Vize, denklik, devlet meslek eğitimi ve Sevilla’da yerleşim üzerine, resmî kaynaklara dayanan ve düzenli güncellenen yazılar.</p>
    </header>
    <ul class="b-grid">
{chr(10).join(cards)}
    </ul>
  </main>
  {site_footer(logo)}
</body>
</html>
'''
    (ROOT / "blog").mkdir(exist_ok=True)
    (ROOT / "blog" / "index.html").write_text(page)


def build_feed(posts):
    items = []
    for p in posts[:30]:
        pub = dt.datetime.combine(p["date"], dt.time(9, 0)).strftime("%a, %d %b %Y %H:%M:%S +0100")
        items.append(f'''  <item>
    <title>{e(p["title"])}</title>
    <link>{p["url"]}</link>
    <guid isPermaLink="true">{p["url"]}</guid>
    <pubDate>{pub}</pubDate>
    <description>{e(p["description"])}</description>
{"".join(f"    <category>{e(t)}</category>{chr(10)}" for t in p["tags"])}  </item>''')
    last = dt.datetime.combine(max([p["updated"] for p in posts], default=dt.date.today()), dt.time(9, 0)).strftime("%a, %d %b %Y %H:%M:%S +0100")
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>dogen.es Blog</title>
  <link>{SITE}/blog/</link>
  <atom:link href="{SITE}/blog/feed.xml" rel="self" type="application/rss+xml" />
  <description>İspanya’da eğitim ve yerleşim üzerine rehber yazılar, Sevilla’dan.</description>
  <language>tr</language>
  <lastBuildDate>{last}</lastBuildDate>
{chr(10).join(items)}
</channel>
</rss>
'''
    (ROOT / "blog" / "feed.xml").write_text(xml)


def build_sitemap(posts):
    home = git_date("src/index.template.html", "app.js", "styles.css", "content/blog")
    blog_last = max([p["updated"] for p in posts], default=dt.date.today()).isoformat()
    alt = ('\n    <xhtml:link rel="alternate" hreflang="tr" href="%s/" />'
           '\n    <xhtml:link rel="alternate" hreflang="es" href="%s/es/" />'
           '\n    <xhtml:link rel="alternate" hreflang="x-default" href="%s/" />') % (SITE, SITE, SITE)
    urls = [(SITE + "/", home, alt), (SITE + "/es/", home, alt), (SITE + "/blog/", blog_last, "")]
    urls += [(p["url"], p["updated"].isoformat(), "") for p in posts]
    body = "\n".join(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{d}</lastmod>{a}\n  </url>" for u, d, a in urls)
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + body + "\n</urlset>\n")
    (ROOT / "robots.txt").write_text("User-agent: *\nDisallow: /r/\nDisallow: /src/\nDisallow: /content/\nDisallow: /tools/\n\nSitemap: %s/sitemap.xml\n" % SITE)


def build_404(logo):
    page = f'''<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Sayfa bulunamadı | dogen.es</title>
  <meta name="robots" content="noindex" />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  {FONT}
  <link rel="stylesheet" href="/blog.css" />
</head>
<body>
  {site_header(logo, "")}
  <main class="b-wrap b-hero b-404">
    <span class="b-kicker">404</span>
    <h1>Aradığınız sayfa burada değil.</h1>
    <p>Bağlantı değişmiş olabilir. <a href="/">Ana sayfaya</a> dönebilir ya da <a href="/blog/">rehber yazılarına</a> göz atabilirsiniz.</p>
  </main>
  {site_footer(logo)}
</body>
</html>
'''
    (ROOT / "404.html").write_text(page)


def main():
    logo = logo_svg()
    posts = load_posts()
    build_home(posts, logo)
    build_blog_index(posts, logo)
    for p in posts:
        build_post(p, posts, logo)
    # Silinmiş yazıların klasörlerini temizle
    keep = {p["slug"] for p in posts}
    for d in (ROOT / "blog").iterdir():
        if d.is_dir() and d.name not in keep and (d / "index.html").exists():
            (d / "index.html").unlink()
            try:
                d.rmdir()
            except OSError:
                pass
            print("  kaldırıldı: blog/%s" % d.name)
    build_feed(posts)
    build_sitemap(posts)
    build_404(logo)
    print("  blog: %d yazı · sitemap.xml · robots.txt · feed.xml · 404.html" % len(posts))


if __name__ == "__main__":
    main()
