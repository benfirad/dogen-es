#!/usr/bin/env python3
"""dogen.es haftalık blog taslağı + aylık kaynak link kontrolü.

Akış (onay kapılı, hiçbir şeyi kendiliğinden yayınlamaz):
  1. content/blog/topics.txt içindeki ilk açık konuyu alır.
  2. Antigravity köprüsü (OpenAI uyumlu) ile marka sesine uygun Türkçe taslak yazdırır.
  3. İkinci bir modelle olgu kontrolü yaptırır; şüpheli cümleler [KONTROL] ile işaretlenir.
  4. Kaynak linklerini HTTP ile doğrular, kırık olanları rapora yazar.
  5. Taslağı `draft: true` olarak content/blog/<slug>.md'ye yazar (sitede görünmez).
  6. Duffy'ye `awaiting_approval` görev ekler; Fırat onaylarsa tools/blog_publish.sh çalışır.

Ayrıca ayın ilk haftasında (veya --check-links ile) yayındaki tüm yazıların kaynak linklerini
kontrol eder; kırık link varsa Duffy'ye bilgi görevi düşer.

Kullanım:  blog_draft.py [--dry-run] [--check-links] [--topic "Başlık | odak"]
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from mdlite import slugify  # noqa: E402

BLOG = ROOT / "content" / "blog"
TOPICS = BLOG / "topics.txt"
BRIDGE = "http://127.0.0.1:8765/v1/chat/completions"
WRITER = "claude-opus-5-5-high"
CHECKER = "gemini-4-argon-high"
DUET_DB = Path("/Users/mac/.hermes/duet/duet.db")
PUBLISH = ROOT / "tools" / "blog_publish.sh"
VERIFIED_URLS = [
    "https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099  (Real Decreto 1155/2024, Yabancılar Yönetmeliği)",
    "https://www.inclusion.gob.es/web/migraciones  (Göç portalı, Ministerio de Inclusión)",
    "https://sede.administracionespublicas.gob.es/  (resmî e-hizmet ve randevu sistemi)",
    "https://www.exteriores.gob.es/Consulados/estambul/es/Paginas/index.aspx  (İspanya İstanbul Başkonsolosluğu)",
    "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Traductores-Interpretes-Jurados.aspx  (yeminli tercüman listesi)",
    "https://turkey.blsspainglobal.com/  (BLS Spain Türkiye vize başvuru merkezi)",
    "https://www.educacionfpydeportes.gob.es/mc/convalidacion-homologacion/convalidacion-no-universitaria.html  (lise denkliği)",
    "https://www.juntadeandalucia.es/educacion/portals/web/formacion-profesional-andaluza  (Endülüs FP portalı)",
    "https://www.todofp.es/  (İspanya FP resmî portalı)",
    "https://www.sede.fnmt.gob.es/certificados/persona-fisica  (FNMT dijital sertifika)",
    "https://www.cervantes.es/  (Instituto Cervantes)",
    "https://www.sevilla.org/  (Sevilla Belediyesi)",
]
LOG = Path.home() / "Library" / "Logs" / "dogen-blog.log"

ALLOWED_DOMAINS = (
    "boe.es", "gob.es", "juntadeandalucia.es", "exteriores.gob.es", "blsspainglobal.com",
    "cervantes.es", "sevilla.org", "fnmt.gob.es", "todofp.es", "uned.es", "europa.eu",
)


def log(msg: str) -> None:
    line = f"{datetime.now():%Y-%m-%d %H:%M:%S} {msg}"
    print(line)
    try:
        LOG.parent.mkdir(parents=True, exist_ok=True)
        with LOG.open("a") as f:
            f.write(line + "\n")
    except OSError:
        pass


def existing_posts() -> list[dict]:
    out = []
    for p in sorted(BLOG.glob("*.md")):
        txt = p.read_text()
        m = re.match(r"---\n(.*?)\n---\n", txt, re.S)
        meta = dict(re.findall(r"^(\w+):\s*(.*)$", m.group(1), re.M)) if m else {}
        out.append({"slug": p.stem, "title": meta.get("title", p.stem), "draft": meta.get("draft") == "true", "text": txt})
    return out


def chat(model: str, system: str, user: str, timeout: int = 420) -> str:
    body = json.dumps({"model": model, "temperature": 0.4,
                       "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}]}).encode()
    req = urllib.request.Request(BRIDGE, body, {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)["choices"][0]["message"]["content"]


STYLE = """Sen dogen.es için yazan, Sevilla'da yaşayan bir eğitim ve yerleşim danışmanısın.
Hedef okur: İspanya'da okumak isteyen Türkiye'deki öğrenciler ve aileleri.

Ses ve üslup:
- Türkçe, sakin, net, "siz" hitabı. Kısa cümleler. Abartı, söz, garanti yok ("garanti", "%100", "kesin" yasak).
- Teknik İspanyolca terimleri ilk geçtiği yerde parantez içinde açıkla, italik yaz (*empadronamiento*).
- Pazarlama dili yok. Son bölüm hariç dogen.es'ten söz etme.

Doğruluk kuralları (çok önemli):
- Yalnızca emin olduğun, resmî kaynaklarla doğrulanabilir bilgileri yaz.
- Ücret, süre, saat, kontenjan gibi bir rakamdan emin değilsen rakamı yazma; genel ifade kullan
  ya da cümlenin sonuna [KONTROL] ekle. Uydurma bir rakam yazmaktansa [KONTROL] koymak her zaman daha iyidir.
- Mevzuat: Yabancılar Yönetmeliği Real Decreto 1155/2024 (20 Mayıs 2025'ten beri yürürlükte).
  Yükseköğretim öğrencileri (FP Grado Superior dahil) ek izin olmadan haftada 30 saate kadar çalışabilir.
  Dil kursu öğrencilerine otomatik çalışma hakkı yoktur. Dil kursları vize için yüz yüze ve haftada en az 20 saat olmalıdır.
- Linkler yalnızca şu resmî alan adlarından olabilir: """ + ", ".join(ALLOWED_DOMAINS) + """.
  Emin olmadığın derin bir URL yerine alan adının ana sayfasını ver. Mümkünse şu doğrulanmış URL'leri kullan:
""" + "\n".join("  - " + u for u in VERIFIED_URLS) + """

Biçim (Markdown, başka hiçbir şey yazma; kod bloğu kullanma):
---
title: <60-70 karakterlik, arama niyetine uygun başlık>
description: <140-160 karakterlik meta açıklama>
tags: <2-3 etiket, virgülle>
---

<2-3 cümlelik giriş paragrafı>

## ... (4-7 adet H2 bölüm; gerekiyorsa H3, madde listesi, bir tablo, bir "> **İpucu:** ..." notu)

## Kaynaklar

- [Kurum adı](https://...)

*Bu yazı genel bilgilendirme amaçlıdır, hukuki görüş değildir. Kendi durumunuz için güncel mevzuatı ve yetkili makamların kararlarını esas alın.*

Uzunluk: 700-1100 kelime."""

CHECK = """Sen titiz bir editör ve İspanya göç/eğitim mevzuatı olgu kontrolcüsüsün.
Sana Türkçe bir blog taslağı verilecek. Görevin:
1. Yanlış, güncel olmayan ya da doğrulanamayan her somut iddianın (rakam, süre, ücret, kurum adı, şart)
   cümle sonuna [KONTROL] ekle. Emin olduğun düzeltmeleri doğrudan yap.
2. "garanti", "%100", "kesin" gibi söz veren ifadeleri yumuşat.
3. Yapıyı, frontmatter'ı, linkleri ve üslubu koru. Yeni bölüm ekleme.
Sadece düzeltilmiş tam Markdown'ı döndür, başka açıklama yazma."""


def clean_md(s: str) -> str:
    s = s.strip()
    s = re.sub(r"^```(?:markdown|md)?\s*\n", "", s)
    s = re.sub(r"\n```\s*$", "", s)
    i = s.find("---")
    return s[i:].strip() + "\n" if i >= 0 else s


def check_url(url: str) -> int | str:
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156 Safari/537.36"
    code = "000"
    for _ in range(2):
        r = subprocess.run(["/usr/bin/curl", "-sL", "-o", "/dev/null", "-m", "45", "-A", ua, "-w", "%{http_code}", url],
                           capture_output=True, text=True)
        code = r.stdout.strip() or "000"
        if code == "200":
            return 200
    return int(code) if code.isdigit() and code != "000" else "erişilemedi"


def links(md: str) -> list[str]:
    return sorted(set(re.findall(r"\]\((https?://[^)\s]+)\)", md)))


def duffy_task(title: str, action: str, cmd: str, summary: str) -> int | None:
    if not DUET_DB.exists():
        log("Duffy veritabanı yok, görev eklenemedi")
        return None
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    con = sqlite3.connect(DUET_DB, timeout=30)
    cur = con.execute(
        "INSERT INTO duet_tasks (title, category, status, approval_Action, approval_cmd, result_summary, created_at, updated_at)"
        " VALUES (?, 'dogen-blog', 'awaiting_approval', ?, ?, ?, ?, ?)",
        (title, action, cmd, summary, ts, ts))
    tid = cur.lastrowid
    con.execute("INSERT INTO duet_logs (task_id, level, message, created_at) VALUES (?, 'INFO', ?, ?)",
                (tid, "dogen.es blog hattı: onay bekleyen görev eklendi.", ts))
    con.commit()
    con.close()
    return tid


def next_topic() -> tuple[int, str] | None:
    for i, line in enumerate(TOPICS.read_text().splitlines()):
        if line.startswith("[ ]"):
            return i, line[3:].strip()
    return None


def mark_topic(idx: int, slug: str) -> None:
    lines = TOPICS.read_text().splitlines()
    lines[idx] = "[x]" + lines[idx][3:] + f"  → {slug}"
    TOPICS.write_text("\n".join(lines) + "\n")


def draft(topic: str | None, dry: bool) -> None:
    pending = [p for p in existing_posts() if p["draft"]]
    if pending and not topic:
        log(f"Onay bekleyen taslak var ({pending[0]['slug']}), yeni taslak üretilmedi")
        return
    idx = None
    if not topic:
        nt = next_topic()
        if not nt:
            log("Konu kuyruğu boş")
            duffy_task("📝 dogen.es blog: konu kuyruğu bitti", "Bilgi: content/blog/topics.txt'ye yeni konu ekleyin",
                       "true", "Haftalık taslak için yeni konu kalmadı.") if not dry else None
            return
        idx, topic = nt
    title_hint, _, focus = topic.partition("|")
    posts = existing_posts()
    others = "\n".join(f"- {p['title']} → /blog/{p['slug']}/" for p in posts if not p["draft"])
    user = (f"Konu: {title_hint.strip()}\nOdak: {focus.strip() or '-'}\n\n"
            f"Sitedeki mevcut yazılar (uygunsa metin içinde 1-2 tanesine bağlantı ver, aynı konuyu tekrar etme):\n{others}\n\n"
            "Son bölümden (Kaynaklar) hemen önce, tek cümlelik yumuşak bir not ekleyebilirsin: kendi durumları için "
            "dogen.es'e WhatsApp'tan yazabilecekleri. Abartma.")
    log(f"Taslak yazılıyor: {title_hint.strip()} ({WRITER})")
    md = clean_md(chat(WRITER, STYLE, user))
    try:
        log(f"Olgu kontrolü: {CHECKER}")
        checked = clean_md(chat(CHECKER, CHECK, md))
        if checked.startswith("---") and len(checked) > len(md) * 0.7:
            md = checked
    except Exception as e:  # noqa: BLE001
        log(f"Olgu kontrolü atlandı: {e}")

    md = re.sub(r"(\w)'(\w)", "\\1\u2019\\2", md)
    m = re.match(r"---\n(.*?)\n---\n", md, re.S)
    if not m:
        raise SystemExit("Model frontmatter üretmedi:\n" + md[:500])
    meta = dict(re.findall(r"^(\w+):\s*(.*)$", m.group(1), re.M))
    title = meta.get("title", title_hint).strip()
    slug = slugify(title.replace("\u2019", ""))[:70].rsplit("-", 1)[0].strip("-") if len(slugify(title.replace("\u2019", ""))) > 70 else slugify(title.replace("\u2019", ""))
    today = date.today().isoformat()
    fm = (f"---\ntitle: {title}\ndescription: {meta.get('description', '').strip()}\n"
          f"date: {today}\nupdated: {today}\ntags: {meta.get('tags', '').strip()}\ndraft: true\n---\n")
    md = fm + md[m.end():]

    bad_domain, broken = [], []
    for u in links(md):
        host = re.sub(r"^https?://", "", u).split("/")[0]
        if not any(host == d or host.endswith("." + d) for d in ALLOWED_DOMAINS):
            bad_domain.append(u)
        st = check_url(u)
        if st != 200:
            broken.append(f"{u} → {st}")
    kontrol = md.count("[KONTROL]")
    words = len(re.sub(r"[#*>\[\]()|-]", " ", md[m.end():]).split())

    path = BLOG / f"{slug}.md"
    if dry:
        print(md)
        log(f"[dry-run] {slug}: {words} kelime, {kontrol} KONTROL, {len(broken)} kırık link")
        return
    path.write_text(md)
    if idx is not None:
        mark_topic(idx, slug)

    report = [f"Taslak: content/blog/{slug}.md  (~{words} kelime)",
              f"Başlık: {title}",
              f"Açıklama: {meta.get('description', '').strip()}",
              f"[KONTROL] işareti: {kontrol}" + ("  ← bunlar düzeltilmeden yayın komutu çalışmaz" if kontrol else ""),
              "Kırık link: " + ("; ".join(broken) if broken else "yok"),
              "Resmî olmayan alan adı: " + (", ".join(bad_domain) if bad_domain else "yok"),
              "", "Onay = yayınla (draft kaldırılır, site derlenir, commit + push). Reddet = taslak kalır.",
              "", md[:3500]]
    tid = duffy_task(f"📝 dogen.es blog taslağı: {title}",
                     f"Yayınla: dogen.es/blog/{slug}/ (build + commit + git push)",
                     f"/bin/bash {PUBLISH} {slug}", "\n".join(report))
    log(f"Taslak hazır: {slug} · Duffy #{tid} · KONTROL={kontrol} · kırık={len(broken)}")


def check_all_links(dry: bool) -> None:
    broken = []
    for p in existing_posts():
        if p["draft"]:
            continue
        for u in links(p["text"]):
            st = check_url(u)
            if st != 200:
                broken.append(f"{p['slug']}: {u} → {st}")
    log(f"Link kontrolü: {len(broken)} kırık")
    if broken and not dry:
        duffy_task("🔗 dogen.es blog: kırık kaynak linki", "Bilgi: linkleri düzeltin (onay sadece görevi kapatır)",
                   "true", "\n".join(broken))
    for b in broken:
        print(" ", b)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--check-links", action="store_true")
    ap.add_argument("--topic")
    ap.add_argument("--no-draft", action="store_true")
    a = ap.parse_args()
    if a.check_links or date.today().day <= 7:
        check_all_links(a.dry_run)
    if not a.no_draft:
        draft(a.topic, a.dry_run)


if __name__ == "__main__":
    main()
