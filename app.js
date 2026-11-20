const I18N = {
  tr: {
    title: "dogen.es — Yakında Hizmetinizdeyiz",
    phase_tag: "Fase 01 — Yakında",
    seal_role: "Eğitim, Dil Okulu ve Yerleşim Ofisi",
    seal_note: "Yeni dijital platformumuz yayına hazırlanıyor. Mevcut dönem kayıtları ve kurumsal okul iş birlikleri doğrudan yürütülmektedir.",
    headline: "Türkiye’den İspanya’ya eğitim, dil okulu ve yerleşim danışmanlığı.",
    r1_t: "Dil Okulu & Üniversite",
    r1_d: "Instituto Cervantes akreditasyonlu dil okulları, UNEDasiss ve Endülüs DUA devlet üniversitesi başvuruları.",
    r2_t: "Vize & İlk 30 Gün Varış",
    r2_d: "Konsolosluk dosya hazırlığı, konaklama, empadronamiento, NIE/TIE ve banka kurulumu.",
    r3_t: "Kurumsal Okul Partnerliği",
    r3_d: "İspanya’daki eğitim kurumları için Türkçe aday yönetimi ve resmi faturalı iş birliği.",
    c1_lbl: "Öğrenci & Aday Başvuruları",
    c2_lbl: "Okul & Kurumsal İş Birliği",
    c3_lbl: "Doğrudan Hat / WhatsApp",
    c4_lbl: "Yönetim & Resmi Künye"
  },
  es: {
    title: "dogen.es — Muy pronto",
    phase_tag: "Fase 01 — Muy pronto",
    seal_role: "Oficina de Estudios y Relocalización",
    seal_note: "Nuestra nueva plataforma web está en preparación. Las matriculaciones actuales y las alianzas corporativas con centros siguen operativas de forma directa.",
    headline: "Consultoría educativa y de relocalización entre Turquía y España.",
    r1_t: "Escuelas de Español y Universidad",
    r1_d: "Centros acreditados por el Instituto Cervantes, acceso universitario vía UNEDasiss y preinscripción DUA en Andalucía.",
    r2_t: "Visado y Aterrizaje (30 Días)",
    r2_d: "Preparación documental consular, alojamiento, empadronamiento, citas NIE/TIE y apertura bancaria.",
    r3_t: "Alianza Corporativa con Escuelas",
    r3_d: "Gestión integral en turco de candidatos internacionales y colaboración formal con facturación oficial.",
    c1_lbl: "Estudiantes y Candidatos",
    c2_lbl: "Escuelas y Alianzas",
    c3_lbl: "Teléfono Directo / WhatsApp",
    c4_lbl: "Dirección y Titularidad"
  }
};

document.querySelectorAll(".lang-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    const lang = btn.dataset.lang;
    const dict = I18N[lang];
    if (!dict) return;
    document.documentElement.lang = lang;
    document.title = dict.title;
    document.querySelectorAll(".lang-btn").forEach((b) => b.classList.toggle("is-active", b === btn));
    document.querySelectorAll("[data-i18n]").forEach((el) => {
      const key = el.dataset.i18n;
      if (dict[key]) {
        el.textContent = dict[key];
      }
    });
  });
});
