# -*- coding: utf-8 -*-
"""dogen iç sayfa içerikleri (TR + ES).

Kurallar (bkz. BRAND.md):
- Marka sesi "dogen" / "biz". Kişi adı pazarlama metninde geçmez; yasal sorumlu yalnızca /yasal/ sayfasında.
- Uydurma rakam, ofis, ekip, öğrenci yorumu yok. "Garanti", "%100" yok.
- Gerçek öğrenci deneyimleri yalnızca content/testimonials.json içinde yazılı izinle (consent: true) yer alır.
"""

WA = "https://wa.me/34666104496"
MAIL = "info@dogen.es"

# Sayfa anahtarı → (TR yolu, ES yolu)
PATHS = {
    "home": ("/", "/es/"),
    "services": ("/hizmetler/", "/es/servicios/"),
    "process": ("/surec/", "/es/proceso/"),
    "about": ("/hakkimizda/", "/es/quienes-somos/"),
    "experiences": ("/deneyimler/", "/es/experiencias/"),
    "contact": ("/iletisim/", "/es/contacto/"),
    "legal": ("/yasal/", "/es/aviso-legal/"),
    "blog": ("/blog/", "/blog/"),
}


def path(key, lang):
    return PATHS[key][0 if lang == "tr" else 1]


# ------------------------------------------------------------------ arayüz metinleri
UI = {
    "tr": dict(
        menu="Menü", menu_open="Menüyü aç", menu_close="Menüyü kapat", skip="İçeriğe geç",
        home="Ana sayfa", services="Hizmetler", process="Süreç", about="Hakkımızda",
        experiences="Öğrenci deneyimleri", contact="İletişim", blog="Blog", legal="Yasal bilgi",
        faq="Sık sorulan sorular",
        col1="dogen’i tanıyın", col2="Yola hazırlık", col3="Rehberden",
        all_services="Tüm hizmetler", all_posts="Tüm yazılar",
        strip="Hedefinizi yazın, rotayı birlikte çizelim.", wa="WhatsApp’tan yazın",
        lang_label="Dil / Idioma", other_lang="Español", other_code="ES", this_code="TR",
        crumbs="Konum", foot_menu="Alt menü", main_menu="Ana menü",
        foot_about="Sevilla merkezli eğitim ve yerleşim danışmanlığı. Türkiye’den İspanya’ya okumaya gelenlerle birebir çalışıyoruz.",
        foot_pages="Sayfalar", foot_guides="Rehber", foot_contact="İletişim",
        legal_line="dogen bağımsız bir eğitim ve yerleşim danışmanlığıdır. Vize ve oturum başvurularını aday şahsen yapar; nihai karar yetkili İspanyol makamlarına aittir.",
        min_read="dk", more="Ayrıntılar",
        cta_h="Kendi yol haritanızı birlikte çıkaralım.",
        cta_p="Hedefinizi, takviminizi ve elinizdeki belgeleri kısaca yazın; Sevilla’dan Türkçe olarak dönelim.",
        example="Örnek senaryo", example_note="Örnek senaryolar, en sık karşılaştığımız yolları anlatır; gerçek kişileri değil.",
        xp_empty_h="Öğrencilerimizin sözleri",
        xp_card_h="İlk sözler yolda",
        xp_empty_p="Öğrencilerimizin kendi anlattıkları deneyimler, yazılı izinleriyle burada yer alacak. Uydurma yorum yayımlamıyoruz.",
        xp_share="Bizimle yol aldıysanız deneyiminizi paylaşın",
        xp_all="Tüm deneyimler", wa_msg_page="Merhaba, dogen sitesindeki “%s” sayfasından yazıyorum.",
        row_cta="Bu yol için yazın", wa_msg_svc="Merhaba, %s hakkında bilgi almak istiyorum.",
        contact_more="Tüm iletişim seçenekleri", close="Kapat",
        more_services="Hizmetlerin ayrıntıları", more_process="Süreci adım adım görün", more_about="dogen’i yakından tanıyın",
        more_faq="Tüm sorular", more_contact="Tüm iletişim seçenekleri",
        home_xp_tag="04 — Öğrenci deneyimleri", home_xp_h="Her yol farklı başlıyor.",
        home_xp_p="Kimi hiç İspanyolca bilmeden, kimi doğrudan üniversite hedefiyle geliyor. Öğrencilerimizin deneyimleri yazılı izinleriyle burada yer alır; aşağıda en sık karşılaştığımız üç yol var.",
        guides_note="",
    ),
    "es": dict(
        menu="Menú", menu_open="Abrir menú", menu_close="Cerrar menú", skip="Saltar al contenido",
        home="Inicio", services="Servicios", process="Proceso", about="Quiénes somos",
        experiences="Experiencias", contact="Contacto", blog="Blog (en turco)", legal="Aviso legal",
        faq="Preguntas frecuentes",
        col1="Conoce dogen", col2="Prepara tu camino", col3="De la guía",
        all_services="Todos los servicios", all_posts="Todas las guías",
        strip="Cuéntanos tu objetivo y trazamos la ruta juntos.", wa="Escríbenos por WhatsApp",
        lang_label="Idioma / Dil", other_lang="Türkçe", other_code="TR", this_code="ES",
        crumbs="Ubicación", foot_menu="Menú inferior", main_menu="Menú principal",
        foot_about="Consultoría educativa y de relocalización con sede en Sevilla. Acompañamos de forma individual a quienes vienen de Turquía a estudiar en España.",
        foot_pages="Páginas", foot_guides="Guías", foot_contact="Contacto",
        legal_line="dogen es una consultoría educativa y de relocalización independiente. Las solicitudes de visado y residencia las presenta personalmente el interesado; su resolución corresponde a las autoridades españolas.",
        min_read="min", more="Detalles",
        cta_h="Tracemos juntos tu hoja de ruta.",
        cta_p="Escríbenos brevemente tu objetivo, tu calendario y los documentos que tienes; te respondemos desde Sevilla.",
        example="Escenario de ejemplo", example_note="Los escenarios de ejemplo describen los caminos más habituales; no son personas reales.",
        xp_empty_h="En palabras de nuestros estudiantes",
        xp_card_h="Las primeras palabras, en camino",
        xp_empty_p="Aquí publicaremos las experiencias contadas por nuestros propios estudiantes, siempre con su autorización por escrito. No publicamos opiniones inventadas.",
        xp_share="¿Has hecho el camino con nosotros? Comparte tu experiencia",
        xp_all="Todas las experiencias", wa_msg_page="Hola, os escribo desde la página «%s» de dogen.",
        row_cta="Escríbenos sobre esta ruta", wa_msg_svc="Hola, me gustaría recibir información sobre: %s.",
        contact_more="Todas las opciones de contacto", close="Cerrar",
        more_services="Detalles de los servicios", more_process="Ver el proceso paso a paso", more_about="Conoce dogen más de cerca",
        more_faq="Todas las preguntas", more_contact="Todas las opciones de contacto",
        home_xp_tag="04 — Experiencias", home_xp_h="Cada camino empieza de forma distinta.",
        home_xp_p="Hay quien llega sin hablar español y quien viene directo a la universidad. Las experiencias de nuestros estudiantes se publican con su autorización por escrito; abajo, las tres rutas que más vemos.",
        guides_note=" (en turco)",
    ),
}

# ------------------------------------------------------------------ hizmetler (menü + sayfa ortak)
SERVICES = {
    "tr": [
        dict(id="dil-okulu", num="01", t="Dil okulu",
             d="Instituto Cervantes akreditasyonlu okullarda, öğrenci vizesi şartlarını karşılayan yoğun İspanyolca programları.",
             fit="İspanyolcası olmayan ya da başlangıç seviyesinde olan, FP veya üniversite öncesi dil temeli kurmak isteyenler.",
             inc=["Seviye tespiti ve hedefe göre program süresi", "Okul seçimi ve kayıt", "Vize için gereken kabul ve ödeme belgeleri", "Konaklama yönlendirmesi"]),
        dict(id="mesleki-egitim", num="02", t="Mesleki eğitim (FP)",
             d="İspanya devlet okullarında ücretsiz, iki yıllık Grado Superior programları ve haftada 30 saate kadar yasal çalışma hakkı.",
             fit="Lise mezunu olup uygulamalı bir meslek eğitimiyle İspanya’da kariyer kurmak isteyenler.",
             inc=["Bölüm ve okul seçimi", "Lise diploması denkliği (homologación) başvurusu", "Junta de Andalucía başvuru takvimi ve tercih listesi", "Kabul sonrası kayıt (matrícula)"]),
        dict(id="universite", num="03", t="Üniversite",
             d="UNEDasiss akreditasyonu ve Endülüs ortak başvuru sistemi DUA üzerinden devlet üniversitelerine başvuru.",
             fit="İspanyol devlet üniversitesinde lisans okumak isteyen lise mezunları.",
             inc=["UNEDasiss kaydı ve belge listesi", "Gerekiyorsa PCE sınav planı", "DUA ön kaydı ve bölüm tercih sırası", "Sonuç ve kayıt takibi"]),
        dict(id="varis-ve-yerlesim", num="04", t="Varış ve yerleşim",
             d="İspanya’daki ilk haftaların resmî işlemleri: hepsi randevulu, hepsi İspanyolca.",
             fit="Kabulü ve vizesi hazır olan, Sevilla’daki ilk ayını sorunsuz geçirmek isteyenler.",
             inc=["Empadronamiento (adres kaydı)", "FNMT dijital sertifikası", "NIE / TIE randevusu ve parmak izi", "Banka, telefon ve ulaşım kartı için yönlendirme"]),
    ],
    "es": [
        dict(id="dil-okulu", num="01", t="Escuela de español",
             d="Programas intensivos en centros acreditados por el Instituto Cervantes que cumplen los requisitos del visado de estudios.",
             fit="Quien no habla español o tiene un nivel inicial y quiere una base sólida antes de FP o universidad.",
             inc=["Prueba de nivel y duración según el objetivo", "Elección de centro y matrícula", "Documentos de admisión y pago para el visado", "Orientación de alojamiento"]),
        dict(id="mesleki-egitim", num="02", t="Formación Profesional (FP)",
             d="Ciclos de Grado Superior de dos años, gratuitos, en centros públicos españoles con permiso de trabajo de hasta 30 h/semana.",
             fit="Personas con bachillerato que quieren construir una carrera en España con una formación práctica.",
             inc=["Elección de ciclo y centro", "Solicitud de homologación del bachillerato", "Calendario de admisión de la Junta de Andalucía y orden de preferencias", "Matrícula tras la adjudicación"]),
        dict(id="universite", num="03", t="Universidad",
             d="Acreditación UNEDasiss y solicitud a universidades públicas andaluzas a través del Distrito Único Andaluz (DUA).",
             fit="Personas con bachillerato que quieren estudiar un grado en una universidad pública española.",
             inc=["Registro en UNEDasiss y lista de documentos", "Plan de PCE si hace falta", "Preinscripción DUA y orden de preferencias", "Seguimiento de resultados y matrícula"]),
        dict(id="varis-ve-yerlesim", num="04", t="Llegada y asentamiento",
             d="Los trámites de las primeras semanas en España: todos con cita previa, todos en español.",
             fit="Quien ya tiene admisión y visado y quiere un primer mes en Sevilla sin sobresaltos.",
             inc=["Empadronamiento", "Certificado digital FNMT", "Cita de NIE / TIE y huellas", "Orientación para banco, teléfono y transporte"]),
    ],
}

# ------------------------------------------------------------------ süreç
STEPS = {
    "tr": [
        dict(t="Ön görüşme", when="Başlangıçtan 9–12 ay önce idealdir",
             us="Durumunuzu dinler, size uygun rotaları ve gerçekçi takvimi anlatırız.",
             you="Hedefinizi, bütçenizi ve elinizdeki belgeleri paylaşırsınız."),
        dict(t="Rota planı", when="Ön görüşmeden sonraki günler",
             us="Okul ve program seçeneklerini, kapsam ve ücretle birlikte yazılı olarak çıkarırız.",
             you="Rotanızı seçer, planı onaylarsınız."),
        dict(t="Kabul ve evrak", when="Rotaya göre birkaç ay",
             us="Okul kaydını, tercüme, apostil ve denklik listesini sırasıyla yönetiriz.",
             you="Belgeleri Türkiye’de temin eder, bize iletirsiniz."),
        dict(t="Vize", when="Kabul belgesi geldikten sonra",
             us="Konsolosluk dosyasını kontrol eder, randevuyu takvime göre planlarız.",
             you="Başvuruyu yasa gereği şahsen yaparsınız."),
        dict(t="İlk 30 gün", when="Sevilla’ya varıştan itibaren",
             us="Empadronamiento, dijital sertifika ve NIE/TIE işlemlerinde yanınızda oluruz.",
             you="Sevilla’ya gelir, randevulara katılırsınız."),
    ],
    "es": [
        dict(t="Primera consulta", when="Lo ideal: 9–12 meses antes del inicio",
             us="Escuchamos tu situación y te explicamos las rutas posibles y un calendario realista.",
             you="Nos cuentas tu objetivo, tu presupuesto y los documentos que tienes."),
        dict(t="Plan de ruta", when="Los días siguientes a la consulta",
             us="Preparamos por escrito las opciones de centro y programa, con alcance y precio.",
             you="Eliges tu ruta y apruebas el plan."),
        dict(t="Admisión y documentos", when="Unos meses, según la ruta",
             us="Gestionamos en orden la matrícula, traducciones, apostillas y homologaciones.",
             you="Consigues los documentos en Turquía y nos los envías."),
        dict(t="Visado", when="Tras recibir la carta de admisión",
             us="Revisamos el expediente consular y planificamos la cita según el calendario.",
             you="Presentas la solicitud en persona, como exige la ley."),
        dict(t="Primeros 30 días", when="Desde tu llegada a Sevilla",
             us="Te acompañamos en el empadronamiento, el certificado digital y el NIE/TIE.",
             you="Llegas a Sevilla y acudes a las citas."),
    ],
}

TIMELINE = {
    "tr": [
        ("Sonbahar – kış", "Ön görüşme, rota planı ve lise diploması denkliği (homologación) başvurusu. Denklik aylar sürebildiği için erken başlanır."),
        ("Bahar", "Belgelerin apostil ve yeminli tercümesi; gerekiyorsa dil okulu kaydı ve İspanyolca seviyesinin yükseltilmesi."),
        ("Haziran", "Junta de Andalucía FP başvuru dönemi: okul ve bölüm tercihleri sırayla girilir."),
        ("Temmuz", "Yerleştirme listeleri (adjudicación) ve kayıt (matrícula)."),
        ("Temmuz – ağustos", "Kabul belgesiyle öğrenci vizesi dosyası ve konsolosluk randevusu."),
        ("Eylül", "Sevilla’ya varış, derslerin başlaması ve ilk 30 günün resmî işlemleri."),
    ],
    "es": [
        ("Otoño – invierno", "Primera consulta, plan de ruta y solicitud de homologación del bachillerato. Como puede tardar meses, conviene empezar pronto."),
        ("Primavera", "Apostilla y traducción jurada de documentos; si hace falta, matrícula en escuela de español para subir de nivel."),
        ("Junio", "Plazo de solicitud de FP de la Junta de Andalucía: se ordenan centros y ciclos por preferencia."),
        ("Julio", "Listas de adjudicación y matrícula."),
        ("Julio – agosto", "Expediente de visado de estudios con la carta de admisión y cita consular."),
        ("Septiembre", "Llegada a Sevilla, inicio de clases y trámites de los primeros 30 días."),
    ],
}

# ------------------------------------------------------------------ örnek yol haritaları (gerçek kişi değil)
EXAMPLES = {
    "tr": [
        dict(who="Lise mezunu, İspanyolcası yok", goal="Hedef: devlet FP’si",
             path=["Dil okulu · 1 yıl", "Denklik", "FP başvurusu · Haziran", "Grado Superior · Eylül"],
             note="İlk yıl öğrenci vizesiyle dil okulu; bu sürede denklik tamamlanır, Haziran’da FP başvurusu yapılır."),
        dict(who="Lise mezunu, İspanyolcası iyi", goal="Hedef: devlet üniversitesi",
             path=["UNEDasiss", "PCE (gerekirse)", "DUA ön kaydı", "Üniversite · Eylül"],
             note="Akreditasyon ve sınav takvimi önceden planlanır; tercih sırası bölüm kontenjanlarına göre kurulur."),
        dict(who="Önce İspanya’yı tanımak isteyen", goal="Hedef: yoğun dil programı",
             path=["Seviye tespiti", "Okul ve kayıt", "Öğrenci vizesi", "Sevilla · ilk 30 gün"],
             note="90 günü aşan yoğun bir dil programıyla başlanır; sonraki adım İspanya’da birlikte değerlendirilir."),
    ],
    "es": [
        dict(who="Bachillerato terminado, sin español", goal="Objetivo: FP pública",
             path=["Escuela de español · 1 año", "Homologación", "Solicitud FP · junio", "Grado Superior · septiembre"],
             note="El primer año, escuela de español con visado de estudios; mientras tanto se completa la homologación y en junio se solicita la FP."),
        dict(who="Bachillerato terminado, buen español", goal="Objetivo: universidad pública",
             path=["UNEDasiss", "PCE (si hace falta)", "Preinscripción DUA", "Universidad · septiembre"],
             note="Acreditación y exámenes se planifican con antelación; el orden de preferencias se ajusta a las plazas de cada grado."),
        dict(who="Quiere conocer España primero", goal="Objetivo: programa intensivo de español",
             path=["Prueba de nivel", "Centro y matrícula", "Visado de estudios", "Sevilla · primeros 30 días"],
             note="Se empieza con un programa intensivo de más de 90 días; el siguiente paso se valora juntos ya en España."),
    ],
}

FAQ = {
    "tr": [
        ("İspanyolcam yok, yine de başlayabilir miyim?", "Evet. Rotaların çoğu bir dil okulu dönemiyle başlar; seviyenize ve hedefinize göre okul ve program öneririz."),
        ("Vize başvurusunu siz mi yapıyorsunuz?", "Hayır. Başvuruyu yasa gereği siz şahsen yaparsınız. Biz dosyanın eksiksiz ve doğru hazırlanmasını, randevu ve takvim planlamasını üstleniriz. Nihai karar yetkili İspanyol makamlarına aittir."),
        ("Ücret nasıl belirleniyor?", "Seçtiğiniz rotaya ve hizmetin kapsamına göre. Ön görüşmeden sonra yazılı olarak paylaşırız."),
        ("Türkiye’deyken görüşebilir miyiz?", "Elbette. Ön görüşmeyi WhatsApp’tan ya da görüntülü yapıyoruz; Sevilla’ya geldiğinizde yüz yüze de buluşabiliriz."),
        ("Kabul ya da vize garantisi veriyor musunuz?", "Hayır. Kabul kararını okullar, vize ve oturum kararını İspanyol makamları verir. Bizim işimiz dosyanızı doğru, eksiksiz ve zamanında hazırlamak."),
        ("Sadece bir adım için destek alabilir miyim?", "Evet. Örneğin yalnızca denklik başvurusu ya da yalnızca varış sonrası işlemler için de çalışabiliriz; kapsam ön görüşmede netleşir."),
    ],
    "es": [
        ("No hablo español, ¿puedo empezar igualmente?", "Sí. La mayoría de las rutas empiezan con un periodo en una escuela de español; te recomendamos centro y programa según tu nivel y tu objetivo."),
        ("¿Presentáis vosotros la solicitud de visado?", "No. La presentas tú personalmente, como exige la ley. Nosotros nos encargamos de que el expediente esté completo y correcto, y de planificar citas y plazos. La decisión final corresponde a las autoridades españolas."),
        ("¿Cómo se determina el precio?", "Según la ruta y el alcance del servicio. Te lo enviamos por escrito después de la primera consulta."),
        ("¿Podemos hablar mientras sigo en Turquía?", "Claro. La primera consulta la hacemos por WhatsApp o videollamada; cuando llegues a Sevilla también podemos vernos en persona."),
        ("¿Garantizáis la admisión o el visado?", "No. La admisión la deciden los centros, y el visado y la residencia, las autoridades españolas. Nuestro trabajo es que tu expediente esté correcto, completo y a tiempo."),
        ("¿Puedo contratar solo un paso?", "Sí. Por ejemplo, solo la homologación o solo los trámites tras la llegada; el alcance se concreta en la primera consulta."),
    ],
}

# ------------------------------------------------------------------ sayfalar
PAGES = {
    "services": {
        "tr": dict(
            title="Hizmetler: dil okulu, FP, üniversite ve yerleşim · Sevilla | dogen",
            desc="dogen hizmetleri: İspanyolca dil okulu, ücretsiz devlet meslek eğitimi (FP), devlet üniversitesi başvurusu ve Sevilla’da varış ve yerleşim işlemleri. Türkçe, birebir.",
            kicker="Hizmetler", h1="Dört rota, tek bir takvim.",
            lead="Çoğu öğrenci bir dil okulu dönemiyle başlayıp FP’ye ya da üniversiteye geçer. Bu yüzden okul, evrak ve varış adımlarını baştan tek bir planda kuruyoruz.",
            fit_label="Kimin için", inc_label="Neler dahil",
            partners_h="Okullar ve kurumlar için",
            partners_p="İspanya’daki dil akademileri ve eğitim kurumlarıyla yazılı ve resmî faturalı iş birliği yapıyoruz. Adayları Türkçe olarak ön değerlendirmeden geçiriyor, başvuru dosyalarını eksiksiz hazırlayıp takip ediyoruz.",
            partners_list="Anlaşmalı kurumlar", partner_desc="İspanyolca dil okulu · Sevilla",
            scope_h="Ne yapıyoruz, ne yapmıyoruz",
            do=["Size uygun rotayı ve takvimi yazılı olarak çıkarırız", "Okul kaydını ve evrak sırasını yönetiriz", "Vize dosyasını başvurudan önce kontrol ederiz", "Sevilla’daki ilk resmî işlemlerde yanınızda oluruz"],
            dont=["Kabul ya da vize garantisi vermeyiz", "Vize başvurusunu sizin adınıza yapmayız", "Hazır paket satmayız", "Resmî harçları gizli kalemlerle fiyatlamayız"],
        ),
        "es": dict(
            title="Servicios: escuela de español, FP, universidad y llegada · Sevilla | dogen",
            desc="Servicios de dogen: escuela de español, Formación Profesional pública y gratuita, acceso a la universidad pública y trámites de llegada en Sevilla. Acompañamiento individual.",
            kicker="Servicios", h1="Cuatro rutas, un solo calendario.",
            lead="La mayoría empieza con un periodo de español y después pasa a FP o a la universidad. Por eso planificamos centro, documentación y llegada en un único plan desde el principio.",
            fit_label="Para quién", inc_label="Qué incluye",
            partners_h="Para escuelas y centros",
            partners_p="Colaboramos por escrito y con facturación oficial con academias de idiomas y centros educativos en España. Hacemos una evaluación previa de los candidatos en turco y preparamos y seguimos expedientes completos.",
            partners_list="Centros colaboradores", partner_desc="Escuela de español · Sevilla",
            scope_h="Qué hacemos y qué no",
            do=["Preparamos por escrito tu ruta y tu calendario", "Gestionamos la matrícula y el orden documental", "Revisamos el expediente de visado antes de presentarlo", "Te acompañamos en los primeros trámites en Sevilla"],
            dont=["No garantizamos admisión ni visado", "No presentamos el visado en tu nombre", "No vendemos paquetes estándar", "No escondemos tasas oficiales en el precio"],
        ),
    },
    "process": {
        "tr": dict(
            title="Süreç: ön görüşmeden Sevilla’daki ilk 30 güne | dogen",
            desc="dogen ile İspanya’da eğitim süreci adım adım: ön görüşme, rota planı, kabul ve evrak, öğrenci vizesi ve Sevilla’daki ilk 30 gün. Kimin neyi yaptığı baştan belli.",
            kicker="Süreç", h1="Kimin neyi, ne zaman yaptığı baştan belli.",
            lead="Vize başvurusunu yasa gereği siz şahsen yaparsınız; dosyanın eksiksiz ve zamanında hazır olması bizim işimiz. Süreç beş adımda ilerler.",
            us="Biz", you="Siz", when="Zamanlama",
            steps_h="Beş adımda süreç", steps_p="Her adımda neyi bizim, neyi sizin yaptığınızı baştan yazılı olarak netleştiriyoruz.",
            tl_h="Örnek takvim: Eylül’de FP’ye başlamak",
            tl_p="Andalucía’da devlet FP’sine başlamak isteyen bir öğrenci için tipik yıl. Tarihler her yıl resmî takvimle teyit edilir.",
        ),
        "es": dict(
            title="Proceso: de la primera consulta a los primeros 30 días en Sevilla | dogen",
            desc="El proceso con dogen paso a paso: primera consulta, plan de ruta, admisión y documentos, visado de estudios y primeros 30 días en Sevilla. Desde el principio, quién hace qué.",
            kicker="Proceso", h1="Desde el principio: quién hace qué, y cuándo.",
            lead="La solicitud de visado la presentas tú personalmente, como exige la ley; que el expediente esté completo y a tiempo es cosa nuestra. El proceso avanza en cinco pasos.",
            us="Nosotros", you="Tú", when="Cuándo",
            steps_h="El proceso en cinco pasos", steps_p="En cada paso dejamos claro por escrito qué hacemos nosotros y qué haces tú.",
            tl_h="Calendario de ejemplo: empezar FP en septiembre",
            tl_p="Un año típico para quien quiere empezar FP pública en Andalucía. Las fechas se confirman cada año con el calendario oficial.",
        ),
    },
    "about": {
        "tr": dict(
            title="Hakkımızda: Sevilla merkezli eğitim ve yerleşim danışmanlığı | dogen",
            desc="dogen, Türkiye’den İspanya’ya okumaya gelmek isteyenlerle Sevilla’dan birebir çalışan bağımsız bir eğitim ve yerleşim danışmanlığıdır.",
            kicker="Hakkımızda", h1="Sevilla’dan, yolu baştan doğru çizmek için.",
            lead="dogen, Sevilla merkezli bağımsız bir eğitim ve yerleşim danışmanlığı. Türkiye’den İspanya’ya okumaya gelmek isteyenlerle birebir çalışıyoruz; hazır paket satmıyor, her dosyaya kendi koşullarıyla bakıyoruz.",
            story_h="Neden varız",
            story=["İspanya’da her şey randevu, belge ve takvimle ilerliyor. Bir eksik evrak ya da kaçırılan bir tarih aylarca gecikme demek. Türkiye’den gelen öğrenciler için bu sistem bir de dil ve uzaklıkla zorlaşıyor.",
                   "dogen bu boşluğu kapatmak için var: süreci İspanya’da, yerinde ve Türkçe yürütüyoruz. İşimizin büyük kısmı sessiz ve titiz: doğru belge, doğru sırada, zamanında."],
            values_h="Nasıl çalışıyoruz",
            values=[("Birebir", "Her dosya kendi koşullarıyla ele alınır; hazır paket yok."),
                    ("Yerinde", "Sevilla’dan, Endülüs’teki kurum ve takvimleri yakından izleyerek."),
                    ("Açık", "Kapsam ve ücret yazılı; kimin neyi yaptığı baştan belli."),
                    ("Gerçekçi", "Garanti vaat etmeyiz; resmî takvime uygun, ulaşılabilir planlar kurarız.")],
            why_h="Neden Sevilla",
            why=["Endülüs’ün başkenti Sevilla, devlet FP programları, köklü üniversiteleri ve çok sayıda akredite dil okuluyla öğrenci için güçlü bir başlangıç noktası.",
                 "Bu şehirde yaşıyor ve çalışıyoruz; okulları, semtleri ve resmî daireleri yerinden tanıyoruz."],
            name_h="İsim nereden geliyor",
            name_p="Japoncada “dō” yol demek. dogen de tam olarak bunu yapıyor: yolu baştan doğru çizmek.",
        ),
        "es": dict(
            title="Quiénes somos: consultoría educativa y de relocalización en Sevilla | dogen",
            desc="dogen es una consultoría educativa y de relocalización independiente con sede en Sevilla que acompaña de forma individual a quienes vienen de Turquía a estudiar en España.",
            kicker="Quiénes somos", h1="Desde Sevilla, para trazar bien el camino desde el principio.",
            lead="dogen es una consultoría educativa y de relocalización independiente con sede en Sevilla. Trabajamos de forma individual con personas de Turquía que quieren venir a estudiar a España; no vendemos paquetes, miramos cada expediente con sus propias circunstancias.",
            story_h="Por qué existimos",
            story=["En España todo avanza con citas, documentos y plazos. Un papel que falta o una fecha perdida pueden suponer meses de retraso. Para quien viene de Turquía, el idioma y la distancia lo complican aún más.",
                   "dogen existe para cerrar esa brecha: llevamos el proceso desde España, sobre el terreno y en turco. Gran parte de nuestro trabajo es discreto y minucioso: el documento correcto, en el orden correcto, a tiempo."],
            values_h="Cómo trabajamos",
            values=[("Individual", "Cada expediente con sus circunstancias; sin paquetes estándar."),
                    ("Sobre el terreno", "Desde Sevilla, siguiendo de cerca a las instituciones y plazos andaluces."),
                    ("Transparente", "Alcance y precio por escrito; desde el principio, quién hace qué."),
                    ("Realista", "No prometemos garantías; planes alcanzables y alineados con el calendario oficial.")],
            why_h="Por qué Sevilla",
            why=["Sevilla, capital de Andalucía, es un gran punto de partida para estudiar: FP pública, universidades con tradición y muchas escuelas de español acreditadas.",
                 "Vivimos y trabajamos aquí; conocemos de primera mano los centros, los barrios y las oficinas públicas."],
            name_h="De dónde viene el nombre",
            name_p="En japonés «dō» significa camino. Eso es exactamente lo que hace dogen: trazar bien el camino desde el principio.",
        ),
    },
    "experiences": {
        "tr": dict(
            title="Öğrenci deneyimleri ve örnek yol haritaları | dogen",
            desc="dogen ile İspanya’ya okumaya gelen öğrencilerin deneyimleri ve en sık karşılaştığımız yol haritaları: dil okulu, devlet FP’si ve üniversite.",
            kicker="Öğrenci deneyimleri", h1="Her yol farklı başlıyor.",
            lead="Kimi hiç İspanyolca bilmeden, kimi doğrudan üniversite hedefiyle geliyor. Burada öğrencilerimizin deneyimlerini ve en sık karşılaştığımız yol haritalarını paylaşıyoruz.",
            ex_h="Örnek yol haritaları",
        ),
        "es": dict(
            title="Experiencias de estudiantes y rutas de ejemplo | dogen",
            desc="Experiencias de estudiantes que han venido a estudiar a España con dogen y las rutas más habituales: escuela de español, FP pública y universidad.",
            kicker="Experiencias", h1="Cada camino empieza de forma distinta.",
            lead="Hay quien llega sin hablar español y quien viene directo a la universidad. Aquí compartimos las experiencias de nuestros estudiantes y las rutas que más vemos.",
            ex_h="Rutas de ejemplo",
        ),
    },
    "contact": {
        "tr": dict(
            title="İletişim: WhatsApp ve e-posta ile Sevilla’dan yanıt | dogen",
            desc="dogen ile iletişim: WhatsApp +34 666 104 496, info@dogen.es. Hedefinizi ve takviminizi yazın; Sevilla’dan Türkçe olarak dönelim.",
            kicker="İletişim", h1="Hedefinizi yazın, rotayı birlikte çizelim.",
            lead="Türkçe ya da İspanyolca yazabilirsiniz. Ön görüşmeyi WhatsApp’tan ya da görüntülü yapıyoruz; Sevilla’ya geldiğinizde yüz yüze de buluşabiliriz.",
            ch_h="Kanallar", wa_l="Telefon ve WhatsApp", mail_l="E-posta", org_l="Okullar ve kurumlar", org_v="İş birliği için e-postayla yazın", city_l="Konum", time_l="Sevilla’da saat",
            first_h="İlk mesajınızda bunları yazarsanız daha hızlı ilerleriz",
            first=["Hedefiniz: dil okulu, FP, üniversite ya da yalnızca yerleşim", "Ne zaman başlamak istediğiniz", "Son mezun olduğunuz okul ve not ortalamanız", "Şu anki İspanyolca seviyeniz", "Elinizde hazır olan belgeler (pasaport, diploma, transkript)"],
            wa_prefill="Merhaba, İspanya’da okumak istiyorum. Hedefim: … / Başlamak istediğim dönem: … / İspanyolca seviyem: …",
            wa_btn="Hazır mesajla WhatsApp’ı aç",
        ),
        "es": dict(
            title="Contacto: WhatsApp y correo, respuesta desde Sevilla | dogen",
            desc="Contacta con dogen: WhatsApp +34 666 104 496, info@dogen.es. Cuéntanos tu objetivo y tu calendario y te respondemos desde Sevilla.",
            kicker="Contacto", h1="Cuéntanos tu objetivo y trazamos la ruta.",
            lead="Puedes escribir en turco o en español. La primera consulta la hacemos por WhatsApp o videollamada; cuando llegues a Sevilla también podemos vernos en persona.",
            ch_h="Canales", wa_l="Teléfono y WhatsApp", mail_l="Correo", org_l="Escuelas y centros", org_v="Escríbenos por correo para colaborar", city_l="Ubicación", time_l="Hora en Sevilla",
            first_h="Si en tu primer mensaje nos cuentas esto, avanzamos más rápido",
            first=["Tu objetivo: escuela de español, FP, universidad o solo llegada", "Cuándo quieres empezar", "Último centro en el que estudiaste y tu nota media", "Tu nivel actual de español", "Documentos que ya tienes (pasaporte, título, expediente)"],
            wa_prefill="Hola, quiero estudiar en España. Mi objetivo: … / Quiero empezar en: … / Mi nivel de español: …",
            wa_btn="Abrir WhatsApp con mensaje",
        ),
    },
    "legal": {
        "tr": dict(
            title="Yasal bilgi ve gizlilik | dogen",
            desc="dogen.es sitesinin yasal bilgileri (Aviso legal, LSSI-CE) ve gizlilik açıklaması.",
            kicker="Yasal bilgi", h1="Yasal bilgi ve gizlilik",
            lead="İspanya Bilgi Toplumu Hizmetleri Kanunu (LSSI-CE, Ley 34/2002) ve Avrupa Genel Veri Koruma Tüzüğü (GDPR / RGPD) kapsamındaki bilgiler.",
        ),
        "es": dict(
            title="Aviso legal y privacidad | dogen",
            desc="Aviso legal (LSSI-CE) y política de privacidad del sitio dogen.es.",
            kicker="Aviso legal", h1="Aviso legal y privacidad",
            lead="Información exigida por la Ley 34/2002 de servicios de la sociedad de la información (LSSI-CE) y el Reglamento General de Protección de Datos (RGPD).",
        ),
    },
}

# Yasal sorumlu (LSSI-CE md. 10). NIF ve tam adres Fırat'tan gelince doldurulacak.
LEGAL_OWNER = dict(name="Fırat Daşdöğen", nif="", address="Sevilla, España", email=MAIL, phone="+34 666 104 496")

LEGAL_HTML = {
    "tr": """<h2>1. Site sahibi</h2>
<p>Bu internet sitesi (<strong>dogen.es</strong>) ve “dogen” markası altında sunulan danışmanlık hizmetinin sorumlusu:</p>
<ul>
<li><strong>Sorumlu kişi:</strong> {name}</li>
{nif_li}<li><strong>Adres:</strong> {address}</li>
<li><strong>E-posta:</strong> <a href="mailto:{email}">{email}</a></li>
<li><strong>Telefon / WhatsApp:</strong> {phone}</li>
</ul>
<h2>2. Hizmetin niteliği</h2>
<p>dogen bağımsız bir eğitim ve yerleşim danışmanlığıdır; herhangi bir kamu kurumunu, konsolosluğu ya da okulu temsil etmez. Vize ve oturum başvurularını aday şahsen yapar; nihai karar yetkili İspanyol makamlarına, kabul kararı ise ilgili eğitim kurumlarına aittir. Sitedeki içerikler genel bilgilendirme amaçlıdır ve hukuki görüş yerine geçmez.</p>
<h2>3. Fikrî mülkiyet</h2>
<p>Sitedeki metinler, logo ve görsel tasarım dogen’e aittir. Kaynak gösterilerek kısa alıntı yapılabilir; izinsiz çoğaltılamaz.</p>
<h2>4. Kişisel veriler</h2>
<p>Sitede form, üyelik ya da reklam/analitik çerezi bulunmaz. WhatsApp ya da e-postayla bize yazdığınızda paylaştığınız bilgiler yalnızca talebinizi yanıtlamak ve size sunulan hizmeti yürütmek için kullanılır; üçüncü kişilere satılmaz. Okul ya da resmî başvuru için bir belgenin iletilmesi gerektiğinde bu, yalnızca sizin onayınızla yapılır.</p>
<p>Verilerinize erişme, düzeltme, silme, itiraz ve taşınabilirlik haklarınızı <a href="mailto:{email}">{email}</a> adresine yazarak kullanabilirsiniz. İspanya Veri Koruma Kurumu’na (<a href="https://www.aepd.es/" rel="noopener" target="_blank">AEPD</a>) şikâyette bulunma hakkınız saklıdır.</p>
<h2>5. Çerezler ve üçüncü taraflar</h2>
<p>Site çerez kullanmaz. Tercih ettiğiniz dil yalnızca tarayıcınızda (localStorage) saklanır ve size geri gönderilmez. Yazı tipleri Google Fonts üzerinden yüklenir; bu sırada tarayıcınız Google sunucularına bağlanır. Site GitHub Pages üzerinde barındırılır.</p>
<h2>6. Uygulanacak hukuk</h2>
<p>Bu site ve hizmetlerle ilgili ilişkilerde İspanya hukuku uygulanır.</p>""",
    "es": """<h2>1. Titular del sitio</h2>
<p>En cumplimiento del artículo 10 de la LSSI-CE, se informa de que el titular de este sitio web (<strong>dogen.es</strong>) y responsable del servicio de consultoría ofrecido bajo la marca «dogen» es:</p>
<ul>
<li><strong>Titular:</strong> {name}</li>
{nif_li}<li><strong>Domicilio:</strong> {address}</li>
<li><strong>Correo electrónico:</strong> <a href="mailto:{email}">{email}</a></li>
<li><strong>Teléfono / WhatsApp:</strong> {phone}</li>
</ul>
<h2>2. Naturaleza del servicio</h2>
<p>dogen es una consultoría educativa y de relocalización independiente; no representa a ningún organismo público, consulado ni centro educativo. Las solicitudes de visado y residencia las presenta personalmente el interesado; su resolución corresponde a las autoridades españolas y la admisión, a cada centro. Los contenidos del sitio son informativos y no constituyen asesoramiento jurídico.</p>
<h2>3. Propiedad intelectual</h2>
<p>Los textos, el logotipo y el diseño del sitio pertenecen a dogen. Se permiten citas breves indicando la fuente; queda prohibida su reproducción sin autorización.</p>
<h2>4. Protección de datos</h2>
<p>El sitio no tiene formularios, registros ni cookies publicitarias o analíticas. Los datos que nos facilitas al escribirnos por WhatsApp o correo se usan únicamente para responder a tu consulta y prestar el servicio solicitado; no se ceden ni se venden a terceros. Si hay que enviar un documento a un centro o a una administración, se hace solo con tu consentimiento.</p>
<p>Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición y portabilidad escribiendo a <a href="mailto:{email}">{email}</a>. También puedes reclamar ante la Agencia Española de Protección de Datos (<a href="https://www.aepd.es/" rel="noopener" target="_blank">AEPD</a>).</p>
<h2>5. Cookies y terceros</h2>
<p>El sitio no utiliza cookies. El idioma que eliges se guarda solo en tu navegador (localStorage) y no se nos envía. Las tipografías se cargan desde Google Fonts, por lo que tu navegador se conecta a servidores de Google. El sitio está alojado en GitHub Pages.</p>
<h2>6. Legislación aplicable</h2>
<p>Las relaciones derivadas de este sitio y de los servicios se rigen por la legislación española.</p>""",
}
