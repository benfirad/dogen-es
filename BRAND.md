# dogen.es — Marka sistemi v3.1 "Cal & Azulejo · Akıcı Katmanlar"

Logo (`logo.svg`, kaligrafik "dogen") **değişmez**. Her zaman tek renk (`--tinta` `#16181D` veya koyu/kobalt yüzeyde `--cal` `#F6F4EF`), yanında küçük italik `.es`.

## Renk
| Ad | Hex | Kullanım |
|---|---|---|
| Cal (kireç badana) | `#F6F4EF` | Ana zemin |
| Cal-2 (sıcak taş) | `#EEEAE1` | İkincil kart yüzeyi |
| Papel | `#FFFFFF` | Öne çıkan temiz kart yüzeyi |
| Tinta | `#16181D` | Ana metin, logo, koyu kapanış kartı |
| Pizarra | `#555B64` | İkincil metin |
| Azulejo (kobalt) | `#1F4A7A` | Ana vurgu, vurgu sahne kartı, perde hover, butonlar, linkler |
| Albero (avlu toprağı) | `#C58B2B` | Çizgi/rota noktası vurgusu · metinde `#8A5A12` · koyu zeminde `#E2B764` |
| Línea | `#D9D3C7` | İnce mimari ayırıcı çizgiler |

## Tipografi (tam Türkçe/İspanyolca `latin-ext`)
- Tek aile: **Instrument Sans** (`400..700`, normal ve italik — `ğ, ş, ı, İ, ö, ü, ç` tam destekli)
- Başlık: Instrument Sans 600–700, `-0.03em`, satır yüksekliği `1.06–1.15`
- Gövde/arayüz: Instrument Sans 400/500/600, `tabular-nums` sayı hizası

## Akış ve Geçiş Dili (`redmono.com/es` mimarisiyle uyumlu)
- **Çevik akıcı kaydırma (Lenis):** `lerp: 0.16, duration: 0.9, smoothTouch: false` — sünger gibi süzülmeyen, çevik ve pürüzsüz tekerlek akışı; çekmece/modal içinde `data-lenis-prevent`.
- **Üst üste kayan bölüm kartları (Sticky Card Stack):** Bölümler `border-radius: 28px 28px 0 0` ve hafif üst gölgeyle bir öncekinin üzerine kayar; altta kalan kart kendi zemin rengiyle (`--cv` örtüsü) yumuşakça sadeleşir, uzun bölümler `top = Math.min(0, vh - offsetHeight)` ile son satırına kadar okunur.
- **İlerleme ve bölüm göstergesi:** Üst kenarda `3px` ilerleme çizgisi, geniş ekranda sol kenarda dikey bölüm kapsülü (`01 · Hizmetler` vb.).
- **Rota çizimleri ("dō = yol"):** Kart ve süreç satırlarında `stroke-dashoffset` ile kendi kendini çizen mimari rota/kemer şemaları ve üzerinde ilerleyen albero odak noktası.
- **Perde hover & satır odağı:** Hizmet kartlarında aşağıdan yukarıya kobalt perde (`translateY(101% → 0)`), süreç satırlarında kaydırmayla aktifleşen odak çubuğu (`cubic-bezier(0.16, 1, 0.3, 1)`).
- **Erişilebilirlik:** `prefers-reduced-motion: reduce` açıkken tüm hareketli dönüşümler devre dışı kalır; dokunmatik cihazlarda hover efektleri `@media (hover: hover)` ile korunur.

## Ses ve Bilgi Mimarisi
- Sakin, net, söz vermeyen. "Garanti", "%100" yok; vize kararı her zaman İspanyol makamlarındadır.
- Müşteri rehberlerinde **önce büyük resim** (görsel rota şeması, karar ağacı, harcanan vs kanıt parası ayrımı), **sonra taranabilir kontrol listesi** ve tıklanabilir terim sözlüğü gelir.
