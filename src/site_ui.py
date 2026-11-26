# -*- coding: utf-8 -*-
"""dogen ortak arayüz parçaları (üst bar, açılır menü, alt bilgi) ve iç sayfa üreticisi."""
import datetime as dt
import html
import json
import pathlib
from urllib.parse import quote

import pages as P

e = lambda s: html.escape(str(s), quote=True)
WA = P.WA
MAIL = P.MAIL
ARROW = '<i aria-hidden="true">→</i>'


def wa(text):
    return WA + "?text=" + quote(text)


def other(lang):
    return "es" if lang == "tr" else "tr"


# ------------------------------------------------------------------ küçük parçalar
def thumb(i):
    bg = ["#1f4a7a", "#16181d", "#c58b2b"][i % 3]
    ring = "#e2b764" if i % 3 != 2 else "#16181d"
    return (f'<svg viewBox="0 0 64 64" aria-hidden="true" focusable="false"><rect width="64" height="64" fill="{bg}"/>'
            f'<g transform="translate(32 32)" fill="none" stroke="#f6f4ef" stroke-width="1.6">'
            f'<rect x="-15" y="-15" width="30" height="30"/><rect x="-15" y="-15" width="30" height="30" transform="rotate(45)"/>'
            f'<circle r="6" stroke="{ring}"/></g><g fill="#f6f4ef" fill-opacity=".85">'
            f'<path d="M0 0h8L0 8Z"/><path d="M64 0h-8l8 8Z"/><path d="M0 64h8L0 56Z"/><path d="M64 64h-8l8-8Z"/></g></svg>')


def lang_links(lang, tr_href, es_href):
    U = P.UI[lang]
    out = []
    for code, href in (("tr", tr_href), ("es", es_href)):
        cur = ' aria-current="true"' if code == lang else ""
        out.append(f'<a href="{href}" hreflang="{code}" lang="{code}" data-lang-link="{code}"{cur}>{code.upper()}</a>')
    return f'<div class="lang" role="group" aria-label="{e(U["lang_label"])}">{"".join(out)}</div>'


def lang_buttons(lang):
    U = P.UI[lang]
    b = "".join(f'<button type="button" data-lang="{c}" aria-pressed="{str(c == lang).lower()}">{c.upper()}</button>' for c in ("tr", "es"))
    return f'<div class="lang" role="group" aria-label="{e(U["lang_label"])}">{b}</div>'


def header(lang, logo, tr_href, es_href, home=False):
    U = P.UI[lang]
    cls, wrap = ("site-header hd", "wrap") if home else ("hd hd-inner", "ui-wrap")
    lang_ctl = lang_buttons(lang) if home else lang_links(lang, tr_href, es_href)
    return f'''<header class="{cls}">
    <div class="{wrap} hd-row">
      <div class="hd-l"><button type="button" class="mn-btn" aria-controls="mn" aria-expanded="false" aria-label="{e(U["menu"])}"><span class="mn-ico" aria-hidden="true"><i></i><i></i></span><span class="mn-lbl">{U["menu"]}</span></button></div>
      <a class="hd-logo" href="{P.path("home", lang)}" aria-label="dogen — {e(U["home"])}">{logo}</a>
      <div class="hd-r">{lang_ctl}<a class="hd-cta" href="{P.path("contact", lang)}">{U["contact"]}</a></div>
    </div>
  </header>'''


def flyout(lang, logo, posts, cur_key, tr_href, es_href):
    U = P.UI[lang]

    def li(key):
        cur = ' aria-current="page"' if key == cur_key else ""
        hl = ' hreflang="tr"' if key == "blog" and lang == "es" else ""
        return f'<li><a href="{P.path(key, lang)}"{hl}{cur}>{U[key]} {ARROW}</a></li>'
    col1 = "".join(li(k) for k in ("services", "process", "experiences", "about", "contact", "blog"))
    sp = P.path("services", lang)
    col2 = "".join(f'<li><a href="{sp}#{s["id"]}">{e(s["t"])} {ARROW}</a></li>' for s in P.SERVICES[lang])
    col2 += f'<li><a href="{sp}#sss">{U["faq"]} {ARROW}</a></li>'
    hl = ' hreflang="tr" lang="tr"' if lang == "es" else ""
    col3 = "".join(
        f'<li class="mn-post"><a href="{p["path"]}"{hl}><span class="mn-thumb">{thumb(i)}</span>'
        f'<span><strong>{e(p["title"])}</strong><span>{p["minutes"]} {U["min_read"]}</span></span></a></li>'
        for i, p in enumerate(posts[:3]))
    return f'''<div class="mn" id="mn" hidden>
    <div class="mn-scrim" data-mn-close></div>
    <div class="mn-sheet">
      <div class="mn-panel" role="dialog" aria-modal="true" aria-label="{e(U["main_menu"])}">
        <div class="ui-wrap hd-row">
          <div class="hd-l"><button type="button" class="mn-x" data-mn-close aria-label="{e(U["menu_close"])}"><span class="mn-ico is-x" aria-hidden="true"><i></i><i></i></span><span class="mn-lbl">{U["close"]}</span></button></div>
          <a class="hd-logo" href="{P.path("home", lang)}" aria-label="dogen — {e(U["home"])}">{logo}</a>
          <div class="hd-r">{lang_links(lang, tr_href, es_href)}</div>
        </div>
        <nav class="ui-wrap mn-cols" aria-label="{e(U["main_menu"])}">
          <section class="mn-col" style="--k:0"><h2>{U["col1"]}</h2><ul>{col1}</ul></section>
          <section class="mn-col" style="--k:1"><h2>{U["col2"]}</h2><ul>{col2}</ul><a class="mn-all" href="{sp}">{U["all_services"]} →</a></section>
          <section class="mn-col" style="--k:2"><h2>{U["col3"]}</h2><ul>{col3}</ul><a class="mn-all" href="/blog/"{hl}>{U["all_posts"]}{U["guides_note"]} →</a></section>
        </nav>
      </div>
      <div class="mn-foot"><div class="ui-wrap mn-foot-row"><p>{U["strip"]}</p><a class="ui-pill" href="{WA}" target="_blank" rel="noopener">{U["wa"]} {ARROW}</a></div></div>
    </div>
  </div>'''


def footer(lang, logo, posts, tr_href, es_href, home=False):
    U = P.UI[lang]
    year = dt.date.today().year
    bhl = ' hreflang="tr"' if lang == "es" else ""
    pages = "".join(f'<li><a href="{P.path(k, lang)}"{bhl if k == "blog" else ""}>{U[k]}</a></li>'
                    for k in ("services", "process", "experiences", "about", "contact", "blog"))
    hl = ' hreflang="tr" lang="tr"' if lang == "es" else ""
    guides = "".join(f'<li><a href="{p["path"]}"{hl}>{e(p["title"])}</a></li>' for p in posts[:4])
    guides += f'<li><a href="/blog/"{hl}>{U["all_posts"]} →</a></li>'
    alt_href = es_href if lang == "tr" else tr_href
    o = other(lang)
    inner = f'''<div class="ft-grid">
        <div class="ft-brand">
          <a class="ft-logo" href="{P.path("home", lang)}" aria-label="dogen — {e(U["home"])}">{logo}</a>
          <p>{U["foot_about"]}</p>
          <a class="ui-pill ui-pill-light" href="{WA}" target="_blank" rel="noopener">{U["wa"]} {ARROW}</a>
        </div>
        <nav aria-label="{e(U["foot_menu"])}"><h2>{U["foot_pages"]}</h2><ul>{pages}</ul></nav>
        <div><h2>{U["foot_guides"]}{U["guides_note"]}</h2><ul>{guides}</ul></div>
        <div><h2>{U["foot_contact"]}</h2><ul><li><a href="{WA}" target="_blank" rel="noopener">+34 666 104 496</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li>Sevilla, España</li></ul></div>
      </div>
      <div class="ft-bottom">
        <p class="ft-legal">{U["legal_line"]}</p>
        <p class="ft-copy">© <span data-yr>{year}</span> dogen · Sevilla · <a href="{P.path("legal", lang)}">{U["legal"]}</a> · <a href="{alt_href}" hreflang="{o}" lang="{o}" data-lang-link="{o}">{P.UI[lang]["other_lang"]}</a></p>
      </div>'''
    if home:
        return f'<footer class="ft ft-in">\n      {inner}\n    </footer>'
    return f'<footer class="ft">\n    <div class="ui-wrap">\n      {inner}\n    </div>\n  </footer>'


# ------------------------------------------------------------------ deneyimler
def testimonials():
    f = pathlib.Path(__file__).resolve().parent.parent / "content" / "testimonials.json"
    try:
        items = json.loads(f.read_text()).get("items", [])
    except FileNotFoundError:
        return []
    return [t for t in items if t.get("consent") is True and t.get("name")]


def quotes_html(lang, items):
    out = []
    for t in items:
        q = t.get("quote_" + lang) or t.get("quote_tr") or ""
        meta = " · ".join(x for x in (t.get("route", ""), str(t.get("year", ""))) if x)
        out.append(f'<li><figure class="xp-quote"><blockquote><p>“{e(q)}”</p></blockquote>'
                   f'<figcaption><b>{e(t["name"])}</b>{(" · " + e(meta)) if meta else ""}</figcaption></figure></li>')
    return f'<ul class="xp-quotes">{"".join(out)}</ul>' if out else ""


def xp_empty(lang):
    U = P.UI[lang]
    msg = "Merhaba, dogen ile yaşadığım deneyimi paylaşmak istiyorum." if lang == "tr" else "Hola, me gustaría compartir mi experiencia con dogen."
    return (f'<div class="xp-empty"><svg viewBox="0 0 48 48" aria-hidden="true" focusable="false"><rect width="48" height="48" rx="12" fill="#e4ebf3"/>'
            f'<path d="M15 30c0-6 3-10 8-12l1 2c-3 2-4 4-4 6h4v8h-9v-4Zm13 0c0-6 3-10 8-12l1 2c-3 2-4 4-4 6h4v8h-9v-4Z" fill="#1f4a7a"/></svg>'
            f'<div><h3>{U["xp_card_h"]}</h3><p>{U["xp_empty_p"]}</p><a href="{wa(msg)}" target="_blank" rel="noopener">{U["xp_share"]} →</a></div></div>')


def xp_cards(lang):
    U = P.UI[lang]
    out = []
    for x in P.EXAMPLES[lang]:
        steps = "".join(f"<li>{e(s)}</li>" for s in x["path"])
        out.append(f'<li class="xp-card"><span class="xp-chip">{U["example"]}</span><h3>{e(x["who"])}</h3>'
                   f'<p class="xp-goal">{e(x["goal"])}</p><ol class="xp-path">{steps}</ol><p class="xp-note">{e(x["note"])}</p></li>')
    return f'<ul class="xp-grid">{"".join(out)}</ul><p class="xp-disclaimer">{U["example_note"]}</p>'


def home_experiences(lang):
    U = P.UI[lang]
    items = testimonials()
    return f'''    <!-- 04 · ÖĞRENCİ DENEYİMLERİ -->
    <section class="d-card" id="deneyimler">
      <span class="d-ghost" aria-hidden="true">04</span>
      <div class="wrap">
        <div class="block-head reveal">
          <div>
            <span class="sec-tag">{U["home_xp_tag"]}</span>
            <h2 class="clip-h">{U["home_xp_h"]}</h2>
          </div>
          <p>{U["home_xp_p"]}</p>
        </div>
        <div class="reveal">
          {quotes_html(lang, items)}
          {xp_cards(lang)}
          <p class="more-row"><a class="more-link" href="{P.path("experiences", lang)}">{U["xp_all"]} <span aria-hidden="true">→</span></a></p>
        </div>
      </div>
    </section>

'''


def more_link(lang, key):
    U = P.UI[lang]
    target = {"services": P.path("services", lang), "process": P.path("process", lang), "about": P.path("about", lang),
              "faq": P.path("services", lang) + "#sss", "contact": P.path("contact", lang)}[key]
    return f'<p class="more-row"><a class="more-link" href="{target}">{U["more_" + key]} <span aria-hidden="true">→</span></a></p>'


# ------------------------------------------------------------------ iç sayfa gövdeleri
def crumbs(lang, key):
    U = P.UI[lang]
    return (f'<nav class="b-crumbs" aria-label="{e(U["crumbs"])}"><a href="{P.path("home", lang)}">dogen</a>'
            f'<span aria-hidden="true">/</span><span aria-current="page">{U[key]}</span></nav>')


def hero(lang, key, pg, actions=True, extra=""):
    U = P.UI[lang]
    act = ""
    if actions:
        act = (f'<div class="pg-actions"><a class="ui-pill" href="{wa(U["wa_msg_page"] % pg["kicker"])}" target="_blank" rel="noopener">{U["wa"]} {ARROW}</a>'
               + (f'<a class="pg-link" href="{P.path("contact", lang)}">{U["contact_more"]}</a>' if key != "contact" else f'<a class="pg-link" href="mailto:{MAIL}">{MAIL}</a>')
               + "</div>")
    return f'''<header class="pg-hero">
      {crumbs(lang, key)}
      <span class="pg-kick">{pg["kicker"]}</span>
      <div class="pg-hero-grid">
        <h1>{pg["h1"]}</h1>
        <div><p class="pg-lead">{pg["lead"]}</p>{act}</div>
      </div>{extra}
    </header>'''


def sec_head(h, p="", kick="", hid=""):
    k = f'<span class="pg-kick">{kick}</span>' if kick else ""
    pp = f"<p>{p}</p>" if p else ""
    idattr = f' id="{hid}"' if hid else ""
    return f'<div class="pg-sec-head"><div>{k}<h2{idattr}>{h}</h2></div>{pp}</div>'


def faq_block(lang):
    return "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in P.FAQ[lang])


def cta(lang, pg):
    U = P.UI[lang]
    return f'''<aside class="pg-cta" aria-label="{e(U["contact"])}">
      <div><h2>{U["cta_h"]}</h2><p>{U["cta_p"]}</p></div>
      <a class="ui-pill ui-pill-light" href="{wa(U["wa_msg_page"] % pg["kicker"])}" target="_blank" rel="noopener">{U["wa"]} {ARROW}</a>
    </aside>'''


def body_services(lang, pg):
    U = P.UI[lang]
    idx = "".join(f'<li><a href="#{s["id"]}"><b>{s["num"]}</b>{e(s["t"])}</a></li>' for s in P.SERVICES[lang])
    idx += f'<li><a href="#sss"><b>?</b>{U["faq"]}</a></li>'
    rows = []
    for s in P.SERVICES[lang]:
        inc = "".join(f"<li>{e(i)}</li>" for i in s["inc"])
        rows.append(f'''<article class="pg-svc" id="{s["id"]}" aria-labelledby="{s["id"]}-h">
        <div class="pg-svc-num" aria-hidden="true">{s["num"]}</div>
        <div><h2 id="{s["id"]}-h">{e(s["t"])}</h2><p class="pg-svc-d">{e(s["d"])}</p><p class="pg-fit"><b>{pg["fit_label"]}</b>{e(s["fit"])}</p></div>
        <div class="pg-inc"><h3>{pg["inc_label"]}</h3><ul class="pg-check">{inc}</ul><a class="pg-link" href="{wa(U["wa_msg_svc"] % s["t"])}" target="_blank" rel="noopener">{U["row_cta"]} →</a></div>
      </article>''')
    dl = ("Yapıyoruz", "Yapmıyoruz") if lang == "tr" else ("Lo que hacemos", "Lo que no hacemos")
    do = "".join(f"<li>{e(x)}</li>" for x in pg["do"])
    dont = "".join(f"<li>{e(x)}</li>" for x in pg["dont"])
    kick_p = "İş birliği" if lang == "tr" else "Colaboración"
    hero_html = hero(lang, "services", pg, extra=f'\n      <ul class="pg-index" aria-label="{e(U["services"])}" style="margin-top:clamp(28px,5vh,48px)">{idx}</ul>')
    return f'''{hero_html}
    <section class="pg-svcs" aria-label="{e(U["services"])}">
      {"".join(rows)}
    </section>
    <section class="pg-sec" aria-labelledby="kapsam">
      {sec_head(pg["scope_h"], hid="kapsam")}
      <div class="pg-two">
        <div class="pg-box"><h3>{dl[0]}</h3><ul class="pg-check">{do}</ul></div>
        <div class="pg-box alt"><h3>{dl[1]}</h3><ul class="pg-check pg-x">{dont}</ul></div>
      </div>
    </section>
    <section class="pg-sec pg-sec-plain" id="kurumlar" aria-labelledby="kurumlar-h">
      <div class="pg-band">
        <span class="pg-band-ghost" aria-hidden="true">dō</span>
        <div class="pg-band-grid">
          <div><span class="pg-kick pg-kick-light">{kick_p}</span><h2 id="kurumlar-h">{pg["partners_h"]}</h2></div>
          <div>
            <p>{pg["partners_p"]}</p>
            <p style="margin-top:16px"><a href="mailto:{MAIL}">{MAIL} →</a></p>
            <span class="pg-kick pg-kick-light" style="margin:28px 0 0">{pg["partners_list"]}</span>
            <ul class="pg-partners"><li><a href="https://sevillahabla.com/" target="_blank" rel="noopener"><strong>Sevilla Habla</strong><span>{pg["partner_desc"]} ↗</span></a></li></ul>
          </div>
        </div>
      </div>
    </section>
    <section class="pg-sec" id="sss" aria-labelledby="sss-h">
      {sec_head(U["faq"], kick="SSS" if lang == "tr" else "FAQ", hid="sss-h")}
      <div class="pg-faq">{faq_block(lang)}</div>
    </section>'''


def body_process(lang, pg):
    steps = "".join(
        f'<li><div><h3>{e(s["t"])}</h3><p class="pg-when">{e(s["when"])}</p></div>'
        f'<p class="who"><b>{pg["us"]}</b>{e(s["us"])}</p><p class="who"><b>{pg["you"]}</b>{e(s["you"])}</p></li>'
        for s in P.STEPS[lang])
    tl = "".join(f"<li><b>{e(a)}</b><p>{e(b)}</p></li>" for a, b in P.TIMELINE[lang])
    return f'''{hero(lang, "process", pg)}
    <section class="pg-sec" aria-labelledby="adimlar">
      {sec_head(pg["steps_h"], pg["steps_p"], hid="adimlar")}
      <ol class="pg-steps">{steps}</ol>
    </section>
    <section class="pg-sec" aria-labelledby="takvim">
      {sec_head(pg["tl_h"], pg["tl_p"], hid="takvim")}
      <ol class="pg-tl">{tl}</ol>
    </section>'''


def body_about(lang, pg):
    story = "".join(f"<p>{e(p)}</p>" for p in pg["story"])
    why = "".join(f"<p>{e(p)}</p>" for p in pg["why"])
    vals = "".join(f"<li><b>{e(a)}</b><span>{e(b)}</span></li>" for a, b in pg["values"])
    return f'''{hero(lang, "about", pg)}
    <section class="pg-sec" aria-labelledby="hikaye">
      <div class="pg-sec-head"><div><h2 id="hikaye">{pg["story_h"]}</h2></div><div class="pg-prose">{story}</div></div>
    </section>
    <section class="pg-sec" aria-labelledby="degerler">
      {sec_head(pg["values_h"], hid="degerler")}
      <ul class="pg-grid4">{vals}</ul>
    </section>
    <section class="pg-sec" aria-labelledby="sevilla">
      <div class="pg-sec-head"><div><h2 id="sevilla">{pg["why_h"]}</h2></div><div class="pg-prose">{why}</div></div>
    </section>
    <section class="pg-sec pg-sec-plain" aria-labelledby="isim">
      <div class="pg-band">
        <span class="pg-band-ghost" aria-hidden="true">dō</span>
        <div class="pg-band-grid"><div><h2 id="isim">{pg["name_h"]}</h2></div><div><p>{pg["name_p"]}</p></div></div>
      </div>
    </section>'''


def body_experiences(lang, pg):
    U = P.UI[lang]
    items = testimonials()
    top = quotes_html(lang, items) if items else xp_empty(lang)
    return f'''{hero(lang, "experiences", pg)}
    <section class="pg-sec" aria-labelledby="sozler">
      {sec_head(U["xp_empty_h"], hid="sozler")}
      {top}
    </section>
    <section class="pg-sec" aria-labelledby="ornekler">
      {sec_head(pg["ex_h"], hid="ornekler")}
      {xp_cards(lang)}
    </section>'''


def body_contact(lang, pg):
    first = "".join(f"<li>{e(x)}</li>" for x in pg["first"])
    return f'''{hero(lang, "contact", pg)}
    <section class="pg-sec" aria-labelledby="kanallar">
      {sec_head(pg["ch_h"], hid="kanallar")}
      <dl class="pg-ch">
        <div><dt>{pg["wa_l"]}</dt><dd><a href="{WA}" target="_blank" rel="noopener">+34 666 104 496</a></dd></div>
        <div><dt>{pg["mail_l"]}</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd></div>
        <div><dt>{pg["org_l"]}</dt><dd><a href="mailto:{MAIL}">{MAIL}</a><small>{pg["org_v"]}</small></dd></div>
        <div><dt>{pg["city_l"]}</dt><dd>Sevilla, España<small>{pg["time_l"]}: <span data-clock>—</span></small></dd></div>
      </dl>
    </section>
    <section class="pg-sec" aria-labelledby="ilk-mesaj">
      {sec_head(pg["first_h"], hid="ilk-mesaj")}
      <ol class="pg-ol">{first}</ol>
      <a class="ui-pill" href="{wa(pg["wa_prefill"])}" target="_blank" rel="noopener">{pg["wa_btn"]} {ARROW}</a>
    </section>'''


def body_legal(lang, pg):
    o = P.LEGAL_OWNER
    nif_li = f'<li><strong>NIF:</strong> {e(o["nif"])}</li>\n' if o["nif"] else ""
    txt = P.LEGAL_HTML[lang].format(name=e(o["name"]), nif_li=nif_li, address=e(o["address"]), email=o["email"], phone=e(o["phone"]))
    return f'''{hero(lang, "legal", pg, actions=False)}
    <section class="pg-legal"><div class="b-prose">
{txt}
    </div></section>'''


BODIES = {"services": body_services, "process": body_process, "about": body_about,
          "experiences": body_experiences, "contact": body_contact, "legal": body_legal}
PAGE_TYPES = {"about": "AboutPage", "contact": "ContactPage"}
